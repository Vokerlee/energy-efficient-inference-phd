# SpargeAttention: Accurate and Training-free Sparse Attention Accelerating Any Model Inference

- Citation key: `zhang2025spargeattn`.
- Authors: Zhang, Jintao; Xiang, Chendong; Huang, Haofeng; Wei, Jia; Xi, Haocheng; Zhu, Jun; Chen, Jianfei.
- Publication: ICML; revised author version, 2025.
- Source: [paper](https://arxiv.org/abs/2502.18137v8); [full text reviewed](https://arxiv.org/html/2502.18137v8).
- Reviewed: 2026-11-14. Status: **full-text focused reading**.
- Reading focus: Sections 3.1–3.6: two filters, online normalization, and SageAttention integration.
- Evidence: Algorithm and GPU inference experiments across language, image, and video models.

## What it establishes

Predicts blocks to omit from QK and PV, then uses online-softmax information to omit additional PV work. Integrates the sparse path with quantized SageAttention.

## Relevance to our goals

A direct joint sparsity/quantization baseline with explicit decision stages.

## Limits and transfer conditions

GPU timings do not establish systolic energy savings or universal quality preservation. Calibration thresholds, fallback, and each filter's available information matter.
