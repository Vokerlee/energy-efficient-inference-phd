# A Shape-Adaptive Architecture with Disaggregated Quantization for Efficient LLM Serving

- Citation key: `guo2026dynacore`.
- Authors: Cong Guo; Chiyue Wei; Bowen Duan; Haoxuan Shan; Benjamin F. Morris III; Yintao He; Hai Helen Li; Yiran Chen.
- Publication: author preprint, 2026; reviewed version `2610.07443v1`.
- Source: [paper](https://arxiv.org/abs/2610.07443v1); [reviewed text](https://arxiv.org/html/2610.07443v1).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Reading focus: Sections 3, 5–7 and 8.1: partial-sum routing, inner-product packing, mode selection and evaluation methodology.

## What it establishes

Combines array reshaping, split-K reduction and phase-specific quantization.
Its low-precision construction increases reduction work along K while retaining
one accumulator/output per PE. Runtime shape selection uses offline hardware
profiling tables. Evaluation includes SystemVerilog synthesis, component models
and a cycle-level serving simulator, rather than reported fabricated silicon.

## Relevance to our goals

Direct architectural comparator for precision-dependent K capacity with fixed
output count. Partial-sum reduction and output routing belong in the same cost
comparison as input precision and operand delivery.

## Limits and transfer conditions

Prepared quantization and phase/batch-shape scheduling do not establish a
calibration-free selector driven by each current activation block. Their
weight-stationarity, buffering, split-K schedule and arithmetic differ from
another accelerator. Neither output-width invariance nor combining tiling
with quantization is sufficient as a new contribution; additional controller,
numerical or integration work needs a matched comparison.
