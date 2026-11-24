# Providing Accuracy Guarantees for the Fixed-Point Emulation of Matrix Multiplication

- Citation key: `brower2026emulationguarantees`.
- Authors: Cole Brower and Peter Caday and John Gunnels.
- Publication/version: 2026; pinned primary source below.
- Source: [primary source](https://arxiv.org/abs/2611.19008v1).
- Reviewed: 2026-11-24. Status: **Primary full text, focused Introduction, Sections 2.4 and 4.1, including binned exponent-span calculation; proofs not independently checked.**

## Findings and relevance

Selects fixed-point mantissa counts for Ozaki-II while preserving stated floating-point GEMM error guarantees. Binned exponent-span estimates use low-precision BF16 products and bound their overprediction. Operand-dependent accuracy selection and inexpensive matrix-assisted bounds are therefore existing methods.

## Limits

Matching a classical error bound relative to a real dot product differs from returning the same BF16 observation as one specified finite-precision accumulation order. This difference in specification alone does not establish a new method. The reported developer cuBLAS/B200 experiments were not reproduced here.
