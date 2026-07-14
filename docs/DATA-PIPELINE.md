# Data pipeline

## Principle

**Raw and intermediate data stay off git.** Only the **cleaned, lean data files** the website
actually reads are committed. The split is by folder:

- [`data-processing/`](../data-processing/) — the **workshop**:
  - `raw/` — source downloads. **Off git** (kept locally).
  - `intermediate/` — working/harmonized files. **Off git.**
  - `scripts/` — the code that cleans, rounds, and splits. **Committed.**
- [`assets/data/`](../assets/data/) — the **finished product**: the small, rounded, split files the
  site fetches on demand. **Committed and served.**

This keeps the repo small (well under the ~1 GB Pages limit), keeps visits light, and keeps the
transformation reproducible without dragging gigabytes of source data along.

```
        data-processing/                              assets/data/
┌──────────────────────────────────┐            ┌────────────────────┐
│ raw/          (OFF git, local)    │  scripts/  │ cleaned files      │─▶ fetched by
│ (IGME, GBD, World Bank,           │ ─────────▶ │ small, rounded,    │   the browser
│  DHS/MICS, WHO)                   │  transform │ split by outcome/  │   on demand
│ intermediate/ (OFF git, local)    │  & round   │ location           │
└──────────────────────────────────┘            └────────────────────┘
        scripts/ are committed                    committed + served
```

## Sources (initial)

IGME, GBD, World Bank, DHS/MICS, WHO. Almost all update **annually at most**.

## Cadence: manual, low-frequency

Because releases are infrequent, the pipeline does **not** need to be automated to start. When a
new data release lands:

1. Drop the new raw files into [`data-processing/raw/`](../data-processing/) (local; off git).
2. Run the code in [`data-processing/scripts/`](../data-processing/).
3. It writes updated cleaned files into [`assets/data/`](../assets/data/).
4. Commit the changed `assets/data/` files (and any script changes); the site redeploys.

Automation can come later if the manual step ever becomes a burden.

## Conventions for cleaned data files

- **Small and split.** Split by outcome (already done on the current dashboard); split by location
  too if files get large, so each fetch stays small.
- **Rounded** to the precision the charts display — no spurious decimals.
- **Documented.** Maintain a data dictionary + metadata (indicator definitions, units, source,
  vintage) alongside the files in `assets/data/`.
- **Stable file names / schema.** The site fetches these by path; renaming a file or changing its
  columns can break a figure. Change deliberately.

## Keeping raw data out of git

`raw/` and `intermediate/` live inside `data-processing/` for local convenience, but their
**contents are git-ignored** — only a `.gitkeep` keeps each empty folder present. The
[`.gitignore`](../.gitignore) also catches a few other common raw-data patterns in case files land
somewhere unexpected.

Because the repo sits in a **shared Box folder**, this gives the team exactly the split we want:
drop raw files into `data-processing/raw/` and **Box syncs them to everyone on the team**, while git
keeps them **off the public site** (they're never committed or pushed). Team-accessible, not public,
no size worries — Box handles large files far better than git. (If the raw archive ever gets huge,
it can move to any other shared folder; git never touches it either way.)
