---
name: Enhancement
about: 内容增补或扩展
title: 'enhance:（第 3.3 节）补充证明'
labels: enhance
assignees: ''

---

checklist
- [ ] 我已经阅读并遵守了 [Issue 规范](../../../issue-format.md)
- [ ] 我确认这是最新版本 [PDF](../../main.pdf) 中需要增强的内容
- [ ] 我已经搜索过之前的 Issue，确保这个建议没有被提出过

位置：第 20 页，第 3.3 节

源文件：`probability.tex`，第 50 行

原文：
> 显然，$P(A \cup B)\leq P(A) + P(B)$。

问题：

证明过程不够详细，建议修改为：

> 根据 union bound 不等式，我们有 $P(A \cup B)\leq P(A) + P(B)$。
