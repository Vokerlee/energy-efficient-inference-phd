# Discovering Faster Matrix Multiplication Algorithms with Reinforcement Learning

- Citation key: `fawzi2022alphatensor`.
- Authors: Fawzi, Alhussein; others.
- Publication: Nature, 2022.
- Source: [paper](https://www.nature.com/articles/s41586-022-05172-4); [full text reviewed](https://www.nature.com/articles/s41586-022-05172-4.pdf).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Arithmetic domains, decomposition, and hardware-specific evaluation.
- Evidence: Algorithm discovery and GPU/TPU benchmarking.

## What it establishes

Discovers multiplication schemes and explores hardware runtime objectives as well as multiplication count.

## Relevance to our goals

Supports evaluating concrete schemes and schedules for target hardware.

## Limits and transfer conditions

Finite-field results are not interchangeable with real-valued neural arithmetic. Hardware-specific GEMM speedups do not establish full-model accuracy or energy.
