# Gemmini: Enabling Systematic Deep-Learning Architecture Evaluation via Full-Stack Integration

- Citation key: `genc2021gemmini`.
- Authors: Genc, Hasan; Kim, Seah; Amid, Alon; Haj-Ali, Ameer; Iyer, Vighnesh; Prakash, Pranav; Zhao, Jerry; Grubb, Daniel; Liew, Harrison; Mao, Howard; Ou, Albert; Schmidt, Colin; Steffl, Samuel; Wright, John; Stoica, Ion; Ragan-Kelley, Jonathan; Asanovic, Krste; Nikolic, Borivoje; Shao, Yakun Sophia.
- Publication: Design Automation Conference (DAC), 2021.
- Source: [paper](https://arxiv.org/abs/1911.09925v3); [full text reviewed](https://arxiv.org/pdf/1911.09925v3).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Architecture template, memory hierarchy, programmable dataflows, and system effects.
- Evidence: Full-stack generator with implemented/fabricated accelerator examples.

## What it establishes

Connects configurable matrix hardware to DMA, scratchpads, accumulators, software, and an SoC. Supports investigation beyond isolated array throughput.

## Relevance to our goals

An architectural reference for general execution abstractions and eventual validation, closely matching our DMA/matrix-system experience.

## Limits and transfer conditions

Using its methodology does not require building or modifying RTL now. Selected generator configurations do not define every systolic implementation.
