# SANA-Sprint: One-Step Diffusion with Continuous-Time Consistency Distillation

- Citation key: `chen2025sanasprint`.
- Authors: Junsong Chen; Shuchen Xue; Yuyang Zhao; Jincheng Yu; Sayak Paul; Junyu Chen; Han Cai; Enze Xie; Song Han.
- Publication: ICCV 2025; reviewed author version `2503.09641v1`.
- Source: [paper](https://arxiv.org/abs/2503.09641v1); [full text](https://arxiv.org/html/2503.09641v1); [official implementation](https://github.com/NVlabs/Sana).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Reading focus: Sections 3–4 and Appendix F.1: model variants, few-step execution, architecture and evaluation protocol.

## What it establishes

Distills a pretrained flow model into a text-to-image generator supporting
few-step inference. Uses SANA-derived architecture and linear attention;
evaluation includes distributional and prompt-alignment metrics. The
training-free flow reparameterization is one part of a pipeline that also
includes trained distillation.

## Relevance to our goals

A modern diffusion workload with a small number of denoising steps. Inspect
projection, channel-mixing and depthwise work separately before applying a
convolution-specific optimization. Quantization must be tested through the
changed denoising trajectory and decoded output.

## Limits and transfer conditions

Few-step execution changes the opportunity for temporal reuse. Paired latent
or image similarity does not reproduce FID or GenEval. Text encoder, denoiser
and VAE have different operator mixes; denoiser-only accounting is not an
end-to-end energy measurement. The reviewed paper does not establish tolerance
to an arbitrary runtime quantization or accumulator policy.
