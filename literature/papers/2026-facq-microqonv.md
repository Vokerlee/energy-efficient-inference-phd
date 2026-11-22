# MicroQonv: Reshaping Convolution Tensors for Efficient Microscaling in Training and Inference

- Citation key: `facq2026microqonv`.
- Authors: Romain Facq; Sami Ben Ali; Olivier Sentieys.
- Publication: 2026.
- Source: [paper](https://arxiv.org/abs/2609.28358v1); [reviewed text](https://arxiv.org/html/2609.28358v1).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Reading focus: Sections II-C, III, IV and V–VIII: quantization directions, square blocks, data movement and evidence scope.

## What it establishes

Quantizes source activations before a channel-batch-first im2col layout. Uses square microscaling blocks, including 8 by 8 blocks in its experiments, to reuse representations across convolution training products. Evaluates accuracy and simulated DRAM movement.

## Relevance to our goals

A direct baseline for combining quantization with convolution lowering; quantize-once-before-expansion is already established.

## Limits and transfer conditions

A hardware-agnostic layout method, not a fabricated feeder. Its conclusion leaves a dedicated accelerator as future work. That does not erase its algorithmic contribution. Per-tensor maxima and group-scale application have implementation costs. Training/transposition benefits and DRAM estimates do not establish live tile selection, short-vector utilization, or energy savings in an on-chip-resident inference design.
