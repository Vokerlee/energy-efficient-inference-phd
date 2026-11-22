# WitCert: Sound Runtime Risk Observability and Gating for KV-Cache Quantization

- Citation key: `wei2026witcert`.
- Authors: Wei, Fanzhe; Liu, Li; Wang, Ziyang; Wang, Chenyu.
- Publication: arXiv preprint, 2026; pinned author version.
- Source: [paper](https://arxiv.org/abs/2607.28699v3); [full text](https://arxiv.org/html/2607.28699v3).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Sections 3–4, 6.2 and 6.4; formal artifact not executed.

## What it establishes

Provides a deterministic band-norm witness for cache-preserving schemes and arbitrary queries. A tighter probabilistic tier uses controlled subtractive-dither INT8 and assumes queries independent of stored dither. Risk observations drive selective repair.

## Relevance to our goals

A comparator for affordable local error observability; certification is not an unexplored label.

## Limits and transfer conditions

The probabilistic theorem does not cover free-running adaptive decoding. Local certificates do not solve multilayer quality composition. The paper reports loose coarse-precision bounds as a limitation. Kernel assumptions, fallback and metadata must be checked; proofs/results were not independently reproduced.
