# 组 9／组 10 关键词质性分类编码报告（concordance 消解后）

> **状态：现行口径**
> 本文档基于 concordance 全部消解后的编码撰写，取代 [`group09_10_coding.md`](group09_10_coding.md)
> 中的一切占比数字。原文档保留为编码过程的审计轨迹，不再更新。
> 完整附表见 [`group09_tables.md`](group09_tables.md)、[`group10_tables.md`](group10_tables.md)，
> 跨组统计见 [`final_report.md`](final_report.md)。

## Baseline ↔ Generic

> **编码方案**：手册 v3　**占比分母**：各层已定标签数
> **组 9**：Baseline vs Generic（目标 = Baseline），131 词位　**组 10**：Generic vs Baseline（目标 = Generic），121 词位
> **对比性质**：Baseline 是**完全无身份标记**的对照条件。本对回答「加上非母语者标记，相对于不加任何标记，改变了什么」。
> **未决项**：0（原 9 个 PENDING 单元格已由 concordance 消解）

---

## 一、结果摘要

| 层 | 组 9（Baseline 侧） | 组 10（Generic 侧） |
|---|---|---|
| 维度一 Focus | 已定 69：**G1 55（79.7%）**／ G2 14（20.3%） | 已定 53：**G2 35（66.0%）**／ G1 18（34.0%） |
| 维度二 act | 已定 36：A3 21（58.3%）／ A2 10／ A1 5（13.9%） | 已定 24：A3 14（58.3%）／ A1 5（20.8%）／ A2 5（20.8%） |
| 维度二 hedge | 已定 5 | 已定 6 |
| 维度三 | 已定 **0** | 已定 **1（`english`）** |

**一句话概括**：两个方向一致——无标记条件的过量词汇偏全局（G1 79.7%），非母语者标记条件偏局部（G2 66.0%），差距 45.7 pp；且**仅仅加上「非母语者」这一标记，就足以让 `english` 作为语言系统指称过量出现**，而 Baseline 侧维度三为零。

---

## 二、维度一：45.7 pp 的差距

### 2.1 组 9（Baseline 侧）：Ideas 独大

| 主类 | 子类 | 词位数 |
|---|---|---:|
| G1 | **Ideas** | **38** |
| G1 | Development | 11 |
| G1 | Global Structure | 6 |
| G2 | Mechanics | 6 |
| G2 | Local Structure | 3 |
| G2 | Wording | 3 |
| G2 | Correctness | 2 |

G1 的 55 项中 Ideas 占 38 项（69%）。代表词：`CLAIM`(1689)、`COUNTERARGUMENT`(409)、`SHARPEN`(143)、`RELY`(132)、`evidence`(1543)。无标记条件下的反馈差异几乎全部落在论证内容上。

### 2.2 组 10（Generic 侧）：Grammar／Wording 双线

| 主类 | 子类 | 词位数 |
|---|---|---:|
| G2 | **Grammar** | **11** |
| G2 | **Wording** | **11** |
| G2 | Correctness | 5 |
| G2 | Mechanics | 4 |
| G2 | Local Structure | 4 |
| G1 | Ideas | 11 |
| G1 | Development | 5 |
| G1 | Global Structure | 2 |

与组 2（Generic vs L1）的结构完全一致：Grammar 与 Wording 各 11 项并列为主。**无论对照的是母语者条件还是无标记条件，非母语者标记都产出同一份局部清单**——这个稳定性本身是结果，说明该清单是标记本身的产物，不依赖于对照对象。

---

## 三、维度三：Baseline 的零锚定了整条梯度

| target corpus | C1 词形数 | 词形 |
|---|---:|---|
| German | 8 | `german`、`english`、`SPEAKER`、`transfer`、`influenced`、`false`、`speaking`、`friends` |
| Chinese | 2 | `chinese`、`english` |
| Generic | 1 | `english` |
| L1 | **0** | — |
| **Baseline** | **0** | — |

组 10 的 `english`（74 词次 vs Baseline 侧 13，LR 2.54）经 concordance 判定为 C1——与组 2 的判定一致。

**Baseline 与 L1 同为零，这一点是整条梯度的锚**。它排除了一种替代解释：C1 词汇不是「谈论写作时的自然背景噪音」，因为在没有任何身份标记时它根本不出现。只有当提示词说明写作者是非母语者时，反馈才开始把「英语」作为一个需要习得的系统来谈。

### 3.1 组 9 的零同时排除了另一种解释

组 9 是 Baseline 相对 Generic 的过量词。如果 Baseline 条件下反馈有任何自己的身份框架词汇（例如泛指的 "native"、"fluency"），它们应当在此出现。**实际结果是零**，说明这不是「两侧各有各的身份词汇、只是词形不同」，而是**单侧现象**。

---

## 四、维度二：A3 占比在两侧几乎相同

| | 组 9 | 组 10 |
|---|---:|---:|
| A3 占比 | 58.3%（21/36） | 58.3%（14/24） |
| A2 占比 | 27.8%（10） | 20.8%（5） |
| A1 占比 | 13.9%（5） | 20.8%（5） |

**A3 的比重在两侧完全一致**（58.3%），说明「以建议为主」是这套反馈的共同体裁特征，不随身份标记变动。变动的是 A1/A2 的相对权重：Baseline 侧批评略多（27.8% vs 20.8%），Generic 侧赞扬略多（20.8% vs 13.9%）。但两侧的 A1 绝对数都是 5，A2 分别是 10 与 5，**分母 36 与 24 尚不足以支撑「非母语者标记下赞扬更多」的结论**，只能与组 1/组 2 的同向观察（17.8% → 34.5%）并列作为趋势提示。

组 10 的 A1 五项中，`GOOD`、`strong`、`strengths` 经强制查询清单判定，`understandable` 为低信度（同组 2、组 7 的争议项），`easy` 为词形判定。

### 4.1 hedge：`would` 的两层在本对中都判 NA

组 9 的 `would`（739 词次）经 concordance 判定 **act=NA、hedge=NA**——与组 1（L1 侧，act=A3 54%、hedge=M1 55%）相反。两组都有索引依据，对照侧不同（Generic vs Generic 的另一方向），故不构成不一致。

这使组 9 的 M1 从消解前的 6 项降为 5 项（`fairly`、`might`、`risk`、`somewhat`、`likely`）。**这是十二组中唯一一处 concordance 消解使某层标签数减少的地方**，值得在方法部分作为「查证并非只做加法」的例子。

---

## 五、concordance 消解带来的变化

| 指标 | 组 9 消解前 → 后 | 组 10 消解前 → 后 |
|---|---|---|
| 维度一 G2 占比 | 20.3% → **20.3%**（无变化） | 68.8%（33/48，另 4 未决）→ **66.0%**（35/53） |
| act A3 占比 | 58.3% → 58.3% | 58.3% → 58.3% |
| M1 词位 | 6 → **5**（`would` 降为 NA） | 5 → **6**（`possible`） |
| C1 词位 | 0 → 0 | 0 → **1**（`english`） |

组 9 定夺 40 词位／44 单元格，组 10 定夺 45 词位／51 单元格。

组 10 的四个维度一未决项去向：`formal`→G2/Wording、`subject`→G2/Grammar、`clearly`→G1/Ideas、`confusing`→G2/Local Structure。三项落 G2、一项落 G1，分母从 48 增至 53，G2 占比下降 2.8 pp。**方向未变**。

组 10 的实质变化在维度三（`english`→C1），与组 2 同理：占比杠杆极小，理论杠杆最大。

几处推翻原判的记录：

| 组 | 词形 | 原判 | 查证后 |
|---|---|---|---|
| 9 | `discussion` | G1/**Ideas** | G1/**Development**（子类改判） |
| 9 | `would` | act 待定、hedge=M1 | act=**NA**、hedge=**NA** |
| 9 | `authority` | 未决 | **G1/Ideas**（与组 1 判 NA 相反，两者对照侧不同） |
| 10 | `direct` | G2/Wording | **G1/Ideas**、维度三 NA |
| 10 | `story` | NA | **G1/Development** |

`authority` 在组 1（L1 侧）判 NA、在组 9（Baseline 侧）判 G1/Ideas，是跨语料编码差异的一例。两者都有索引依据；详见 [`final_report.md`](final_report.md) 第 4 节列出的 17 个此类词形。

---

## 六、遗留问题

1. **低信度项**：组 9 的 `authority`、组 10 的 `understandable`。后者是贯穿组 2／7／10 的同一争议项（低门槛褒扬是否构成 A1），应统一裁定而非逐组处理。
2. **组 9 与组 1 的高度相似**：两组的 Baseline 与 L1 侧清单重叠度很高（`CLAIM`、`SHARPEN`、`correctness`、`rather`、`prose`、`distract` 等均在两组出现）。这与组 11/12 的直接对比结果一致——Baseline ≈ L1。若论文采用「Baseline 作为 L1 的替代对照」的处理，本组提供支持证据。
3. **A1/A2 的权重差异**（第四节）分母不足，只能作为趋势提示。
4. **议题内容残留**：组 9 的 `paper`（265，文本指称）、组 10 的 `luck`／`thank`／`comment`（人际礼貌与元话语），均为两层 NA。

---

## 附表

完整编码表与分布统计见 [`group09_tables.md`](group09_tables.md)、[`group10_tables.md`](group10_tables.md)，
由 `scripts/analyze.py 9` 与 `scripts/analyze.py 10` 生成。
