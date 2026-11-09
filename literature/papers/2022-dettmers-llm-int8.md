# LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale

- Citation key: `dettmers2022llmint8`.
- Authors: Dettmers, Tim; Lewis, Mike; Belkada, Younes; Zettlemoyer, Luke.
- Publication: NeurIPS, 2022.
- Source: [paper](https://arxiv.org/abs/2208.07339v2); [full text reviewed](https://arxiv.org/pdf/2208.07339v2).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Mixed-precision decomposition and outlier feature selection.
- Evidence: GPU implementation and language-model quality evaluation.

## What it establishes

Separates exceptional feature dimensions into a higher-precision multiplication while quantizing the remaining path.

## Relevance to our goals

A direct baseline for selective precision based on activation outliers.

## Limits and transfer conditions

Feature-wise exceptions are not arbitrary element-wise sparse correction. Reported memory/quality behavior does not establish systolic energy savings or a universal detection threshold.
