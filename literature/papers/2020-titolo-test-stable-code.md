# Automatic generation and verification of test-stable floating-point code

- Citation key: `titolo2020teststable`.
- Authors: Laura Titolo and Mariano Moscato and Cesar A. Muñoz.
- Publication/version: arXiv 2001.02981v1.
- Source: [primary paper](https://arxiv.org/abs/2001.02981v1).
- Reviewed: 2026-11-24. Status: **Primary full text, focused Introduction and Sections 4–5; theorem/proof details not independently checked.**

## Findings and relevance

Combines PRECiSA, Frama-C and PVS to generate C with stability contracts from real-valued specifications. It extends earlier transformation support to calls, bounded recursion and symbolic parameters. Warnings identify executions for which agreement of computational paths is not established.

## Limits and comparison

General guarded execution, control-flow stability and verification are already researched. The prospective neural-inference contribution must demonstrate useful decision/state validation and trustworthy optimization comparisons on declared arithmetic contracts; repackaging an existing guard in an inference engine is insufficient.
