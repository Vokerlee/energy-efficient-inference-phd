# 08 — Accumulation precision and block-scale arithmetic

Reviewed: **2026-11-08**. Four new focused sources, with shared microscaling,
vector-scaling, and energy evidence.

## Main finding

Operand quantization, exact integer partial sums, scale alignment, and final
accumulation are separate numerical stages.
[Block-FMA analysis](../papers/2020-blanchard-block-fma.md) motivates specifying
their actual semantics. [A2Q](../papers/2023-colbert-a2q.md) and
[A2Q+](../papers/2024-colbert-a2q-plus.md) establish constrained accumulation
methods, but rely on weight/training choices.

A narrow safe accumulator is therefore a candidate optimization, not an
automatic consequence of narrow inputs.

## Conservative integer bounds

For a block of K_b integer products with |a_i| <= A and |b_i| <= B:

```text
|sum_i a_i*b_i| <= K_b*A*B
```

A signed width w is sufficient if its positive limit covers that bound.
A tighter available bound is A*sum_i|b_i|, using known quantized weights.
These are elementary conservative deductions, not a new theorem or policy.

Include the actual signed ranges, bias, prior partial sum, asymmetric
zero-point corrections, and any fused residual. Bound intermediate values,
not just a final sum where cancellation happens to occur.

A block-local accumulator can be narrower than the complete reduction, but
this introduces another stage whose conversion/rescaling cost must be counted.

## Independently scaled K blocks

For one output element, a block-scaled multiplication has the form:

```text
c_hat = sum_b (sA_b * sB_b) * sum_i(qA_bi * qB_bi)
```

Scales may additionally depend on output row/column. Integer sums with different
scale products cannot simply be added as though they share one unit.

Choices include rescaling each partial result to floating point, aligning to
a shared integer domain, or retaining block exponents for later reduction.
Each changes rounding, storage, and hardware cost.
[VS-Quant](../papers/2021-dai-vs-quant.md) and
[MX](../papers/2023-rouhani-microscaling.md) provide representation baselines.

## Exactness claims need boundaries

FP32 can exactly represent integers within its consecutive-integer range, but
that fact alone does not make a scaled block reduction exact. Conversion,
non-power-of-two scales, overflow/underflow, and adding differently sized
partials can introduce error.

Likewise, a simulated FP32 sum does not reproduce a device's internal reduction
unless its ordering and rounding points match. Changing tile size or schedule
can change the numerical result even with the same operand formats.

The initial numerical reference must declare:

- product and accumulator formats;
- rounding/saturation/wraparound behavior;
- K-block length and partial-sum order;
- scale representation/application;
- bias, activation, and output-conversion placement.

## Hardware cost and possible adaptivity

[Microscaling reduction work](../papers/2025-cuyckens-mx-reduction.md)
demonstrates that reduction design deserves separate attention. Its component
results do not establish an array-wide percentage for our chip.

A future policy could use available activation bounds plus fixed weight
metadata to select an accumulator mode. It must know the bound before issuing
the affected work or retain a recovery path. Observed cancellation is not a
safe future bound.

Compare fixed wide accumulation, conservative bounded narrow accumulation,
and measured/predicted adaptive accumulation at equal operand quantization.
Then vary operand precision separately. This isolates benefits and errors.

## Required experiments

Use adversarial signed extremes, alternating signs, long reductions, abrupt
scale changes, and realistic activations. Compare overflow counts, numerical
error, and final task quality. Record alignment shifts, normalizations,
conversions, accumulator-buffer accesses, and fallback.

Quantization-aware retraining is a separate comparison category. Keep it out
of the primary fixed-weight activation experiment unless explicitly introduced.

## Additional accumulator and native-MX baselines

Supplement reviewed **2026-11-14**. The September report supplied discovery
leads; its numerical percentages and novelty verdicts are not imported.

| Source | Existing result | Transfer condition |
|---|---|---|
| [WrapNet](../papers/2021-ni-wrapnet.md) | Train for narrow wrap-around accumulation | Modified network/training, not exact unchanged inference |
| [Sakr et al.](../papers/2019-sakr-accumulation-width.md) | Model variance retention, chunking, and sparse reduction lengths | Statistical assumptions and training setting |
| [MXDOTP](../papers/2025-islamoglu-mxdotp.md) | Native scaled dot product with early accumulation | Wide internal representation and defined final rounding |
| [MX robotics hardware](../papers/2025-cuyckens-mx-robotics.md) | Precision-scalable arithmetic and component costs | Specified implementation and input activity |

A proposed runtime accumulator policy must distinguish three objectives:
exact bounded integer reduction, controlled floating-point information loss,
and task-tolerated approximation. A bound for one objective does not prove
another. Changing block length or skipping terms also changes reduction
semantics; a density-adjusted statistical estimate is not a worst-case bound.

Use the declared physical reduction order and scale alignment when testing
width changes. Compare conservative fixed width, a proven-bound mode where
applicable, and any approximate mode separately. Include promotion, state
transfer, and rounding costs, then evaluate full-model outputs.

Native MX support is an important baseline: comparison against repeated
software format conversion can exaggerate the headroom of a proposed
hardware policy. Component breakdowns motivate characterization; they do not
supply universal whole-array energy coefficients.

## Search and limits

Web searches on **2026-11-08** covered accumulator-aware quantization, A2Q+,
mixed-precision block FMA, and precision-scalable microscaling reduction.
Full-text focus: guarantees, arithmetic assumptions, and evaluation boundaries.

No dynamic accumulator algorithm or chip energy split has been established.
Safe widths, efficient variable-width hardware, and final-model quality all
require separate validation.
