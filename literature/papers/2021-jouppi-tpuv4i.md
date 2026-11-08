# Ten Lessons From Three Generations Shaped Google's TPUv4i: Industrial Product

- Citation key: `jouppi2021tpuv4i`.
- Authors: Jouppi, Norman P.; Yoon, Doe Hyun; Ashcraft, Matthew; Gottscho, Mark; Jablin, Thomas B.; Kurian, George; Laudon, James; Li, Sheng; Ma, Peter; Ma, Xiaoyu; Norrie, Thomas; Patil, Nishant; Prasad, Sushma; Young, Cliff; Zhou, Zongwei; Patterson, David.
- Publication: ACM/IEEE International Symposium on Computer Architecture (ISCA), 2021.
- Source: [paper](https://markgottscho.com/cv/papers/2021_NJouppi_ISCA.pdf).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Lesson 1, Table 2, memory-system design, and performance/TDP evaluation.
- Evidence: Production architecture evidence, component estimates, and TDP-based comparisons.

## What it establishes

Documents unequal scaling of arithmetic, SRAM, wiring, and DRAM. Table 2 updates operation-energy examples to 7 nm and specifies memory costs per 64-bit access.

## Relevance to our goals

Prevents carrying historical energy ratios forward unchanged; motivates retaining memory and communication costs even for BF16 systolic inference.

## Limits and transfer conditions

Component estimates, measured performance, and performance/TDP are different evidence types. Table entries and their banking/I/O footnotes must be preserved; they do not provide a complete per-inference energy decomposition.
