# RAELLA: Reforming the Arithmetic for Efficient, Low-Resolution, and Low-Loss Analog PIM: No Retraining Required!

- Citation key: `andrulis2023raella`.
- Authors: Tanner Andrulis; Joel S. Emer; Vivienne Sze.
- Publication: 2023; author version `2304.07935v1`.
- Source: [paper](https://arxiv.org/abs/2304.07935v1); [full text](https://arxiv.org/html/2304.07935v1).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Reading focus: Sections 3.3–3.4, 4.3 and 6.1: speculation/recovery, column gating and modeled evaluation.

## What it establishes

Combines prepared weight encoding/slicing with live speculative input slicing. Failed ADC columns receive recovery conversions while successful columns gate their ADCs.

## Relevance to our goals

Demonstrates that data-dependent recovery can save energy without saving execution cycles. Useful for separating conversion, array activity and numerical fidelity.

## Limits and transfer conditions

In the reviewed architecture the entire crossbar runs recovery even when only some columns failed, and recovery saturation can be accepted. Gains rely on analog/ADC costs and cannot be transferred to a digital systolic array. Weight preparation and online input control are different stages; no-retraining does not mean no preparation.
