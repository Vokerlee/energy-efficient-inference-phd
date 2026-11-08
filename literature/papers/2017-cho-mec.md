# MEC: Memory-efficient Convolution for Deep Neural Network

- Citation key: `cho2017mec`.
- Authors: Cho, Minsik; Brand, Daniel.
- Publication: ICML, 2017.
- Source: [paper](https://proceedings.mlr.press/v70/cho17a.html); [full text reviewed](https://proceedings.mlr.press/v70/cho17a/cho17a.pdf).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Compact lowering, small GEMM decomposition, and platform evaluation.
- Evidence: Convolution algorithm and software performance/memory evaluation.

## What it establishes

Reduces the size of the lowered representation and completes convolution using multiple smaller matrix multiplications.

## Relevance to our goals

A baseline for trading expansion traffic against matrix size and reuse in a fixed-size execution model.

## Limits and transfer conditions

Lower memory footprint does not guarantee lower energy or higher systolic utilization. The tested software platforms and exact shapes constrain its speedups.
