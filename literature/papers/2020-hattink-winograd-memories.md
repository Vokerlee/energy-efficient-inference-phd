# A Scalable Architecture for CNN Accelerators Leveraging High-Performance Memories

- Citation key: `hattink2020winograd`.
- Authors: Maarten Hattink; Giuseppe Di Guglielmo; Luca P. Carloni; Keren Bergman.
- Publication: HPEC 2020.
- Source: [author PDF](https://sld.cs.columbia.edu/pubs/hattink_hpec20.pdf).
- Reviewed: 2026-11-24. Status: **full-text focused reading**, Section III and Figures 1–3.

## Contribution and relevance

Implements Winograd with input/output row buffers, pretransformed weights and
high-bandwidth memory. Spatial output contributions are accumulated after
inverse transformation. Its unrolled variant can first combine multiple
contributions before transforming, trading additions against parallel resources.

## Comparison boundary

Inverse-before-channel-sum execution and spatial partial-output retention are
already architectural techniques. A numerical experiment comparing these orders
must not claim the reordering itself as new. Fixed-point widths, buffering and
external-memory configuration differ from a BF16/FP32 matrix interface. The
review does not reproduce the FPGA performance measurements.
