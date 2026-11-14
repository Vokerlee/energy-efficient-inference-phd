# 05 — Runtime outliers and selective precision

Reviewed: **2026-11-08**. Five primary full-text focused notes. Focus:
activation-driven decisions, retaining weight handling as a controlled baseline.

## Evidence and the scope of an outlier

[LLM.int8()](../papers/2022-dettmers-llm-int8.md) establishes selective
higher-precision feature computation. [OliVe](../papers/2023-guo-olive.md)
shows a different route through local lossy encoding.
[MicroScopiQ](../papers/2025-ramachandran-microscopiq.md) is useful hardware
background, but its weight mechanism must not be mislabeled runtime activation
adaptation.

[SVDQuant](../papers/2025-li-svdquant.md) provides a low-rank correction
comparison. [SharQ](../papers/2026-meng-sharq.md) is particularly close to
our interests: online sparse/dense decomposition already has an implemented
baseline, including generation workloads.

An outlier can mean a rare value, a large magnitude relative to its group,
a recurrent exceptional channel, or a value whose quantization strongly affects
an output. These definitions are not interchangeable. A magnitude test is
hardware-friendly, but its relation to model sensitivity needs evidence.

## Compare mechanisms, not just thresholds

| Mechanism | Work retained | Main hardware question |
|---|---|---|
| Promote the entire tile | One regular higher-precision operation | How often does one value force promotion? |
| Separate feature dimensions | Dense main path plus selected features | Packing and gathering cost |
| Sparse exception correction | Dense low-bit path plus exceptional residual | Pattern support, metadata, and scatter/reduction |
| Local outlier/victim encoding | Aligned representation with sacrificed values | Quality loss from victims |
| Low-rank branch | Low-bit residual plus compact dense correction | Projection/fusion cost and rank occupancy |
| Sparse backbone plus dense residual | Two low-bit paths | Preparation, supported sparsity, and duplicate work |

This table is a design comparison, not a claim that every mechanism is suitable
for the same hardware.

## A precise decomposition for experiments

An algebraic activation split A = A_base + A_exception gives:

```text
A*W = A_base*W + A_exception*W
```

After quantization, define each residual relative to the representation actually
used. A residual formed before rounding generally does not correct the same
error as a residual formed after rounding. Both branches may introduce further
error.

Exact algebra does not make execution free. Charge for detection, mask
construction, packing, storage, conversion, extra matrix operations, result
alignment, and accumulation. Match final model quality.

## Fixed-size systolic consequences

Element-wise exceptions do not automatically form efficient matrix blocks.
A few exceptions spread across many columns can require many nearly empty
physical operations. Compare per-tile promotion, channel/block grouping, and
pattern-constrained masks using the same physical array modes.

Bound queue capacity and the number of exceptions per group. If that bound is
exceeded, specify whether the hardware promotes, replays, or spills. Include
this path in typical and adverse-input cost, rather than assuming an unlimited
exception engine.

Dense low precision plus sparse higher precision is therefore one candidate,
not the definition of outlier handling. SharQ is an important counterexample to
that narrow framing.

## Proposed first comparison

Use a current-group magnitude detector as the simple reference, then compare
percentile/tail-count, normalized-range, and history-based detectors under the
same state and latency budget. The latter mechanisms are experimental
candidates, not established improvements.

Measure missed consequential values, unnecessary promotions, exception
dispersion, fallback frequency, and complete-network quality. Use input
sequences that change distribution to test detector stability. Any sensitivity
information from a reference model belongs in offline analysis unless its
runtime acquisition cost is included.

A useful research question is whether a causal bounded-cost detector can
achieve a better complete-model quality–energy trade-off than these baselines.
This review does not establish its novelty or feasibility.

## Temporal differences as a separate comparison

Supplement reviewed **2026-11-14**. [Ditto](../papers/2025-kim-ditto.md)
classifies temporal differences for low/full-width execution and zero skipping.
Such a residual is a change from stored history, not the exceptional-value
residual of an outlier decomposition.

[EXION](../papers/2025-heo-exion.md) reuses selected outputs, while
[SQ-DM](../papers/2025-fan-sq-dm.md) changes activations through ReLU fine-tuning.
[Cambricon-D](../papers/2024-kong-cambricon-d.md) remains a publisher-abstract
record pending full text. Compare these interventions separately from outlier
routing so that retained state, model changes, and approximation are visible.

## Search and limits

Web discovery on **2026-11-08** covered LLM.int8, OliVe, MicroScopiQ,
SVDQuant, and SharQ. Full texts were inspected for the exception definition,
decomposition, implementation, and quality conditions. Source versions are
recorded in the notes.

The evidence is LLM/diffusion-heavy. Portability to CNN/video operators needs
experiments. No new detector or energy result has been evaluated.
