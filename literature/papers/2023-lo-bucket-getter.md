# Bucket Getter: A Bucket-based Processing Engine for Low-bit Block Floating Point (BFP) DNNs

- Citation key: `lo2023bucketgetter`.
- Authors: Yun-Chen Lo; Ren-Shuo Liu.
- Publication: 2023; DOI `10.1145/3613424.3614249`.
- Source: [publisher](https://doi.org/10.1145/3613424.3614249).
- Publisher abstract: [IEEE record](https://ieeexplore.ieee.org/document/10411385/).
- Reviewed: 2026-11-23. Status: **publisher abstract and verified metadata; full-text review pending**.
- Reading focus: Integer buckets before floating-point accumulation; DOI/author metadata checked through Crossref.

## What it establishes

Uses small fixed-point accumulation buckets for bounded exponent ranges before floating-point accumulation, targeting the remaining accumulation cost in low-bit BFP processing.

## Relevance to our goals

Direct hardware precedent for exponent grouping and deferred floating-point accumulation; these primitives cannot be presented as new.

## Limits and transfer conditions

Exact bucket assignment, flushing, precision, physical dataflow and control costs require full-text review. Absence of accessible code is not evidence of missing hardware. A proposed streaming or tile-specific policy needs a mechanism-level comparison, including bucket state and merge costs.
