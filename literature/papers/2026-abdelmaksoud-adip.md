# ADiP: Adaptive-Precision Systolic Array for Matrix Multiplication Acceleration

- Citation key: `abdelmaksoud2026adip`.
- Authors: Abdelmaksoud, Ahmed J.; Sestito, Cristian; Wang, Shiwei; Prodromakis, Themis.
- Publication: arXiv preprint, 2026.
- Source: [paper](https://arxiv.org/abs/2510.10623v3); [full text reviewed](https://arxiv.org/pdf/2510.10623v3).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Reconfigurable PEs, precision modes, sharing, and evaluation.
- Evidence: 22 nm design exploration and transformer-workload estimates.

## What it establishes

Supports multiple operand-width modes with shared shifters/accumulators and reuse across matrix operations.

## Relevance to our goals

A close precision-scalable systolic datapath comparator for the eventual hardware implementation.

## Limits and transfer conditions

Precision-scalable execution alone does not establish autonomous live-activation range selection. Our review does not verify a complete statistics-to-policy controller here. Workload cost improvements are implementation estimates, not our full-model results.
