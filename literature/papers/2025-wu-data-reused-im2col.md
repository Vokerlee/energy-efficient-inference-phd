# An energy-efficient data-reused on-the-fly Im2col for OS-dataflow systolic array-based accelerator

- Citation key: `wu2025reusedim2col`.
- Authors: Jianghui Wu; Jianpeng Fan; Xueying Wang; Jun Chen; Weixing Li.
- Publication: 2025.
- Source: [paper](https://doi.org/10.1016/j.mejo.2025.106831).
- Reviewed: 2026-11-23. Status: **publisher abstract and section snippets; full-text review pending**.
- Reading focus: Reuse hierarchy, irregular OS dataflow, 16 by 16 INT8 example and stride limitations; metadata checked through Crossref.

## What it establishes

Describes an on-the-fly feeder with two reuse schemes and an output-stationary consumer supporting irregular streams. Separates overall, SRAM-level and dataflow-level reuse.

## Relevance to our goals

A close hardware comparator for reducing feeder buffers and aligning repeated data in time.

## Limits and transfer conditions

Accessible text limits the illustrated accelerator to 3 by 3 and 1 by 1 convolutions; its conclusion warns about the cost of non-unit strides. Full RTL/control details and matched energy accounting remain unreviewed. Do not generalize to all convolution shapes.
