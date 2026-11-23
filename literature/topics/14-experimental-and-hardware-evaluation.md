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

## Cost of observing a matrix product

Supplement reviewed **2026-11-15**. [Slalom](../papers/2019-tramer-slalom.md)
distinguishes preprocessing from online projected verification.
[SProbe](../papers/2026-napolean-sprobe.md) contrasts trailing verification,
which rereads matrix data, with fused checksums. Their verification goals
and arithmetic differ, but both reinforce the need to count observation
traffic and auxiliary computation rather than treating them as free.

## CUDA execution and comparison sources

Supplement reviewed **2026-11-15**. [CUTLASS](../papers/2026-nvidia-cutlass-kernels.md)
provides source-level kernel building blocks; [PyTorch operator integration](../papers/2026-pytorch-custom-cuda-operators.md)
connects custom execution to full models; [cuBLASLt](../papers/2026-nvidia-cublaslt-reference.md)
provides a separate library comparator. Match arithmetic settings and include
layout/workspace costs. Kernel speed, semantic fidelity and target-accelerator
energy are distinct evaluation quantities.

[CUDA component archives](../papers/2026-nvidia-cuda-redistributables.md)
provide versioned compiler/runtime inputs. Record these alongside Python
dependencies, source revisions and GPU architectures; a driver version alone
does not identify the compiler used for a native kernel.

## Architecture references for component scaling

Supplement reviewed **2026-11-22**. [Mistral 7B](../papers/2023-jiang-mistral-7b.md)
and [Llama 3](../papers/2024-dubey-llama-3.md) provide versioned dimensions
for defining reduced components. Preserve or explicitly vary hidden/FFN
ratios, head dimensions, query/key-value head ratios and attention rules.
Specify output-head size independently: the papers use different vocabularies.
A reduced initialized block tests a numerical mechanism, not the quality of
the trained source model.

Llama 3's FP8 evaluation also shows why a standard aggregate benchmark alone
can miss rare response failures. Dynamic-scaling experiments should report
their actual scaling restrictions and output-quality checks; architecture
similarity does not transfer numerical tolerances or energy claims.

## Component-energy attribution

Supplement reviewed **2026-11-22**. [CLEAR](../papers/2026-jain-clear-transformer-energy.md)
replays saved inputs to overcome coarse GPU energy-sensor timing. Repetitions
can alter caches, clocks and launch amortization, so validate against complete
model invocations and the actual fused baseline. Its language-model findings
are not direct ViT/DiT energy measurements.

[Diffusion energy scaling](../papers/2026-iyengar-diffusion-energy-scaling.md)
fits complete-run idle-subtracted GPU energy; its FLOP decomposition does not
isolate stage energy. Combine physical observations with mapping/action counts
rather than turning latency or FLOP percentages into joule percentages.
See [topic 01](01-inference-energy.md) for the vision/diffusion evidence split.

## Search and limits

Primary web searches on **2026-11-09** covered TVM, MLPerf Inference, MLPerf
Power, and SCALE-Sim v3. Full texts were examined for the sections recorded in
their notes; versions are pinned there. Current
[MLCommons inference documentation](https://mlcommons.org/benchmarks/inference-datacenter/)
was checked for its full-system measurement boundary.

This targeted review does not select a complete software stack or claim that
an existing simulator models our controller. No runtime, neural-network
experiment, hardware simulation, or energy measurement was executed here.

## Architecture-specific evaluation boundaries

Supplement reviewed **2026-11-22** from primary architecture descriptions and
checkpoint documentation, with reading depth recorded per source.

- [SigLIP 2](../papers/2025-tschannen-siglip2.md): distinguish the vision tower from the full image/text system and preserve the final classification/retrieval protocol.
- [Sana](../papers/2024-xie-sana.md): linear attention and depthwise Mix-FFN invalidate a conventional quadratic-attention/two-linear-MLP accounting shortcut.
- [PixArt-Sigma](../papers/2024-chen-pixart-sigma.md): query and key/value token lengths can differ; inspect the actual checkpoint's compression configuration.
- [Qwen-Image](../papers/2025-wu-qwen-image.md): weight bytes alone do not establish peak memory; generator size and full pipeline costs differ.

Freeze checkpoint revision, configuration, preprocessing, precision and execution
path before a hypothesis test. Separate uninstrumented timing from activation
inspection; changing fusion, offload or conditioning reuse changes the measured
system. Architecture descriptions do not establish approximation headroom or
energy savings, and no model run was performed in this review.

## Arithmetic and quality validation boundaries

Supplement reviewed **2026-11-23**. [MIAO](../papers/2026-wong-miao.md) combines
synthesis-based hardware estimates, an accuracy predictor and bit-exact
end-to-end candidate evaluation. This is stronger implementation evidence
than counting useful MACs, but remains tied to its declared architecture and
calibration/search procedure. [FnRR boundaries](../papers/2026-he-bfp-accumulation-boundary.md)
is another accumulation/hardware comparator whose complete assumptions await
full-text review.

[Kernel Contracts](../papers/2026-veit-kernel-contracts.md) motivates recording
a reference oracle and tolerance separately from the measurement protocol.
Its checker measurements do not establish a controller's energy or a full
network guarantee. Preserve the distinction between fixed-input local replay,
accumulated DAG discrepancy and task-level quality, especially when changing
block order, accumulator width or the number of rounding points.

## Current model families and preserved per-model evidence

Supplement reviewed **2026-11-23**. [DINOv3](../papers/2025-simeoni-dinov3.md)
requires distinguishing a feature backbone from its downstream evaluation head.
[SANA-Sprint](../papers/2025-chen-sana-sprint.md) separates text encoding,
few-step denoising and decoding. [ConvNeXt V2](../papers/2023-woo-convnext-v2.md)
provides a depthwise/channel-mixing control rather than a dense-convolution
surrogate. Preserve pinned checkpoints, input conditions, complete operator
profiles and numerical measurements for each model, including unfavorable
results. Shape-only MAC profiles and task-quality runs are different evidence.

## Full text-to-image scope

Supplement reviewed **2026-11-23**. [DC-AE](../papers/2025-chen-dc-ae.md)
keeps a neural image decoder outside the latent denoiser; its compression
choice changes the arithmetic balance. [Gemma2](../papers/2024-gemma-team-gemma2.md)
can serve as a full-sequence prompt encoder without an executed LM head.
A complete request profile must state text-encoding calls, denoising steps,
classifier-free/guidance-embedding behavior and image-decoding calls. Cold and
cached-prompt requests differ. Denoiser-only MAC shares cannot be generalized
to whole-pipeline energy. Preserve component configurations and independent
count checks; embedding lookup and masked-kernel behavior need separate accounting.

## Upsampling without explicit expanded tensors

Supplement reviewed **2026-11-23**. [Colbert et al.](../papers/2021-colbert-upsampling.md)
already fold nearest-neighbor duplication into prepared weights, reducing2x
resize-plus3x3 arithmetic to4/9 of its original dense MAC count. This is a
baseline, not a new decomposition. [Sestito et al.](../papers/2021-sestito-flexible-convolution.md)
provide a distinct online remapping implementation for zero-insertion transposed
convolution. Check border/phase ordering, numerical formats, array utilization,
weight growth and buffering; modeled energy is not target-chip measurement.

## Numerical research tools and testing protocols

Supplement reviewed **2026-11-24**. [QPyTorch](../papers/2019-zhang-qpytorch.md)
and [Arbitor](../papers/2023-jiang-arbitor.md) already support portable numerical
emulation, with different accumulator granularity. [INT-FP-QSim](../papers/2023-nair-int-fp-qsim.md)
adds a model/format comparison baseline (abstract-only here).
[QAPPA2017](../papers/2017-moreau-qappa.md) and the distinct
[QAPPA2022](../papers/2022-inci-qappa.md) address quality/energy or quantization-aware
PPA exploration. [NNSmith](../papers/2023-liu-nnsmith.md) and
[DiverGet](../papers/2022-yahmed-diverget.md) establish generated/differential tests
and quantization-robustness search. A new tool is not automatically a new method.
Compare arithmetic boundaries, causal decisions/state, acceptable approximation,
cost characterization and scientific findings. Full-method dependencies are
marked in each record; this map is not an exhaustive novelty verdict.

Focused follow-up **2026-11-24**: [DiverGet](../papers/2022-yahmed-diverget.md)
is now read in Sections4.1–4.4 and5.1. Its search objectives include output
Jensen–Shannon divergence and coverage-signature differences, using
hyperspectral-domain transformations and TensorFlow Lite PTQ/QAT subjects.
Do not describe this as merely random noise testing.

For numerical-validation comparisons, state which claims are actually tested:

| Comparison axis | Evidence to inspect |
|---|---|
| Arithmetic fidelity | Primitive rounding, accumulation boundaries, exceptional values and reference semantics |
| Adaptive decisions | Information deadline, actual decisions, prior state and reset behavior |
| Counterfactual interpretation | Fixed versus recomputed configuration, changed future trajectories and interaction terms |
| Model outcome | Complete execution, task/fidelity metric, strong controls and independent input scope |
| Cost validity | Activity counts, characterized coefficients, uncertainty and unmodified-work denominator |

The inspected DiverGet protocol does not report the same live/frozen controller
intervention as the decoder diagnostics. This narrow comparison does not prove
absence from all prior work. General custom arithmetic emulators may be
extensible; lack of a reported experiment is not lack of implementation capability.

## Existing analysis of unstable numerical decisions

Focused primary-source follow-up **2026-11-24**: [FLUCTUAT](../papers/2013-goubault-fluctuat-unstable-tests.md)
already separates round-off effects from discontinuity caused by different
branches. [Titolo et al. 2018](../papers/2018-titolo-eliminating-unstable-tests.md)
and [2020](../papers/2020-titolo-test-stable-code.md) give sound guarded execution
and verified code generation, rather than merely observing that rounding can
change a decision. Margin checks and selective escalation must be compared
with this prior art; their generic principle is not a new contribution.

A finite-precision neural experiment can ask a different empirical question:
which decisions and state matter for comparing candidate optimizations, and
when does a cheaper implementation preserve the comparison? It must still
justify its bounds, intervention, acceptance criterion and input scope. An
observed perturbation envelope is diagnostic evidence, not a universal
certificate; unchanged decisions alone do not certify unchanged output codes
or task quality.

Focused follow-up **2026-11-24**: [NNSmith](../papers/2023-liu-nnsmith.md)
Sections2.3,3 and4 distinguish graph/type validity from numerical validity.
Its gradient search avoids exceptional intermediates even when downstream
operators would hide them. Any comparison against this baseline must preserve
that distinction; naive random-tensor testing is not representative of NNSmith.
