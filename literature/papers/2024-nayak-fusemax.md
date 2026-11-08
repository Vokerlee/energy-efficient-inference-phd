# FuseMax: Leveraging Extended Einsums to Optimize Attention Accelerator Design

- Citation key: `nayak2024fusemax`.
- Authors: Nayak, Nandeeka; Wu, Xinrui; Odemuyiwa, Toluwanimi O.; Pellauer, Michael; Emer, Joel S.; Fletcher, Christopher W..
- Publication: MICRO, 2024.
- Source: [paper](https://arxiv.org/abs/2406.10491v3); [full text reviewed](https://arxiv.org/pdf/2406.10491v3).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Cascade dependencies, passes, buffer requirements, and array mapping.
- Evidence: Attention architecture/model evaluation.

## What it establishes

Uses explicit dependent tensor computations to co-design attention execution, storage, and compute utilization.

## Relevance to our goals

A hardware-centered comparator for combining matrix and reduction/nonlinear stages.

## Limits and transfer conditions

Its specialized mapping and cost assumptions must be preserved. It is not a generic proof that fusion removes every data bottleneck.
