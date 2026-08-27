# 组 9／组 10 关键词质性分类编码报告
## Baseline ↔ Generic（RQ3 第一对）

> **编码日期**：2026-08-27（第一轮编码）
> **编码方案**：手册 v3　**编码对象集**：组 9 全部 131 词位、组 10 全部 121 词位　**占比分母**：各层已定标签数
> **服务的 RQ**：RQ3——无标记 baseline 条件的关键词分布更接近 L1 还是 L2

> ### ⚠ 关于编码复用的方法说明（务必先读）
> 组 9 有 **91／131** 个词位、组 10 有 **101／121** 个词位在前八组中已出现过同一词形，本轮**直接沿用其既有编码**（note 字段以〔沿用组 N〕标注），仅对新出现的 39 项与 20 项作新编码。
>
> 这样做保证了跨组一致性，但**必须明确它对推论的限制**：既然相同词形被赋予相同标签，两张清单的类别分布在很大程度上是由「清单共享哪些词」决定的，而非由编码判断独立决定。因此——
>
> **本报告 RQ3 结论的主要证据是清单重合度统计（§2），那是编码之前就已确定的事实；编码分布（§3）与之一致，但不构成独立证据。** 两者不可当作两条独立线索相互印证。

---

## 一、结果摘要

| 层 | 组 9（Baseline 侧过量） | 组 10（Generic 侧过量） |
|---|---|---|
| 维度一 | 已定 52：**G1 44（84.6%）**／ G2 8（15.4%） | 已定 31：**G2 22（71.0%）**／ G1 9（29.0%） |
| 维度二 act | 已定 29：A3 16／A2 9／A1 4 | 已定 16：A3 9／A2 5／A1 2 |
| 维度二 hedge | 已定 4：`fairly`、`risk`、`somewhat`、`likely` | 已定 4：`slightly`、`some`、`probably`、`usually` |
| 维度三 | **C1 0，PENDING 0** | C1 0，PENDING 4（`language`、`english`、`natural`、`direct`） |
| N/A ／ PENDING（维度一） | 57 ／ 22 | 65 ／ 25 |

敏感性区间：组 9 的 G1 占比 [59.5%, 89.2%]，组 10 [16.1%, 60.7%]。重叠区仅 [59.5%, 60.7%]——比组 1／组 2 的 [56.0, 68.9] 窄得多，接近不重叠。

---

## 二、主要证据：清单重合度（编码之前的事实）

### 2.1 以 Generic 为参照的四张清单

四个条件各自相对 Generic 产出一张清单（组 1 L1、组 3 Chinese、组 7 German、组 9 Baseline）。若 Baseline 更像某一侧，它的清单应与那一侧的清单共享更多词形。

| 重合率 | L1 | Chinese | German | Baseline |
|---|---:|---:|---:|---:|
| **L1**（128） | — | 1% | 3% | **47%** |
| **Chinese**（37） | 1% | — | 11% | 2% |
| **German**（77） | 3% | 11% | — | 3% |
| **Baseline**（131） | **47%** | 2% | 3% | — |

（重合数／两清单并集；对角线为清单规模）

### 2.2 以 Generic 为目标的四张清单

| 重合率 | vs L1 | vs Chinese | vs German | vs Baseline |
|---|---:|---:|---:|---:|
| **vs L1**（131） | — | 5% | 7% | **56%** |
| **vs Chinese**（30） | 5% | — | 7% | 3% |
| **vs German**（65） | 7% | 7% | — | 6% |
| **vs Baseline**（121） | **56%** | 3% | 6% | — |

### 2.3 这两张表为什么是干净的证据

关键在于**对照本身内建在表里**。如果「凡是以 Generic 为参照的清单都彼此相像」，那么表中所有格子都会偏高，Baseline–L1 的 47% 就不说明问题。实际情况是：除 Baseline–L1 一格外，其余五格全部落在 1%–11% 区间。**Baseline 与 L1 的重合度是任何其他配对的 4–47 倍。** 目标侧的表（56% vs 3%–7%）形态相同。

### 2.4 清单规模的旁证

| 语料对 | 两方向关键词总数 |
|---|---:|
| L1 ↔ Generic | 259 |
| Baseline ↔ Generic | 252 |
| German ↔ Generic | 142 |
| Chinese ↔ German | 115 |
| Chinese ↔ Generic | 67 |
| **Baseline ↔ L1** | **56** |

Baseline 与 L1 直接对比时，通过 R1／R2 筛选的关键词只有 56 个——是 Baseline↔Generic（252）的约五分之一，也是全部六对语料中最少的一对。**两个条件在关键词层面几乎难以区分。**（组 11／组 12 的编码将直接检验这 56 个词的性质。）

**RQ3 的答案**：无标记 baseline 条件的关键词分布**明确更接近 L1 条件**，而非任何 L2 条件。

---

## 三、编码分布（与 §2 一致，但非独立证据）

### 3.1 维度一：组 9 复制了组 1 的形态

| | 组 1（L1 vs Generic） | 组 9（Baseline vs Generic） |
|---|---:|---:|
| G1 占比 | 80.8%（42/52） | **84.6%（44/52）** |
| G2 词位 | 10 | 8 |
| **G2 中的 Grammar 子类** | **0** | **0** |

| | 组 2（Generic vs L1） | 组 10（Generic vs Baseline） |
|---|---:|---:|
| G2 占比 | 52.8%（19/36） | **71.0%（22/31）** |
| **G2 中的 Grammar 子类** | **6** | **7** |

组 9 的 G2 八项是 `correctness`、`PROOFREAD`、`mechanical`、`mechanics`、`typos`、`prose`、`phrasing`、`cut`——**全部是范畴元标签、机械层面与措辞，没有一项是具体语法范畴**。组 10 的 Grammar 七项是 `grammar`、`tense`、`verb`、`past`、`form`、`plural`、`agreement`。

这与组 1／组 2 的形态完全一致，包括组 1 报告第二节提出的那个「元标签 vs 具体纠正」的分野。换言之，**无标记条件在这一点上的表现与被标记为母语者的条件无法区分**。

### 3.2 维度三：Baseline 侧连候选材料都没有

组 9 的 131 个词位中，**C1 已定 0、待定 0**——比组 1 更干净（组 1 尚有 `cultural` 一项待定，且很可能是议题残留）。

组 10 的四项待定（`language`、`english`、`natural`、`direct`）与组 2 的四项（`language`、`english`、`background`、`natural`）高度重叠。也就是说，**当参照系从 L1 换成 Baseline 时，Generic 侧浮现的身份候选词几乎是同一批**。

至此维度三的完整形态（十组已编码）：

| 条件 | 确定 C1 | 说明 |
|---|---|---|
| L1 | 0 | 相对 Generic 无候选（唯一待定项疑为议题残留） |
| **Baseline** | **0** | **相对 Generic 连待定项都没有** |
| Generic | 0 | 仅相对 L1／Baseline 有候选；相对 Chinese／German 归零 |
| Chinese | 1 | `chinese` |
| German | 3 | `german`、`SPEAKER`、`transfer` |

### 3.3 hedge 层

组 9 与组 10 各 4 项 M1，词位数持平。这与组 1／组 2 的强不对称（2 : 5，123 : 1608 词次）**不同**——但两组的 hedge PENDING 分别为 4 项与 3 项，且 `some`（组 10，939 词次）单词即可主导词次口径。**本对的 hedge 结论待 concordance，现阶段不作方向判断**（教训见组 5／组 6 报告 §4.2 的更正）。

### 3.4 act 层

组 9 已定 29 项，是十组中最多的一组；A3 16／A2 9／A1 4。组 10 为 A3 9／A2 5／A1 2。两组的 A1 仍然稀少，且 act 层 PENDING 各 13 项，其中含 `GOOD`、`strong`、`strengths`、`strongest`、`address`、`tackles` 等高体量或强制查询词。**act 层仍不作跨组解读。**

---

## 四、本轮的两处编码处置

### 4.1 `tackles` 未沿用组 1 的 A1，改判 PENDING

组 4 报告 §5 已指出：`tackles`（组 1，编为 A1／M）与 `raises`（组 4，编为 PENDING）是同一构式，判定不一致，且我认为 PENDING 才是正确处理。

本轮组 9 再次出现 `tackles`。**沿用组 1 的 A1 等于把一个我已认定有问题的编码复制出去**，因此本组单独改判为 act PENDING，并在 note 中写明。**组 1 的编码不作追溯改动**——第一轮记录是 intra-rater 信度的基准，须保持原样；两组的差异留待十二组完成后的跨组一致性检查统一回填，并在修订日志中记为「跨组一致性复核」。

这是本研究中第一处**有意保留的跨组编码不一致**，须在方法部分说明其理由，而不是当作疏漏。

### 4.2 口径效应实例增至六个

本轮新增四例：`use`（组 10）vs 归并 `USE`（组 2）；`strengths`（组 10）vs 归并 `STRENGTH`（组 2）；归并 `SENTENCE`（组 10）vs `sentences`（组 2）；`gives`（组 9）vs 归并 `GIVE`（组 1）。加上此前的 `word`／`WORD`、`claims`／`CLAIM`，共六例。

其中 `use`／`USE` 正是交接文档 §三「已知口径效应」段落所举的原例。建议方法部分直接引用该例并附本表，说明这是 R1 先行于 R4 的必然结果。

---

## 五、数据问题

### 5.1 议题内容残留

组 9：确认 5 项（`public`、`policy`、`economic`、`historical`、`treatment`）＋ 疑似 2 项（`studies`、`dates`）。
组 10：确认 3 项（`society`、`women`、`students`）＋ 疑似 5 项（`people`、`she`、`he`、`her`、`story`）。

组 10 的第三人称代词群（`she`、`he`、`her`）与组 2、组 3、组 4 的同类疑似项属同一批，**建议一次性 concordance 判定后统一处理**，不要逐组单判。

### 5.2 手册 v3 强制查询清单仍未获得

组 9 含 `address`、`strongest`、`STRENGTHEN`；组 10 含 `strong`、`strengths`。累计待重扫词位：583 ＋ 131 ＋ 121 = **835 个**。

---

## 六、下一步

1. **组 11／组 12（Baseline ↔ L1）**：RQ3 的另一对，也是本报告 §2.4 那 56 个词的直接检验。若这 56 个词在三个维度上都不构成系统性差异，RQ3 的结论即告闭合。
2. concordance 优先级不变（`false` 右搭配 → `natural`／`unnatural`／`sounds` → `chinese` 子类 → 内容动词统一规则）。
3. 十二组完成后执行跨组一致性检查，统一回填 `tackles`／`raises`。
4. 补齐 v3 强制查询清单，重扫累计 835 个词位。

---

# 附表：组 9（Baseline → Generic）

## 附表 A：组 9 完整编码表（131 词位，按 LL 降序）

| # | Type | Freq_Tar | LL | LR | 维度一 | 子类 | 维度二 act | 维度二 hedge | 维度三 | 信度 | 判定依据 |
|---:|---|---:|---:|---:|---|---|---|---|---|---|---|
| 1 | paper | 265 | 74.303 | 1.379 | NA | — | NA | NA | NA | H | 文本指称语，不指示层级〔沿用组 1〕 |
| 2 | CLAIM | 1689 | 70.689 | 0.453 | G1 | Ideas | NA | NA | NA | H | 论断/主张名词，Ideas 明示；本身中性，act 层不赋值〔沿用组 1〕 |
| 3 | SHARPEN | 143 | 42.460 | 1.432 | G1 | Ideas | A3 | NA | NA | M | 主导搭配 sharpen your claim/thesis/argument〔沿用组 1〕 |
| 4 | rather | 784 | 38.880 | 0.497 | NA | — | NA | PENDING | NA | — | M1待定：手册列为 hedge，但"rather than"（建议对比框架）可能占主导〔沿用组 1〕 |
| 5 | correctness | 49 | 37.529 | 3.002 | G2 | Correctness | NA | NA | NA | H | 直接命名 Correctness 焦点〔沿用组 1〕 |
| 6 | evidence | 1543 | 31.423 | 0.308 | G1 | Development | NA | NA | NA | H | Development 核心〔沿用组 1〕 |
| 7 | COUNTERARGUMENT | 409 | 26.547 | 0.577 | G1 | Ideas | NA | NA | NA | H | Ideas 明示（counterargument） |
| 8 | RELY | 132 | 25.417 | 1.086 | G1 | Development | NA | NA | NA | M | rely on evidence/sources〔沿用组 1〕 |
| 9 | distract | 66 | 25.073 | 1.695 | PENDING | — | A2 | NA | NA | — | 维度一待定：typos distract(G2)vs digression distracts(G1)〔沿用组 1〕 |
| 10 | prose | 52 | 24.323 | 1.973 | G2 | Wording | NA | NA | NA | M | 主导搭配 tighten/clarify your prose，句级文风〔沿用组 1〕 |
| 11 | instance | 185 | 24.161 | 0.860 | NA | — | NA | NA | NA | M | 主导为"for instance"元话语（反馈自身举例，非要求学生举例）〔沿用组 1〕 |
| 12 | concerns | 110 | 23.836 | 1.169 | NA | — | A2 | NA | NA | M | my main concerns are…，批评标记语〔沿用组 1〕 |
| 13 | address | 302 | 23.654 | 0.641 | PENDING | — | PENDING | NA | NA | — | 手册 v3 强制查询清单（G1/A3 争议），不得凭词形归类：address counterarguments(G1+A3) vs 元话语"address the points below"(NA)〔沿用组 1〕 |
| 14 | STRENGTHEN | 525 | 23.078 | 0.466 | G1 | Ideas | A3 | NA | NA | M | strengthen your argument/thesis；Ideas/Development 子类边界待核〔沿用组 1〕 |
| 15 | PROOFREAD | 340 | 21.894 | 0.575 | G2 | Correctness | A3 | NA | NA | H | 校对行动，Correctness+建议〔沿用组 1〕 |
| 16 | credible | 130 | 21.677 | 0.995 | G1 | Development | A1 | NA | NA | M | credible sources/evidence〔沿用组 1〕 |
| 17 | arguable | 96 | 20.695 | 1.165 | G1 | Ideas | A1 | NA | NA | M | an arguable thesis，域固定于论断〔沿用组 1〕 |
| 18 | NEED | 1043 | 20.460 | 0.302 | NA | — | A3 | NA | NA | H | need to = Hyland&Hyland 明示建议套语〔沿用组 1〕 |
| 19 | reasoning | 267 | 20.407 | 0.632 | G1 | Ideas | NA | NA | NA | H | Ideas 定义明示 lines of thought and reasoning〔沿用组 1〕 |
| 20 | aim | 67 | 20.345 | 1.454 | G1 | Ideas | PENDING | NA | NA | — | act 层待定："aim to/for"（A3）vs "your aim"（名词，NA）〔沿用组 1〕 |
| 21 | anecdote | 111 | 19.038 | 1.012 | G1 | Development | NA | NA | NA | H | 证据类型〔沿用组 1〕 |
| 22 | gives | 287 | 18.960 | 0.583 | NA | — | NA | NA | NA | M | 无固定层级所指。注：组 1 为归并 GIVE（gives+given），本组为 gives 单独入选，系 R1 先行的口径效应 |
| 23 | fairly | 84 | 18.849 | 1.195 | NA | — | NA | M1 | NA | H | 手册 v3 M1 明示 hedge〔沿用组 1〕 |
| 24 | mechanical | 60 | 18.848 | 1.487 | G2 | Mechanics | NA | NA | NA | H | mechanical errors〔沿用组 1〕 |
| 25 | even | 241 | 18.686 | 0.637 | NA | — | NA | NA | NA | H | 焦点副词，非 hedge〔沿用组 1〕 |
| 26 | reads | 188 | 18.055 | 0.720 | PENDING | — | NA | NA | NA | — | 维度一待定：the essay reads(整体)vs this sentence reads(句级)〔沿用组 1〕 |
| 27 | actual | 206 | 17.986 | 0.682 | NA | — | NA | NA | NA | M | 对比性强调词〔沿用组 1〕 |
| 28 | credibility | 251 | 17.687 | 0.604 | G1 | Development | NA | NA | NA | M | 与 credible 同域〔沿用组 1〕 |
| 29 | just | 271 | 17.246 | 0.571 | NA | — | NA | PENDING | NA | — | M1待定：最小化降调(M1)vs"仅仅是"强化批评(NA)；竞争读法全在 hedge 层，与 act 层无关〔沿用组 1〕 |
| 30 | might | 189 | 16.823 | 0.689 | NA | — | PENDING | PENDING | NA | — | 手册指定共享项〔沿用组 1〕 |
| 31 | BUILD | 126 | 16.527 | 0.862 | G1 | Ideas | NA | NA | NA | M | building on/building your argument；沿用组 1 building 口径 |
| 32 | complexity | 61 | 15.963 | 1.318 | G1 | Ideas | NA | NA | NA | M | acknowledge the complexity of the issue〔沿用组 1〕 |
| 33 | would | 739 | 15.873 | 0.317 | NA | — | PENDING | PENDING | NA | — | 手册指定共享项，concordance 抽 50 行判 A3/M1〔沿用组 1〕 |
| 34 | arguing | 102 | 15.598 | 0.945 | G1 | Ideas | NA | NA | NA | H | Ideas 明示 arguments〔沿用组 1〕 |
| 35 | ASSERTION | 99 | 15.503 | 0.958 | G1 | Ideas | NA | NA | NA | H | Ideas 明示；沿用组 1 assertion 口径 |
| 36 | analysis | 322 | 14.778 | 0.477 | G1 | Ideas | NA | NA | NA | H | Ideas 明示 analysis〔沿用组 1〕 |
| 37 | tackles | 82 | 13.974 | 1.008 | NA | — | PENDING | NA | NA | — | act 层待定：your essay tackles a difficult question 属开场归功套语(A1)vs 描述(NA)。与组 4 raises 并案；组 1 的 A1 编码不追溯改动，留待跨组一致性检查统一回填 |
| 38 | EDIT | 164 | 13.953 | 0.672 | PENDING | — | A3 | NA | NA | — | 维度一待定：表层编辑(G2)vs 全局修改(G1)；沿用组 1 edit 口径 |
| 39 | matters | 168 | 13.002 | 0.637 | G1 | Ideas | NA | NA | NA | M | why this matters，论点意义；沿用组 1 MATTER 口径 |
| 40 | authority | 58 | 12.871 | 1.187 | G1 | Ideas | NA | NA | NA | L | 写作者论述权威/立场，归修辞语境→G1〔沿用组 1〕 |
| 41 | BROAD | 288 | 12.516 | 0.463 | G1 | Ideas | NA | NA | NA | M | broad/broader context 与 implications；沿用组 1 broader 口径 |
| 42 | promising | 51 | 12.326 | 1.253 | NA | — | A1 | NA | NA | M | a promising start，正向评价；目标态框架风险 |
| 43 | sweeping | 46 | 12.148 | 1.326 | G1 | Ideas | A2 | NA | NA | H | sweeping generalization，域固定于论断〔沿用组 1〕 |
| 44 | effectively | 120 | 11.801 | 0.730 | NA | — | A1 | NA | NA | M | effectively argues／effectively supports，方式副词但携正向评价；与组 2 effective 同族，目标态框架风险 |
| 45 | phrasing | 198 | 10.828 | 0.525 | G2 | Wording | NA | NA | NA | H | Wording 明示〔沿用组 1〕 |
| 46 | takes | 44 | 10.759 | 1.262 | NA | — | NA | NA | NA | M | 轻动词〔沿用组 1〕 |
| 47 | distinct | 83 | 10.744 | 0.856 | G1 | Ideas | NA | NA | NA | M | distinct points/ideas〔沿用组 1〕 |
| 48 | should | 1313 | 10.233 | 0.187 | NA | — | A3 | NA | NA | H | Hyland&Hyland 明示建议套语〔沿用组 1〕 |
| 49 | kind | 90 | 10.202 | 0.792 | NA | — | NA | NA | NA | M | the kind of evidence／this kind of claim，类指名词 |
| 50 | opening | 198 | 10.045 | 0.504 | G1 | Global Structure | NA | NA | NA | H | 引言段，大单位〔沿用组 1〕 |
| 51 | currently | 246 | 10.038 | 0.447 | NA | — | NA | NA | NA | M | 元话语对比框架（现状→建议），本身非行为〔沿用组 1〕 |
| 52 | level | 248 | 9.932 | 0.443 | PENDING | — | NA | NA | NA | — | 维度一待定：sentence-level(G2)/paragraph-level(G1)/level of detail(G1-Dev)〔沿用组 1〕 |
| 53 | revise | 477 | 9.697 | 0.308 | NA | — | A3 | NA | NA | H | 手册 A3 明示〔沿用组 5〕 |
| 54 | asserted | 57 | 9.553 | 0.998 | G1 | Ideas | NA | NA | NA | H | Ideas 明示；沿用组 1 ASSERT 口径 |
| 55 | narrow | 54 | 9.486 | 1.027 | G1 | Ideas | PENDING | NA | NA | — | 与本组 BROAD 构成论断范围对举，域固定于论断；act 层待定：narrow your claim(A3)vs too narrow(A2) |
| 56 | tension | 59 | 9.082 | 0.948 | G1 | Ideas | NA | NA | NA | M | a tension in your argument，论证内部张力 |
| 57 | improving | 70 | 9.028 | 0.854 | NA | — | A3 | NA | NA | M | 改进指向，层级由宾语决定〔沿用组 1〕 |
| 58 | public | 281 | 9.004 | 0.393 | NA | — | NA | NA | NA | H | 议题内容残留（LOCNESS 主题词）〔沿用组 1〕 |
| 59 | contains | 50 | 8.846 | 1.031 | NA | — | NA | NA | NA | H | 描述性动词〔沿用组 1〕 |
| 60 | strongest | 176 | 8.843 | 0.501 | NA | — | PENDING | NA | NA | — | 手册 v3 强制查询清单（strong 系 A1/A3 争议），不得凭词形归类：your strongest evidence(A1) vs 目标态框架(A3)〔沿用组 1〕 |
| 61 | observations | 41 | 8.777 | 1.160 | NA | — | NA | NA | NA | M | 元话语（a few observations），与组 6/7 notes 同簇 |
| 62 | mechanics | 186 | 8.578 | 0.478 | G2 | Mechanics | NA | NA | NA | H | Mechanics 明示〔沿用组 1〕 |
| 63 | clarify | 212 | 8.494 | 0.443 | PENDING | — | A3 | NA | NA | — | 维度一待定（手册 clear 系）；建议动词〔沿用组 8〕 |
| 64 | heavily | 55 | 8.440 | 0.947 | NA | — | NA | NA | NA | M | 强化词（rely heavily），非 hedge〔沿用组 1〕 |
| 65 | entirely | 52 | 8.348 | 0.973 | NA | — | NA | NA | NA | M | 强化词；"not entirely"否定缓和待观察〔沿用组 1〕 |
| 66 | engage | 44 | 7.886 | 1.040 | G1 | Ideas | A3 | NA | NA | M | engage with counterarguments/the reader〔沿用组 1〕 |
| 67 | readers | 337 | 7.804 | 0.330 | G1 | Ideas | NA | NA | NA | M | 受众；按窄口径 C1 规定归 G1〔沿用组 1〕 |
| 68 | making | 152 | 7.776 | 0.506 | NA | — | NA | NA | NA | H | 轻动词〔沿用组 1〕 |
| 69 | argument | 1966 | 7.770 | 0.131 | G1 | Ideas | NA | NA | NA | H | Ideas 明示〔沿用组 8〕 |
| 70 | framing | 55 | 7.695 | 0.896 | G1 | Ideas | NA | NA | NA | M | 论点呈现方式〔沿用组 1〕 |
| 71 | right | 538 | 7.694 | 0.256 | PENDING | — | NA | NA | NA | — | 维度一待定：the right word(G2)vs right now(NA)〔沿用组 1〕 |
| 72 | policy | 144 | 7.550 | 0.513 | NA | — | NA | NA | NA | H | 议题内容残留〔沿用组 1〕 |
| 73 | economic | 93 | 7.536 | 0.654 | NA | — | NA | NA | NA | H | 议题内容残留 |
| 74 | organizing | 90 | 7.359 | 0.657 | G1 | Global Structure | NA | NA | NA | H | Global Structure 明示〔沿用组 5〕 |
| 75 | reorganize | 101 | 7.201 | 0.608 | G1 | Global Structure | A3 | NA | NA | H | 大单位重排，Global Structure 明示〔沿用组 1〕 |
| 76 | treatment | 70 | 7.125 | 0.744 | PENDING | — | NA | NA | NA | — | 维度一待定：your treatment of the topic(G1-Ideas)vs 议题内容残留，待核 |
| 77 | precisely | 41 | 6.986 | 1.008 | NA | — | NA | NA | NA | M | 方式副词〔沿用组 1〕 |
| 78 | sharper | 59 | 6.963 | 0.811 | NA | — | PENDING | NA | NA | — | act 层待定：比较级多嵌于目标态框架（make it sharper=A3）而非评价（A1）〔沿用组 1〕 |
| 79 | replace | 167 | 6.866 | 0.449 | PENDING | — | A3 | NA | NA | — | 维度一待定：replace this word(G2)vs replace this paragraph(G1)〔沿用组 1〕 |
| 80 | material | 126 | 6.853 | 0.524 | G1 | Development | NA | NA | NA | M | source material，属支撑材料〔沿用组 1〕 |
| 81 | inconsistent | 72 | 6.852 | 0.716 | PENDING | — | A2 | NA | NA | — | 维度一待定：inconsistent tense(G2)vs inconsistent argument(G1)〔沿用组 1〕 |
| 82 | numerous | 42 | 6.742 | 0.973 | NA | — | NA | NA | NA | M | 量词 |
| 83 | risk | 65 | 6.658 | 0.747 | NA | — | NA | M1 | NA | M | M1：risks sounding X，删除后批评仍在且更强〔沿用组 1〕 |
| 84 | weakness | 57 | 6.651 | 0.805 | NA | — | PENDING | NA | NA | — | act 层待定：反馈小标题"Weaknesses:"（元话语 NA）vs 负向评价（A2）；与 STRENGTH 同构处理 |
| 85 | analytical | 148 | 6.551 | 0.468 | G1 | Ideas | NA | NA | NA | M | analytical depth/analytical claim；描述论述方式而非归功〔沿用组 1〕 |
| 86 | overly | 43 | 6.515 | 0.939 | NA | — | A2 | NA | NA | M | 标记过度=内在负向〔沿用组 1〕 |
| 87 | once | 111 | 6.345 | 0.538 | NA | — | NA | NA | NA | M | 时间/条件连接词〔沿用组 7〕 |
| 88 | something | 134 | 6.316 | 0.484 | NA | — | NA | NA | NA | H | 不定指代〔沿用组 1〕 |
| 89 | studies | 112 | 6.270 | 0.532 | G1 | Development | NA | NA | NA | M | 来源/证据类型（studies show）；疑似议题内容残留，待核 |
| 90 | views | 77 | 6.250 | 0.654 | G1 | Ideas | NA | NA | NA | M | opposing views，反驳层；同组 8 opposing 口径 |
| 91 | similarly | 64 | 6.217 | 0.725 | NA | — | NA | NA | NA | H | 连接副词〔沿用组 1〕 |
| 92 | offer | 38 | 6.100 | 0.973 | NA | — | PENDING | NA | NA | — | act 层待定：offer more evidence（A3）vs you offer（描述）；内容动词类 |
| 93 | move | 146 | 5.972 | 0.448 | PENDING | — | PENDING | NA | NA | — | 维度一待定：move this paragraph(G1)vs move on to(NA)；act 层随之待定〔沿用组 1〕 |
| 94 | vague | 96 | 5.850 | 0.557 | PENDING | — | A2 | NA | NA | — | 维度一待定：与 unclear 同族，可指论证或用词〔沿用组 1〕 |
| 95 | additionally | 36 | 5.779 | 0.973 | NA | — | NA | NA | NA | M | 连接副词 |
| 96 | early | 115 | 5.670 | 0.496 | PENDING | — | NA | NA | NA | — | 维度一待定：early in your essay（G1-Structure 位置）vs early on（NA） |
| 97 | acknowledge | 104 | 5.650 | 0.523 | G1 | Ideas | A3 | NA | NA | M | acknowledge counterarguments〔沿用组 1〕 |
| 98 | personal | 463 | 5.613 | 0.235 | PENDING | — | NA | NA | NA | — | 维度一待定：personal experience/anecdote(G1-Development)vs personal opinion(G1-Ideas)vs too personal(register) |
| 99 | section | 155 | 5.520 | 0.416 | G1 | Global Structure | NA | NA | NA | M | 大于段落的单位〔沿用组 1〕 |
| 100 | typos | 66 | 5.430 | 0.659 | G2 | Mechanics | NA | NA | NA | H | Mechanics 明示〔沿用组 1〕 |
| 101 | loosely | 38 | 5.343 | 0.899 | PENDING | — | A2 | NA | NA | — | 维度一待定：loosely connected(G1 连贯)vs loosely worded(G2)〔沿用组 1〕 |
| 102 | actually | 154 | 5.258 | 0.406 | NA | — | NA | NA | NA | M | 强化/对比副词〔沿用组 1〕 |
| 103 | somewhat | 94 | 5.176 | 0.527 | NA | — | NA | M1 | NA | H | 手册 v3 M1 明示 hedge |
| 104 | reflection | 55 | 5.149 | 0.709 | PENDING | — | NA | NA | NA | — | 维度一待定：your reflection on the topic(G1-Ideas)vs a reflection of（NA） |
| 105 | weaken | 101 | 5.078 | 0.501 | NA | — | A2 | NA | NA | M | weakens your argument，层级由宾语决定〔沿用组 1〕 |
| 106 | seriously | 60 | 5.078 | 0.670 | NA | — | NA | NA | NA | M | 强化副词（take seriously），非 hedge |
| 107 | precision | 80 | 5.019 | 0.567 | PENDING | — | NA | NA | NA | — | 维度一待定：precision of language(G2)vs of claims(G1)〔沿用组 1〕 |
| 108 | significance | 75 | 5.010 | 0.587 | G1 | Ideas | NA | NA | NA | M | the significance of your claim，论点意义 |
| 109 | historical | 280 | 5.005 | 0.288 | NA | — | NA | NA | NA | H | 议题内容残留 |
| 110 | deserves | 57 | 4.902 | 0.676 | NA | — | PENDING | NA | NA | — | act 层待定：this point deserves more attention＝隐性建议（A3）vs 正向评价（A1） |
| 111 | repeated | 72 | 4.827 | 0.588 | PENDING | — | NA | NA | NA | — | 维度一待定：repeated errors(G2)vs repeated ideas(G2-Local，手册 repetitive 口径)vs 论点重复(G1) |
| 112 | cut | 58 | 4.787 | 0.661 | G2 | Local Structure | A3 | NA | NA | M | 删削冗余，句内/句间〔沿用组 1〕 |
| 113 | discussion | 83 | 4.778 | 0.540 | G1 | Ideas | NA | NA | NA | M | your discussion of X；子类 Ideas 与 Global Structure 边界待核 |
| 114 | specifically | 90 | 4.669 | 0.510 | NA | — | NA | NA | NA | M | 元话语副词（区别于手册中 PENDING 的 specific）〔沿用组 1〕 |
| 115 | saying | 110 | 4.536 | 0.450 | NA | — | PENDING | NA | NA | — | act 层待定：you say X（描述）vs say more about（A3）；内容动词类 |
| 116 | specific | 630 | 4.522 | 0.179 | PENDING | — | NA | NA | NA | — | 手册明列 specific 为 PENDING：细节不足(G1-Dev)vs 用词不准(G2)〔沿用组 5〕 |
| 117 | define | 87 | 4.488 | 0.509 | PENDING | — | A3 | NA | NA | — | 维度一待定：define your terms 属 Wording(G2)还是概念澄清(G1)〔沿用组 1〕 |
| 118 | serve | 39 | 4.483 | 0.799 | NA | — | NA | NA | NA | M | 描述性动词〔沿用组 1〕 |
| 119 | rebuttal | 66 | 4.463 | 0.591 | G1 | Ideas | NA | NA | NA | H | 反驳层，与 COUNTERARGUMENT 同域 |
| 120 | single | 94 | 4.408 | 0.483 | NA | — | NA | NA | NA | H | 数量词〔沿用组 1〕 |
| 121 | logically | 57 | 4.392 | 0.635 | G1 | Ideas | NA | NA | NA | M | 手册 Ideas 词族例含 logic；若主导搭配为 organize…logically 则应改判 Global Structure〔沿用组 3〕 |
| 122 | dates | 44 | 4.345 | 0.732 | NA | — | NA | NA | NA | M | 疑似议题内容残留（与 historical 共现）vs 引证信息，待核 |
| 123 | line | 74 | 4.230 | 0.538 | PENDING | — | NA | NA | NA | — | 维度一待定：line of reasoning(G1)vs this line(G2)〔沿用组 1〕 |
| 124 | showing | 41 | 4.181 | 0.745 | NA | — | NA | NA | NA | M | 描述性框架动词 |
| 125 | distinguish | 37 | 4.173 | 0.790 | G1 | Ideas | A3 | NA | NA | M | distinguish between claims〔沿用组 1〕 |
| 126 | fully | 253 | 4.171 | 0.276 | NA | — | NA | NA | NA | M | 强化词，非 hedge |
| 127 | ask | 118 | 4.136 | 0.412 | PENDING | — | NA | NA | NA | — | 维度一待定：a reader will ask（G1-Ideas 预设反驳）vs ask yourself（元话语） |
| 128 | thesis | 1673 | 4.124 | 0.103 | G1 | Ideas | NA | NA | NA | H | Ideas 明示〔沿用组 5〕 |
| 129 | now | 559 | 4.072 | 0.180 | NA | — | NA | NA | NA | H | 时间/话语副词〔沿用组 1〕 |
| 130 | likely | 136 | 3.966 | 0.373 | NA | — | NA | M1 | NA | H | 认识型 hedge，与手册 probably/possibly 同类〔沿用组 6〕 |
| 131 | undermines | 39 | 3.878 | 0.734 | NA | — | A2 | NA | NA | M | undermines your credibility，层级由宾语决定；同组 1 weaken 口径 |

### B1 维度一 Feedback Focus

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| G1 | 44 | 84.6% | 12390 | 92.5% | 0.744 |
| G2 | 8 | 15.4% | 1009 | 7.5% | 1.170 |
| **已定标签合计** | **52** | **100.0%** | **13399** | **100.0%** | — |
| N/A（不计入分母） | 57 | — | — | — | — |
| PENDING（不计入分母） | 22 | — | — | — | — |
| 清单总数 | 131 | — | — | — | — |

**子类分布（分母同为已定标签 52）**

| 主类 | 子类 | 词位数 | 占比 |
|---|---|---:|---:|
| G1 | Development | 7 | 13.5% |
| G1 | Global Structure | 4 | 7.7% |
| G1 | Ideas | 33 | 63.5% |
| G2 | Correctness | 2 | 3.8% |
| G2 | Local Structure | 1 | 1.9% |
| G2 | Mechanics | 3 | 5.8% |
| G2 | Wording | 2 | 3.8% |

### B2 维度二 · act 层（A1 Praise / A2 Criticism / A3 Suggestion）

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| A3 | 16 | 55.2% | 4885 | 82.9% | 0.614 |
| A2 | 9 | 31.0% | 611 | 10.4% | 0.948 |
| A1 | 4 | 13.8% | 397 | 6.7% | 1.036 |
| **已定标签合计** | **29** | **100.0%** | **5893** | **100.0%** | — |
| N/A（不计入分母） | 89 | — | — | — | — |
| PENDING（不计入分母） | 13 | — | — | — | — |
| 清单总数 | 131 | — | — | — | — |

### B3 维度二 · hedge 层（M1 Hedges）

hedge 层与 act 层并行判定、可共存（Hyland & Hyland：hedge 施加于 act 之上）。分母为本层已定标签数。

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| M1 | 4 | 100.0% | 379 | 100.0% | 0.711 |
| **已定标签合计** | **4** | **100.0%** | **379** | **100.0%** | — |
| N/A（不计入分母） | 123 | — | — | — | — |
| PENDING（不计入分母） | 4 | — | — | — | — |
| 清单总数 | 131 | — | — | — | — |

### B4 维度三 Larger Contexts of Writing

**已定标签 0 项** —— 本层无任何词位获得标签，占比不适用（分母为 0）。

| 标签 | 词位数 | Freq_Tar 合计 |
|---|---:|---:|
| 已定标签合计 | 0 | 0 |
| N/A（不计入分母） | 131 | — |
| PENDING（不计入分母） | 0 | — |
| 清单总数 | 131 | — |

### B5 维度二两层共现（词位数）

| act ＼ hedge | M1 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|
| **A1** | 0 | 4 | 0 | **4** |
| **A2** | 0 | 9 | 0 | **9** |
| **A3** | 0 | 16 | 0 | **16** |
| **NA** | 4 | 83 | 2 | **89** |
| **PENDING** | 0 | 11 | 2 | **13** |
| **合计** | 4 | 123 | 4 | **131** |

act ＋ hedge 双标签共现：**0** 项

### B6 维度一 × 维度二 act 层 交叉表（词位数）

| 维度一＼act | A1 | A2 | A3 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|---:|---:|
| **G1** | 2 | 1 | 6 | 33 | 2 | **44** |
| **G2** | 0 | 0 | 2 | 6 | 0 | **8** |
| **NA** | 2 | 4 | 4 | 38 | 9 | **57** |
| **PENDING** | 0 | 4 | 4 | 12 | 2 | **22** |
| **合计** | 4 | 9 | 16 | 89 | 13 | **131** |

### B7 LL 前 20 词位的维度一构成

| | G1 | G2 | N/A | PENDING |
|---|---:|---:|---:|---:|
| 词位数 | 10 | 3 | 5 | 2 |

### B8 敏感性分析：维度一 PENDING 的极端归属

| 情形 | G1 词位 | G2 词位 | G1 占比 |
|---|---:|---:|---:|
| 现状（PENDING 不计入） | 44 | 8 | 84.6% |
| 22 个 PENDING 全归 G1（上界） | 66 | 8 | 89.2% |
| 22 个 PENDING 全归 G2（下界） | 44 | 30 | 59.5% |

### B9 concordance 待办清单

共 **36** 个词族需 concordance 判定（含 2 个低信度已定项）。

| Type | Freq_Tar | 待定层 | 竞争读法 |
|---|---:|---|---|
| `rather` | 784 | hedge | M1待定：手册列为 hedge，但"rather than"（建议对比框架）可能占主导〔沿用组 1〕 |
| `distract` | 66 | 维度一 | 维度一待定：typos distract(G2)vs digression distracts(G1)〔沿用组 1〕 |
| `address` | 302 | 维度一、act | 手册 v3 强制查询清单（G1/A3 争议），不得凭词形归类：address counterarguments(G1+A3) vs 元话语"address the points below"(NA)〔沿用组 1〕 |
| `aim` | 67 | act | act 层待定："aim to/for"（A3）vs "your aim"（名词，NA）〔沿用组 1〕 |
| `reads` | 188 | 维度一 | 维度一待定：the essay reads(整体)vs this sentence reads(句级)〔沿用组 1〕 |
| `just` | 271 | hedge | M1待定：最小化降调(M1)vs"仅仅是"强化批评(NA)；竞争读法全在 hedge 层，与 act 层无关〔沿用组 1〕 |
| `might` | 189 | act、hedge | 手册指定共享项〔沿用组 1〕 |
| `would` | 739 | act、hedge | 手册指定共享项，concordance 抽 50 行判 A3/M1〔沿用组 1〕 |
| `tackles` | 82 | act | act 层待定：your essay tackles a difficult question 属开场归功套语(A1)vs 描述(NA)。与组 4 raises 并案；组 1 的 A1 编码不追溯改动，留待跨组一致性检查统一回填 |
| `EDIT` | 164 | 维度一 | 维度一待定：表层编辑(G2)vs 全局修改(G1)；沿用组 1 edit 口径 |
| `authority` | 58 | 低信度复核 | 写作者论述权威/立场，归修辞语境→G1〔沿用组 1〕 |
| `level` | 248 | 维度一 | 维度一待定：sentence-level(G2)/paragraph-level(G1)/level of detail(G1-Dev)〔沿用组 1〕 |
| `narrow` | 54 | act | 与本组 BROAD 构成论断范围对举，域固定于论断；act 层待定：narrow your claim(A3)vs too narrow(A2) |
| `strongest` | 176 | act | 手册 v3 强制查询清单（strong 系 A1/A3 争议），不得凭词形归类：your strongest evidence(A1) vs 目标态框架(A3)〔沿用组 1〕 |
| `clarify` | 212 | 维度一 | 维度一待定（手册 clear 系）；建议动词〔沿用组 8〕 |
| `right` | 538 | 维度一 | 维度一待定：the right word(G2)vs right now(NA)〔沿用组 1〕 |
| `treatment` | 70 | 维度一 | 维度一待定：your treatment of the topic(G1-Ideas)vs 议题内容残留，待核 |
| `sharper` | 59 | act | act 层待定：比较级多嵌于目标态框架（make it sharper=A3）而非评价（A1）〔沿用组 1〕 |
| `replace` | 167 | 维度一 | 维度一待定：replace this word(G2)vs replace this paragraph(G1)〔沿用组 1〕 |
| `inconsistent` | 72 | 维度一 | 维度一待定：inconsistent tense(G2)vs inconsistent argument(G1)〔沿用组 1〕 |
| `weakness` | 57 | act | act 层待定：反馈小标题"Weaknesses:"（元话语 NA）vs 负向评价（A2）；与 STRENGTH 同构处理 |
| `offer` | 38 | act | act 层待定：offer more evidence（A3）vs you offer（描述）；内容动词类 |
| `move` | 146 | 维度一、act | 维度一待定：move this paragraph(G1)vs move on to(NA)；act 层随之待定〔沿用组 1〕 |
| `vague` | 96 | 维度一 | 维度一待定：与 unclear 同族，可指论证或用词〔沿用组 1〕 |
| `early` | 115 | 维度一 | 维度一待定：early in your essay（G1-Structure 位置）vs early on（NA） |
| `personal` | 463 | 维度一 | 维度一待定：personal experience/anecdote(G1-Development)vs personal opinion(G1-Ideas)vs too personal(register) |
| `loosely` | 38 | 维度一 | 维度一待定：loosely connected(G1 连贯)vs loosely worded(G2)〔沿用组 1〕 |
| `reflection` | 55 | 维度一 | 维度一待定：your reflection on the topic(G1-Ideas)vs a reflection of（NA） |
| `precision` | 80 | 维度一 | 维度一待定：precision of language(G2)vs of claims(G1)〔沿用组 1〕 |
| `deserves` | 57 | act | act 层待定：this point deserves more attention＝隐性建议（A3）vs 正向评价（A1） |
| `repeated` | 72 | 维度一 | 维度一待定：repeated errors(G2)vs repeated ideas(G2-Local，手册 repetitive 口径)vs 论点重复(G1) |
| `saying` | 110 | act | act 层待定：you say X（描述）vs say more about（A3）；内容动词类 |
| `specific` | 630 | 维度一 | 手册明列 specific 为 PENDING：细节不足(G1-Dev)vs 用词不准(G2)〔沿用组 5〕 |
| `define` | 87 | 维度一 | 维度一待定：define your terms 属 Wording(G2)还是概念澄清(G1)〔沿用组 1〕 |
| `line` | 74 | 维度一 | 维度一待定：line of reasoning(G1)vs this line(G2)〔沿用组 1〕 |
| `ask` | 118 | 维度一 | 维度一待定：a reader will ask（G1-Ideas 预设反驳）vs ask yourself（元话语） |

### B10 高效应量词位（LR ≥ 1.5）

| Type | LL | LR | 维度一 | act | hedge |
|---|---:|---:|---|---|---|
| correctness | 37.529 | 3.002 | G2/Correctness | NA | NA |
| prose | 24.323 | 1.973 | G2/Wording | NA | NA |
| distract | 25.073 | 1.695 | PENDING | A2 | NA |

# 附表：组 10（Generic → Baseline）

## 附表 A：组 10 完整编码表（121 词位，按 LL 降序）

| # | Type | Freq_Tar | LL | LR | 维度一 | 子类 | 维度二 act | 维度二 hedge | 维度三 | 信度 | 判定依据 |
|---:|---|---:|---:|---:|---|---|---|---|---|---|---|
| 1 | GOOD | 949 | 185.834 | 1.082 | NA | — | PENDING | NA | NA | — | act 层待定：good+better 归并，comparative 多嵌于目标态框架（make it better=A3）vs 评价（A1）；LL 全组最高，须查〔沿用组 2〕 |
| 2 | language | 642 | 143.329 | 1.174 | PENDING | — | NA | NA | PENDING | — | 维度三待定：your language background/first language(C1) vs academic language(G2 Wording)；本组理论枢纽词〔沿用组 2〕 |
| 3 | corrections | 90 | 89.818 | 3.934 | G2 | Correctness | NA | NA | NA | M | 命名 Correctness 焦点的元话语标签；中性焦点名词，act 层不赋值〔沿用组 2〕 |
| 4 | main | 716 | 60.781 | 0.663 | G1 | Ideas | NA | NA | NA | M | main point/argument/idea；子类 Ideas 与 Global Structure 边界待核〔沿用组 2〕 |
| 5 | writing | 439 | 60.306 | 0.875 | NA | — | NA | NA | NA | M | 文本指称/写作过程，不指示层级〔沿用组 2〕 |
| 6 | word | 439 | 58.932 | 0.863 | G2 | Wording | NA | NA | NA | H | Wording 明示。注：本组为单数 word 独立入选（组 2 为归并 WORD），系 R1 先行的口径效应〔沿用组 3〕 |
| 7 | academic | 841 | 55.170 | 0.574 | PENDING | — | NA | NA | NA | — | 维度一待定：属 register，手册列 tone/formal/register 为 PENDING〔沿用组 2〕 |
| 8 | grammar | 658 | 55.167 | 0.658 | G2 | Grammar | NA | NA | NA | H | Correctness/Grammar 明示；中性焦点名词〔沿用组 2〕 |
| 9 | strengths | 165 | 49.273 | 1.417 | NA | — | PENDING | NA | NA | — | act 层待定：反馈小标题"Strengths:"（元话语 NA）vs 归功（A1）；且属 strong 词族，按 v3 强制查询规则不得凭词形定。注：组 2 为归并 STRENGTH，本组为 strengths 单独入选，系口径效应 |
| 10 | english | 74 | 48.406 | 2.536 | NA | — | NA | NA | PENDING | — | 手册明列：指语言系统（correct English）→C1；作文体修饰（English essay）→NA。两读法维度一均为 NA〔沿用组 2〕 |
| 11 | IDEA | 830 | 45.188 | 0.517 | G1 | Ideas | NA | NA | NA | H | Ideas 明示〔沿用组 2〕 |
| 12 | SENTENCE | 1590 | 43.755 | 0.357 | G2 | Local Structure | NA | NA | NA | H | Local Structure 明示。注：组 2 为 sentences 单独入选，本组为归并 SENTENCE，系口径效应 |
| 13 | verb | 221 | 41.820 | 1.060 | G2 | Grammar | NA | NA | NA | H | Correctness/Grammar 明示〔沿用组 2〕 |
| 14 | ARTICLE | 167 | 41.715 | 1.261 | PENDING | — | NA | NA | NA | — | 维度一待定：英语冠词(G2-Grammar)vs 引用的文章(G1-Development)；L2 语法标记的关键判别点〔沿用组 2〕 |
| 15 | use | 897 | 39.259 | 0.459 | PENDING | — | PENDING | NA | NA | — | 维度一与 act 层皆待定；内容动词类。注：组 2 为归并 USE（use+using），本组为 use 单独入选——交接文档 §三 预告的口径效应实例 |
| 16 | slightly | 58 | 36.018 | 2.426 | NA | — | NA | M1 | NA | H | 手册 v3 M1 明示 hedge〔沿用组 2〕 |
| 17 | recurring | 77 | 35.100 | 1.902 | NA | — | NA | NA | NA | M | recurring errors/patterns，层级由宾语决定；构成"错误模式化"框架〔沿用组 2〕 |
| 18 | choice | 395 | 31.663 | 0.642 | G2 | Wording | NA | NA | NA | M | word choice；your choice of topic 读法待观察〔沿用组 2〕 |
| 19 | suggestions | 160 | 29.580 | 1.046 | NA | — | PENDING | NA | NA | — | act 层待定：反馈小标题"Suggestions:"（元话语 NA）vs 名词化建议行为（A3）〔沿用组 2〕 |
| 20 | check | 144 | 29.339 | 1.110 | PENDING | — | A3 | NA | NA | — | 维度一待定：check your spelling(G2)vs check your logic(G1)；手册 A3 明示〔沿用组 2〕 |
| 21 | some | 939 | 29.048 | 0.381 | NA | — | NA | M1 | NA | H | 手册 v3 M1 明示 hedge〔沿用组 2〕 |
| 22 | here | 250 | 27.826 | 0.774 | NA | — | NA | NA | NA | M | 指示元话语〔沿用组 2〕 |
| 23 | patterns | 56 | 27.794 | 2.027 | PENDING | — | NA | NA | NA | — | 维度一待定：error patterns(G2)vs sentence patterns(G2-Local)vs 论证模式(G1)〔沿用组 2〕 |
| 24 | formal | 364 | 27.609 | 0.622 | PENDING | — | NA | NA | NA | — | 维度一待定（register）；命名目标态而非评价，act 层不赋值〔沿用组 2〕 |
| 25 | comment | 57 | 26.932 | 1.953 | NA | — | NA | NA | NA | M | 元话语（a comment on… / 小标题）〔沿用组 2〕 |
| 26 | too | 529 | 26.381 | 0.493 | NA | — | A2 | NA | NA | M | 标记过度=内在负向（同组 1 overly 口径）；polysemy 高于 overly，信度中等〔沿用组 2〕 |
| 27 | tense | 99 | 25.892 | 1.299 | G2 | Grammar | NA | NA | NA | H | Correctness/Grammar 明示〔沿用组 2〕 |
| 28 | expressions | 49 | 24.786 | 2.057 | G2 | Wording | NA | NA | NA | H | Wording 明示〔沿用组 2〕 |
| 29 | original | 135 | 24.666 | 1.038 | NA | — | NA | NA | NA | M | 与 revised 配对的"原句/改后句"对照格式，元话语〔沿用组 2〕 |
| 30 | form | 106 | 24.496 | 1.201 | G2 | Grammar | NA | NA | NA | M | verb form / the correct form〔沿用组 2〕 |
| 31 | probably | 59 | 23.792 | 1.740 | NA | — | NA | M1 | NA | H | 认识型 hedge，与手册 possibly/maybe 同类〔沿用组 2〕 |
| 32 | OPINION | 215 | 21.672 | 0.731 | G1 | Ideas | NA | NA | NA | M | your opinion / opinion vs fact，属论断层〔沿用组 2〕 |
| 33 | strong | 711 | 21.022 | 0.372 | NA | — | PENDING | NA | NA | — | 手册 v3 强制查询清单（A1/A3 争议），不得凭词形归类〔沿用组 2〕 |
| 34 | understandable | 62 | 20.614 | 1.522 | PENDING | — | A1 | NA | NA | L | 维度一待定（clear 系）；act 低信度：作为"低门槛褒扬"（your English is understandable）与 A1 定义是否相符须查〔沿用组 2〕 |
| 35 | vocabulary | 42 | 19.937 | 1.960 | G2 | Wording | NA | NA | NA | H | Wording 明示〔沿用组 2〕 |
| 36 | advice | 128 | 19.833 | 0.940 | NA | — | PENDING | NA | NA | — | act 层待定：反馈小标题（NA）vs my advice is to…（A3）〔沿用组 2〕 |
| 37 | example | 1106 | 19.447 | 0.282 | G1 | Development | NA | NA | NA | H | Development 明示〔沿用组 2〕 |
| 38 | subject | 181 | 18.887 | 0.746 | PENDING | — | NA | NA | NA | — | 维度一待定：subject-verb agreement(G2-Grammar)vs the subject of your essay(G1)〔沿用组 2〕 |
| 39 | avoid | 308 | 18.462 | 0.546 | NA | — | A3 | NA | NA | H | 手册 A3 明示〔沿用组 2〕 |
| 40 | try | 431 | 17.345 | 0.439 | NA | — | A3 | NA | NA | H | Hyland&Hyland 明示建议套语（the verb try）〔沿用组 2〕 |
| 41 | write | 264 | 17.207 | 0.572 | NA | — | PENDING | NA | NA | — | act 层待定：when you write（描述 NA）vs write this as…（A3）〔沿用组 2〕 |
| 42 | plural | 46 | 17.111 | 1.644 | G2 | Grammar | NA | NA | NA | H | 单复数，Correctness/Grammar 明示〔沿用组 7〕 |
| 43 | below | 163 | 16.470 | 0.732 | NA | — | NA | NA | NA | M | 指示元话语（see below）〔沿用组 2〕 |
| 44 | thank | 50 | 16.288 | 1.501 | NA | — | NA | NA | NA | M | 人际礼貌行为（thank you for sharing），未归功于文本属性，不构成 A1；属手册排除的 paired acts 类〔沿用组 2〕 |
| 45 | luck | 36 | 16.100 | 1.875 | NA | — | NA | NA | NA | M | 人际礼貌（good luck）〔沿用组 2〕 |
| 46 | i | 431 | 16.073 | 0.421 | NA | — | NA | NA | NA | M | 反馈者自称（I suggest/I noticed）＝人称归因，属手册排除的缓和策略，不入 M1〔沿用组 2〕 |
| 47 | agreement | 182 | 15.517 | 0.665 | G2 | Grammar | NA | NA | NA | H | subject-verb agreement〔沿用组 2〕 |
| 48 | CLEAR | 1289 | 15.206 | 0.229 | PENDING | — | PENDING | NA | NA | — | 维度一待定（手册 clear 系）；act 层待定：clear(A1)vs clearer 目标态框架(A3)〔沿用组 2〕 |
| 49 | natural | 49 | 14.281 | 1.394 | PENDING | — | PENDING | NA | PENDING | — | 三层皆待定：sounds natural 是否以母语者语感为隐含标准（C1）；若判 C1 则维度一二依规则归 NA〔沿用组 2〕 |
| 50 | people | 608 | 13.877 | 0.324 | NA | — | NA | NA | NA | M | 疑似议题内容残留（LOCNESS 主题）；people reading your essay 读法待核〔沿用组 2〕 |
| 51 | long | 248 | 12.561 | 0.498 | G2 | Local Structure | NA | NA | NA | M | long sentences，句级冗长；评价由 too 承担〔沿用组 2〕 |
| 52 | only | 333 | 12.235 | 0.418 | NA | — | NA | PENDING | NA | — | hedge 层待定：最小化降调（only a few errors=M1）vs 限定（NA）；同组 1 just〔沿用组 2〕 |
| 53 | consistent | 129 | 12.007 | 0.699 | PENDING | — | NA | NA | NA | — | 维度一待定：consistent tense(G2)vs consistent argument(G1)；同组 2 consistency 口径 |
| 54 | past | 73 | 11.905 | 0.969 | G2 | Grammar | NA | NA | NA | M | past tense〔沿用组 2〕 |
| 55 | meaning | 59 | 11.892 | 1.103 | PENDING | — | NA | NA | NA | — | 维度一待定：the meaning is unclear（G1 表意）vs 词义(G2-Wording) |
| 56 | think | 89 | 11.849 | 0.859 | NA | — | NA | NA | NA | M | I think…＝人称归因，属手册排除的缓和策略，不入 M1 |
| 57 | her | 91 | 11.531 | 0.835 | NA | — | NA | NA | NA | M | 疑似议题内容残留，待核〔沿用组 2〕 |
| 58 | many | 557 | 11.447 | 0.307 | NA | — | NA | NA | NA | M | 量词〔沿用组 2〕 |
| 59 | improved | 48 | 11.375 | 1.220 | NA | — | A3 | NA | NA | M | 改进指向，层级由宾语决定；同组 2 IMPROVE 口径 |
| 60 | sharing | 37 | 11.200 | 1.430 | NA | — | NA | NA | NA | M | 人际礼貌（thank you for sharing）〔沿用组 2〕 |
| 61 | sounds | 122 | 11.143 | 0.691 | NA | — | NA | NA | NA | M | 听感评价框架动词（sounds awkward/natural）；与 natural/unnatural 共现，其 C1 权重由后者承担〔沿用组 7〕 |
| 62 | eg | 339 | 11.134 | 0.394 | NA | — | NA | NA | NA | M | 举例元话语（e.g.），与组 1 的 for instance 构成对照〔沿用组 2〕 |
| 63 | paragraph | 1699 | 11.077 | 0.168 | PENDING | — | NA | NA | NA | — | 维度一待定：手册明示段落内部组织→G2、段落间安排→G1 |
| 64 | informal | 190 | 10.830 | 0.531 | PENDING | — | A2 | NA | NA | — | 维度一待定（register）；学术语境下标记偏离=负向（同组 1 casual 口径）〔沿用组 2〕 |
| 65 | contain | 80 | 10.612 | 0.858 | NA | — | NA | NA | NA | M | 描述性动词〔沿用组 2〕 |
| 66 | ONE | 1118 | 10.591 | 0.204 | NA | — | NA | NA | NA | M | 数量词/指代词 |
| 67 | please | 55 | 10.298 | 1.054 | NA | — | NA | NA | NA | M | 礼貌标记；手册 M1 限于 hedges，礼貌标记不入 M1〔沿用组 2〕 |
| 68 | introduction | 579 | 10.222 | 0.283 | G1 | Global Structure | NA | NA | NA | H | 大单位，Global Structure 明示〔沿用组 2〕 |
| 69 | correct | 152 | 9.995 | 0.575 | G2 | Correctness | PENDING | NA | NA | — | act 层待定：correct these errors(A3)vs the correct form(NA)〔沿用组 2〕 |
| 70 | important | 323 | 9.924 | 0.380 | NA | — | PENDING | NA | NA | — | act 层待定：an important point(A1)vs it is important to…(A3 框架)〔沿用组 2〕 |
| 71 | needed | 50 | 9.836 | 1.086 | NA | — | A3 | NA | NA | M | more detail is needed，need 系建议套语的被动形式 |
| 72 | easy | 70 | 9.541 | 0.871 | NA | — | A1 | NA | NA | M | easy to follow/read，正向评价；目标态框架风险〔沿用组 2〕 |
| 73 | worth | 64 | 9.184 | 0.898 | NA | — | PENDING | NA | NA | — | act 层待定：it's worth adding X＝隐性建议（A3）vs 价值评价（A1）；与组 9 deserves 同构 |
| 74 | areas | 267 | 9.101 | 0.402 | NA | — | NA | NA | NA | M | 元话语（areas for improvement，反馈小标题）〔沿用组 2〕 |
| 75 | way | 149 | 8.931 | 0.546 | NA | — | NA | NA | NA | M | a way to／the way you，无固定层级所指 |
| 76 | she | 70 | 8.869 | 0.835 | NA | — | NA | NA | NA | M | 疑似议题内容残留（引述作文内容），待核〔沿用组 2〕 |
| 77 | proper | 73 | 8.431 | 0.791 | G2 | Correctness | NA | NA | NA | M | proper grammar/punctuation；规范性框架词〔沿用组 2〕 |
| 78 | common | 107 | 8.036 | 0.619 | NA | — | NA | NA | NA | M | 常见性标记（a common error）＝正常化框架；属手册排除的缓和策略，不入 M1〔沿用组 2〕 |
| 79 | relevant | 114 | 7.938 | 0.594 | G1 | Development | NA | NA | NA | M | relevant evidence/examples〔沿用组 2〕 |
| 80 | usually | 89 | 7.696 | 0.670 | NA | — | NA | M1 | NA | H | 手册 v3 M1 明示 hedge〔沿用组 3〕 |
| 81 | especially | 204 | 7.680 | 0.424 | NA | — | NA | NA | NA | M | 焦点副词〔沿用组 2〕 |
| 82 | above | 42 | 7.542 | 1.027 | NA | — | NA | NA | NA | M | 指示元话语（see above）〔沿用组 6〕 |
| 83 | spelling | 294 | 7.520 | 0.344 | G2 | Mechanics | NA | NA | NA | H | Mechanics 明示〔沿用组 2〕 |
| 84 | topic | 602 | 7.507 | 0.236 | PENDING | — | NA | NA | NA | — | 维度一待定：the topic of your essay(G1-Ideas)vs topic sentence(G2/G1 边界)〔沿用组 2〕 |
| 85 | work | 245 | 7.499 | 0.379 | NA | — | NA | NA | NA | M | 文本指称语（your work） |
| 86 | commas | 64 | 7.207 | 0.780 | G2 | Mechanics | NA | NA | NA | H | Mechanics 明示〔沿用组 6〕 |
| 87 | very | 173 | 6.973 | 0.440 | NA | — | NA | NA | NA | M | 强化词，非 hedge〔沿用组 2〕 |
| 88 | emotional | 217 | 6.657 | 0.380 | PENDING | — | NA | NA | NA | — | 维度一待定：emotional language(G2-Wording/register)vs emotional appeal(G1-Ideas)；亦可能为议题残留〔沿用组 2〕 |
| 89 | must | 121 | 6.634 | 0.520 | NA | — | A3 | NA | NA | H | 手册 A3 明示〔沿用组 2〕 |
| 90 | unclear | 153 | 6.487 | 0.452 | PENDING | — | A2 | NA | NA | — | 维度一待定（手册 clear 系）；负向评价〔沿用组 2〕 |
| 91 | final | 414 | 6.472 | 0.266 | PENDING | — | NA | NA | NA | — | 维度一待定：your final paragraph(G1-Structure)vs"Final thoughts:"小标题(NA)〔沿用组 2〕 |
| 92 | shows | 255 | 6.445 | 0.342 | NA | — | NA | NA | NA | M | 描述性框架动词〔沿用组 2〕 |
| 93 | consistency | 105 | 6.412 | 0.552 | PENDING | — | NA | NA | NA | — | 维度一待定：consistency of tense(G2)vs of argument(G1)〔沿用组 2〕 |
| 94 | clearly | 502 | 6.335 | 0.237 | PENDING | — | NA | NA | NA | — | 维度一待定（clear 系）；方式副词，act 层不赋值〔沿用组 2〕 |
| 95 | statement | 156 | 6.039 | 0.430 | G1 | Ideas | NA | NA | NA | M | thesis statement〔沿用组 2〕 |
| 96 | their | 357 | 5.905 | 0.274 | NA | — | NA | NA | NA | M | 人称代词 |
| 97 | another | 104 | 5.670 | 0.518 | NA | — | NA | NA | NA | M | 限定词 |
| 98 | accuracy | 112 | 5.611 | 0.495 | G2 | Correctness | NA | NA | NA | H | Correctness 明示〔沿用组 2〕 |
| 99 | suggested | 86 | 5.586 | 0.571 | NA | — | PENDING | NA | NA | — | act 层待定：the suggested revision（NA）vs I suggested（A3）〔沿用组 2〕 |
| 100 | recommend | 59 | 5.515 | 0.701 | NA | — | A3 | NA | NA | H | 手册 A3 明示〔沿用组 5〕 |
| 101 | content | 107 | 5.503 | 0.502 | G1 | Ideas | NA | NA | NA | M | 内容层，与 organization 对举〔沿用组 2〕 |
| 102 | possible | 192 | 5.458 | 0.365 | NA | — | NA | PENDING | NA | — | hedge 层待定：it is possible that（M1）vs possible improvements（NA）〔沿用组 2〕 |
| 103 | he | 110 | 5.347 | 0.487 | NA | — | NA | NA | NA | M | 疑似议题内容残留，待核〔沿用组 2〕 |
| 104 | confusing | 56 | 5.299 | 0.706 | PENDING | — | A2 | NA | NA | — | 维度一待定（clear 系）；手册 A2 词族例明列 confusing〔沿用组 5〕 |
| 105 | briefly | 119 | 5.271 | 0.463 | NA | — | NA | PENDING | NA | — | hedge 层待定：briefly explain 削减要求强度（M1）vs 单纯方式副词（NA）〔沿用组 2〕 |
| 106 | we | 152 | 5.260 | 0.405 | NA | — | NA | NA | NA | M | 包容性人称，团结策略；不入 M1〔沿用组 2〕 |
| 107 | missing | 283 | 5.209 | 0.289 | NA | — | A2 | NA | NA | H | 手册 A2 词族例明列 missing |
| 108 | society | 248 | 4.736 | 0.295 | NA | — | NA | NA | NA | H | 议题内容残留〔沿用组 2〕 |
| 109 | direct | 129 | 4.553 | 0.409 | PENDING | — | NA | NA | PENDING | — | 维度三待定（先验较低）：German writing is direct（文化—语用框架，C1）vs be more direct(G2)/direct quotation(NA)〔沿用组 6〕 |
| 110 | third | 48 | 4.542 | 0.706 | NA | — | NA | NA | NA | M | 序数词，反馈条目枚举 |
| 111 | shorter | 59 | 4.501 | 0.625 | G2 | Local Structure | NA | NA | NA | M | shorter sentences；比较级，评价由框架承担〔沿用组 2〕 |
| 112 | story | 86 | 4.381 | 0.500 | NA | — | NA | NA | NA | M | 疑似议题内容残留，待核〔沿用组 8〕 |
| 113 | end | 243 | 4.194 | 0.280 | G1 | Global Structure | NA | NA | NA | M | the end of your essay/paragraph〔沿用组 2〕 |
| 114 | revised | 107 | 4.121 | 0.429 | NA | — | NA | NA | NA | M | 与 original 配对的改写对照，元话语〔沿用组 2〕 |
| 115 | women | 316 | 4.019 | 0.238 | NA | — | NA | NA | NA | H | 议题内容残留〔沿用组 2〕 |
| 116 | periods | 38 | 4.018 | 0.752 | G2 | Mechanics | NA | NA | NA | H | 句号，Mechanics 明示 |
| 117 | adding | 128 | 4.003 | 0.384 | NA | — | A3 | NA | NA | H | 手册 A3 明示（add）〔沿用组 2〕 |
| 118 | remove | 102 | 3.997 | 0.433 | PENDING | — | A3 | NA | NA | — | 维度一待定：remove this word(G2)vs remove this paragraph(G1)；建议动词 |
| 119 | usage | 49 | 3.926 | 0.642 | G2 | Correctness | NA | NA | NA | M | article usage / comma usage，语言使用规范层〔沿用组 6〕 |
| 120 | students | 151 | 3.913 | 0.347 | NA | — | NA | NA | NA | H | 议题内容残留〔沿用组 2〕 |
| 121 | citation | 132 | 3.886 | 0.371 | PENDING | — | NA | NA | NA | — | 维度一待定：引用来源的使用(G1-Development)vs 引用格式(G2-Mechanics) |

### B1 维度一 Feedback Focus

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| G2 | 22 | 71.0% | 5079 | 55.5% | 1.037 |
| G1 | 9 | 29.0% | 4066 | 44.5% | 0.476 |
| **已定标签合计** | **31** | **100.0%** | **9145** | **100.0%** | — |
| N/A（不计入分母） | 65 | — | — | — | — |
| PENDING（不计入分母） | 25 | — | — | — | — |
| 清单总数 | 121 | — | — | — | — |

**子类分布（分母同为已定标签 31）**

| 主类 | 子类 | 词位数 | 占比 |
|---|---|---:|---:|
| G1 | Development | 2 | 6.5% |
| G1 | Global Structure | 2 | 6.5% |
| G1 | Ideas | 5 | 16.1% |
| G2 | Correctness | 5 | 16.1% |
| G2 | Grammar | 7 | 22.6% |
| G2 | Local Structure | 3 | 9.7% |
| G2 | Mechanics | 3 | 9.7% |
| G2 | Wording | 4 | 12.9% |

### B2 维度二 · act 层（A1 Praise / A2 Criticism / A3 Suggestion）

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| A3 | 9 | 56.2% | 1391 | 50.9% | 0.715 |
| A2 | 5 | 31.2% | 1211 | 44.3% | 0.494 |
| A1 | 2 | 12.5% | 132 | 4.8% | 1.196 |
| **已定标签合计** | **16** | **100.0%** | **2734** | **100.0%** | — |
| N/A（不计入分母） | 92 | — | — | — | — |
| PENDING（不计入分母） | 13 | — | — | — | — |
| 清单总数 | 121 | — | — | — | — |

### B3 维度二 · hedge 层（M1 Hedges）

hedge 层与 act 层并行判定、可共存（Hyland & Hyland：hedge 施加于 act 之上）。分母为本层已定标签数。

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| M1 | 4 | 100.0% | 1145 | 100.0% | 1.304 |
| **已定标签合计** | **4** | **100.0%** | **1145** | **100.0%** | — |
| N/A（不计入分母） | 114 | — | — | — | — |
| PENDING（不计入分母） | 3 | — | — | — | — |
| 清单总数 | 121 | — | — | — | — |

### B4 维度三 Larger Contexts of Writing

**已定标签 0 项** —— 本层无任何词位获得标签，占比不适用（分母为 0）。

| 标签 | 词位数 | Freq_Tar 合计 |
|---|---:|---:|
| 已定标签合计 | 0 | 0 |
| N/A（不计入分母） | 117 | — |
| PENDING（不计入分母） | 4 | — |
| 清单总数 | 121 | — |

### B5 维度二两层共现（词位数）

| act ＼ hedge | M1 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|
| **A1** | 0 | 2 | 0 | **2** |
| **A2** | 0 | 5 | 0 | **5** |
| **A3** | 0 | 9 | 0 | **9** |
| **NA** | 4 | 85 | 3 | **92** |
| **PENDING** | 0 | 13 | 0 | **13** |
| **合计** | 4 | 114 | 3 | **121** |

act ＋ hedge 双标签共现：**0** 项

### B6 维度一 × 维度二 act 层 交叉表（词位数）

| 维度一＼act | A1 | A2 | A3 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|---:|---:|
| **G1** | 0 | 0 | 0 | 9 | 0 | **9** |
| **G2** | 0 | 0 | 0 | 21 | 1 | **22** |
| **NA** | 1 | 2 | 7 | 46 | 9 | **65** |
| **PENDING** | 1 | 3 | 2 | 16 | 3 | **25** |
| **合计** | 2 | 5 | 9 | 92 | 13 | **121** |

### B7 LL 前 20 词位的维度一构成

| | G1 | G2 | N/A | PENDING |
|---|---:|---:|---:|---:|
| 词位数 | 2 | 6 | 7 | 5 |

### B8 敏感性分析：维度一 PENDING 的极端归属

| 情形 | G1 词位 | G2 词位 | G1 占比 |
|---|---:|---:|---:|
| 现状（PENDING 不计入） | 9 | 22 | 29.0% |
| 25 个 PENDING 全归 G1（上界） | 34 | 22 | 60.7% |
| 25 个 PENDING 全归 G2（下界） | 9 | 47 | 16.1% |

### B9 concordance 待办清单

共 **39** 个词族需 concordance 判定（含 2 个低信度已定项）。

| Type | Freq_Tar | 待定层 | 竞争读法 |
|---|---:|---|---|
| `GOOD` | 949 | act | act 层待定：good+better 归并，comparative 多嵌于目标态框架（make it better=A3）vs 评价（A1）；LL 全组最高，须查〔沿用组 2〕 |
| `language` | 642 | 维度一、维度三 | 维度三待定：your language background/first language(C1) vs academic language(G2 Wording)；本组理论枢纽词〔沿用组 2〕 |
| `academic` | 841 | 维度一 | 维度一待定：属 register，手册列 tone/formal/register 为 PENDING〔沿用组 2〕 |
| `strengths` | 165 | act | act 层待定：反馈小标题"Strengths:"（元话语 NA）vs 归功（A1）；且属 strong 词族，按 v3 强制查询规则不得凭词形定。注：组 2 为归并 STRENGTH，本组为 strengths 单独入选，系口径效应 |
| `english` | 74 | 维度三 | 手册明列：指语言系统（correct English）→C1；作文体修饰（English essay）→NA。两读法维度一均为 NA〔沿用组 2〕 |
| `ARTICLE` | 167 | 维度一 | 维度一待定：英语冠词(G2-Grammar)vs 引用的文章(G1-Development)；L2 语法标记的关键判别点〔沿用组 2〕 |
| `use` | 897 | 维度一、act | 维度一与 act 层皆待定；内容动词类。注：组 2 为归并 USE（use+using），本组为 use 单独入选——交接文档 §三 预告的口径效应实例 |
| `suggestions` | 160 | act | act 层待定：反馈小标题"Suggestions:"（元话语 NA）vs 名词化建议行为（A3）〔沿用组 2〕 |
| `check` | 144 | 维度一 | 维度一待定：check your spelling(G2)vs check your logic(G1)；手册 A3 明示〔沿用组 2〕 |
| `patterns` | 56 | 维度一 | 维度一待定：error patterns(G2)vs sentence patterns(G2-Local)vs 论证模式(G1)〔沿用组 2〕 |
| `formal` | 364 | 维度一 | 维度一待定（register）；命名目标态而非评价，act 层不赋值〔沿用组 2〕 |
| `strong` | 711 | act | 手册 v3 强制查询清单（A1/A3 争议），不得凭词形归类〔沿用组 2〕 |
| `understandable` | 62 | 维度一、低信度复核 | 维度一待定（clear 系）；act 低信度：作为"低门槛褒扬"（your English is understandable）与 A1 定义是否相符须查〔沿用组 2〕 |
| `advice` | 128 | act | act 层待定：反馈小标题（NA）vs my advice is to…（A3）〔沿用组 2〕 |
| `subject` | 181 | 维度一 | 维度一待定：subject-verb agreement(G2-Grammar)vs the subject of your essay(G1)〔沿用组 2〕 |
| `write` | 264 | act | act 层待定：when you write（描述 NA）vs write this as…（A3）〔沿用组 2〕 |
| `CLEAR` | 1289 | 维度一、act | 维度一待定（手册 clear 系）；act 层待定：clear(A1)vs clearer 目标态框架(A3)〔沿用组 2〕 |
| `natural` | 49 | 维度一、act、维度三 | 三层皆待定：sounds natural 是否以母语者语感为隐含标准（C1）；若判 C1 则维度一二依规则归 NA〔沿用组 2〕 |
| `only` | 333 | hedge | hedge 层待定：最小化降调（only a few errors=M1）vs 限定（NA）；同组 1 just〔沿用组 2〕 |
| `consistent` | 129 | 维度一 | 维度一待定：consistent tense(G2)vs consistent argument(G1)；同组 2 consistency 口径 |
| `meaning` | 59 | 维度一 | 维度一待定：the meaning is unclear（G1 表意）vs 词义(G2-Wording) |
| `paragraph` | 1699 | 维度一 | 维度一待定：手册明示段落内部组织→G2、段落间安排→G1 |
| `informal` | 190 | 维度一 | 维度一待定（register）；学术语境下标记偏离=负向（同组 1 casual 口径）〔沿用组 2〕 |
| `correct` | 152 | act | act 层待定：correct these errors(A3)vs the correct form(NA)〔沿用组 2〕 |
| `important` | 323 | act | act 层待定：an important point(A1)vs it is important to…(A3 框架)〔沿用组 2〕 |
| `worth` | 64 | act | act 层待定：it's worth adding X＝隐性建议（A3）vs 价值评价（A1）；与组 9 deserves 同构 |
| `topic` | 602 | 维度一 | 维度一待定：the topic of your essay(G1-Ideas)vs topic sentence(G2/G1 边界)〔沿用组 2〕 |
| `emotional` | 217 | 维度一 | 维度一待定：emotional language(G2-Wording/register)vs emotional appeal(G1-Ideas)；亦可能为议题残留〔沿用组 2〕 |
| `unclear` | 153 | 维度一 | 维度一待定（手册 clear 系）；负向评价〔沿用组 2〕 |
| `final` | 414 | 维度一 | 维度一待定：your final paragraph(G1-Structure)vs"Final thoughts:"小标题(NA)〔沿用组 2〕 |
| `consistency` | 105 | 维度一 | 维度一待定：consistency of tense(G2)vs of argument(G1)〔沿用组 2〕 |
| `clearly` | 502 | 维度一 | 维度一待定（clear 系）；方式副词，act 层不赋值〔沿用组 2〕 |
| `suggested` | 86 | act | act 层待定：the suggested revision（NA）vs I suggested（A3）〔沿用组 2〕 |
| `possible` | 192 | hedge | hedge 层待定：it is possible that（M1）vs possible improvements（NA）〔沿用组 2〕 |
| `confusing` | 56 | 维度一 | 维度一待定（clear 系）；手册 A2 词族例明列 confusing〔沿用组 5〕 |
| `briefly` | 119 | hedge | hedge 层待定：briefly explain 削减要求强度（M1）vs 单纯方式副词（NA）〔沿用组 2〕 |
| `direct` | 129 | 维度一、维度三 | 维度三待定（先验较低）：German writing is direct（文化—语用框架，C1）vs be more direct(G2)/direct quotation(NA)〔沿用组 6〕 |
| `remove` | 102 | 维度一 | 维度一待定：remove this word(G2)vs remove this paragraph(G1)；建议动词 |
| `citation` | 132 | 维度一 | 维度一待定：引用来源的使用(G1-Development)vs 引用格式(G2-Mechanics) |

### B10 高效应量词位（LR ≥ 1.5）

| Type | LL | LR | 维度一 | act | hedge |
|---|---:|---:|---|---|---|
| corrections | 89.818 | 3.934 | G2/Correctness | NA | NA |
| english | 48.406 | 2.536 | NA | NA | NA |
| slightly | 36.018 | 2.426 | NA | NA | M1 |
| expressions | 24.786 | 2.057 | G2/Wording | NA | NA |
| patterns | 27.794 | 2.027 | PENDING | NA | NA |
| vocabulary | 19.937 | 1.960 | G2/Wording | NA | NA |
| comment | 26.932 | 1.953 | NA | NA | NA |
| recurring | 35.100 | 1.902 | NA | NA | NA |
| luck | 16.100 | 1.875 | NA | NA | NA |
| probably | 23.792 | 1.740 | NA | NA | M1 |
| plural | 17.111 | 1.644 | G2/Grammar | NA | NA |
| understandable | 20.614 | 1.522 | PENDING | A1 | NA |
| thank | 16.288 | 1.501 | NA | NA | NA |
