# Fast Matrix Multiplication in fp8: Certified Coefficient Optimization and Measured Error

- Citation key: `xie2026fp8fastmatmul`.
- Authors: Xie, Shuxiao; Xie, Shuyang; Cao, Yuan; Ran, Dezhi; Yang, Wei; Xie, Tao.
- Publication: arXiv preprint, pinned version 1.
- Source: [primary source](https://arxiv.org/abs/2609.26077v1).
- Reviewed: 2026-11-22. Status: **Primary abstract and metadata only; full-text proof/experiment audit pending.**

## What it establishes

Studies exact rank-7 multiplication realizations with different FP8 errors. The abstract proposes coefficient optimization under an explicit stochastic block-scaled model and reports kernel/model evaluations.

## Relevance to our goals

Coefficient choice and low-precision fast multiplication are an existing research intersection.

## Limits and transfer conditions

The claimed optimum concerns a specified coefficient functional, not universal network quality or energy. Proof assumptions, kernel arithmetic and reported results were not independently checked. Do not infer runtime algorithm selection from the title.
