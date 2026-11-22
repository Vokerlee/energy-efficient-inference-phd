# WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity

- Citation key: `chen2026wisparse`.
- Authors: Chen, Lei; Meng, Yuan; Zhan, Xiaoyu; Wang, Zhi; Zhu, Wenwu.
- Publication: arXiv preprint, 2026; version 1.
- Source: [paper](https://arxiv.org/abs/2602.14452v1); [full text](https://arxiv.org/html/2602.14452v1).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Sections 4.2–4.3.

## What it establishes

Scores channels using activation magnitude and weight norms raised to calibrated layer-specific exponents. Coarse-to-fine preparation allocates sparsity across Transformer blocks and their layers; live masks use fixed thresholds.

## Relevance to our goals

Weight-aware activation scoring and mixed sparsity allocation already have explicit prior art.

## Limits and transfer conditions

Mixed granularity here refers to block/layer allocation, not demonstrated runtime changes to physical matrix-tile geometry. Preparation uses calibration; this difference does not alone establish novelty for an alternative controller.
