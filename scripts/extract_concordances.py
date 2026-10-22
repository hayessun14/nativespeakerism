#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_concordances.py
=======================
Pull AntConc 4.x corpus databases (*.db) from GitHub and extract every
concordance line (KWIC, 10 words left / 10 words right) for each
"word form x target corpus" pair listed in a TSV wordlist.

Corpus format
-------------
The .db files are AntConc 4.x SQLite corpora.  Relevant tables:

    corpus(id, doc_id, doc_token_id, doc_lex_token_id,
           type_id, type, type_lc, type_ws, pos, headword)
    lexicon(type_id, type, type_lc, pos, headword, freq, range, range_lc)
    docs(doc_id, doc_file_name, type_count, token_count,
         corpus_id_from, corpus_id_to)
    doc_metadata(doc_id, filename, auto_category)
    corpus_info(full_name, short_name, file_count, token_count,
                type_count, token_definition, ...)

Matching
--------
Whole-word only.  A token matches when its surface form equals the query
form exactly, compared case-insensitively (`corpus.type_lc == word.lower()`).
No stemming, no substring matching, no regex.

Context window
--------------
+/- 10 tokens taken from the retained token stream of the SAME document,
ordered by doc_token_id.  Windows are clipped at document boundaries; they
never cross into a neighbouring document.

Merged (uppercase) labels
-------------------------
The wordlist contains R4 merge labels written in uppercase (USE, INFLUENCE,
...).  These are word families, not surface forms.  Supply their member
forms via --merged-map (TSV: LABEL <tab> form1,form2,...), e.g.

    USE     use,uses,used,using
    ARTICLE article,articles

Without a mapping the label is matched literally (i.e. `USE` -> `use`
only) and every affected row is flagged in the output column
`merge_expanded` as `NO(unmapped)`.  Use --on-unmapped-merge=error to make
that a hard failure instead.  --write-merge-stub writes a ready-to-fill
stub of all labels found.

Usage
-----
    # 0. see what the script would do, no download, no extraction
    python3 scripts/extract_concordances.py --wordlist LIST.tsv --dry-run

    # 1. download the corpora only (resumable, cached, checksum-verified)
    python3 scripts/extract_concordances.py --wordlist LIST.tsv --fetch-only

    # 2. trial run: 3 pairs, 5 lines each, print corpus diagnostics
    python3 scripts/extract_concordances.py --wordlist LIST.tsv \
        --max-pairs 3 --max-lines-per-pair 5 --inspect

    # 3. full run
    python3 scripts/extract_concordances.py --wordlist LIST.tsv \
        --merged-map merged_map.tsv --out out/concordances.tsv

Only the Python standard library is used.
"""

from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import os
import sqlite3
import sys
import tempfile
import time
import urllib.error
import urllib.request

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

REPO = "hayessun14/nativespeakerism"
REF = "claude/keen-brahmagupta-kkr013"          # branch holding the .db files
RAW = "https://raw.githubusercontent.com/{repo}/{ref}/{name}"

CORPORA = ["L1", "Generic", "Chinese", "German", "Baseline"]

WINDOW = 10                                     # tokens each side
RETRIES = 4                                     # network retries
BACKOFF = [2, 4, 8, 16]                         # seconds

OUT_COLUMNS = [
    "query_word",       # form exactly as written in the wordlist
    "match_form",       # surface form actually found in the corpus
    "corpus",           # L1 / Generic / Chinese / German / Baseline
    "groups",           # keyword-list group ids that requested this pair
    "layers",           # coding layers that requested this pair
    "merge_expanded",   # YES / NO / NO(unmapped)
    "doc_id",
    "filename",
    "token_pos",        # doc_token_id of the node
    "left",             # 10 tokens, space-joined
    "node",
    "right",            # 10 tokens, space-joined
]


# --------------------------------------------------------------------------
# Wordlist
# --------------------------------------------------------------------------

def read_wordlist(path):
    """Read the wordlist TSV and collapse it to unique (word, corpus) pairs.

    Returns an ordered dict keyed by (word, corpus) -> {"groups": [...],
    "layers": [...]}, so a pair requested by several groups is extracted
    once and carries all requesting group ids.
    """
    with open(path, encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        missing = {"word", "target_corpus"} - set(reader.fieldnames or [])
        if missing:
            sys.exit(f"ERROR: wordlist is missing column(s): {sorted(missing)}\n"
                     f"       found: {reader.fieldnames}")
        pairs = collections.OrderedDict()
        for lineno, row in enumerate(reader, start=2):
            word = (row.get("word") or "").strip()
            corpus = (row.get("target_corpus") or "").strip()
            if not word or not corpus:
                print(f"WARN  line {lineno}: blank word or target_corpus, skipped",
                      file=sys.stderr)
                continue
            if corpus not in CORPORA:
                sys.exit(f"ERROR: line {lineno}: unknown target_corpus {corpus!r}. "
                         f"Expected one of {CORPORA}")
            entry = pairs.setdefault((word, corpus), {"groups": [], "layers": []})
            grp = (row.get("group") or "").strip()
            lay = (row.get("layer") or "").strip()
            if grp and grp not in entry["groups"]:
                entry["groups"].append(grp)
            if lay and lay not in entry["layers"]:
                entry["layers"].append(lay)
    return pairs


def read_merged_map(path):
    """Read LABEL<tab>form1,form2,... into {label: [forms]}."""
    mapping = {}
    with open(path, encoding="utf-8-sig", newline="") as fh:
        for lineno, line in enumerate(fh, start=1):
            line = line.rstrip("\n").rstrip("\r")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 2:
                sys.exit(f"ERROR: {path}:{lineno}: expected 'LABEL<TAB>forms'")
            label = parts[0].strip()
            forms = [f.strip() for f in parts[1].replace(";", ",").split(",")
                     if f.strip()]
            if not forms:
                sys.exit(f"ERROR: {path}:{lineno}: no member forms for {label!r}")
            mapping[label] = forms
    return mapping


def is_merge_label(word):
    """A merge label is an all-uppercase multi-letter token (USE, RUN-ON)."""
    letters = [c for c in word if c.isalpha()]
    return bool(letters) and all(c.isupper() for c in letters) and len(letters) > 1


def expand(word, merged_map, on_unmapped):
    """Return (forms, merge_expanded_flag) for one query word."""
    if not is_merge_label(word):
        return [word], "NO"
    if word in merged_map:
        return list(merged_map[word]), "YES"
    if on_unmapped == "error":
        sys.exit(f"ERROR: {word!r} looks like an R4 merge label but has no entry "
                 f"in --merged-map. Supply one, or pass "
                 f"--on-unmapped-merge=literal to match it literally.")
    return [word], "NO(unmapped)"


# --------------------------------------------------------------------------
# Download
# --------------------------------------------------------------------------

def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def fetch_corpus(name, cache_dir, repo, ref, force=False):
    """Download <name>.db into cache_dir unless already cached. Returns path."""
    fname = f"{name}.db"
    dest = os.path.join(cache_dir, fname)
    if os.path.exists(dest) and not force:
        if is_sqlite(dest):
            print(f"      cached  {fname}  ({os.path.getsize(dest):,} bytes)",
                  file=sys.stderr)
            return dest
        print(f"WARN  cached {fname} is not a valid SQLite file, re-downloading",
              file=sys.stderr)

    url = RAW.format(repo=repo, ref=ref, name=fname)
    os.makedirs(cache_dir, exist_ok=True)
    last_err = None
    for attempt in range(RETRIES + 1):
        try:
            print(f"      GET     {url}", file=sys.stderr)
            tmp_fd, tmp = tempfile.mkstemp(dir=cache_dir, suffix=".part")
            os.close(tmp_fd)
            with urllib.request.urlopen(url, timeout=120) as resp, \
                    open(tmp, "wb") as out:
                total = resp.headers.get("Content-Length")
                total = int(total) if total else None
                got = 0
                while True:
                    chunk = resp.read(1 << 20)
                    if not chunk:
                        break
                    out.write(chunk)
                    got += len(chunk)
                    if total:
                        pct = 100.0 * got / total
                        print(f"\r      {fname}: {got:,}/{total:,} "
                              f"({pct:5.1f}%)", end="", file=sys.stderr)
                print("", file=sys.stderr)
            if total is not None and got != total:
                raise IOError(f"truncated transfer: {got} of {total} bytes")
            if not is_sqlite(tmp):
                raise IOError("downloaded file is not a SQLite database "
                              "(wrong ref? Git-LFS pointer? 404 page?)")
            os.replace(tmp, dest)
            print(f"      ok      {fname}  sha256={sha256_of(dest)[:16]}...",
                  file=sys.stderr)
            return dest
        except (urllib.error.URLError, IOError, TimeoutError) as exc:
            last_err = exc
            try:
                os.unlink(tmp)
            except OSError:
                pass
            if attempt < RETRIES:
                wait = BACKOFF[min(attempt, len(BACKOFF) - 1)]
                print(f"WARN  {fname}: {exc} - retrying in {wait}s "
                      f"({attempt + 1}/{RETRIES})", file=sys.stderr)
                time.sleep(wait)
    sys.exit(f"ERROR: could not download {fname}: {last_err}")


def is_sqlite(path):
    try:
        with open(path, "rb") as fh:
            return fh.read(16) == b"SQLite format 3\x00"
    except OSError:
        return False


# --------------------------------------------------------------------------
# Corpus access
# --------------------------------------------------------------------------

def open_corpus(path):
    con = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    return con


def corpus_diagnostics(con, name):
    """Print the corpus_info row so the trial run can confirm tokenisation."""
    lines = [f"--- {name} ---"]
    try:
        row = con.execute("SELECT * FROM corpus_info LIMIT 1").fetchone()
        for key in ("full_name", "file_count", "token_count", "type_count",
                    "encoding", "token_definition", "indexer", "db_version"):
            if row is not None and key in row.keys():
                lines.append(f"    {key:18s} {row[key]}")
    except sqlite3.Error as exc:
        lines.append(f"    corpus_info unreadable: {exc}")
    try:
        n_docs = con.execute("SELECT COUNT(*) FROM docs").fetchone()[0]
        n_tok = con.execute("SELECT COUNT(*) FROM corpus").fetchone()[0]
        lines.append(f"    docs (actual)      {n_docs}")
        lines.append(f"    corpus rows        {n_tok}")
    except sqlite3.Error as exc:
        lines.append(f"    count failed: {exc}")
    return "\n".join(lines)


def load_filenames(con):
    """doc_id -> filename, preferring doc_metadata, falling back to docs."""
    names = {}
    for table, col in (("docs", "doc_file_name"), ("doc_metadata", "filename")):
        try:
            for row in con.execute(f"SELECT doc_id, {col} FROM {table}"):
                if row[1]:
                    names[row[0]] = row[1]
        except sqlite3.Error:
            continue
    return names


def load_token_stream(con):
    """Load the whole corpus into memory as doc_id -> (forms, token_ids).

    ~270k tokens per corpus, so this is a few tens of MB and lets every
    query for that corpus run against plain Python lists.  `forms` holds
    the surface form, `token_ids` the AntConc doc_token_id, both ordered
    by doc_token_id within the document.
    """
    forms = collections.defaultdict(list)
    token_ids = collections.defaultdict(list)
    lowers = collections.defaultdict(list)
    sql = ("SELECT doc_id, doc_token_id, type, type_lc "
           "FROM corpus ORDER BY doc_id, doc_token_id")
    for doc_id, tok_id, surface, surface_lc in con.execute(sql):
        surface = surface if surface is not None else ""
        forms[doc_id].append(surface)
        lowers[doc_id].append(surface_lc if surface_lc is not None
                              else surface.lower())
        token_ids[doc_id].append(tok_id)
    return forms, lowers, token_ids


def concordance(forms, lowers, token_ids, targets, window=WINDOW):
    """Yield one dict per hit. `targets` is a set of lowercase surface forms."""
    for doc_id in sorted(forms):
        doc_forms = forms[doc_id]
        doc_lower = lowers[doc_id]
        doc_ids = token_ids[doc_id]
        for i, low in enumerate(doc_lower):
            if low not in targets:
                continue
            left = doc_forms[max(0, i - window):i]
            right = doc_forms[i + 1:i + 1 + window]
            yield {
                "doc_id": doc_id,
                "match_form": doc_forms[i],
                "token_pos": doc_ids[i],
                "left": " ".join(left),
                "node": doc_forms[i],
                "right": " ".join(right),
            }


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Extract KWIC concordances from AntConc 4 corpora on GitHub.",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--wordlist", required=True,
                    help="TSV with columns word / layer / group / target_corpus")
    ap.add_argument("--out", default="out/concordances.tsv",
                    help="output TSV path (default: out/concordances.tsv)")
    ap.add_argument("--cache-dir", default="corpora",
                    help="where the .db files are cached (default: corpora/)")
    ap.add_argument("--merged-map", default=None,
                    help="TSV mapping uppercase merge labels to member forms")
    ap.add_argument("--on-unmapped-merge", choices=("literal", "error"),
                    default="literal",
                    help="what to do with an unmapped uppercase label "
                         "(default: literal, flagged in the output)")
    ap.add_argument("--write-merge-stub", metavar="PATH", default=None,
                    help="write a fill-in stub of every merge label found, "
                         "then exit")
    ap.add_argument("--window", type=int, default=WINDOW,
                    help="context tokens per side (default: 10)")
    ap.add_argument("--ref", default=REF, help=f"git ref (default: {REF})")
    ap.add_argument("--repo", default=REPO, help=f"repo (default: {REPO})")
    ap.add_argument("--corpora", default=None,
                    help="comma-separated subset of corpora to process")
    ap.add_argument("--max-pairs", type=int, default=None,
                    help="TRIAL: process only the first N word x corpus pairs")
    ap.add_argument("--max-lines-per-pair", type=int, default=None,
                    help="TRIAL: keep only the first N concordance lines per pair")
    ap.add_argument("--dry-run", action="store_true",
                    help="report the plan, download nothing, extract nothing")
    ap.add_argument("--fetch-only", action="store_true",
                    help="download the corpora and stop")
    ap.add_argument("--force-download", action="store_true",
                    help="re-download even if cached")
    ap.add_argument("--inspect", action="store_true",
                    help="print corpus_info diagnostics for each corpus")
    args = ap.parse_args(argv)

    # ---- wordlist -------------------------------------------------------
    pairs = read_wordlist(args.wordlist)
    merged_map = read_merged_map(args.merged_map) if args.merged_map else {}

    labels = sorted({w for (w, _c) in pairs if is_merge_label(w)})
    if args.write_merge_stub:
        with open(args.write_merge_stub, "w", encoding="utf-8") as fh:
            fh.write("# LABEL<TAB>form1,form2,...  (from keyword_ALL_merged_labels.md)\n")
            for lab in labels:
                fh.write(f"{lab}\t{merged_map.get(lab, [''])[0] if lab in merged_map else ''}\n")
        print(f"Wrote merge-label stub with {len(labels)} labels to "
              f"{args.write_merge_stub}", file=sys.stderr)
        return 0

    unmapped = [l for l in labels if l not in merged_map]
    if unmapped:
        print("WARN  uppercase merge labels with no --merged-map entry "
              f"({len(unmapped)}): {', '.join(unmapped)}", file=sys.stderr)
        print("WARN  they will be matched literally and flagged "
              "'NO(unmapped)' in the output.", file=sys.stderr)

    wanted = ([c.strip() for c in args.corpora.split(",")]
              if args.corpora else CORPORA)
    selected = [(w, c) for (w, c) in pairs if c in wanted]
    if args.max_pairs:
        selected = selected[:args.max_pairs]
    by_corpus = collections.OrderedDict()
    for w, c in selected:
        by_corpus.setdefault(c, []).append(w)

    # ---- plan -----------------------------------------------------------
    print(f"Wordlist        {args.wordlist}", file=sys.stderr)
    print(f"Unique pairs    {len(pairs)} total, {len(selected)} selected",
          file=sys.stderr)
    print(f"Unique words    {len({w for w, _ in selected})}", file=sys.stderr)
    print(f"Merge labels    {len(labels)} ({len(labels) - len(unmapped)} mapped)",
          file=sys.stderr)
    print(f"Corpora         {', '.join(by_corpus)}", file=sys.stderr)
    print(f"Window          +/-{args.window} tokens", file=sys.stderr)
    print(f"Output          {args.out}", file=sys.stderr)
    for c, ws in by_corpus.items():
        print(f"    {c:9s} {len(ws):4d} pairs", file=sys.stderr)
    if args.dry_run:
        print("\n--dry-run: nothing downloaded, nothing extracted.",
              file=sys.stderr)
        return 0

    # ---- download -------------------------------------------------------
    print("\nFetching corpora...", file=sys.stderr)
    paths = {c: fetch_corpus(c, args.cache_dir, args.repo, args.ref,
                             force=args.force_download)
             for c in by_corpus}
    if args.fetch_only:
        print("--fetch-only: corpora cached, stopping.", file=sys.stderr)
        return 0

    # ---- extract --------------------------------------------------------
    out_dir = os.path.dirname(os.path.abspath(args.out))
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    totals = collections.OrderedDict()
    zero_hits = []
    n_rows = 0

    with open(args.out, "w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=OUT_COLUMNS, delimiter="\t",
                                lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()

        for corpus_name, words in by_corpus.items():
            print(f"\n[{corpus_name}] loading token stream...", file=sys.stderr)
            con = open_corpus(paths[corpus_name])
            if args.inspect:
                print(corpus_diagnostics(con, corpus_name), file=sys.stderr)
            filenames = load_filenames(con)
            forms, lowers, token_ids = load_token_stream(con)
            con.close()
            n_tok = sum(len(v) for v in forms.values())
            print(f"[{corpus_name}] {len(forms)} docs, {n_tok:,} tokens",
                  file=sys.stderr)

            for word in words:
                variants, flag = expand(word, merged_map, args.on_unmapped_merge)
                targets = {v.lower() for v in variants}
                meta = pairs[(word, corpus_name)]
                hits = 0
                for hit in concordance(forms, lowers, token_ids, targets,
                                       window=args.window):
                    if (args.max_lines_per_pair
                            and hits >= args.max_lines_per_pair):
                        break
                    writer.writerow({
                        "query_word": word,
                        "match_form": hit["match_form"],
                        "corpus": corpus_name,
                        "groups": ",".join(meta["groups"]),
                        "layers": ";".join(meta["layers"]),
                        "merge_expanded": flag,
                        "doc_id": hit["doc_id"],
                        "filename": filenames.get(hit["doc_id"], ""),
                        "token_pos": hit["token_pos"],
                        "left": hit["left"],
                        "node": hit["node"],
                        "right": hit["right"],
                    })
                    hits += 1
                    n_rows += 1
                totals[(word, corpus_name)] = hits
                if hits == 0:
                    zero_hits.append((word, corpus_name))
                print(f"    {word:<18s} {corpus_name:<9s} {hits:6d} lines"
                      + (f"  [{'|'.join(variants)}]" if flag == "YES" else ""),
                      file=sys.stderr)

    # ---- summary --------------------------------------------------------
    print(f"\nWrote {n_rows:,} concordance lines to {args.out}", file=sys.stderr)
    if zero_hits:
        print(f"\nWARN  {len(zero_hits)} pair(s) returned ZERO hits - check "
              f"spelling, merge expansion, or tokenisation:", file=sys.stderr)
        for w, c in zero_hits:
            print(f"      {w} @ {c}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
