# Computing's Energy Problem (and What We Can Do About It)

- Citation key: `horowitz2014energy`.
- Authors: Horowitz, Mark.
- Publication: IEEE International Solid-State Circuits Conference (ISSCC), 2014.
- Source: [paper](https://doi.org/10.1109/ISSCC.2014.6757323); [full text reviewed](https://gwern.net/doc/cs/hardware/2014-horowitz-2.pdf).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Sections 5–6 and the conditions of the operation-energy comparison.
- Evidence: Technology-specific component estimates and architectural argument.

## What it establishes

Explains why arithmetic savings must be considered alongside memory access and instruction/control costs. Locality and specialization influence attainable energy efficiency.

## Relevance to our goals

Motivates separating arithmetic, operand delivery, storage, and control in an inference energy model.

## Limits and transfer conditions

The familiar operation costs concern 45 nm technology and particular operation/access definitions. They are historical reference points, not current BF16/FP8 costs or a universal DRAM-to-MAC ratio.
