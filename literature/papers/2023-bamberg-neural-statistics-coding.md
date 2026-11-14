# Exploiting Neural-Network Statistics for Low-Power DNN Inference

- Citation key: `bamberg2023nnstats`.
- Authors: Bamberg, Lennart; Najafi, Ardalan; Garcia-Ortiz, Alberto.
- Publication: arXiv preprint, 2023.
- Source: [paper](https://arxiv.org/abs/2311.05557v1); [full text reviewed](https://arxiv.org/pdf/2311.05557v1).
- Reviewed: 2026-11-14. Status: **full-text focused reading**.
- Reading focus: Sections 3–4: bit statistics, physical-word/integer/real levels, and coding at memory/PE boundaries.
- Evidence: Statistical analysis and low-power representation/circuit evaluation.

## What it establishes

Exploits bit probabilities and switching statistics through low-cost coding of stored/transmitted weights and activations.

## Relevance to our goals

Shows that represented width alone is insufficient to model memory, interconnect, and arithmetic energy.

## Limits and transfer conditions

The activation analysis is ReLU-oriented. Component-specific estimates, representations, and pruning conditions cannot be generalized to BF16/SiLU diffusion or whole-chip savings.
