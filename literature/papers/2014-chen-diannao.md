# DianNao: A Small-Footprint High-Throughput Accelerator for Ubiquitous Machine-Learning

- Citation key: `chen2014diannao`.
- Authors: Chen, Tianshi; Du, Zidong; Sun, Ninghui; Wang, Jia; Wu, Chengyong; Chen, Yunji; Temam, Olivier.
- Publication: ASPLOS, 2014.
- Source: [paper](https://users.cs.duke.edu/~lkw34/papers/diannao-asplos2014.pdf).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Neural functional unit, buffering, numerical format, and evaluation methodology.
- Evidence: 65 nm post-layout design estimates and workload evaluation.

## What it establishes

Organizes neural computation into multiplications, reduction, and nonlinear stages with specialized buffers. Emphasizes memory costs and uses truncated 16-bit fixed-point arithmetic.

## Relevance to our goals

A concrete reduction-oriented alternative to relying on a conventional two-dimensional systolic organization.

## Limits and transfer conditions

Its arithmetic and benchmark assumptions are historical. Comparisons with a SIMD baseline do not rank modern vector hardware or prove our adaptation benefits.
