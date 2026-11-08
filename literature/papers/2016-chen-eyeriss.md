# Eyeriss: A Spatial Architecture for Energy-Efficient Dataflow for Convolutional Neural Networks

- Citation key: `chen2016eyeriss`.
- Authors: Chen, Yu-Hsin; Emer, Joel; Sze, Vivienne.
- Publication: ACM/IEEE International Symposium on Computer Architecture (ISCA), 2016.
- Source: [paper](https://eems.mit.edu/wp-content/uploads/2016/04/eyeriss_isca_2016.pdf).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Energy hierarchy, fair dataflow comparison, and AlexNet evaluation.
- Evidence: Architectural energy analysis with fabricated-design validation.

## What it establishes

Compares CNN dataflows under matched area and parallelism. Row-stationary execution exploits activation, weight, and partial-sum reuse; reported convolution energy-efficiency gains span 1.4–2.5× against the evaluated alternatives.

## Relevance to our goals

Shows why reducing operand and partial-sum movement remains relevant when convolutions contain substantial arithmetic.

## Limits and transfer conditions

The ratios concern the paper's AlexNet mappings and technology assumptions. They neither establish a universal CNN energy breakdown nor directly predict benefits on our systolic array.
