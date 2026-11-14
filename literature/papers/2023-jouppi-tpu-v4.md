# TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings

- Citation key: `jouppi2023tpuv4`.
- Authors: Jouppi, Norman P.; others.
- Publication: ISCA, 2023.
- Source: [paper](https://arxiv.org/abs/2304.01433v1); [full text](https://arxiv.org/pdf/2304.01433v1).
- Reviewed: 2026-11-14. Status: **full-text focused reading**.
- Reading focus: Section 3, Table 4, Figure 13, and Section 7.5: compute units, memory, and CMEM comparisons.
- Evidence: Production-system architecture and workload measurements.

## What it establishes

Each of two TensorCores has four 128x128 MXUs, a VPU, and 16 MiB VMEM;
the chip also has shared 128 MiB CMEM. The paper compares operation with
and without CMEM, showing workload-dependent effects beyond peak MAC rate.

## Relevance

Distinguishes local working memory, shared on-chip storage, and HBM when
analyzing operand reuse and matrix/vector execution.

## Limits

TPU v4 is a historical generation and this paper primarily evaluates training.
Its optical switching connects chips; matrix arithmetic remains electronic.
Do not transfer its measured gains to another generation or inference workload.
