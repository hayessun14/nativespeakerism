# 组 7／组 8 关键词质性分类编码报告

> **状态：编码过程记录（concordance 消解前）**
> 本文档保留编码当时的判断与未决理由，作为审计轨迹，内容不随后续消解改写。
> 其中的占比数字计算于 PENDING 尚未消解之时，**已不是现行口径**；
> 最终统计以 [`final_report.md`](final_report.md) 及各组 `group*_tables.md` 为准。

## German ↔ Generic　（附：组 1–8 阶段性综合）

> **编码日期**：2026-08-27（第一轮编码）
> **编码方案**：手册 v3　**编码对象集**：组 7 全部 77 词位、组 8 全部 65 词位　**占比分母**：各层已定标签数
> **本对的作用**：补齐组 5／组 6 报告 §2 中唯一仍以主表原始频次代替编码结果的一段（German ↔ Generic），使 RQ1／RQ2 的八组闭合。
> **本轮新增校验**：`scripts/analyze.py` 增加取值合法性与主类／子类一致性断言。该校验发现并修正了组 7 的一处录入错误（`beginning` 的信度值误写入 act 列）与组 1 的一处字段规范问题（`move` 的子类字段应为 `-`）。**两处均不改变任何已发布的统计数字**，组 1 附表经 diff 确认仅该行显示变化。

---

## 一、结果摘要

| 层 | 组 7（German 侧过量） | 组 8（Generic 侧过量） |
|---|---|---|
| 维度一 | 已定 19：**G2 15（78.9%）**／ G1 4（21.1%） | 已定 24：**G1 21（87.5%）**／ G2 3（12.5%） |
| 维度二 act | 已定 8：A3 3／A1 2／A2 2 | 已定 14：A3 8／A2 4／A1 2 |
| 维度二 hedge | 已定 **5**：`often`、`likely`、`usually`、`generally`、`quite` | 已定 **0**（PENDING 1） |
| 维度三 | **C1 3**（`german`、`SPEAKER`、`transfer`），**PENDING 9** | **C1 0，PENDING 0** |
| N/A ／ PENDING（维度一） | 35 ／ 23 | 29 ／ 12 |

敏感性区间：组 7 的 G1 占比 [9.5%, 64.3%]，组 8 [58.3%, 91.7%]。重叠区仅 [58.3%, 64.3%]，是四对语料中重叠最窄的一对（组 3／组 4 完全不重叠，组 1／组 2 与组 5／组 6 重叠较宽）。

---

## 二、维度一：局部序列闭合

组 7 的 G2 子类构成是全研究最细的一份：Grammar 5（`NOUN`、`prepositions`、`singular`、`plural`、`forms`）、Local Structure 5（`clauses`、`splices`、`sentences`、`SHORT`、`independent`）、Wording 3、Mechanics 1（`COMMA`）、Correctness 1（`usage`）。加上维度一 PENDING 中的 `ARTICLE`、`order`、`PATTERN`，德语侧的局部清单是：**冠词、名词、介词、单复数、动词形式、从句、独立分句、逗号粘连、逗号、语序**。

组 8 的 G1 子类：Ideas 10（`ideas`、`point`、`argument`、`reasons`、`opposing`、`connection`、`comparison`、`impact`、`strengthen`、`readers`）、Global Structure 6、Development 5。G2 仅 3 项。

### 2.1 四对语料的方向一致（传递性检验）

至此四条腿全部由编码结果给出，不再依赖原始频次代替：

| 对比 | 更偏局部的一侧 | 依据 |
|---|---|---|
| L1 ↔ Generic | Generic | 组 1 G1 80.8%／组 2 G2 52.8% |
| Chinese ↔ Generic | Chinese | 组 3 G2 90.9%／组 4 G1 83.3% |
| German ↔ Generic | **German** | 组 7 G2 78.9%／组 8 G1 87.5% |
| Chinese ↔ German | German | 组 5 G1 72.2%／组 6 G2 71.4% |

四个成对判断可以合成为单一全序：**German > Chinese > Generic > L1**（局部倾向由高到低），且**四对之间没有任何一对与该全序矛盾**。

这一点值得强调：成对比较的方向一致性（传递性）不是设计所保证的——四个条件各自独立生成反馈，完全可能出现 A>B、B>C 而 C>A 的循环。没有出现循环，是对「存在一条单一潜在维度在驱动焦点分配」这一读法的独立支持。

需要说明的是：**该全序只由方向构成，不由百分比构成**。各对的占比分母不同（52、36、11、12、18、14、19、24），不可跨对相减；上表的百分比仅用于确认每一对内部的方向，不构成序列上的距离。

### 2.2 组 5／组 6 §2 的结论得到确认

组 5／组 6 报告曾以主表原始频次（`ARTICLE` 479 : 272 : 167 : 74）临时代替 German ↔ Generic 一段。本组编码结果与该临时依据方向一致，**该报告 §2 的推论无需修改**。

---

## 三、维度三：Generic 侧第三次归零，德语侧达到峰值

| 组 | 目标条件 | C1 已定 | 词次 | C1 待定 | 待定词次 |
|---:|---|---|---:|---:|---:|
| 1 | L1 | — | 0 | 1 | 80 |
| 2 | Generic（vs L1） | — | 0 | 4 | 870 |
| 3 | Chinese（vs Generic） | `chinese` | 61 | 2 | 850 |
| 4 | Generic（vs Chinese） | — | 0 | **0** | **0** |
| 5 | Chinese（vs German） | `chinese` | 61 | **0** | **0** |
| 6 | German（vs Chinese） | `german`、`SPEAKER`、`transfer` | 647 | 7 | 1044 |
| 7 | German（vs Generic） | `german`、`SPEAKER`、`transfer` | **647** | **9** | **1822** |
| 8 | Generic（vs German） | — | 0 | **0** | **0** |

三条可以直接陈述的事实：

1. **八组中，确定的 C1 只出现在两个条件**：Chinese（1 项）与 German（3 项）。L1 与 Generic 两个条件在任何方向上都没有产生确定的 C1。
2. **Generic 侧三次归零**：当参照系是 Chinese（组 4）或 German（组 8）时，Generic 侧连 C1 候选都没有；只有当参照系是 L1（组 2）时才出现 4 项候选。也就是说，Generic 条件的身份词汇只相对于「完全不被标记」而言存在。
3. **German 侧是峰值**：组 7 的 C1 候选材料合计 12 项 2469 词次，是组 3（Chinese vs Generic）的 3 项 911 词次的约 2.7 倍。

组 7 新增两个候选词族，值得单独记录：

- `influenced`（47 vs 12，LR 1.966）——与组 6 的 `INFLUENCE` 同族。若判为 C1，则 Transfer framing 在德语条件有 `transfer` 与 `influence` 两个独立词族。
- `unnatural`（39 vs 16，LR 1.282）——与 `natural` 构成正反对。二者同时落在德语侧，且 `sounds`（156 vs 122）与之共现，构成一个「听起来自然／不自然」的评判框架。**若该框架的隐含标准是母语者语感，则它属于 C1，且是本研究中唯一以「规范」而非「命名」形式出现的身份框架**——这一判定的理论分量高于其 LL 值所提示的分量，建议列入第一优先 concordance。

---

## 四、维度二：hedge 层的完整对照（含对前一份报告的更正）

### 4.1 更正

组 5／组 6 报告 §4.2 曾称「中文条件在它参与的两个对比中都是 hedge 更少的一侧」。**该陈述有误**：组 3（Chinese 侧）的 hedge 层有已定 M1 `usually`（115 词次），并非 0。原报告已就地更正并加注。

### 4.2 更正后的完整对照

| 组 | 条件 | M1 词位 | M1 词次 | 具体词 |
|---:|---|---:|---:|---|
| 1 | L1 | 2 | 123 | `risk`、`fairly` |
| 2 | Generic（vs L1） | 5 | 1608 | `some`、`may`、`slightly`、`probably`、`sometimes` |
| 3 | Chinese（vs Generic） | 1 | 115 | `usually` |
| 4 | Generic（vs Chinese） | 1 | 110 | `feels` |
| 5 | Chinese（vs German） | 1 | 987 | `some` |
| 6 | German（vs Chinese） | 3 | 542 | `likely`、`often`、`quite` |
| 7 | German（vs Generic） | **5** | 765 | `often`、`likely`、`usually`、`generally`、`quite` |
| 8 | Generic（vs German） | **0** | 0 | — |

可稳健成立的只有两条，两种口径一致：

- **Generic > L1**（5 项 1608 词次 vs 2 项 123 词次）
- **German > Generic**（5 项 765 词次 vs 0 项）

不可判定的一条：**Chinese ↔ German** 在两种口径下方向相反（词位 3 : 1 偏德语，词次 542 : 987 偏中文），差异由高频弱 hedge `some` 单独驱动。**Chinese ↔ Generic** 则基本持平（各 1 项，115 : 110）。

因此现阶段能说的是 German > Generic > L1，**Chinese 在 hedge 序列中的位置无法判定**——这与维度一的全序形成对照：焦点维度上四个条件可排成一线，缓和维度上不能。这个不对称本身是结果，不应被抹平。

### 4.3 act 层

组 8 已定 14 项（A3 8、A2 4、A1 2），是八组中 act 层已定标签最多的一组；组 7 已定 8 项。两组的 A1 仍然很少（各 2 项），且 act 层 PENDING 分别为 6 和 8 项，其中组 8 含 `good`、`stronger`、`address` 三个强制查询／高体量词。**act 层仍不作跨组解读。**

---

## 五、数据问题

### 5.1 议题内容残留

组 7：**无确认残留**——是八组中唯一如此的一组。唯一沾边的是 `friends`，但它的竞争读法之一正是 C1（false friends），与 §3 的判定绑定，不单列为残留。
组 8：确认 2 项（`policy`、`health`）；疑似 2 项（`effects`、`story`）；`data` 已编为 G1/Development 但需核实是否为议题词。

### 5.2 组 7 的 PENDING 比例为八组最高

维度一 PENDING 23/77 = 29.9%，维度三 PENDING 9/77 = 11.7%。原因与组 6 相同：德语侧清单集中了大量跨层歧义词（`order`、`style`、`register`、`precision`、`rhetorical`、`basis`、`academic`、`MEAN`、`number`、`appropriate`、`double`、`vary`）。组 7 的点估计 21.1% 因此是八组中可靠性最低的之一，敏感性下界 9.5%／上界 64.3% 的跨度也最大。

### 5.3 手册 v3 强制查询清单仍未获得

组 8 含清单已知条目 `address` 与 `stronger`（strong 系），均已转 PENDING。组 8 的 `strengthen` 按组 1 `STRENGTHEN` 的口径编为 G1/Ideas ＋ A3，但它同属 strong 词族——**若清单覆盖该词族的派生形式，组 1 与组 8 的两处 `strengthen` 须一并改判**。

累计待重扫词位：128 ＋ 131 ＋ 37 ＋ 30 ＋ 56 ＋ 59 ＋ 77 ＋ 65 = **583 个**。

---

## 六、组 1–8 阶段性综合（RQ1／RQ2）

八组覆盖 L1、Generic、Chinese、German 四个条件间的全部四对对比。RQ3 所需的 Baseline 四组（9–12）尚未编码。

**RQ1（L2 标记 vs L1 标记）**：反馈焦点从全局移向局部（组 1 G1 80.8% → 组 2 G2 52.8%），语法子类从 0 项增至 6 项，认识型 hedge 从 2 项 123 词次增至 5 项 1608 词次，语言身份候选材料从 1 项（且很可能是议题残留）增至 4 项 870 词次。四条线索方向一致。**唯一的稳健性缺口**是组 1／组 2 的敏感性区间存在重叠 [56.0, 68.9]，须以 concordance 重算值定稿。

**RQ2（L2 群体之间）**：差异是**语言特异**的，不是 L2 标记程度的函数。局部倾向的全序为 German > Chinese > Generic > L1，四对方向无矛盾。语言身份框架在德语条件达到峰值（3 项确定 ＋ 9 项候选，2469 词次），中文条件仅 1 项确定；**显性迁移框架（`transfer`、`influenced`）只出现在德语条件**。

一个必须在讨论中处理的张力（沿自组 5／组 6 报告 §3.3）：身份框架的**数量**在西方语言标记下更高，而 Holliday 的论点针对的是非西方背景者的**缺陷叙事强度**。二者不是同一个量。判定需要 concordance 层面的评价极性与语力分析，词位计数无法回答。本阶段不引入 Holliday。

---

## 七、下一步

1. **组 9–12（Baseline 四组）**：RQ3，判定无标记条件更接近哪一侧。
2. **concordance 第一优先三项**：`false` 右搭配（判定 false friends）；`natural`／`unnatural`／`sounds` 的隐含标准（判定唯一的「规范型」C1）；`chinese` 子类（判定中文条件是否含迁移归因）。
3. **确定内容动词统一判定规则**（组 5／组 6 报告 §5），写入手册 v4 后再启动逐词 concordance。
4. 补齐 v3 强制查询清单，重扫累计 583 个词位。
5. 十二组编码完成后执行跨组一致性检查（组 4 报告 §5）。

---

# 附表：组 7（German → Generic）

## 附表 A：组 7 完整编码表（77 词位，按 LL 降序）

| # | Type | Freq_Tar | LL | LR | 维度一 | 子类 | 维度二 act | 维度二 hedge | 维度三 | 信度 | 判定依据 |
|---:|---|---:|---:|---:|---|---|---|---|---|---|---|
| 1 | german | 491 | 647.497 | 7.351 | NA | — | NA | NA | C1 | H | Identity marking 明示；Range 279/348＝80.2% |
| 2 | english | 508 | 362.732 | 2.776 | NA | — | NA | NA | PENDING | — | 手册明列：指语言系统（correct English）→C1；作文体修饰→NA。本组 Range 255/348，C1 先验极高，仍依规则待查 |
| 3 | ARTICLE | 479 | 156.605 | 1.517 | PENDING | — | NA | NA | NA | — | 维度一待定：英语冠词(G2-Grammar)vs 引用的文章(G1-Development) |
| 4 | SPEAKER | 113 | 79.165 | 2.729 | NA | — | NA | NA | C1 | H | 手册 Identity marking 词族例明列 speaker |
| 5 | PATTERN | 241 | 54.634 | 1.195 | PENDING | — | NA | NA | NA | — | 维度一待定：error patterns(G2)vs sentence patterns(G2-Local)vs 论证模式(G1) |
| 6 | order | 118 | 42.865 | 1.631 | PENDING | — | NA | NA | NA | — | 维度一待定：word order（G2-Grammar，德语语序迁移典型项）vs "in order to"（NA） |
| 7 | common | 223 | 41.407 | 1.056 | NA | — | NA | NA | NA | M | 常见性标记（a common error）＝正常化框架；属手册排除的 paired acts 类 |
| 8 | transfer | 43 | 37.705 | 3.423 | NA | — | NA | NA | C1 | H | 手册 Transfer framing 词族例明列 transfer |
| 9 | NOUN | 107 | 32.774 | 1.453 | G2 | Grammar | NA | NA | NA | H | Correctness/Grammar 明示；德语名词首字母大写为典型迁移项 |
| 10 | watch | 252 | 32.205 | 0.845 | NA | — | A3 | NA | NA | M | watch for / watch out for＝注意指令 |
| 11 | usage | 122 | 32.022 | 1.313 | G2 | Correctness | NA | NA | NA | M | article usage / comma usage，语言使用规范层 |
| 12 | moment | 107 | 28.056 | 1.312 | NA | — | NA | NA | NA | M | 元话语现状框架（at the moment），与组 1 currently 同构 |
| 13 | writer | 65 | 26.524 | 1.771 | NA | — | NA | NA | NA | M | 第三人称指称写作者（the writer），与 your 的第二人称形成对照 |
| 14 | natural | 113 | 25.840 | 1.202 | PENDING | — | PENDING | NA | PENDING | — | 三层皆待定：sounds natural 是否以母语者语感为隐含标准（C1）；同组 2、组 6 口径 |
| 15 | check | 243 | 25.390 | 0.751 | PENDING | — | A3 | NA | NA | — | 维度一待定：check your spelling(G2)vs check your logic(G1) |
| 16 | style | 410 | 25.199 | 0.557 | PENDING | — | NA | NA | NA | — | 维度一待定（手册列 tone/register 为 PENDING） |
| 17 | REQUIRE | 109 | 25.193 | 1.210 | NA | — | PENDING | NA | NA | — | act 层待定：this requires a comma（A3）vs German requires…（描述，且可能属 C1 共现语境） |
| 18 | register | 73 | 24.443 | 1.542 | PENDING | — | NA | NA | NA | — | 维度一待定（手册列 register 为 PENDING）；元语言学术语 |
| 19 | influenced | 47 | 22.112 | 1.966 | PENDING | — | NA | NA | PENDING | — | 维度三待定：influenced by German（Transfer framing，C1）vs influence the reader（G1）；与组 6 INFLUENCE 同族 |
| 20 | argumentation | 112 | 20.566 | 1.049 | G1 | Ideas | NA | NA | NA | H | Ideas 明示 |
| 21 | false | 49 | 20.512 | 1.804 | NA | — | NA | NA | PENDING | — | 维度三待定：false friends（C1）vs false dichotomy（G1-Ideas）；与 friends 的 Freq/Range 近乎同步 |
| 22 | COMMA | 330 | 18.930 | 0.536 | G2 | Mechanics | NA | NA | NA | H | Mechanics 明示 |
| 23 | often | 320 | 18.815 | 0.544 | NA | — | NA | M1 | NA | H | 手册 v3 M1 明示 hedge |
| 24 | eg | 456 | 17.027 | 0.424 | NA | — | NA | NA | NA | M | 举例元话语（e.g.） |
| 25 | structure | 795 | 16.676 | 0.312 | G1 | Global Structure | NA | NA | NA | H | 手册边界规则明示：structure 主导义为篇章结构 |
| 26 | clauses | 73 | 16.348 | 1.186 | G2 | Local Structure | NA | NA | NA | H | 手册 Local Structure 词族例明列 clause |
| 27 | language | 795 | 15.998 | 0.305 | PENDING | — | NA | NA | PENDING | — | 维度三待定：your language background(C1)vs academic language(G2 Wording) |
| 28 | likely | 166 | 14.749 | 0.685 | NA | — | NA | M1 | NA | H | 认识型 hedge |
| 29 | speaking | 61 | 14.405 | 1.227 | NA | — | NA | NA | PENDING | — | 维度三待定：German-speaking / German speakers（C1）vs generally speaking（NA） |
| 30 | SHORT | 174 | 13.898 | 0.645 | G2 | Local Structure | NA | NA | NA | M | short/shorter sentences；比较级，评价由框架承担 |
| 31 | fine | 71 | 13.236 | 1.059 | NA | — | A1 | NA | NA | L | 低信度：this is fine 属低门槛褒扬，与 A1「归功于正面价值特征」的定义是否相符须查；同组 2 understandable |
| 32 | academic | 997 | 12.928 | 0.242 | PENDING | — | NA | NA | NA | — | 维度一待定（register） |
| 33 | prepositions | 40 | 11.733 | 1.412 | G2 | Grammar | NA | NA | NA | H | Correctness/Grammar 明示 |
| 34 | splices | 130 | 11.371 | 0.679 | G2 | Local Structure | NA | NA | NA | H | comma splice 与 run-on 同属句界错误，依手册 run-on 口径归 Local Structure |
| 35 | usually | 139 | 10.939 | 0.640 | NA | — | NA | M1 | NA | H | 手册 v3 M1 明示 hedge |
| 36 | forms | 86 | 10.837 | 0.838 | G2 | Grammar | NA | NA | NA | M | verb forms / plural forms |
| 37 | unnatural | 39 | 9.866 | 1.282 | PENDING | — | PENDING | NA | PENDING | — | 三层皆待定：与 natural 同族，是否以母语者语感为隐含标准（C1）；若非 C1 则 act 为 A2 |
| 38 | very | 236 | 9.599 | 0.445 | NA | — | NA | NA | NA | M | 强化词，非 hedge |
| 39 | MEAN | 206 | 9.061 | 0.464 | PENDING | — | NA | NA | NA | — | 维度一待定：what you mean（G1 表意清晰）vs by means of（NA） |
| 40 | phrasing | 188 | 8.614 | 0.474 | G2 | Wording | NA | NA | NA | H | Wording 明示 |
| 41 | second | 127 | 8.279 | 0.576 | NA | — | NA | NA | NA | M | 序数词，反馈条目枚举 |
| 42 | abstract | 52 | 7.990 | 0.942 | PENDING | — | A2 | NA | NA | — | 维度一待定：too abstract＝缺具体支撑(G1-Dev)vs abstract language(G2)；同组 1 口径 |
| 43 | friends | 46 | 7.761 | 0.997 | NA | — | NA | NA | PENDING | — | 维度三待定：false friends（C1）vs 议题内容残留；参照侧 Freq 23 提示存在非 C1 基线用法 |
| 44 | generally | 84 | 7.526 | 0.688 | NA | — | NA | M1 | NA | H | 手册 v3 M1 明示 hedge |
| 45 | precision | 85 | 7.413 | 0.678 | PENDING | — | NA | NA | NA | — | 维度一待定：precision of language(G2)vs of claims(G1)；同组 1 口径 |
| 46 | sentences | 694 | 7.236 | 0.216 | G2 | Local Structure | NA | NA | NA | H | Local Structure 明示 |
| 47 | word | 522 | 6.992 | 0.246 | G2 | Wording | NA | NA | NA | H | Wording 明示 |
| 48 | double | 73 | 6.642 | 0.695 | PENDING | — | PENDING | NA | NA | — | 维度一与 act 层皆待定：double-check（A3）vs double negative（G2-Grammar） |
| 49 | confusion | 53 | 6.403 | 0.818 | PENDING | — | A2 | NA | NA | — | 维度一待定（clear 系）；负向评价 |
| 50 | notes | 46 | 6.256 | 0.876 | NA | — | NA | NA | NA | M | 元话语（a few notes on…） |
| 51 | therefore | 63 | 6.194 | 0.726 | NA | — | NA | NA | NA | M | 连接副词；亦可能为被建议使用的衔接词，待核 |
| 52 | singular | 55 | 6.099 | 0.778 | G2 | Grammar | NA | NA | NA | H | 单复数，Correctness/Grammar 明示 |
| 53 | come | 74 | 6.012 | 0.651 | NA | — | NA | NA | NA | M | comes across / comes from |
| 54 | vary | 65 | 5.951 | 0.697 | PENDING | — | PENDING | NA | NA | — | 维度一与 act 层皆待定：vary your sentence length(G2＋A3)vs 描述；内容动词类 |
| 55 | independent | 44 | 5.923 | 0.871 | G2 | Local Structure | NA | NA | NA | M | independent clause，与 clauses 共现 |
| 56 | basis | 44 | 5.923 | 0.871 | PENDING | — | NA | NA | NA | — | 维度一待定：the basis of your claim(G1-Ideas)vs on a …basis（NA） |
| 57 | contains | 44 | 5.923 | 0.871 | NA | — | NA | NA | NA | H | 描述性动词 |
| 58 | once | 108 | 5.906 | 0.523 | NA | — | NA | NA | NA | M | 时间/条件连接词 |
| 59 | only | 398 | 5.640 | 0.254 | NA | — | NA | PENDING | NA | — | hedge 层待定：最小化降调（only a few errors）vs 限定；同组 2 |
| 60 | understandable | 91 | 5.462 | 0.550 | PENDING | — | A1 | NA | NA | L | 维度一待定（clear 系）；act 低信度：低门槛褒扬与 A1 定义是否相符须查；同组 2 |
| 61 | phrases | 289 | 5.451 | 0.295 | G2 | Wording | NA | NA | NA | H | Wording 明示 |
| 62 | pay | 125 | 5.295 | 0.455 | NA | — | A3 | NA | NA | M | pay attention to＝注意指令 |
| 63 | always | 117 | 5.016 | 0.458 | NA | — | NA | NA | NA | M | 最大化副词，非 hedge |
| 64 | few | 173 | 4.877 | 0.365 | NA | — | NA | PENDING | NA | — | hedge 层待定：a few errors 最小化降调 vs 单纯量词；同组 6 |
| 65 | rhetorical | 192 | 4.818 | 0.343 | PENDING | — | NA | NA | NA | — | 维度一待定：rhetorical question（局部修辞手段）vs rhetorical strategy（G1） |
| 66 | given | 43 | 4.779 | 0.779 | NA | — | NA | NA | NA | M | given that / given the topic |
| 67 | beginning | 73 | 4.696 | 0.572 | G1 | Global Structure | NA | NA | NA | M | the beginning of your essay，大单位位置 |
| 68 | number | 58 | 4.631 | 0.645 | PENDING | — | NA | NA | NA | — | 维度一待定：singular/plural number(G2-Grammar)vs a number of（NA） |
| 69 | similarly | 59 | 4.533 | 0.631 | NA | — | NA | NA | NA | H | 连接副词 |
| 70 | raise | 37 | 4.434 | 0.814 | G1 | Ideas | PENDING | NA | NA | — | act 层待定：raises an important question 属开场归功套语(A1)vs 描述(NA)；与组 1 tackles、组 4 raises 并案 |
| 71 | quite | 56 | 4.336 | 0.634 | NA | — | NA | M1 | NA | H | 手册 v3 M1 明示 hedge |
| 72 | appropriate | 52 | 4.238 | 0.653 | PENDING | — | NA | NA | NA | — | 维度一待定：appropriate tone(register)vs appropriate word choice(G2)；规范性框架词 |
| 73 | plural | 68 | 4.221 | 0.560 | G2 | Grammar | NA | NA | NA | H | 单复数，Correctness/Grammar 明示 |
| 74 | argumentative | 673 | 4.141 | 0.165 | NA | — | NA | NA | NA | M | 文体标签（argumentative essay），不指示层级 |
| 75 | direct | 164 | 4.109 | 0.343 | PENDING | — | NA | NA | PENDING | — | 维度三待定（先验较低）：German writing is direct（文化—语用框架）vs be more direct(G2) |
| 76 | sounds | 156 | 4.089 | 0.351 | NA | — | NA | NA | NA | M | 听感评价框架动词（sounds awkward/natural）；与 natural/unnatural 共现，其 C1 权重由后者承担 |
| 77 | introduces | 72 | 3.937 | 0.523 | NA | — | NA | NA | NA | M | 描述性动词（your introduction introduces…） |

### B1 维度一 Feedback Focus

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| G2 | 15 | 78.9% | 2922 | 74.2% | 0.767 |
| G1 | 4 | 21.1% | 1017 | 25.8% | 0.687 |
| **已定标签合计** | **19** | **100.0%** | **3939** | **100.0%** | — |
| N/A（不计入分母） | 35 | — | — | — | — |
| PENDING（不计入分母） | 23 | — | — | — | — |
| 清单总数 | 77 | — | — | — | — |

**子类分布（分母同为已定标签 19）**

| 主类 | 子类 | 词位数 | 占比 |
|---|---|---:|---:|
| G1 | Global Structure | 2 | 10.5% |
| G1 | Ideas | 2 | 10.5% |
| G2 | Correctness | 1 | 5.3% |
| G2 | Grammar | 5 | 26.3% |
| G2 | Local Structure | 5 | 26.3% |
| G2 | Mechanics | 1 | 5.3% |
| G2 | Wording | 3 | 15.8% |

### B2 维度二 · act 层（A1 Praise / A2 Criticism / A3 Suggestion）

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| A3 | 3 | 42.9% | 620 | 69.9% | 0.684 |
| A1 | 2 | 28.6% | 162 | 18.3% | 0.804 |
| A2 | 2 | 28.6% | 105 | 11.8% | 0.880 |
| **已定标签合计** | **7** | **100.0%** | **887** | **100.0%** | — |
| N/A（不计入分母） | 64 | — | — | — | — |
| PENDING（不计入分母） | 6 | — | — | — | — |
| 清单总数 | 77 | — | — | — | — |

### B3 维度二 · hedge 层（M1 Hedges）

hedge 层与 act 层并行判定、可共存（Hyland & Hyland：hedge 施加于 act 之上）。分母为本层已定标签数。

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| M1 | 5 | 100.0% | 765 | 100.0% | 0.638 |
| **已定标签合计** | **5** | **100.0%** | **765** | **100.0%** | — |
| N/A（不计入分母） | 70 | — | — | — | — |
| PENDING（不计入分母） | 2 | — | — | — | — |
| 清单总数 | 77 | — | — | — | — |

### B4 维度三 Larger Contexts of Writing

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| C1 | 3 | 100.0% | 647 | 100.0% | 4.501 |
| **已定标签合计** | **3** | **100.0%** | **647** | **100.0%** | — |
| N/A（不计入分母） | 65 | — | — | — | — |
| PENDING（不计入分母） | 9 | — | — | — | — |
| 清单总数 | 77 | — | — | — | — |

### B5 维度二两层共现（词位数）

| act ＼ hedge | M1 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|
| **A1** | 0 | 2 | 0 | **2** |
| **A2** | 0 | 2 | 0 | **2** |
| **A3** | 0 | 3 | 0 | **3** |
| **NA** | 5 | 57 | 2 | **64** |
| **PENDING** | 0 | 6 | 0 | **6** |
| **合计** | 5 | 70 | 2 | **77** |

act ＋ hedge 双标签共现：**0** 项

### B6 维度一 × 维度二 act 层 交叉表（词位数）

| 维度一＼act | A1 | A2 | A3 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|---:|---:|
| **G1** | 0 | 0 | 0 | 3 | 1 | **4** |
| **G2** | 0 | 0 | 0 | 15 | 0 | **15** |
| **NA** | 1 | 0 | 2 | 31 | 1 | **35** |
| **PENDING** | 1 | 2 | 1 | 15 | 4 | **23** |
| **合计** | 2 | 2 | 3 | 64 | 6 | **77** |

### B7 LL 前 20 词位的维度一构成

| | G1 | G2 | N/A | PENDING |
|---|---:|---:|---:|---:|
| 词位数 | 1 | 2 | 9 | 8 |

### B8 敏感性分析：维度一 PENDING 的极端归属

| 情形 | G1 词位 | G2 词位 | G1 占比 |
|---|---:|---:|---:|
| 现状（PENDING 不计入） | 4 | 15 | 21.1% |
| 23 个 PENDING 全归 G1（上界） | 27 | 15 | 64.3% |
| 23 个 PENDING 全归 G2（下界） | 4 | 38 | 9.5% |

### B9 concordance 待办清单

共 **32** 个词族需 concordance 判定（含 2 个低信度已定项）。

| Type | Freq_Tar | 待定层 | 竞争读法 |
|---|---:|---|---|
| `english` | 508 | 维度三 | 手册明列：指语言系统（correct English）→C1；作文体修饰→NA。本组 Range 255/348，C1 先验极高，仍依规则待查 |
| `ARTICLE` | 479 | 维度一 | 维度一待定：英语冠词(G2-Grammar)vs 引用的文章(G1-Development) |
| `PATTERN` | 241 | 维度一 | 维度一待定：error patterns(G2)vs sentence patterns(G2-Local)vs 论证模式(G1) |
| `order` | 118 | 维度一 | 维度一待定：word order（G2-Grammar，德语语序迁移典型项）vs "in order to"（NA） |
| `natural` | 113 | 维度一、act、维度三 | 三层皆待定：sounds natural 是否以母语者语感为隐含标准（C1）；同组 2、组 6 口径 |
| `check` | 243 | 维度一 | 维度一待定：check your spelling(G2)vs check your logic(G1) |
| `style` | 410 | 维度一 | 维度一待定（手册列 tone/register 为 PENDING） |
| `REQUIRE` | 109 | act | act 层待定：this requires a comma（A3）vs German requires…（描述，且可能属 C1 共现语境） |
| `register` | 73 | 维度一 | 维度一待定（手册列 register 为 PENDING）；元语言学术语 |
| `influenced` | 47 | 维度一、维度三 | 维度三待定：influenced by German（Transfer framing，C1）vs influence the reader（G1）；与组 6 INFLUENCE 同族 |
| `false` | 49 | 维度三 | 维度三待定：false friends（C1）vs false dichotomy（G1-Ideas）；与 friends 的 Freq/Range 近乎同步 |
| `language` | 795 | 维度一、维度三 | 维度三待定：your language background(C1)vs academic language(G2 Wording) |
| `speaking` | 61 | 维度三 | 维度三待定：German-speaking / German speakers（C1）vs generally speaking（NA） |
| `fine` | 71 | 低信度复核 | 低信度：this is fine 属低门槛褒扬，与 A1「归功于正面价值特征」的定义是否相符须查；同组 2 understandable |
| `academic` | 997 | 维度一 | 维度一待定（register） |
| `unnatural` | 39 | 维度一、act、维度三 | 三层皆待定：与 natural 同族，是否以母语者语感为隐含标准（C1）；若非 C1 则 act 为 A2 |
| `MEAN` | 206 | 维度一 | 维度一待定：what you mean（G1 表意清晰）vs by means of（NA） |
| `abstract` | 52 | 维度一 | 维度一待定：too abstract＝缺具体支撑(G1-Dev)vs abstract language(G2)；同组 1 口径 |
| `friends` | 46 | 维度三 | 维度三待定：false friends（C1）vs 议题内容残留；参照侧 Freq 23 提示存在非 C1 基线用法 |
| `precision` | 85 | 维度一 | 维度一待定：precision of language(G2)vs of claims(G1)；同组 1 口径 |
| `double` | 73 | 维度一、act | 维度一与 act 层皆待定：double-check（A3）vs double negative（G2-Grammar） |
| `confusion` | 53 | 维度一 | 维度一待定（clear 系）；负向评价 |
| `vary` | 65 | 维度一、act | 维度一与 act 层皆待定：vary your sentence length(G2＋A3)vs 描述；内容动词类 |
| `basis` | 44 | 维度一 | 维度一待定：the basis of your claim(G1-Ideas)vs on a …basis（NA） |
| `only` | 398 | hedge | hedge 层待定：最小化降调（only a few errors）vs 限定；同组 2 |
| `understandable` | 91 | 维度一、低信度复核 | 维度一待定（clear 系）；act 低信度：低门槛褒扬与 A1 定义是否相符须查；同组 2 |
| `few` | 173 | hedge | hedge 层待定：a few errors 最小化降调 vs 单纯量词；同组 6 |
| `rhetorical` | 192 | 维度一 | 维度一待定：rhetorical question（局部修辞手段）vs rhetorical strategy（G1） |
| `number` | 58 | 维度一 | 维度一待定：singular/plural number(G2-Grammar)vs a number of（NA） |
| `raise` | 37 | act | act 层待定：raises an important question 属开场归功套语(A1)vs 描述(NA)；与组 1 tackles、组 4 raises 并案 |
| `appropriate` | 52 | 维度一 | 维度一待定：appropriate tone(register)vs appropriate word choice(G2)；规范性框架词 |
| `direct` | 164 | 维度一、维度三 | 维度三待定（先验较低）：German writing is direct（文化—语用框架）vs be more direct(G2) |

### B10 高效应量词位（LR ≥ 1.5）

| Type | LL | LR | 维度一 | act | hedge |
|---|---:|---:|---|---|---|
| german | 647.497 | 7.351 | NA | NA | NA |
| transfer | 37.705 | 3.423 | NA | NA | NA |
| english | 362.732 | 2.776 | NA | NA | NA |
| SPEAKER | 79.165 | 2.729 | NA | NA | NA |
| influenced | 22.112 | 1.966 | PENDING | NA | NA |
| false | 20.512 | 1.804 | NA | NA | NA |
| writer | 26.524 | 1.771 | NA | NA | NA |
| order | 42.865 | 1.631 | PENDING | NA | NA |
| register | 24.443 | 1.542 | PENDING | NA | NA |
| ARTICLE | 156.605 | 1.517 | PENDING | NA | NA |

# 附表：组 8（Generic → German）

## 附表 A：组 8 完整编码表（65 词位，按 LL 降序）

| # | Type | Freq_Tar | LL | LR | 维度一 | 子类 | 维度二 act | 维度二 hedge | 维度三 | 信度 | 判定依据 |
|---:|---|---:|---:|---:|---|---|---|---|---|---|---|
| 1 | your | 5416 | 30.919 | 0.157 | NA | — | NA | NA | NA | M | 人称代词 |
| 2 | mechanics | 131 | 29.128 | 1.179 | G2 | Mechanics | NA | NA | NA | H | Mechanics 明示 |
| 3 | errors | 317 | 25.001 | 0.639 | G2 | Correctness | A2 | NA | NA | H | 手册边界规则明示：error/mistake 归 G2-Correctness 且同时得批评标签 |
| 4 | clarity | 271 | 17.830 | 0.578 | PENDING | — | NA | NA | NA | — | 维度一待定（手册 clear 系） |
| 5 | organization | 396 | 17.756 | 0.468 | G1 | Global Structure | NA | NA | NA | H | Global Structure 明示 |
| 6 | specific | 546 | 16.535 | 0.379 | PENDING | — | NA | NA | NA | — | 手册明列 specific 为 PENDING：细节不足(G1-Dev)vs 用词不准(G2) |
| 7 | EXPLAIN | 603 | 16.353 | 0.357 | NA | — | PENDING | NA | NA | — | act 层待定：you explain X well（描述）vs explain this further（A3）；内容动词类 |
| 8 | SECTION | 177 | 15.956 | 0.690 | G1 | Global Structure | NA | NA | NA | M | 大于段落的单位 |
| 9 | readers | 263 | 15.034 | 0.535 | G1 | Ideas | NA | NA | NA | M | 受众；依窄口径 C1 规定归 G1 |
| 10 | say | 171 | 11.177 | 0.576 | NA | — | PENDING | NA | NA | — | act 层待定：you say X（描述）vs say more about（A3）；内容动词类 |
| 11 | level | 179 | 11.003 | 0.557 | PENDING | — | NA | NA | NA | — | 维度一待定：sentence-level(G2)/paragraph-level(G1)/level of detail(G1) |
| 12 | body | 588 | 10.796 | 0.290 | G1 | Global Structure | NA | NA | NA | H | body paragraphs，大单位 |
| 13 | revise | 378 | 10.212 | 0.356 | NA | — | A3 | NA | NA | H | 手册 A3 明示 |
| 14 | data | 85 | 9.881 | 0.798 | G1 | Development | NA | NA | NA | M | 证据类型；疑似议题内容残留，待核 |
| 15 | strengthen | 346 | 9.071 | 0.351 | G1 | Ideas | A3 | NA | NA | M | strengthen your argument/thesis；同组 1 STRENGTHEN 口径。注：属 strong 词族，若 v3 强制查询清单覆盖则须改判 PENDING |
| 16 | impact | 102 | 8.871 | 0.676 | G1 | Ideas | NA | NA | NA | M | the impact of your argument on the reader；同组 4 口径 |
| 17 | HELP | 302 | 8.823 | 0.372 | NA | — | NA | NA | NA | M | 描述性动词（this helps the reader） |
| 18 | FOCUS | 579 | 8.749 | 0.262 | PENDING | — | PENDING | NA | NA | — | 维度一待定：your focus(G1)vs focus on this sentence(G2)；act 层待定，内容动词类 |
| 19 | policy | 99 | 8.671 | 0.679 | NA | — | NA | NA | NA | H | 议题内容残留 |
| 20 | SUPPORT | 626 | 8.232 | 0.244 | G1 | Development | NA | NA | NA | H | 手册边界规则明示：support 归 G1 Development |
| 21 | significant | 109 | 8.177 | 0.622 | NA | — | NA | NA | NA | M | 程度形容词，极性依宾语 |
| 22 | organizing | 56 | 8.049 | 0.904 | G1 | Global Structure | NA | NA | NA | H | Global Structure 明示 |
| 23 | grammar | 658 | 7.980 | 0.234 | G2 | Grammar | NA | NA | NA | H | Correctness/Grammar 明示 |
| 24 | restate | 134 | 7.956 | 0.546 | G1 | Global Structure | A3 | NA | NA | M | restate your thesis in the conclusion，大单位安排 |
| 25 | luck | 36 | 7.943 | 1.173 | NA | — | NA | NA | NA | M | 人际礼貌（good luck）；属手册排除的 paired acts 类 |
| 26 | stronger | 477 | 7.934 | 0.276 | NA | — | PENDING | NA | NA | — | 手册 v3 强制查询清单（strong 系 A1/A3 争议），不得凭词形归类 |
| 27 | recommend | 59 | 7.513 | 0.842 | NA | — | A3 | NA | NA | H | 手册 A3 明示 |
| 28 | reasons | 149 | 7.393 | 0.495 | G1 | Ideas | NA | NA | NA | H | 手册 Ideas 词族例明列 reason |
| 29 | briefly | 119 | 7.358 | 0.558 | NA | — | NA | PENDING | NA | — | hedge 层待定：briefly explain 削减要求强度（M1）vs 单纯方式副词（NA）；同组 2 |
| 30 | details | 49 | 7.225 | 0.918 | G1 | Development | NA | NA | NA | H | Development 明示 |
| 31 | lack | 85 | 7.049 | 0.658 | NA | — | A2 | NA | NA | H | 手册 A2 词族例明列 lack |
| 32 | confusing | 56 | 6.688 | 0.811 | PENDING | — | A2 | NA | NA | — | 维度一待定（clear 系）；手册 A2 词族例明列 confusing |
| 33 | good | 509 | 6.680 | 0.243 | NA | — | PENDING | NA | NA | — | act 层待定：评价（A1）vs 目标态框架；同组 2 GOOD 口径 |
| 34 | now | 484 | 6.678 | 0.250 | NA | — | NA | NA | NA | M | 时间/话语副词 |
| 35 | clarify | 153 | 6.471 | 0.454 | PENDING | — | A3 | NA | NA | — | 维度一待定（手册 clear 系）；建议动词 |
| 36 | paper | 100 | 6.212 | 0.560 | NA | — | NA | NA | NA | H | 文本指称语，不指示层级 |
| 37 | address | 190 | 6.176 | 0.393 | PENDING | — | PENDING | NA | NA | — | 手册 v3 强制查询清单（G1/A3 争议），不得凭词形归类 |
| 38 | ideas | 450 | 6.090 | 0.247 | G1 | Ideas | NA | NA | NA | H | Ideas 明示 |
| 39 | areas | 267 | 5.985 | 0.323 | NA | — | NA | NA | NA | M | 元话语（areas for improvement，反馈小标题） |
| 40 | using | 171 | 5.704 | 0.399 | PENDING | — | PENDING | NA | NA | — | 维度一与 act 层皆待定；内容动词类 |
| 41 | conclusion | 734 | 5.448 | 0.181 | G1 | Global Structure | NA | NA | NA | H | 大单位，Global Structure 明示 |
| 42 | awkward | 142 | 5.334 | 0.425 | PENDING | — | A2 | NA | NA | — | 维度一待定：awkward phrasing(G2)vs awkward transition(G1)；手册 A2 词族例明列 awkward |
| 43 | effects | 143 | 5.291 | 0.422 | NA | — | NA | NA | NA | M | 疑似议题内容残留（effects of X）vs 对读者的效果，待核 |
| 44 | point | 431 | 5.133 | 0.231 | G1 | Ideas | NA | NA | NA | H | 手册 Ideas 词族例明列 point |
| 45 | consider | 578 | 5.112 | 0.198 | NA | — | A3 | NA | NA | H | 手册 A3 明示 |
| 46 | fix | 82 | 4.992 | 0.554 | PENDING | — | A3 | NA | NA | — | 维度一待定：fix these errors(G2)vs fix the structure(G1)；建议动词 |
| 47 | powerful | 61 | 4.934 | 0.649 | NA | — | A1 | NA | NA | M | 手册 A1 明示；目标态框架风险 |
| 48 | shows | 255 | 4.897 | 0.297 | NA | — | NA | NA | NA | M | 描述性框架动词 |
| 49 | clearly | 502 | 4.669 | 0.204 | PENDING | — | NA | NA | NA | — | 维度一待定（clear 系）；方式副词，act 层不赋值 |
| 50 | meaningful | 41 | 4.540 | 0.776 | NA | — | A1 | NA | NA | M | 正向评价；目标态框架风险 |
| 51 | right | 442 | 4.525 | 0.214 | PENDING | — | NA | NA | NA | — | 维度一待定：the right word(G2)vs right now(NA)；同组 1 口径 |
| 52 | all | 375 | 4.496 | 0.232 | NA | — | NA | NA | NA | M | 量词 |
| 53 | original | 135 | 4.395 | 0.394 | NA | — | NA | NA | NA | M | 与 revised 配对的"原句/改后句"对照格式，元话语；同组 2 |
| 54 | sure | 152 | 4.377 | 0.369 | NA | — | A3 | NA | NA | M | 主导用法为 make sure，手册 A3 明示 |
| 55 | story | 86 | 4.334 | 0.499 | NA | — | NA | NA | NA | M | 疑似议题内容残留，待核 |
| 56 | serious | 86 | 4.334 | 0.499 | NA | — | NA | NA | NA | M | 严重性强化词，极性依宾语（serious errors / no serious issues） |
| 57 | connection | 93 | 4.308 | 0.477 | G1 | Ideas | NA | NA | NA | M | the connection between your points，论点关联 |
| 58 | research | 155 | 4.283 | 0.361 | G1 | Development | NA | NA | NA | M | 来源使用，证据层 |
| 59 | comparison | 103 | 4.155 | 0.442 | G1 | Ideas | NA | NA | NA | M | 论证方式 |
| 60 | state | 279 | 4.065 | 0.257 | NA | — | PENDING | NA | NA | — | act 层待定：state your thesis clearly（A3）vs 描述；内容动词类 |
| 61 | evidence | 1223 | 4.005 | 0.119 | G1 | Development | NA | NA | NA | H | Development 核心 |
| 62 | health | 114 | 4.002 | 0.410 | NA | — | NA | NA | NA | H | 议题内容残留 |
| 63 | opposing | 130 | 3.998 | 0.382 | G1 | Ideas | NA | NA | NA | H | opposing views，反驳层 |
| 64 | argument | 1761 | 3.910 | 0.097 | G1 | Ideas | NA | NA | NA | H | Ideas 明示 |
| 65 | frequent | 37 | 3.892 | 0.753 | NA | — | NA | NA | NA | M | 频率标记（frequent errors）；与 recurring/common 同簇 |

### B1 维度一 Feedback Focus

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| G1 | 21 | 87.5% | 8051 | 87.9% | 0.450 |
| G2 | 3 | 12.5% | 1106 | 12.1% | 0.684 |
| **已定标签合计** | **24** | **100.0%** | **9157** | **100.0%** | — |
| N/A（不计入分母） | 29 | — | — | — | — |
| PENDING（不计入分母） | 12 | — | — | — | — |
| 清单总数 | 65 | — | — | — | — |

**子类分布（分母同为已定标签 24）**

| 主类 | 子类 | 词位数 | 占比 |
|---|---|---:|---:|
| G1 | Development | 5 | 20.8% |
| G1 | Global Structure | 6 | 25.0% |
| G1 | Ideas | 10 | 41.7% |
| G2 | Correctness | 1 | 4.2% |
| G2 | Grammar | 1 | 4.2% |
| G2 | Mechanics | 1 | 4.2% |

### B2 维度二 · act 层（A1 Praise / A2 Criticism / A3 Suggestion）

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| A3 | 8 | 57.1% | 1882 | 72.8% | 0.459 |
| A2 | 4 | 28.6% | 600 | 23.2% | 0.633 |
| A1 | 2 | 14.3% | 102 | 3.9% | 0.713 |
| **已定标签合计** | **14** | **100.0%** | **2584** | **100.0%** | — |
| N/A（不计入分母） | 43 | — | — | — | — |
| PENDING（不计入分母） | 8 | — | — | — | — |
| 清单总数 | 65 | — | — | — | — |

### B3 维度二 · hedge 层（M1 Hedges）

hedge 层与 act 层并行判定、可共存（Hyland & Hyland：hedge 施加于 act 之上）。分母为本层已定标签数。

**已定标签 0 项** —— 本层无任何词位获得标签，占比不适用（分母为 0）。

| 标签 | 词位数 | Freq_Tar 合计 |
|---|---:|---:|
| 已定标签合计 | 0 | 0 |
| N/A（不计入分母） | 64 | — |
| PENDING（不计入分母） | 1 | — |
| 清单总数 | 65 | — |

### B4 维度三 Larger Contexts of Writing

**已定标签 0 项** —— 本层无任何词位获得标签，占比不适用（分母为 0）。

| 标签 | 词位数 | Freq_Tar 合计 |
|---|---:|---:|
| 已定标签合计 | 0 | 0 |
| N/A（不计入分母） | 65 | — |
| PENDING（不计入分母） | 0 | — |
| 清单总数 | 65 | — |

### B5 维度二两层共现（词位数）

| act ＼ hedge | M1 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|
| **A1** | 0 | 2 | 0 | **2** |
| **A2** | 0 | 4 | 0 | **4** |
| **A3** | 0 | 8 | 0 | **8** |
| **NA** | 0 | 42 | 1 | **43** |
| **PENDING** | 0 | 8 | 0 | **8** |
| **合计** | 0 | 64 | 1 | **65** |

act ＋ hedge 双标签共现：**0** 项

### B6 维度一 × 维度二 act 层 交叉表（词位数）

| 维度一＼act | A1 | A2 | A3 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|---:|---:|
| **G1** | 0 | 0 | 2 | 19 | 0 | **21** |
| **G2** | 0 | 1 | 0 | 2 | 0 | **3** |
| **NA** | 2 | 1 | 4 | 17 | 5 | **29** |
| **PENDING** | 0 | 2 | 2 | 5 | 3 | **12** |
| **合计** | 2 | 4 | 8 | 43 | 8 | **65** |

### B7 LL 前 20 词位的维度一构成

| | G1 | G2 | N/A | PENDING |
|---|---:|---:|---:|---:|
| 词位数 | 8 | 2 | 6 | 4 |

### B8 敏感性分析：维度一 PENDING 的极端归属

| 情形 | G1 词位 | G2 词位 | G1 占比 |
|---|---:|---:|---:|
| 现状（PENDING 不计入） | 21 | 3 | 87.5% |
| 12 个 PENDING 全归 G1（上界） | 33 | 3 | 91.7% |
| 12 个 PENDING 全归 G2（下界） | 21 | 15 | 58.3% |

### B9 concordance 待办清单

共 **18** 个词族需 concordance 判定（含 2 个低信度已定项）。

| Type | Freq_Tar | 待定层 | 竞争读法 |
|---|---:|---|---|
| `clarity` | 271 | 维度一 | 维度一待定（手册 clear 系） |
| `specific` | 546 | 维度一 | 手册明列 specific 为 PENDING：细节不足(G1-Dev)vs 用词不准(G2) |
| `EXPLAIN` | 603 | act | act 层待定：you explain X well（描述）vs explain this further（A3）；内容动词类 |
| `say` | 171 | act | act 层待定：you say X（描述）vs say more about（A3）；内容动词类 |
| `level` | 179 | 维度一 | 维度一待定：sentence-level(G2)/paragraph-level(G1)/level of detail(G1) |
| `FOCUS` | 579 | 维度一、act | 维度一待定：your focus(G1)vs focus on this sentence(G2)；act 层待定，内容动词类 |
| `stronger` | 477 | act | 手册 v3 强制查询清单（strong 系 A1/A3 争议），不得凭词形归类 |
| `briefly` | 119 | hedge | hedge 层待定：briefly explain 削减要求强度（M1）vs 单纯方式副词（NA）；同组 2 |
| `confusing` | 56 | 维度一 | 维度一待定（clear 系）；手册 A2 词族例明列 confusing |
| `good` | 509 | act | act 层待定：评价（A1）vs 目标态框架；同组 2 GOOD 口径 |
| `clarify` | 153 | 维度一 | 维度一待定（手册 clear 系）；建议动词 |
| `address` | 190 | 维度一、act | 手册 v3 强制查询清单（G1/A3 争议），不得凭词形归类 |
| `using` | 171 | 维度一、act | 维度一与 act 层皆待定；内容动词类 |
| `awkward` | 142 | 维度一 | 维度一待定：awkward phrasing(G2)vs awkward transition(G1)；手册 A2 词族例明列 awkward |
| `fix` | 82 | 维度一 | 维度一待定：fix these errors(G2)vs fix the structure(G1)；建议动词 |
| `clearly` | 502 | 维度一 | 维度一待定（clear 系）；方式副词，act 层不赋值 |
| `right` | 442 | 维度一 | 维度一待定：the right word(G2)vs right now(NA)；同组 1 口径 |
| `state` | 279 | act | act 层待定：state your thesis clearly（A3）vs 描述；内容动词类 |

### B10 高效应量词位（LR ≥ 1.5）

| Type | LL | LR | 维度一 | act | hedge |
|---|---:|---:|---|---|---|
