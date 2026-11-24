# PyTorch Inductor intermediate precision-cast preservation

- Citation key: `pytorch2026precisioncasts`.
- Authors: PyTorch contributors.
- Publication/version: 2026; pinned primary source below.
- Source: [primary source](https://github.com/pytorch/pytorch/blob/70d99e998b4955e0049d13a98d77ae1b14db1f45/torch/_inductor/config.py).
- Reviewed: 2026-11-24. Status: **Pinned upstream source and matching locally installed Torch source inspected, especially emulate_precision_casts. Software record, not a research paper.**

## Findings and relevance

The configuration describes elimination of intermediate downcast/upcast rounding during fusion. The emulate_precision_casts option preserves eager-style precision truncations. This can affect a numerical predicate built around an intermediate BF16 observation.

## Limits

A compiler may improve approximation to real arithmetic while changing a specified finite-precision execution. Guards and model computations both need validation under the actual compiler configuration. The implementation-specific option is not a novel research mechanism or a promise about all compiler transformations.
