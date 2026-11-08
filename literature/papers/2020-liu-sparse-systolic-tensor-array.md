# Sparse Systolic Tensor Array for Efficient CNN Hardware Acceleration

- Citation key: `liu2020ssta`.
- Authors: Liu, Zhi-Gang; Whatmough, Paul N.; Mattina, Matthew.
- Publication: arXiv preprint, 2020.
- Source: [paper](https://arxiv.org/abs/2009.02381v2); [full text reviewed](https://arxiv.org/pdf/2009.02381v2).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Late hardware IM2COL, activation reuse, and design-space evaluation.
- Evidence: INT8 accelerator implementation estimates and architectural exploration.

## What it establishes

Places IM2COL after local SRAM near the datapath, reusing buffered activations to expand delivery bandwidth. Integrates tensor processing elements with variable density-bound sparsity.

## Relevance to our goals

Direct prior art for jointly designing window generation, operand reuse, and sparse systolic execution.

## Limits and transfer conditions

Its reported bandwidth multiplier concerns particular convolution/dataflow conditions. It does not establish universal benefits for dilation, every window size, or dynamic precision.
