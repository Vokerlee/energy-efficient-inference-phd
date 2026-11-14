# 03 — Efficient hardware im2col and convolution mapping

Reviewed: **2026-11-08**. Targeted review of six additional primary papers,
shared architecture sources, and official implementation documentation.
The goal is to identify efficient alternatives under stated conditions.

## Current conclusion

There is no established implementation that is best for all convolution shapes,
memory systems, and array modes. For our systolic focus, the strongest starting
comparisons are explicit lowering, bounded/tiled lowering, and late streaming
generation with reuse. Quantization belongs in this same comparison because its
placement changes reuse, statistics, and representation lifetime.

## Approaches and trade-offs

| Approach | Materialized data | Main opportunity | Main cost or restriction |
|---|---|---|---|
| Full explicit im2col | Expanded windows | Simple dense GEMM baseline | Copy traffic and storage |
| Compact/partial lowering | Smaller intermediate | Limit expansion and working set | More/smaller GEMMs and setup |
| Indirect convolution | Addresses rather than copied values | Reuse original activation storage | Pointer traffic and specialized kernel |
| Implicit GEMM | Construct operand tiles during loads | Avoid a full expanded matrix | Address generation and load/reuse scheduling |
| Streaming hardware feeder | Local line/patch state | Reuse overlapping windows near the array | Buffering, banking, and supported patterns |
| Direct convolution mapping | Original tensor plus local reuse | Avoid general lowering overhead | Different mapping/dataflow requirements |

Evidence: [MEC](../papers/2017-cho-mec.md),
[Indirect Convolution](../papers/2019-dukhan-indirect-convolution.md),
[SPOTS](../papers/2022-soltaniyeh-spots.md),
[late IM2COL](../papers/2020-liu-sparse-systolic-tensor-array.md), and
[Fornt et al.](../papers/2023-fornt-on-the-fly-im2col.md).
NVIDIA's [CUTLASS convolution documentation](https://docs.nvidia.com/cutlass/latest/media/docs/cpp/implicit_gemm_convolution.html)
describes constructing implicit-GEMM tiles during loading; it is implementation
documentation, not evidence of an energy ranking against an ASIC feeder.

[Gemmini](../papers/2021-genc-gemmini.md) supplies a full-system context.
“On-chip im2col” is insufficient detail: identify whether expansion happens
before or after the storage/bandwidth boundary we intend to optimize.

## Window length and fixed-size hardware

For conventional grouped convolution, a logical reduction contains:

```text
K = kernel_height * kernel_width * (input_channels / groups)
M = batch * output_height * output_width
N = output_channels / groups       # per-group GEMM
```

These are algebraic dimensions; layout may transpose them.

A 3×3 or 5×5 spatial window has 9 or 25 values **per input channel**.
Depthwise reductions can therefore be short. Your hardware can also process
channel-wise windows in short vectors and accumulate channels separately.
The review must preserve that actual mapping rather than assume a full
multi-channel window fits one operation.

Unused positions can arise from:

- image-boundary padding;
- short vectors packed into wider physical slots;
- grouping represented through block-diagonal matrices;
- numerical zeros in real activations;
- zeros introduced by quantization or pruning.

These have different causes and exploitable granularities. Dilation changes
sample coordinates; it does not require physically inserting zeros in the input
stream. A dense block-diagonal embedding can create substantial artificial work
that a group-aware mapping avoids.

[FuSeConv](../papers/2021-selvam-fuseconv.md) demonstrates the mapping problem,
but changes the operator and training. It is not an interchangeable exact
convolution baseline.

## Quantize before or after generating windows?

This is a proposed comparison derived from the reviewed mechanisms.

**Before expansion:** quantize a source activation once and reuse it in multiple
windows. Benefits depend on shared compatible scales, retained representation,
and the position of the quantizer relative to storage. Coarse source groups may
lose precision compared with local window groups.

**After expansion:** choose scales for the actual consumer group. This can better
match window values, but may repeat statistics/conversion for overlapping inputs.
If scales differ by window, a single original value can acquire different
quantized approximations in its different uses.

**Joint generation and adaptation:** line/patch storage might support incremental
statistics or reuse of already converted values. A causal implementation must
account for when all required values arrive, eviction, replay, and scale changes.
This is a candidate investigation, not an established novelty claim.

For all placements, K-block scales must be reconciled during accumulation.
Different window packing must preserve outputs and group boundaries; reusing
statistics alone does not guarantee that the quantized computation is equivalent.

## Connections with sparsity

[SPOTS](../papers/2022-soltaniyeh-spots.md) already couples hardware lowering with
zero-block tags. [S2TA](../papers/2022-liu-s2ta.md) supplies a structured-sparsity
comparison. Our evaluation must count tag generation and the exact transfers or
issued operations avoided.

Deterministic padding can be recognized from coordinates. Data sparsity requires
inspection or trustworthy metadata. Neither a high element-zero fraction nor a
short kernel proves that an entire physical block can be skipped.

## How to identify the most efficient variant

Use one fixed array/memory budget and a sweep covering:

- 1×1, 3×3, 5×5, rectangular kernels, stride, dilation, and boundary-heavy inputs;
- standard, grouped, and depthwise convolutions;
- channel counts and output sizes around physical alignment boundaries;
- numerical precision, scale groups, and conversion placement.

For each variant collect source reads, expanded writes, local-buffer accesses,
address/control actions, scale/tag traffic, issued MACs, utilization, cycles,
and peak storage. Distinguish estimated energy from measured energy. Include
setup and scheduling costs for small workloads.

First verify exact mappings against convolution outputs. Then apply actual
quantization/sparsity interventions and evaluate complete-model quality.
Keep operator replacements and retraining in a separate experimental category.

The first portable prototype should compare a small number of these mappings;
chip-simulator programming remains final validation work.

## Search record and limits

Web searches on **2026-11-08** covered “hardware im2col,” “SPOTS,” “on-the-fly
im2col Fornt,” “Sparse Systolic Tensor Array,” “MEC convolution,” “Indirect
Convolution,” and “FuSeConv.” Full-text focus: lowering location, buffers,
reuse, supported patterns, and evaluation boundaries.

Recent/adjacent candidates needing further full-text assessment include
[p-im2col](https://ieeexplore.ieee.org/abstract/document/9650846) and
[OMEC](https://www.sciencedirect.com/science/article/pii/S1383762126002316).
Their search visibility is recorded without adopting their numerical claims.

No common-hardware experiment was performed. Cross-paper figures cannot
identify a global winner, and the combination of feeder reuse and adaptation
requires a dedicated novelty search before a PhD claim.

## Bitmap lowering and the sparse multiplier

Supplement reviewed **2026-11-14**. [Dual-side Sparse Tensor Core](../papers/2021-wang-dual-side-sparse-tensor-core.md)
performs im2col on bitmap structure and fetches corresponding nonzeros for an
outer-product-oriented consumer. It demonstrates that sparse lowering must
match the compute primitive and sparse format.

Its bitmap-lowering comparison is faster than the tested CSR alternative,
but does not make sparse lowering universally cheaper than dense lowering.
Compare the entire convolution path, including formation, metadata, index
work, traffic, and matrix execution at the actual activation pattern.

For quantized activations, regenerate the sparse representation at the stage
where zeros are defined, preserve zero-point semantics, and keep physical
padding separate. Short spatial windows do not by themselves establish either
compressibility or profitable sparse execution.
