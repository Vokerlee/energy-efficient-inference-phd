# APT: Accelerating Diffusion Transformers via Attention Probability-Guided Pruning and Quantization

- Citation key: `yoo2026apt`.
- Authors: Yoo, Sungyeob; Kim, Seeyeon; Park, Joonyong; Han, Seunghee; Kim, Joo-Young.
- Publication: ICCAD 2026; pinned author version.
- Source: [paper](https://arxiv.org/abs/2608.25380v1); [full text](https://arxiv.org/html/2608.25380v1).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Sections 3.1–3.2, 4 and 5.1.

## What it establishes

Attention probabilities select skipping, 6-bit or 12-bit execution. Runtime masks depend on inputs, while thresholds use per-model, per-head/timestep offline statistics. Previous-step normalization estimates enable tiled attention; hardware manages masks and sparse addresses.

## Relevance to our goals

An existing unified signal for precision and pruning, rather than an empty research niche.

## Limits and transfer conditions

Charge normalization prediction, mask handling and refresh. Evaluation combines model-quality tests and hardware estimates, not measured custom silicon. Removing profiling alone would not establish a new algorithm.
