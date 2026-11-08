# Accelergy: An Architecture-Level Energy Estimation Methodology for Accelerator Designs

- Citation key: `wu2019accelergy`.
- Authors: Wu, Yannan N.; Emer, Joel S.; Sze, Vivienne.
- Publication: IEEE/ACM International Conference on Computer-Aided Design (ICCAD), 2019.
- Source: [paper](https://accelergy.mit.edu/paper.pdf).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Sections 1–3 and Eyeriss validation.
- Evidence: Action-based energy estimation with component-level reference validation.

## What it establishes

Combines action counts with energy reference tables for primitive and compound components. Repeated accesses and different data patterns can require distinct action categories.

## Relevance to our goals

Offers a way to account for detectors, converters, buffers, interconnect, and arithmetic separately while hardware descriptions remain abstract.

## Limits and transfer conditions

Accuracy depends on event counts and characterized components. Validation on Eyeriss is not an accuracy guarantee for our design, another process node, or dynamic quantization circuitry.
