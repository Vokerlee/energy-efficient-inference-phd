# PassionSR: Post-Training Quantization with Adaptive Scale in One-Step Diffusion based Image Super-Resolution

- Citation key: `zhu2025passionsr`.
- Authors: Zhu, Libo; Li, Jianze; Qin, Haotong; Li, Wenbo; Zhang, Yulun; Guo, Yong; Yang, Xiaokang.
- Publication: CVPR2025, pp.12778–12788.
- Sources: [proceedings and metadata](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_PassionSR_Post-Training_Quantization_with_Adaptive_Scale_in_One-Step_Diffusion_based_CVPR_2025_paper.html); [paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhu_PassionSR_Post-Training_Quantization_with_Adaptive_Scale_in_One-Step_Diffusion_based_CVPR_2025_paper.pdf); [supplement](https://openaccess.thecvf.com/content/CVPR2025/supplemental/Zhu_PassionSR_Post-Training_Quantization_CVPR_2025_supplemental.pdf).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Focus: main Sections3.2–3.4,4.1, Table3; supplement Sections2–3.1.

## Findings, relevance and limits

The method quantizes both UNet and VAE for one-step diffusion super-resolution. It removes the prompt-encoding branch in favor of a prepared empty-prompt embedding. Learnable clipping boundaries and channel scale/shift transformations are fitted on calibration pairs; the original model weights are frozen during this optimization. Thus “adaptive scale” here does not establish a calibration-free hardware controller using current source groups.

Section4.1 uses500 cropped low/high-resolution pairs from DIV2K training for calibration. Section3.4 separates calibration stages and defines encoder/decoder reconstruction losses. The supplement compares UNet-only with UNet-and-VAE quantization: VAE precision contributes additional reconstruction degradation. This is direct prior art against treating low-bit image decoding as an untouched application. It also motivates complete-pipeline component coverage and separate decoder fidelity checks.

The reported operation/storage reductions are not measured energy, and do not specify a source-before-im2col causal feedback datapath. Super-resolution metrics against high-resolution targets differ from pixel fidelity to an original text-to-image output. Results were not reproduced here; no DC-AE-specific or runtime hardware novelty is established by this reading.
