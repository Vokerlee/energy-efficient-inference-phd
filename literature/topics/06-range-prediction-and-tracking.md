# 06 — Activation-range prediction and tracking

Reviewed: **2026-11-08**. Four new full-text focused notes, one pending
competitor record, and official scaling documentation.

## Established mechanisms and the open comparison

Prediction is already part of numerical-format research:
[Autoflex](../papers/2017-koster-flexpoint.md) uses bounded history;
[ScalePredictor](../papers/2026-li-scale-predictor.md) uses shallow features to
predict deeper scales. [MixQ](../papers/2024-chen-mixq.md) is an important
online-prediction competitor still awaiting full-text assessment here.

NVIDIA's [delayed-scaling documentation](https://docs.nvidia.com/deeplearning/transformer-engine/features/low_precision_training/fp8_delayed_scaling/fp8_delayed_scaling.html)
describes historical amax-based scaling and contrasts it with current scaling.
This is existing software/library practice, primarily documented for training;
it does not establish our desired autonomous inference controller.

The research question is narrower: can a cheap causal predictor replace enough
measurement/conversion overhead while preserving final inference quality on
fixed-size hardware?

## Candidate information sources

| Available information | Possible use | Limitation |
|---|---|---|
| Previous blocks of the same operator | Track changing range | Block order may lack correlation |
| Earlier observations of the same layer | Persistent estimate | Requests can change distribution |
| Producer/shallow-layer statistics | Predict later ranges | Predictor may need model-specific calibration |
| Known iteration or timestep | Condition a policy | Does not reveal future activations |
| Current values already buffered | Measure a range | Buffering/access is not free |

[FP8 formats](../papers/2022-micikevicius-fp8-formats.md) provide a
representation baseline. A scale's dynamic range, update rule, and observation
history are separate design choices.

## Causal execution contract

Let h_t contain only state available before block t is quantized:

```text
range_t = predict(h_t, available_side_information_t)
q_t = quantize(x_t, range_t)
h_(t+1) = update(h_t, observations_collected_from_x_t)
```

This is a proposed experimental contract. If observing all of x_t is needed to
choose range_t, the design must first buffer/scan it or label that measurement
as a different baseline.

Detecting overflow after casting does not recover information already lost.
A fallback requires the original values or a valid way to regenerate them;
include retention, replay, and downstream synchronization costs.

## Algorithms to compare

Start with previous maximum, a bounded rolling maximum, and exponential
smoothing. Then consider fast upward/slow downward updates, trend/headroom
estimates, fixed-bin tail counts, and a small learned predictor.

These are comparison candidates, not proposed novel algorithms. Quantile
summaries such as [t-digest](../papers/2019-dunning-t-digest.md) can serve as
software references, but should not be assumed cheap enough for a hardware
critical path.

For each method define state size, arithmetic width, updates per element/block,
initialization, reset conditions, and scale-change behavior. Quantized state
updates should be tested as part of the numerical algorithm.

## Evaluation that distinguishes useful prediction

Test steady distributions, abrupt transitions, rare large values, alternating
inputs, and realistic model sequences. Keep the deployment block order fixed.

Record:

- range underestimation and clipping, weighted by affected computation;
- excess headroom and lost effective precision;
- fallback/replay rate and physical overhead;
- state and detector traffic;
- complete-network task quality and energy estimates.

Prediction error alone is insufficient: an overestimate can avoid clipping but
still degrade precision, and a rare underestimate can have a disproportionate
effect. Compare against fixed calibration and fully charged current-block
measurement, not only an ideal oracle.

## Hardware and research limits

Per-layer or per-channel history is easier to describe than to provision:
count all live states and their access bandwidth. Reusing one prediction across
several physical operations changes decision granularity and needs evaluation.

No current source proves the best predictor for our chip or a novel smoothing
rule. Training-history mechanisms and model-specific image predictors are
transfer candidates, not inference guarantees.

## Search record

Web searches on **2026-11-08** covered ScalePredictor, MixQ online prediction,
Flexpoint/Autoflex, FP8 formats, streaming quantiles, and NVIDIA delayed/current
scaling. Full-text focus and pending status are recorded per paper.
The current official documentation was checked after an older URL failed.

This is a targeted review. MixQ full-text verification, broader nonstationary
streaming methods, and model-specific hardware cost evaluation remain open.
No prediction policy has been implemented or validated.
