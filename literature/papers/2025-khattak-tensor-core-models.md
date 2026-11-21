# Accurate Models of NVIDIA Tensor Cores

- Citation key: `khattak2025tensorcoremodels`.
- Authors: Khattak, Faizan A.; Mikaitis, Mantas.
- Publication: arXiv preprint, 2025, version 1.
- Source: [arXiv v1](https://arxiv.org/abs/2512.07004v1).
- Reviewed: 2026-11-21. Status: **abstract and bibliographic verification only**.
- Evidence: Authors describe software models of low/mixed-precision inner products.

## Scope and relevance

The abstract identifies rounding, accumulator width and normalization points
as properties that hardware-sensitive test vectors must distinguish.
It describes models for several NVIDIA matrix-unit generations and formats.
This is a reference for numerical hardware modeling, rather than a generic
assumption that all matrix instructions follow the same arithmetic.

## Limits

Model implementation, validation results and format-specific coverage have not
been examined here. No claim about arbitrary FP32 library GEMMs or whole-network
accuracy follows from this abstract check. The record is pinned to v1 rather
than silently incorporating later revisions.
