# SVDQuant: Absorbing Outliers by Low-Rank Components for 4-Bit Diffusion Models

- Citation key: `li2025svdquant`.
- Authors: Li, Muyang; Lin, Yujun; Zhang, Zhekai; Cai, Tianle; Li, Xiuyu; Guo, Junxian; Xie, Enze; Meng, Chenlin; Zhu, Jun-Yan; Han, Song.
- Publication: ICLR, 2025.
- Source: [paper](https://arxiv.org/abs/2411.05007v4); [full text reviewed](https://arxiv.org/pdf/2411.05007v4).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Outlier migration, low-rank branch, and Nunchaku fusion.
- Evidence: Diffusion quality and GPU implementation evaluation.

## What it establishes

Moves activation outliers into weights, then absorbs them in a higher-precision low-rank branch alongside low-bit residual computation.

## Relevance to our goals

Connects outlier handling, low-rank computation, and execution fusion in compute-intensive generation.

## Limits and transfer conditions

The decomposition is not a newly selected activation subspace at every hardware tile. Extra branches and weight changes must be isolated in comparisons.
