# LMAI2C: Low memory access Im2col method for CNN inference

- Citation key: `li2025lmai2c`.
- Authors: Mengda Li; Ziyi Chen; Jiangen Hong; Yiheng Zhang; Xiaoran Hao; Ming Chen; Mao Ni.
- Publication: 2025.
- Source: [paper](https://doi.org/10.1587/elex.22.20250246); [reviewed text](https://globals.ieice.org/en_publications/elex/10.1587/elex.22.20250246/_f).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Reading focus: Sections 3–4: aligned padded storage, stride-adaptive register reuse and separate DDR/BRAM accounting.

## What it establishes

Implements row-aligned input storage and shift-register reuse on an FPGA. Its evaluated YOLOv4-tiny feeder moves expansion on chip and reduces repeated external reads while increasing BRAM activity.

## Relevance to our goals

A concrete reference for combining feeder reuse with alignment/padding and local-memory costs.

## Limits and transfer conditions

The implementation uses 16-bit fixed-point inputs, not a new online quantization controller. DDR savings and an access-energy model do not establish savings for tensors already in on-chip SRAM. The abstract and conclusion give inconsistent CPU+DMA speedup figures, so this review adopts neither.
