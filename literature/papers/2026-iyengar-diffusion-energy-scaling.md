# Energy Scaling Laws for Diffusion Models: Quantifying Compute in Image Generation

- Citation key: `iyengar2026diffusionenergy`.
- Authors: Aniketh Iyengar, Jiaqi Han, Boris Ruf, Vincent Grari, Marcin Detyniecki and Stefano Ermon.
- Publication: accepted at ACM FAccT 2026; arXiv:2511.17031v2 reviewed, revised 2026-05-12.
- Source: [versioned paper](https://arxiv.org/abs/2511.17031v2); [full text](https://arxiv.org/html/2511.17031v2).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Sections 2–5, Figure 1, measurement boundary and Appendix A.1.
- Evidence: Whole-GPU idle-subtracted energy estimates and analytical FLOP decomposition.

## What it establishes

Examines SD2, SD3.5, Flux and Qwen-Image using architecture/configuration-based
FLOP estimates and GPU energy observations. Text encoding and decoding are
one-off stages; the denoising backbone is evaluated repeatedly. Figure 1
assigns over 90% of FLOPs to denoising for its shown configurations, including
10-step generation. This is a compute share, not a measured stage-energy share.

Measurements use CodeCarbon/NVML at 1 Hz, subtract idle power and use batch
size one. Fitted energy–FLOP exponents near one are reported for several
model/hardware combinations.

## Relevance to our goals

Motivates accounting for repeated transformer/convolution execution and
including steps, resolution, guidance implementation and precision in each
comparison. Useful for choosing a profiling scope before hardware modeling.

## Limits and transfer conditions

Whole-run energy fits do not identify the energy of individual operators,
memory levels or circuits. Near-linear scaling alone does not prove a compute
bottleneck, since traffic and duration can also scale with work. One-Hz
observations cannot resolve individual short kernels. Validate model-specific
FLOP formulas and actual guidance/checkpoint behavior before reusing them;
do not transfer fitted coefficients or assume every diffusion setup is compute-bound.
