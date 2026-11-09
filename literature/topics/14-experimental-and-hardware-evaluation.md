# 14 — Portable experiments and credible hardware evaluation

Reviewed: **2026-11-09**. Four new full-text focused notes and shared modeling
and energy-measurement evidence. This review proposes an evaluation approach;
it does not implement an engine or establish energy savings.

## Main conclusion

Keep numerical validity, hardware cost estimation, and measured performance as
separate results connected by a defined execution contract. Portable software
can evaluate an algorithm intended for autonomous hardware decisions without
requiring the final chip simulator during early research.

## Relevant evidence

[TVM](../papers/2018-chen-tvm.md) provides a precedent for separating computation,
schedules, and target tensor primitives. It motivates an extensible boundary,
not a requirement to reproduce a complete compiler.

[MLPerf Inference](../papers/2020-reddi-mlperf-inference.md) motivates fixed
workload scenarios and explicit task-quality acceptance.
[MLPerf Power](../papers/2025-tschand-mlperf-power.md) supplies measurement
methodology; its historical paper must not substitute for current rules.

[Timeloop](../papers/2019-parashar-timeloop.md),
[Accelergy](../papers/2019-wu-accelergy.md), and
[Sparseloop](../papers/2022-wu-sparseloop.md) support mapping/action-based cost
analysis. [SCALE-Sim v3](../papers/2025-raj-scale-sim-v3.md) illustrates the
additional effects of memory timing and layouts. Validation remains specific
to the configurations actually checked.

## Minimal portable runtime

Begin with one complete reference model and one replaceable operation path.
Use an established framework for loading and unchanged operators if useful;
a new graph compiler and every operator are not prerequisites.

The reusable engine should own tensor/layout contracts, finite execution
blocks, numerical formats, accumulation, generic policy state, and event
reporting. Model names, datasets, task metrics, and PhD hypotheses do not belong
in that layer. Model-specific adapters and reproducible runs belong in the
experiments repository; scientific interpretation stays in this repository.

Specify the contract before optimizing the implementation:

- physical block dimensions per supported mode and edge/padding behavior;
- statistics and quantization groups, with their relationship to those blocks;
- rounding, clipping, scale representation, rescaling, and accumulation order;
- observation timing, controller state/reset rules, initialization, and fallback;
- unsupported-operator handling and the boundary of the modeled hardware path.

The policy must alter operands used by downstream computation. Tests of a
finite block and partial sums should establish arithmetic semantics before
full-model task evaluation. A reference forward pass may be an offline
comparison, but its values cannot silently inform the runtime policy.

## Evidence ladder

| Stage | Question answered | Limitation |
|---|---|---|
| Full-model numerical emulation | Does the intervention preserve task quality? | Host runtime is not target-chip latency |
| Mapping and action counts | Which operations and transfers are required? | Counts alone do not establish joules |
| Characterized cost model | Is the estimated trade-off promising? | Accuracy depends on components and scheduling assumptions |
| Selected detailed validation | Does the proposed mechanism survive realistic timing/control? | Covers the cases actually validated |
| Physical measurement, where available | What energy was consumed within the stated boundary? | Another device does not directly measure the proposed chip |

Detailed programming of the user's chip simulator belongs at the final
validation stage for a selected mechanism. Public tools are methodological
references or optional cross-checks, not additional mandatory implementations.

## Count the mechanism, not just saved MACs

Record issued blocks and useful work separately. Include physical padding,
feeder/im2col actions, conversions, scale/state traffic, detection, metadata,
exception handling, retained buffers, and replay. Define where compression
occurs: conversion near the array cannot save upstream transfers already made.

Do not estimate latency by summing all component times if execution overlaps;
do not assume overlap when a dependency forces serialization. Account for
array fill/drain, bandwidth, mode changes, and finite queues at an appropriate
model fidelity. An average sparse density may miss correlations and imbalance.

Use action energy coefficients with their provenance and characterize new
components when necessary. Report sensitivity to uncertain coefficients,
bandwidth, and overhead. Compare policies on the same hardware, and distinguish
that comparison from a redesign with different area or throughput resources.

## Measurement and reproducibility

For real execution, state the measured system boundary, interval, warmup,
synchronization, batching, concurrency, power settings, and repetitions.
Integrate valid power samples over the stated interval or use appropriate
energy counters. Preserve raw samples and elapsed times.

[GPU-sensor analysis](../papers/2024-yang-power-measurements.md) and the
[ML.ENERGY benchmark](../papers/2025-chung-ml-energy-benchmark.md) provide
additional measurement context. Neither TDP nor a faster fake-quantization
implementation demonstrates energy savings for a proposed accelerator.

Keep a small run configuration with resolved engine/experiment revisions,
checkpoint and input identities, preprocessing, seeds, policy parameters,
hardware description, cost coefficients, evaluator version, and environment.
Preserve raw outputs and scripts that regenerate summaries. A central research
milestone can pin the nested code revisions; routine code commits need no
central submodule update. Git history alone does not preserve external model
and dataset contents, so record stable versions and content identifiers.

## First experiment, proposed rather than implemented

Compare a fixed calibrated activation policy, a current-block range baseline
with its buffering/prepass charged, and one causal history-based policy.
Hold weight handling, supported formats, mapping, and quality requirements
fixed. Use the complete adapted forward trajectory and held-out task evaluation
from [topic 13](13-end-to-end-quality.md).

Measure quality first, then estimate the hardware cost of acceptable candidates.
Record failures and include fallback in the totals. Add sparsity, low-rank
execution, or broader model coverage only as separate, justified experiments.

## Search and limits

Primary web searches on **2026-11-09** covered TVM, MLPerf Inference, MLPerf
Power, and SCALE-Sim v3. Full texts were examined for the sections recorded in
their notes; versions are pinned there. Current
[MLCommons inference documentation](https://mlcommons.org/benchmarks/inference-datacenter/)
was checked for its full-system measurement boundary.

This targeted review does not select a complete software stack or claim that
an existing simulator models our controller. No runtime, neural-network
experiment, hardware simulation, or energy measurement was executed here.
