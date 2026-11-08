# Power and Energy-efficiency Roofline Model for GPUs

- Citation key: `ghane2018energyroofline`.
- Authors: Ghane, Millad; Larkin, Jeff; Shi, Larry; Chandrasekaran, Sunita; Cheung, Margaret S..
- Publication: arXiv preprint, 2018.
- Source: [paper](https://arxiv.org/abs/1809.09206v1); [full text reviewed](https://arxiv.org/pdf/1809.09206v1).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Section II model construction and GPU optimization ceilings.
- Evidence: Analytical energy/power model with GTX 970 and K80 examples.

## What it establishes

Extends roofline-style reasoning to energy efficiency and power, separating arithmetic and memory work. Different optimizations can affect time and power differently.

## Relevance to our goals

Supports analyzing energy per useful operation alongside a performance roofline, rather than inferring energy from speedup.

## Limits and transfer conditions

The model uses simplified energy terms and older GPUs. Its treatment of constant system energy needs care when runtime changes; our model uses background power integrated over duration.
