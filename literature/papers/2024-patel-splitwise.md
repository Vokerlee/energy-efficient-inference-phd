# Splitwise: Efficient Generative LLM Inference Using Phase Splitting

- Citation key: `patel2024splitwise`.
- Authors: Patel, Pratyush; Choukse, Esha; Zhang, Chaojie; Shah, Aashaka; Goiri, Inigo; Maleki, Saeed; Bianchini, Ricardo.
- Publication: ACM/IEEE International Symposium on Computer Architecture (ISCA), 2024.
- Source: [paper](https://arxiv.org/abs/2311.18677v2); [full text reviewed](https://arxiv.org/pdf/2311.18677v2).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Section III characterization, particularly power-cap sensitivity; methodology.
- Evidence: A100/H100 phase measurements plus cluster simulation.

## What it establishes

Prompt processing and token generation show different resource and power-cap sensitivities. In the tested configuration, reducing the token-generation power cap from 700 to 350 W has little latency impact.

## Relevance to our goals

Supplies a within-model contrast for compute-intensive and bandwidth-sensitive execution, without excluding an entire model family from research.

## Limits and transfer conditions

A power cap is not measured average power or joules. Batch size, context, cache capacity, serving policy, and cluster simulation boundaries constrain transfer of the findings.
