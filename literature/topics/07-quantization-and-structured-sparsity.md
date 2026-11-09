# 07 — Joint activation quantization and structured sparsity

Reviewed: **2026-11-08**. Four additional focused paper notes and shared
systolic, feeder, outlier, and decomposition sources.

## What already exists

The combination is well researched at several levels:
[SPARQ](../papers/2021-shomron-sparsity-aware-quantization.md) exploits runtime
activation bit structure; [S2TA](../papers/2022-liu-s2ta.md) supports structured
activation sparsity; [Panacea](../papers/2025-kam-panacea.md) combines
representation choices with slice-level opportunities.
[SharQ](../papers/2026-meng-sharq.md) supplies an online sparse/dense low-bit
baseline. A contribution therefore needs a specific improvement, not the
generic combination of quantization and sparsity.

## Different kinds of sparsity

| Structure | What it might avoid | What it requires |
|---|---|---|
| Existing numerical zeros | Ineffectual operations | Detection and compatible skipping |
| Runtime forced N:M mask | Bounded work per group | Additional approximation and mask generation |
| Entire zero blocks/columns | Whole operations or deliveries | Suitable physical alignment |
| Bit/slice structure | Parts of arithmetic/representation | Specialized datapath and correction |
| Sparse exceptions or backbone | A selected computation path | Packing, metadata, and result combination |

[SCNN](../papers/2017-parashar-scnn.md) illustrates compressed execution,
while [Sparseloop](../papers/2022-wu-sparseloop.md) distinguishes format,
gating, and skipping costs. Percent zeros alone does not determine any of these
benefits.

## The quantization interaction

Quantization can map small values to represented zero, but the amount depends
on scale, rounding, and clipping. Masking can reduce the range of retained
values and improve their precision, while introducing a separate pruning error.

For asymmetric integer quantization, real zero is generally represented by
the zero-point code z. Testing only whether the stored integer equals zero
can therefore be incorrect. The hardware must match the numerical
representation and account for centering/correction.

Track the intermediate representations in this order: original activation,
mask/decomposition, quantized operands, and executed result. Count errors and
savings at the stage where they occur.

## Systolic mapping constraints

A regular N:M pattern can bound work, but support depends on which operand and
dimension the hardware compresses. Transposing/repacking an activation to fit
a weight-oriented sparse mode has costs and can change dataflow.

[Late IM2COL](../papers/2020-liu-sparse-systolic-tensor-array.md) and
[SPOTS](../papers/2022-soltaniyeh-spots.md) connect operand formation with sparse
execution. Deterministic padding, activation zeros, and artificial packing
zeros must remain separate.

A pattern usable in a flexible sparse engine may still map poorly to our
regular array. [Flexagon](../papers/2023-munoz-martinez-flexagon.md) is a
comparison for traversal/reduction choices, not a drop-in systolic mechanism.

## Candidate experiment matrix

Compare at fixed weights, quality target, and hardware resources:

1. dense BF16/reference execution;
2. dense low precision;
3. existing-zero handling without forced pruning;
4. structured activation masking at fixed precision;
5. joint masking and quantization;
6. a correction/decomposition path where supported.

Ablations should separate scale improvement from avoided work. Use measured
activation patterns, including non-ReLU and diffusion workloads; do not assume
their zeros resemble older CNNs.

Collect physical block occupancy, mask/scale/index bytes, compaction operations,
per-PE work imbalance, issued cycles, buffers, and final task quality. Include
dense fallback when preparation or sparse execution loses efficiency.

## Research direction and limits

A potentially useful investigation is a causal policy that selects dense versus
structured sparse execution and numerical precision under one bounded budget.
The reviewed work makes that a crowded comparison space; novelty remains
unestablished.

The [action-model approach](../papers/2022-wu-sparseloop.md) can support early
evaluation, but measured correlated patterns and a valid hardware contract are
required. No joint algorithm or energy result has been validated here.

## Search record

Web searches on **2026-11-08** covered post-training sparsity-aware
quantization, Panacea, SCNN, and Sparseloop, with reference chaining to the
already reviewed systolic and online-decomposition papers. Full-text focus:
representation, mask generation, accumulation, and cost boundaries.
The review is targeted and does not cover every structured-sparsity proposal.
