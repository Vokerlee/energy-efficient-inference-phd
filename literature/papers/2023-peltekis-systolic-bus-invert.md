# Low-Power Data Streaming in Systolic Arrays with Bus-Invert Coding and Zero-Value Clock Gating

- Citation key: `peltekis2023bic`.
- Authors: Peltekis, Christodoulos; Filippas, Dionysios; Dimitrakopoulos, Giorgos; Nicopoulos, Chrysostomos.
- Publication: MOCAST; author preprint reviewed, 2023.
- Source: [paper](https://arxiv.org/abs/2304.12691v3); [full text reviewed](https://arxiv.org/pdf/2304.12691v3).
- Reviewed: 2026-11-14. Status: **full-text focused reading**.
- Reading focus: Sections III–IV: selective coding, zero bubbles, and synthesis/power methodology.
- Evidence: HLS/RTL synthesis and power estimates for a BF16 systolic array.

## What it establishes

Uses bus-invert coding on weight mantissas and zero-value gating on activation inputs to reduce switching in a fixed systolic schedule.

## Relevance to our goals

A lossless representation/gating baseline for energy changes without lower numerical precision.

## Limits and transfer conditions

The tested array, process, models, and activity determine the result. Gated zero bubbles do not demonstrate elimination of scheduled cycles; reported power savings are implementation estimates.
