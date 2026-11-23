# ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders

- Citation key: `woo2023convnextv2`.
- Authors: Sanghyun Woo; Shoubhik Debnath; Ronghang Hu; Xinlei Chen; Zhuang Liu; In So Kweon; Saining Xie.
- Publication: CVPR 2023; reviewed author version `2301.00808v1`.
- Source: [paper](https://arxiv.org/abs/2301.00808v1); [full text](https://arxiv.org/html/2301.00808v1); [official implementation](https://github.com/facebookresearch/ConvNeXt-V2).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Reading focus: Sections 3–5 and Appendix A: masked pretraining, global response normalization, model configuration and fine-tuned evaluation.

## What it establishes

Combines fully convolutional masked-autoencoder pretraining with global
response normalization. Fine-tuned ConvNeXt models provide classification and
downstream vision backbones; sparse encoding is part of the pretraining
implementation rather than a general inference sparsity guarantee.

## Relevance to our goals

A supervised architectural control with depthwise spatial processing,
channel-mixing products and additional normalization. Useful for checking
whether conclusions from older dense-convolution networks transfer.

## Limits and transfer conditions

Parameter count and image accuracy do not reveal a matrix accelerator's
operator energy split. Depthwise geometry differs from dense im2col, and
pretraining sparsity cannot be counted as saved inference MACs. Check the
specific checkpoint, resolution, normalization and arithmetic when modifying
runtime activation representations.
