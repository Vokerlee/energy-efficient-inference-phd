# CompAct: On-chip Compression of Activations for Low Power Systolic Array Based CNN Acceleration

- Citation key: `zhang2019compact`.
- Authors: Jeff (Jun) Zhang; Parul Raj; Shuayb Zarar; Amol Ambardekar; Siddharth Garg.
- Publication: 2019.
- Source: [paper](https://doi.org/10.1145/3358178); [reviewed text](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/04/Compact_ESWEEK2019_Final.pdf).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Reading focus: Sections 3.1–3.4: row-major scheduling, RLC/Sparse-RLC/Lossy-RLC and buffer snoozing.

## What it establishes

Co-designs convolution scheduling with compressed on-chip activation storage and buffer sleep control. Its decoder reconstructs the original dense stream before the array; compression alone does not skip issued MACs.

## Relevance to our goals

Prior work already combines activation representation, convolution scheduling and local-memory energy.

## Limits and transfer conditions

Lossy coding and mode selection need their stated preparation and quality checks. Synthesized/model-based savings on older CNNs are not measured savings in another memory system. This source separates compressed SRAM accesses from unchanged array slots.
