# RT-Lynx: Putting the GEMM Sparsity In a Right Way for Diffusion Models

- Citation key: `cong2026rtlynx`.
- Authors: Cong, Xing; Tang, Hanlin; Liu, Kan; Tao, Lan; Qu, Lin; Xie, Chenhao.
- Publication: arXiv preprint, 2026; version 2.
- Source: [paper](https://arxiv.org/abs/2605.26632v2); [full text](https://arxiv.org/html/2605.26632v2).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Sections 4.1–4.4 and Table 3.

## What it establishes

Applies N:M activation sparsity, rescales retained values to compensate norm loss, and trains a LoRA correction branch. CUDA execution fuses selection/compression and overlaps sparse and correction work.

## Relevance to our goals

A direct diffusion activation-sparsity comparator; fusion and norm compensation are already described.

## Limits and transfer conditions

LoRA correction adds computation and preparation. The ablation without adaptation must be separated from the complete method. Preserving activation norm does not establish preservation of the receiving matrix output. No custom-array energy result is adopted here.
