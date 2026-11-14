# TPU architecture and generation-specific memory hierarchy

- Citation key: `google2026tpuarchitecture`.
- Author: Google Cloud; JAX authors for the hardware reference.
- Publication: Official technical documentation; living pages accessed 2026-11-14.
- Sources: [TPU architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm), [TPU7x](https://docs.cloud.google.com/tpu/docs/tpu7x), [JAX hardware reference](https://docs.jax.dev/en/latest/pallas/tpu/hardware.html).
- Reviewed: 2026-11-14. Status: **documentation focused reading**.
- Reading focus: TensorCore components, generation differences, memory hierarchy, and specification units.
- Evidence: Vendor and framework documentation; not independent energy measurements.

## What it establishes

TensorCores combine matrix, vector, and scalar units. The architecture page
distinguishes 128x128 and newer 256x256 MXUs; vector units perform operations
including activations and softmax. TPU7x documentation distinguishes HBM,
on-chip VMEM, and host memory. JAX labels its specifications per TensorCore.

## Relevance

Supports generation-specific comparisons of operand delivery and intermediate
storage instead of treating every TPU as one fixed matrix/memory design.

## Limits

Chip totals differ from per-TensorCore figures; physical HBM differs from
allocatable memory. The pages are not immutable snapshots. The architecture
page's stated 256x256 MAC count needs reconciliation before numerical reuse;
do not derive throughput from that count here. Supported formats also need
generation-specific confirmation when documentation tables differ.
