# Error Analysis and Improving the Accuracy of Winograd Convolution for Deep Neural Networks

- Citation key: `barabasz2019winograd`.
- Authors: Barabasz, Barbara; Anderson, Andrew; Soodhalter, Kirk M.; Gregg, David.
- Publication: arXiv preprint, 2019.
- Source: [paper](https://arxiv.org/abs/1803.10986v3); [full text reviewed](https://arxiv.org/pdf/1803.10986v3).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Conditioning, transform size, summation, and mixed precision.
- Evidence: Numerical analysis and convolution experiments.

## What it establishes

Analyzes Winograd rounding error and methods for reducing it, including evaluation order and mixed precision.

## Relevance to our goals

A baseline for testing whether fewer multiplications require more precision elsewhere.

## Limits and transfer conditions

Local numerical bounds are not a full-network quality guarantee and do not provide a hardware energy comparison.
