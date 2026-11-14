# A New Approach to Probabilistic Rounding Error Analysis

- Citation key: `higham2019probabilistic`.
- Authors: Higham, Nicholas J.; Mary, Theo.
- Publication: SIAM Journal on Scientific Computing 41(5), A2815–A2835, 2019.
- Source: [publisher record](https://doi.org/10.1137/18M1226312); [author manuscript](https://eprints.maths.manchester.ac.uk/2731/1/paper.pdf).
- Reviewed: 2026-11-15. Status: **full-text focused reading**.
- Reading focus: Author manuscript dated 2019-03-18, Section 2 Model 2.1 and bounds; Section 3.1 inner products.
- Evidence: Probabilistic backward-error analysis under an explicit rounding model.

## What it establishes

Derives concentration-based rounding bounds under bounded, independent,
zero-mean errors, without requiring identical distributions. Its bounds can
grow substantially more slowly than deterministic worst-case bounds.

## Relevance to our goals

A rigorous comparator for statistical accumulation claims and the assumptions
needed before invoking square-root-like behavior.

## Limits and transfer conditions

These are probabilistic backward-error bounds, not the exact RMS of additive
neural errors. Their probability parameters and higher-order terms matter.
Model 2.1 is not universally valid for deterministic rounding; it establishes
neither isotropic activation noise nor preserved end-to-end task quality.
