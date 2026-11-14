# A probabilistic framework for dynamic quantization

- Citation key: `santini2025probabilistic`.
- Authors: Santini, Gabriele; Paissan, Francesco; Farella, Elisabetta.
- Publication: arXiv preprint 2505.10689v1, 2025-05-15.
- Source: [record](https://arxiv.org/abs/2505.10689v1); [full text](https://arxiv.org/html/2505.10689v1).
- Reviewed: 2026-11-15. Status: **full-text focused reading**.
- Reading focus: Sections 4.1–4.2, Eqs. (8)–(13), calibration of interval parameters, and Section 5.1.
- Evidence: Output-range surrogate and embedded implementation; results not reproduced here.

## What it establishes

Predicts output statistics from inputs and weight moments under an i.i.d.
Gaussian-weight surrogate. Calibrated interval parameters convert predicted
moments into input-dependent quantization ranges; spatial subsampling reduces
estimation work.

## Relevance to our goals

Close prior art for low-memory runtime range prediction and observation-cost
trade-offs. Separate live measurements from calibrated constants.

## Limits and transfer conditions

The weight-distribution assumption is not proved for trained models. The
interval parameters remain fixed after calibration. This is a range predictor,
not a demonstrated signed accumulated-error precision controller. The reviewed
preprint contains template publication metadata; cite its verified arXiv version.
