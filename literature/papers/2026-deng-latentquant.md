# LatentQuant: Preserving the Policy-Facing Latent Contract under NVFP4 VAE Quantization

- Citation key: `deng2026latentquant`.
- Authors: Deng, Ziye; Chen, Lufang; Feng, Shuyu; Duan, Zhenwei; Ye, Zicong; Sun, Yu; Li, Xiaofan; Gan, Ruyi; Wang, Hao; Zhang, Hao.
- Publication: arXiv2610.03959v1,2026-10-02; preprint.
- Source: [versioned primary abstract](https://arxiv.org/abs/2610.03959v1).
- Reviewed: 2026-11-23. Status: **primary abstract/metadata only; full-text review pending**.

## Findings, relevance and limits

The abstract describes NVFP4 quantization-aware training of video VAEs used by world-action models. It reports that joint encoder/decoder adaptation can preserve reconstruction while moving latents enough to damage a frozen downstream control policy. A two-stage method aligns the encoder, freezes it, then adapts the decoder. Decoder Jacobian changes are discussed as a training-time mechanism.

This is a useful counterexample to equating reconstruction fidelity with downstream task preservation. Distinguish an image decoder at the end of generation from an encoder whose output feeds a policy, and inference-time error propagation from gradients during quantization-aware training. The abstract reports GPU VAE speedups; these are neither independently reproduced nor energy measurements for another accelerator.

Do not infer its exact activation scaling, layout, calibration, packing or controller protocol from the abstract. It is a comparison dependency, not evidence that all online VAE activation optimizations are covered.
