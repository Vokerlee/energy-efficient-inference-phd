# Any-Precision Deep Neural Networks

- Citation key: `yu2021anyprecision`.
- Authors: Yu, Haichao; Li, Haoxiang; Shi, Humphrey; Huang, Thomas S.; Hua, Gang.
- Publication: AAAI, 2021.
- Source: [paper](https://arxiv.org/abs/1911.07346); [full text reviewed](https://arxiv.org/pdf/1911.07346).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Training for selectable precision and inference-mode behavior.
- Evidence: Model training and multi-precision evaluation.

## What it establishes

Trains one network to support different inference precision settings rather than requiring a separate checkpoint for each setting.

## Relevance to our goals

A comparator when considering retraining to make runtime modes more robust.

## Limits and transfer conditions

Selectable modes do not define an autonomous hardware selector. Training changes place it outside the primary unchanged-checkpoint activation experiment.
