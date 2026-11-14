# Hutch++: Optimal Stochastic Trace Estimation

- Citation key: `meyer2021hutchplusplus`.
- Authors: Meyer, Raphael A.; Musco, Cameron; Musco, Christopher; Woodruff, David P.
- Publication: SOSA 2021, pages 142–155.
- Source: [publisher DOI](https://doi.org/10.1137/1.9781611976496.16); [author manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC8553228/).
- Reviewed: 2026-11-15. Status: **full-text focused reading**.
- Reading focus: Sections 1.1–1.3, Eq. (1), Algorithm 1, and Theorem 1.1.
- Evidence: Trace estimators, probabilistic guarantees, and numerical comparisons.

## What it establishes

Reviews the Girard–Hutchinson estimator and improves its query complexity
using a low-rank variance-reduction step. The basic identity estimates a
matrix trace from independent zero-mean, unit-variance probe vectors.

## Relevance to our goals

Applying the identity to a fixed error matrix's Gram matrix estimates squared
Frobenius error from projected products. This is established mathematics.

## Limits and transfer conditions

The basic estimator is not Hutch++ itself. Small probe counts do not imply a
tight certificate, and changing the error matrix using estimator feedback
requires separate justification. Include projection and postprocessing costs.
