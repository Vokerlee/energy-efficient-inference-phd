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
