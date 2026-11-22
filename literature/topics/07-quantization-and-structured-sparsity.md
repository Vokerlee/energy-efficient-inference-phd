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

## Sparse attention and activation sparsity

Supplement reviewed **2026-11-14** from original full texts. Attention sparsity
removes selected token interactions; it does not require Q, K, or V to contain
numerical zeros. Retained blocks can still use dense matrix multiplication.

| Method | Selection | Preparation and transfer limit |
|---|---|---|
| [STA](../papers/2025-zhang-sliding-tile-attention.md) | Spatial-temporal tile windows | Profiled per-head choices; optional fine-tuning is a separate variant |
| [SpargeAttention](../papers/2025-zhang-spargeattention.md) | Live block prediction plus a later softmax-aware filter | Quantized implementation already exists; charge preparation |
| [NSA](../papers/2025-yuan-native-sparse-attention.md) | Compressed context, selected blocks, local window | Native model training, not an interchangeable post-training baseline |
| [GSRS](../papers/2026-dai-growing-sparsity-reduced-search.md) | Step-dependent Top-p with candidate reuse | Early search and retained state; persistence is empirical |

The generic combination of quantization and sparse attention is established.
A proposed policy needs a more specific contribution and matched baselines.

For a systolic target, count **issued physical blocks** in both QK and PV,
including partial occupancy. A token mask may save no array work if every
physical block retains something. Include index generation, gather/reordering,
mask storage, selection latency, and any dense fallback.

A proposed ablation uses dense BF16, dense low precision, sparse BF16, and
sparse low precision under the same full-model quality requirement.
First freeze a common mask to isolate arithmetic error; then run the live
selector on the altered trajectory. Quantization can change rankings and
therefore the selected computation. Measure this interaction rather than
assuming the two approximations are independent.

## Diffusion accelerator comparisons

Supplement reviewed **2026-11-14** from original methods, with one explicit
full-text dependency.

| Source | Existing combination | Required comparison distinction |
|---|---|---|
| [Ditto](../papers/2025-kim-ditto.md) | Width classification and zero skipping on differences | History, encoder, reordering, reconstruction |
| [SQ-DM](../papers/2025-fan-sq-dm.md) | Prepared precision and live channel routing | ReLU replacement/fine-tuning versus unchanged checkpoint |
| [EXION](../papers/2025-heo-exion.md) | Output reuse/prediction and compaction | An omitted output is not a zero input |
| [Cambricon-D](../papers/2024-kong-cambricon-d.md) | Differential dataflow | Full-text details pending |

The generic idea of one hardware observation supporting precision and skipping
already has relevant prior art. Compare a specific new policy at matched
hardware resources and full-model quality. Include dense refresh and metadata;
do not credit checkpoint modifications to the runtime selector.

## Packing, compression, and actual skipped work

Supplement reviewed **2026-11-14**.

- [Column combining](../papers/2019-kung-column-combining.md) improves systolic occupancy through prepared weight packing and model changes.
- [Dual-side Sparse Tensor Core](../papers/2021-wang-dual-side-sparse-tensor-core.md) pairs sparse operands with bitmap lowering and outer-product execution.
- [Compressing DMA](../papers/2018-rhu-compressing-dma.md) reduces traffic on a particular transfer path, without by itself changing array cycles.

Keep these benefits separate in a runtime activation experiment. Account for
packing/index generation, order restoration, metadata, additional source reads,
and the supported sparse operand/dimension. A smaller stored tensor, fewer
useful MACs, and fewer issued physical blocks are three different observations.

Compare prepared weight mechanisms as baselines while keeping weights fixed
for the proposed activation-only policy. Do not silently charge their model
changes to one system and omit them from another.

## Search record

Web searches on **2026-11-08** covered post-training sparsity-aware
quantization, Panacea, SCNN, and Sparseloop, with reference chaining to the
already reviewed systolic and online-decomposition papers. Full-text focus:
representation, mask generation, accumulation, and cost boundaries.
The review is targeted and does not cover every structured-sparsity proposal.

## Runtime sparsity beyond numerical zeros

Supplement reviewed **2026-11-22**. Keep three opportunities distinct:
thresholding activations, omitting selected attention interactions, and reusing
prior outputs instead of recomputing them. Each changes a different computation.

[Activation Concentration](../papers/2026-yang-activation-concentration.md)
compares scalar and column inactivity under a particular FFN-Reuse mapping.
Its column constraint must not be generalized to every systolic design.
[Phantom](../papers/2026-fu-phantom.md) instead compacts selected temporal updates
into dense work; [DiSC](../papers/2026-yoon-disc.md) co-designs reuse and sparse
attention with bank distribution. Packing and memory scheduling are therefore
existing research mechanisms, not automatic novelty.

Joint precision/pruning also has specific comparators:
[APT](../papers/2026-yoo-apt.md) uses runtime attention masks with prepared
threshold statistics; [DSTAR](../papers/2026-zhang-dstar.md) combines live
differential precision with prepared attention masks and temporal reuse.
Neither can be classified as entirely offline or entirely preparation-free.

Measure avoided arithmetic switching, issued cycles and storage/transfer
changes separately. Gating need not reduce cycles; compaction can reduce work
but add selection, gathering and utilization costs. Report full-model quality,
including the changed diffusion trajectory. Percentage scalar sparsity alone
establishes none of these benefits.

## Concrete combined-method comparators

Supplement reviewed **2026-11-22** from the stated method sections.

| Method | Combination already present | Boundary to preserve |
|---|---|---|
| [DIP](../papers/2025-federici-dip.md) | Live pruning scores modified by cache residency | Flash/DRAM-limited decoding; optional adaptation |
| [Chipmunk](../papers/2025-silveria-chipmunk.md) | Shared token-chunk masks, temporal deltas, dense packing | Stored history; MLP selection includes a smaller matrix product |
| [RT-Lynx](../papers/2026-cong-rt-lynx.md) | N:M activation pruning, norm compensation, LoRA and fusion | Correction work and training are part of the complete method |
| [WiSparse](../papers/2026-chen-wisparse.md) | Live weight-aware masks and mixed sparsity allocation | Calibrated exponents/thresholds; mixed granularity means block/layer allocation |
| [Prox](../papers/2026-liu-prox.md) | Quantized proxy selection and sparse exact recomputation | Extra proxy products, stored weights and calibrated thresholds |

Do not equate training-free with calibration-free, or a shared mask across
projections with a shared mask across token rows. Neither the generic
combination nor memory awareness alone establishes novelty.

For interacting techniques, compare each alone, both application orders,
and a jointly selected version on the same supported hardware actions and
full-model quality targets. Include an optimized fixed combined policy.
This distinguishes a combination benefit from the benefit of one component,
extra preparation, correction work or an unsupported execution mode.

## Signed geometry and assignment comparisons

Supplement reviewed **2026-11-22**.

| Source | Existing mechanism | Scope distinction |
|---|---|---|
| [VR-SparseQuant](../papers/2026-khaki-vr-sparsequant.md) | Quantization-error gains select sparse contributions | Local reconstruction objective; prepared scale ratio |
| [WAS](../papers/2025-wang-was.md) | Receiving-weight norm scores activation importance | Prepared allocation and thresholds |
| [RoShift](../papers/2026-song-roshift.md) | Weight geometry informs activation sparsification | Prepared rotations and runtime corrections |
| [SparseSwaps](../papers/2025-zimmer-sparseswaps.md) | Gram-based quadratic mask refinement | Calibration inputs and prepared parameter masks |

Output-error objectives and pairwise quadratic interactions are established
mathematics. A bounded runtime activation mechanism still needs an exact
preparation/execution comparison; changing which operand is pruned is not a
novelty proof. A group-local objective also omits interactions between groups.
