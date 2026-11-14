# 12 — Hardware control policies for adaptive execution

Reviewed: **2026-11-08**. Three additional focused papers and shared runtime
quantization, sparsity, and predictor evidence.

## Separate policy preparation from runtime decisions

[HAQ](../papers/2019-wang-haq.md) uses hardware feedback to search a policy
offline. [Any-Precision](../papers/2021-yu-any-precision.md) prepares a model
for selectable modes. Neither alone supplies the autonomous selector we want.

[Bit-Pragmatic](../papers/2016-albericio-bit-pragmatic.md) demonstrates
data-dependent hardware work selection.
[SPARQ](../papers/2021-shomron-sparsity-aware-quantization.md) and
[ScalePredictor](../papers/2026-li-scale-predictor.md) provide more specific
activation-driven mechanisms.

Our intended decision is made from information available at a hardware
boundary, without a host program analyzing each tensor and prescribing its
mode. Its algorithm can first be emulated in portable software.

## A minimal controller contract

Specify:

- observation point and input features;
- state retained between decisions;
- supported actions and their physical granularity;
- decision deadline and execution latency;
- initialization, transitions, and fallback;
- how the selected action alters arithmetic.

A mode table may be prepared offline. Selecting an entry online from measured
features is distinct from fixing the entry per layer before deployment.

Start with **one action dimension**, such as activation precision. Sparse/dense
routing or rank selection should enter only after separate pilots establish
their value. This avoids turning the PhD into simultaneous implementation of
all reviewed mechanisms.

## What a controller can optimize

The desired objective is energy subject to task quality and latency constraints.
But final task quality is usually not observable at the local decision point.

Offline evaluation can relate features to conservative modes or quality risk.
Runtime signals such as clipping counts are proxies, not guaranteed task-quality
bounds. A controller must not inspect the reference forward pass or future
outputs unless that extra computation is explicitly part of the mechanism.

[DRQ](../papers/2020-song-drq.md),
[Drift](../papers/2024-liu-drift.md), and
[MixQ](../papers/2024-chen-mixq.md) remain priority full-text comparison
dependencies before a novelty claim.

## Costs and stability

Even a small decision can add serial work, buffer retention, state accesses,
or a mode-change bubble. Count these at the actual decision frequency.
Overlapping control with loading requires an explicit dependency schedule;
it cannot hide a required future statistic.

Hysteresis, promotion guards, and minimum dwell time are candidate stability
mechanisms. They may reduce switching while retaining an unnecessarily costly
mode longer. Test both effects.

Variable-latency paths also require bounded queues and clear completion rules.
The numerical result must remain defined when different blocks choose
different representations.

## Proposed evaluation

Compare fixed policy, per-layer offline policy, simple live rule, and
stateful predictor. Add a learned selector only if simpler rules leave a
measurable opportunity.

For every policy, use the same hardware actions and quantify:

- final quality on held-out inputs and changed input distributions;
- energy and latency, including control and fallback;
- observation/state traffic and decision rate;
- mode changes, queue pressure, and worst observed overhead.

Use an unattainable oracle only to estimate headroom and label it clearly.
A learned policy's measured average performance does not prove safety or
optimality on every input.

## Prepared choices and decisions made during inference

Supplement reviewed **2026-11-14**. The additional controller baselines are:

- [CADyQ](../papers/2022-hong-cadyq.md): train a selector, then choose feature precision online.
- [NAWQ-SR](../papers/2023-venieris-nawq-sr.md): prepare precision/DRE placement, then update selected ranges online.
- [ResQ](../papers/2023-abati-resq.md): use an error surrogate to select residual precision.
- [PIVOT](../papers/2024-moitra-pivot.md): use a completed low-effort prediction to decide on a second inference.

A signal can be causal yet expensive. PIVOT's low-effort logits are available
at its decision point, but this does not make them available to an earlier
tile quantizer. Likewise, estimating every candidate's error has work that a
small history predictor might avoid.

These papers narrow the comparison needed before any novelty claim. Separate
the scientific policy from its hardware realization, and include both
preparation costs and runtime overhead in the appropriate evaluation.

## Search and limits

Web searches on **2026-11-08** covered hardware-aware policy search,
selectable-precision networks, and data-dependent bit processing. Full-text
focus: what is trained or searched offline, what is decided online, and the
cost of realizing the decision.

The current corpus supports these distinctions but does not establish an
optimal control algorithm or complete novelty coverage. No hardware controller
has been implemented; final chip-simulator work remains deferred.
