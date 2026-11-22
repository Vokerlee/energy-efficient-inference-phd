# Characterizing and Demystifying the Implicit Convolution Algorithm on Commercial Matrix-Multiplication Accelerators

- Citation key: `zhou2021implicitconv`.
- Authors: Yangjie Zhou; Mengtian Yang; Cong Guo; Jingwen Leng; Yun Liang; Quan Chen; Minyi Guo; Yuhao Zhu.
- Publication: 2021.
- Source: [paper](https://arxiv.org/abs/2110.03901v1); [reviewed text](https://arxiv.org/html/2110.03901v1).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Reading focus: Implicit lowering, channel-first layout, mapping/tiling and TPU/Tensor Core evaluation.

## What it establishes

Describes a channel-first implicit lowering algorithm and its mapping to GEMM accelerators. Evaluates convolution variants and argues, through measurements, that related behavior is present in commercial implementations.

## Relevance to our goals

A strong implicit-lowering baseline; small spatial kernels do not inherently require issuing one short input-channel window at a time.

## Limits and transfer conditions

The commercial-algorithm attribution is an inference, not access to proprietary RTL. Low overhead in the evaluated systems is not zero-cost addressing, universal utilization, or a target-chip energy measurement. Its rearranged accumulation order also needs a declared numerical reference.
