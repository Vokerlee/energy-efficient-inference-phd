# MLPerf Power: Benchmarking the Energy Efficiency of Machine Learning Systems from Microwatts to Megawatts for Sustainable AI

- Citation key: `tschand2025mlperfpower`.
- Authors: Tschand, Arya; Rajan, Arun Tejusve Raghunath; Idgunji, Sachin; Ghosh, Anirban; Holleman, Jeremy; Kiraly, Csaba; others.
- Publication: HPCA, 2025.
- Source: [paper](https://arxiv.org/abs/2410.12032v2); [full text reviewed](https://arxiv.org/pdf/2410.12032v2).
- Reviewed: 2026-11-09. Status: **full-text focused reading**.
- Reading focus: Inference measurement intervals, instruments, synchronization, and system scope.
- Evidence: Energy benchmarking methodology and measured submissions.

## What it establishes

Adapts instrumentation to system scale and aligns measured power with workload execution to derive energy-efficiency metrics.

## Relevance to our goals

Supports explicit measurement boundaries and reproducible energy integration rather than using device power ratings.

## Limits and transfer conditions

Instrumentation and boundary differ across deployment scales. Full-system energy and GPU-only telemetry are different quantities; neither automatically isolates the cost of a new hardware block.
