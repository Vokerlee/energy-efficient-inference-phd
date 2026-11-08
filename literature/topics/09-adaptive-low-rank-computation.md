# 09 — Adaptive low-rank activation computation

Reviewed: **2026-11-08**. Four additional focused sources plus shared
outlier/low-rank execution evidence.

## Distinguish the possible directions

- **Weight factorization:** replace a fixed matrix by smaller factors.
- **Activation projection:** represent current features in a smaller subspace.
- **Adaptive rank:** select how much of a prepared representation to execute.
- **Online basis discovery:** find a new subspace from current activations.

These have different costs and model requirements.
[RaNA](../papers/2025-garcia-rana.md) and
[NA-LR](../papers/2025-wang-noise-adaptive-low-rank.md) establish adaptive-rank
prior art. [Randomized decomposition](../papers/2011-halko-randomized-decompositions.md)
provides an algorithmic reference for discovery costs.

[SVDQuant](../papers/2025-li-svdquant.md) is a relevant low-rank correction
baseline; [Palu](../papers/2025-chang-palu.md) is a memory-oriented contrast.

## A concrete activation-projection example

For A[M,K], W[K,N], and an orthonormal basis P[K,r], an illustrative
approximation is:

```text
A*W ~= (A*P) * (P^T*W)
```

With a fixed P, projected weights can be prepared offline. Ignoring setup and
hardware inefficiency, runtime multiplication work changes from M*K*N to
M*r*(K+N). This is an algebraic cost comparison, not a measured speedup.

If P changes per input or block, P^T*W generally must change too. Treating it
as precomputed would hide runtime work. Online SVD/range finding also requires
passes, workspace, and arithmetic; it is not a free statistic.

## Why nested ranks are an attractive first experiment

A fixed ordered basis can support a discrete prefix of ranks. This separates
rank selection from expensive basis rediscovery and can preserve precomputed
weight projections.

However, choosing rank after computing every projected component saves only
later work. Define what the selector observes before omitted components would
have been computed. Learned rank selection, offline layer sensitivity, and
current activation measurements are different baselines.

Moving a projection through an arbitrary nonlinearity is not an exact
transformation. Place approximations at explicitly defined operator boundaries.

## Systolic mapping

Two smaller GEMMs may use more physical operations or temporary traffic than
one well-utilized dense GEMM. Ranks below a physical reduction/output granule
may not reduce cycles. Compare ranks aligned to actual hardware modes, including
padding and rank-transition costs.

Track projection outputs, prepared-weight storage, accumulation, and possible
fusion. A good logical rank is not necessarily a good physical shape.

## Evaluation and sequencing

This should be a separate bounded pilot after the basic intervention/runtime
contract exists:

1. measure activation spectra offline as exploratory evidence;
2. compare fixed ranks and fixed bases with the unchanged dense baseline;
3. introduce causal rank selection;
4. consider basis adaptation only if its complete cost appears recoverable.

Measure full-model quality, physical work, intermediate traffic, and sensitivity
to changed input distributions. Captured singular-value energy is a local
approximation metric, not a task-quality guarantee.

Separate post-training approximations from retrained/adapted models. A
quantization combination can be investigated later, after establishing the
low-rank mechanism's independent value.

## Search and limits

Web searches on **2026-11-08** covered adaptive rank allocation/RaNA,
noise-adaptive low-rank diffusion, randomized matrix decompositions, and Palu.
Full-text focus: when factors are prepared, what changes online, and which
costs are included.

The corpus is deliberately small and mechanism-oriented. It does not establish
novelty for activation-subspace execution or prove a net energy benefit.
NA-LR is workshop-scale evidence; Palu's memory objective differs from our
compute-intensive target. No low-rank experiment has been run.
