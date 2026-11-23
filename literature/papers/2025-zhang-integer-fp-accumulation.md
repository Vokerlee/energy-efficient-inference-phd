# Transforming floating-point addition into integer addition for artificial intelligence applications

- Citation key: `zhang2025integerfpaccum`.
- Authors: Chuanjun Zhang; Leonardo Borges; Mitchell Diamond; Olivier Franza.
- Publication: 2025.
- Source: [record](https://patents.google.com/patent/US20250284460A1/en); [reviewed text](https://patents.google.com/patent/US20250284460A1/en).
- Reviewed: 2026-11-23. Status: **technical-description focused reading; patent application**.
- Reading focus: US20250284460A1, published 2025-09-11: descriptions of Figures 27–37, dynamic exponent cache, overflow and finalization.

## What it establishes

Describes exponent-tagged integer intermediate accumulation, bounded alignment shifts, impending-overflow flushing and a floating finalizer that can be gated between events. Inputs and outputs can retain floating formats.

## Relevance to our goals

Integer intermediates with floating outputs and a dynamically enabled normalizer are already described in hardware prior art.

## Limits and transfer conditions

A published design description is not proof of a released implementation or independently measured savings. Compare cache rows, flushing, shifts, finalization and state with a proposed primitive-local mechanism. This review records technical prior art and makes no patent-scope determination.
