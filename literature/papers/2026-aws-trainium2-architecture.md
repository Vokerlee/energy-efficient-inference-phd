# Trainium2 Architecture Guide for NKI

- Citation key: `aws2026trainium2architecture`.
- Author: Amazon Web Services.
- Publication: AWS Neuron documentation, version 2.32.0.
- Source: [architecture guide](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/nki/guides/architecture/trainium2_arch.html).
- Reviewed: 2026-11-14. Status: **documentation focused reading**.
- Reading focus: Tensor Engine, double-FP8 layout, data movement, and engine memory-access conflicts.
- Evidence: Vendor architecture and ISA documentation.

## What it establishes

NeuronCore-v3 has 28 MiB SBUF and 2 MiB PSUM. DMA connects HBM and SBUF;
compute-engine instructions move results between PSUM and SBUF. Double-FP8
increases the logical contraction dimension to 256 on a physical 128x128
array through paired products. Layout and bank-conflict rules still apply.

## Relevance

A concrete comparator for distinct operand and accumulation storage, and for
precision-dependent instruction shapes that differ from physical array shape.

## Limits

NeuronCore-v3 details do not specify every Trainium generation. Buffer capacity
alone does not determine usable tile size, and documented peak rates are not
end-to-end speed or energy measurements.
