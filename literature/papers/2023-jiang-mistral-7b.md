# Mistral 7B

- Citation key: `jiang2023mistral7b`.
- Authors: Albert Q. Jiang and colleagues.
- Publication: arXiv:2310.06825v1, 2023.
- Source: [versioned paper](https://arxiv.org/abs/2310.06825v1); [full text](https://arxiv.org/html/2310.06825v1).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Section 2, Table 1, grouped-query and sliding-window attention.
- Evidence: Published architecture and inference implementation choices.

## What it establishes

Table 1 specifies hidden width 4096, FFN width 14336, 32 layers, 32 query
heads, eight key/value heads, head dimension 128 and vocabulary size 32000.
Grouped-query attention shares key/value heads; sliding-window attention
and a rolling cache limit retained context per layer.

## Relevance to our goals

Supplies concrete dimensions and attention variants for component experiments.
Record head dimension, query-to-key/value ratio and window/cache rules
separately when scaling a test configuration. Vocabulary size is independent
of hidden width and must be specified for an experimental output head.

## Limits and transfer conditions

A reduced, randomly initialized component is not a reproduction of the trained
model. Reported inference behavior does not establish energy consumption or
numerical-error tolerances for another implementation. The original paper's
context length must not be silently replaced by later checkpoint settings.
