# TFApprox: Towards a Fast Emulation of DNN Approximate Hardware Accelerators on GPU

- Citation key: `vaverka2020tfapprox`.
- Authors: Filip Vaverka and Vojtech Mrazek and Zdenek Vasicek and Lukas Sekanina.
- Publication/version: 2020; pinned primary source below.
- Source: [primary source](https://arxiv.org/abs/2002.09481v1).
- Reviewed: 2026-11-24. Status: **Primary abstract and version metadata; full-method review pending.**

## Findings and relevance

Emulates approximate arithmetic circuits through CUDA texture-memory look-up tables in a TensorFlow extension. Fast GPU emulation of nonstandard arithmetic is established prior art. Its reported acceleration is relative to an optimized CPU emulator, not a prediction for a GPU-versus-GPU comparison.

## Limits

A selective finite-reference implementation must compare with complete GPU emulation, including preparation and selection costs. The abstract does not establish a BF16 observation-boundary guard or demonstrate absence of such a feature from every implementation.
