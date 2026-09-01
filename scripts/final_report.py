#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""由 concordance 消解完毕的总表生成最终统计报告 coding/final_report.md。

分析单位是「成对关键词清单」而非「条件」：每组占比刻画的是该次对比中
差异词的分布，不是该语料自身的绝对属性。故一切跨条件结论都以
成对方向（第 g 组与其反向组）的复合来陈述，不做跨清单的求并集。
"""
import csv, statistics as st
from collections import Counter, defaultdict

ALL = "coding/all_codes.tsv"
OUT = "coding/final_report.md"
PAIRS = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12)]

rows = list(csv.DictReader(open(ALL, encoding="utf-8"), delimiter="\t"))
for r in rows:
    r["g"] = int(r["group"]); r["ft"] = int(r["freq_tar"]); r["lr"] = float(r["lr"])
G = lambda g: [r for r in rows if r["g"] == g]

out = []; W = out.append


def prop(rs, key, labels):
    """分母＝该层已赋值标签数（NA 不计入）。返回 (计数字典, 分母)。"""
    coded = [r for r in rs if r[key] not in ("NA", "PENDING")]
    return Counter(r[key] for r in coded), len(coded)


W("# 最终编码统计报告")
W("")
W("本报告由 `scripts/final_report.py` 从 `coding/all_codes.tsv` 生成，"
  "反映 concordance 全部消解后的口径。八份 `group*_coding.md` 是编码当时的"
  "过程记录（含彼时的未决理由），其中的占比数字早于本轮消解，以本报告为准。")
W("")

# ── 0 总览 ──
npend = sum(1 for r in rows for L in ("d1", "act", "hedge", "c") if r[L] == "PENDING")
src_rows = [r for r in rows if r["src"] != "-"]
cells = Counter(L for r in src_rows for L in r["src"].split("+"))
W("## 0 数据总览")
W("")
W("| 项目 | 值 |")
W("|---|---:|")
W(f"| 关键词位（12 份成对清单合计） | {len(rows)} |")
W(f"| 唯一词形 | {len({r['type'] for r in rows})} |")
W(f"| 跨组重复出现的词形 | {sum(1 for v in Counter(r['type'] for r in rows).values() if v > 1)} |")
W(f"| 未决单元格 | {npend} |")
W(f"| 经 concordance 定夺的词位 | {len(src_rows)} |")
W(f"| 经 concordance 定夺的单元格 | {sum(cells.values())} |")
W("")
W(f"定夺单元格按层分布：维度一 {cells['d1']}、act 层 {cells['act']}、"
  f"hedge 层 {cells['hedge']}、维度三 {cells['c']}。"
  f"该出处逐层记录于总表 `src` 列，与编码者信度评级 `conf` 分列，互不覆盖。")
W("")

# ── 1 维度一 ──
W("## 1 维度一 Feedback Focus（Straub & Lunsford 1995）")
W("")
W("G1 Global＝Ideas／Development／Global Structure；"
  "G2 Local＝Local Structure／Wording／Correctness（含 Grammar、Mechanics）。")
W("")
W("| 组 | 对比方向 | target | G1 | G2 | 分母 | G2 占比 |")
W("|---:|---|---|---:|---:|---:|---:|")
for g in range(1, 13):
    rs = G(g); c, n = prop(rs, "d1", None)
    W(f"| {g} | {rs[0]['contrast']} | {rs[0]['target_corpus']} | {c['G1']} | {c['G2']} | "
      f"{n} | {c['G2']/n*100:.1f}% |")
W("")

W("### 1.1 六组成对方向")
W("")
W("每对的两组互为反向，比较各自 target 的 G2 占比即得该对比中"
  "「谁的差异词更偏局部」。")
W("")
W("| 对 | 组 | target | G2 占比 | 组 | target | G2 占比 | 更偏局部 | 差距 |")
W("|---:|---:|---|---:|---:|---|---:|---|---:|")
edges = []
for a, b in PAIRS:
    ra, rb = G(a), G(b)
    ca, na = prop(ra, "d1", None); cb, nb = prop(rb, "d1", None)
    pa, pb = ca["G2"]/na*100, cb["G2"]/nb*100
    hi = ra[0]["target_corpus"] if pa > pb else rb[0]["target_corpus"]
    lo = rb[0]["target_corpus"] if pa > pb else ra[0]["target_corpus"]
    edges.append((hi, lo, abs(pa-pb)))
    W(f"| {a}/{b} | {a} | {ra[0]['target_corpus']} | {pa:.1f}% | {b} | "
      f"{rb[0]['target_corpus']} | {pb:.1f}% | **{hi}** | {abs(pa-pb):.1f} pp |")
W("")

W("### 1.2 方向的复合")
W("")
W("把六条方向按「更偏局部」串起来，检查是否存在互相矛盾的回路。")
W("")
for hi, lo, d in edges:
    W(f"- {hi} ＞ {lo}（相差 {d:.1f} pp）")
W("")
# 拓扑排序检验传递性
nodes = {x for e in edges for x in e[:2]}
succ = defaultdict(set)
for hi, lo, _ in edges: succ[hi].add(lo)
order, seen = [], set()
def visit(n, stack):
    if n in stack: return False
    if n in seen: return True
    stack.add(n)
    for m in succ[n]:
        if not visit(m, stack): return False
    stack.discard(n); seen.add(n); order.append(n)
    return True
ok = all(visit(n, set()) for n in nodes)
if ok:
    seq = list(reversed(order))
    W(f"六条方向可复合为一条全序，无回路：**{' ＞ '.join(seq)}**。")
    W("")
    W(f"传递性成立意味着这 {len(seq)} 个条件在「局部化倾向」上可以排成一列，"
      "而不是各对之间各说各话。需要强调的是，这条序来自六次两两对比的复合，"
      "不是把各条件的关键词表并成一张表算出来的——12 份清单各有自己的分母，"
      "跨清单求并集会改变分母的含义。")
else:
    W("六条方向存在回路，无法复合为全序——各对之间的排序互相矛盾。")
W("")

W("### 1.3 子类分布")
W("")
W("| 组 | target | Ideas | Develop. | Global St. | Local St. | Wording | Correct. | Grammar | Mech. |")
W("|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|")
SUBS = ["Ideas", "Development", "Global Structure", "Local Structure",
        "Wording", "Correctness", "Grammar", "Mechanics"]
for g in range(1, 13):
    rs = G(g); c = Counter(r["d1sub"] for r in rs if r["d1"] in ("G1", "G2"))
    W(f"| {g} | {rs[0]['target_corpus']} | " + " | ".join(str(c[s]) for s in SUBS) + " |")
W("")

# ── 2 维度二 ──
W("## 2 维度二 Feedback Acts（Hyland & Hyland 2001）")
W("")
W("两层结构：act 层（A1 Praise／A2 Criticism／A3 Suggestion，至多一个）"
  "与 hedge 层（M1 Hedges，至多一个）并行判定、可共存。两层各自计算分母。")
W("")
W("### 2.1 act 层")
W("")
W("| 组 | target | A1 | A2 | A3 | 分母 | A1% | A2% | A3% |")
W("|---:|---|---:|---:|---:|---:|---:|---:|---:|")
for g in range(1, 13):
    rs = G(g); c, n = prop(rs, "act", None)
    if n:
        W(f"| {g} | {rs[0]['target_corpus']} | {c['A1']} | {c['A2']} | {c['A3']} | {n} | "
          f"{c['A1']/n*100:.1f}% | {c['A2']/n*100:.1f}% | {c['A3']/n*100:.1f}% |")
    else:
        W(f"| {g} | {rs[0]['target_corpus']} | 0 | 0 | 0 | 0 | — | — | — |")
W("")
W("各组 act 层分母普遍偏小（4–45），占比对单个词位的增减敏感，"
  "宜作趋势参考而非精确估计。")
W("")

W("### 2.2 hedge 层")
W("")
W("本层只有 M1 一个非 NA 取值，故「占已定标签」恒为 100%，该比例不含信息；"
  "有意义的是 M1 的**词位数**与**词次**。")
W("")
W("| 组 | target | M1 词位 | M1 词次 | 词形 |")
W("|---:|---|---:|---:|---|")
for g in range(1, 13):
    rs = G(g); m = [r for r in rs if r["hedge"] == "M1"]
    W(f"| {g} | {rs[0]['target_corpus']} | {len(m)} | {sum(r['ft'] for r in m)} | "
      + ("、".join(f"`{r['type']}`" for r in m) if m else "—") + " |")
W("")

W("### 2.3 两层共现")
W("")
co = [r for r in rows if r["act"] != "NA" and r["hedge"] == "M1"]
W(f"全表 act 与 hedge 双标签共现 **{len(co)}** 个词位：")
W("")
if co:
    W("| 组 | target | Type | act | hedge |")
    W("|---:|---|---|---|---|")
    for r in co:
        W(f"| {r['g']} | {r['target_corpus']} | `{r['type']}` | {r['act']} | {r['hedge']} |")
W("")

# ── 3 维度三 ──
W("## 3 维度三 Cross-Linguistic & Identity Framing（窄口径）")
W("")
W("C1 涵盖 Transfer framing（把文本特征归因于母语迁移）与 "
  "Identity marking（点明写作者的语言身份）。依手册规则，C1 项在维度一、"
  "维度二一律归 NA，故 C1 不参与前两个维度的分母。")
W("")
by_corpus = defaultdict(set)
for r in rows:
    if r["c"] == "C1": by_corpus[r["target_corpus"]].add(r["type"])
W("| target corpus | C1 词形数 | 词形 |")
W("|---|---:|---|")
for corp in ["German", "Chinese", "Generic", "L1", "Baseline"]:
    fs = sorted(by_corpus.get(corp, []), key=str.lower)
    W(f"| {corp} | {len(fs)} | " + ("、".join(f"`{f}`" for f in fs) if fs else "（无）") + " |")
W("")
W("| 组 | 对比方向 | target | C1 词位 | C1 词次 |")
W("|---:|---|---|---:|---:|")
for g in range(1, 13):
    rs = G(g); c1 = [r for r in rs if r["c"] == "C1"]
    W(f"| {g} | {rs[0]['contrast']} | {rs[0]['target_corpus']} | {len(c1)} | "
      f"{sum(r['ft'] for r in c1)} |")
W("")

# ── 4 跨语料编码一致性 ──
W("## 4 同词形跨语料的编码差异")
W("")
W("一致性要求施加在「词形 × target corpus」上而非仅「词形」上："
  "concordance 是分语料抽取的，同一词形在不同语料中的主导用法本就可能不同，"
  "这种差异是观察结果，不是编码失误。以下先验证语料内一致，再列出跨语料的分歧。")
W("")
within = defaultdict(list)
for r in rows: within[(r["type"], r["target_corpus"])].append(r)
bad = [(k, v) for k, v in within.items() if len(v) > 1 and
       len({(x["d1"], x["d1sub"], x["act"], x["hedge"], x["c"]) for x in v}) > 1]
W(f"「词形 × 语料」组合 {len(within)} 个，其中跨组重复出现 "
  f"{sum(1 for v in within.values() if len(v) > 1)} 个；"
  f"**语料内编码不一致 {len(bad)} 处**。")
W("")
if bad:
    for (form, corp), v in bad:
        W(f"- `{form}` / {corp}：" + "；".join(
            f"组{x['g']} d1={x['d1']}/{x['d1sub']} act={x['act']} hedge={x['hedge']} c={x['c']}"
            for x in v))
    W("")

byform = defaultdict(list)
for r in rows: byform[r["type"]].append(r)
cross = []
for form, v in byform.items():
    if len({r["target_corpus"] for r in v}) < 2: continue
    sig = {}
    for r in v:
        sig.setdefault(r["target_corpus"], (r["d1"], r["d1sub"], r["act"], r["hedge"], r["c"]))
    if len(set(sig.values())) > 1: cross.append((form, sig))
W(f"跨语料编码不同的词形 **{len(cross)}** 个：")
W("")
W("| 词形 | 语料 | 维度一 | act | hedge | 维度三 |")
W("|---|---|---|---|---|---|")
for form, sig in sorted(cross):
    for i, (corp, (d1, sub, a, h, c)) in enumerate(sorted(sig.items())):
        W(f"| {'`'+form+'`' if i == 0 else ''} | {corp} | "
          f"{d1 + ('/' + sub if sub != '-' else '')} | {a} | {h} | {c} |")
W("")

# ── 5 高效应量 ──
W("## 5 高效应量词位（LR ≥ 1.5）")
W("")
W("| 组 | target | Type | LL | LR | 维度一 | act | hedge | 维度三 |")
W("|---:|---|---|---:|---:|---|---|---|---|")
for r in sorted([r for r in rows if r["lr"] >= 1.5], key=lambda x: -x["lr"]):
    W(f"| {r['g']} | {r['target_corpus']} | {r['type']} | {float(r['ll']):.3f} | {r['lr']:.3f} | "
      f"{r['d1'] + ('/' + r['d1sub'] if r['d1sub'] != '-' else '')} | "
      f"{r['act']} | {r['hedge']} | {r['c']} |")
W("")

# ── 6 信度与出处 ──
W("## 6 信度与判定出处")
W("")
W("`conf` 是编码者对该行标签的信度评级，`src` 记录该行哪些层由 concordance 查证定夺。"
  "两者独立：一个凭手册即可高信度判定的词位 `src` 为空，"
  "一个查过索引行的词位仍可能因语境驳杂而评为低信度。")
W("")
W("| conf | 词位数 | 其中经 concordance 定夺 |")
W("|---|---:|---:|")
for k in ["H", "M", "L", "-"]:
    n = sum(1 for r in rows if r["conf"] == k)
    s = sum(1 for r in rows if r["conf"] == k and r["src"] != "-")
    W(f"| {k if k != '-' else '（未评级）'} | {n} | {s} |")
W("")
low = [r for r in rows if r["conf"] == "L"]
W(f"低信度（conf=L）词位 **{len(low)}** 个，复核时应优先重看：")
W("")
W("| 组 | target | Type | 维度一 | act | 索引定夺 |")
W("|---:|---|---|---|---|---|")
for r in low:
    W(f"| {r['g']} | {r['target_corpus']} | `{r['type']}` | "
      f"{r['d1'] + ('/' + r['d1sub'] if r['d1sub'] != '-' else '')} | {r['act']} | "
      f"{r['src'].replace('+', '、') if r['src'] != '-' else '—'} |")
W("")

# ── 7 研究限制与承重提示 ──
# 本节把八份 group*_coding_resolved.md 的限定条件汇总到一处，使本报告
# 与 all_codes.tsv 两个文件即可支撑后续分析，无须逐组翻阅叙述报告。
W("## 7 研究限制与承重提示")
W("")
W("本节汇总各组叙述报告（`group*_coding_resolved.md`）中的限定条件，"
  "使「本报告 ＋ `all_codes.tsv`」两个文件足以支撑后续分析。"
  "凡引用上文任何占比之前，请先核对本节。")
W("")

W("### 7.1 各层分母：哪些占比可用于数值论证")
W("")
W("判定口径：分母 ≥ 30 可用于数值论证；10–29 仅作方向提示，不得换算百分比作比较；"
  "< 10 不作解读。分母指该层已赋值标签数（NA 不计入）。")
W("")
W("| 组 | target | 维度一 | act 层 | hedge 层 | 维度三 |")
W("|---:|---|---|---|---|---|")


def verdict(n):
    if n == 0:   return "0 ✗"
    if n < 10:   return f"{n} ✗"
    if n < 30:   return f"{n} △"
    return f"{n} ✓"


for g in range(1, 13):
    rs = G(g)
    ns = [len([r for r in rs if r[k] not in ("NA", "PENDING")])
          for k in ("d1", "act", "hedge", "c")]
    W(f"| {g} | {rs[0]['target_corpus']} | " + " | ".join(verdict(n) for n in ns) + " |")
W("")
W("✓ 可用于数值论证　△ 仅作方向提示　✗ 不作解读")
W("")
W("**hedge 层与维度三另有一条独立限制**：两层各自只有一个非 NA 取值"
  "（M1 与 C1），故「占已定标签」恒为 100%，该比例不含任何信息。"
  "这两层只能以**词位数**与**词次**陈述，任何情况下都不得报告其百分比。")
W("")

W("### 7.2 单个词位的权重")
W("")
W("维度一占比对单个词位的敏感度随分母变化，跨组比较 pp 差值时必须同时看分母。")
W("")
W("| 组 | target | 维度一分母 | 1 个词位 = |")
W("|---:|---|---:|---:|")
for g in range(1, 13):
    rs = G(g); n = len([r for r in rs if r["d1"] not in ("NA", "PENDING")])
    W(f"| {g} | {rs[0]['target_corpus']} | {n} | {100/n:.1f} pp |")
W("")
W("举例：组 3 一个词位值 5.3 pp，组 9 只值 1.4 pp。"
  "§1.1 中 11/12 对的 40.9 pp 建立在分母 11 与 14 之上，"
  "与 7/8 对的 61.1 pp（分母各 36）不可等量齐观。"
  "**呈现 §1.2 的全序时应标注各条边的分母。**")
W("")

W("### 7.3 标签成立但证据强度不足的三处")
W("")
W("以下三项的标签本身没有问题，但**若用来承载结论则超出其依据**，"
  "援引前须补查 concordance 或改以定性方式表述。")
W("")
W("| 位置 | 情况 | 风险 |")
W("|---|---|---|")
W("| 组 1 `correctness`（LR 3.284，全组最高） | 编为 G2/Correctness，信度 H，"
  "但 `src` 为空——**零 concordance 支持**，是凭词形判定的 | "
  "它是局部标签却出现在全局倾斜的一侧。"
  "「母语者标记下纠错被降格为次要关切」这一读法很自然，但当前无索引证据。"
  "组 9 的 `correctness`（LR 3.002）同理 |")
W("| 组 11 的五个 A1（`accurate`、`effectively`、`engaging`、`promising`、`balanced`） | "
  "A1 占该组 act 层 62.5%（5/8），为全研究最高；**五项的 act 层全部未经查证** "
  "（`accurate` 只查证了维度一，act 层同样是词形判定） | "
  "存在目标态框架风险（\"make it more engaging\" 是建议而非赞扬）。"
  "补查前不应援引「Baseline 条件下赞扬最多」 |")
W("| 组 7 `MEAN` | concordance 结果为 G2-Wording(50%) / NA(50%) 完全并列，"
  "最终由**编码者裁定**而非索引裁定 | "
  "全研究 351 个定夺单元格中唯一一个索引未能给出主导判定的。"
  "其 `src` 标为 d1，但证据强度弱于其余 350 个 |")
W("")
W("此外，A1 层整体存在**目标态框架**的系统性风险：比较级与「使其更 X」"
  "结构可读作建议（A3）而非赞扬（A1）。经强制查询清单查证的仅 "
  "`strong` 词族、`GOOD`、`strongest`、`strength`、`strengths` 等数项，"
  "其余 A1 为词形判定。若 A1／A3 分界进入论证，应整族补查。")
W("")

W("### 7.4 同词形跨语料编码不同")
W("")
W(f"§4 列出的 {len(cross)} 个词形在不同语料中编码不同。这是观察结果而非编码失误"
  "（concordance 分语料抽取，同一词形的主导用法本就可能因语料而异），"
  "语料内一致性为 0 例外。但**统计时不可按词形合并**——"
  "`check` 在四个语料中有三种维度一判定，合并会抹掉这一结果本身。")
W("")
W("其中一处需单独说明：`INFLUENCE`（组 6，维度三 NA，判定强度 59%）与 "
  "`influenced`（组 7，维度三 C1，判定强度 74%）同族异判。"
  "59% 偏低，建议把 `influenced` 计入 C1、把 `INFLUENCE` 标为边界案例"
  "并披露其判定强度，而非按词族统一处理。")
W("")

W("### 7.5 尚未完成的工作")
W("")
W("| 项目 | 状态 | 影响 |")
W("|---|---|---|")
W(f"| 维度三 C1 子类判定 | **未进行**。`c` 列只有 C1／NA，无子类字段；"
  f"{sum(1 for r in rows if r['c']=='C1')} 个 C1 词位只判到范畴层 | "
  "Identity marking（身份命名）与 Transfer framing（迁移归因）未区分。"
  "这是维度三的理论要害——「把你叫作中文母语者」与「说你的错误来自中文干扰」"
  "是两种不同的 native-speakerism 表现 |")
W("| 组内信度检验（κ） | **未进行**。计划两周后重编 15%（约 134 词位） | "
  "质性编码研究通常要求报告该值，缺失则编码部分方法上不完整 |")
W(f"| 低信度词位复核 | {len(low)} 个 conf=L 项待复核（见 §6） | "
  "其中 `understandable` 横跨组 2／7／10，"
  "「低门槛褒扬是否构成 praise」应统一裁定而非逐组处理 |")
W("| 手册 v3 强制查询清单 | **从未完整获得**，仅用到已知条目"
  "（`address`、`strong` 词族等） | 若完整清单另有条目，需重扫 891 词位 |")
W("")

W("---")
W("")
W("**文件对应关系**：本报告与 `coding/all_codes.tsv` 构成完整的分析基础。"
  "各组的详细论证与逐词讨论见 `coding/group*_coding_resolved.md`（8 份）；"
  "各组完整编码表与 B1–B10 附表见 `coding/group*_tables.md`（12 份）；"
  "二者的全部内容均可由 `all_codes.tsv` 复现。"
  "不带 `_resolved` 的 `group*_coding.md` 是 concordance 消解前的过程存档，"
  "其占比数字已作废。")
W("")

open(OUT, "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"写出 {OUT}（{len(out)} 行）")
print(f"未决单元格 {npend}；concordance 定夺 {len(src_rows)} 词位 / {sum(cells.values())} 单元格")
print(f"语料内不一致 {len(bad)} 处；跨语料编码不同的词形 {len(cross)} 个")
