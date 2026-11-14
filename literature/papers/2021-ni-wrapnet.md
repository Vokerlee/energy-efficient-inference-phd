# WrapNet: Neural Net Inference with Ultra-Low-Precision Arithmetic

- Citation key: `ni2021wrapnet`.
- Authors: Ni, Renkun; Chu, Hong-min; Castañeda, Oscar; Chiang, Ping-yeh; Studer, Christoph; Goldstein, Tom.
- Publication: ICLR; 2020 author preprint reviewed, 2021.
- Source: [paper](https://arxiv.org/abs/2007.13242v1); [full text reviewed](https://arxiv.org/pdf/2007.13242v1).
- Reviewed: 2026-11-14. Status: **full-text focused reading**.
- Reading focus: Sections 3–4: cyclic activation, overflow regularization, and training. The preprint title says Ultra-Low-Resolution Arithmetic.
- Evidence: Trained quantized networks and software/hardware arithmetic evaluation.

## What it establishes

Trains networks to tolerate narrow wrap-around accumulators through a cyclic activation and overflow-aware preparation.

## Relevance to our goals

A baseline for the quality consequences of narrow accumulation, distinct from guaranteeing exact integer sums.

## Limits and transfer conditions

Weights/activations and training are changed. This is not a drop-in overflow policy for an unchanged pretrained inference model.
