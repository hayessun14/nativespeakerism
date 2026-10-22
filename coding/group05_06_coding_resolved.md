# 组 5／组 6 关键词质性分类编码报告（concordance 消解后）

> **状态：现行口径**
> 本文档基于 concordance 全部消解后的编码撰写，取代 [`group05_06_coding.md`](group05_06_coding.md)
> 中的一切占比数字。原文档保留为编码过程的审计轨迹，不再更新。
> 完整附表见 [`group05_tables.md`](group05_tables.md)、[`group06_tables.md`](group06_tables.md)，
> 跨组统计见 [`final_report.md`](final_report.md)。

## Chinese ↔ German（RQ2 的决定性一对）

> **编码方案**：手册 v3　**占比分母**：各层已定标签数
> **组 5**：Chinese vs German（目标 = Chinese），56 词位　**组 6**：German vs Chinese（目标 = German），59 词位
> **对比性质**：两侧**都是 L2 条件，且都指明了母语**。差异只在于指明的是哪一门母语。
> **未决项**：0（原 4 个 PENDING 单元格已由 concordance 消解）

> ### ⚠ 本对的特殊地位
> 这是全研究唯一一对能够直接回答「反馈是否针对具体母语做差异化处理」的对比。
> 组 3／组 4 只能说明「指明母语 vs 未指明」，本对才能说明「指明中文 vs 指明德语」。

---

## 一、结果摘要

| 层 | 组 5（Chinese 侧） | 组 6（German 侧） |
|---|---|---|
| 维度一 Focus | 已定 25：**G1 16（64.0%）**／ G2 9（36.0%） | 已定 26：**G2 18（69.2%）**／ G1 8（30.8%） |
| 维度二 act | 已定 14：A3 7／ A2 5／ A1 2 | 已定 4：A3 3／ A2 1／ A1 0 |
| 维度二 hedge | 已定 1：`some` | 已定 4：`likely`、`often`、`few`、`quite` |
| 维度三 | 已定 1：**C1 `chinese`** | 已定 7：**C1 七项** |

**一句话概括**：两个方向一致指向同一结论——**德语标记比中文标记更强地拉动局部词汇**（G2 69.2% vs 36.0%，差距 33.2 pp），且德语标记触发了**七个**跨语言框架词位（含显性迁移词 `transfer`、`false friends`），而中文标记只有一个身份命名词。这与「中文母语迁移诊断」的预期方向相反。

---

## 二、维度三：本研究最强的结果

### 2.1 组 6 的七个 C1

| Type | Freq_Tar (German) | Freq_Ref (Chinese) | LL | LR | 性质 |
|---|---:|---:|---:|---:|---|
| `german` | 491 | **0** | 668.504 | **9.902** | 身份命名 |
| `english` | 508 | 138 | 216.155 | 1.843 | 语言系统指称 |
| `SPEAKER` | 113 | 25 | 58.482 | 2.139 | 身份命名（German speaker） |
| `transfer` | 43 | 6 | 30.549 | 2.804 | **显性迁移框架** |
| `false` | 49 | 9 | 29.321 | 2.407 | **显性迁移框架**（false friends） |
| `speaking` | 61 | 21 | — | 1.501 | 身份命名 |
| `friends` | 46 | 20 | — | 1.156 | **显性迁移框架**（false friends） |

`german` 的 Freq_Ref 为 **0**：在 348 篇 Chinese 条件的反馈中，"German" 一次都没出现；而在 German 条件中出现 491 次。LR 9.902 是全研究最高值，LL 668.504 亦然。

更关键的是 **`transfer`、`false`、`friends` 三项构成显性的跨语言迁移框架**——"transfer from German"、"false friends" 是元语言学术语，把文本特征直接归因于母语。这类词汇在 Chinese 条件中**完全不出现**。

### 2.2 组 5 的一个 C1

Chinese 侧只有 `chinese`（61 词次，Freq_Ref 1，LR 5.968），且是身份命名，**没有任何显性迁移词汇**。

### 2.3 这一不对称推翻了组 3 的诱人读法

组 3 曾观察到 Chinese 条件的局部词汇清单（冠词、单复数、逗号、流水句）与 L2 文献中的「中文迁移错误目录」高度吻合，并提示这可能被误读为「针对中文的特异性诊断」。本对给出了决定性反驳：

| | Chinese 条件 | German 条件 |
|---|---:|---:|
| 局部词汇占比（本对内） | 36.0% | **69.2%** |
| `ARTICLE` 词次 | 272 | **479** |
| 显性迁移框架词 | **0** | 3（`transfer`、`false`、`friends`） |
| C1 词位总数 | 1 | **7** |

**德语是有冠词的语言，但 German 条件谈冠词谈得比 Chinese 条件多得多**（479 : 272）。如果反馈在做母语特异性诊断，这个方向应当反过来。四项指标一致表明：不是「针对中文的迁移诊断」，而是「德语标记整体上更强烈地激活了跨语言框架与局部形式关注」。

至于为何德语标记的激活强度远高于中文标记，本研究的数据不足以回答。可能与训练数据中德英对比语言学文献的密度有关，也可能与 "German speaker"、"false friends" 这类搭配在英语中的固化程度有关。**这属于超出本设计的推测，应在讨论部分标为待检验假设，不作为结论。**

---

## 三、维度一：方向明确，但两侧的 G1 内涵不同

| 组 5（Chinese 侧，G1 主导） | 组 6（German 侧，G2 主导） |
|---|---|
| Global Structure 6：`organization`、`body`、`restate`、`organizing`、`paragraphs`、`conclusion` | Wording 6：`style`、`phrasing`、`register`、`academic`、`emotionally`、`placeholder` |
| Ideas 6：`thesis`、`ideas`、`readers`、`discuss`、`debatable`、`logic` | Ideas 6：`argumentation`、`basis`、`direct`、`question`、`precise`、`raise` |
| Development 4：`specific`、`details`、`data`、`inaccurate` | Local Structure 4：`order`、`clauses`、`rhetorical`、`cut` |
| Local Structure 4：`level`、`confusing`、`clarity`、`RUN-ON` | Grammar 3：`ARTICLE`、`patterns`、`noun` |
| Wording 2：`awkward`、`choice` | Mechanics 3：`commas`、`capitalization`、`punctuation` |
| Grammar 1、Mechanics 1、Correctness 1 | Correctness 2、Global Structure 2 |

Chinese 侧的 G1 重心在 **Global Structure（6 项）**——篇章组织、主体段、结论、重述论点；German 侧的 G2 重心在 **Wording（6 项）**——文体、语域、措辞。

值得注意的是，German 侧的 G1 也有 6 个 Ideas 项，但性质不同：`argumentation`、`basis`、`direct`、`precise` 更接近**论证风格**的评价，而 Chinese 侧的 `thesis`、`ideas`、`logic` 更接近**论证内容**本身。这个区别在当前编码粒度下无法形式化，仅作观察记录。

---

## 四、维度二：组 6 的 act 层几近空白

| | 组 5 | 组 6 |
|---|---|---|
| act 已定 | 14（A3 7、A2 5、A1 2） | **4**（A3 3、A2 1、A1 0） |
| hedge 已定 | 1（`some`） | **4**（`likely`、`often`、`few`、`quite`） |

组 6 的 act 层只有 4 项（`watch`、`rewrite`、`cut` 为 A3，`placeholder` 为 A2），**分母过小，不作解读**。

但两侧的 hedge 对照值得记录：German 侧 4 项 vs Chinese 侧 1 项。这与编码过程报告中的一处说法相反——原报告曾称「Chinese 条件在两对中都更少被缓和」，该说法当时忽略了组 3 的 `usually`（115 词次）。**现更正为**：本对中 German 侧的 hedge 词位多于 Chinese 侧（4 : 1），但两侧分母都极小，且 hedge 层只有 M1 一个非 NA 取值，占比恒为 100%、不含信息。**这个对照只能以词位数陈述，不能以比例陈述。**

组 5 的 A1 两项中，`effort`（信度 L）经 concordance 判定为 **A1**——归功对象是写作者的努力而非文本属性。这一判定与手册对 praise 的定义存在张力（Hyland & Hyland 的 praise 指向文本属性），保留 A1 但标低信度，复核时应优先重看。

---

## 五、concordance 消解带来的变化

| 指标 | 组 5 消解前 → 后 | 组 6 消解前 → 后 |
|---|---|---|
| 维度一 G2 占比 | 37.5%（9/24，另 1 未决）→ **36.0%**（9/25） | 69.2% → **69.2%**（无变化） |
| act A3 占比 | 53.8%（7/13）→ **50.0%**（7/14） | 75.0% → 75.0% |
| M1 词位 | 1 → 1 | 3 → **4**（`few`） |
| C1 词位 | 1 → 1 | 7 → 7 |

组 5 定夺 20 词位／22 单元格，组 6 定夺 26 词位／32 单元格。**两组的结论方向均未改变**；组 5 的 `paragraphs`→G1/Global Structure 使 G2 占比下降 1.5 pp，组 6 的 `few`→M1 使 hedge 词位增至 4。

组 6 值得注意的一点：七个 C1 中，只有 `english` 是经 concordance 定夺的（`src=c`），其余六项（`german`、`SPEAKER`、`transfer`、`false`、`speaking`、`friends`）在第一轮即以高信度直接判定——它们的 C1 归属不依赖索引行，词形本身即已明示跨语言框架。**这是本研究中证据最硬的一组标签。**

几处推翻原判的记录：

| 组 | 词形 | 原判倾向 | 查证后 |
|---|---|---|---|
| 5 | `confusing` | 偏 clear 系（待定） | **G2/Local Structure** |
| 5 | `clarity` | 待定 | **G2/Local Structure** |
| 5 | `inaccurate` | 偏 G2（用词不准） | **G1/Development**（事实不准） |
| 5 | `using`、`effects`、`summary`、`action`、`tool` | 维度一待定 | 全部 **NA** |
| 6 | `direct` | 待定（C1 可能） | 维度一 **G1/Ideas**、维度三 **NA** |
| 6 | `natural` | 三层皆待定（C1 可能） | 三层全部 **NA** |

`direct` 与 `natural` 两项特别值得记录：二者都曾被怀疑承载「以母语者语感为隐含标准」的 C1 框架（"German writing is direct"、"sounds natural"），查证后**均判为 NA**。若当初凭理论预期把它们编为 C1，German 侧的 C1 会虚增到 9 项。**这是窄口径 C1 定义发挥作用的实例：只有显性的迁移归因或身份命名才计入，隐含的母语者标准不计。**

---

## 六、遗留问题

1. **低信度项**：组 5 的 `effort`（A1，见第四节争议）。组 6 无低信度项。
2. **`chinese` 与 `german` 的 C1 子类**均未细分（Identity marking vs Transfer framing）。组 6 的 `transfer`／`false`／`friends` 已明确属迁移框架，但 `german` 本身的子类仍需单独标注。
3. **组 6 act 层分母仅 4**：不应产出任何 act 层的数值结论。
4. **德语激活强度的成因**（见 2.3）超出本设计，只能作为待检验假设。
5. **议题内容残留**：组 5 的 `schools`（109）等；组 6 的 `moment`（107）、`common`（223）——后者属正常化框架，依手册不入 M1，编码为 NA。

---

## 附表

完整编码表与分布统计见 [`group05_tables.md`](group05_tables.md)、[`group06_tables.md`](group06_tables.md)，
由 `scripts/analyze.py 5` 与 `scripts/analyze.py 6` 生成。
