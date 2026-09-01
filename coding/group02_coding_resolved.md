# 组 2 关键词质性分类编码报告（concordance 消解后）

> **状态：现行口径**
> 本文档基于 concordance 全部消解后的编码撰写，取代 [`group02_coding.md`](group02_coding.md)
> 中的一切占比数字。原文档保留为编码过程的审计轨迹，不再更新。
> 完整附表见 [`group02_tables.md`](group02_tables.md)，跨组统计见 [`final_report.md`](final_report.md)。

## Generic → L1（目标语料 = Generic 条件，参照语料 = L1 条件）

> **编码方案**：手册 v3　**编码对象集**：本清单全部 131 词位　**占比分母**：各层已定标签数
> **服务的 RQ**：RQ1　**对比性质**：组 1 的反方向，与组 1 构成同一对语料，可直接对读
> **未决项**：0（原 6 个 PENDING 单元格已由 concordance 消解）

---

## 一、结果摘要

| 层 | 已定标签 | 分布 | N/A |
|---|---:|---|---:|
| 维度一 Focus | 54 | **G2 29（53.7%）／ G1 25（46.3%）** | 77 |
| 维度二 act | 29 | A3 15（51.7%）／ **A1 10（34.5%）**／ A2 4（13.8%） | 102 |
| 维度二 hedge | 8 | M1 8 | 123 |
| 维度三 | 1 | **C1 = 1（`english`）** | 130 |

**一句话概括**：与组 1 对读，同一对语料的两个方向给出一致的结论——非母语者标记下的过量词汇偏局部（G2 53.7% vs L1 侧 30.6%），且赞扬词汇的比重显著更高（A1 34.5% vs L1 侧 17.8%）；维度三出现本研究**唯一一个在未指明母语的条件下成立的 C1**。

---

## 二、维度一：局部倾斜，且语法—词汇双线

已定 54 项中 G2 占 29 项（53.7%）。与组 1 的 G2 30.6% 对读，同一对语料的两个方向**互相印证**：过量词汇的局部/全局倾向随身份标记而移动，差距 23.1 pp。

| 主类 | 子类 | 词位数 | 代表词 |
|---|---|---:|---|
| G1 | Ideas | 15 | `main`、`IDEA`、`topic`、`OPINION`、`statement`、`accurate` |
| G2 | Wording | 10 | `language`、`academic`、`WORD`、`vocabulary`、`expressions`、`informal` |
| G2 | Grammar | **10** | `grammar`、`tense`、`verb`、`ARTICLE`、`past`、`form`、`agreement`、`patterns`、`consistency`、`subject` |
| G1 | Development | 6 | `example`、`facts`、`details`、`relevant`、`USE` |
| G2 | Correctness | 4 | `corrections`、`accuracy`、`proper`、`CLEAR`(否) |
| G1 | Global Structure | 4 | `introduction`、`organization`、`end`、`restate` |
| G2 | Local Structure | 3 | `sentences`、`long`、`shorter` |
| G2 | Mechanics | 2 | `spelling`、`check` |

G2 的 29 项中，**Grammar 10 项与 Wording 10 项并列为主**。Grammar 一支构成一份具体清单：时态、动词形式、冠词、主谓一致、过去式。这与组 3（Chinese 条件）的语法清单高度重叠——但组 3 的对照侧正是本组的目标侧，说明**这份语法清单在「未指明母语」这一层就已经成形**，不是指明中文之后才出现的。

### 2.1 `english` 与 `language` 的分野

本组两个理论枢纽词经 concordance 判定后走向不同：

| 词形 | Freq_Tar | Freq_Ref | LR | 维度一 | 维度三 |
|---|---:|---:|---:|---|---|
| `english` | 74 | 16 | 2.248 | NA | **C1** |
| `language` | 642 | 285 | 1.210 | G2/Wording | NA |

`english` 判为 C1：主导用法是把英语作为**语言系统**来谈（"correct English"、"natural English"），而非作为文体修饰（"English essay"）。`language` 判为 G2/Wording、维度三 NA：主导用法是 "academic language"，即措辞层面，不是 "your language background"。

两词同族而异判，且都经 concordance 定夺，这个分野本身是结果：**非母语者标记触发的是对「英语」这一系统的指称，而不是对写作者语言背景的指称**。后者要到指明具体母语（组 3、组 6/7）才出现。

---

## 三、维度二 act 层：赞扬比重是组 1 的两倍

已定 29 项：A3 15（51.7%）、A1 10（34.5%）、A2 4（13.8%）。

| 标签 | 词位 |
|---|---|
| A1 Praise | `GOOD`、`STRENGTH`、`understandable`、`strong`、`easy`、`balanced`、`meaningful`、`effective`、`powerful`、`accurate` |
| A2 Criticism | `too`、`informal`、`difficult`、`unclear` |
| A3 Suggestion | `suggestions`、`try`、`advice`、`IMPROVE`、`avoid`、`correct`、`adding`、`check`、`suggested`、`write`、`must`、`restate`、`could`、`reduce`、`choose` |

A1 占比 34.5%，接近组 1 的两倍（17.8%）。四个 LL 最高的 A1 词位——`GOOD`（949 词次，LL 155.6 全组最高）、`STRENGTH`（257）、`strong`（711）——**全部经 concordance 强制查询清单判定为 A1**，不是凭词形归类。这一点很重要：这三个词的竞争读法（目标态框架 "make it stronger"、反馈小标题 "Strengths:"）如果成立，A1 的比重会大幅下降。查证结果是 `strong` 91% 为 A1、`STRENGTH` 与 `GOOD` 亦判 A1，故这个差异是实的。

### 3.1 `understandable` 值得单列

`understandable`（62 词次，LR 1.600）编为 G1/Ideas + A1，信度 **L（低）**。它是一种「低门槛褒扬」——"your English is understandable" 承认可理解，但同时把标准设在了可理解性而非质量上。它是否符合 Hyland & Hyland 的 praise 定义，本身就有争议；本研究保留 A1 但标低信度，是为了让这个判断在复核时可被推翻。

该词只出现在 Generic 与 German 条件（组 2、7、10），**不出现在 L1 与 Baseline**。若后续要论证「非母语者标记下的赞扬带有降格性质」，此词是关键证据，但需要先解决它的编码争议。

### 3.2 hedge 层：8 项，本研究最多

M1 八项：`some`（939）、`may`（404）、`could`（499，与 A3 共现）、`possible`（192）、`sometimes`（148）、`briefly`（119）、`probably`（59）、`slightly`（58）。

其中 `briefly` 与 `possible` 经 concordance 判定为 M1（分别 71% 与查证确认），`could` 两层分判（act=A3 53%、hedge=M1 53%）。`only`（333）判为 hedge=**NA**——限定而非最小化降调。

需要说明手册的排除规则：`please`、`i`、`common`、`thank`、`sharing`、`luck` 均**不入 M1**。前三者属人称归因与正常化框架，后三者属人际礼貌（paired acts），二者都是缓和策略但不是 Hyland & Hyland 意义上的 hedge。本组这类词汇密集出现，若放宽口径，M1 会虚增一倍以上。

---

## 四、维度三：一个 C1，且它改写了原结论

`english`（74 词次，Freq_Ref 16，LR 2.248）判为 **C1**。

这是**编码过程报告中未曾预期的结果**。原报告（及组 5/6、7/8、9/10 的过程报告）都记载「C1 仅见于 Chinese 与 German 条件」，因为当时 `english` 在 Generic 条件下的维度三是 PENDING。查证后它成立，梯度随之变为：

| target corpus | C1 词形数 | 词形 |
|---|---:|---|
| German | 8 | `german`、`english`、`SPEAKER`、`transfer`、`influenced`、`false`、`friends`、`speaking` |
| Chinese | 2 | `chinese`、`english` |
| **Generic** | **1** | **`english`** |
| L1 | 0 | — |
| Baseline | 0 | — |

**理论含义变了，而且变强了**。原结论把身份框架系于「指明了哪个母语」；新结论把它系于「是否标记了非母语身份」——只要标记，就出现语言系统框架（`english`），指明母语后再叠加身份命名（`chinese`／`german`）与迁移框架（`transfer`、`influenced`、`false friends`）。这是一条两段式的梯度，而不是一个二元开关。

---

## 五、concordance 消解带来的变化

本组 **49 个词位、58 个单元格**经查证定夺（维度一 31、act 18、hedge 5、维度三 4），是十二组中定夺量最大的一组。

| 指标 | 消解前 | 消解后 | 变化 |
|---|---|---|---|
| 维度一 G2 占比 | 54.0%（27/50，另 3 项未决） | 53.7%（29/54） | −0.3 pp |
| act A3 占比 | 51.7% | 51.7% | 无 |
| M1 词位 | 7 | **8** | +1（`possible`） |
| C1 词位 | 0 | **1** | +1（`english`） |

维度一四个未决项的去向：`clearly`→G1/Ideas、`formal`→G2/Wording、`subject`→G2/Grammar、`complete`→NA。两两抵消，占比几乎不动。

**唯一实质变化在维度三**（见第四节）。这说明一件方法上的事：杠杆筛查当初把 `english` 的维度三判为「必查」是对的——它对占比的影响微乎其微（维度三分母从 0 变 1），但对**结论的定性**影响最大。占比杠杆与理论杠杆不是一回事。

几处 concordance 推翻原判或收紧标签的记录：

| 词形 | 原判 | 查证后 |
|---|---|---|
| `USE` | 维度一 NA | **G1/Development**（your use of evidence 占主导） |
| `important` | 待定（A1 vs A3 框架） | act=**NA**（"it is important to" 为框架而非评价） |
| `CLEAR` | 待定 | 维度一=G1/Ideas，act=**NA** |
| `people`、`she`、`he`、`her`、`become` | 疑似议题残留 | 全部 **NA**，确认为残留 |
| `complex`、`final`、`reduce`、`emotional`、`neutral` | 维度一待定 | 全部 **NA** |

后两行共 10 个词位查证后落入 NA，即退出维度一分母。这是本组维度一分母仅 54/131 的主要原因——**不是编码保守，而是过量词汇里确有相当比例并不指示反馈焦点**。

---

## 六、遗留问题

1. **低信度项 2 个**：`understandable`（见 3.1，编码争议未解决）、`effort`（act=NA，已查证）。
2. **A1 的目标态框架**：三个高频 A1 已查证，但 `easy`、`meaningful`、`effective`、`powerful`、`balanced` 五项为词形判定，存在同类风险。
3. **`consistency` 的子类**：判为 G2/Grammar（时态一致），但 "consistency of argument" 读法未被完全排除，查证覆盖率 38%。
4. **议题内容残留**：`society`、`government`、`women`、`modern`、`today`、`live`、`students` 及查证确认的 `people`／`she`／`he`／`her`／`become`，共约 12 项，均为两层 NA，移除后清单总数 131 → 119。

---

## 附表

完整编码表（附表 A）与分布统计（B1–B10）见 [`group02_tables.md`](group02_tables.md)，
由 `scripts/analyze.py 2` 生成。
