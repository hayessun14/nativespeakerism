#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
merge_by_condition.py
=====================
Merge the 174 feedback texts of each condition x model into one .txt file,
giving 10 files (5 corpora x Claude / GPT), named after AntConc's
auto_category, e.g. Baseline_anthropic.txt, L2_chinese_openai.txt.

Each feedback is preceded by a marker line naming its original file:

    ===== ICLE-US-IND-0001.1.txt =====

The text is taken verbatim from docs_fulltext (original punctuation and
paragraph breaks kept).  Feedbacks are ordered by doc_id, which is the
alphabetical order of the source file names.

After writing, every file is parsed back and checked: 174 markers, the
expected file names, and each block byte-identical to the stored text.

Usage
-----
    python3 scripts/merge_by_condition.py              # all 10 files
    python3 scripts/merge_by_condition.py --out-dir out/merged

Only the Python standard library is used.
"""

from __future__ import annotations

import argparse
import os
import re
import sqlite3
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from extract_concordances import CORPORA, REF, REPO, fetch_corpus  # noqa: E402

MARKER = "===== {name} ====="
MARKER_RE = re.compile(r"^===== (.+?) =====$", re.M)


def load(path):
    """Return {auto_category: [(file_name, full_text), ...]} ordered by doc_id."""
    con = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    rows = con.execute(
        "SELECT d.doc_id, d.doc_file_name, m.auto_category, f.full_text "
        "FROM docs d "
        "JOIN doc_metadata m USING (doc_id) "
        "JOIN docs_fulltext f USING (doc_id) "
        "ORDER BY d.doc_id").fetchall()
    con.close()
    groups = {}
    for _doc_id, name, category, text in rows:
        groups.setdefault(category, []).append((name, text))
    return groups


def render(docs):
    """One marker line, the text with trailing whitespace trimmed, a blank line."""
    parts = []
    for name, text in docs:
        parts.append(MARKER.format(name=name))
        parts.append(text.rstrip())
        parts.append("")
    return "\n".join(parts) + "\n"


def verify(path, docs):
    """Parse the written file back and compare it with the source texts."""
    content = open(path, encoding="utf-8").read()
    marks = list(MARKER_RE.finditer(content))
    if len(marks) != len(docs):
        return f"expected {len(docs)} markers, found {len(marks)}"
    for k, (m, (name, text)) in enumerate(zip(marks, docs)):
        if m.group(1) != name:
            return f"block {k + 1}: marker {m.group(1)!r} != {name!r}"
        end = marks[k + 1].start() if k + 1 < len(marks) else len(content)
        body = content[m.end():end].strip("\n")
        if body != text.rstrip():
            return f"block {k + 1} ({name}): text differs from source"
    return None


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--out-dir", default="out/merged")
    ap.add_argument("--cache-dir", default="corpora")
    ap.add_argument("--repo", default=REPO)
    ap.add_argument("--ref", default=REF)
    args = ap.parse_args(argv)

    os.makedirs(args.out_dir, exist_ok=True)
    written = []
    for corpus in CORPORA:
        path = fetch_corpus(corpus, args.cache_dir, args.repo, args.ref)
        for category, docs in sorted(load(path).items()):
            # the marker must never occur inside a feedback, or parsing breaks
            for name, text in docs:
                if MARKER_RE.search(text):
                    sys.exit(f"ERROR: marker pattern found inside {category}/{name}")
            out = os.path.join(args.out_dir, f"{category}.txt")
            with open(out, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(render(docs))
            problem = verify(out, docs)
            if problem:
                sys.exit(f"ERROR: {out}: {problem}")
            names = [n for n, _ in docs]
            written.append((corpus, category, out, len(docs), len(set(names)),
                            os.path.getsize(out)))
            print(f"  {category:24s} {len(docs):4d} feedbacks  "
                  f"{os.path.getsize(out):>9,d} bytes  verified", file=sys.stderr)

    print(f"\nWrote {len(written)} files to {args.out_dir}/", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
