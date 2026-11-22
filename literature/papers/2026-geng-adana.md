# Adana: Accelerating Large Language Models via Adaptive Nonuniform Asymmetric Quantization

- Citation key: `geng2026adana`.
- Authors: Xinkuang Geng; Siting Liu; Hui Wang; Leibo Liu; Jie Han; Honglan Jiang.
- Publication: DAC 2026 conference program; author-hosted presentation.
- Source: [official program](https://63dac.conference-program.com/presentation/?id=RESEARCH2184&sess=sess140); [author slides](https://www.ece.ualberta.ca/~jhan8/publications/dac26-adana.pdf).
- Reviewed: 2026-11-22. Status: **official abstract and presentation focused reading**; paper full text not reviewed.
- Reading focus: numeric grids, approximate online error metric and quantization engine.

## What it establishes

Describes an adaptive numeric representation, an approximate activation-error
metric and a dedicated quantization/matrix-engine architecture.

## Relevance to our goals

Direct comparator for reducing online selection cost through algorithm and
hardware co-design, even when the broad quantization objective is established.

## Limits and transfer conditions

Slides and abstract do not establish a particular RTL, FPGA or silicon maturity.
Do not infer calibration independence or unexamined implementation details.
