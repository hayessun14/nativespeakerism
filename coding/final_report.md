# 最终编码统计报告

本报告由 `scripts/final_report.py` 从 `coding/all_codes.tsv` 生成，反映 concordance 全部消解后的口径。八份 `group*_coding.md` 是编码当时的过程记录（含彼时的未决理由），其中的占比数字早于本轮消解，以本报告为准。

## 0 数据总览

| 项目 | 值 |
|---|---:|
| 关键词位（12 份成对清单合计） | 891 |
| 唯一词形 | 491 |
| 跨组重复出现的词形 | 290 |
| 未决单元格 | 0 |
| 经 concordance 定夺的词位 | 306 |
| 经 concordance 定夺的单元格 | 351 |

定夺单元格按层分布：维度一 204、act 层 93、hedge 层 25、维度三 29。该出处逐层记录于总表 `src` 列，与编码者信度评级 `conf` 分列，互不覆盖。

## 1 维度一 Feedback Focus（Straub & Lunsford 1995）

G1 Global＝Ideas／Development／Global Structure；G2 Local＝Local Structure／Wording／Correctness（含 Grammar、Mechanics）。

| 组 | 对比方向 | target | G1 | G2 | 分母 | G2 占比 |
|---:|---|---|---:|---:|---:|---:|
| 1 | L1 vs Generic | L1 | 50 | 22 | 72 | 30.6% |
| 2 | Generic vs L1 | Generic | 25 | 29 | 54 | 53.7% |
| 3 | Chinese vs Generic | Chinese | 5 | 14 | 19 | 73.7% |
| 4 | Generic vs Chinese | Generic | 11 | 3 | 14 | 21.4% |
| 5 | Chinese vs German | Chinese | 16 | 9 | 25 | 36.0% |
| 6 | German vs Chinese | German | 8 | 18 | 26 | 69.2% |
| 7 | German vs Generic | German | 7 | 29 | 36 | 80.6% |
| 8 | Generic vs German | Generic | 29 | 7 | 36 | 19.4% |
| 9 | Baseline vs Generic | Baseline | 55 | 14 | 69 | 20.3% |
| 10 | Generic vs Baseline | Generic | 18 | 35 | 53 | 66.0% |
| 11 | Baseline vs L1 | Baseline | 10 | 1 | 11 | 9.1% |
| 12 | L1 vs Baseline | L1 | 7 | 7 | 14 | 50.0% |

### 1.1 六组成对方向

每对的两组互为反向，比较各自 target 的 G2 占比即得该对比中「谁的差异词更偏局部」。

| 对 | 组 | target | G2 占比 | 组 | target | G2 占比 | 更偏局部 | 差距 |
|---:|---:|---|---:|---:|---|---:|---|---:|
| 1/2 | 1 | L1 | 30.6% | 2 | Generic | 53.7% | **Generic** | 23.1 pp |
| 3/4 | 3 | Chinese | 73.7% | 4 | Generic | 21.4% | **Chinese** | 52.3 pp |
| 5/6 | 5 | Chinese | 36.0% | 6 | German | 69.2% | **German** | 33.2 pp |
| 7/8 | 7 | German | 80.6% | 8 | Generic | 19.4% | **German** | 61.1 pp |
| 9/10 | 9 | Baseline | 20.3% | 10 | Generic | 66.0% | **Generic** | 45.7 pp |
| 11/12 | 11 | Baseline | 9.1% | 12 | L1 | 50.0% | **L1** | 40.9 pp |

### 1.2 方向的复合

把六条方向按「更偏局部」串起来，检查是否存在互相矛盾的回路。

- Generic ＞ L1（相差 23.1 pp）
- Chinese ＞ Generic（相差 52.3 pp）
- German ＞ Chinese（相差 33.2 pp）
- German ＞ Generic（相差 61.1 pp）
- Generic ＞ Baseline（相差 45.7 pp）
- L1 ＞ Baseline（相差 40.9 pp）

六条方向可复合为一条全序，无回路：**German ＞ Chinese ＞ Generic ＞ L1 ＞ Baseline**。

传递性成立意味着这 5 个条件在「局部化倾向」上可以排成一列，而不是各对之间各说各话。需要强调的是，这条序来自六次两两对比的复合，不是把各条件的关键词表并成一张表算出来的——12 份清单各有自己的分母，跨清单求并集会改变分母的含义。

### 1.3 子类分布

| 组 | target | Ideas | Develop. | Global St. | Local St. | Wording | Correct. | Grammar | Mech. |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | L1 | 30 | 12 | 8 | 3 | 11 | 2 | 1 | 5 |
| 2 | Generic | 15 | 6 | 4 | 3 | 10 | 4 | 10 | 2 |
| 3 | Chinese | 1 | 3 | 1 | 4 | 4 | 0 | 5 | 1 |
| 4 | Generic | 8 | 1 | 2 | 0 | 1 | 1 | 0 | 1 |
| 5 | Chinese | 6 | 4 | 6 | 4 | 2 | 1 | 1 | 1 |
| 6 | German | 6 | 0 | 2 | 4 | 6 | 2 | 3 | 3 |
| 7 | German | 4 | 1 | 2 | 7 | 12 | 1 | 7 | 2 |
| 8 | Generic | 15 | 8 | 6 | 2 | 1 | 1 | 1 | 2 |
| 9 | Baseline | 38 | 11 | 6 | 3 | 3 | 2 | 0 | 6 |
| 10 | Generic | 11 | 5 | 2 | 4 | 11 | 5 | 11 | 4 |
| 11 | Baseline | 6 | 4 | 0 | 1 | 0 | 0 | 0 | 0 |
| 12 | L1 | 3 | 4 | 0 | 3 | 2 | 0 | 1 | 1 |

## 2 维度二 Feedback Acts（Hyland & Hyland 2001）

两层结构：act 层（A1 Praise／A2 Criticism／A3 Suggestion，至多一个）与 hedge 层（M1 Hedges，至多一个）并行判定、可共存。两层各自计算分母。

### 2.1 act 层

| 组 | target | A1 | A2 | A3 | 分母 | A1% | A2% | A3% |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | L1 | 8 | 13 | 24 | 45 | 17.8% | 28.9% | 53.3% |
| 2 | Generic | 10 | 4 | 15 | 29 | 34.5% | 13.8% | 51.7% |
| 3 | Chinese | 0 | 3 | 4 | 7 | 0.0% | 42.9% | 57.1% |
| 4 | Generic | 2 | 1 | 2 | 5 | 40.0% | 20.0% | 40.0% |
| 5 | Chinese | 2 | 5 | 7 | 14 | 14.3% | 35.7% | 50.0% |
| 6 | German | 0 | 1 | 3 | 4 | 0.0% | 25.0% | 75.0% |
| 7 | German | 2 | 3 | 3 | 8 | 25.0% | 37.5% | 37.5% |
| 8 | Generic | 3 | 4 | 12 | 19 | 15.8% | 21.1% | 63.2% |
| 9 | Baseline | 5 | 10 | 21 | 36 | 13.9% | 27.8% | 58.3% |
| 10 | Generic | 5 | 5 | 14 | 24 | 20.8% | 20.8% | 58.3% |
| 11 | Baseline | 5 | 1 | 2 | 8 | 62.5% | 12.5% | 25.0% |
| 12 | L1 | 1 | 2 | 4 | 7 | 14.3% | 28.6% | 57.1% |

各组 act 层分母普遍偏小（4–45），占比对单个词位的增减敏感，宜作趋势参考而非精确估计。

### 2.2 hedge 层

本层只有 M1 一个非 NA 取值，故「占已定标签」恒为 100%，该比例不含信息；有意义的是 M1 的**词位数**与**词次**。

| 组 | target | M1 词位 | M1 词次 | 词形 |
|---:|---|---:|---:|---|
| 1 | L1 | 3 | 909 | `would`、`risk`、`fairly` |
| 2 | Generic | 8 | 2418 | `some`、`may`、`briefly`、`slightly`、`possible`、`probably`、`sometimes`、`could` |
| 3 | Chinese | 1 | 115 | `usually` |
| 4 | Generic | 2 | 609 | `could`、`feels` |
| 5 | Chinese | 1 | 987 | `some` |
| 6 | German | 4 | 715 | `likely`、`often`、`few`、`quite` |
| 7 | German | 6 | 938 | `often`、`likely`、`usually`、`generally`、`few`、`quite` |
| 8 | Generic | 1 | 119 | `briefly` |
| 9 | Baseline | 5 | 568 | `fairly`、`might`、`risk`、`somewhat`、`likely` |
| 10 | Generic | 6 | 1456 | `slightly`、`some`、`probably`、`usually`、`possible`、`briefly` |
| 11 | Baseline | 2 | 445 | `may`、`fairly` |
| 12 | L1 | 0 | 0 | — |

### 2.3 两层共现

全表 act 与 hedge 双标签共现 **4** 个词位：

| 组 | target | Type | act | hedge |
|---:|---|---|---|---|
| 1 | L1 | `would` | A3 | M1 |
| 2 | Generic | `could` | A3 | M1 |
| 4 | Generic | `could` | A3 | M1 |
| 9 | Baseline | `might` | A3 | M1 |

## 3 维度三 Cross-Linguistic & Identity Framing（窄口径）

C1 涵盖 Transfer framing（把文本特征归因于母语迁移）与 Identity marking（点明写作者的语言身份）。依手册规则，C1 项在维度一、维度二一律归 NA，故 C1 不参与前两个维度的分母。

| target corpus | C1 词形数 | 词形 |
|---|---:|---|
| German | 8 | `english`、`false`、`friends`、`german`、`influenced`、`SPEAKER`、`speaking`、`transfer` |
| Chinese | 2 | `chinese`、`english` |
| Generic | 1 | `english` |
| L1 | 0 | （无） |
| Baseline | 0 | （无） |

| 组 | 对比方向 | target | C1 词位 | C1 词次 |
|---:|---|---|---:|---:|
| 1 | L1 vs Generic | L1 | 0 | 0 |
| 2 | Generic vs L1 | Generic | 1 | 74 |
| 3 | Chinese vs Generic | Chinese | 2 | 199 |
| 4 | Generic vs Chinese | Generic | 0 | 0 |
| 5 | Chinese vs German | Chinese | 1 | 61 |
| 6 | German vs Chinese | German | 7 | 1311 |
| 7 | German vs Generic | German | 8 | 1358 |
| 8 | Generic vs German | Generic | 0 | 0 |
| 9 | Baseline vs Generic | Baseline | 0 | 0 |
| 10 | Generic vs Baseline | Generic | 1 | 74 |
| 11 | Baseline vs L1 | Baseline | 0 | 0 |
| 12 | L1 vs Baseline | L1 | 0 | 0 |

## 4 同词形跨语料的编码差异

一致性要求施加在「词形 × target corpus」上而非仅「词形」上：concordance 是分语料抽取的，同一词形在不同语料中的主导用法本就可能不同，这种差异是观察结果，不是编码失误。以下先验证语料内一致，再列出跨语料的分歧。

「词形 × 语料」组合 705 个，其中跨组重复出现 174 个；**语料内编码不一致 0 处**。

跨语料编码不同的词形 **17** 个：

| 词形 | 语料 | 维度一 | act | hedge | 维度三 |
|---|---|---|---|---|---|
| `authority` | Baseline | G1/Ideas | NA | NA | NA |
|  | L1 | NA | NA | NA | NA |
| `check` | Chinese | G1/Development | A3 | NA | NA |
|  | Generic | G2/Mechanics | A3 | NA | NA |
|  | German | G2/Wording | A3 | NA | NA |
|  | L1 | G1/Development | A3 | NA | NA |
| `clarity` | Chinese | G2/Local Structure | NA | NA | NA |
|  | Generic | G1/Ideas | NA | NA | NA |
| `clearly` | Baseline | NA | NA | NA | NA |
|  | Generic | G1/Ideas | NA | NA | NA |
| `could` | Generic | NA | A3 | M1 | NA |
|  | German | NA | NA | NA | NA |
| `effort` | Chinese | NA | A1 | NA | NA |
|  | Generic | NA | NA | NA | NA |
| `explain` | Baseline | NA | NA | NA | NA |
|  | Chinese | NA | A3 | NA | NA |
| `might` | Baseline | NA | A3 | M1 | NA |
|  | L1 | NA | A3 | NA | NA |
| `move` | Baseline | NA | NA | NA | NA |
|  | L1 | G1/Global Structure | NA | NA | NA |
| `precision` | Baseline | G2/Wording | NA | NA | NA |
|  | German | NA | NA | NA | NA |
|  | L1 | NA | NA | NA | NA |
| `reads` | Baseline | G1/Ideas | NA | NA | NA |
|  | L1 | G1/Global Structure | NA | NA | NA |
| `replace` | Baseline | G1/Development | A3 | NA | NA |
|  | L1 | G2/Wording | A3 | NA | NA |
| `tackles` | Baseline | NA | NA | NA | NA |
|  | L1 | NA | A1 | NA | NA |
| `understandable` | Generic | G1/Ideas | A1 | NA | NA |
|  | German | NA | A1 | NA | NA |
| `using` | Chinese | NA | NA | NA | NA |
|  | Generic | G1/Development | A3 | NA | NA |
| `vague` | Baseline | G1/Ideas | A2 | NA | NA |
|  | L1 | G2/Wording | A2 | NA | NA |
| `would` | Baseline | NA | NA | NA | NA |
|  | German | NA | NA | NA | NA |
|  | L1 | NA | A3 | M1 | NA |

## 5 高效应量词位（LR ≥ 1.5）

| 组 | target | Type | LL | LR | 维度一 | act | hedge | 维度三 |
|---:|---|---|---:|---:|---|---|---|---|
| 6 | German | german | 668.504 | 9.902 | NA | NA | NA | C1 |
| 7 | German | german | 647.497 | 7.351 | NA | NA | NA | C1 |
| 5 | Chinese | chinese | 77.281 | 5.968 | NA | NA | NA | C1 |
| 3 | Chinese | chinese | 77.135 | 5.965 | NA | NA | NA | C1 |
| 10 | Generic | corrections | 89.818 | 3.934 | G2/Correctness | NA | NA | NA |
| 7 | German | transfer | 37.705 | 3.423 | NA | NA | NA | C1 |
| 1 | L1 | correctness | 49.868 | 3.284 | G2/Correctness | NA | NA | NA |
| 2 | Generic | corrections | 75.765 | 3.208 | G2/Correctness | NA | NA | NA |
| 9 | Baseline | correctness | 37.529 | 3.002 | G2/Correctness | NA | NA | NA |
| 2 | Generic | vocabulary | 31.338 | 2.846 | G2/Wording | NA | NA | NA |
| 6 | German | transfer | 30.549 | 2.804 | NA | NA | NA | C1 |
| 7 | German | english | 362.732 | 2.776 | NA | NA | NA | C1 |
| 7 | German | SPEAKER | 79.165 | 2.729 | NA | NA | NA | C1 |
| 10 | Generic | english | 48.406 | 2.536 | NA | NA | NA | C1 |
| 10 | Generic | slightly | 36.018 | 2.426 | NA | NA | M1 | NA |
| 6 | German | false | 29.321 | 2.407 | NA | NA | NA | C1 |
| 2 | Generic | thank | 30.185 | 2.360 | NA | NA | NA | NA |
| 1 | L1 | tighten | 24.264 | 2.251 | G1/Ideas | A3 | NA | NA |
| 2 | Generic | english | 42.086 | 2.248 | NA | NA | NA | C1 |
| 6 | German | SPEAKER | 58.482 | 2.139 | NA | NA | NA | C1 |
| 2 | Generic | sharing | 19.045 | 2.078 | NA | NA | NA | NA |
| 10 | Generic | expressions | 24.786 | 2.057 | G2/Wording | NA | NA | NA |
| 10 | Generic | patterns | 27.794 | 2.027 | G2/Grammar | NA | NA | NA |
| 9 | Baseline | prose | 24.323 | 1.973 | G2/Wording | NA | NA | NA |
| 7 | German | influenced | 22.112 | 1.966 | NA | NA | NA | C1 |
| 10 | Generic | vocabulary | 19.937 | 1.960 | G2/Wording | NA | NA | NA |
| 10 | Generic | comment | 26.932 | 1.953 | NA | NA | NA | NA |
| 10 | Generic | recurring | 35.100 | 1.902 | NA | NA | NA | NA |
| 1 | L1 | aim | 40.757 | 1.900 | G1/Ideas | A3 | NA | NA |
| 1 | L1 | defensible | 23.177 | 1.882 | G1/Ideas | A1 | NA | NA |
| 10 | Generic | luck | 16.100 | 1.875 | NA | NA | NA | NA |
| 2 | Generic | expressions | 21.536 | 1.846 | G2/Wording | NA | NA | NA |
| 6 | German | english | 216.155 | 1.843 | NA | NA | NA | C1 |
| 1 | L1 | mechanical | 32.556 | 1.836 | G2/Mechanics | NA | NA | NA |
| 7 | German | false | 20.512 | 1.804 | NA | NA | NA | C1 |
| 7 | German | writer | 26.524 | 1.771 | NA | NA | NA | NA |
| 10 | Generic | probably | 23.792 | 1.740 | NA | NA | M1 | NA |
| 6 | German | basis | 17.018 | 1.722 | G1/Ideas | NA | NA | NA |
| 9 | Baseline | distract | 25.073 | 1.695 | G2/Mechanics | A2 | NA | NA |
| 6 | German | order | 43.921 | 1.675 | G2/Local Structure | NA | NA | NA |
| 1 | L1 | prose | 15.334 | 1.654 | G2/Wording | NA | NA | NA |
| 10 | Generic | plural | 17.111 | 1.644 | G2/Grammar | NA | NA | NA |
| 7 | German | order | 42.865 | 1.631 | G2/Local Structure | NA | NA | NA |
| 2 | Generic | tense | 36.317 | 1.623 | G2/Grammar | NA | NA | NA |
| 2 | Generic | comment | 20.908 | 1.623 | NA | NA | NA | NA |
| 2 | Generic | understandable | 22.275 | 1.600 | G1/Ideas | A1 | NA | NA |
| 1 | L1 | sweeping | 19.484 | 1.599 | G1/Ideas | A2 | NA | NA |
| 3 | Chinese | happy | 15.857 | 1.557 | NA | NA | NA | NA |
| 7 | German | register | 24.443 | 1.542 | G2/Wording | NA | NA | NA |
| 10 | Generic | understandable | 20.614 | 1.522 | G1/Ideas | A1 | NA | NA |
| 7 | German | ARTICLE | 156.605 | 1.517 | G2/Grammar | NA | NA | NA |
| 6 | German | speaking | 19.353 | 1.501 | NA | NA | NA | C1 |
| 10 | Generic | thank | 16.288 | 1.501 | NA | NA | NA | NA |

## 6 信度与判定出处

`conf` 是编码者对该行标签的信度评级，`src` 记录该行哪些层由 concordance 查证定夺。两者独立：一个凭手册即可高信度判定的词位 `src` 为空，一个查过索引行的词位仍可能因语境驳杂而评为低信度。

| conf | 词位数 | 其中经 concordance 定夺 |
|---|---:|---:|
| H | 262 | 2 |
| M | 354 | 29 |
| L | 9 | 9 |
| （未评级） | 266 | 266 |

低信度（conf=L）词位 **9** 个，复核时应优先重看：

| 组 | target | Type | 维度一 | act | 索引定夺 |
|---:|---|---|---|---|---|
| 1 | L1 | `authority` | NA | NA | d1 |
| 1 | L1 | `measured` | G2/Wording | A1 | d1 |
| 2 | Generic | `understandable` | G1/Ideas | A1 | d1 |
| 2 | Generic | `effort` | NA | NA | act |
| 5 | Chinese | `effort` | NA | A1 | act |
| 7 | German | `fine` | NA | A1 | act |
| 7 | German | `understandable` | NA | A1 | d1 |
| 9 | Baseline | `authority` | G1/Ideas | NA | d1 |
| 10 | Generic | `understandable` | G1/Ideas | A1 | d1 |

## 7 研究限制与承重提示

本节汇总各组叙述报告（`group*_coding_resolved.md`）中的限定条件，使「本报告 ＋ `all_codes.tsv`」两个文件足以支撑后续分析。凡引用上文任何占比之前，请先核对本节。

### 7.1 各层分母：哪些占比可用于数值论证

判定口径：分母 ≥ 30 可用于数值论证；10–29 仅作方向提示，不得换算百分比作比较；< 10 不作解读。分母指该层已赋值标签数（NA 不计入）。

| 组 | target | 维度一 | act 层 | hedge 层 | 维度三 |
|---:|---|---|---|---|---|
| 1 | L1 | 72 ✓ | 45 ✓ | 3 ✗ | 0 ✗ |
| 2 | Generic | 54 ✓ | 29 △ | 8 ✗ | 1 ✗ |
| 3 | Chinese | 19 △ | 7 ✗ | 1 ✗ | 2 ✗ |
| 4 | Generic | 14 △ | 5 ✗ | 2 ✗ | 0 ✗ |
| 5 | Chinese | 25 △ | 14 △ | 1 ✗ | 1 ✗ |
| 6 | German | 26 △ | 4 ✗ | 4 ✗ | 7 ✗ |
| 7 | German | 36 ✓ | 8 ✗ | 6 ✗ | 8 ✗ |
| 8 | Generic | 36 ✓ | 19 △ | 1 ✗ | 0 ✗ |
| 9 | Baseline | 69 ✓ | 36 ✓ | 5 ✗ | 0 ✗ |
| 10 | Generic | 53 ✓ | 24 △ | 6 ✗ | 1 ✗ |
| 11 | Baseline | 11 △ | 8 ✗ | 2 ✗ | 0 ✗ |
| 12 | L1 | 14 △ | 7 ✗ | 0 ✗ | 0 ✗ |

✓ 可用于数值论证　△ 仅作方向提示　✗ 不作解读

**hedge 层与维度三另有一条独立限制**：两层各自只有一个非 NA 取值（M1 与 C1），故「占已定标签」恒为 100%，该比例不含任何信息。这两层只能以**词位数**与**词次**陈述，任何情况下都不得报告其百分比。

### 7.2 单个词位的权重

维度一占比对单个词位的敏感度随分母变化，跨组比较 pp 差值时必须同时看分母。

| 组 | target | 维度一分母 | 1 个词位 = |
|---:|---|---:|---:|
| 1 | L1 | 72 | 1.4 pp |
| 2 | Generic | 54 | 1.9 pp |
| 3 | Chinese | 19 | 5.3 pp |
| 4 | Generic | 14 | 7.1 pp |
| 5 | Chinese | 25 | 4.0 pp |
| 6 | German | 26 | 3.8 pp |
| 7 | German | 36 | 2.8 pp |
| 8 | Generic | 36 | 2.8 pp |
| 9 | Baseline | 69 | 1.4 pp |
| 10 | Generic | 53 | 1.9 pp |
| 11 | Baseline | 11 | 9.1 pp |
| 12 | L1 | 14 | 7.1 pp |

举例：组 3 一个词位值 5.3 pp，组 9 只值 1.4 pp。§1.1 中 11/12 对的 40.9 pp 建立在分母 11 与 14 之上，与 7/8 对的 61.1 pp（分母各 36）不可等量齐观。**呈现 §1.2 的全序时应标注各条边的分母。**

### 7.3 标签成立但证据强度不足的三处

以下三项的标签本身没有问题，但**若用来承载结论则超出其依据**，援引前须补查 concordance 或改以定性方式表述。

| 位置 | 情况 | 风险 |
|---|---|---|
| 组 1 `correctness`（LR 3.284，全组最高） | 编为 G2/Correctness，信度 H，但 `src` 为空——**零 concordance 支持**，是凭词形判定的 | 它是局部标签却出现在全局倾斜的一侧。「母语者标记下纠错被降格为次要关切」这一读法很自然，但当前无索引证据。组 9 的 `correctness`（LR 3.002）同理 |
| 组 11 的五个 A1（`accurate`、`effectively`、`engaging`、`promising`、`balanced`） | A1 占该组 act 层 62.5%（5/8），为全研究最高；**五项的 act 层全部未经查证** （`accurate` 只查证了维度一，act 层同样是词形判定） | 存在目标态框架风险（"make it more engaging" 是建议而非赞扬）。补查前不应援引「Baseline 条件下赞扬最多」 |
| 组 7 `MEAN` | concordance 结果为 G2-Wording(50%) / NA(50%) 完全并列，最终由**编码者裁定**而非索引裁定 | 全研究 351 个定夺单元格中唯一一个索引未能给出主导判定的。其 `src` 标为 d1，但证据强度弱于其余 350 个 |

此外，A1 层整体存在**目标态框架**的系统性风险：比较级与「使其更 X」结构可读作建议（A3）而非赞扬（A1）。经强制查询清单查证的仅 `strong` 词族、`GOOD`、`strongest`、`strength`、`strengths` 等数项，其余 A1 为词形判定。若 A1／A3 分界进入论证，应整族补查。

### 7.4 同词形跨语料编码不同

§4 列出的 17 个词形在不同语料中编码不同。这是观察结果而非编码失误（concordance 分语料抽取，同一词形的主导用法本就可能因语料而异），语料内一致性为 0 例外。但**统计时不可按词形合并**——`check` 在四个语料中有三种维度一判定，合并会抹掉这一结果本身。

其中一处需单独说明：`INFLUENCE`（组 6，维度三 NA，判定强度 59%）与 `influenced`（组 7，维度三 C1，判定强度 74%）同族异判。59% 偏低，建议把 `influenced` 计入 C1、把 `INFLUENCE` 标为边界案例并披露其判定强度，而非按词族统一处理。

### 7.5 尚未完成的工作

| 项目 | 状态 | 影响 |
|---|---|---|
| 维度三 C1 子类判定 | **未进行**。`c` 列只有 C1／NA，无子类字段；20 个 C1 词位只判到范畴层 | Identity marking（身份命名）与 Transfer framing（迁移归因）未区分。这是维度三的理论要害——「把你叫作中文母语者」与「说你的错误来自中文干扰」是两种不同的 native-speakerism 表现 |
| 组内信度检验（κ） | **未进行**。计划两周后重编 15%（约 134 词位） | 质性编码研究通常要求报告该值，缺失则编码部分方法上不完整 |
| 低信度词位复核 | 9 个 conf=L 项待复核（见 §6） | 其中 `understandable` 横跨组 2／7／10，「低门槛褒扬是否构成 praise」应统一裁定而非逐组处理 |
| 手册 v3 强制查询清单 | **从未完整获得**，仅用到已知条目（`address`、`strong` 词族等） | 若完整清单另有条目，需重扫 891 词位 |

---

**文件对应关系**：本报告与 `coding/all_codes.tsv` 构成完整的分析基础。各组的详细论证与逐词讨论见 `coding/group*_coding_resolved.md`（8 份）；各组完整编码表与 B1–B10 附表见 `coding/group*_tables.md`（12 份）；二者的全部内容均可由 `all_codes.tsv` 复现。不带 `_resolved` 的 `group*_coding.md` 是 concordance 消解前的过程存档，其占比数字已作废。

