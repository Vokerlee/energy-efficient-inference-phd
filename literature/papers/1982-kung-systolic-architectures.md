# Why Systolic Architectures?

- Citation key: `kung1982systolic`.
- Authors: Kung, H. T..
- Publication: Computer, 1982.
- Source: [paper](https://doi.org/10.1109/MC.1982.1653825); [full text reviewed](https://www.eecs.harvard.edu/~htk/publication/1982-kung-why-systolic-architecture.pdf).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Scanned pages 37–38: regularity, local communication, and I/O balance.
- Evidence: Architectural argument, not modern neural-inference measurements.

## What it establishes

Describes rhythmic movement through regular processing elements, allowing repeated computation per external access. Discusses balancing concurrency with communication and decomposition when problems exceed the device.

## Relevance to our goals

Explains the systolic assumptions our runtime should preserve: local reuse, bounded storage, regular schedules, and finite hardware.

## Limits and transfer conditions

Historical qualitative principles do not determine current energy, supported precision, or the cost of adaptive control.
