# DiSC: Resolution-Scalable Acceleration of Diffusion Models by Exploiting Sparsity and Cached Token Reuse with Hash-based Distribution

- Citation key: `yoon2026disc`.
- Authors: Yoon, Jieon; Lee, Hangyeol; Heo, Jaehoon; Kim, Joo-Young.
- Publication: arXiv preprint, 2026; pinned author version.
- Source: [paper](https://arxiv.org/abs/2605.25798v1); [full text](https://arxiv.org/html/2605.25798v1).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Sections III–IV and V-A.

## What it establishes

Uses latent differences to select cached-token reuse and reuses thresholded attention masks. Hash-based on-chip bank distribution maps hybrid sparse/dense work onto shared compute engines.

## Relevance to our goals

Direct prior art for joining runtime work omission, memory addressing and regular computation.

## Limits and transfer conditions

Hyperparameters were tuned on a data subset. The custom accelerator uses cycle simulation and synthesized logic/memory estimates; GPU timing/energy is measured separately. Thus cross-platform savings are not isolated algorithm-only gains. Retained history, bank conflicts and mask-generation/refresh costs remain relevant.
