# 01 — Energy of compute-bound versus memory-bound inference

Reviewed: **2026-11-08**. Scope: targeted literature review, including public
preprints available by this date. Evidence base: **17 papers**, with focused
reading of their full texts. No new hardware or model experiments were run.

## Research question and current answer

When does inference energy come primarily from arithmetic, data movement, or
execution overhead, and which of those costs can hardware-driven activation
adaptation actually reduce?

**A performance bottleneck and an energy breakdown answer different questions.**
The reviewed literature does not establish a universal energy ratio between
compute-bound and memory-bound networks. Such a ratio needs a defined workload,
hardware, operating point, quality requirement, and accounting boundary.

Our target remains compute-intensive inference on hardware centered on systolic
arrays. This review supports that target as a workload-selection criterion,
while requiring evidence of the energy costs that a proposed mechanism changes.

## 1. Define the comparison before drawing conclusions

For each result, specify:

- **Work:** model/checkpoint, operator or full network, input shape, batch,
  output length/resolution, and iterative steps.
- **Execution:** physical hardware, supported arithmetic mode, software version,
  mapping, fusion, and degree of parallelism.
- **Constraints:** task quality, latency or throughput target, and memory capacity.
- **Boundary:** MAC datapath, array including local buffers, accelerator chip,
  board/module, or whole system.
- **Accounting:** total joules per completed task or incremental energy above a
  stated idle baseline; steady-state service or individual request.

A compute-bound label is specific to these conditions. Bandwidth limitation,
memory-capacity limitation, host/launch overhead, and poor physical utilization
must be distinguished. A kernel far below both roofline ceilings has not thereby
been proven compute-bound.

[Roofline](../papers/2009-williams-roofline.md) supplies a throughput bound.
[TPU measurements](../papers/2017-jouppi-tpu.md) demonstrate hardware-dependent
workload behavior; the [recent edge study](../papers/2026-bonazzi-tinyml-memory-wall.md)
shows why a model family's arithmetic count alone is insufficient.

## 2. Performance and energy require different models

The following equations are this review's analytical framework, informed by
[Roofline](../papers/2009-williams-roofline.md),
[energy-roofline work](../papers/2018-ghane-energy-roofline.md), and
[action-based accelerator modeling](../papers/2019-wu-accelergy.md).
They are not a fitted model of our chip.

Let F be useful arithmetic operations, D_l bytes crossing memory boundary l,
B_l its sustainable bandwidth, and C the sustainable arithmetic ceiling for
the chosen shape and mode. A simplified lower bound is:

```text
T >= max(F / C, D_1 / B_1, ..., D_L / B_L)
I_l = F / D_l
```

This assumes adequate overlap and excludes additional latency/control bounds.
Real fixed-size execution may perform padded work; compute-time estimation must
use the actual issued workload and utilization, not useful F alone.

Energy instead needs action accounting:

```text
E_total = sum_a(N_a * e_a) + integral(P_background(t), dt)
```

Actions a include multiplication, accumulation, buffer reads/writes, transfers,
conversion, range detection, metadata processing, and mode changes. The action
cost e_a depends on precision, component implementation, operating point, and
potentially operand activity. Define action and background terms to avoid
counting clock or leakage costs twice.

For a deliberately simplified single-memory model:

```text
E / F = e_op + e_byte / I + P_background / (F / T)
Performance crossover: I_P = C / B
Arithmetic/memory dynamic-energy crossover: I_E = e_byte / e_op
```

Both crossovers have units of operations per byte, but depend on different
parameters. If I_P < I_E, there can be a compute-bound region in which memory
still consumes more dynamic energy than arithmetic. This is a conditional
deduction, not a measured claim about every accelerator.

The [Timeloop paper](../papers/2019-parashar-timeloop.md) offers a way to derive
mapping-dependent action counts. It does not remove the need to characterize
a new controller or account for stalls outside its assumptions.

## 3. What the selected evidence actually supports

Numerical results below retain their original boundaries. They are not
cross-paper hardware rankings.

| Source | Evidence and conditions | Relevant result | Interpretation limit |
|---|---|---|---|
| [Eyeriss, 2016](../papers/2016-chen-eyeriss.md) | Matched-resource CNN dataflow analysis | Row-stationary convolution energy efficiency improves 1.4–2.5× over evaluated alternatives | Data reuse matters; ratios are mapping-specific |
| [TPU, 2017](../papers/2017-jouppi-tpu.md) | Production inference, hardware counters | Different limits for evaluated MLP/LSTM and CNN workloads | Workload/hardware classification, not a universal family label |
| [TPUv4i, 2021](../papers/2021-jouppi-tpuv4i.md) | Production architecture plus component estimates | Arithmetic, wiring, and storage scale unequally | Performance/TDP and component costs are not measured task energy |
| [S2TA, 2022](../papers/2022-liu-s2ta.md) | Implemented-design estimates, INT8 baseline | MAC datapath is about 20% in its reported breakdown | Buffer costs restrict arithmetic-only savings |
| [Splitwise, 2024](../papers/2024-patel-splitwise.md) | Phase/power-cap characterization | Decode tolerates a large cap reduction in the tested case | Cap settings do not equal actual power |
| [Input-dependent power, 2024](../papers/2024-gregersen-input-dependent-power.md) | Fixed-shape, repeated A100 GEMMs | Operand patterns affect power despite similar runtime | Synthetic activity is not validated full-model savings |
| [ViDiT-Q, 2025](../papers/2025-zhao-vidit-q.md) | Diffusion quality, memory, latency | Narrower stored weights do not necessarily accelerate the arithmetic path | No direct energy measurement |
| [ML.ENERGY, 2025](../papers/2025-chung-ml-energy-benchmark.md) | GPU service measurements | Batch and accounting choices affect measured request energy | GPU boundary excludes host/platform components |
| [Where Do the Joules Go?, 2026](../papers/2026-chung-where-joules-go.md) | H100/B200 serving study | FP8 loses energy comparisons at small batches in a reported subset | Software/precision changes are not isolated circuit effects |
| [Mobile NPU study, 2026](../papers/2026-cai-mobile-npu-efficiency.md) | CPU/GPU/NPU phases and telemetry | Host scheduling and invocation affect accelerator-backed inference | Backend attribution is not an internal datapath split |
| [TinyML memory wall, 2026](../papers/2026-bonazzi-tinyml-memory-wall.md) | Edge CNN measurements and traffic fits | Idle subtraction can change energy rankings | Small-sample correlations and differing measurement domains |

Two additional foundations matter:
[Horowitz](../papers/2014-horowitz-computing-energy.md) explains component and
locality costs, while [sensor characterization](../papers/2024-yang-power-measurements.md)
requires checking how energy observations are obtained. Historical operation
tables must not be substituted for current hardware characterization.

## 4. Consequences for hardware-driven activation adaptation

### Identify where the representation actually changes

If activations remain BF16 in external memory and are quantized only during
array loading, that operation cannot retroactively reduce their external-memory
traffic. Savings can begin in downstream buffers, links, and arithmetic that
actually consume the narrower representation. Additional reads or buffering
needed to determine the scale must also be counted.

This is an architectural accounting deduction. It makes the conversion point,
reuse lifetime, physical storage width, and scale-metadata path essential inputs
to future experiments.

### Bound savings before choosing an algorithm

Let f be the fraction of baseline energy affected by a mechanism and r its
fractional reduction. With unchanged runtime and other components, the ideal
whole-boundary saving is f*r, before adaptation overhead.

For illustration only, a 50% reduction of a component contributing 20% would
save at most 10% of that boundary's energy. The S2TA breakdown motivates this
calculation; it does not supply our chip's f. Runtime changes additionally alter
background energy, so the fixed-time assumption must be removed in the full model.

### Distinguish electrical savings from execution savings

Reduced switching, clock-gating, skipped issued work, and increased arithmetic
throughput are distinct mechanisms. An all-zero operand does not automatically
shorten a dense systolic operation. A narrower format does not automatically
increase throughput unless the hardware mode supports it.

Fixed-size submatrices, padding, fill/drain behavior, and operand reuse constrain
which savings can occur. We need useful work, issued work, active cycles, and
transferred bytes as separate quantities.

### Recompute the bottleneck after optimization

A faster arithmetic path can expose operand-delivery limits. Added measurement,
conversion, or correction can create a new critical path. End-to-end energy must
include operators that remain unchanged.

Because E = average_power * T, a lower-power implementation can still consume
more energy if it runs sufficiently longer. Conversely, faster execution can
reduce energy despite higher instantaneous power. These are accounting
identities, not predictions that either behavior must occur.

## 5. A practical comparison for the first research experiments

This is a proposed evaluation design, not an implemented benchmark or a claim
of novelty.

1. **Start with controlled matrix shapes.** On a fixed hardware model, vary
   reuse and shape to cover arithmetic-limited, bandwidth-limited, and
   underutilized execution. Include complete and partial physical tiles.
2. **Separate the interventions.** Compare baseline execution, statistics-only
   collection, actual quantization, and the complete adaptive policy. Include
   scale traffic, conversion, correction/fallback, and extra passes.
3. **Collect an energy ledger.** Count arithmetic and accumulation actions,
   physical buffer accesses, transfers at each boundary, and control actions.
   Vary uncertain energy coefficients instead of importing a single old table.
4. **Return to complete networks.** Profile representative operators and phases
   from multiple domains. Classify measured configurations rather than selecting
   them solely because they are CNNs, transformers, or diffusion models.
5. **Validate final task quality.** Changed activations must participate in
   forward computation and affect later layers/steps. Fixed weights, inputs,
   quality thresholds, and generation settings make comparisons interpretable.
6. **Validate hardware costs progressively.** Use portable numerical experiments
   and explicit action models first. Final simulator work should test the
   selected mechanism's timing, buffering, and control assumptions.

For compute-intensive workloads, activation adaptation can target several costs
at once: datapath activity, operand transport, storage, and execution duration.
Which dominates remains an empirical question.

## 6. Measurement and reporting requirements

Report joules per completed inference/task, latency, throughput, average power,
quality, and the accounting boundary together. State whether results are
measured, estimated, or analytically derived.

For physical measurements, document warm-up, synchronization, repetitions,
thermal state, clocks/power limits, telemetry version, and sensor/counter
semantics. Polling faster does not guarantee finer underlying observations.
Report variation; apparent gains below uncertainty need further validation.

Report total energy as the primary cost at a declared boundary. If incremental
energy is useful, give it separately:

```text
E_incremental = E_total - P_idle * T
```

A matched idle baseline is an operational measurement, not a direct estimate of
transistor leakage. Subtracting it does not make board, rail, and chip
measurements interchangeable. Likewise, concurrent-request energy attribution
must state its allocation rule.

## 7. What remains unresolved

- This corpus does not provide a controlled, portable multiplier/SRAM/NoC/DRAM
  decomposition across matched compute-bound and memory-bound inference
  configurations on our target hardware.
- It does not establish the fraction of energy removable by our proposed
  activation adaptation, or its detector/converter break-even point.
- GPU telemetry, RTL-based estimates, and mobile backend measurements provide
  complementary evidence; none alone determines our array's energy breakdown.
- A missing result in this targeted corpus is not proof of an unresearched
  field. Any candidate contribution needs a separate, updated novelty search.

## Search record and coverage limits

Search date: **2026-11-08**. Web discovery preceded drafting. Primary papers were
located through arXiv, author/project sites, publisher metadata, and reference
chaining. PDFs were accessed for focused reading; no third-party summaries were
used as evidence for the conclusions.

Representative query families:

- `compute bound memory bound inference energy measurement NPU GPU`
- `Roofline energy model GPUs`
- `Eyeriss dataflow energy`, `TPU inference roofline power`
- `Timeloop Accelergy action energy`
- `ViDiT-Q compute-bound`, `Splitwise power prefill decode`
- `ML.ENERGY inference benchmark`, `Where Do the Joules Go`
- `NVIDIA power sensor sampling measurement`
- `2026 mobile NPU inference energy`, `TinyML memory wall`

Included: sources contributing bottleneck definitions, component accounting,
inference measurements, or measurement validation. Retained older foundations
alongside recent evidence; training-only and unrelated deployment reports were
not used to answer the inference comparison.

Screened but not incorporated as detailed evidence in this pass:
[Is INT8 Portable?](https://arxiv.org/abs/2609.16085) and
[De-Quantization Penalties](https://ieeexplore.ieee.org/abstract/document/11368735).
Their detailed numerical/quality implications require full-text assessment.

This is a targeted review, not an exhaustive systematic search. Selection is
English-language and public-access biased; GPU serving evidence is richer here
than internal energy decompositions of current inference ASICs. Recent preprints
may change. Historical workspace reviews supplied search leads only; their
old scope exclusions and novelty verdicts were not adopted.
