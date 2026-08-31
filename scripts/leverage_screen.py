#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""P4–P6 PENDING 项的杠杆筛查：判定哪些必须查 concordance、哪些可留作未决。

只读 coding/all_codes.tsv 与 coding/pending_worklist.tsv，不修改任何编码。

占比口径：分母 = 该组该层已定标签数（N/A 与 PENDING 不计入）。
杠杆   ：把该 PENDING 单元格分别假定为该层每一种可能归属，各算一次全组占比，
         取任一类别占比相对基线的最大变动幅度（百分点）；词种与词次各算一遍取大者。
"""
import csv, itertools
from collections import defaultdict

CATS = {"d1": ["G1", "G2", "NA"], "act": ["A1", "A2", "A3", "NA"],
        "hedge": ["M1", "NA"], "c": ["C1", "NA"]}
NONNA = {k: [c for c in v if c != "NA"] for k, v in CATS.items()}
LAYER_CN = {"d1": "维度一", "act": "act 层", "hedge": "hedge 层", "c": "维度三"}
THRESH = 3.0          # 条款 1 杠杆阈值（百分点）
WIDTH_WARN = 5.0      # 可留未决合计区间宽度警告阈值

rows = list(csv.DictReader(open("coding/all_codes.tsv", encoding="utf-8"), delimiter="\t"))
prio = {r["type"]: int(r["priority"])
        for r in csv.DictReader(open("coding/pending_worklist.tsv", encoding="utf-8"), delimiter="\t")}

# ---- 基线：各组各层的已定标签计数与词次 ----
base_c = defaultdict(lambda: defaultdict(int))   # (g,layer) -> cat -> 词种数
base_w = defaultdict(lambda: defaultdict(int))   # (g,layer) -> cat -> 词次
pend = defaultdict(list)                          # (g,layer) -> [(type, freq)]
for r in rows:
    g = int(r["group"]); f = int(r["freq_tar"])
    for layer in CATS:
        v = r[layer]
        if v == "PENDING":
            pend[(g, layer)].append((r["type"], f))
        elif v != "NA":
            base_c[(g, layer)][v] += 1
            base_w[(g, layer)][v] += f

def pct(counts, cats):
    tot = sum(counts.get(c, 0) for c in cats)
    return {c: (counts.get(c, 0) / tot * 100 if tot else 0.0) for c in cats}, tot

def scenario(g, layer, assign):
    """assign: [(cat, freq), ...] 追加到基线上，返回 (词种占比, 词次占比)。"""
    cc = dict(base_c[(g, layer)]); ww = dict(base_w[(g, layer)])
    for cat, f in assign:
        if cat == "NA":
            continue
        cc[cat] = cc.get(cat, 0) + 1
        ww[cat] = ww.get(cat, 0) + f
    return pct(cc, NONNA[layer])[0], pct(ww, NONNA[layer])[0]

def leverage(g, layer, freq):
    """单个 PENDING 单元格的杠杆：词种、词次、是否改变类别大小排序。"""
    b_c, b_w = scenario(g, layer, [])
    lev_c = lev_w = 0.0; reorder = False
    for cat in CATS[layer]:
        s_c, s_w = scenario(g, layer, [(cat, freq)])
        lev_c = max(lev_c, max(abs(s_c[k] - b_c[k]) for k in NONNA[layer]))
        lev_w = max(lev_w, max(abs(s_w[k] - b_w[k]) for k in NONNA[layer]))
        for a, b in itertools.combinations(NONNA[layer], 2):
            for bb, ss in ((b_c, s_c), (b_w, s_w)):
                if (bb[a] > bb[b] and ss[a] < ss[b]) or (bb[a] < bb[b] and ss[a] > ss[b]):
                    reorder = True
    return lev_c, lev_w, reorder

def envelope(g, layer, unresolved, mode="c"):
    """把 unresolved 全部同时推向同一极端，返回各类别占比的 (min,max) 区间。

    mode="c" 词种口径，mode="w" 词次口径——两种口径量纲不同，不并作一个区间，
    否则未决集合为空时也会显示出一段「区间」，那其实只是两种口径的差值。
    """
    idx = 0 if mode == "c" else 1
    lo = {c: 100.0 for c in NONNA[layer]}; hi = {c: 0.0 for c in NONNA[layer]}
    for cat in CATS[layer]:
        s = scenario(g, layer, [(cat, f) for _, f in unresolved])[idx]
        for k in NONNA[layer]:
            lo[k] = min(lo[k], s[k]); hi[k] = max(hi[k], s[k])
    return lo, hi

def intra_flip(g, layer, unresolved):
    """组内结论是否可能翻转：类别两两大小关系在任一极端下反转。"""
    b_c, b_w = scenario(g, layer, [])
    for cat in CATS[layer]:
        s_c, s_w = scenario(g, layer, [(cat, f) for _, f in unresolved])
        for a, b in itertools.combinations(NONNA[layer], 2):
            for bb, ss in ((b_c, s_c), (b_w, s_w)):
                if (bb[a] > bb[b] and ss[a] < ss[b]) or (bb[a] < bb[b] and ss[a] > ss[b]):
                    return True, f"{a}%／{b}% 大小关系反转"
    return False, ""

print("[基线核对] 各组各层已定标签数：")
for g in range(1, 13):
    parts = []
    for layer in ("d1", "act", "hedge", "c"):
        n = sum(base_c[(g, layer)].values())
        p = len(pend[(g, layer)])
        parts.append(f"{LAYER_CN[layer]} {n}(+{p}待定)")
    print(f"  组{g:<3} " + "　".join(parts))

# ---------------- 单类别层的指标退化 ----------------
# hedge 层与维度三层各只有一个非 N/A 类别（M1／C1），占比恒为 100%（或分母为 0 时的 0%）。
# 占比口径在这类层上不承载信息：无论新增多少个 M1，占比都是 100%。
# 因此这些单元格不能凭「杠杆 = 0」留作未决——本脚本对其单列标记，并按保守方向判为必查。
DEGENERATE = {layer for layer in CATS if len(NONNA[layer]) == 1}

# ---------------- 逐单元格计算 ----------------
SCREEN_PRIO = {4, 5, 6}
cells = []
for (g, layer), lst in pend.items():
    for t, f in lst:
        p = prio.get(t, 6)
        lev_c, lev_w, reorder = leverage(g, layer, f)
        cells.append(dict(group=g, layer=layer, type=t, freq=f, prio=p,
                          lev_c=lev_c, lev_w=lev_w, lev=max(lev_c, lev_w),
                          reorder=reorder, degen=layer in DEGENERATE))

screen = [c for c in cells if c["prio"] in SCREEN_PRIO]
N_SCREEN = sum(1 for t, v in prio.items() if v in SCREEN_PRIO)   # P4–P6 词形数
N_MUST_PRIO = sum(1 for t, v in prio.items() if v not in SCREEN_PRIO)  # P1–P3 词形数
N_TOTAL = len(prio)
print(f"\n[范围] PENDING 单元格 {len(cells)} 个；其中 P4–P6 待筛查 {len(screen)} 个，"
      f"涉及词形 {len({c['type'] for c in screen})} 个")
print(f"[退化层] {', '.join(LAYER_CN[l] for l in sorted(DEGENERATE))} 只有一个非 N/A 类别，占比指标失效；"
      f"P4–P6 中此类单元格 {sum(1 for c in screen if c['degen'])} 个")

# ---------------- 条款 1、2 ----------------
must = set()          # 触发必查的 (group, layer, type)
why = defaultdict(list)
for c in screen:
    if c["degen"]:
        must.add((c["group"], c["layer"], c["type"])); why[(c["group"], c["layer"], c["type"])].append("退化层")
        continue
    if c["lev"] >= THRESH:
        must.add((c["group"], c["layer"], c["type"])); why[(c["group"], c["layer"], c["type"])].append("条款1")
    if c["reorder"]:
        must.add((c["group"], c["layer"], c["type"])); why[(c["group"], c["layer"], c["type"])].append("条款2")
print(f"[条款 1／2] 触发必查单元格 {len(must)} 个")

# ---------------- 条款 3：集合区间翻转 ----------------
# 未决集合 = 该组该层尚未被标为必查的 P4–P6 单元格。
# P1–P3 一律必查，视同将被解决，故不计入未决集合（本轮为第一遍，
# 待 P1–P3 实际解决后须按分母变化重跑，以第二遍为准）。
def unresolved(g, layer):
    return [(c["type"], c["freq"]) for c in screen
            if c["group"] == g and c["layer"] == layer
            and (g, layer, c["type"]) not in must]

clause3_log = []
for (g, layer) in sorted(pend, key=lambda k: (k[0], k[1])):
    if layer in DEGENERATE:
        continue
    while True:
        U = unresolved(g, layer)
        if not U:
            break
        flip, desc = intra_flip(g, layer, U)
        if not flip:
            break
        # 按杠杆从大到小逐个标为必查
        cand = sorted((c for c in screen if c["group"] == g and c["layer"] == layer
                       and (g, layer, c["type"]) not in must),
                      key=lambda c: -c["lev"])[0]
        key = (g, layer, cand["type"])
        must.add(key); why[key].append("条款3")
        clause3_log.append((g, layer, cand["type"], round(cand["lev"], 2), desc))

# ---------------- 条款 3 的跨组部分 ----------------
CROSS = [("组1 vs 组2 的 G2%", 1, 2, "d1", "G2"),
         ("中文组 vs 德语组的 G2%（组5 vs 组6）", 5, 6, "d1", "G2"),
         ("Baseline vs L1 的维度一 G1%（组11 vs 组12）", 11, 12, "d1", "G1"),
         ("Baseline vs L1 的 act 层 A1%（组11 vs 组12）", 11, 12, "act", "A1"),
         ("Baseline vs L1 的 act 层 A3%（组11 vs 组12）", 11, 12, "act", "A3")]

def bounds(g, layer, cat, mode="c"):
    lo, hi = envelope(g, layer, unresolved(g, layer), mode)
    return lo[cat], hi[cat]

cross_log = []
for name, ga, gb, layer, cat in CROSS:
    while True:
        flip = False
        for mi, mode in ((0, "c"), (1, "w")):
            a_now = scenario(ga, layer, [])[mi][cat]; b_now = scenario(gb, layer, [])[mi][cat]
            a_lo, a_hi = bounds(ga, layer, cat, mode); b_lo, b_hi = bounds(gb, layer, cat, mode)
            if a_now < b_now and a_hi > b_lo:   flip = True
            if a_now > b_now and a_lo < b_hi:   flip = True
        a_now = scenario(ga, layer, [])[0][cat]; b_now = scenario(gb, layer, [])[0][cat]
        a_lo, a_hi = bounds(ga, layer, cat); b_lo, b_hi = bounds(gb, layer, cat)
        if not flip:
            cross_log.append((name, a_now, (a_lo, a_hi), b_now, (b_lo, b_hi), "不翻转"))
            break
        pool = [c for c in screen if c["layer"] == layer and c["group"] in (ga, gb)
                and (c["group"], layer, c["type"]) not in must]
        if not pool:
            cross_log.append((name, a_now, (a_lo, a_hi), b_now, (b_lo, b_hi),
                              "仍可翻转：P4–P6 已全部标为必查，剩余不确定性来自 P1–P3"))
            break
        cand = sorted(pool, key=lambda c: -c["lev"])[0]
        key = (cand["group"], layer, cand["type"])
        must.add(key); why[key].append("条款3跨组")
        cross_log.append((name, a_now, (a_lo, a_hi), b_now, (b_lo, b_hi),
                          f"可翻转 → 标记 组{cand['group']} `{cand['type']}` 必查"))

print(f"[条款 3] 组内追加必查 {len(clause3_log)} 个；跨组检验 {len(CROSS)} 项")
print(f"[合计] 必查单元格 {len(must)} 个 / 待筛查 {len(screen)} 个")
must_types = {t for _, _, t in must}
print(f"[词形口径] 必查词形 {len(must_types)} 个 / P4–P6 词形 {N_SCREEN} 个")

# ---------------- 输出 1：leverage_screen.tsv ----------------
CLAUSE_CN = {"条款1": "条款1 杠杆≥3.0", "条款2": "条款2 改变排序",
             "条款3": "条款3 组内集合翻转", "条款3跨组": "条款3 跨组集合翻转",
             "退化层": "退化层 占比指标失效"}
FIELDS = ["group", "type", "layer", "freq_tar", "杠杆_词种", "杠杆_词次",
          "杠杆_max", "触发条款", "判定"]
screen.sort(key=lambda c: (-c["lev"], c["group"], c["type"]))
with open("coding/leverage_screen.tsv", "w", encoding="utf-8", newline="\n") as f:
    f.write("\t".join(FIELDS) + "\n")
    for c in screen:
        k = (c["group"], c["layer"], c["type"])
        cl = "＋".join(CLAUSE_CN[x] for x in dict.fromkeys(why[k])) if k in must else "—"
        f.write("\t".join([str(c["group"]), c["type"], LAYER_CN[c["layer"]], str(c["freq"]),
                           f"{c['lev_c']:.2f}", f"{c['lev_w']:.2f}", f"{c['lev']:.2f}",
                           cl, "必查" if k in must else "可留未决"]) + "\n")

# ---------------- 输出 2：leverage_summary.md ----------------
md = []; W = md.append
W("# P4–P6 PENDING 项杠杆筛查结果\n")
W("> 由 `scripts/leverage_screen.py` 生成，只读 `coding/all_codes.tsv` 与 "
  "`coding/pending_worklist.tsv`，未修改任何编码。")
W(f"> **P1–P3（{N_MUST_PRIO} 个词形）一律必查，不参与筛查。** 本报告只处理 P4–P6 的 {N_SCREEN} 个词形。")
W("> 占比口径：分母 = 该组该层已定标签数（N/A 与 PENDING 不计入）。\n")

W("## 一、缩减效果\n")
W("| | 词形 | 单元格 |")
W("|---|---:|---:|")
W(f"| P4–P6 总计 | {N_SCREEN} | {len(screen)} |")
W(f"| 判定必查 | **{len(must_types)}** | {len(must)} |")
W(f"| 可留未决 | {N_SCREEN - len(must_types)} | {len(screen) - len(must)} |")
W("")
W(f"**{N_SCREEN} → {len(must_types)}**，减少 {N_SCREEN - len(must_types)} 个词形（{(N_SCREEN-len(must_types))/N_SCREEN*100:.0f}%）。")
W(f"连同 P1–P3 的 {N_MUST_PRIO} 个，concordance 必查词形合计 **{len(must_types) + N_MUST_PRIO}** 个"
  f"（原 {N_TOTAL} 个，减少 {N_TOTAL - len(must_types) - N_MUST_PRIO} 个）。\n")
W("> **缩减幅度有限，原因在分母。** 本研究多数组的已定标签数是 11–52，"
  "个别组的 act 层只有 2–7。分母越小，单个词位的占比杠杆越大——"
  "组 4 act 层分母为 2，一个词位就能移动 33 个百分点。"
  "因此「可留未决」主要落在组 1／2／9／10 这四个分母较大的组，"
  "小分母组几乎无法留白。\n")

W("## 二、各组各层的集合区间（未决项全部推向同一极端）\n")
W("> 词种与词次两种口径量纲不同，分列报告，不并作一个区间。"
  "只列出仍有可留未决项的组×层——未决集合为空者，占比已被必查项完全锁定。\n")
W("| 组 | 层 | 类别 | 词种现值 | 词种区间 | 宽度 | 词次现值 | 词次区间 | 宽度 | 可留未决项数 |")
W("|---|---|---|---:|---|---:|---:|---|---:|---:|")
warnings = []
for g in range(1, 13):
    for layer in ("d1", "act"):
        U = unresolved(g, layer)
        if not U:
            continue
        lo_c, hi_c = envelope(g, layer, U, "c"); lo_w, hi_w = envelope(g, layer, U, "w")
        b_c, b_w = scenario(g, layer, [])
        for cat in NONNA[layer]:
            wc = hi_c[cat] - lo_c[cat]; ww = hi_w[cat] - lo_w[cat]
            W(f"| {g} | {LAYER_CN[layer]} | {cat} | {b_c[cat]:.1f}% | "
              f"[{lo_c[cat]:.1f}%, {hi_c[cat]:.1f}%] | {wc:.1f} | "
              f"{b_w[cat]:.1f}% | [{lo_w[cat]:.1f}%, {hi_w[cat]:.1f}%] | {ww:.1f} | {len(U)} |")
            if max(wc, ww) > WIDTH_WARN:
                warnings.append((g, LAYER_CN[layer], cat, b_c[cat], lo_c[cat], hi_c[cat],
                                 max(wc, ww), len(U)))
W("")
if warnings:
    W(f"### ⚠ 警告：{len(warnings)} 处可留未决项的合计区间宽度超过 {WIDTH_WARN} 个百分点\n")
    W("| 组 | 层 | 类别 | 现值 | 区间 | 宽度 | 未决项数 |")
    W("|---|---|---|---:|---|---:|---:|")
    for g, l, cat, b, lo_, hi_, w, n in sorted(warnings, key=lambda x: -x[6]):
        W(f"| {g} | {l} | {cat} | {b:.1f}% | [{lo_:.1f}%, {hi_:.1f}%] | **{w:.1f}** | {n} |")
    W("")
    W("这些区间宽度不足以翻转任何已检验的结论（否则会被条款 3 捕获），"
      "但**足以改变占比的报告精度**。\n")
    W("#### 必须挑明的一点：筛查缩减的是工作量，不是不确定性\n")
    W("组 1 维度一是最清楚的例子。**全部 23 个 PENDING 都未决时**，各组报告给出的敏感性区间是 "
      "G1 [56.0%, 86.7%]；**筛查把其中 2 个标为必查、留下 21 个未决后**，区间是 G1 [57.5%, 86.3%]——"
      "宽度从 30.7 降到 28.8 个百分点，几乎没有收窄。组 9 同理（25.7 个百分点）。")
    W("原因是这些组的维度一 PENDING 数量大（21、18 个）且个体杠杆都不高，"
      "条款 1 的 3.0 个百分点阈值逐个看都不触发，合起来却能移动近 30 个百分点。"
      "条款 3 只保证**方向**（G1% > G2%）不翻转，不保证**数值**稳定。")
    W("因此结论取决于论文要报告什么：")
    W(f"- 只报告**方向**（「L1 侧偏全局」「Generic 侧偏局部」）→ {N_SCREEN - len(must_types)} 个词形确实可以留作未决；")
    W("- 要报告**点估计**（「G1 占 80.8%」）→ 组 1／组 9／组 10 维度一的未决项仍须补查，"
      "否则该数字应改为区间报告。")
    W("这一点不是筛查方法的缺陷，而是它的正确输出：它回答的是「哪些词会改变结论」，"
      "不是「哪些词会改变数字」。\n")
    W("#### 一个未纳入检验的既有问题\n")
    W("各组报告曾指出：组 1 与组 2 的 **G1% 敏感性区间存在重叠 [56.0%, 68.9%]**，"
      "是十二组中唯一如此的一对。本次跨组检验按任务指定检验的是「组1 与组2 的 **G2%** 高低」，"
      "两者不是同一个量。**那处重叠未被本次筛查覆盖，仍然成立，仍须由 P1–P3 与本轮必查项的 "
      "concordance 结果来消解。**\n")
else:
    W("所有可留未决项的合计区间宽度均不超过 %.1f 个百分点。\n" % WIDTH_WARN)

W("## 三、跨组结论的翻转检验\n")
W("> 区间为词种口径；翻转判定同时检验词种与词次两种口径，任一可翻转即判为可翻转。\n")
W("| 结论 | 组 A 现值 | 组 A 区间 | 组 B 现值 | 组 B 区间 | 判定 |")
W("|---|---:|---|---:|---|---|")
for name, a, ai, b, bi, res in cross_log:
    W(f"| {name} | {a:.1f}% | [{ai[0]:.1f}%, {ai[1]:.1f}%] | {b:.1f}% | "
      f"[{bi[0]:.1f}%, {bi[1]:.1f}%] | {res} |")
W("")

W("## 四、必查词形（按杠杆降序）\n")
seen = {}
for c in screen:
    k = (c["group"], c["layer"], c["type"])
    if k in must:
        if c["type"] not in seen or c["lev"] > seen[c["type"]]["lev"]:
            seen[c["type"]] = dict(c, clause="＋".join(dict.fromkeys(why[k])))
W("| 词形 | 最大杠杆 | 组 | 层 | Freq_Tar | 触发条款 |")
W("|---|---:|---:|---|---:|---|")
for t, c in sorted(seen.items(), key=lambda x: -x[1]["lev"]):
    W(f"| `{t}` | {c['lev']:.2f} | {c['group']} | {LAYER_CN[c['layer']]} | {c['freq']} | "
      f"{'＋'.join(CLAUSE_CN[x] for x in dict.fromkeys(why[(c['group'], c['layer'], c['type'])]))} |")
W("")

W("## 五、可留未决词形\n")
free = {}
for c in screen:
    if (c["group"], c["layer"], c["type"]) not in must and c["type"] not in must_types:
        if c["type"] not in free or c["lev"] > free[c["type"]]["lev"]:
            free[c["type"]] = c
W(f"共 **{len(free)}** 个词形，全部单元格均未触发任何条款。\n")
W("| 词形 | 最大杠杆 | 组 | 层 | Freq_Tar |")
W("|---|---:|---:|---|---:|")
for t, c in sorted(free.items(), key=lambda x: -x[1]["lev"]):
    W(f"| `{t}` | {c['lev']:.2f} | {c['group']} | {LAYER_CN[c['layer']]} | {c['freq']} |")
W("")

W("## 六、两点必须说明的限制\n")
W("### 6.1 hedge 层与维度三的占比指标失效\n")
W("这两层各只有一个非 N/A 类别（M1／C1），占比恒为 100%——无论新增多少个 M1，"
  "M1 占已定标签的比例都不会变。**占比杠杆在这两层上恒等于 0，不承载任何信息。**")
W(f"P4–P6 中此类单元格 {sum(1 for c in screen if c['degen'])} 个，"
  "本脚本未让它们凭「杠杆 = 0」留作未决，而是按保守方向一律判为必查，"
  "并在触发条款列标注「退化层」。")
W("若要对这两层做实质筛查，应改用**计数口径**（如 M1 词位数由 2 增至 6 是三倍变化），"
  "而非占比口径——这需要另行定义阈值，不在本次任务范围内。\n")
W("### 6.2 20 个词形无 PENDING 单元格，杠杆不适用\n")
W(f"P4–P6 的 {N_SCREEN} 个词形中，有 {N_SCREEN - len({c['type'] for c in screen})} 个在总表中没有任何 PENDING 单元格——"
  "它们进入待办清单的理由是 note 标记待核（议题残留疑似、子类边界）或属强制查询清单。"
  "**它们不占任何层的分母，也不改变任何已定标签占比，因此杠杆恒为 0，本筛查对其不适用。**")
W("其中议题残留疑似项若判定为残留，影响的是清单总数与 N/A 计数，不影响任何已定标签占比"
  "（各组报告已论证）；子类边界项只影响子类占比，不影响主类。二者均可留作未决，"
  "但**属强制查询清单的条目按规则仍须复核**。\n")
W("## 七、第二遍筛查的触发条件\n")
W(f"本轮为第一遍。P1–P3 的 {N_MUST_PRIO} 个词形解决后，各层分母将改变"
  "（每解决一个 PENDING 且判为非 N/A，该层分母 +1，所有占比随之变化）。"
  "**须对 P6 剩余项重跑本脚本，以第二遍结果为准。** 脚本可直接重跑："
  "更新 `all_codes.tsv` 中已解决项的标签后执行 `python3 scripts/leverage_screen.py` 即可。\n")

open("coding/leverage_summary.md", "w", encoding="utf-8").write("\n".join(md))
print(f"\n写出 coding/leverage_screen.tsv（{len(screen)} 行）与 coding/leverage_summary.md（{len(md)} 行）")
print(f"区间宽度超阈警告：{len(warnings)} 处")
