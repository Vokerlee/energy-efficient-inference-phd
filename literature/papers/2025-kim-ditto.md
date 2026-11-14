# Ditto: Accelerating Diffusion Model via Temporal Value Similarity

- Citation key: `kim2025ditto`.
- Authors: Kim, Sungbin; Lee, Hyunwuk; Cho, Wonho; Park, Mincheol; Ro, Won Woo.
- Publication: HPCA, 2025.
- Source: [paper](https://arxiv.org/abs/2501.11211v1); [full text reviewed](https://arxiv.org/pdf/2501.11211v1).
- Reviewed: 2026-11-14. Status: **full-text focused reading**.
- Reading focus: Sections IV–V: temporal differences, Defo, encoder classification, and compute datapath.
- Evidence: Algorithm, full-model quality checks, and modeled accelerator evaluation.

## What it establishes

Processes temporal activation differences with zero/low/full-width classification. Encoder reordering and mixed-width adder-tree PEs exploit both sparsity and precision; Defo selects execution flow.

## Relevance to our goals

Direct hardware prior art for a shared observation point choosing reduced-width work and skipping.

## Limits and transfer conditions

Past-state storage and reconstruction remain costs. Its datapath and conditional integer equivalence do not establish equivalence of arbitrary floating-point nonlinear networks or benefits on our array.
