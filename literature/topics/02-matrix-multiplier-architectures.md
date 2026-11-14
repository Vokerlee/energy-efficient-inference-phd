# 02 — Systolic-array architectures and alternative matrix multipliers

Reviewed: **2026-11-08**. Targeted primary-source review. Systolic arrays are
the central target; alternatives test the limits and portability of our ideas.
Seven new paper notes complement the shared evidence from topic 01.

## Main finding

The useful comparison is not simply “systolic versus other.” Physical
connectivity, reduction organization, dataflow, arithmetic format, and
programmability are partly independent choices. Inner/outer-product scheduling
does not, by itself, specify a physical architecture.

[Kung](../papers/1982-kung-systolic-architectures.md) establishes the locality
rationale. [TPU](../papers/2017-jouppi-tpu.md) and
[Gemmini](../papers/2021-genc-gemmini.md) supply concrete systolic examples.
[Timeloop](../papers/2019-parashar-timeloop.md) separates architecture from mapping.

## Comparison relevant to this research

This table synthesizes architectural trade-offs; its qualitative assessments
are not measured rankings under identical implementation constraints.

| Organization | Potential advantage | Cost or limitation to investigate | Relevance to adaptive activations |
|---|---|---|---|
| Regular systolic forwarding | Local reuse and regular schedules | Shape mismatch, delivery limits, pipeline overhead | Preserve regular flow; charge for scales and exceptions |
| Parallel vector/dot-product units | Programmable decomposition and short-vector execution | Repeated operand delivery and reduction/storage costs | A portable reference/comparison backend |
| Specialized multiply–reduce pipeline | Explicit staged arithmetic and reduction | Fixed reduction shape and buffer requirements | Compare accumulation and conversion placement |
| Configurable distribution/reduction networks | More flexible partitioning and irregular work | Switches, wiring, control, and area | Can absorb irregular outlier/sparse paths at a cost |
| Sparse product/merge engines | Avoid work on absent entries | Index traversal, intermediate products, merging | Requires a compatible sparse representation and workload |

Evidence anchors: [DianNao](../papers/2014-chen-diannao.md) for staged reduction,
[MAERI](../papers/2018-kwon-maeri.md) and [SIGMA](../papers/2020-qin-sigma.md)
for flexible networks, [Flexagon](../papers/2023-munoz-martinez-flexagon.md)
for sparse traversal. These are overlapping design dimensions, not an exhaustive,
mutually exclusive taxonomy.

[Eyeriss v2](../papers/2019-chen-eyeriss-v2.md) adds a particularly useful lesson:
operand-delivery flexibility and arithmetic utilization must be assessed together.

## Fixed-size operations: what our model must represent

A logical multiplication A[M,K] B[K,N] exceeds the device operation in general.
Record per hardware mode:

- physical output dimensions R and C;
- supported reduction grouping and whether K streams or must be padded;
- operand, accumulator, and output formats;
- fill/drain and inter-block overlap rules;
- buffer capacity, banking, bandwidth, and supported reuse.

For a dense rectangular mapping that pads only M and N, the following
**derived spatial occupancy bound** is useful:

```text
U_spatial = M*N / ((ceil(M/R)*R) * (ceil(N/C)*C))
```

It excludes time, K behavior, sparsity, and communication. It is not total
utilization. A single long streaming reduction and many short independent
reductions can have different overhead even with equal useful MAC counts.

The example modes discussed in this project—128×128 BF16 and 256×256 FP8—are
illustrative target constraints, not specifications of every accelerator.
Mode-dependent shapes may change occupancy and delivery requirements as well
as arithmetic cost. Their throughput/energy ratio must be established.

## Where adaptivity fits

**At loading:** statistics and conversion may share an operand-delivery path,
but complete-block statistics require access to the relevant values before use.
Charge for storage, a prepass, replay, or conservative prediction.

**Inside the array:** per-element precision or exceptions can conflict with a
regular mode shared across a tile. Examine whether an outlier path stalls,
replays, or runs independently.

**At reduction boundaries:** separately scaled K blocks require valid partial-sum
alignment. A scale common to a tile is not automatically common to every
reduction operand.

**Across operations:** an efficient mode for one layer may require expensive
repacking before the next. Include transitions in the full-network result.

These are research deductions from the hardware constraints, not proposed
contributions already validated by the cited papers.

## Comparisons worth carrying into portable experiments

1. Keep a regular dense systolic baseline and the same buffer/bandwidth budget.
2. Compare numerical policies with identical execution mapping first.
3. Then permit mapping or packing changes and attribute their additional benefit.
4. Add a flexible-reduction comparator only when the selected mechanism requires
   irregular work; include routing, metadata, and reduction costs.
5. Preserve complete-model quality and the energy accounting from topic 01.

[S2TA](../papers/2022-liu-s2ta.md) is relevant when structured work can retain
regularity; [TPUv4i](../papers/2021-jouppi-tpuv4i.md) illustrates that real
matrix engines operate inside a larger memory and control system.

## Evidence limits and search record

Web searches on **2026-11-08** covered “Why Systolic Architectures,” “MAERI,”
“SIGMA sparse irregular GEMM,” “Gemmini full-stack,” “Eyeriss v2,” “DianNao,”
and “Flexagon.” Sources were original papers on author/university sites and
versioned arXiv records. Reading focused on datapaths, interconnects, mappings,
and evaluation boundaries; the scanned Kung source was inspected visually.

The alternative-architecture subset is deliberately bounded. SIGMA is primarily
training-oriented; Flexagon targets sparse-sparse multiplication. Their
mechanisms inform comparisons, while their headline results do not directly
establish inference-energy gains. Analog/in-memory and optical designs need a
separate scope decision before extending this comparison.

No experiment was run and no architecture or novelty claim was selected.

## Sparse packing and operand delivery comparisons

Supplement reviewed **2026-11-14**. [Column combining](../papers/2019-kung-column-combining.md)
packs prepared filters for systolic execution, with conflict pruning and
retraining. [Dual-side Sparse Tensor Core](../papers/2021-wang-dual-side-sparse-tensor-core.md)
uses bitmap operands and an outer-product primitive. They expose different
trade-offs in regularity, routing, and preparation.

[Compressing DMA](../papers/2018-rhu-compressing-dma.md) changes a transfer
path, not the array's issued computation. Include feeder and transfer costs
when comparing architectures. Systolic arrays remain central: these sources
supply packing precedents and alternative delivery/reduction comparisons,
not a reason to assume our array has their sparse capabilities.

## Encoding and gating within the same array

Supplement reviewed **2026-11-14**. [Peltekis et al.](../papers/2023-peltekis-systolic-bus-invert.md)
encode selected BF16 fields and gate zero-valued activation work.
[Bamberg et al.](../papers/2023-bamberg-neural-statistics-coding.md)
separate physical bit coding from integer and real-value interpretation.

These mechanisms can change energy without changing the matrix algorithm.
Place encoders/decoders at explicit boundaries and verify that arithmetic
receives the intended values. If arithmetic consumes an encoded representation
directly, its datapath and correction logic must implement that contract.

Zero gating and compaction are different: retaining an empty scheduled slot
may save switching while leaving latency unchanged. Compare both within the
same physical resources before attributing a throughput gain to sparsity.
