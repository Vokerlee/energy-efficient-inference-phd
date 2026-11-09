# A2Q: Accumulator-Aware Quantization with Guaranteed Overflow Avoidance

- Citation key: `colbert2023a2q`.
- Authors: Colbert, Ian; Pappalardo, Alessandro; Petri-Koenig, Jakoba.
- Publication: ICCV, 2023.
- Source: [paper](https://arxiv.org/abs/2308.13504v1); [full text reviewed](https://arxiv.org/pdf/2308.13504v1).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Accumulator bounds, weight-norm constraints, and deployment.
- Evidence: Quantization-aware training and FPGA/resource evaluation.

## What it establishes

Constrains quantized weight norms during training to avoid accumulator overflow under specified activation bounds.

## Relevance to our goals

A principled overflow baseline and a warning that narrow accumulation can require model changes.

## Limits and transfer conditions

It is weight/training based, not autonomous activation adaptation. Overflow avoidance is not equivalent to preserving floating-point model outputs.
