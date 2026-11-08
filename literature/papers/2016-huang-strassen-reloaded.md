# Strassen's Algorithm Reloaded

- Citation key: `huang2016strassen`.
- Authors: Huang, Jianyu; Smith, Tyler M.; Henry, Greg M.; van de Geijn, Robert A..
- Publication: SC, 2016.
- Source: [paper](https://jianyuhuang.com/papers/sc16.pdf).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Packing, fusion, workspace, and finite-size implementation.
- Evidence: CPU DGEMM implementation and performance evaluation.

## What it establishes

Integrates Strassen operations into high-performance packing/microkernel machinery to reduce temporary-workspace and traffic overhead.

## Relevance to our goals

A systems implementation baseline for testing arithmetic savings honestly.

## Limits and transfer conditions

CPU double-precision results do not establish systolic low-precision energy savings. Packing and arithmetic throughput differ across hardware.
