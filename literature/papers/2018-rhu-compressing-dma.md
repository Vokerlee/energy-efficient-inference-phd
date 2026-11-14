# Compressing DMA Engine: Leveraging Activation Sparsity for Training Deep Neural Networks

- Citation key: `rhu2018cdma`.
- Authors: Rhu, Minsoo; O'Connor, Mike; Chatterjee, Niladrish; Pool, Jeff; Kwon, Youngeun; Keckler, Stephen W..
- Publication: HPCA; 2017 author preprint reviewed, 2018.
- Source: [paper](https://research.nvidia.com/sites/default/files/pubs/2018-02_Compressing-DMA-Engine%3A/rhu.hpca2018.pdf); [full text reviewed](https://arxiv.org/pdf/1705.01626v1).
- Reviewed: 2026-11-14. Status: **full-text focused reading**.
- Reading focus: Preprint introduction/architecture: activation offload, compression boundary, and bandwidth demand. Published author list differs from the five-author preprint.
- Evidence: Compression/DMA proposal evaluated for GPU training-memory virtualization.

## What it establishes

Compresses sparse activations while transferring between GPU and CPU memory to reduce offload traffic.

## Relevance to our goals

A hardware precedent for exploiting activation sparsity at a transfer boundary rather than only at arithmetic.

## Limits and transfer conditions

Training offload and ReLU-era data differ from compute-bound inference. Keep preprint/published measurements separate; compression does not automatically avoid matrix cycles.
