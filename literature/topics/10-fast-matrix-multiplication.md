# 10 — Fast matrix multiplication for neural inference

Reviewed: **2026-11-08**. Five new focused primary sources.
This is a distinct research pilot, not an extension to implement alongside
every quantization and sparsity experiment.

## What is established

Fast multiplication can reduce multiplication counts while adding linear
combinations and a different execution schedule.
[Strassen Reloaded](../papers/2016-huang-strassen-reloaded.md) shows why
implementation details influence practical crossover.
[AlphaTensor](../papers/2022-fawzi-alphatensor.md) adds hardware-oriented
algorithm discovery. Neither makes multiplication count an energy estimate.

The arithmetic domain is essential: a valid identity over a finite field is
not automatically a valid identity over the reals. Verify each candidate's
coefficients and domain before treating it as neural matrix multiplication.

## Fixed-size systolic interpretation

A single Strassen level replaces eight ordinary block multiplications with
seven, plus additions/subtractions and result recombination. The blocks must
ultimately be decomposed into supported physical operations.

Potential savings compete with:

- constructing temporary operands and partial outputs;
- padding and shape mismatch;
- extra storage and movement;
- changes to arithmetic precision and overflow headroom;
- lost reuse or pipeline overlap.

This is a derived accounting framework, not a predicted speedup.
The right comparison uses identical array resources, memory budget, supported
formats, and a conventional dense mapping optimized to the same standard.

## Interaction with quantization

Pre-additions change value ranges. Quantizing operands before forming linear
combinations and quantizing the combinations themselves are different algorithms.

Independent scales cannot be ignored during additions. Wider temporary
arithmetic or additional rescaling can erase part of the multiplier saving.
Repeated levels can amplify range and cancellation issues.

[Fast linear algebra stability](../papers/2007-demmel-fast-linear-algebra.md)
shows that broad stability claims need explicit assumptions. It does not
establish that a particular BF16/FP8 implementation preserves model quality.

## Convolution alternatives belong in the comparison

[Winograd filtering](../papers/2016-lavin-fast-convolution.md) reduces
multiplication work for suitable small convolutions, while
[error analysis](../papers/2019-barabasz-winograd-error.md) exposes numerical
trade-offs. Compare its transforms against the actual im2col/direct mapping,
not just the original logical MAC count.

A transform-based convolution and a new matrix multiplication algorithm are
different mechanisms. Report their benefits separately before considering
composition.

## A bounded first pilot

Start with one verified real-arithmetic scheme and one recursion level:

1. implement an exact/high-precision reference decomposition;
2. map every suboperation to fixed physical tiles;
3. count additions, temporary traffic, and issued matrix operations;
4. introduce controlled numerical formats;
5. run the modified computation in complete networks.

Sweep rectangular shapes and small/large reductions around alignment
boundaries. Include adversarial cancellation and realistic activations.
Keep useful-operation accounting separate from physical execution.

Potential algorithm selection by runtime shape is a later step. Avoid online
search or many schemes before a single candidate shows a quality–energy
benefit over a strong baseline.

## Search record and limits

Web searches on **2026-11-08** covered Strassen Reloaded, AlphaTensor,
fast-linear-algebra stability, Winograd convolution, and its numerical analysis.
Full-text focus: arithmetic domains, finite-size overhead, and precision.

A [2026 fast-multiplication catalog](https://arxiv.org/abs/2606.13408) was
screened as a future search lead; its individual schemes were not verified here.
The current selection is foundational rather than an exhaustive catalog of
2025–2026 algorithms.

No scheme has been implemented in our engine and no new neural-network
energy/quality result or novelty claim is established.

## Recent specific comparators

Supplement screened **2026-11-22** at primary-abstract level; detailed reviews
remain pending and no results were reproduced.

- [SubCuber](../papers/2026-jangda-subcuber.md) generates fused shape/GPU-dependent CUDA schedules.
- [Strassen with dynamic block quantization](../papers/2025-chiu-strassen-dynamic-quantization.md) is explicitly described for ViT in an official 2025 conference poster abstract.
- [FP8 coefficient optimization](../papers/2026-xie-fp8-fast-matmul.md) studies numerical differences between exact multiplication realizations under a specified model.

These sources constrain broad novelty claims without establishing that every
runtime selection, finite-memory mapping or error-control problem is covered.
Do not label Strassen-plus-quantization or GPU schedule generation as new solely
because the foundational review did not contain these recent comparators.

## Quantized Winograd in diffusion already has direct precedents

Focused supplement **2026-11-24**. [Pan et al.](../papers/2025-pan-group-quantized-winograd.md)
combine dynamic group activation scales, synthetic-data optimization of transform
scales and diffusion inference. [PAW](../papers/2023-chen-paw-winograd.md), reviewed
at abstract level, already addresses full quantization and factorized scales.
Generic Winograd-plus-dynamic-quantization is therefore not a new contribution.
Compare offline transform preparation with any current-tile rule, including
input/output transforms, extra transformed-weight capacity, fixed matrix tiles
and the FP32 result path. Fewer products can coexist with more intermediate
traffic. Do not transfer CPU latency into systolic energy.

## Hardware baselines for transform and reduction ordering

Reviewed **2026-11-24**. [Tap-wise quantization](../papers/2022-andri-tap-wise-winograd.md)
requires matched transform/compute rates. [Hattink et al.](../papers/2020-hattink-winograd-memories.md)
already accumulate spatial partial outputs and discuss summation before inverse
transforms. Neither generic fusion nor this reordering alone is new.

## Transform and geometry comparators

Supplement reviewed **2026-11-24**. [Channel balancing](../papers/2022-chikin-winograd-balancing.md),
[quantization-friendly transforms](../papers/2024-protsenko-quantization-friendly-winograd.md)
and [Wino Vidi Vici](../papers/2024-mori-wino-vidi-vici.md) distinguish calibration,
model-independent preparation and training. [Concentration–alignment analysis](../papers/2026-federici-concentration-alignment.md)
provides a direct geometry comparator at abstract-reading scope. These broad
connections are established; a new live mechanism needs a specific difference
and matched numerical/cost evidence. Individual records state reading limits.

## Prepared tile selection and specialized transform costs

[Ji et al.](../papers/2021-ji-winograd-tile-fusion.md) already select Winograd
tiles from layer-dependent total-work models. [Hybrid CIM](../papers/2025-guo-winograd-hybrid-cim.md)
already accelerates output transforms. Reviews dated **2026-11-24** retain
publication/reading limits; broad titles do not resolve every live-controller case.

## Transform-domain sparse execution

Focused review **2026-11-24**: [WINS](../papers/2025-park-wins.md) already
co-designs structured transformed weights with sub-GEMM workload balance.
[Winograd-ReLU](../papers/2018-liu-sparse-winograd.md) already produces dynamic
transformed activation zeros, but changes network semantics and retrains.
Neither observation makes arbitrary live pruning of an unchanged model safe.
Compare useful products, padded array work, metadata and scheduling separately.
