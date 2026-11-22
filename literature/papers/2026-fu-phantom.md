# Phantom: Temporal Caching for Diffusion Models

- Citation key: `fu2026phantom`.
- Authors: Fu, Yuzhe; Guo, Cong; Shao, Zishan; Duan, Bowen; Wei, Chiyue; Shan, Haoxuan; Jiang, Ting; Ye, Hancheng; Ku, Jonathan; Zhou, Changchun; Li, Hai Helen; Chen, Yiran.
- Publication: arXiv preprint, 2026; pinned author version.
- Source: [paper](https://arxiv.org/abs/2611.06019v1); [full text](https://arxiv.org/html/2611.06019v1).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Sections III–VI and VII-D.

## What it establishes

Alternates full refresh and differential steps. Token-change reductions, an online TopK heap and merged address masks select recomputation. A condensed pipeline gathers selected tokens into dense systolic work and scatters updates.

## Relevance to our goals

Direct prior art for translating runtime temporal sparsity into regular matrix execution.

## Limits and transfer conditions

A partition of the global buffer stages cache tiles; bulk layer histories reside in DRAM. Neither cache capacity nor traffic is free. Stride/TopK choices and refresh are part of the quality tradeoff. Reported gains were not reproduced.
