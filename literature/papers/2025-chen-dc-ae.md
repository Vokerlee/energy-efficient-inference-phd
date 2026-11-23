# Deep Compression Autoencoder for Efficient High-Resolution Diffusion Models

- Citation key: `chen2025dcae`.
- Authors: Chen, Junyu; Cai, Han; Chen, Junsong; Xie, Enze; Yang, Shang; Tang, Haotian; Li, Muyang; Han, Song. The reviewed earlier author version additionally lists Yao Lu.
- Publication: ICLR2025; focused author version2410.10733v1,2024.
- Sources: [focused full text](https://arxiv.org/html/2410.10733v1); [proceedings record](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f062da1973ac9ac61fc6d44dd7fa309f-Abstract-Conference.html).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Focus: Sections3.2–3.3,4.1 and4.3: residual compression, decoder, profiling scope and generation.

## Findings, relevance and limits

DC-AE uses space/channel residual pathways and staged high-resolution adaptation to support highly compressed latent spaces. Its decoder remains a separate neural network. Changing latent compression alters denoiser token counts and reconstruction tradeoffs.

Profile the instantiated image decoder as well as the denoiser, especially for few-step generation. Paper-level GPU profiling uses explicit resolution, precision and sampling-step assumptions; these are not universal energy shares. The selected SANA checkpoint has its own fixed decoder configuration. Distinguish image encoding from text-to-image decoding, reconstruction quality from generation quality, and MAC counts from hardware energy. No reported result was reproduced here.
