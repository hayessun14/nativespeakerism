#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 concordance 回填后的总表拆回十二个分组编码文件。

回填后的总表由外部流程从原始基线重跑得到，其 note 以
  〔concordance回填：<层>=<标签>；主导判定=<原始判定串>〕
记录每一次落位。本脚本据此派生 src 列，逐层记录哪些层由 concordance 定夺：
  src = "d1"、"act"、"d1+act"、"-" …

之所以另起一列而不复用 conf：conf 是编码者对标签的信度评级（H/M/L），
与"该标签的依据是不是查了索引行"是两件事。上一版把二者挤进同一列，
凡回填即写 conf=C，40 个原有 H/M/L 评级因此被覆盖；分列后两者都不丢，
且 src 精确到层——同一行里哪几层查过、哪几层是原判，一目了然。
"""
import csv, re, sys
from pathlib import Path

SRC = sys.argv[1] if len(sys.argv) > 1 else "coding/all_codes_concordance_backfilled.tsv"
OUT_FIELDS = ["type", "d1", "d1sub", "act", "hedge", "c", "conf", "src", "note"]
EXPECTED = {1: 128, 2: 131, 3: 37, 4: 30, 5: 56, 6: 59,
            7: 77, 8: 65, 9: 131, 10: 121, 11: 30, 12: 26}
# 回填标注里的层名 → 列名
LAYER = {"维度一": "d1", "act 层": "act", "hedge 层": "hedge",
         "维度三": "c", "C1子类": "c"}
MARK = re.compile(r"〔concordance回填：(.*?)〕")

rows = list(csv.DictReader(open(SRC, encoding="utf-8-sig", newline=""), delimiter="\t"))
for r in rows:
    for k in list(r):
        if isinstance(r.get(k), str):
            r[k] = r[k].replace("\r", "")
assert len(rows) == 891, f"总表 {len(rows)} 行，应为 891"

unknown = set()
for r in rows:
    layers = []
    for m in MARK.findall(r["note"]):
        name = m.split("；")[0].split("=")[0].strip()
        col = LAYER.get(name)
        if col is None:
            unknown.add(name)
        elif col not in layers:
            layers.append(col)
    # 固定列序输出，便于跨行比对
    r["src"] = "+".join([L for L in ("d1", "act", "hedge", "c") if L in layers]) or "-"
assert not unknown, f"note 中出现未知的回填层名: {unknown}"

for g in range(1, 13):
    rs = [r for r in rows if int(r["group"]) == g]
    assert len(rs) == EXPECTED[g], f"组 {g} 有 {len(rs)} 行，应为 {EXPECTED[g]}"
    fp = Path(f"coding/group{g:02d}_codes.tsv")
    with open(fp, "w", encoding="utf-8", newline="\n") as f:
        f.write("\t".join(OUT_FIELDS) + "\n")
        for r in rs:
            f.write("\t".join(r[k] for k in OUT_FIELDS) + "\n")
    print(f"写出 {fp}：{len(rs)} 行")

n_src = sum(1 for r in rows if r["src"] != "-")
from collections import Counter
print(f"\nconcordance 定夺：{n_src} 行 / {891} 行")
print("按层组合：", dict(Counter(r["src"] for r in rows if r["src"] != "-")))
cells = sum(len(r["src"].split("+")) for r in rows if r["src"] != "-")
print(f"定夺单元格数：{cells}")
print("conf 分布（未被覆盖）：", dict(Counter(r["conf"] for r in rows)))
