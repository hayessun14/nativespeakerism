#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""合并关键词主表与人工编码，输出维度分布统计与报告附表（手册 v3 编号）。

维度二为两层结构：act 层（A1/A2/A3，0–1 个）＋ hedge 层（M1，0–1 个），二者可共存。
"""
import csv, statistics as st
from collections import Counter

import sys
G = sys.argv[1] if len(sys.argv) > 1 else "1"
SRC, CODES = "data_keyword_ALL_selected.md", f"coding/group{int(G):02d}_codes.tsv"
HEAD = f"## 组 {G}："
NEXT = f"## 组 {int(G)+1}：" if int(G) < 12 else "@@NO_NEXT@@"

def parse_group(path, head, nxt):
    rows, on = [], False
    for line in open(path, encoding="utf-8"):
        if line.startswith(head): on = True; continue
        if on and line.startswith(nxt): break
        if on and line.startswith("|"):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            if len(c) < 8 or not c[0].isdigit(): continue
            rows.append(dict(rank=int(c[0]), type=c[1], ft=int(c[2]),
                             ll=float(c[6]), lr=float(c[7])))
    return rows

rows  = parse_group(SRC, HEAD, NEXT)
codes = {r["type"]: r for r in csv.DictReader(open(CODES, encoding="utf-8"), delimiter="\t")}
N = {"1":128,"2":131,"3":37,"4":30,"5":56,"6":59,"7":77,"8":65,"9":131,"10":121,"11":30,"12":26}[G]
assert len(rows) == N, f"解析到 {len(rows)} 行，应为 {N}"
assert {r["type"] for r in rows} == set(codes), "编码表与主表不匹配"
for r in rows: r.update(codes[r["type"]])
LEGAL = {"d1": {"G1","G2","NA","PENDING"},
         "d1sub": {"Ideas","Development","Global Structure","Local Structure",
                   "Wording","Correctness","Grammar","Mechanics","-"},
         "act": {"A1","A2","A3","NA","PENDING"},
         "hedge": {"M1","NA","PENDING"},
         "c": {"C1","NA","PENDING"},
         "conf": {"H","M","L","C","-"}}
bad = [(r["type"], k, r[k]) for r in rows for k in LEGAL if r[k] not in LEGAL[k]]
assert not bad, f"非法取值: {bad}"
sub = [(r["type"], r["d1"], r["d1sub"]) for r in rows
       if (r["d1"] in ("G1","G2")) != (r["d1sub"] != "-")]
assert not sub, f"主类与子类不匹配: {sub}"
print(f"[校验] {N} 行全部匹配，取值合法，主类/子类一致\n")

out = []; W = out.append

W(f"## 附表 A：组 {G} 完整编码表（{N} 词位，按 LL 降序）\n")
W("| # | Type | Freq_Tar | LL | LR | 维度一 | 子类 | 维度二 act | 维度二 hedge | 维度三 | 信度 | 判定依据 |")
W("|---:|---|---:|---:|---:|---|---|---|---|---|---|---|")
for r in rows:
    W(f"| {r['rank']} | {r['type']} | {r['ft']} | {r['ll']:.3f} | {r['lr']:.3f} | {r['d1']} | "
      f"{r['d1sub'] if r['d1sub'] != '-' else '—'} | {r['act']} | {r['hedge']} | {r['c']} | "
      f"{r['conf'] if r['conf'] != '-' else '—'} | {r['note']} |")
W("")

def tbl(title, key, subkey=None, note=None):
    """分母 = 该层已定标签数；n=0 时不生成占比行（避免除零）。"""
    W(f"### {title}\n")
    if note: W(note + "\n")
    coded = [r for r in rows if r[key] not in ("NA", "PENDING")]
    na  = sum(1 for r in rows if r[key] == "NA")
    pd_ = sum(1 for r in rows if r[key] == "PENDING")
    n   = len(coded)
    if n == 0:
        W(f"**已定标签 0 项** —— 本层无任何词位获得标签，占比不适用（分母为 0）。\n")
        W("| 标签 | 词位数 | Freq_Tar 合计 |")
        W("|---|---:|---:|")
        W("| 已定标签合计 | 0 | 0 |")
        W(f"| N/A（不计入分母） | {na} | — |")
        W(f"| PENDING（不计入分母） | {pd_} | — |")
        W(f"| 清单总数 | {len(rows)} | — |")
        W("")
        return
    cnt, fsum = Counter(), Counter()
    for r in coded: cnt[r[key]] += 1; fsum[r[key]] += r["ft"]
    tf = sum(fsum.values())
    W("| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |")
    W("|---|---:|---:|---:|---:|---:|")
    for lab, c in cnt.most_common():
        lrs = [r["lr"] for r in coded if r[key] == lab]
        W(f"| {lab} | {c} | {c/n*100:.1f}% | {fsum[lab]} | {fsum[lab]/tf*100:.1f}% | {st.mean(lrs):.3f} |")
    W(f"| **已定标签合计** | **{n}** | **100.0%** | **{tf}** | **100.0%** | — |")
    W(f"| N/A（不计入分母） | {na} | — | — | — | — |")
    W(f"| PENDING（不计入分母） | {pd_} | — | — | — | — |")
    W(f"| 清单总数 | {len(rows)} | — | — | — | — |")
    W("")
    if subkey:
        W(f"**子类分布（分母同为已定标签 {n}）**\n")
        W("| 主类 | 子类 | 词位数 | 占比 |")
        W("|---|---|---:|---:|")
        for (a, b), c in sorted(Counter((r[key], r[subkey]) for r in coded).items()):
            W(f"| {a} | {b} | {c} | {c/n*100:.1f}% |")
        W("")

tbl("B1 维度一 Feedback Focus", "d1", "d1sub")
tbl("B2 维度二 · act 层（A1 Praise / A2 Criticism / A3 Suggestion）", "act")
tbl("B3 维度二 · hedge 层（M1 Hedges）", "hedge",
    note="hedge 层与 act 层并行判定、可共存（Hyland & Hyland：hedge 施加于 act 之上）。分母为本层已定标签数。")
tbl("B4 维度三 Larger Contexts of Writing", "c")

W("### B5 维度二两层共现（词位数）\n")
acts = ["A1", "A2", "A3", "NA", "PENDING"]; hs = ["M1", "NA", "PENDING"]
W("| act ＼ hedge | " + " | ".join(hs) + " | 合计 |")
W("|---|" + "---:|" * (len(hs) + 1))
for a in acts:
    W(f"| **{a}** | " + " | ".join(str(sum(1 for r in rows if r["act"] == a and r["hedge"] == h)) for h in hs)
      + f" | **{sum(1 for r in rows if r['act'] == a)}** |")
W("| **合计** | " + " | ".join(str(sum(1 for r in rows if r["hedge"] == h)) for h in hs) + f" | **{len(rows)}** |")
co = [r["type"] for r in rows if r["act"] not in ("NA", "PENDING") and r["hedge"] == "M1"]
W(f"\nact ＋ hedge 双标签共现：**{len(co)}** 项" + ("（" + "、".join(f"`{t}`" for t in co) + "）" if co else "") + "\n")

W("### B6 维度一 × 维度二 act 层 交叉表（词位数）\n")
d1s = ["G1", "G2", "NA", "PENDING"]
W("| 维度一＼act | " + " | ".join(acts) + " | 合计 |")
W("|---|" + "---:|" * (len(acts) + 1))
for a in d1s:
    W(f"| **{a}** | " + " | ".join(str(sum(1 for r in rows if r["d1"] == a and r["act"] == b)) for b in acts)
      + f" | **{sum(1 for r in rows if r['d1'] == a)}** |")
W("| **合计** | " + " | ".join(str(sum(1 for r in rows if r["act"] == b)) for b in acts) + f" | **{len(rows)}** |\n")

W("### B7 LL 前 20 词位的维度一构成\n")
top = rows[:20]
W("| | G1 | G2 | N/A | PENDING |")
W("|---|---:|---:|---:|---:|")
W("| 词位数 | " + " | ".join(str(sum(1 for r in top if r["d1"] == x)) for x in d1s) + " |")
W("")

W("### B8 敏感性分析：维度一 PENDING 的极端归属\n")
g1 = sum(1 for r in rows if r["d1"] == "G1"); g2 = sum(1 for r in rows if r["d1"] == "G2")
p  = sum(1 for r in rows if r["d1"] == "PENDING")
W("| 情形 | G1 词位 | G2 词位 | G1 占比 |")
W("|---|---:|---:|---:|")
W(f"| 现状（PENDING 不计入） | {g1} | {g2} | {g1/(g1+g2)*100:.1f}% |")
W(f"| {p} 个 PENDING 全归 G1（上界） | {g1+p} | {g2} | {(g1+p)/(g1+g2+p)*100:.1f}% |")
W(f"| {p} 个 PENDING 全归 G2（下界） | {g1} | {g2+p} | {g1/(g1+g2+p)*100:.1f}% |")
W("")

W("### B9 concordance 待办清单\n")
pend = [r for r in rows if "PENDING" in (r["d1"], r["act"], r["hedge"], r["c"]) or r["conf"] == "L"]
W(f"共 **{len(pend)}** 个词族需 concordance 判定（含 2 个低信度已定项）。\n")
W("| Type | Freq_Tar | 待定层 | 竞争读法 |")
W("|---|---:|---|---|")
for r in pend:
    d = [n for n, k in (("维度一", "d1"), ("act", "act"), ("hedge", "hedge"), ("维度三", "c")) if r[k] == "PENDING"]
    if r["conf"] == "L": d.append("低信度复核")
    W(f"| `{r['type']}` | {r['ft']} | {'、'.join(d)} | {r['note']} |")
W("")

W("### B10 高效应量词位（LR ≥ 1.5）\n")
W("| Type | LL | LR | 维度一 | act | hedge |")
W("|---|---:|---:|---|---|---|")
for r in sorted(rows, key=lambda x: -x["lr"]):
    if r["lr"] >= 1.5:
        W(f"| {r['type']} | {r['ll']:.3f} | {r['lr']:.3f} | "
          f"{r['d1']}{'/' + r['d1sub'] if r['d1sub'] != '-' else ''} | {r['act']} | {r['hedge']} |")
W("")

open(f"coding/group{int(G):02d}_tables.md", "w", encoding="utf-8").write("\n".join(out))

# --- 终端摘要 ---
def summ(key):
    c = Counter(r[key] for r in rows)
    n = sum(v for k, v in c.items() if k not in ("NA", "PENDING"))
    return c, n
for name, key in (("维度一", "d1"), ("act 层", "act"), ("hedge 层", "hedge"), ("维度三", "c")):
    c, n = summ(key)
    parts = [f"{k} {v}" + (f" ({v/n*100:.1f}%)" if n else "") for k, v in c.most_common() if k not in ("NA", "PENDING")]
    print(f"{name:<7} 已定 {n:>3} | " + "、".join(parts) if parts else f"{name:<7} 已定 {n:>3} | 无")
    print(f"        N/A {c['NA']}、PENDING {c['PENDING']}")
print(f"\nconcordance 清单 {len(pend)} 项；写出 coding/group{int(G):02d}_tables.md")
