# 组 7／组 8 关键词质性分类编码报告（concordance 消解后）

> **状态：现行口径**
> 本文档基于 concordance 全部消解后的编码撰写，取代 [`group07_08_coding.md`](group07_08_coding.md)
> 中的一切占比数字。原文档保留为编码过程的审计轨迹，不再更新。
> 完整附表见 [`group07_tables.md`](group07_tables.md)、[`group08_tables.md`](group08_tables.md)，
> 跨组统计见 [`final_report.md`](final_report.md)。

## German ↔ Generic

> **编码方案**：手册 v3　**占比分母**：各层已定标签数
> **组 7**：German vs Generic（目标 = German），77 词位　**组 8**：Generic vs German（目标 = Generic），65 词位
> **对比性质**：两侧**都是 L2 条件**。差异是「指明母语为德语 vs 未指明母语」。
> **未决项**：0（原 7 个 PENDING 单元格已由 concordance 消解）

---

## 一、结果摘要

| 层 | 组 7（German 侧） | 组 8（Generic 侧） |
|---|---|---|
| 维度一 Focus | 已定 36：**G2 29（80.6%）**／ G1 7（19.4%） | 已定 36：**G1 29（80.6%）**／ G2 7（19.4%） |
| 维度二 act | 已定 8：A3 3／ A2 3／ A1 2 | 已定 19：A3 12（63.2%）／ A2 4／ A1 3 |
| 维度二 hedge | 已定 6：`often`、`likely`、`usually`、`generally`、`few`、`quite` | 已定 1：`briefly` |
| 维度三 | 已定 **8**：C1 八项 | 已定 **0** |

**一句话概括**：这是六对中分化最彻底的一对——两侧的维度一占比恰好互为镜像（80.6% : 19.4%），差距 61.1 pp，为全研究最大；德语标记侧有 8 个 C1 与 6 个 hedge 词位，未指明母语侧则**各为零与一**。

---

## 二、维度一：一对完美的镜像

两组的分母同为 36，G2/G1 的比例恰好对调。这个对称性不是设计出来的（两份清单的词位数分别是 77 与 65），而是编码结果自然呈现的。

### 2.1 组 7（German 侧）：29 个局部词位

| 子类 | 词位 |
|---|---|
| Wording **12** | `academic`(997)、`language`(795)、`word`(522)、`style`(410)、`phrases`(289)、`check`(243)、`MEAN`(206)、`phrasing`(188)、`register`(73)、`confusion`(53)、`appropriate`(52)、`unnatural`(39) |
| Grammar **7** | `ARTICLE`(479)、`PATTERN`(241)、`NOUN`(107)、`forms`(86)、`plural`(68)、`singular`(55)、`prepositions`(40) |
| Local Structure **7** | `sentences`(694)、`rhetorical`(192)、`SHORT`(174)、`splices`(130)、`order`(118)、`clauses`(73)、`independent`(44) |
| Mechanics 2 | `COMMA`(330)、`double`(73) |
| Correctness 1 | `usage`(122) |

G1 的 7 项为：Ideas 4（`direct`(164)、`argumentation`(112)、`basis`(44)、`raise`(37)）、
Global Structure 2（`structure`(795)、`beginning`(73)）、Development 1（`abstract`(52)）。

德语侧的局部清单同时覆盖**措辞/语域**（Wording 一支最重）与**语法形式**（冠词、名词单复数、介词、动词形式）。`unnatural`（39 词次）被编为 G2/Wording + A2，其「不自然」的判断标准隐含母语者语感——但依窄口径 C1 规则，隐含标准不计入维度三，该词维度三经查证为 NA。

### 2.2 组 8（Generic 侧）：29 个全局词位

| 子类 | 词位 |
|---|---|
| Ideas **15** | `argument`(1761)、`FOCUS`(579)、`clearly`(502)、`ideas`(450)、`point`(431)、`strengthen`(346)、`clarity`(271)、`readers`(263)、`address`(190)、`clarify`(153)、`reasons`(149)、`opposing`(130)、`comparison`(103)、`impact`(102)、`connection`(93) |
| Development **8** | `evidence`(1223)、`SUPPORT`(626)、`specific`(546)、`using`(171)、`research`(155)、`story`(86)、`data`(85)、`details`(49) |
| Global Structure 6 | `conclusion`(734)、`body`(588)、`organization`(396)、`SECTION`(177)、`restate`(134)、`organizing`(56) |

G2 的 7 项为：Mechanics 2（`mechanics`(131)、`fix`(82)）、Local Structure 2（`level`(179)、`confusing`(56)）、
Correctness 1（`errors`(317)）、Grammar 1（`grammar`(658)）、Wording 1（`awkward`(142)）。

未指明母语侧的全局清单以**论证内容**（Ideas 15 项）为主，辅以证据支撑（Development 8）与篇章组织（Global Structure 6）。

### 2.3 与组 5/6 合读

| 条件 | 相对 Generic 的 G2 占比 | 相对对方 L2 的 G2 占比 |
|---|---:|---:|
| German | **80.6%**（组 7） | 69.2%（组 6，vs Chinese） |
| Chinese | 73.7%（组 3） | 36.0%（组 5，vs German） |

德语标记无论对照谁都强烈拉动局部词汇；中文标记只在对照「未指明母语」时如此，一旦对照德语就反转为全局倾向。**这再次确认组 3 提出的梯度解释，并进一步显示这条梯度的上端是德语而非中文。**

---

## 三、维度三：八个 C1，含三个显性迁移框架

| Type | Freq_Tar (German) | Freq_Ref (Generic) | LR | 索引定夺 | 性质 |
|---|---:|---:|---:|---|---|
| `german` | 491 | 3 | **7.35** | — | 身份命名 |
| `transfer` | 43 | 4 | 3.42 | — | **显性迁移** |
| `english` | 508 | 74 | 2.78 | c | 语言系统指称 |
| `SPEAKER` | 113 | 17 | 2.73 | — | 身份命名 |
| `influenced` | 47 | 12 | 1.97 | d1+c | **显性迁移** |
| `false` | 49 | 14 | 1.80 | c | **显性迁移**（false friends） |
| `speaking` | 61 | 26 | 1.23 | c | 身份命名 |
| `friends` | 46 | 23 | 1.00 | c | **显性迁移**（false friends） |

组 7 比组 6 多出一项 `influenced`（"influenced by German"），因为参照侧从 Chinese 换成 Generic 后该词成为过量词。

**八项中有五项的 LR ≥ 1.8，且 `german`、`transfer`、`SPEAKER` 三项无需 concordance 即可高信度判定。** 这是全研究维度三证据最集中的一组。

### 3.1 `INFLUENCE` 与 `influenced` 的不一致

| 词形 | 组 | 维度三判定 | 索引依据 |
|---|---:|---|---|
| `INFLUENCE` | 6 | **NA** | 维度一=NA(100%)，维度三=NA(59%) |
| `influenced` | 7 | **C1** | 维度一=NA(100%)，维度三=C1(74%) |

同一词族在组 6 与组 7 得到相反判定，且两项都有索引依据（59% 与 74%）。这不是编码失误——两组的对照侧不同（Chinese vs Generic），过量的具体形态与语境也不同。但 59% 这个数字偏低，说明组 6 的 `INFLUENCE` 判定本身不稳健。

**建议在论文中把 `influenced` 计入 C1、把 `INFLUENCE` 标为边界案例并说明其 59% 的判定强度**，而不是简单地按词族统一处理。

---

## 四、维度二：两侧的分工

| | 组 7（German 侧） | 组 8（Generic 侧） |
|---|---|---|
| act 已定 | 8 | **19** |
| A3 | 3（`watch`、`check`、`pay`） | **12**（`EXPLAIN`、`revise`、`strengthen`、`restate`、`stronger`、`recommend`、`clarify`、`address`、`using`、`consider`、`fix`、`sure`） |
| A2 | 3（`unnatural`、`abstract`、`confusion`） | 4（`errors`、`lack`、`confusing`、`awkward`） |
| A1 | 2（`fine`、`understandable`） | 3（`good`、`powerful`、`meaningful`） |
| hedge 已定 | **6** | 1 |

组 7 的 act 层分母仅 8，不作数值解读。但**两项 A1 都值得单独记录**：

- `fine`（信度 L）：经 concordance 判定为 A1。"this is fine" 是一种低强度认可，与 `good`／`powerful` 的正向程度不在一个量级。
- `understandable`（信度 L）：同组 2 的争议项，"your English is understandable" 承认可理解性但把标准设在了可理解而非质量上。

**两个低信度 A1 同时出现在德语标记侧，且都属「低门槛褒扬」类型**，而 Generic 侧的三个 A1（`good`、`powerful`、`meaningful`）是常规正向评价。这个对照与本研究的理论关切直接相关，但**两侧 A1 的绝对数分别只有 2 和 3，不足以支撑结论**。若要坐实，须回到全文层面统计赞扬的强度分布，而非依赖关键词表。

### 4.1 hedge 层：6 : 1

组 7 六项（`often`、`likely`、`usually`、`generally`、`few`、`quite`）vs 组 8 一项（`briefly`）。其中 `few` 与 `only` 经 concordance 分别判为 M1 与 NA——前者是最小化降调（"a few errors"），后者是限定。

这个 6 : 1 的对照在词位数层面是清楚的，但 hedge 层只有 M1 一个非 NA 取值，**占比恒为 100%、不含信息**，只能以词位数与词次陈述。

---

## 五、concordance 消解带来的变化

| 指标 | 组 7 消解前 → 后 | 组 8 消解前 → 后 |
|---|---|---|
| 维度一 G2 占比 | 80.0%（28/35，另 1 未决）→ **80.6%**（29/36） | 18.2%（6/33，另 2 未决）→ **19.4%**（7/36） |
| act A3 占比 | 37.5% → 37.5% | 63.2% → 63.2% |
| M1 词位 | 5 → **6**（`few`） | 1 → 1 |
| C1 词位 | 8 → 8 | 0 → 0 |

组 7 定夺 33 词位／42 单元格，组 8 定夺 22 词位／25 单元格。**两组结论方向均未改变**，占比移动均在 1.5 pp 以内。

组 7 的 `MEAN` 是全研究唯一一个 concordance **未能给出主导判定**的词位——查证结果为 G2-Wording(50%) / NA(50%) 的完全并列。最终判为 G2/Wording，属编码者裁定而非索引裁定。**该项在附表中的 `src` 标为 d1，但其证据强度弱于其他定夺项，复核时应注意。**

几处推翻原判的记录：

| 组 | 词形 | 原判倾向 | 查证后 |
|---|---|---|---|
| 7 | `check` | 偏 G2/Mechanics（同组 2） | **G2/Wording** |
| 7 | `abstract` | 偏 G2（abstract language） | **G1/Development**（缺具体支撑） |
| 7 | `natural`、`vary`、`understandable`(d1) | 待定 | 全部 **NA** |
| 8 | `story` | NA | **G1/Development** |
| 8 | `using` | 待定 | **G1/Development + A3** |
| 8 | `specific` | 待定 | **G1/Development**（47%） |

`check` 在四个语料中得到三种不同的维度一判定（Generic→Mechanics、Chinese→Development、German→Wording、L1→Development），全部有索引依据。这是「同词形跨语料编码不同」现象中最典型的一例，详见 [`final_report.md`](final_report.md) 第 4 节。

---

## 六、遗留问题

1. **低信度项**：组 7 的 `fine`、`understandable`（均为 A1，见 4.1）。组 8 无低信度项。
2. **`MEAN` 的 50/50 并列**（见第五节）：唯一由编码者而非索引裁定的定夺项。
3. **`INFLUENCE`／`influenced` 的族内不一致**（见 3.1）：建议按边界案例处理并披露判定强度。
4. **组 7 act 层分母仅 8**：不应产出 act 层的数值结论。
5. **`german` 与 `SPEAKER` 的 C1 子类**未细分，与组 6 的遗留问题相同。

---

## 附表

完整编码表与分布统计见 [`group07_tables.md`](group07_tables.md)、[`group08_tables.md`](group08_tables.md)，
由 `scripts/analyze.py 7` 与 `scripts/analyze.py 8` 生成。
