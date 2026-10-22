# Concordance 提取日志

生成时间：2026-09-17 03:01:59

## 参数

| 项 | 值 |
|---|---|
| 组规格 | `data/groups_spec.tsv` |
| 归并映射 | `data/merged_map_groups.tsv` |
| KWIC 窗口 | 左右各 10 词 |
| 匹配方式 | 整词（whole-token），不区分大小写 |
| 语料来源 | `hayessun14/nativespeakerism` @ `claude/keen-brahmagupta-kkr013` |
| 输出目录 | `out/groups/` |

语料 tokenizer 为 `[\p{L}]+`（仅保留字母序列），连字符不进入 token。因此 `run-on` / `run-ons` 在语料中只能以 bigram `run on` / `run ons` 出现，脚本按 n-gram 检索，命中在 `match_form` 中标注 `(split)`。

## 各组汇总

| 组 | target corpus | 检索词数 | 总命中数 | 文件 |
|---|---|---:|---:|---|
| group01 | L1 | 8 | 2439 | `concordance_group01.tsv` |
| group02 | Generic | 9 | 2459 | `concordance_group02.tsv` |
| group03 | Chinese | 8 | 1868 | `concordance_group03.tsv` |
| group04 | Generic | 4 | 655 | `concordance_group04.tsv` |
| group05 | Chinese | 8 | 2325 | `concordance_group05.tsv` |
| group06 | German | 11 | 2200 | `concordance_group06.tsv` |
| group07 | German | 12 | 2398 | `concordance_group07.tsv` |
| group08 | Generic | 4 | 1639 | `concordance_group08.tsv` |
| group09 | Baseline | 11 | 4577 | `concordance_group09.tsv` |
| group10 | Generic | 8 | 2382 | `concordance_group10.tsv` |
| group11 | Baseline | 7 | 2040 | `concordance_group11.tsv` |
| group12 | L1 | 5 | 1369 | `concordance_group12.tsv` |
| **合计** | — | — | **26351** | — |

## 每个「词形 × 组」的命中数

### group01（target = L1，共 2439 行）

| 检索词 | 展开词形 | 命中数 | 各词形分项 |
|---|---|---:|---|
| CLAIM | claim + claims | 1663 | `claim` 994, `claims` 639, `Claims` 21, `Claim` 9 |
| defensible | — | 53 | `defensible` 53 |
| sweeping | — | 56 | `sweeping` 56 |
| reasoning | — | 281 | `reasoning` 275, `Reasoning` 6 |
| tighten | — | 44 | `tighten` 26, `Tighten` 18 |
| aim | — | 92 | `Aim` 59, `aim` 33 |
| RELY | rely + relies | 125 | `relies` 69, `rely` 56 |
| credible | — | 125 | `credible` 125 |

### group02（target = Generic，共 2459 行）

| 检索词 | 展开词形 | 命中数 | 各词形分项 |
|---|---|---:|---|
| corrections | — | 90 | `corrections` 84, `Corrections` 6 |
| english | — | 74 | `English` 74 |
| GOOD | good + better | 949 | `good` 424, `better` 253, `Better` 187, `Good` 85 |
| vocabulary | — | 42 | `vocabulary` 42 |
| tense | — | 99 | `tense` 97, `Tense` 2 |
| expressions | — | 49 | `expressions` 48, `Expressions` 1 |
| ARTICLE | article + articles | 167 | `article` 70, `articles` 48, `Article` 34, `Articles` 15 |
| thank | — | 50 | `Thank` 48, `thank` 2 |
| some | — | 939 | `some` 530, `Some` 409 |

### group03（target = Chinese，共 1868 行）

| 检索词 | 展开词形 | 命中数 | 各词形分项 |
|---|---|---:|---|
| chinese | — | 61 | `Chinese` 61 |
| ARTICLE | article + articles | 272 | `articles` 105, `article` 85, `Article` 58, `Articles` 24 |
| RUN-ON | run-on + run-ons + run on + run ons | 151 | `run ons (split)` 72, `run on (split)` 46, `Run on (split)` 31, `Run ons (split)` 2 |
| splices | — | 112 | `splices` 111, `Splices` 1 |
| sentences | — | 667 | `sentences` 648, `Sentences` 19 |
| patterns | — | 93 | `patterns` 91, `Patterns` 2 |
| english | — | 138 | `English` 138 |
| issues | — | 374 | `issues` 316, `Issues` 58 |

### group04（target = Generic，共 655 行）

| 检索词 | 展开词形 | 命中数 | 各词形分项 |
|---|---|---:|---|
| arguments | — | 163 | `arguments` 157, `Arguments` 6 |
| question | — | 128 | `question` 125, `Question` 3 |
| raises | — | 47 | `raises` 47 |
| errors | — | 317 | `errors` 312, `Errors` 5 |

### group05（target = Chinese，共 2325 行）

| 检索词 | 展开词形 | 命中数 | 各词形分项 |
|---|---|---:|---|
| chinese | — | 61 | `Chinese` 61 |
| organization | — | 417 | `organization` 277, `Organization` 140 |
| body | — | 595 | `body` 305, `Body` 290 |
| organizing | — | 54 | `organizing` 51, `Organizing` 3 |
| readers | — | 285 | `readers` 265, `Readers` 20 |
| grammar | — | 680 | `grammar` 499, `Grammar` 181 |
| mechanics | — | 99 | `Mechanics` 60, `mechanics` 39 |
| restate | — | 134 | `restate` 86, `Restate` 48 |

### group06（target = German，共 2200 行）

| 检索词 | 展开词形 | 命中数 | 各词形分项 |
|---|---|---:|---|
| german | — | 491 | `German` 491 |
| transfer | — | 43 | `transfer` 38, `Transfer` 5 |
| false | — | 49 | `false` 35, `False` 14 |
| SPEAKER | speaker + speakers | 113 | `speaker` 73, `speakers` 38, `Speakers` 2 |
| english | — | 508 | `English` 508 |
| speaking | — | 61 | `speaking` 61 |
| INFLUENCE | influence + influenced | 103 | `influence` 54, `influenced` 46, `Influence` 2, `Influenced` 1 |
| order | — | 118 | `order` 118 |
| ARTICLE | article + articles | 479 | `article` 177, `articles` 156, `Article` 100, `Articles` 46 |
| usage | — | 122 | `usage` 122 |
| natural | — | 113 | `natural` 112, `Natural` 1 |

### group07（target = German，共 2398 行）

| 检索词 | 展开词形 | 命中数 | 各词形分项 |
|---|---|---:|---|
| german | — | 491 | `German` 491 |
| ARTICLE | article + articles | 479 | `article` 177, `articles` 156, `Article` 100, `Articles` 46 |
| transfer | — | 43 | `transfer` 38, `Transfer` 5 |
| english | — | 508 | `English` 508 |
| SPEAKER | speaker + speakers | 113 | `speaker` 73, `speakers` 38, `Speakers` 2 |
| influenced | — | 47 | `influenced` 46, `Influenced` 1 |
| PATTERN | pattern + patterns | 241 | `patterns` 162, `pattern` 71, `Patterns` 8 |
| NOUN | noun + nouns | 107 | `nouns` 54, `noun` 53 |
| order | — | 118 | `order` 118 |
| register | — | 73 | `register` 42, `Register` 31 |
| natural | — | 113 | `natural` 112, `Natural` 1 |
| writer | — | 65 | `writer` 64, `Writer` 1 |

### group08（target = Generic，共 1639 行）

| 检索词 | 展开词形 | 命中数 | 各词形分项 |
|---|---|---:|---|
| clarity | — | 271 | `clarity` 240, `Clarity` 31 |
| organization | — | 396 | `organization` 276, `Organization` 120 |
| SUPPORT | support + supporting | 626 | `support` 506, `supporting` 83, `Support` 36, `Supporting` 1 |
| strengthen | — | 346 | `strengthen` 174, `Strengthen` 172 |

### group09（target = Baseline，共 4577 行）

| 检索词 | 展开词形 | 命中数 | 各词形分项 |
|---|---|---:|---|
| CLAIM | claim + claims | 1689 | `claim` 1018, `claims` 643, `Claims` 15, `Claim` 13 |
| COUNTERARGUMENT | counterargument + counterarguments | 409 | `counterargument` 194, `counterarguments` 119, `Counterargument` 69, `Counterarguments` 27 |
| evidence | — | 1543 | `evidence` 1388, `Evidence` 155 |
| reasoning | — | 267 | `reasoning` 258, `Reasoning` 9 |
| RELY | rely + relies | 132 | `relies` 73, `rely` 59 |
| arguable | — | 96 | `arguable` 95, `Arguable` 1 |
| credible | — | 130 | `credible` 130 |
| correctness | — | 49 | `correctness` 48, `Correctness` 1 |
| prose | — | 52 | `prose` 52 |
| SHARPEN | sharpen + sharpening | 143 | `sharpening` 50, `Sharpen` 46, `sharpen` 42, `Sharpening` 5 |
| aim | — | 67 | `Aim` 39, `aim` 28 |

### group10（target = Generic，共 2382 行）

| 检索词 | 展开词形 | 命中数 | 各词形分项 |
|---|---|---:|---|
| corrections | — | 90 | `corrections` 84, `Corrections` 6 |
| english | — | 74 | `English` 74 |
| slightly | — | 58 | `slightly` 58 |
| GOOD | good + better | 949 | `good` 424, `better` 253, `Better` 187, `Good` 85 |
| grammar | — | 658 | `grammar` 485, `Grammar` 173 |
| verb | — | 221 | `verb` 186, `Verb` 35 |
| ARTICLE | article + articles | 167 | `article` 70, `articles` 48, `Article` 34, `Articles` 15 |
| strengths | — | 165 | `Strengths` 101, `strengths` 64 |

### group11（target = Baseline，共 2040 行）

| 检索词 | 展开词形 | 命中数 | 各词形分项 |
|---|---|---:|---|
| evidence | — | 1543 | `evidence` 1388, `Evidence` 155 |
| accurate | — | 79 | `accurate` 77, `Accurate` 2 |
| anecdote | — | 111 | `anecdote` 105, `Anecdote` 6 |
| expert | — | 38 | `expert` 37, `Expert` 1 |
| effectively | — | 120 | `effectively` 120 |
| engaging | — | 98 | `engaging` 75, `Engaging` 23 |
| promising | — | 51 | `promising` 51 |

### group12（target = L1，共 1369 行）

| 检索词 | 展开词形 | 命中数 | 各词形分项 |
|---|---|---:|---|
| underdeveloped | — | 65 | `underdeveloped` 59, `Underdeveloped` 6 |
| consistent | — | 135 | `consistent` 128, `Consistent` 7 |
| sentence | — | 942 | `sentence` 799, `Sentence` 143 |
| vague | — | 126 | `vague` 112, `Vague` 14 |
| check | — | 101 | `check` 85, `Check` 16 |

## 零命中词形

无。所有检索词在其 target corpus 中均有命中。

## 文件生成清单

| 文件 | 存在 | 数据行数 |
|---|---|---:|
| `concordance_group01.tsv` | 是 | 2439 |
| `concordance_group02.tsv` | 是 | 2459 |
| `concordance_group03.tsv` | 是 | 1868 |
| `concordance_group04.tsv` | 是 | 655 |
| `concordance_group05.tsv` | 是 | 2325 |
| `concordance_group06.tsv` | 是 | 2200 |
| `concordance_group07.tsv` | 是 | 2398 |
| `concordance_group08.tsv` | 是 | 1639 |
| `concordance_group09.tsv` | 是 | 4577 |
| `concordance_group10.tsv` | 是 | 2382 |
| `concordance_group11.tsv` | 是 | 2040 |
| `concordance_group12.tsv` | 是 | 1369 |

共 12 个组文件（全部生成），另有本日志 `extraction_log.md`。无命中的组仍会生成仅含列标题的文件。

## 核验发现：RUN-ON 的实际频次低于既有记录

研究背景文档记录：「run（组 3、5）更名 RUN-ON：concordance 确认全部 175 次均为
run-on(s) 切分残留」。本次提取的逐条核验**不支持**该结论。

对 `run` 的每一次出现检查其后继 token 是否为 `on` / `ons`：

| 语料 | token `run` 总数 | 属 run-on 切分 | 真实动词/名词 `run` |
|---|---:|---:|---:|
| Chinese | 175 | **151** | **24** |
| German | 144 | 117 | 27 |
| Generic | 134 | 110 | 24 |

Chinese 语料中 24 例非切分残留的 `run`，语境示例：

- `a cool million` **run** `like hell guess what happens`（引用作文原文的口语表达）
- `We` **run** `the risk of contaminating our land`
- `and is harmless in the long` **run** `Which do you believe`
- `situations should be situation` **run** `a careful spell check pass`
- `Several sentences` **run** `together without proper punctuation`（动词用法，非复合名词）
- `coaches do` **run** `up the score`

最后一类值得注意：`sentences run together` 在语义上确实描述流水句，但 `run` 在此
是动词，不是 `run-on` 这一复合名词的切分残留，与 `Run on sentences` 属不同词位。

**影响**：RUN-ON 在 Chinese 的 Freq_Tar 应为 **151** 而非 175，German 为 117，
Generic 为 110。若关键词表中该词位的 LL / LR 基于 175 计算，需重算。

本次提取严格按 bigram `run` + `on|ons` 匹配，故 group03 的 RUN-ON 共 151 行，
不含上述 24 例。
