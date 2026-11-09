# SCALE-Sim v3: A modular cycle-accurate systolic accelerator simulator for end-to-end system analysis

- Citation key: `raj2025scalesimv3`.
- Authors: Raj, Ritik; Banerjee, Sarbartha; Chandra, Nikhil; Wan, Zishen; Tong, Jianming; Samajdar, Ananda; Krishna, Tushar.
- Publication: ISPASS, 2025.
- Source: [paper](https://arxiv.org/abs/2504.15377v2); [full text reviewed](https://arxiv.org/pdf/2504.15377v2).
- Reviewed: 2026-11-09. Status: **full-text focused reading**.
- Reading focus: Sparse assumptions, memory/layout modeling, Accelergy integration, and validation.
- Evidence: Cycle-based modeling with selected RTL and implementation comparisons.

## What it establishes

Extends systolic-array analysis with sparse execution, multicore behavior, DRAM, layouts, and action-based energy estimation.

## Relevance to our goals

A reference for deciding which omitted stalls or memory effects could change an analytical ranking.

## Limits and transfer conditions

Reported validation is configuration-specific. Its modeled sparse patterns and datapaths do not automatically represent runtime activation masks, adaptive conversion, or full-model numerical quality.
