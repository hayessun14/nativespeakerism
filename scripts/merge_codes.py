#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把十二组编码 TSV 合并为一张总表，并回填主表的频次与统计量。

输出 coding/all_codes.tsv，字段：
  group contrast target_corpus ref_corpus rank type freq_tar freq_ref
  range_tar range_ref ll lr d1 d1sub act hedge c conf src note

src 逐层记录哪些层由 concordance 定夺（d1/act/hedge/c，"+"连接；"-"为无），
与 conf（编码者信度 H/M/L）分列，互不覆盖。
"""
import csv, sys

SRC = "data_keyword_ALL_selected.md"
OUT = "coding/all_codes.tsv"
CODE_FIELDS = ["d1", "d1sub", "act", "hedge", "c", "conf", "src", "note"]
OUT_FIELDS = ["group", "contrast", "target_corpus", "ref_corpus", "rank", "type",
              "freq_tar", "freq_ref", "range_tar", "range_ref", "ll", "lr"] + CODE_FIELDS

CONTRAST = {1: ("L1", "Generic"), 2: ("Generic", "L1"), 3: ("Chinese", "Generic"),
            4: ("Generic", "Chinese"), 5: ("Chinese", "German"), 6: ("German", "Chinese"),
            7: ("German", "Generic"), 8: ("Generic", "German"), 9: ("Baseline", "Generic"),
            10: ("Generic", "Baseline"), 11: ("Baseline", "L1"), 12: ("L1", "Baseline")}
EXPECTED = {1: 128, 2: 131, 3: 37, 4: 30, 5: 56, 6: 59,
            7: 77, 8: 65, 9: 131, 10: 121, 11: 30, 12: 26}

def parse_group(text, g):
    """从主表抽取某组的原始数据行，保留 Range 的 ≥ 记号。"""
    nxt = f"## 组 {g + 1}：" if g < 12 else "@@NO_NEXT@@"
    sec = text.split(f"## 组 {g}：")[1].split(nxt)[0]
    rows = []
    for line in sec.splitlines():
        if not line.startswith("|"):
            continue
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) < 8 or not c[0].isdigit():
            continue
        rows.append(dict(rank=c[0], type=c[1], freq_tar=c[2], freq_ref=c[3],
                         range_tar=c[4], range_ref=c[5], ll=c[6], lr=c[7]))
    return rows

text = open(SRC, encoding="utf-8").read()
merged = []
for g in range(1, 13):
    raw = parse_group(text, g)
    codes = {r["type"]: r for r in
             csv.DictReader(open(f"coding/group{g:02d}_codes.tsv", encoding="utf-8"), delimiter="\t")}
    assert len(raw) == EXPECTED[g], f"组 {g} 主表解析到 {len(raw)} 行，应为 {EXPECTED[g]}"
    assert {r["type"] for r in raw} == set(codes), f"组 {g} 主表与编码表词形不匹配"
    tgt, ref = CONTRAST[g]
    for r in raw:
        row = dict(group=g, contrast=f"{tgt} vs {ref}", target_corpus=tgt, ref_corpus=ref, **r)
        row.update({k: codes[r["type"]][k] for k in CODE_FIELDS})
        merged.append(row)

assert len(merged) == 891, f"合并后 {len(merged)} 行，应为 891"
# 字段内不含制表符或换行，故以 QUOTE_NONE 写出纯制表符分隔文件——
# 否则 note 中的英文引号会触发整格加引号，给 Excel / R 的读取添麻烦。
bad = [(r["group"], r["type"], k) for r in merged for k in OUT_FIELDS
       if any(ch in str(r[k]) for ch in "\t\r\n")]
assert not bad, f"字段含制表符或换行，无法以 QUOTE_NONE 写出: {bad}"
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write("\t".join(OUT_FIELDS) + "\n")
    for r in merged:
        f.write("\t".join(str(r[k]) for k in OUT_FIELDS) + "\n")

# 汇总核对
from collections import Counter
print(f"写出 {OUT}：{len(merged)} 行 × {len(OUT_FIELDS)} 列")
print(f"唯一词形 {len({r['type'] for r in merged})}\n")
print(f"{'组':<4}{'对比':<22}{'词位':>5}{'G1':>5}{'G2':>5}{'A1':>4}{'A2':>4}{'A3':>4}{'M1':>4}{'C1':>4}")
for g in range(1, 13):
    rs = [r for r in merged if r["group"] == g]
    n = lambda k, v: sum(1 for r in rs if r[k] == v)
    print(f"{g:<4}{rs[0]['contrast']:<22}{len(rs):>5}{n('d1','G1'):>5}{n('d1','G2'):>5}"
          f"{n('act','A1'):>4}{n('act','A2'):>4}{n('act','A3'):>4}{n('hedge','M1'):>4}{n('c','C1'):>4}")
tot = Counter()
for r in merged:
    for k in ("d1", "act", "hedge", "c"):
        tot[(k, r[k])] += 1
print(f"\n全表标签计数：G1 {tot[('d1','G1')]}、G2 {tot[('d1','G2')]}、"
      f"A1 {tot[('act','A1')]}、A2 {tot[('act','A2')]}、A3 {tot[('act','A3')]}、"
      f"M1 {tot[('hedge','M1')]}、C1 {tot[('c','C1')]}")
print(f"PENDING：维度一 {tot[('d1','PENDING')]}、act {tot[('act','PENDING')]}、"
      f"hedge {tot[('hedge','PENDING')]}、维度三 {tot[('c','PENDING')]}")
src_rows = [r for r in merged if r["src"] != "-"]
src_cells = Counter(L for r in src_rows for L in r["src"].split("+"))
print(f"concordance 定夺：{len(src_rows)} 行 / {sum(src_cells.values())} 单元格"
      f"（维度一 {src_cells['d1']}、act {src_cells['act']}、"
      f"hedge {src_cells['hedge']}、维度三 {src_cells['c']}）")
