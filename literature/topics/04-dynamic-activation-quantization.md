# 04 — Hardware-driven dynamic activation quantization

Reviewed: **2026-11-08**. Six new full-text focused notes and two explicitly
pending full-text records; shared diffusion and energy sources are reused.

## Distinctions that define the research question

Runtime quantization has several separate meanings:

1. executing a fixed conversion rule on current activations;
2. deriving scales from live values;
3. selecting the numerical format or bit width;
4. choosing the policy autonomously in hardware.

A programmable kernel can perform the first three. Our intended research
emphasizes the fourth, with causal information and a hardware cost budget.
A precision-scalable array alone does not establish autonomous decision-making.

## Evidence map

| Source | Role | What must remain distinct |
|---|---|---|
| [VS-Quant](../papers/2021-dai-vs-quant.md) | Vector scaling and hardware overhead | Calibration versus live conversion |
| [5 nm prototype](../papers/2022-keller-vector-scaled-accelerator.md) | Physical low-bit inference support | Whole design versus activation-only benefit |
| [ZeroQuant](../papers/2022-yao-zeroquant.md) | Runtime software baseline | Kernel execution versus hardware policy |
| [MX](../papers/2023-rouhani-microscaling.md) | Shared-scale formats | Representation block versus execution tile |
| [ADiP](../papers/2026-abdelmaksoud-adip.md) | Reconfigurable systolic datapath | Supported precision versus its selection rule |
| [Finer Better?](../papers/2026-fasoli-microscaling-limits.md) | Scale-format limitations | More groups versus representable scales |
| [ViDiT-Q](../papers/2025-zhao-vidit-q.md) | Diffusion quality and execution baseline | Dynamic values versus offline sensitivity choices |

[DRQ](../papers/2020-song-drq.md) and [Drift](../papers/2024-liu-drift.md) are
important competitors whose full-text mechanisms remain unverified in this
pass. Their existence precludes treating “dynamic activation quantization” as
a novelty claim by itself.

## The hardware-realistic decision point

For every candidate, define the values already available, the state retained,
and the deadline for issuing the affected computation.

A measured current-block maximum requires seeing the relevant block. Viable
implementations might buffer it, make a prepass, reuse statistics already
available at a producer, or predict a conservative range. Each option has
different latency, traffic, and failure behavior.

Distinguish three granularities:

- **statistics group:** values summarized together;
- **quantization group:** values sharing a representation/scale;
- **execution tile:** the physical matrix operation and its shared mode.

They may differ. A policy that picks separate widths for groups inside one
tile needs hardware support for that mixture, separate execution, or promotion
to a common mode. Include the cost of that reconciliation.

## Representation and arithmetic

For symmetric integer quantization, an initial reference can use:

```text
q = clamp(round(x / s), q_min, q_max)
x_hat = s * q
```

Specify rounding, clipping, signed range, zero handling, scale representation,
and exceptional values. This is an experimental reference definition, not a
new algorithm.

For A and B partitioned along K, independently scaled integer products must
be rescaled before being combined into one numerical output. Scale generation
and application are part of the computation, not free annotations.
[MX](../papers/2023-rouhani-microscaling.md) motivates that representation
contract; [scale-format analysis](../papers/2026-fasoli-microscaling-limits.md)
warns against assuming that small groups remove all numerical problems.

Hold weight handling fixed while studying runtime activations. Weight
quantization methods can be baselines or dependencies, without becoming the
research contribution.

## First algorithm comparison

This is a proposed portable experiment:

- fixed calibrated activation scales;
- current-group measured range with fully charged buffering/prepass;
- conservative predicted range with the same allowed hardware state;
- adaptive precision with an explicit promotion/fallback rule;
- an offline oracle, labeled unattainable at runtime, to bound potential benefit.

Actually replace operands in the forward pass. Compare final task quality,
clipping incidence, precision distribution, physical issued work, metadata,
conversion, and fallback overhead. A low local MSE does not establish full-model
validity.

Use the same supported format modes and numerical execution contract for every
policy. Only then investigate whether a different block layout improves results.

## Research implications and limits

The useful candidate question is whether a particular causal policy can improve
the quality–energy trade-off after its complete hardware cost is included.
That question still requires experiments and a deeper competitor comparison.

The [2026 energy study](../papers/2026-chung-where-joules-go.md) reinforces the
need to measure the complete execution path. No energy saving follows merely
from selecting fewer bits.

## Search record

Web searches on **2026-11-08** covered dynamic region/distribution quantization,
DRQ, Drift, VS-Quant, the 5 nm vector-scaled prototype, ZeroQuant, microscaling,
ADiP, and scale-format limits. Full texts were read selectively for grouping,
conversion, datapaths, and evaluation. Versions are pinned in the notes.

Drift metadata was checked using
[Crossref's publisher-deposited record](https://api.crossref.org/works/10.1145%2F3649329.3655986);
publisher access failed. DRQ uses an author publication record. These records
are intentionally not labeled completed full-text reviews.

This targeted corpus is not exhaustive. No new algorithm, measurement, or
novelty conclusion is established here.
