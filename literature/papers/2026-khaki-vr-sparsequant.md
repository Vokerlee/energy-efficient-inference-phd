# VR-SparseQuant: Accurate FP4 Quantization with 2:4 Sparsity on Vera Rubin

- Citation key: `khaki2026vrsparsequant`.
- Authors: Khaki, Samir; Wang, Wei-Chen; Han, Song; Wang, Ryan Hanrui.
- Publication: arXiv author version, 2026; `2611.25717v1` reviewed.
- Source: [paper](https://arxiv.org/abs/2611.25717v1); [full text](https://arxiv.org/html/2611.25717v1).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Sections 3.3, 3.5 and 4.1–4.2.

## What it establishes

Represents an activation with two sparse FP4 streams. Online quartet selection ranks quantization-error reductions, with a second residual assignment. A calibrated scale ratio uses receiving-output error; shared-weight execution combines both products.

## Relevance to our goals

Direct prior art for quantizer-dependent gain selection, sparse residual correction and fused execution.

## Limits and transfer conditions

Fixed-scale local gain optimality does not imply output-error or task-quality optimality. Both streams together retain dense nonzero FLOP count; metadata adds traffic. No generic novelty follows from selecting two best error reductions. Reported hardware results were not reproduced.
