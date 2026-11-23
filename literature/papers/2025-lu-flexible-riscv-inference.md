# Efficient Flexible Edge Inference for Mixed-Precision Quantized DNN using Customized RISC-V Core

- Citation key: `lu2025flexibleriscv`.
- Authors: Tianshuo Lu; Jiangyang Ding; Huachen Zhang; Bowen Jiang; Wei Xu; Zhilei Chai.
- Publication: ACM Transactions on Architecture and Code Optimization; published 2025-12-16; DOI `10.1145/3768630`.
- Source: [publisher](https://doi.org/10.1145/3768630); [metadata](https://api.crossref.org/works/10.1145/3768630).
- Reviewed: 2026-11-23. Status: **publisher-indexed section excerpts; direct full text unavailable**.
- Reading focus: indexed Sections 2–5: adaptive packing, local im2col, configurable execution and evaluation workflow. Author/date metadata checked against Crossref.

## What it establishes

Combines mixed-precision inference, lane packing, local convolution lowering,
custom RISC-V instructions and configurable multiplication hardware. The
described workflow prepares quantized ONNX models and generates model-specific
code; software performs coarse lowering/packing while hardware handles fine
arithmetic. FPGA evaluation and ASIC synthesis are described.

## Relevance to our goals

Direct comparator for ISA-guided packing and convolution/matmul co-design.
Neither configurable hardware nor a combination of lowering and low precision
is sufficient by itself as a novelty claim.

## Limits and transfer conditions

Dynamic configuration should be distinguished from selecting precision using
each live activation block. Reviewed excerpts do not establish source-group
statistics reuse with pre-issue bounded accumulation. Missing complete text
leaves that comparison unresolved; it does not prove absence of the mechanism.
