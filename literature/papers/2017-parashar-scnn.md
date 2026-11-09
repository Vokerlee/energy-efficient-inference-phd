# SCNN: An Accelerator for Compressed-sparse Convolutional Neural Networks

- Citation key: `parashar2017scnn`.
- Authors: Parashar, Angshuman; others.
- Publication: ISCA, 2017.
- Source: [paper](https://arxiv.org/abs/1708.04485v1); [full text reviewed](https://arxiv.org/pdf/1708.04485v1).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Compressed operands, multiplier reuse, and scatter accumulation.
- Evidence: Sparse accelerator architecture evaluation.

## What it establishes

Maintains sparse weights and activations in compressed form and uses specialized accumulation to handle generated products.

## Relevance to our goals

A concrete reference for sparse data movement and accumulation overhead.

## Limits and transfer conditions

It does not establish efficient execution of arbitrary activation masks on a conventional systolic array. Combined weight/activation sparsity must be separated in our comparisons.
