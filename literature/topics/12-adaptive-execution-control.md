# 12 — Hardware control policies for adaptive execution

## Runtime configuration versus live-value selection

Supplement reviewed **2026-11-23**. [DBFS](../papers/2024-yu-dbfs.md) adapts
frequency to selected SIMD widths and explicitly includes accumulation
repacking. [Lu et al.](../papers/2025-lu-flexible-riscv-inference.md) combine
custom instructions, configurable arithmetic and local im2col/packing for
prepared mixed-precision models. Configuring hardware at runtime and deriving
a mode from the current activation values are distinct mechanisms. Neither
ISA support nor the general combination of lowering and quantization is new.
Compare scheduling, pack/control costs and how precision is actually selected.

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

[DRQ](../papers/2020-song-drq.md) now has a focused full-text review of live
selection and prepared region settings. [Drift](../papers/2024-liu-drift.md) and
[MixQ](../papers/2024-chen-mixq.md) remain full-text comparison dependencies.

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

## Controllers for temporal diffusion execution

Supplement reviewed **2026-11-14**. [Ditto](../papers/2025-kim-ditto.md)
contains both a width/zero classifier and execution-flow control informed by
observed layer cycles. [EXION](../papers/2025-heo-exion.md) combines prepared
thresholds, refresh iterations, and sparse execution. [SQ-DM](../papers/2025-fan-sq-dm.md)
routes channels online but does not freshly optimize its bitwidth table per input.
[Cambricon-D](../papers/2024-kong-cambricon-d.md) needs full-text assessment.

These are essential competitors for autonomous adaptive hardware. Specify
which decision is live, its frequency, its state, and its deadline. Compare
fixed, simple live, and stateful policies on the same supported actions.
Temporal similarity is an empirical input property, not permission to omit
nonlinear updates or reconstruction without checking the complete trajectory.

## Sensitivity and grouping comparisons

Supplement reviewed **2026-11-15**. [FGMP](../papers/2025-hooper-fgmp.md)
provides a live block-precision comparator with prepared sensitivity metadata.
[QBitOpt](../papers/2023-peters-qbitopt.md) is a training-time allocator;
[IGQ-ViT](../papers/2024-moon-igq-vit.md) has live group assignments with
prepared quantizers. Preserve these distinctions in controller comparisons.

## Randomized observations and feedback

Supplement reviewed **2026-11-15**. [Slalom](../papers/2019-tramer-slalom.md)
uses projected neural-operator checks; [SProbe](../papers/2026-napolean-sprobe.md)
checks quantized GEMMs and illustrates the traffic cost of trailing observation.
These are verification mechanisms, not automatically real-error precision
selectors. [Hardt and Woodruff](../papers/2012-hardt-adaptive-sketches.md)
show why guarantees for fixed inputs need not survive adaptive sketch queries.
[Probabilistic range prediction](../papers/2025-santini-probabilistic-quantization.md)
is another runtime-observation comparator with distinct calibrated preparation.

## Search and limits

Web searches on **2026-11-08** covered hardware-aware policy search,
selectable-precision networks, and data-dependent bit processing. Full-text
focus: what is trained or searched offline, what is decided online, and the
cost of realizing the decision.

The current corpus supports these distinctions but does not establish an
optimal control algorithm or complete novelty coverage. No hardware controller
has been implemented; final chip-simulator work remains deferred.

## Precision, omission and reuse controllers

Supplement reviewed **2026-11-22**. [Phantom](../papers/2026-fu-phantom.md)
uses streaming token-change reductions, TopK and address merging before dense
execution. [DiSC](../papers/2026-yoon-disc.md) connects token/mask reuse to
on-chip bank placement. [DSTAR](../papers/2026-zhang-dstar.md) and
[APT](../papers/2026-yoo-apt.md) combine live decisions with prepared statistics.
The broad notion of autonomous runtime adaptation is already represented.

Certification also has comparators: [Runtime-certified attention](../papers/2026-calver-runtime-certified-attention.md)
pays for scoring and tiered recovery, while [WitCert](../papers/2026-wei-witcert.md)
distinguishes deterministic and restricted probabilistic guarantees. A
controller's information availability, amortization, state and actual critical
path must be compared explicitly; “online” does not imply negligible cost.

## Budgeted scheduling and the actual decision inputs

Supplement reviewed **2026-11-22**. [ReCache](../papers/2026-aliev-recache.md)
learns schedules conditioned on a requested step budget;
[BudCache](../papers/2026-lei-budcache.md) searches schedules offline.
Neither title alone establishes live activation-error or cache-capacity control.
[DIP](../papers/2025-federici-dip.md), however, explicitly includes residency in
live scores, so a memory-aware pruning proposal must compare its mechanism.

[WiSparse](../papers/2026-chen-wisparse.md) has live masks with prepared
exponents/thresholds. [Prox](../papers/2026-liu-prox.md) pays for proxy products;
[Chipmunk](../papers/2025-silveria-chipmunk.md) also has a reduced MLP prediction
product. Classify such work by its size, frequency and critical path, rather
than calling every online selector lightweight.

## Geometry can enter preparation rather than live optimization

Supplement reviewed **2026-11-22**. [RoShift](../papers/2026-song-roshift.md)
uses weight Gram information to prepare rotations; [WAS](../papers/2025-wang-was.md)
prepares sparsity allocation and applies weighted live masks. Compare observation,
preparation and per-input work separately; neither “weight-aware” nor “Gram”
alone identifies an unexplored controller.

## Temporal residual control predates diffusion accelerators

Supplement reviewed **2026-11-22**. [Sigma-Delta networks](../papers/2016-oconnor-sigma-delta.md)
retain state and quantize updates. A new temporal controller must differ in a
specified algorithm or execution result; historical residual feedback alone
is not a novelty claim.

## Autonomous arithmetic control and output-driven recovery

Supplement reviewed **2026-11-23**. [Overflow-driven DPS](../papers/2026-fasolino-overflow-dps.md)
describes a fully hardware per-MAC monitor. [FAST](../papers/2021-zhang-fast.md)
already couples live precision decisions to native variable-width arithmetic
in training. Distinguish these from prepared configuration search in
[MIAO](../papers/2026-wong-miao.md); prepared search is still hardware/software
codesign, and does not establish absence of a different online contribution.

[CoMPAQt](../papers/2025-kabaha-compaqt.md) prepares class-specific bounds but
performs acceptance/refinement online. [RAELLA](../papers/2023-andrulis-raella.md)
uses live speculative input slicing with recovery and ADC gating. In its
reviewed design the crossbar still runs recovery cycles, so energy reductions
do not imply shorter array execution. Price the component actually gated,
the retained state, fallback and result-release boundary.

## Runtime scope in convolution-related designs

Supplement reviewed **2026-11-23**. [OverQ](../papers/2021-zhao-overq.md) provides
live overwrite/routing with profiled clipping ranges. The
[CNN-LSTM ASIC](../papers/2026-chen-sleep-dynamic-quantization.md) observes ranges
online for selected layers with prepared precision. These are hardware
contributions even where some parameters are chosen offline. Compare state
reset, live statistics and decision granularity individually.

## Exponent-driven execution is already a hardware mechanism

Supplement reviewed **2026-11-23**. [BFP-CIM](../papers/2024-chang-bfp-cim.md)
changes wordline execution from live exponents. The
[integer-accumulation patent description](../papers/2025-zhang-integer-fp-accumulation.md)
uses exponent cache events and impending overflow to activate finalization.
A proposed pre-issue metadata rule must be compared with those actual controls,
including retained state, exception paths and dataflow costs.

## Shape scheduling and value-driven decisions

Supplement reviewed **2026-11-23**. [DynaCore](../papers/2026-guo-dynacore.md)
selects runtime configurations using batch shapes and prepared hardware cost
tables; quantization follows execution phases. Distinguish this from choosing
a representation from the current activation values. A live-value controller
still needs a hardware cost model; its CUDA execution time is not that model.

## Precision regularity and scheduling axes

Supplement reviewed **2026-11-23**. [Atom](../papers/2024-zhao-atom.md) moves
activation channels online using calibrated IDs and aligned weight reordering.
[TileQuant](../papers/2026-zhang-tilequant.md) packs fixed weight precision maps
and adapts row tiling/splitting to call shape. [OFGQ](../papers/2026-wang-ofgq.md)
explicitly links format granularity to synchronized variable-cycle systolic
execution; its full control protocol remains unreviewed.

Distinguish reduction-channel permutation, static weight-tile packing,
activation-row scheduling and live precision decisions. The terms mixed
precision, runtime scheduling and reordering alone do not identify a new
mechanism. Charge format residency, source lookahead, row IDs, output ordering,
mode changes and fill/drain under the actual multiplier geometry. Missing full
text is an unresolved comparison, not evidence that a mechanism is absent.

## Online setup and residency decisions

Supplement reviewed **2026-11-23**. [Karlin et al.](../papers/1994-karlin-competitive-randomized.md)
provide established rent-or-buy/caching theory for decisions with recurring
service costs and one-time state changes. Mapping such a decision to numerical
format preparation requires explicit setup, residence, eviction and service
costs. Competitive guarantees depend on the comparator's constraints; a
single-phase result is not a proof of globally optimal inference energy.
Numerical eligibility and end-to-end quality remain separate obligations.
