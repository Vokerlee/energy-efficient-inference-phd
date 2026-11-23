# DiverGet: A Search-Based Software Testing Approach for Deep Neural Network Quantization Assessment

- Citation key: `yahmed2022diverget`.
- Authors: Ahmed Haj Yahmed; Houssem Ben Braiek; Foutse Khomh; Sonia Bouzidi; Rania Zaatour.
- Publication/version: 2022; version/source pinned below.
- Source: [primary source](https://arxiv.org/abs/2207.06282v1).
- Reviewed: 2026-11-24. Status: **Full-text focused reading: version1 Sections4.1–4.4 and5.1.**

## Findings, relevance and limits

Uses search-based testing to assess quantized-model robustness under shifted inputs. Finding disagreement between full-precision and quantized networks is already a research direction. A proposed validation methodology must distinguish desired approximation, implementation mismatch, state-dependent controller decisions and sampled occurrence rates. Full search objectives and hardware/cost treatment remain reading dependencies; no results were reproduced.

Focused follow-up2026-11-24: the protocol searches domain-specific hyperspectral
transformations, with Jensen–Shannon output divergence and coverage-signature
differences as fitness objectives. Its evaluated subject pairs use TensorFlow
Lite PTQ/QAT classifiers. This is more specific than generic random perturbation.
The inspected protocol does not supply the live/frozen controller intervention
used in the present decoder diagnostics; this distinction is not an exhaustive
claim about all testing literature or proof of a new method.
