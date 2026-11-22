# ReCache: Learning Budget-Aware Caching Schedules for Diffusion Models via REINFORCE

- Citation key: `aliev2026recache`.
- Authors: Aliev, Mishan; Neudachina, Eva; Bykov, Ilya; Oganov, Aleksandr; Struminsky, Kirill; Alanov, Aibek; Rakitin, Denis.
- Publication: arXiv preprint, 2026; version 1.
- Source: [paper](https://arxiv.org/abs/2606.06060v1); [full text](https://arxiv.org/html/2606.06060v1).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Section 3 and Appendix B.3.

## What it establishes

Learns budget-conditioned recomputation schedules using policy gradients and full-inference targets. A small network maps the target step budget to schedule logits.

## Relevance to our goals

Budget-aware caching is established; specifying a compute budget alone is not a new contribution.

## Limits and transfer conditions

Training is per model/caching mechanism. The reviewed schedule input is the budget, not live activation error or cache occupancy. Step-count budgets do not directly bound energy or retained-state capacity. No experiments were reproduced.
