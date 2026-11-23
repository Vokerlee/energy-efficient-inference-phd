# Robustness analysis of finite precision implementations

- Citation key: `goubault2013unstabletests`.
- Authors: Eric Goubault and Sylvie Putot.
- Publication/version: arXiv 1309.3910v1.
- Source: [primary paper](https://arxiv.org/abs/1309.3910v1).
- Reviewed: 2026-11-24. Status: **Primary full text, focused Introduction and Section 3, especially test interpretation and discontinuity-error terms.**

## Findings and relevance

FLUCTUAT extends round-off analysis beyond coinciding real/finite-precision paths. It tracks an additional discontinuity contribution when conditional decisions differ, with constraints narrowing the unstable input region. Consequently, separating ordinary arithmetic error from decision-induced error is established prior art, not a new principle of neural inference.

## Limits and comparison

Its semantics compare real and finite-precision programs. Our decoder intervention instead compares two declared finite-precision implementations and follows quantizer decisions through a pretrained model. The inspected work does not establish our model-level ranking result; conversely our finite sample is not its sound static bound.
