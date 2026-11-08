# Fast Algorithms for Convolutional Neural Networks

- Citation key: `lavin2016fastconv`.
- Authors: Lavin, Andrew; Gray, Scott.
- Publication: CVPR, 2016.
- Source: [paper](https://arxiv.org/abs/1509.09308v2); [full text reviewed](https://arxiv.org/pdf/1509.09308v2).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Winograd transforms, operation costs, and GPU evaluation.
- Evidence: Convolution algorithm and implementation benchmarks.

## What it establishes

Uses small-tile Winograd filtering to reduce multiplication counts while introducing input/filter/output transforms.

## Relevance to our goals

An alternative convolution baseline when comparing lowering and matrix computation.

## Limits and transfer conditions

Transform cost, shape restrictions, and numerical behavior must be included. Historical GPU speedups do not determine current hardware energy.
