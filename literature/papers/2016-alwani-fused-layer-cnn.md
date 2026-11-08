# Fused-Layer CNN Accelerators

- Citation key: `alwani2016fused`.
- Authors: Alwani, Manoj; Chen, Han; Ferdman, Michael; Milder, Peter.
- Publication: MICRO, 2016.
- Source: [paper](https://doi.org/10.1109/MICRO.2016.7783725); [full text reviewed](https://compas.cs.stonybrook.edu/~mferdman/downloads.php/MICRO16_Fused_Layer_CNN_Accelerators.pdf).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Inter-layer reuse, storage model, and FPGA prototype.
- Evidence: Analytical design-space exploration and FPGA demonstration.

## What it establishes

Fuses consecutive convolution layers to retain intermediate data on chip rather than repeatedly transferring feature maps.

## Relevance to our goals

A hardware baseline for measuring avoided intermediate movement.

## Limits and transfer conditions

Fusion depth, halos, buffering, and parallelism constrain benefits. Results for selected VGG layers do not generalize to every operator graph.
