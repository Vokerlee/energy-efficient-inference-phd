# NVDLA v1 convolution pipeline and Winograd mode

- Citation key: `nvidia2026nvdla`.
- Author: NVIDIA.
- Source: [official unit description](https://nvdla.org/hw/v1/ias/unit_description).
- Reviewed: 2026-11-24. Status: **primary documentation, focused reading** of Convolution Pipeline, Direct Convolution and Winograd Convolution; release scope `nvdlav1`.

## Contribution and relevance

Documents a convolution pipeline with shared activation/weight buffering,
precision-dependent MAC resources, a separate accumulator and optional
Winograd transforms. Atomic work dimensions depend on precision; they are not
an arbitrary giant matrix multiplication.

## Comparison boundary

Useful implemented architectural baseline for accounting across DMA, feeder,
MAC and accumulator boundaries. Optional features and resource sizes vary by
release/configuration. Do not transfer its integer dimensions, memory sizes or
throughput to another accelerator. This documentation establishes design
behavior, not an energy measurement of our proposed configuration.
