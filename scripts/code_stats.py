#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""合并关键词主表与人工编码，输出维度分布统计。"""
import re, sys, csv
from collections import Counter, defaultdict

SRC = "data_keyword_ALL_selected.md"
GROUP_HEAD = "## 组 1："
NEXT_HEAD  = "## 组 2："

def parse_group(path, head, nxt):
    rows, on = [], False
    for line in open(path, encoding="utf-8"):
        if line.startswith(head): on = True; continue
        if on and line.startswith(nxt): break
        if on and line.startswith("|"):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            if len(c) < 8 or not c[0].isdigit(): continue
            rows.append(dict(rank=int(c[0]), type=c[1],
                             ft=int(c[2]), fr=int(c[3]),
                             ll=float(c[6]), lr=float(c[7])))
    return rows

def load_codes(path):
    with open(path, encoding="utf-8") as f:
        return {r["type"]: r for r in csv.DictReader(f, delimiter="\t")}

rows  = parse_group(SRC, GROUP_HEAD, NEXT_HEAD)
codes = load_codes("coding/group01_codes.tsv")

# --- 完整性校验 ---
tl, cl = {r["type"] for r in rows}, set(codes)
assert len(rows) == 128, f"解析到 {len(rows)} 行，应为 128"
assert tl == cl, f"未编码: {sorted(tl-cl)} / 多余编码: {sorted(cl-tl)}"
for r in rows: r.update(codes[r["type"]])
print(f"[校验] 128 行全部匹配，无遗漏无冗余\n")

def block(title, key, rows, subkey=None):
    print(f"### {title}")
    coded = [r for r in rows if r[key] not in ("NA", "PENDING")]
    na    = [r for r in rows if r[key] == "NA"]
    pend  = [r for r in rows if r[key] == "PENDING"]
    n = len(coded)
    cnt, fsum = Counter(), Counter()
    for r in coded:
        lab = r[key]
        cnt[lab] += 1; fsum[lab] += r["ft"]
    tot_f = sum(fsum.values())
    for lab, c in cnt.most_common():
        print(f"  {lab:<6} 词位 {c:>3} ({c/n*100:5.1f}%)  Freq_Tar {fsum[lab]:>6} ({fsum[lab]/tot_f*100:5.1f}%)")
    print(f"  —— 已定标签合计 {n}；N/A {len(na)}；PENDING {len(pend)}；清单总数 {len(rows)}")
    if subkey:
        sub = Counter((r[key], r[subkey]) for r in coded)
        print("  子类：")
        for (a, b), c in sorted(sub.items()):
            print(f"    {a}/{b:<18} {c:>3} ({c/n*100:5.1f}%)")
    print()

block("维度一 Feedback Focus（G1/G2）", "d1", rows, "d1sub")
block("维度二 Feedback Acts（D1/D2/D3）", "d2", rows)
block("维度三 Larger Contexts（C1）", "c", rows)

# D0
d0 = Counter(r["d0"] for r in rows)
print("### D0 Mitigation（补充观察，不入主维度）")
print(f"  D0=1 {d0['1']}  PENDING {d0['PENDING']}  非 hedge {d0['0']}")
print("  D0=1: " + ", ".join(r["type"] for r in rows if r["d0"] == "1"))
print("  PENDING: " + ", ".join(r["type"] for r in rows if r["d0"] == "PENDING") + "\n")

# 交叉表
print("### 维度一 × 维度二 交叉表（词位数）")
d1s = ["G1", "G2", "NA", "PENDING"]; d2s = ["D1", "D2", "D3", "NA", "PENDING"]
print("        " + "".join(f"{x:>9}" for x in d2s) + f"{'合计':>9}")
for a in d1s:
    line = f"{a:<8}"
    for b in d2s:
        line += f"{sum(1 for r in rows if r['d1']==a and r['d2']==b):>9}"
    line += f"{sum(1 for r in rows if r['d1']==a):>9}"
    print(line)
line = f"{'合计':<7}"
for b in d2s: line += f"{sum(1 for r in rows if r['d2']==b):>9}"
print(line + f"{len(rows):>9}\n")

# LL 前 20 构成
print("### LL 前 20 词位构成")
for r in rows[:20]:
    print(f"  {r['rank']:>3} {r['type']:<16} LL {r['ll']:>7.3f}  LR {r['lr']:>5.3f}  "
          f"D1={r['d1']}{'/'+r['d1sub'] if r['d1sub'] not in ('-','') else ''}  D2={r['d2']}")
top = [r for r in rows[:20]]
print(f"  前 20 中 G1={sum(1 for r in top if r['d1']=='G1')}  G2={sum(1 for r in top if r['d1']=='G2')}  "
      f"N/A={sum(1 for r in top if r['d1']=='NA')}  PENDING={sum(1 for r in top if r['d1']=='PENDING')}\n")

# 敏感性：PENDING 全归 G1 / 全归 G2
g1 = sum(1 for r in rows if r["d1"]=="G1"); g2 = sum(1 for r in rows if r["d1"]=="G2")
p  = sum(1 for r in rows if r["d1"]=="PENDING")
print("### 敏感性分析（维度一 PENDING 极端归属）")
print(f"  现状        G1 {g1}/{g1+g2} = {g1/(g1+g2)*100:.1f}%")
print(f"  PENDING→G1  G1 {g1+p}/{g1+g2+p} = {(g1+p)/(g1+g2+p)*100:.1f}%")
print(f"  PENDING→G2  G1 {g1}/{g1+g2+p} = {g1/(g1+g2+p)*100:.1f}%\n")

# 置信度
print("### 编码置信度分布（已定标签项）")
c = Counter(r["conf"] for r in rows)
for k in ("H","M","L","-"):
    if c[k]: print(f"  {k}: {c[k]}")
print("  L（低信度，优先送 concordance）: " + ", ".join(r["type"] for r in rows if r["conf"]=="L"))

# 效应量剖面
import statistics as st
print("\n### 效应量剖面（Log Ratio）")
for key, labs in (("d1", ["G1","G2","NA","PENDING"]), ("d2", ["D1","D2","D3","NA","PENDING"])):
    for lab in labs:
        sel = [r["lr"] for r in rows if r[key] == lab]
        if sel:
            print(f"  {key.upper()}={lab:<8} n={len(sel):>3}  LR 均值 {st.mean(sel):.3f}  中位 {st.median(sel):.3f}  最大 {max(sel):.3f}")
print()
print("### LR ≥ 1.5 的高效应量词位")
for r in sorted(rows, key=lambda x: -x["lr"]):
    if r["lr"] >= 1.5:
        print(f"  {r['type']:<14} LR {r['lr']:>5.3f}  LL {r['ll']:>7.3f}  D1={r['d1']}  D2={r['d2']}  {r['note'][:34]}")
print()
print("### 议题内容残留（应在前置清洗中移除但仍在表内）")
for r in rows:
    if "议题内容残留" in r["note"]:
        print(f"  #{r['rank']:<4}{r['type']:<12} Freq_Tar {r['ft']:>4}  Range_Tar 见主表  LL {r['ll']:.3f}")
