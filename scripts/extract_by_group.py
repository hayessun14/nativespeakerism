#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_by_group.py
===================
Per-group concordance extraction.  Each of the twelve keyword groups is
searched ONLY in its own target corpus, and each group gets its own TSV.

Differences from extract_concordances.py
----------------------------------------
* input is a group spec (group / target_corpus / comma-separated words)
  rather than a flat word x corpus list;
* one output file per group, written even when the group has no hits
  (header row only), so the twelve files always exist;
* merge labels may expand to MULTI-TOKEN sequences.  This matters for
  RUN-ON: the AntConc corpora were built with token_definition [\\p{L}]+,
  which drops hyphens, so "run-on" can only ever appear in the token
  stream as the bigram run + on (or run + ons).  Such hits are matched as
  n-grams and flagged "(split)" in match_form.

Matching is whole-token and case-insensitive: a token matches only when
its full surface form equals the query form, so `use` never matches
`because` and `sentence` never matches `sentences`.

Context window: 10 tokens left / 10 tokens right of the node, taken from
the same document and clipped at document boundaries.

Usage
-----
    python3 scripts/extract_by_group.py --dry-run
    python3 scripts/extract_by_group.py --groups group03
    python3 scripts/extract_by_group.py                 # all twelve

Only the Python standard library is used.
"""

from __future__ import annotations

import argparse
import collections
import csv
import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from extract_concordances import (          # noqa: E402  (path set above)
    CORPORA,
    REF,
    REPO,
    WINDOW,
    corpus_diagnostics,
    fetch_corpus,
    is_merge_label,
    load_token_stream,
    open_corpus,
)

OUT_COLUMNS = ["query_word", "match_form", "corpus",
               "doc_id", "token_pos", "left", "node", "right"]


# --------------------------------------------------------------------------
# Config
# --------------------------------------------------------------------------

def read_group_spec(path):
    """Read group / target_corpus / words into an ordered list of dicts."""
    groups = []
    seen = set()
    with open(path, encoding="utf-8-sig", newline="") as fh:
        rows = [ln for ln in fh
                if ln.strip() and not ln.lstrip().startswith("#")]
    reader = csv.DictReader(rows, delimiter="\t")
    required = {"group", "target_corpus", "words"}
    if required - set(reader.fieldnames or []):
        sys.exit(f"ERROR: {path} needs columns {sorted(required)}, "
                 f"found {reader.fieldnames}")
    for lineno, row in enumerate(reader, start=2):
        name = row["group"].strip()
        corpus = row["target_corpus"].strip()
        words = [w.strip() for w in row["words"].split(",") if w.strip()]
        if corpus not in CORPORA:
            sys.exit(f"ERROR: {path}:{lineno}: unknown corpus {corpus!r}")
        if not words:
            sys.exit(f"ERROR: {path}:{lineno}: group {name} has no words")
        if name in seen:
            sys.exit(f"ERROR: {path}:{lineno}: duplicate group {name!r}")
        seen.add(name)
        # keep the spec order but drop an accidental repeat within a group
        deduped = list(dict.fromkeys(words))
        groups.append({"group": name, "corpus": corpus, "words": deduped})
    return groups


def read_merge_map(path):
    """Read LABEL -> [member forms]; a form may contain spaces (an n-gram)."""
    mapping = {}
    with open(path, encoding="utf-8-sig") as fh:
        for lineno, line in enumerate(fh, start=1):
            line = line.rstrip("\n").rstrip("\r")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 2:
                sys.exit(f"ERROR: {path}:{lineno}: expected 'LABEL<TAB>forms'")
            forms = [f.strip() for f in parts[1].split(",") if f.strip()]
            if not forms:
                sys.exit(f"ERROR: {path}:{lineno}: no forms for {parts[0]!r}")
            mapping[parts[0].strip()] = forms
    return mapping


def expand(word, merge_map):
    """Return the list of surface forms to search for one query word.

    A plain word searches for itself.  A merge label searches for every
    member form listed in the map.
    """
    if not is_merge_label(word):
        return [word]
    if word not in merge_map:
        sys.exit(f"ERROR: {word!r} is a merge label with no entry in the "
                 f"merge map. Add one before running.")
    return list(merge_map[word])


def as_token_seq(form):
    """Split a search form into the tokens the corpus indexer would produce.

    token_definition [\\p{L}]+ keeps runs of letters only, so 'run-on'
    becomes ('run', 'on') and any hyphenated form is inherently a
    multi-token search.  Returns (tokens, was_split).
    """
    tokens = []
    current = []
    for ch in form:
        if ch.isalpha():
            current.append(ch)
        elif current:
            tokens.append("".join(current))
            current = []
    if current:
        tokens.append("".join(current))
    tokens = [t.lower() for t in tokens]
    return tuple(tokens), len(tokens) > 1


# --------------------------------------------------------------------------
# Extraction
# --------------------------------------------------------------------------

def build_targets(forms):
    """Map each distinct token sequence to whether it came from a split form.

    Two spellings can collapse onto the same token sequence -- 'run-on' and
    'run on' both index as ('run','on') -- so the sequence is the key and
    the flag records that it is a multi-token match.
    """
    targets = {}
    for form in forms:
        seq, _ = as_token_seq(form)
        if not seq:
            continue
        targets.setdefault(seq, len(seq) > 1)
    # longest first so a 2-token match wins over a 1-token prefix
    return sorted(targets.items(), key=lambda kv: -len(kv[0]))


def concordance(forms_by_doc, lower_by_doc, ids_by_doc, targets, window):
    """Yield one hit dict per match, document by document."""
    for doc_id in sorted(forms_by_doc):
        surfaces = forms_by_doc[doc_id]
        lowers = lower_by_doc[doc_id]
        tok_ids = ids_by_doc[doc_id]
        n = len(lowers)
        i = 0
        while i < n:
            for seq, is_split in targets:
                k = len(seq)
                if i + k <= n and tuple(lowers[i:i + k]) == seq:
                    node = " ".join(surfaces[i:i + k])
                    yield {
                        "doc_id": doc_id,
                        "match_form": node + (" (split)" if is_split else ""),
                        "token_pos": tok_ids[i],
                        "left": " ".join(surfaces[max(0, i - window):i]),
                        "node": node,
                        "right": " ".join(surfaces[i + k:i + k + window]),
                    }
                    i += k - 1          # skip past a multi-token node
                    break
            i += 1


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Per-group KWIC extraction from the AntConc corpora.")
    ap.add_argument("--spec", default="data/groups_spec.tsv")
    ap.add_argument("--merge-map", default="data/merged_map_groups.tsv")
    ap.add_argument("--out-dir", default="out/groups")
    ap.add_argument("--cache-dir", default="corpora")
    ap.add_argument("--window", type=int, default=WINDOW)
    ap.add_argument("--groups", default=None,
                    help="comma-separated subset, e.g. group03,group07")
    ap.add_argument("--repo", default=REPO)
    ap.add_argument("--ref", default=REF)
    ap.add_argument("--force-download", action="store_true")
    ap.add_argument("--inspect", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    groups = read_group_spec(args.spec)
    merge_map = read_merge_map(args.merge_map)

    if args.groups:
        wanted = {g.strip() for g in args.groups.split(",")}
        unknown = wanted - {g["group"] for g in groups}
        if unknown:
            sys.exit(f"ERROR: unknown group(s): {sorted(unknown)}")
        groups = [g for g in groups if g["group"] in wanted]

    # resolve every query word up front so a bad label fails before download
    for g in groups:
        g["expanded"] = {w: expand(w, merge_map) for w in g["words"]}

    print(f"Spec        {args.spec}", file=sys.stderr)
    print(f"Groups      {len(groups)}", file=sys.stderr)
    print(f"Corpora     {', '.join(sorted({g['corpus'] for g in groups}))}",
          file=sys.stderr)
    print(f"Window      +/-{args.window} tokens", file=sys.stderr)
    print(f"Output      {args.out_dir}/", file=sys.stderr)
    for g in groups:
        labels = [w for w in g["words"] if is_merge_label(w)]
        extra = f"  (labels: {', '.join(labels)})" if labels else ""
        print(f"    {g['group']}  target={g['corpus']:9s} "
              f"{len(g['words']):2d} words{extra}", file=sys.stderr)
    if args.dry_run:
        print("\n--dry-run: nothing downloaded, nothing extracted.",
              file=sys.stderr)
        return 0

    os.makedirs(args.out_dir, exist_ok=True)

    print("\nFetching corpora...", file=sys.stderr)
    needed = sorted({g["corpus"] for g in groups})
    paths = {c: fetch_corpus(c, args.cache_dir, args.repo, args.ref,
                             force=args.force_download) for c in needed}

    # one pass per corpus: load its token stream once, serve every group
    streams = {}
    for corpus in needed:
        print(f"\n[{corpus}] loading token stream...", file=sys.stderr)
        con = open_corpus(paths[corpus])
        if args.inspect:
            print(corpus_diagnostics(con, corpus), file=sys.stderr)
        streams[corpus] = load_token_stream(con)
        con.close()
        surfaces = streams[corpus][0]
        print(f"[{corpus}] {len(surfaces)} docs, "
              f"{sum(len(v) for v in surfaces.values()):,} tokens",
              file=sys.stderr)

    stats = collections.OrderedDict()
    written = []

    for g in groups:
        name, corpus = g["group"], g["corpus"]
        surfaces, lowers, tok_ids = streams[corpus]
        path = os.path.join(args.out_dir, f"concordance_{name}.tsv")
        per_word = collections.OrderedDict()
        per_form = collections.defaultdict(collections.Counter)
        total = 0

        print(f"\n[{name}] target={corpus}", file=sys.stderr)
        with open(path, "w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=OUT_COLUMNS, delimiter="\t",
                                    lineterminator="\n",
                                    quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()
            for word in g["words"]:
                targets = build_targets(g["expanded"][word])
                hits = 0
                for hit in concordance(surfaces, lowers, tok_ids,
                                       targets, args.window):
                    writer.writerow({
                        "query_word": word,
                        "match_form": hit["match_form"],
                        "corpus": corpus,
                        "doc_id": hit["doc_id"],
                        "token_pos": hit["token_pos"],
                        "left": hit["left"],
                        "node": hit["node"],
                        "right": hit["right"],
                    })
                    per_form[word][hit["match_form"]] += 1
                    hits += 1
                per_word[word] = hits
                total += hits
                note = ""
                if is_merge_label(word):
                    note = "  [" + " | ".join(g["expanded"][word]) + "]"
                print(f"    {word:<18s} {hits:6d}{note}", file=sys.stderr)

        written.append(path)
        stats[name] = {"corpus": corpus, "words": g["words"],
                       "per_word": per_word, "per_form": per_form,
                       "total": total, "path": path,
                       "expanded": g["expanded"]}
        print(f"    {'TOTAL':<18s} {total:6d}  -> {path}", file=sys.stderr)

    write_log(args, groups, stats, os.path.join(args.out_dir,
                                                "extraction_log.md"))
    print(f"\nWrote {len(written)} group files + extraction_log.md "
          f"to {args.out_dir}/", file=sys.stderr)
    return 0


# --------------------------------------------------------------------------
# Log
# --------------------------------------------------------------------------

def write_log(args, groups, stats, path):
    zero = [(n, w) for n, s in stats.items()
            for w, c in s["per_word"].items() if c == 0]
    lines = [
        "# Concordance 提取日志",
        "",
        f"生成时间：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## 参数",
        "",
        "| 项 | 值 |",
        "|---|---|",
        f"| 组规格 | `{args.spec}` |",
        f"| 归并映射 | `{args.merge_map}` |",
        f"| KWIC 窗口 | 左右各 {args.window} 词 |",
        f"| 匹配方式 | 整词（whole-token），不区分大小写 |",
        f"| 语料来源 | `{args.repo}` @ `{args.ref}` |",
        f"| 输出目录 | `{args.out_dir}/` |",
        "",
        "语料 tokenizer 为 `[\\p{L}]+`（仅保留字母序列），连字符不进入 token。"
        "因此 `run-on` / `run-ons` 在语料中只能以 bigram `run on` / `run ons` 出现，"
        "脚本按 n-gram 检索，命中在 `match_form` 中标注 `(split)`。",
        "",
        "## 各组汇总",
        "",
        "| 组 | target corpus | 检索词数 | 总命中数 | 文件 |",
        "|---|---|---:|---:|---|",
    ]
    for name, s in stats.items():
        lines.append(f"| {name} | {s['corpus']} | {len(s['words'])} | "
                     f"{s['total']} | `{os.path.basename(s['path'])}` |")
    grand = sum(s["total"] for s in stats.values())
    lines += [f"| **合计** | — | — | **{grand}** | — |", "",
              "## 每个「词形 × 组」的命中数", ""]

    for name, s in stats.items():
        lines += [f"### {name}（target = {s['corpus']}，共 {s['total']} 行）", "",
                  "| 检索词 | 展开词形 | 命中数 | 各词形分项 |",
                  "|---|---|---:|---|"]
        for word, count in s["per_word"].items():
            forms = s["expanded"][word]
            forms_cell = " + ".join(forms) if is_merge_label(word) else "—"
            if s["per_form"][word]:
                breakdown = ", ".join(
                    f"`{f}` {c}" for f, c
                    in sorted(s["per_form"][word].items(),
                              key=lambda kv: -kv[1]))
            else:
                breakdown = "—"
            flag = " **(0)**" if count == 0 else ""
            lines.append(f"| {word}{flag} | {forms_cell} | {count} | "
                         f"{breakdown} |")
        lines.append("")

    lines += ["## 零命中词形", ""]
    if zero:
        lines += ["| 组 | 检索词 | target corpus |", "|---|---|---|"]
        lines += [f"| {n} | {w} | {stats[n]['corpus']} |" for n, w in zero]
    else:
        lines.append("无。所有检索词在其 target corpus 中均有命中。")
    lines += ["", "## 文件生成清单", "",
              "| 文件 | 存在 | 数据行数 |", "|---|---|---:|"]
    for name, s in stats.items():
        exists = os.path.exists(s["path"])
        with open(s["path"], encoding="utf-8") as fh:
            n_rows = max(0, sum(1 for _ in fh) - 1)
        lines.append(f"| `{os.path.basename(s['path'])}` | "
                     f"{'是' if exists else '否'} | {n_rows} |")
    n_files = len(stats)
    lines += ["",
              f"共 {n_files} 个组文件"
              f"{'（全部生成）' if n_files == len(groups) else ''}，"
              "另有本日志 `extraction_log.md`。"
              "无命中的组仍会生成仅含列标题的文件。", ""]

    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


if __name__ == "__main__":
    sys.exit(main())
