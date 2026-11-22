# Dissecting Transformers: A CLEAR Perspective Towards Green AI

- Citation key: `jain2026clear`.
- Authors: Hemang Jain, Shailender Goyal, Divyansh Pandey and Karthik Vaidhyanathan.
- Publication: arXiv:2510.02810v2, revised 2026-04-07.
- Source: [versioned paper](https://arxiv.org/abs/2510.02810v2); [full text](https://arxiv.org/html/2510.02810v2).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Sections 3–5 and 8, Appendix A model coverage.
- Evidence: Component-replay GPU energy observations for language-model transformers.

## What it establishes

CLEAR saves activations, repeatedly executes isolated components, and divides
measured aggregate energy by repetition count. It checks variability and
agreement between component sums and complete-model measurements. The paper
reports attention consuming more energy per FLOP than dense MLP operations
in its tested language-model configurations.

## Relevance to our goals

Offers a practical starting point for component profiling when energy sensors
cannot resolve a single short operation. Reinforces distinguishing operation
counts, elapsed time and joules, and specifying what an attention block includes.

## Limits and transfer conditions

The models are language transformers, not a measured ViT/DiT energy survey.
Repeated execution can change cache residency, frequency, thermal conditions
and launch amortization. Internal consistency does not establish identical
per-component costs within a normal model invocation. Cross-check full-run
energy and actual fused execution; do not transfer the reported energy-per-FLOP
ratios directly to a systolic accelerator.
