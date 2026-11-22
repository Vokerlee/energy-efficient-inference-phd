# The Llama 3 Herd of Models

- Citation key: `dubey2024llama3`.
- Authors: Abhimanyu Dubey and colleagues (Llama Team, AI at Meta).
- Publication: arXiv:2407.21783v1, 2024.
- Source: [versioned paper](https://arxiv.org/abs/2407.21783v1); [full text](https://arxiv.org/html/2407.21783v1).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Section 3.2, Table 3 and Section 6.2; not an exhaustive review.
- Evidence: Architecture specification and reported FP8 inference evaluation.

## What it establishes

The 8B configuration has hidden width 4096, FFN width 14336, 32 query heads
and eight key/value heads. Head dimension 128 follows from 4096/32.
The vocabulary is about 128K, not 32000.

For 405B inference, Section 6.2 uses dynamic row-wise FP8 scaling with
additional restrictions, including unquantized first/last Transformer layers
and a scale cap of 1200. Strong standard-benchmark scores can coexist with
occasional corrupted responses; the authors also compare reward-score
distributions for generated responses.

## Relevance to our goals

Provides architecture proportions and an existing dynamic-scaling comparator.
The quality evaluation motivates testing response distributions and rare
failures in addition to aggregate scores.

## Limits and transfer conditions

These are distinct 8B architecture and 405B inference observations.
They do not establish a universal scale cap, calibration-free hardware policy
or energy saving. Reduced initialized blocks cannot establish trained-model
quality or long-trajectory error behavior.
