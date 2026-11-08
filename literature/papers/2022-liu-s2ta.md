# S2TA: Exploiting Structured Sparsity for Energy-Efficient Mobile CNN Acceleration

- Citation key: `liu2022s2ta`.
- Authors: Liu, Zhi-Gang; Whatmough, Paul N.; Zhu, Yuhao; Mattina, Matthew.
- Publication: IEEE International Symposium on High-Performance Computer Architecture (HPCA), 2022.
- Source: [paper](https://arxiv.org/abs/2107.07983v2); [full text reviewed](https://arxiv.org/pdf/2107.07983v2).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Figure 1; Sections 2, 7, and 8; gating versus skipping.
- Evidence: RTL/physical-design-based accelerator estimates and model-quality evaluation.

## What it establishes

Its conventional INT8 systolic baseline attributes about 20% of energy to the MAC datapath; operand/result buffers dominate. Structured sparsity also targets buffering and execution overhead.

## Relevance to our goals

A direct warning against treating reduced MAC work as proportional accelerator energy savings. Clock-gating zeros and shortening execution must be accounted for separately.

## Limits and transfer conditions

The fraction concerns that baseline and sparsity conditions, not a universal array or whole-system split. Lossy activation pruning requires fine-tuning in the evaluated setup.
