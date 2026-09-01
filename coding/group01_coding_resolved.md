# 组 1 关键词质性分类编码报告（concordance 消解后）

> **状态：现行口径**
> 本文档基于 concordance 全部消解后的编码撰写，取代 [`group01_coding.md`](group01_coding.md)
> 中的一切占比数字。原文档保留为编码过程的审计轨迹，记录当时为何判未决，不再更新。
> 完整附表见 [`group01_tables.md`](group01_tables.md)，跨组统计见 [`final_report.md`](final_report.md)。

## L1 → Generic（目标语料 = L1 条件，参照语料 = Generic 条件）

> **编码方案**：手册 v3　**编码对象集**：本清单全部 128 词位　**占比分母**：各层已定标签数
> **服务的 RQ**：RQ1（母语者标记 vs 非母语者标记）
> **对比性质**：两侧作文文本相同，唯一差别是提示词把写作者标记为母语者还是未指明母语的非母语者。
> **未决项**：0（原 5 个 PENDING 单元格已由 concordance 消解）

---

## 一、结果摘要

| 层 | 已定标签 | 分布 | N/A |
|---|---:|---|---:|
| 维度一 Focus | 72 | **G1 50（69.4%）／ G2 22（30.6%）** | 56 |
| 维度二 act | 45 | A3 24（53.3%）／ A2 13（28.9%）／ A1 8（17.8%） | 83 |
| 维度二 hedge | 3 | M1 3（`would`、`risk`、`fairly`） | 125 |
| 维度三 | **0** | **无 C1** | 128 |

**一句话概括**：L1 条件相对 Generic 条件的过量词汇明显偏向全局层面（G1 69.4%），其中 Ideas 子类以 30 项独占 G1 的 50 项中的六成；维度三为**零**——当写作者被标记为母语者时，反馈中不出现任何跨语言或语言身份框架的词汇。

---

## 二、维度一：全局倾斜，且集中在论证内容

已定 72 项中 G1 占 50 项（69.4%）。子类分布：

| 主类 | 子类 | 词位数 | 代表词 |
|---|---|---:|---|
| G1 | Ideas | **30** | `CLAIM`、`reasoning`、`analysis`、`counterarguments`、`arguable`、`sweeping` |
| G1 | Development | 12 | `evidence`、`credible`、`anecdote`、`detail`、`integrate` |
| G1 | Global Structure | 8 | `reorganize`、`structural`、`opening`、`section`、`shifts`、`reads` |
| G2 | Wording | 11 | `phrasing`、`wording`、`prose`、`placeholder`、`imprecise` |
| G2 | Mechanics | 5 | `mechanical`、`typos`、`mechanics`、`distract`、`inconsistent` |
| G2 | Local Structure | 3 | `level`、`line`、`cut` |
| G2 | Correctness | 2 | `correctness`、`PROOFREAD` |
| G2 | Grammar | 1 | `edit` |

G1 内部的重心不在结构而在**内容**：Ideas 与 Development 合计 42 项，Global Structure 仅 8 项。也就是说，母语者标记下的反馈差异主要体现在「说了什么、有没有证据支撑」，而不是「篇章怎么组织」。

### 2.1 `correctness` 的方向需要留意

| 词形 | Freq_Tar (L1) | Freq_Ref (Generic) | LL | LR |
|---|---:|---:|---:|---:|
| `correctness` | 60 | 6 | 49.868 | **3.284** |
| `mechanical` | 77 | 21 | 32.556 | 1.836 |

`correctness` 是本组 LR 最高的词位，而它被编为 **G2/Correctness**——一个局部标签，却在**全局倾斜的一侧**过量出现。这不构成矛盾：该词是命名焦点范畴的元话语标签，不是实施纠错。反馈说「correctness」时，很可能正是在把它与别的东西对举（"beyond correctness"、"not just correctness"）。

但这一读法目前**没有 concordance 支持**——该词位信度为 H、`src` 为空，是凭手册直接判定的。若要在论文中援引「母语者标记下反馈把纠错降格为次要关切」这类说法，需要补查 `correctness` 与 `mechanical` 的索引行；仅凭词频方向不足以支撑。这是本组唯一一处「已定标签但结论承重超出其依据」的地方。

---

## 三、维度二 act 层：建议为主，赞扬最少

已定 45 项：A3 24（53.3%）、A2 13（28.9%）、A1 8（17.8%）。

| 标签 | 词位 |
|---|---|
| A3 Suggestion | `aim`、`SHARPEN`、`edit`、`would`、`tighten`、`NEED`、`CLARIFY`、`cut`、`might`、`PROOFREAD`、`address`、`reorganize`、`STRENGTHEN`、`should`、`engage`、`define`、`replace`、`acknowledge`、`distinguish`、`improving`、`sharper`、`integrate`、`want`、`develop` |
| A2 Criticism | `sweeping`、`vague`、`distract`、`imprecise`、`underdeveloped`、`concerns`、`placeholder`、`loosely`、`weaken`、`abstract`、`inconsistent`、`casual`、`overly` |
| A1 Praise | `defensible`、`credible`、`strongest`、`measured`、`arguable`、`tackles`、`genuine`、`polished` |

A1 的 8 项中有 5 项（`defensible`、`credible`、`arguable`、`genuine`、`strongest`）域固定于论断与证据——赞扬的对象也是全局内容，与维度一的倾斜一致。

需要标注一个方法风险：A1 词汇普遍存在**目标态框架**的竞争读法（"make it more defensible" 是建议而非赞扬）。其中 `strongest` 经 concordance 判定为 A1（属手册 v3 强制查询清单），`polished`、`measured` 的维度一经查证但 act 层未查。若后续需要精确的 A1/A3 分界，这几项应补查。

### 3.1 hedge 层：分母仅 3 项，不作解读

M1 三项：`would`（786 词次，与 A3 共现）、`risk`（64）、`fairly`（59）。其中 `would` 的两层均经 concordance 判定（act=A3 54%、hedge=M1 55%）——两个比例都逼近五五开，说明该词在本语料中确实兼具建议与缓和两种功能，不是判定不清。

`rather`（833 词次，LL 排第 2）与 `just`（263）经 concordance 判定 hedge=**NA**：前者主导用法是 "rather than" 的对比框架，后者是强化而非最小化降调。二者都曾被手册列为 hedge 候选，查证后排除——这是 concordance 消解**收紧**而非放宽标签的两个例子。

---

## 四、维度三：零 C1，且这个零是有信息的

本组 128 词位中维度三全部为 NA。唯一的候选 `cultural`（80 词次，LR 0.611）经 concordance 判定为 **NA(100%)**——全部是议题内容残留（LOCNESS 作文主题），不是把文本特征归因于文化背景。

这个零需要与其他组对读才有意义：

| target corpus | C1 词形数 |
|---|---:|
| German | 8 |
| Chinese | 2 |
| Generic | 1（`english`） |
| **L1** | **0** |
| Baseline | 0 |

L1 条件与 Baseline（无身份标记）同为零。**只要写作者未被标记为非母语者，语言身份框架就不出现**；一旦标记，就出现，且标记得越具体（指明母语）出现得越多。这条梯度是本研究维度三的核心结果，而组 1 提供的是它的下端锚点。

---

## 五、concordance 消解带来的变化

本组 **34 个词位、38 个单元格**经 concordance 查证定夺（维度一 28、act 6、hedge 3、维度三 1），出处逐条记录在总表 `src` 列与附表 A 的「索引定夺」列。

| 指标 | 消解前 | 消解后 | 变化 |
|---|---|---|---|
| 维度一 G2 占比 | 29.2%（21/72，另 1 项未决） | 30.6%（22/72） | +1.4 pp |
| act A3 占比 | 53.3% | 53.3% | 无 |
| M1 词位 | 3 | 3 | 无 |
| C1 词位 | 0 | 0 | 无 |

唯一的维度一未决项 `edit` 判为 **G2/Grammar**（表层编辑而非全局修改），G2 增 1 项。**本组所有结论的方向均未改变**，占比移动幅度在 1.5 pp 以内。

值得单独记录的是几处 concordance **推翻了原判**的地方：

| 词形 | 原判 | 查证后 | 说明 |
|---|---|---|---|
| `authority` | G1/Ideas | **NA** | 原按「论述权威」归 G1，实为议题内容残留 |
| `precision` | 未决 | **NA** | precision of language 与 of claims 两读法均未占主导 |
| `right` | 未决 | **NA** | 主导为 "right now" 等时间/话语用法，非 "the right word" |
| `power` | 未决 | **NA** | 议题内容残留（政治权力），非 "the power of your argument" |

四项全部落到 NA，即**从两个维度的分母中移出**。这类「查证后发现根本不属于反馈焦点」的结果，比填进某个具体标签更常见，也更容易在只看词形时被误编。

---

## 六、遗留问题

1. **低信度项 2 个**：`authority`（NA/NA，已查证为议题残留，信度评级可上调）、`measured`（G2/Wording，act=A1 未查证）。复核时优先。
2. **`correctness` 的承重问题**（见 2.1）：若论文要援引该词的方向性，须补查索引行。
3. **A1 的目标态框架风险**：8 个 A1 中仅 `strongest` 经查证，其余 7 项的 act 层为词形判定。若 A1/A3 分界进入论证，应整族补查。
4. **议题内容残留**：`public`、`policy`、`financial`、`cultural`、`power` 等，两个维度均为 NA，移除不改变任何已定标签占比，只影响清单总数（128 → 123）。

---

## 附表

完整编码表（附表 A，含每个词位的信度与索引定夺记录）与分布统计（B1–B10）见
[`group01_tables.md`](group01_tables.md)，由 `scripts/analyze.py 1` 生成。
