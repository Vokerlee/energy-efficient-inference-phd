# PREFILT: Prefiltering for Fully Quantized Image Restoration Neural Networks

- Citation key: `makhov2025prefilt`.
- Authors: Denis Makhov; Ruslan Ostapets; Irina Zhelavskaya; Dehua Song.
- Publication: ICCV Workshops 2025, BiVision, pages 4101–4110.
- Source: [paper](https://openaccess.thecvf.com/content/ICCV2025W/BiVision/papers/Makhov_PREFILT_Prefiltering_for_Fully_Quantized_Image_Restoration_Neural_Networks_ICCVW_2025_paper.pdf).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Reading focus: Sections 1–4: frequency-domain motivation, prefilter, bypass estimate and quantization-aware training setup.

## What it establishes

Combines image prefiltering and a bypass estimate with quantized restoration
networks. Studies fixed and trainable filters; the evaluation includes
quantization-aware training. Its frequency-domain reasoning connects noise
distribution to subsequent filtering rather than relying only on tensor MSE.

## Relevance to our goals

Prior art for reshaping a quantization problem using its downstream filtering
and reconstruction path. Include preprocessing and bypass work when comparing
end-to-end accuracy or efficiency.

## Limits and transfer conditions

An input-image preprocessing/training method is not a demonstrated live
per-layer residual-feedback controller. White or weakly correlated noise is
a modeling assumption, not a universal property of deterministic activation
quantization. Restoration-specific quality and execution claims do not transfer
directly to classifiers, diffusion inference or another accelerator.
