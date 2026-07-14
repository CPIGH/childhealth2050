# data-processing/  ·  the data workshop

Turns **raw source data → the cleaned files the site serves**. This is the workshop; the
*finished product* is written out to [`assets/data/`](../assets/data/) (where the live site reads
it). See [docs/DATA-PIPELINE.md](../docs/DATA-PIPELINE.md).

```
data-processing/
├── raw/            source downloads (IGME, GBD, World Bank, DHS/MICS, WHO)   ← OFF git
├── intermediate/   working/harmonized files                                  ← OFF git
├── scripts/        the code that cleans + rounds + splits                     ← committed
└── README.md
```

Output ─▶ [`../assets/data/`](../assets/data/) (small, rounded, split; committed and served).

## What's committed vs. not

- **Committed:** `scripts/` (so the transformation is reproducible and reviewable) and the final
  files in `assets/data/`.
- **Off git:** everything in `raw/` and `intermediate/`. These stay local (they're bulky and don't
  belong on the published site). The empty folders are kept via `.gitkeep` so you know where to put
  things; their *contents* are git-ignored. See [`.gitignore`](../.gitignore).

## Cadence

Run **manually** when a new data release lands — sources update annually at most, so no automation
is needed to start. Add it later only if the manual step becomes a burden.

## Conventions (fill in when the first script lands)

- Keep the transformation deterministic: same `raw/` inputs → same `assets/data/` outputs.
- Round numbers to the precision the charts actually show; split files so each fetch stays small
  (by outcome, and by location if they get large).
- Processing is done in **R**. For reproducibility, capture package versions — an `renv.lock`
  (via [renv](https://rstudio.github.io/renv/)) committed alongside the scripts is ideal; at a
  minimum, record `sessionInfo()`.

Empty for now.
