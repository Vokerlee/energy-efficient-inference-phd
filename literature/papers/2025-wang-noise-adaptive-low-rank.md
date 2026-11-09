# NA-LR: Noise-Adaptive Low-Rank Parameterisation for Efficient Diffusion Models

- Citation key: `wang2025nalr`.
- Authors: Wang, Jingyuan; Ottomano, Federico; Li, Yingzhen.
- Publication: Rethinking AI Workshop at EurIPS, 2025.
- Source: [paper](https://fedeotto.github.io/publications/nalr.html); [full text reviewed](https://rethinking-ai.github.io/assets/papers/9_NA_LR_Noise_Adaptive_Low_Ran.pdf).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Nested rank schedule, training masks, and diffusion evaluation.
- Evidence: Workshop algorithm and small diffusion-model experiments.

## What it establishes

Allocates rank slices according to noise level and trains models to support the nested schedule.

## Relevance to our goals

An existing example of iteration-conditioned low-rank inference.

## Limits and transfer conditions

This is not runtime activation factorization of an unchanged checkpoint. Its model/dataset scale and training requirements constrain transfer.
