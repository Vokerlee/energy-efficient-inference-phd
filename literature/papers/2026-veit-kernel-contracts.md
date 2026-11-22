# Kernel Contracts: A Specification Language for ML Kernel Correctness Across Heterogeneous Silicon

- Citation key: `veit2026kernelcontracts`.
- Authors: Cooper Veit.
- Publication: 2026; author version `2604.22032v1`.
- Source: [paper](https://arxiv.org/abs/2604.22032v1); [full text](https://arxiv.org/html/2604.22032v1).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Reading focus: Sections 3, 5.7 and 8.2–8.3: declared oracles/tolerances, verification overhead and composition limits.

## What it establishes

Proposes explicit kernel contracts covering reference semantics, numerical tolerances, measurement protocols and failure signatures. Includes a measured Freivalds-style checking primitive.

## Relevance to our goals

Methodological comparator for separating an intended arithmetic change from an implementation failure in numerical experiments.

## Limits and transfer conditions

A preprint proposal, not an adopted standard or independently validated certification. Operator checks do not establish whole-model quality; contract composition is left open. A randomized checker is not automatically an unbiased observer after it influences precision choices, and its floating-point sensitivity/overhead require separate validation.
