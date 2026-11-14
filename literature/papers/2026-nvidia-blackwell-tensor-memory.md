# Blackwell SM100 tensor-memory epilogue

- Citation key: `nvidia2026blackwelltmem`.
- Author: NVIDIA.
- Publication: CUTLASS documentation, version 4.8.0.
- Source: [Blackwell SM100 utilities](https://docs.nvidia.com/cutlass/4.8.0/media/docs/pythonDSL/cute_dsl_api/utils_sm100.html).
- Reviewed: 2026-11-14. Status: **documentation focused reading**.
- Reading focus: `compute_epilogue_tile_shape`, TMEM-to-register flow, and shared-memory budget.
- Evidence: Vendor implementation documentation and resource constraints.

## What it establishes

The described epilogue loads accumulator subtiles from TMEM into registers,
performs fused operations such as bias and activation, and stages output stores.
Epilogue staging shares the SMEM budget with operand pipeline buffers; larger
epilogue subtiles can reduce available mainloop pipeline depth.

## Relevance

Shows why result conversion and vector work must be considered with matrix
execution. TMEM storage and TMA data transport are different mechanisms.

## Limits

These details concern SM100 and a particular CUTLASS implementation, not every
GPU or Blackwell variant. Tile heuristics are not universal optimal choices.
No kernels, performance measurements, or energy experiments were run here.
