# Roofline: An Insightful Visual Performance Model for Multicore Architectures

- Citation key: `williams2009roofline`.
- Authors: Williams, Samuel; Waterman, Andrew; Patterson, David.
- Publication: Communications of the ACM, 2009.
- Source: [paper](https://doi.org/10.1145/1498765.1498785); [full text reviewed](https://aiichironakano.github.io/cs596/Williams-Roofline-CACM09.pdf).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Operational intensity, ceilings, and bottleneck interpretation.
- Evidence: Analytical performance model; multicore measurements.

## What it establishes

Relates attainable arithmetic throughput to compute capability and sustainable memory bandwidth. Its operational intensity counts bytes crossing a specified memory boundary, rather than tensor size alone.

## Relevance to our goals

Provides the starting test for selecting compute-bound inference configurations and identifying bottleneck changes after optimization.

## Limits and transfer conditions

A throughput ceiling does not identify energy contributors. Hardware utilization and additional execution limits still require measurement; the original CPU examples do not calibrate a modern accelerator.
