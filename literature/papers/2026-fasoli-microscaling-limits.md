# Is Finer Better? The Limits of Microscaling Formats in Large Language Models

- Citation key: `fasoli2026microscaling`.
- Authors: Fasoli, Andrea; Kar, Monodeep; Liu, Chi-Chun; Venkataramani, Swagath; Srinivasan, Viji; Chang, Leland; Wang, Naigang.
- Publication: arXiv preprint, 2026.
- Source: [paper](https://arxiv.org/abs/2601.19026v1); [full text reviewed](https://arxiv.org/pdf/2601.19026v1).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Small-block anomaly, scale dynamic range, and analytical explanation.
- Evidence: Numerical analysis and LLM distribution/model experiments.

## What it establishes

Shows conditions where smaller quantization blocks worsen results because the scale representation itself has insufficient range.

## Relevance to our goals

Requires testing scale encoding rather than assuming finer groups always improve activation quantization.

## Limits and transfer conditions

The phenomenon depends on specific formats and distributions. It is not a universal failure of fine-grained quantization or measured energy evidence.
