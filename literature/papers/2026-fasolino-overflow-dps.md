# Overflow-Driven Dynamic Precision Scaling Fixed-Point Multiply-Accumulator Unit

- Citation key: `fasolino2026overflowdps`.
- Authors: Andrea Fasolino; Rosalba Liguori; Luigi Di Benedetto; Alfredo Rubino; Gian Domenico Licciardo.
- Publication: 2026; DOI `10.1109/TVLSI.2026.3680254`.
- Source: [publisher](https://doi.org/10.1109/TVLSI.2026.3680254).
- Reviewed: 2026-11-23. Status: **publisher abstract and indexed introduction; full-text review pending**.
- Reading focus: Autonomous monitoring granularity, representation updates and stated implementation evidence; metadata checked through Crossref.

## What it establishes

Describes a hardware MAC monitor that observes carry/sign behavior and shifts the fixed-point representation to handle overflow and over-representation without a software controller. Reports FPGA and synthesized implementation results.

## Relevance to our goals

Existing autonomous per-accumulation control rules out novelty of merely moving an overflow detector into hardware.

## Limits and transfer conditions

The full algorithm and scope of its rounding-error statement require full-text review. Per-MAC behavior is not a demonstrated whole-array block-scale schedule or whole-network guarantee. Do not transfer reported power figures to another array or assume that every signed intermediate is exact.
