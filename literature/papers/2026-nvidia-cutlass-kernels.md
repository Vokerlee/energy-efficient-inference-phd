# CUTLASS C++ kernels and implicit convolution lowering

- Citation key: `nvidia2026cutlasskernels`.
- Author: NVIDIA.
- Publication: CUTLASS documentation and release v4.8.0.
- Source: [overview](https://docs.nvidia.com/cutlass/4.8.0/overview.html), [functionality](https://docs.nvidia.com/cutlass/4.8.0/media/docs/cpp/functionality.html), [GEMM API](https://docs.nvidia.com/cutlass/4.8.0/media/docs/cpp/gemm_api.html), [convolution](https://docs.nvidia.com/cutlass/4.8.0/media/docs/cpp/implicit_gemm_convolution.html), [release source](https://github.com/NVIDIA/cutlass/tree/v4.8.0).
- Reviewed: 2026-11-15. Status: **documentation focused reading**.
- Reading focus: Compatibility, C++ kernel support tables, implicit-GEMM algorithm, operand iterators, and the GEMM model/device-wide API sections.
- Verified tag commit: `098de2a652cf8f00fd70b2df54051c7eccbb855a`.

## Findings and relevance

C++ templates expose kernel building blocks and architecture-specific MMA.
Implicit convolution constructs operand tiles while loading data, avoiding a
complete expanded matrix. This supports numerical experimentation at operand
loading and matrix-reduction boundaries.

The GEMM API distinguishes grid, threadblock, warp and instruction scopes.
Its device operator accepts operand pointers and leading dimensions; template
choices expose input/output types, accumulator type and target instruction
class. Separate APIs cover batched products and parallel split-K. This gives
an explicit baseline execution contract; choosing a tile still requires
measurement on the intended shapes and layouts.

## Limits

Formats, layouts, alignment and kernel families have specific support limits.
GPU tiles and arithmetic are not an ASIC systolic-array model. Library support
does not establish performance for a particular customized kernel; no kernel
was compiled or benchmarked in this documentation review.
