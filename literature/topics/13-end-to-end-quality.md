# 13 — End-to-end quality under runtime approximation

Reviewed: **2026-11-09**. Five new full-text focused notes and shared
quantization/low-rank evidence. Web discovery began 2026-11-08.

## Main conclusion

A runtime intervention is valid only after the altered computation is evaluated
through the complete model and its task. Local tensor error remains diagnostic;
it is not the acceptance criterion.

[Q-Diffusion](../papers/2023-li-q-diffusion.md),
[PTQD](../papers/2023-he-ptqd.md), and
[Q-Drift](../papers/2026-ryu-q-drift.md) show several existing approaches to
trajectory-level numerical behavior. They also introduce different calibration
and correction mechanisms that must be separated in comparisons.

## What must actually change

Quantized/pruned/projected activations must feed the next computation.
In iterative generation, later states must arise from the modified trajectory.

Three experiments answer different questions:

1. observing original activations and estimating local errors offline;
2. executing the whole model with quantize/dequantize interventions;
3. executing the whole model with physical-block arithmetic and scale/rounding
   semantics emulated.

The first is exploratory statistics. The second tests operand approximation.
The third additionally tests the numerical contract intended for hardware.
An ordinary floating-point GEMM after fake quantization does not automatically
reproduce reduced accumulation, block rescaling, or a changed reduction order.

## Quality depends on the task

| Task | Primary comparison examples | Diagnostic complements |
|---|---|---|
| Classification/detection | Established dataset task metrics | Logit and activation error |
| Language/speech | Task accuracy, perplexity, word error as applicable | Layer/output distribution changes |
| Image generation | Distributional quality and prompt alignment | Paired perceptual/pixel differences |
| Video generation | Temporal, motion, and content dimensions | Per-frame and trajectory differences |

[FID](../papers/2017-heusel-frechet-inception-distance.md) compares feature
distributions; [VBench](../papers/2024-huang-vbench.md) illustrates why video
needs multiple dimensions. Neither provides a universal acceptance threshold.

Use established model/task evaluations rather than one metric imposed across
all domains. Vision and generation remain examples, not the engine's scope.

## Controlled comparisons

Pin the checkpoint, input preprocessing, dataset split, sampler/schedule,
guidance, seed policy, generation length/resolution, and evaluation code.

Separate calibration/development inputs from final held-out evaluation.
Tune policy thresholds on development data, then freeze them for comparison.
Specify meaningful quality tolerances before inspecting the final results.

For stochastic generation, paired seeds help interpret changes, but identical
pixels are not the task objective. Conversely, a few attractive examples cannot
establish preserved output distribution or temporal quality. Report sampling
variation and metric uncertainty.

## Error structure and adaptation

Track clipping, bias, exceptional values, fallback, and errors across layers and
iterations. The same local MSE can have different downstream effects depending
on where and how the error occurs.

Condition diagnostics on the actual adapted trajectory. Replaying a policy
only on reference activations can miss the activation changes caused by earlier
decisions.

Per-step correction and precision adaptation should be separate ablations.
A sampler change, low-rank branch, or weight modification must not be silently
credited to the activation detector.

[ViDiT-Q](../papers/2025-zhao-vidit-q.md) and
[SVDQuant](../papers/2025-li-svdquant.md) are relevant full-model comparisons,
with their respective interventions preserved.

## What runtime hardware can know

Reference outputs, final labels, and future denoising states belong to offline
evaluation. A hardware policy may use only its defined observations and state.

A local clipping guard can constrain one failure mode; it cannot by itself
guarantee task quality. Any stronger guarantee needs explicit assumptions and
evidence. Present empirical acceptance separately from formal guarantees.

## Proposed acceptance procedure

First validate the reference model and evaluator. Then introduce one numerical
mechanism and verify that its runtime path is actually exercised.
Evaluate full-model quality before spending effort on detailed simulator work.

Only candidates meeting the task-quality requirement proceed to a credible
hardware cost comparison. Report Pareto trade-offs when tolerances differ;
do not rank policies using energy savings obtained at incomparable quality.

## Search and limits

Primary web discovery on **2026-11-08**, with focused reading completed
**2026-11-09**, covered Q-Diffusion, PTQD, Q-Drift, FID, and VBench.
The selected versions are recorded in their canonical notes.

This is a targeted review. It does not establish a universal error budget,
guaranteed detector validity, or a complete evaluation suite.
No neural-network outputs were generated or measured during this review.
