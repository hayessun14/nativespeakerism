# 组 4 关键词质性分类编码报告
## Generic → Chinese（目标语料 = Generic 条件，参照语料 = Chinese 条件）

> **编码日期**：2026-08-27（第一轮编码）
> **编码方案**：手册 v3　**编码对象集**：本清单全部 30 词位　**占比分母**：各层已定标签数
> **服务的 RQ**：RQ2
> **与组 3 的关系**：组 3 与组 4 是**同一对语料的两个方向**（Chinese 348 篇 ↔ Generic 348 篇）。因此「某词落在哪一侧」可直接对读；占比数值分母不同，不可相减。

> ### ⚠ 分母警告
> 本组 30 词位，各层已定标签：维度一 12、**act 层 2**、hedge 层 1、维度三 0。act 层与 hedge 层**不作解读**。

---

## 一、结果摘要

| 层 | 已定标签 | 分布 | N/A | PENDING |
|---|---:|---|---:|---:|
| 维度一 Focus | 12 | **G1 83.3%**（10）／ G2 16.7%（2） | 15 | 3 |
| 维度二 act | 2 | A3 1（`choose`）／ A2 1（`errors`）／ **A1 0** | 23 | 5 |
| 维度二 hedge | 1 | M1 1（`feels`） | 28 | 1 |
| 维度三 | 0 | **C1 = 0，且 PENDING = 0** | 30 | 0 |

**一句话概括**：本组与组 3 构成一个干净的镜像——同一对语料中，Chinese 侧的过量词汇集中于局部语言形式（G2 10/11），Generic 侧的过量词汇集中于论断层（G1 10/12，其中 Ideas 8 项）；且**全部语言身份材料只出现在 Chinese 一侧**。

---

## 二、维度一：与组 3 构成镜像

| | 组 3（Chinese 侧过量） | 组 4（Generic 侧过量） |
|---|---:|---:|
| G1 | 1（9.1%） | **10（83.3%）** |
| G2 | **10（90.9%）** | 2（16.7%） |
| 已定标签 | 11 | 12 |

由于两组是同一对语料的两个方向，这个镜像不是两个独立结果的巧合，而是**同一分布的两侧读数**。

Generic 侧的 G1 以 Ideas 为主体（8/12，66.7%）：`claims`、`arguments`、`point`、`question`、`raises`、`thought`、`describing`、`impact`。Development 1（`experience`）、Global Structure 1（`section`）。G2 仅 2 项，且都是错误范畴本身（`errors`、`punctuation`）。

敏感性检验（附表 B8）：3 个 PENDING 全归 G2 时 G1 仍占 66.7%，全归 G1 则 86.7%。**方向不翻转**，且区间比组 1／组 2 窄得多（PENDING 只有 3 项）。

将两组的敏感性区间放在一起看：

| | 现状 | 下界 | 上界 |
|---|---:|---:|---:|
| 组 3 G1 占比 | 9.1% | 5.3% | 47.4% |
| 组 4 G1 占比 | 83.3% | 66.7% | 86.7% |

**两组区间不重叠**（组 3 上界 47.4% < 组 4 下界 66.7%）。这与组 1／组 2 的情况不同——那一对的极端边界有重叠区 [56.0, 68.9]，结论尚未被 PENDING 排除。**Chinese ↔ Generic 这一对的焦点差异，在 PENDING 的任何归属下都成立。** 这是目前全研究中稳健性最高的维度一结果。

### 2.1 `describing` 值得单独记一笔

`describing`（Freq_Tar 41，LR 0.864）编为 G1/Ideas，其典型语境是 "describing rather than analysing" 这类描述—分析对举。它落在 **Generic 一侧**，即：相对于被指明母语为中文的写作者，未指明母语的写作者更常被要求从描述走向分析。

这与 Holliday 关于「非西方背景者被叙述为 unable to be critical and self-determined」的论点**方向相反**——若该论点在本数据中成立，分析／批判类要求应更多出现在被具体标记的一侧。此处仅作记录：单个词位、LL 5.384（接近阈值）、且解释框架不参与本阶段编码。组 5–8 编码完成后应回看 `analytical`、`thinking`、`logically`、`describing` 这一组词在各条件的落点。

---

## 三、维度三：本对语料的身份材料是单向的

| | 组 3（Chinese 侧） | 组 4（Generic 侧） |
|---|---|---|
| C1 已定 | 1（`chinese`，LR 5.965） | **0** |
| C1 PENDING | 2（`english`、`language`） | **0** |
| 合计候选材料 | 3 项 / 911 词次 | **0 项** |

组 4 的 30 个词位中，**没有任何一个涉及语言身份或语言系统**——没有 `english`、没有 `language`、没有任何母语名称。

这一点与组 1／组 2 的结果形态一致，但更干净：组 2 的 Generic 侧至少有 4 个 C1 候选（`language`、`english`、`background`、`natural`），因为它的参照系是 L1 条件；而当参照系换成 Chinese 条件时，Generic 侧的身份材料**归零**。

由此得到一个可以直接写进 RQ1／RQ2 的分层陈述：

> 语言身份词汇的密度随「身份被指明的程度」单调上升：L1 条件 0 → Generic 条件（相对 L1）4 项候选 → Chinese 条件（相对 Generic）1 项确定 ＋ 2 项候选。反方向（越不具体的一侧）在每一对中都不产生新的身份材料。

需要说明的限制：这是**词位层面的有无判断**，不是密度的定量比较（各对语料的分母不同）。定量陈述须等 Szczepanik 式的跨条件频率百分比分析（交接文档 §维度三分析路径已规划）。

---

## 四、维度二：不作解读，但记录两件事

### 4.1 A1 = 0 在本对语料的两个方向上同时成立

组 3 A1 = 0，组 4 A1 = 0。也就是说，**Chinese ↔ Generic 这一对语料在赞扬词汇上没有产生任何确定的方向性差异**。

但这个空缺不能直接解读，因为本组 act 层 PENDING 有 5 项，其中 `strongest`（122）、`strength`（92）、`raises`（47）、`essential`（59）全部是潜在 A1。若它们经 concordance 判为 A1，Generic 侧将出现 4 项赞扬词汇而 Chinese 侧仍为 0——那会是一个实质结果。**现在说「两侧赞扬相当」和说「Generic 侧赞扬更多」都没有证据。**

### 4.2 `feels` 是本轮新增的一个 M1

`feels`（110 词次）编为 hedge 层 M1：其典型用法 "this feels abrupt / feels rushed" 与手册 M1 词族例中的 `seem`、`appear` 同类，删除后批评仍然成立且语力更强。

它落在 Generic 一侧。加上组 2 的 5 个 M1 也全部落在 Generic 一侧（相对 L1），目前 M1 的分布形态是：**Generic 条件在两个方向上都是 hedge 的富集侧**。这一点在组 5–8 编码后可以进一步检验（Chinese、German 条件相对彼此是否也富集 hedge）。

---

## 五、发现的一个编码一致性问题（需并案处理）

`raises`（本组）与 `tackles`（组 1，Freq_Tar 66）是**同一种构式**：「your essay raises/tackles an important question」，都出现在反馈开场的归功位置，且归功的语力实际由后随的形容词（important、difficult）承担。

组 1 我将 `tackles` 编为 **A1／信度 M**；本组我将 `raises` 编为 **act PENDING**。两者判定不一致。

我倾向 PENDING 是更正确的处理（该构式本身是描述性的，A1 与否取决于共现修饰语），但**不在本轮单方面改动组 1 的已 commit 编码**——那会破坏 intra-rater 信度所需的第一轮记录。建议的处理是：把 `tackles` 加入 concordance 清单，与 `raises` 并案判定，判定结果一并回填两组，并在修订日志中记录这是「跨组一致性复核」而非「重编码」。

这也说明**跨组一致性检查应作为一道独立工序**，在全部十二组编码完成后统一做一遍，而不是逐组发现逐组改。

---

## 六、数据问题

### 6.1 议题内容残留仅 1 项疑似

`her`（91）——与组 2、组 3 的第三人称代词属同一批疑似残留，待核。本组无确认残留，是目前十二组中最干净的一组。

### 6.2 口径效应的第二个确认实例

`claims` 在本组以**复数独立词位**入选（554），而在组 1 是归并标签 `CLAIM`（claim + claims，1663）。与组 3 的 `word` / `WORD` 同理，系 R1 先行的必然结果。两个实例合并写入方法部分即可。

### 6.3 手册 v3 强制查询清单仍未获得

本组含清单已知条目 `strongest`，已按规则转 PENDING；`strength` 同族且自身具双读法，一并转 PENDING。累计待重扫词位：128 ＋ 131 ＋ 37 ＋ 30 = **326 个**。

---

## 七、下一步

1. **组 5／组 6（Chinese ↔ German）**：RQ2 的决定性一对。需同时处理三件事——组 3 §3.1 的「梯度 vs 特异诊断」两种解释、组 3 §3.2 的母语名称 8 倍差异、以及本组 §4.2 的 hedge 分布形态。
2. **concordance 判定 8 个词族**（附表 B9），并将组 1 的 `tackles` 并入 `raises` 一案。
3. 补齐 v3 强制查询清单，重扫累计 326 个词位。
4. 全部十二组编码完成后，做一道**跨组一致性检查**（见第五节）。

---
## 附表 A：组 4 完整编码表（30 词位，按 LL 降序）

| # | Type | Freq_Tar | LL | LR | 维度一 | 子类 | 维度二 act | 维度二 hedge | 维度三 | 信度 | 判定依据 |
|---:|---|---:|---:|---:|---|---|---|---|---|---|---|
| 1 | emotionally | 63 | 13.009 | 1.136 | PENDING | — | NA | NA | NA | — | 维度一待定：emotionally charged language(G2-Wording/register)vs emotional appeal(G1-Ideas)；同组 2 emotional 口径 |
| 2 | luck | 36 | 9.511 | 1.329 | NA | — | NA | NA | NA | M | 人际礼貌（good luck）；属手册排除的 paired acts 类，不入 M1 |
| 3 | could | 499 | 8.327 | 0.278 | NA | — | PENDING | PENDING | NA | — | 手册指定共享项，抽 50 行分别判 act 层与 hedge 层 |
| 4 | question | 128 | 8.199 | 0.574 | G1 | Ideas | NA | NA | NA | M | the question your essay raises／questions worth addressing，属论断层 |
| 5 | raises | 47 | 7.846 | 0.997 | G1 | Ideas | PENDING | NA | NA | — | act 层待定：raises an important question 属开场归功套语(A1)vs 单纯描述(NA)；与组 1 tackles 同构，须并案处理 |
| 6 | arguments | 163 | 7.607 | 0.482 | G1 | Ideas | NA | NA | NA | H | Ideas 明示 |
| 7 | essential | 59 | 7.514 | 0.849 | NA | — | PENDING | NA | NA | — | act 层待定：an essential point(A1)vs it is essential to…(A3 框架)；同组 2 important 口径 |
| 8 | comment | 57 | 7.201 | 0.845 | NA | — | NA | NA | NA | M | 元话语（a comment on… / 小标题） |
| 9 | choose | 102 | 6.956 | 0.594 | NA | — | A3 | NA | NA | M | choose more precise words，层级由宾语决定 |
| 10 | your | 5416 | 6.839 | 0.073 | NA | — | NA | NA | NA | M | 人称代词，无固定层级所指 |
| 11 | feels | 110 | 6.693 | 0.558 | NA | — | NA | M1 | NA | M | this feels abrupt/rushed：与手册 M1 词族例 seem/appear 同类；删除后批评仍在且更强 |
| 12 | errors | 317 | 6.680 | 0.315 | G2 | Correctness | A2 | NA | NA | H | 手册边界规则明示：error/mistake 归 G2-Correctness 且同时得批评标签 |
| 13 | impact | 102 | 6.506 | 0.573 | G1 | Ideas | NA | NA | NA | M | the impact of your argument on the reader；受众/效果，依窄口径归 G1 |
| 14 | makes | 216 | 6.250 | 0.372 | NA | — | NA | NA | NA | M | 轻动词 |
| 15 | find | 52 | 6.094 | 0.809 | NA | — | NA | NA | NA | M | I find… / readers may find…＝人称归因，属手册排除的缓和策略，不入 M1 |
| 16 | experience | 105 | 5.839 | 0.531 | G1 | Development | NA | NA | NA | M | personal experience 作为证据类型，与组 1 anecdote 同位 |
| 17 | thought | 73 | 5.564 | 0.632 | G1 | Ideas | NA | NA | NA | M | your thought process／well-thought-out |
| 18 | paper | 100 | 5.407 | 0.523 | NA | — | NA | NA | NA | H | 文本指称语，不指示层级 |
| 19 | describing | 41 | 5.384 | 0.864 | G1 | Ideas | NA | NA | NA | M | describing rather than analysing，描述—分析对举，属论述方式 |
| 20 | final | 414 | 5.116 | 0.238 | PENDING | — | NA | NA | NA | — | 维度一待定：your final paragraph(G1-Structure)vs"Final thoughts:"小标题(NA) |
| 21 | punctuation | 238 | 5.001 | 0.314 | G2 | Mechanics | NA | NA | NA | H | Mechanics 明示 |
| 22 | her | 91 | 4.485 | 0.497 | NA | — | NA | NA | NA | M | 疑似议题内容残留（引述作文内容），待核 |
| 23 | strongest | 122 | 4.439 | 0.421 | NA | — | PENDING | NA | NA | — | 手册 v3 强制查询清单（strong 系 A1/A3 争议），不得凭词形归类 |
| 24 | strength | 92 | 4.419 | 0.490 | NA | — | PENDING | NA | NA | — | act 层待定：反馈小标题"Strengths:"（元话语 NA）vs 归功（A1）；且属 strong 词族，按 v3 强制查询规则不得凭词形定 |
| 25 | key | 88 | 4.308 | 0.495 | NA | — | NA | NA | NA | M | 重要性前置修饰语（your key claim），少见于 it is key to… 框架，故与 essential/important 不同判 |
| 26 | point | 431 | 4.198 | 0.210 | G1 | Ideas | NA | NA | NA | H | 手册 Ideas 词族例明列 point |
| 27 | moves | 79 | 4.160 | 0.515 | PENDING | — | NA | NA | NA | — | 维度一待定：the essay moves from X to Y(G1-Structure)vs move this paragraph(元话语/G1)；同组 1 move 口径 |
| 28 | claims | 554 | 3.970 | 0.179 | G1 | Ideas | NA | NA | NA | H | Ideas 明示。注：本组为复数 claims 独立入选（组 1 为归并 CLAIM），系 R1 先行的口径效应 |
| 29 | several | 487 | 3.915 | 0.190 | NA | — | NA | NA | NA | M | 量词 |
| 30 | section | 114 | 3.888 | 0.407 | G1 | Global Structure | NA | NA | NA | M | 大于段落的单位 |

### B1 维度一 Feedback Focus

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| G1 | 10 | 83.3% | 1758 | 76.0% | 0.545 |
| G2 | 2 | 16.7% | 555 | 24.0% | 0.315 |
| **已定标签合计** | **12** | **100.0%** | **2313** | **100.0%** | — |
| N/A（不计入分母） | 15 | — | — | — | — |
| PENDING（不计入分母） | 3 | — | — | — | — |
| 清单总数 | 30 | — | — | — | — |

**子类分布（分母同为已定标签 12）**

| 主类 | 子类 | 词位数 | 占比 |
|---|---|---:|---:|
| G1 | Development | 1 | 8.3% |
| G1 | Global Structure | 1 | 8.3% |
| G1 | Ideas | 8 | 66.7% |
| G2 | Correctness | 1 | 8.3% |
| G2 | Mechanics | 1 | 8.3% |

### B2 维度二 · act 层（A1 Praise / A2 Criticism / A3 Suggestion）

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| A3 | 1 | 50.0% | 102 | 24.3% | 0.594 |
| A2 | 1 | 50.0% | 317 | 75.7% | 0.315 |
| **已定标签合计** | **2** | **100.0%** | **419** | **100.0%** | — |
| N/A（不计入分母） | 23 | — | — | — | — |
| PENDING（不计入分母） | 5 | — | — | — | — |
| 清单总数 | 30 | — | — | — | — |

### B3 维度二 · hedge 层（M1 Hedges）

hedge 层与 act 层并行判定、可共存（Hyland & Hyland：hedge 施加于 act 之上）。分母为本层已定标签数。

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| M1 | 1 | 100.0% | 110 | 100.0% | 0.558 |
| **已定标签合计** | **1** | **100.0%** | **110** | **100.0%** | — |
| N/A（不计入分母） | 28 | — | — | — | — |
| PENDING（不计入分母） | 1 | — | — | — | — |
| 清单总数 | 30 | — | — | — | — |

### B4 维度三 Larger Contexts of Writing

**已定标签 0 项** —— 本层无任何词位获得标签，占比不适用（分母为 0）。

| 标签 | 词位数 | Freq_Tar 合计 |
|---|---:|---:|
| 已定标签合计 | 0 | 0 |
| N/A（不计入分母） | 30 | — |
| PENDING（不计入分母） | 0 | — |
| 清单总数 | 30 | — |

### B5 维度二两层共现（词位数）

| act ＼ hedge | M1 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|
| **A1** | 0 | 0 | 0 | **0** |
| **A2** | 0 | 1 | 0 | **1** |
| **A3** | 0 | 1 | 0 | **1** |
| **NA** | 1 | 22 | 0 | **23** |
| **PENDING** | 0 | 4 | 1 | **5** |
| **合计** | 1 | 28 | 1 | **30** |

act ＋ hedge 双标签共现：**0** 项

### B6 维度一 × 维度二 act 层 交叉表（词位数）

| 维度一＼act | A1 | A2 | A3 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|---:|---:|
| **G1** | 0 | 0 | 0 | 9 | 1 | **10** |
| **G2** | 0 | 1 | 0 | 1 | 0 | **2** |
| **NA** | 0 | 0 | 1 | 10 | 4 | **15** |
| **PENDING** | 0 | 0 | 0 | 3 | 0 | **3** |
| **合计** | 0 | 1 | 1 | 23 | 5 | **30** |

### B7 LL 前 20 词位的维度一构成

| | G1 | G2 | N/A | PENDING |
|---|---:|---:|---:|---:|
| 词位数 | 7 | 1 | 10 | 2 |

### B8 敏感性分析：维度一 PENDING 的极端归属

| 情形 | G1 词位 | G2 词位 | G1 占比 |
|---|---:|---:|---:|
| 现状（PENDING 不计入） | 10 | 2 | 83.3% |
| 3 个 PENDING 全归 G1（上界） | 13 | 2 | 86.7% |
| 3 个 PENDING 全归 G2（下界） | 10 | 5 | 66.7% |

### B9 concordance 待办清单

共 **8** 个词族需 concordance 判定（含 2 个低信度已定项）。

| Type | Freq_Tar | 待定层 | 竞争读法 |
|---|---:|---|---|
| `emotionally` | 63 | 维度一 | 维度一待定：emotionally charged language(G2-Wording/register)vs emotional appeal(G1-Ideas)；同组 2 emotional 口径 |
| `could` | 499 | act、hedge | 手册指定共享项，抽 50 行分别判 act 层与 hedge 层 |
| `raises` | 47 | act | act 层待定：raises an important question 属开场归功套语(A1)vs 单纯描述(NA)；与组 1 tackles 同构，须并案处理 |
| `essential` | 59 | act | act 层待定：an essential point(A1)vs it is essential to…(A3 框架)；同组 2 important 口径 |
| `final` | 414 | 维度一 | 维度一待定：your final paragraph(G1-Structure)vs"Final thoughts:"小标题(NA) |
| `strongest` | 122 | act | 手册 v3 强制查询清单（strong 系 A1/A3 争议），不得凭词形归类 |
| `strength` | 92 | act | act 层待定：反馈小标题"Strengths:"（元话语 NA）vs 归功（A1）；且属 strong 词族，按 v3 强制查询规则不得凭词形定 |
| `moves` | 79 | 维度一 | 维度一待定：the essay moves from X to Y(G1-Structure)vs move this paragraph(元话语/G1)；同组 1 move 口径 |

### B10 高效应量词位（LR ≥ 1.5）

| Type | LL | LR | 维度一 | act | hedge |
|---|---:|---:|---|---|---|
