# Flexpoint: An Adaptive Numerical Format for Efficient Training of Deep Neural Networks

- Citation key: `koster2017flexpoint`.
- Authors: Koster, Urs; others.
- Publication: NeurIPS, 2017.
- Source: [paper](https://arxiv.org/abs/1711.02213v2); [full text reviewed](https://arxiv.org/pdf/1711.02213v2).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Autoflex initialization, bounded history, and exponent prediction.
- Evidence: Numerical-format algorithm with simulated training experiments.

## What it establishes

Autoflex predicts shared exponents from a bounded history of observed maxima and includes initialization/recovery behavior.

## Relevance to our goals

Historical evidence that range prediction and headroom management already exist.

## Limits and transfer conditions

Training tensors evolve differently from inference streams. Its numerical results do not validate our causal inference policy or physical controller cost.
