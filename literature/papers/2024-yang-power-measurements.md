# Part-time Power Measurements: nvidia-smi's Lack of Attention

- Citation key: `yang2024parttime`.
- Authors: Yang, Zeyu; Adamek, Karel; Armour, Wesley.
- Publication: International Conference for High Performance Computing, Networking, Storage and Analysis (SC), 2024.
- Source: [paper](https://arxiv.org/abs/2312.02741v3); [full text reviewed](https://arxiv.org/pdf/2312.02741v3).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Sensor characterization, external-meter comparison, and measurement practices.
- Evidence: Measurement-method validation across NVIDIA GPU generations.

## What it establishes

Shows that polling rate alone does not characterize the underlying sensor's observation window. Sampling behavior can bias energy estimates, particularly for intermittent workloads.

## Relevance to our goals

Requires checking telemetry semantics before attributing small energy gains to runtime precision policies.

## Limits and transfer conditions

Results apply to tested hardware/software interfaces. They neither invalidate every GPU measurement nor prove that a different generation or cumulative counter has identical behavior. Recheck the actual measurement path.
