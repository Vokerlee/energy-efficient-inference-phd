# PTQD: Accurate Post-Training Quantization for Diffusion Models

- Citation key: `he2023ptqd`.
- Authors: He, Yefei; Liu, Luping; Liu, Jing; Wu, Weijia; Zhou, Hong; Zhuang, Bohan.
- Publication: NeurIPS, 2023.
- Source: [paper](https://arxiv.org/abs/2305.10657v4); [full text reviewed](https://arxiv.org/pdf/2305.10657v4).
- Reviewed: 2026-11-09. Status: **full-text focused reading**.
- Reading focus: Correlated/residual error, mean/variance correction, and sampling.
- Evidence: Quantization-error model and diffusion experiments.

## What it establishes

Models quantization effects within denoising and evaluates correction and timestep precision choices.

## Relevance to our goals

A baseline for distinguishing local quantization error from trajectory-level consequences.

## Limits and transfer conditions

Noise-model assumptions and calibrated corrections are not universal guarantees. Bit-operation savings are not directly hardware energy measurements.
