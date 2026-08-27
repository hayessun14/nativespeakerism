#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成组 1 编码报告的表格与统计段落（正文解读由人工撰写后拼接）。"""
import csv, statistics as st
from collections import Counter
exec(open("scripts/code_stats.py").read().split("rows  = parse_group")[0])

rows  = parse_group("data_keyword_ALL_selected.md", "## 组 1：", "## 组 2：")
codes = {r["type"]: r for r in csv.DictReader(open("coding/group01_codes.tsv", encoding="utf-8"), delimiter="\t")}
for r in rows: r.update(codes[r["type"]])

out = []
W = out.append

W("## 附表 A：组 1 完整编码表（128 词位，按 LL 降序）\n")
W("| # | Type | Freq_Tar | LL | LR | 维度一 | 子类 | 维度二 | D0 | 维度三 | 信度 | 判定依据 |")
W("|---:|---|---:|---:|---:|---|---|---|---|---|---|---|")
for r in rows:
    d0 = {"0": "—", "1": "✔", "PENDING": "PEND"}[r["d0"]]
    W(f"| {r['rank']} | {r['type']} | {r['ft']} | {r['ll']:.3f} | {r['lr']:.3f} | "
      f"{r['d1']} | {r['d1sub'] if r['d1sub'] != '-' else '—'} | {r['d2']} | {d0} | {r['c']} | "
      f"{r['conf'] if r['conf'] != '-' else '—'} | {r['note']} |")
W("")

def tbl(title, key, subkey=None):
    W(f"### {title}\n")
    coded = [r for r in rows if r[key] not in ("NA", "PENDING")]
    n = len(coded); cnt, fsum = Counter(), Counter()
    for r in coded: cnt[r[key]] += 1; fsum[r[key]] += r["ft"]
    tf = sum(fsum.values()) or 1
    W("| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |")
    W("|---|---:|---:|---:|---:|---:|")
    for lab, c in cnt.most_common():
        lrs = [r["lr"] for r in coded if r[key] == lab]
        W(f"| {lab} | {c} | {c/n*100:.1f}% | {fsum[lab]} | {fsum[lab]/tf*100:.1f}% | {st.mean(lrs):.3f} |")
    na = sum(1 for r in rows if r[key] == "NA"); pd = sum(1 for r in rows if r[key] == "PENDING")
    W(f"| **已定标签合计** | **{n}** | **100.0%** | **{tf}** | **100.0%** | — |")
    W(f"| N/A（不计入分母） | {na} | — | — | — | — |")
    W(f"| PENDING（不计入分母） | {pd} | — | — | — | — |")
    W(f"| 清单总数 | {len(rows)} | — | — | — | — |")
    W("")
    if subkey:
        W("**子类分布（分母同为已定标签 %d）**\n" % n)
        W("| 主类 | 子类 | 词位数 | 占比 |")
        W("|---|---|---:|---:|")
        for (a, b), c in sorted(Counter((r[key], r[subkey]) for r in coded).items()):
            W(f"| {a} | {b} | {c} | {c/n*100:.1f}% |")
        W("")

tbl("B1 维度一 Feedback Focus", "d1", "d1sub")
tbl("B2 维度二 Feedback Acts", "d2")
tbl("B3 维度三 Larger Contexts of Writing", "c")

W("### B4 D0 Mitigation（补充观察，不计入主维度）\n")
d0c = Counter(r["d0"] for r in rows)
W(f"- 确认 hedge：{d0c['1']} 个 —— " + "、".join(f"`{r['type']}`" for r in rows if r["d0"] == "1"))
W(f"- 待定：{d0c['PENDING']} 个 —— " + "、".join(f"`{r['type']}`" for r in rows if r["d0"] == "PENDING"))
W(f"- 非 hedge：{d0c['0']} 个\n")

W("### B5 维度一 × 维度二 交叉表（词位数）\n")
d1s = ["G1", "G2", "NA", "PENDING"]; d2s = ["D1", "D2", "D3", "NA", "PENDING"]
W("| 维度一＼维度二 | " + " | ".join(d2s) + " | 合计 |")
W("|---|" + "---:|" * (len(d2s) + 1))
for a in d1s:
    cells = [str(sum(1 for r in rows if r["d1"] == a and r["d2"] == b)) for b in d2s]
    W(f"| **{a}** | " + " | ".join(cells) + f" | **{sum(1 for r in rows if r['d1']==a)}** |")
cells = [str(sum(1 for r in rows if r["d2"] == b)) for b in d2s]
W("| **合计** | " + " | ".join(cells) + f" | **{len(rows)}** |\n")

W("### B6 LL 前 20 词位的类别构成\n")
top = rows[:20]
W("| 前 20 中 | G1 | G2 | N/A | PENDING |")
W("|---|---:|---:|---:|---:|")
W("| 维度一 | " + " | ".join(str(sum(1 for r in top if r["d1"] == x)) for x in d1s) + " |")
W("")

W("### B7 敏感性分析：维度一 PENDING 的极端归属\n")
g1 = sum(1 for r in rows if r["d1"] == "G1"); g2 = sum(1 for r in rows if r["d1"] == "G2")
p = sum(1 for r in rows if r["d1"] == "PENDING")
W("| 情形 | G1 词位 | G2 词位 | G1 占比 |")
W("|---|---:|---:|---:|")
W(f"| 现状（PENDING 不计入） | {g1} | {g2} | {g1/(g1+g2)*100:.1f}% |")
W(f"| 22 个 PENDING 全归 G1（上界） | {g1+p} | {g2} | {(g1+p)/(g1+g2+p)*100:.1f}% |")
W(f"| 22 个 PENDING 全归 G2（下界） | {g1} | {g2+p} | {g1/(g1+g2+p)*100:.1f}% |")
W("")

W("### B8 concordance 待办清单\n")
pend = [r for r in rows if "PENDING" in (r["d1"], r["d2"], r["d0"], r["c"]) or r["conf"] == "L"]
W(f"共 **{len(pend)}** 个词族需 concordance 判定（含 2 个低信度已定项）。\n")
W("| Type | 待定维度 | 竞争读法 |")
W("|---|---|---|")
for r in pend:
    dims = [n for n, k in (("一", "d1"), ("二", "d2"), ("D0", "d0"), ("三", "c")) if r[k] == "PENDING"]
    if r["conf"] == "L": dims.append("低信度复核")
    W(f"| `{r['type']}` | {'、'.join(dims)} | {r['note']} |")
W("")

W("### B9 高效应量词位（LR ≥ 1.5）\n")
W("| Type | LL | LR | 维度一 | 维度二 |")
W("|---|---:|---:|---|---|")
for r in sorted(rows, key=lambda x: -x["lr"]):
    if r["lr"] >= 1.5:
        W(f"| {r['type']} | {r['ll']:.3f} | {r['lr']:.3f} | {r['d1']}{'/'+r['d1sub'] if r['d1sub']!='-' else ''} | {r['d2']} |")
W("")

open("coding/group01_tables.md", "w", encoding="utf-8").write("\n".join(out))
print(f"写出 coding/group01_tables.md（{len(out)} 行），PENDING/复核清单 {len(pend)} 项")
