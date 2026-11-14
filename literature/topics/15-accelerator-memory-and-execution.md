# 15 — Modern neural accelerator memory hierarchies and matrix/vector execution

Reviewed: **2026-11-14**. Initial targeted review of primary papers and official
documentation. TPU is the central production reference; Trainium2, Blackwell
SM100, and Gemmini provide bounded comparisons. This is not an exhaustive
survey of current products or a ranking of accelerator efficiency.

## Scope

Follow tensors through device memory, local operand storage, finite matrix
operations, partial sums, result storage, vector operations, and writeback.
[Topic 02](02-matrix-multiplier-architectures.md) compares multiplier designs;
this topic examines the surrounding execution system. Convolution lowering
and inter-operator fusion remain in [03](03-im2col-and-convolution-mapping.md)
and [11](11-operator-fusion-and-streaming.md).

## Evidence and architectural comparison

| Reference | Documented organization | Consequence for matrix execution |
|---|---|---|
| [TPU v1](../papers/2017-jouppi-tpu.md), [TPUv4i](../papers/2021-jouppi-tpuv4i.md) | Historical production inference systems | Anchor generation-specific workload and utilization comparisons. |
| [TPU v4](../papers/2023-jouppi-tpu-v4.md) | Per TensorCore: four 128x128 MXUs and 16 MiB VMEM; two TensorCores share 128 MiB CMEM | Local and shared storage are distinct; extra matrix throughput does not remove memory constraints. |
| [Current TPU documentation](../papers/2026-google-tpu-architecture.md) | Matrix, vector, and scalar units; generation-dependent MXUs and memory hierarchy | Keep per-core/chip units and supported formats explicit. |
| [Pallas TPU](../papers/2026-jax-tpu-pipelining.md) | HBM/SRAM transfers, semaphores, persistent scratch, multiple buffering | Allocation and overlap constrain usable working space. |
| [Trainium2](../papers/2026-aws-trainium2-architecture.md) | Per NeuronCore-v3: 28 MiB SBUF, 2 MiB PSUM; distinct transfer paths | Operand and partial-sum storage impose different constraints. |
| [Blackwell SM100](../papers/2026-nvidia-blackwell-tensor-memory.md) | TMEM accumulators, register epilogues, shared-memory staging | Result handling competes with operand-pipeline resources. |
| [Gemmini](../papers/2021-genc-gemmini.md) | Configurable scratchpads, accumulator memory, DMA, and system integration | An inspectable reference for separating array and system effects. |

The comparison is qualitative. Buffer names do not imply equivalent placement,
port counts, bandwidth, or accessibility. Shared memory and dedicated result
memory need not be interchangeable. TPU v4's optical interconnect is not a
photonic matrix multiplier.

## Capacity, bandwidth, and finite operations

The following are analytical bookkeeping requirements, not measured results.
For a conventional blocked GEMM with resident A[M,K], B[K,N], and C[M,N],
a first payload estimate in bytes is:

```text
B_A = M*K*bytes_A
B_B = K*N*bytes_B
B_C = M*N*bytes_accumulator
```

Apply each term to the memory that actually holds it. Add pipeline copies,
scales, metadata, alignment, live residuals, and statistics scratch. A wide
accumulator can dominate result storage even when inputs use fewer bits.
Streaming or retaining a stationary operand changes the residency assumption.

Capacity only establishes whether a mapping can fit. Sustained execution also
depends on banking, bytes per cycle, DMA transaction shape, load overlap,
array fill/drain, and output evacuation. Distinguish physical PE dimensions,
instruction tile limits, and software blocking: Trainium2's double-FP8 mode
is a concrete example of different logical and physical dimensions.

## Matrix outputs are inputs to vector computation

The published TPU and SM100 paths demonstrate that matrix results feed other
compute units. The following numerical implications are deductions:

- For affine activation quantization, a code q represents `x_hat = s*(q-z)`.
  A consumer must receive this interpretation or a mathematically equivalent
  implementation; treating the code as the original floating-point value is wrong.
- Dequantization restores units, not information lost through rounding or clipping.
  Vector operations therefore consume an approximation of the original result.
- Partial products from differently scaled K groups require valid scale alignment
  before addition. Wider accumulation does not automatically resolve that issue.
- Softmax, normalization, and residual addition impose their own range, reduction,
  and scale requirements. Moving a scale across an operation needs justification.
- Lossless packing changes layout without necessarily changing values. Arithmetic
  quantization changes values; separate these effects in a representation contract.
- In-place conversion of shared storage affects other consumers. A separate copy
  preserves their input but consumes capacity, transfers, and synchronization.

An appropriate tensor contract records format, layout, scale/zero point, grouping,
ownership, and completion state at every producer-consumer boundary.

## Where runtime statistics and conversion can be placed

Compare collection during transfer, in local operand storage, during result
production, or in vector processing. These placements observe different values
and save different transfers. Conversion after an uncompressed transfer cannot
retroactively reduce its bytes. A maximum over an entire group is available
only after that group has been observed; buffering, replay, or prediction must
be accounted for. Dedicated collection logic and a vector-unit reduction also
have different resource costs. These are architectural constraints, not evidence
of a new adaptation algorithm.

## Search record and limitations

Web search on **2026-11-14** covered official TPU architecture/generation pages,
Pallas memory and pipelining, Trainium NKI architecture, Blackwell accumulator
transport, and the original TPU v4 paper. Five new canonical source notes
record focused reading; earlier TPU and Gemmini notes are reused.

Living documentation is dated by access; AWS and CUTLASS links pin documentation
versions. The Google/JAX notes flag inconsistent format or MAC-count reporting
instead of silently combining it into a specification. Neither marketing peak
rates nor training-system results establish inference joules per task.

Coverage is bounded to documented mechanisms, not every available generation.
No inference experiment, kernel implementation, simulator change, or new PhD
novelty claim is part of this review.
