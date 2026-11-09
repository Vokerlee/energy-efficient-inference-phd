# Microscaling Data Formats for Deep Learning

- Citation key: `rouhani2023mx`.
- Authors: Darvish Rouhani, Bita; others.
- Publication: arXiv preprint, 2023.
- Source: [paper](https://arxiv.org/abs/2310.10537v3); [full text reviewed](https://arxiv.org/pdf/2310.10537v3).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Block representation, conversion algorithm, scaling format, and inference evaluation.
- Evidence: Numerical format specification/evaluation; training and inference experiments.

## What it establishes

Defines shared-scale blocks with narrow element formats. Representation, scale format, and block size jointly determine numerical behavior.

## Relevance to our goals

A hardware-oriented format baseline; scale metadata and reduction grouping must be modeled explicitly.

## Limits and transfer conditions

A format definition does not specify an autonomous predictor or our execution tile. Training results are not inference evidence; conversion and physical implementation costs need separate evaluation.
