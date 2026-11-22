# Low-Power Data Streaming in Systolic Arrays with Bus-Invert Coding and Zero-Value Clock Gating

- Citation key: `peltekis2023bic`.
- Authors: Peltekis, Christodoulos; Filippas, Dionysios; Dimitrakopoulos, Giorgos; Nicopoulos, Chrysostomos.
- Publication: MOCAST; author preprint reviewed, 2023.
- Source: [paper](https://arxiv.org/abs/2304.12691v3); [full text reviewed](https://arxiv.org/pdf/2304.12691v3).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Sections II–IV: arithmetic versus streaming/sum movement, selective coding, zero bubbles, and synthesis/power methodology.
- Evidence: HLS/RTL synthesis and power estimates for a BF16 systolic array.

## What it establishes

Uses bus-invert coding on weight mantissas and zero-value gating on activation inputs to reduce switching in a fixed systolic schedule.

## Relevance to our goals

A lossless representation/gating baseline for energy changes without lower numerical precision.

## Limits and transfer conditions

The tested array, process, models, and activity determine the result. Gated zero bubbles do not demonstrate elimination of scheduled cycles; reported power savings are implementation estimates.

## Component-energy interpretation

Section II separates operand loading/forwarding, multiplication/addition and
sum accumulation/unloading. Forwarding consumes energy in both clocked
pipeline registers and connecting wires. Computation is described as the
largest consumer in the authors' setting; that is not a universal ordering
between multipliers, wide accumulators, registers and local SRAM in another
implementation.

The example is output-stationary: results accumulate locally in PEs and are
unloaded after computation. Capacity in a separate result SRAM does not by
itself establish that dataflow. A design that reads/writes partial sums between
K tiles needs those SRAM actions counted even when all results fit on chip.

Section IV evaluates a16x16 BF16 array synthesized from Catapult HLS with a
45nm library, using Oasys and PowerPro. The reported application-average
dynamic-power reductions are9.4% for ResNet50 and6.2% for MobileNet, with5.7%
area overhead. These are combined coding/gating results, not a measured
component-energy breakdown for a128x128 BF16/FP32 array or a whole accelerator.
Do not infer energy proportional to useful MAC count, numerical bit width,
zero fraction, or a GPU implementation's latency from these figures.
