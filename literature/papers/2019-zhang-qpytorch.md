# QPyTorch: A Low-Precision Arithmetic Simulation Framework

- Citation key: `zhang2019qpytorch`.
- Authors: Tianyi Zhang; Zhiqiu Lin; Guandao Yang; Christopher De Sa.
- Publication/version: 2019; version/source pinned below.
- Source: [primary source](https://arxiv.org/html/1910.04540v1).
- Reviewed: 2026-11-24. Status: **Full-text focused reading: Sections3–3.2.**

## Findings, relevance and limits

Supports flexible formats/rounding and efficient GPU emulation. Section3 explicitly uses high-precision accumulation for composite matrix products; layer-level quantize/dequantize is not per-primitive hardware arithmetic. A general low-precision engine and its convenient API are existing contributions. Compare accumulator boundaries and exceptional-value semantics before transferring conclusions. No result was reproduced here.
