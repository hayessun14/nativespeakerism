# nativespeakerism

AI 学术写作反馈中的 native-speakerism：语料库驱动的关键词研究。

174 篇 LOCNESS 英语母语者议论文，各附 5 种语言身份标签（L1 / Generic / Chinese / German / Baseline），分别交给 Claude 与 GPT 生成反馈，共 1,740 条。作文文本完全相同，唯一变量是 prompt 中的身份标签。

## 目录

```
corpora/          5 个 AntConc 语料库（.db，SQLite），每库 348 篇反馈
                  （doc_id 0–173 为 Claude，174–347 为 GPT）
keywords/         关键词主表 keyword_ALL_selected.md（12 组 891 词位）
                  归并标签对照表、待定词表、修订日志
  groups/         12 组各自的关键词提取结果
coding/           编码结果
                  all_codes.tsv      全部 891 词位的三维度编码总表
                  final_report.md    最终编码统计报告（由 all_codes.tsv 生成）
                  group*_tables.md   各组编码表与附表（由 analyze.py 生成）
                  group*_coding_resolved.md   各组论证（concordance 消解后）
                  group*_coding.md   消解前的过程存档，其中占比数字已作废
concordances/
  wordlists/      检索词表与归并映射
  by_group/       按 12 组提取的 concordance（每组只在其 target corpus 中检索）
  batches/        待定词 concordance，分 6 批
  judgments_batch1.tsv   concordance 语义判定，第 1 批
merged/           10 个 txt：每个条件 × 模型的 174 条反馈合为一个文件，
                  每条前标注原始文件名
references/       Holliday 一书的 PDF 与 markdown 转写
scripts/          全部脚本，均在仓库根目录下运行
```

## 数据流

```
corpora/*.db
  ├─ extract_concordances.py / extract_by_group.py ─→ concordances/
  └─ merge_by_condition.py ─→ merged/

keywords/keyword_ALL_selected.md + coding/group*_codes.tsv
  └─ merge_codes.py ─→ coding/all_codes.tsv
                          ├─ final_report.py ─→ coding/final_report.md
                          └─ analyze.py <组号> ─→ coding/group*_tables.md
```

`apply_verdicts.py` 已停用，仅作过程存档，请勿再运行。

## 运行

只用 Python 标准库，无需安装依赖。在仓库根目录下运行，例如：

```bash
python3 scripts/final_report.py
python3 scripts/extract_by_group.py --groups group03
python3 scripts/merge_by_condition.py
```

## 关于分支

`main` 是唯一的工作分支。每次 Claude Code 对话会自动建一个 `claude/…` 分支，做完后合并回 `main`。旧的 `claude/…` 分支已全部并入 `main`，仅作存档。
