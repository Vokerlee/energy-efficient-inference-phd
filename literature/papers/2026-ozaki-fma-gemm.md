# Fast and accurate algorithms for matrix multiplication using fused multiply-add and their rounding error analysis

- Citation key: `ozaki2026fma`.
- Authors: Katsuhisa Ozaki and Toru Koizumi.
- Publication/version: 2026; pinned primary source below.
- Source: [primary source](https://doi.org/10.1007/s13160-026-00816-8).
- Reviewed: 2026-11-24. Status: **Primary full text, focused Introduction and Section 3.1–3.2; full implementation/benchmark review pending.**

## Findings and relevance

Develops compensated FMA techniques and matrix algorithms. Some local error results require a magnitude condition such as the accumulator dominating twice the product; counterexamples show why this condition matters. Accurate GEMM and compensation are established comparison families.

## Limits

The aim is improved approximation to real arithmetic, not reproduction of a chosen low-accuracy finite accumulation graph. Our boundary-check specialization must still establish useful performance and a distinct contribution; merely implementing compensation or a bound is insufficient.
