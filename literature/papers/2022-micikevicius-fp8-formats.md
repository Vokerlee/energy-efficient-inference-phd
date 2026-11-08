# FP8 Formats for Deep Learning

- Citation key: `micikevicius2022fp8`.
- Authors: Micikevicius, Paulius; others.
- Publication: arXiv preprint, 2022.
- Source: [paper](https://arxiv.org/abs/2209.05433v2); [full text reviewed](https://arxiv.org/pdf/2209.05433v2).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Scaling discussion, format choices, and inference versus training evidence.
- Evidence: Format proposal and numerical experiments.

## What it establishes

Defines E4M3/E5M2 formats and explains the role of scaling; detailed scaling-factor selection is outside its main scope.

## Relevance to our goals

Separates representation range from the algorithm that predicts or measures it.

## Limits and transfer conditions

Format support is not autonomous hardware adaptation. Most training evidence cannot establish inference quality or energy for a new controller.
