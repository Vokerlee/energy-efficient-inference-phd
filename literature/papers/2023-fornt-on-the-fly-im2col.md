# An Energy-Efficient GeMM-Based Convolution Accelerator With On-the-Fly im2col

- Citation key: `fornt2023im2col`.
- Authors: Fornt, Jordi; Fontova-Muste, Pau; Caro, Marti; Abella, Jaume; Moll, Francesc; Altet, Josep; Studer, Christoph.
- Publication: IEEE Transactions on Very Large Scale Integration Systems, 2023.
- Source: [paper](https://doi.org/10.1109/TVLSI.2023.3286122); [full text reviewed](https://upcommons.upc.edu/server/api/core/bitstreams/b45393e2-44d8-46d5-9b47-6e6020016374/content).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Data feeder, stride/dilation support, implementation constraints, and energy accounting.
- Evidence: 22 nm FP16 implementation analysis and memory-traffic estimates.

## What it establishes

Generates convolution operands on-chip using a feeder that supports strided and dilated patterns. Evaluates the feeder's area/power overhead against avoided memory transactions.

## Relevance to our goals

A direct hardware baseline for assessing feeder cost, reuse, and general convolution support.

## Limits and transfer conditions

Configured registers, SRAM access widths, and capacity limit concrete implementations. System-level memory savings use an energy model; they are not measurements of our chip.
