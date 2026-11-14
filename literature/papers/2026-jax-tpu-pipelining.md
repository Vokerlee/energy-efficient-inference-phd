# TPU Pipelining

- Citation key: `jax2026tpupipelining`.
- Author: JAX authors.
- Publication: Official JAX technical documentation; living page accessed 2026-11-14.
- Source: [documentation](https://docs.jax.dev/en/latest/pallas/tpu/pipelining.html).
- Reviewed: 2026-11-14. Status: **documentation focused reading**.
- Reading focus: Memory spaces, copy semaphores, multiple buffering, and persistent scratch buffers.
- Evidence: Framework programming model and documented execution constraints.

## What it establishes

Pallas exposes HBM/VMEM transfers, vector and scalar SRAM, synchronization,
and persistent scratch storage. Multiple buffering consumes storage for each
pipeline argument; its documented default is two buffers for inputs and outputs.

## Relevance

An extra statistics pass or converted tensor competes with pipeline buffers
and partial results. Overlapping DMA and computation needs explicit storage
and completion dependencies, not just sufficient total memory capacity.

## Limits

This is a software interface, not proof of a hardware-autonomous quantizer.
API defaults and accessible resources can change with framework versions.
No example kernel or inference experiment was executed for this reading.
