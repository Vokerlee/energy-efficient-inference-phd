# A Strassen-base Block Matrix Multiply With Dynamic Quantization for Vision Transformer(ViT) Acceleration

- Citation key: `chiu2025strassenquant`.
- Authors: Chiu, Jih-Ching; Lin, Qing-You; Lin, Yu-Hsin; Chen, Pin-Tze.
- Publication: VLSI-DAT 2025, poster P1-24, official poster abstract book.
- Source: [primary source](https://vlsicad2025.conf.tw/site/userdata/1639/file/session/Poster_1.pdf).
- Reviewed: 2026-11-22. Status: **Primary conference abstract only; full-paper review pending.**

## What it establishes

Describes a four-stage Strassen-based block multiplier and dynamic shared-exponent quantization for 8-by-8 blocks. Internal arithmetic is 16-bit integer, with fractional alignment deferred to a final shift.

## Relevance to our goals

The specific combination of Strassen, block quantization and ViT acceleration already has a prior description.

## Limits and transfer conditions

An abstract cannot establish every selector, memory schedule or numerical guarantee. Detailed arithmetic, quality evaluation and implementation evidence remain unverified; reported cross-platform performance is not adopted as our evidence.
