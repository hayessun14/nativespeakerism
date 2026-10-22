#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 pending_worklist 展开为逐行清单：一行 = 一个（词形 × 层 × 组）组合。

层与组的对应关系不能从 pending_worklist 还原——那里的 layers 是跨组聚合后的
字符串（如「维度一＋维度三」），并未说明哪一层出现在哪一组。故逐格数据取自
coding/all_codes.tsv，词形范围与优先级取自 coding/pending_worklist.tsv。
"""
import csv
from collections import defaultdict

TARGET = {1: "L1", 2: "Generic", 3: "Chinese", 4: "Generic",
          5: "Chinese", 6: "German", 7: "German", 8: "Generic",
          9: "Baseline", 10: "Generic", 11: "Baseline", 12: "L1"}
LAYER_CN = {"d1": "维度一", "act": "act 层", "hedge": "hedge 层", "c": "维度三"}

wl = list(csv.DictReader(open("coding/pending_worklist.tsv", encoding="utf-8"), delimiter="\t"))
prio = {r["type"]: int(r["priority"]) for r in wl}
wl_layers = {r["type"]: r["layers"] for r in wl}
rows = list(csv.DictReader(open("coding/all_codes.tsv", encoding="utf-8"), delimiter="\t"))

# 校验组号→target corpus 映射与总表的 target_corpus 列一致
mismatch = {(int(r["group"]), r["target_corpus"]) for r in rows
            if TARGET[int(r["group"])] != r["target_corpus"]}
assert not mismatch, f"组号映射与总表不符: {sorted(mismatch)}"

out = []
covered = set()
for r in rows:
    t = r["type"]
    if t not in prio:
        continue
    g = int(r["group"])
    for layer in ("d1", "act", "hedge", "c"):
        if r[layer] == "PENDING":
            out.append((prio[t], t, LAYER_CN[layer], g, TARGET[g]))
            covered.add(t)

# 无 PENDING 单元格的词形（note 标记待核 / 强制查询清单）：层取清单中的标签，
# 组取该词形在总表中出现的全部组
for t, p in prio.items():
    if t in covered:
        continue
    for g in sorted({int(r["group"]) for r in rows if r["type"] == t}):
        out.append((p, t, wl_layers[t], g, TARGET[g]))

out.sort(key=lambda x: (x[0], x[1].lower(), x[3]))
with open("coding/pending_wordlist.tsv", "w", encoding="utf-8", newline="\n") as f:
    f.write("word\tlayer\tgroup\ttarget_corpus\n")
    for _, t, layer, g, tc in out:
        f.write(f"{t}\t{layer}\t{g}\t{tc}\n")

# 覆盖自检
n_pend = sum(1 for r in rows for k in ("d1", "act", "hedge", "c")
             if r[k] == "PENDING" and r["type"] in prio)
n_expanded = sum(1 for x in out if x[1] in covered)
assert n_pend == n_expanded, f"PENDING 单元格 {n_pend} ≠ 展开行 {n_expanded}"
print(f"写出 coding/pending_wordlist.tsv：{len(out)} 行")
print(f"  其中源自 PENDING 单元格 {n_expanded} 行（与总表 PENDING 数一致）、"
      f"源自 note 标记／强制查询清单 {len(out) - n_expanded} 行")
print(f"  涉及词形 {len({x[1] for x in out})} 个（清单共 {len(prio)} 个）\n")
from collections import Counter
print("按优先级：", dict(sorted(Counter(x[0] for x in out).items())))
print("按 target corpus：", dict(sorted(Counter(x[4] for x in out).items())))
print("按层：", dict(sorted(Counter(x[2] for x in out).items(), key=lambda kv: -kv[1])))
dedup = {(x[1], x[2], x[4]) for x in out}
print(f"\n若按（词形 × 层 × target corpus）去重：{len(dedup)} 行"
      f"（组 2/4/8/10 同为 Generic、组 6/7 同为 German、组 3/5 同为 Chinese、组 1/12 同为 L1、"
      f"组 9/11 同为 Baseline，故同一语料会被检索多次）")
