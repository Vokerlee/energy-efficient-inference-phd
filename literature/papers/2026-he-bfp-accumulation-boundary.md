# Precision boundary modeling for area-efficient Block Floating Point accumulation

- Citation key: `he2026bfpboundary`.
- Authors: Jun He; Jing Feng; Xin Ju; Yasong Cao; Zhongdi Luo; Jianchao Yang; Jingkui Yang; Gang Li; Jian Cheng; Dong Chen; Mei Wen.
- Publication: 2026; DOI `10.1016/j.sysarc.2026.103704`.
- Source: [publisher](https://doi.org/10.1016/j.sysarc.2026.103704).
- Reviewed: 2026-11-23. Status: **publisher abstract, introduction and section snippets; full-text review pending**.
- Reading focus: FnRR, direct/chunked accumulation and hardware/accuracy claim boundaries; authors verified through Crossref.

## What it establishes

Introduces a Frobenius-norm-retention analysis for BFP accumulation precision, including a hierarchical chunked scheme and corresponding hardware. Evaluates model accuracy alongside implementation costs.

## Relevance to our goals

Close baseline for reducing accumulator precision and choosing chunk structure rather than only lowering operand width.

## Limits and transfer conditions

Accessible evidence does not establish the complete runtime policy or a universally valid task-error bound. A statistical similarity metric and tested accuracy boundaries are distinct from exact accumulation. Full formulas, assumptions and online-versus-prepared choices remain reading dependencies; reported implementation savings are not target-array measurements.
