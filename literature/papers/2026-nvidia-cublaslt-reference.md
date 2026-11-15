# cuBLASLt as a CUDA matrix-kernel comparison baseline

- Citation key: `nvidia2026cublaslt`.
- Author: NVIDIA.
- Publication: cuBLAS documentation archived with CUDA 12.8.1.
- Source: [official reference](https://docs.nvidia.com/cuda/archive/12.8.1/cublas/index.html).
- Reviewed: 2026-11-15. Status: **documentation focused reading**.
- Reading focus: Introduction and cuBLASLt descriptions, layouts, compute types, algorithms and heuristics.

## Findings and relevance

cuBLASLt exposes matrix-layout and compute-type choices plus algorithm
selection for GPU GEMM. It is a useful independent numerical/performance
comparator for custom kernels under matched settings.

## Limits

An opaque library call does not expose arbitrary operand-observation or
reduction-boundary changes. Compare workspaces, conversions and precision
settings fairly; algorithm and architecture choices affect results. Using this
library alone does not implement a configurable systolic-array research path.
No cuBLASLt benchmark was run in this review.
