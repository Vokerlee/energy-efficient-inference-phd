# Budget-Constrained Step-Level Diffusion Caching

- Citation key: `lei2026budcache`.
- Authors: Lei, Mingkun; Zhao, Tong; Yuan, Liangyu; Zhang, Chi.
- Publication: arXiv preprint, 2026; version 1.
- Source: [paper](https://arxiv.org/abs/2606.13496v1); [full text](https://arxiv.org/html/2606.13496v1).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Sections 3.2–3.4.

## What it establishes

BudCache searches step-level recomputation policies offline with simulated annealing and hill climbing under a fixed compute budget. Schedule alignment adjusts the discretization for aggressive caching.

## Relevance to our goals

Distinguishes prepared budgeted scheduling from per-input runtime decisions.

## Limits and transfer conditions

It is not evidence for an autonomous tile-level selector or cache-capacity management. Count offline search separately from runtime work; a fixed number of evaluations does not establish a fixed energy cost. Reported quality and speed were not reproduced.
