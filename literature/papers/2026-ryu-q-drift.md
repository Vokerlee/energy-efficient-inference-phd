# Q-Drift: Quantization-Aware Drift Correction for Diffusion Model Sampling

- Citation key: `ryu2026qdrift`.
- Authors: Ryu, Sooyoung; Salzmann, Mathieu; Javed, Saqib.
- Publication: arXiv preprint, 2026.
- Source: [paper](https://arxiv.org/abs/2603.18095v2); [full text reviewed](https://arxiv.org/pdf/2603.18095v2).
- Reviewed: 2026-11-09. Status: **full-text focused reading**.
- Reading focus: Conditional residual variance, calibrated factors, and sampling evaluation.
- Evidence: Sampler-side correction and diffusion quality experiments.

## What it establishes

Uses calibrated quantization-residual information to adjust sampling drift through per-step correction factors.

## Relevance to our goals

Recent prior art for improving final generation despite quantized model execution.

## Limits and transfer conditions

It modifies the sampler and relies on calibration. Better distributional quality need not mean closer paired outputs; it does not validate our hardware or range controller.
