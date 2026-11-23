# Arbitor: A Numerically Accurate Hardware Emulation Tool for DNN Accelerators

- Citation key: `jiang2023arbitor`.
- Authors: Chenhao Jiang; Anand Jayarajan; Hao Lu; Gennady Pekhimenko.
- Publication/version: 2023; version/source pinned below.
- Source: [primary source](https://www.usenix.org/conference/atc23/presentation/jiang-chenhao).
- Reviewed: 2026-11-24. Status: **Full-text focused reading: Sections3–4.1 in the author proceedings PDF.**

## Findings, relevance and limits

Arbitor uses TensorFlow/XLA primitive-operation manipulation to emulate low-precision, approximate and sparse computations on GPUs. It explicitly shows that layer-level emulation can misrepresent numerical behavior. Numerically faithful fast GPU emulation is therefore an existing methodology, not a new contribution solely from replacing a slow simulator. Its custom data-type/mask policies are a comparison baseline; current-block decisions, bounded state and cost uncertainty need mechanism-level comparison. Reported results were not reproduced.

[Reviewed proceedings PDF](https://www.usenix.org/system/files/atc23-jiang-chenhao.pdf), pp.519–536.
