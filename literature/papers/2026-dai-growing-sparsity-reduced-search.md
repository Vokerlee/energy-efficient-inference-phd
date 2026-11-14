# Sparse Attention for Video Generation Acceleration via Growing Sparsity and Reduced Search

- Citation key: `dai2026gsrs`.
- Authors: Dai, Yun; Chen, Yuyun; Wen, Jiarui; Zhuang, Huiping; Chen, Cen; Zeng, Ziqian.
- Publication: arXiv preprint, 2026.
- Source: [paper](https://arxiv.org/abs/2610.21129v1); [full text reviewed](https://arxiv.org/html/2610.21129v1).
- Reviewed: 2026-11-14. Status: **full-text focused reading**.
- Reading focus: Sections 5.1–5.3 and Appendix A: search reuse and two-phase importance recovery.
- Evidence: Recent training-free algorithm and video-generation GPU experiments.

## What it establishes

Progressively changes Top-p selection within an early candidate set. Recovers block importance after current row normalization is available using stored block statistics.

## Relevance to our goals

A recent temporal-adaptation baseline that makes statistic-availability dependencies visible.

## Limits and transfer conditions

Search passes and warmup still execute work. Reusing candidates can miss later-emerging blocks; the evaluated models do not prove universal persistence or hardware cost.
