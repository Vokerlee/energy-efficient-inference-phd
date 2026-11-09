# MicroScopiQ: Accelerating Foundational Models through Outlier-Aware Microscaling Quantization

- Citation key: `ramachandran2025microscopiq`.
- Authors: Ramachandran, Akshat; Kundu, Souvik; Krishna, Tushar.
- Publication: ISCA, 2025.
- Source: [paper](https://arxiv.org/abs/2411.05282v4); [full text reviewed](https://arxiv.org/pdf/2411.05282v4).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Outlier storage, pruning, multi-precision PEs, and ReCoN.
- Evidence: Quantization experiments and accelerator evaluation.

## What it establishes

Preserves outlier precision by reallocating space from pruned weights and supporting reconstruction through specialized hardware.

## Relevance to our goals

A comparator for the cost of aligned exceptional values and mixed-precision delivery.

## Limits and transfer conditions

The weight-outlier/pruning mechanism is not an autonomous runtime activation detector. Its contribution cannot be transferred unchanged to our activation-focused research.
