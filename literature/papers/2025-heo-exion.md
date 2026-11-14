# EXION: Exploiting Inter- and Intra-Iteration Output Sparsity for Diffusion Models

- Citation key: `heo2025exion`.
- Authors: Heo, Jaehoon; Putra, Adiwena; Yoon, Jieon; Yune, Sungwoong; Lee, Hangyeol; Kim, Ji-Hoon; Kim, Joo-Young.
- Publication: HPCA, 2025.
- Source: [paper](https://arxiv.org/abs/2501.05680v1); [full text reviewed](https://arxiv.org/html/2501.05680v1).
- Reviewed: 2026-11-14. Status: **full-text focused reading**.
- Reading focus: Sections III–V: dense/sparse iterations, output reuse, ConMerge, eager prediction, and evaluation boundary.
- Evidence: Diffusion task evaluation, RTL synthesis, and cycle/DRAM simulation.

## What it establishes

Reuses selected FFN outputs across iterations, predicts attention work, and compacts output-sparse computation with ConMerge.

## Relevance to our goals

Separates omitted output computation from zero-valued input sparsity and shows the need to account for compaction.

## Limits and transfer conditions

Thresholds, refresh iterations, integer conversion, and reuse all affect quality. Accelerator energy is estimated from implementation/modeling, not a physical chip measurement.
