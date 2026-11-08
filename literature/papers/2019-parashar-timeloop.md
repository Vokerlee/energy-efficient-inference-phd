# Timeloop: A Systematic Approach to DNN Accelerator Evaluation

- Citation key: `parashar2019timeloop`.
- Authors: Parashar, Angshuman; Raina, Priyanka; Shao, Yakun Sophia; Chen, Yu-Hsin; Ying, Victor A.; Mukkara, Anurag; Venkatesan, Rangharajan; Khailany, Brucek; Keckler, Stephen W.; Emer, Joel.
- Publication: IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS), 2019.
- Source: [paper](https://ysshao.github.io/assets/papers/ispass_2019.pdf).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Sections IV–VI: mappings, action counts, performance, and energy.
- Evidence: Analytical architecture/mapping model, validated against reference designs.

## What it establishes

Separates workload, architecture, and mapping. It derives arithmetic, buffer, and communication actions to estimate performance and energy without requiring cycle-accurate simulation.

## Relevance to our goals

Provides a methodological baseline for portable research before final chip-simulator validation.

## Limits and transfer conditions

The original performance model assumes effectively pipelined execution with negligible disruptive stalls. Cross-layer reuse and a new data-dependent controller need explicit treatment; tool availability does not validate new hardware automatically.
