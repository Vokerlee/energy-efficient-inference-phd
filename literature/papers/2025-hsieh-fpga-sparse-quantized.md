# FPGA Co-Design for Efficient N:M Sparse and Quantized Model Inference

- Citation key: `hsieh2025fpgasparsequantized`.
- Authors: Fen-Yu Hsieh; Yun-Chang Teng; Ding-Yong Hong; Jan-Jan Wu.
- Publication: arXiv author version, 2025.
- Source: [full text](https://arxiv.org/html/2512.24713v1).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: 3.2–3.4 and 4.1–4.2.

## What it establishes

Pruning, INT4 weight quantization and packing are prepared offline. Host-side
dequantization feeds floating-point values to a systolic FPGA design whose
PEs suppress accumulation for zero weights. Benchmarks include random inputs.

## Relevance to our goals

A hardware implementation can execute a prepared sparse representation
without implementing a live activation-selection policy or integer arithmetic.

## Limits and transfer conditions

Storage bits, MAC arithmetic and runtime decision placement are separate
properties. This evidence does not establish autonomous activation pruning,
end-to-end trained-model quality or native INT4 computation in the array.
