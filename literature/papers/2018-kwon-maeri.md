# MAERI: Enabling Flexible Dataflow Mapping over DNN Accelerators via Reconfigurable Interconnects

- Citation key: `kwon2018maeri`.
- Authors: Kwon, Hyoukjun; Samajdar, Ananda; Krishna, Tushar.
- Publication: ASPLOS, 2018.
- Source: [paper](https://anands09.github.io/papers/maeri_asplos2018.pdf).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Distribution/reduction networks, mapping flexibility, and implementation costs.
- Evidence: Architecture evaluation and hardware implementation estimates.

## What it establishes

Uses configurable distribution and augmented reduction networks to support different computation partitions and reuse patterns.

## Relevance to our goals

A comparator for assessing whether systolic underutilization justifies more flexible routing and reduction.

## Limits and transfer conditions

Flexibility has area, wiring, switching, and scheduling costs. Reported utilization gains depend on mappings and baselines; they are not direct energy savings for our inference workload.
