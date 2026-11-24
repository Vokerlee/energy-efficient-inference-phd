# A Tile-Fusion Method for Accelerating Winograd Convolutions

- Citation key: `ji2021winogradfusion`.
- Authors: Zeyu Ji; Xingjun Zhang; Zheng Wei; Jingbo Li; Jia Wei.
- Publication: Neurocomputing460,9–19,2021; DOI10.1016/j.neucom.2021.06.003.
- Source: [publisher record](https://www.sciencedirect.com/science/article/pii/S0925231221008985).
- Reviewed: 2026-11-24. Status: **primary indexed abstract and publisher section excerpts**. Full OpenReview copy encountered a browser-verification challenge; full paper not read.

## Relevance and limits

Uses a layer-dependent arithmetic-complexity model to select Winograd tile sizes
and reduce total inference overhead. The inspected material distinguishes
multiplication work from input/filter/output-transform costs.

A comparator against claiming shape-aware Winograd selection itself as new.
The available excerpts do not settle every precision-dependent K-packing,
current-input controller or finite-buffer case. Detailed numerical and mapping
mechanisms require full-paper inspection; reported speedups were not reproduced.
