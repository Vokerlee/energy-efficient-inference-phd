# In-Datacenter Performance Analysis of a Tensor Processing Unit

- Citation key: `jouppi2017tpu`.
- Authors: Jouppi, Norman P.; others.
- Publication: ACM/IEEE International Symposium on Computer Architecture (ISCA), 2017.
- Source: [paper](https://arxiv.org/abs/1704.04760v1); [full text reviewed](https://arxiv.org/pdf/1704.04760v1).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Sections 3–6: workload rooflines, utilization counters, and power accounting.
- Evidence: Production inference measurements; selected counterfactual hardware estimates.

## What it establishes

On one TPU generation, evaluated MLP/LSTM workloads encounter weight-bandwidth limits while CNN workloads encounter different compute/utilization limits. The paper distinguishes die and server-level comparisons.

## Relevance to our goals

Provides a systolic-accelerator example of workload-dependent bottlenecks and the importance of useful versus available MAC capacity.

## Limits and transfer conditions

This is an INT8-era TPU comparison with contemporary Haswell/K80 systems. Peak TOPS/W and projected bandwidth upgrades are not modern measured joules per inference.
