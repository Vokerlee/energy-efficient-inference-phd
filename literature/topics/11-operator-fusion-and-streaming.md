# 11 — Operator fusion and streaming inference

Reviewed: **2026-11-08**. Five new focused papers, with shared decomposition
and feeder references. Systolic execution remains the target.

## Why this matters even for compute-intensive inference

Removing intermediate transfers can reduce energy while an arithmetic path
remains the latency bottleneck. Fusion also changes the values and statistics
available to a quantizer and may remove the opportunity to inspect a complete
tensor.

[Hardware layer fusion](../papers/2016-alwani-fused-layer-cnn.md) and
[FlashAttention](../papers/2022-dao-flashattention.md) establish existing
approaches. [FuseMax](../papers/2024-nayak-fusemax.md) supplies a spatial
accelerator perspective beyond GPU kernels.

## Three different changes

| Change | Intended benefit | Required accounting |
|---|---|---|
| Keep intermediates local | Avoid transfers/materialization | Live storage, banking, halos |
| Overlap producer and consumer | Hide otherwise idle time | Dependencies, queues, stalls |
| Combine numerical transforms | Avoid repeated reads/conversions | Scale availability and rounding |

These mechanisms can coexist but must be evaluated separately.
[FlashAttention-3](../papers/2024-shah-flashattention-3.md) illustrates their
interaction; [FlashAttention-4](../papers/2026-zadouri-flashattention-4.md)
shows how changing hardware throughput moves the limiting stage.

## Attention as a bounded-storage example

QK products, normalization, and multiplication by V cannot be treated as one
unbounded matrix operation. A streaming implementation maintains normalization
state while visiting tiles and produces a numerically defined output.

Distinguish exact algebraic attention from approximated attention patterns,
and distinguish both from floating-point reordering. Lower precision adds
another approximation that needs full-model validation.

The execution model must include non-matrix work: exponentials, reductions,
normalization, elementwise operations, and transfers. Faster matrix multiplication
does not automatically accelerate these stages.

## Quantization creates new dependencies

If a producer emits values directly to a consumer, a scale based on the complete
consumer group may not yet be available. Compare:

- buffering/replaying that group;
- a causal historical or producer-derived scale;
- smaller groups with additional metadata;
- retaining higher precision across the fused boundary.

Fusing amax calculation into production does not mean the final amax is known
before earlier values must be quantized. Record decision timing explicitly.

Similarly, fusing two branches may reduce duplicated activation reads without
removing their arithmetic or combination cost.
[SVDQuant](../papers/2025-li-svdquant.md) provides a concrete execution baseline.
[Streaming im2col](../papers/2023-fornt-on-the-fly-im2col.md) is another producer
that can change statistics and reuse opportunities.

## A suitable experiment

Begin with one common operator chain or attention block:

1. define an unfused numerical reference;
2. add a storage-bounded fused schedule without approximation;
3. verify outputs under the declared arithmetic semantics;
4. introduce quantization at one explicit boundary;
5. measure complete-network quality and account for all stages.

Compare peak live storage, bytes at every boundary, issued work, nonlinear
actions, synchronization, latency, and energy estimates. Ensure the baseline
has the same memory capacity and reasonable fusion opportunities.

This is a proposed evaluation sequence, not an implementation task.

## Sparse attention within tiled execution

Supplement reviewed **2026-11-14**. Sparse attention chooses interactions to
retain; FlashAttention-style tiling and online normalization organize execution.
The two can coexist. Dense attention remains a useful reference for measuring
the approximation introduced by interaction removal.

[STA](../papers/2025-zhang-sliding-tile-attention.md) keeps dense work inside
selected tiles. [SpargeAttention](../papers/2025-zhang-spargeattention.md)
distinguishes skipping QK and PV together from skipping PV only after scores
have been computed. The second decision cannot retroactively save QK.

[NSA](../papers/2025-yuan-native-sparse-attention.md) is a separate trained
architecture comparison. [GSRS](../papers/2026-dai-growing-sparsity-reduced-search.md)
provides a temporal-search baseline: exact current block importance is recovered
after row normalization completes. This is not a statistic available for free
before the score computation that produced it.

Record whether blocks are excluded before normalization or contributions are
omitted later; preserve each method's denominator and output-update semantics.
Also record initialization, empty-row handling, and rescaling when the running
maximum changes. A correct mask alone does not define correct streaming output.

For portable experiments, first implement a fixed block mask with explicit
normalization semantics and full-forward evaluation. Next add one causal
selector, with its search passes and state charged. Finally vary retained-block
precision. Compare whole-model quality, QK/PV blocks, softmax work, live storage,
traffic, latency, and modeled energy. GPU results motivate candidates; they do
not validate a new systolic implementation.

This supplement is targeted, not an exhaustive sparse-attention survey.

## Search and limits

Web searches on **2026-11-08** covered fused-layer CNN accelerators,
FlashAttention, FlashAttention-3/4, and FuseMax. Full-text focus: dependencies,
local storage, non-matrix work, and numerical boundaries.

[Hardware-Aware FP4 FlashAttention-4](https://arxiv.org/abs/2609.04105) and
[recent block-scaled implementation work](https://pytorch.org/blog/low-precision-flash-attention-4-end-to-end-block-scaled-attention-for-blackwell/)
were screened as follow-up leads; their detailed results were not incorporated.

This is a targeted review, not a complete fusion-compiler survey. No new fusion
schedule or energy benefit is validated.
