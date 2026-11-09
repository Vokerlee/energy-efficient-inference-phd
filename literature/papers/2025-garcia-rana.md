# Adaptive Rank Allocation: Speeding Up Modern Transformers with RaNA Adapters

- Citation key: `garcia2025rana`.
- Authors: Garcia, Roberto; Liu, Jerry; Sorvisto, Daniel; Eyuboglu, Sabri.
- Publication: ICLR, 2025.
- Source: [paper](https://arxiv.org/abs/2503.18216v2); [full text reviewed](https://arxiv.org/pdf/2503.18216v2).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Low-rank adapters, input masks, and model evaluation.
- Evidence: Learned adaptive-computation method and transformer experiments.

## What it establishes

Combines low-rank linear decomposition with input-dependent rank/neuron masking.

## Relevance to our goals

Direct prior art for adaptive rank allocation without relying on ordinary activation zeros.

## Limits and transfer conditions

Learned adapters/masking change the model. Logical FLOP reduction does not determine fixed-size array utilization or controller energy.
