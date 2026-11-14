# ResQ: Residual Quantization for Video Perception

- Citation key: `abati2023resq`.
- Authors: Abati, Davide; Ben Yahia, Haitam; Nagel, Markus; Habibian, Amirhossein.
- Publication: ICCV, 2023.
- Source: [paper](https://arxiv.org/abs/2308.09511v1); [full text reviewed](https://arxiv.org/pdf/2308.09511v1).
- Reviewed: 2026-11-14. Status: **full-text focused reading**.
- Reading focus: Section 4.2: per-pixel activation precision and Young-inequality error surrogate.
- Evidence: Analytical local error bound, calibrated quantizer policy, and video task evaluation.

## What it establishes

Quantizes temporal residuals and selects per-pixel activation precision from calibrated candidates using a norm-based output-error bound.

## Relevance to our goals

Direct prior art against claiming that deriving an online precision rule from local error is inherently new.

## Limits and transfer conditions

A local bound is not a global task-quality guarantee. Include stored reference features, reconstruction, policy evaluation, and mapping per-pixel modes to physical tiles.
