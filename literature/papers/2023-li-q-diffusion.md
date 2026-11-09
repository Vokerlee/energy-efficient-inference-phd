# Q-Diffusion: Quantizing Diffusion Models

- Citation key: `li2023qdiffusion`.
- Authors: Li, Xiuyu; others.
- Publication: ICCV, 2023.
- Source: [paper](https://arxiv.org/abs/2302.04304v3); [full text reviewed](https://arxiv.org/pdf/2302.04304v3).
- Reviewed: 2026-11-09. Status: **full-text focused reading**.
- Reading focus: Timestep calibration, shortcut quantization, and full sampling evaluation.
- Evidence: Diffusion PTQ method and generation-quality experiments.

## What it establishes

Adapts calibration and quantization to diffusion timesteps and activation structure.

## Relevance to our goals

Shows why static samples or isolated layers can miss errors during iterative inference.

## Limits and transfer conditions

The calibration/method changes must be controlled when attributing a new runtime policy's benefit. Its results are not a universal timestep sensitivity rule.
