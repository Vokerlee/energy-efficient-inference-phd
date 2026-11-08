# TinyML Hits the Memory Wall: A Benchmark of Ten Sub-Watt Edge Devices

- Citation key: `bonazzi2026tinyml`.
- Authors: Bonazzi, Pietro; Capogrosso, Luigi; Celik, Ahmet; Manzo, Rosanna; Giordano, Marco; Rucinski, Szymon; Hungerbuehler, Jonathan; Magno, Michele.
- Publication: arXiv preprint, 2026.
- Source: [paper](https://arxiv.org/abs/2611.03392v1); [full text reviewed](https://arxiv.org/pdf/2611.03392v1).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Sections 3.3–5: traffic proxy, measurement domains, idle subtraction, and scaling fits.
- Evidence: Ten-device edge comparison; power measured on six devices.

## What it establishes

CNN latency correlates more closely with the paper's traffic proxy than MAC counts on the evaluated accelerators. Total energy and energy above idle can produce different device rankings.

## Relevance to our goals

A recent counterexample to classifying CNNs as intrinsically compute-bound; encourages reporting measurement boundaries and baseline energy.

## Limits and transfer conditions

Fits use only three or four CNN points per device, and traffic counts each tensor once. Correlation does not directly measure saturated bandwidth; idle subtraction does not equalize different measurement domains.
