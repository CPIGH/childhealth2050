# Country Profiles  ·  `/profiles`

**Tool 1 of 4.** A single-country home base that combines figures, tables, background statistics,
and a concise narrative context for the selected country.

## What it shows

- A **scorecard** across the main lenses from the concept note:
  - **Child Health Indicators** — mortality, nutrition, coverage
  - **Equity** — gaps by wealth, sex, urban/rural
  - **Financing**
  - **Future Outlook**
- A short standardized narrative section that can start as an **AI-generated draft** and later be
  reviewed and rewritten by authors.
- A prominent link to a fuller **country deep dive** when one is available.
- Entry points into the other tools scoped to this country (compare it, explore its trends,
  see its 2050 trajectory).

## Content & data

- **Country list** (drives the selection tree): [`assets/data/countries.json`](../assets/data/) —
  `{ name, slug, iso3, region }` per country. A starter list for now; to be replaced by the canonical
  set from [data-processing/](../data-processing/).
- **Standardized context** (short, AI-generated-first, then author-rewritten):
  [`content/profiles/standardized/<slug>.md`](../content/profiles/standardized/), one Markdown file per
  country under the fixed rubric in [`content/profiles/rubrics.md`](../content/profiles/rubrics.md).
  Frontmatter `status: ai-generated` makes the page show an **"AI-generated draft"** banner; changing
  it to `author-reviewed` removes the banner.
- **Deep dives** (optional, richer, Word documents):
  [`content/profiles/deepdives/<Country>.docx`](../content/profiles/deepdives/), rendered via
  mammoth.js. Listed in the generated `deepdives.json` (see below).
- **Numbers**: fetched on demand from [assets/data/](../assets/data/) (small, rounded, split files).

## Link sharing

Selection lives in the URL query string, for example `/profiles/?country=nigeria`, so a copied link
reopens the same country. Each country view sets its own Open Graph tags for nice social previews.
See [docs/ARCHITECTURE.md](../docs/ARCHITECTURE.md).

## Link sharing across the three views

Selection and view live in the query string:

- `/profiles/?country=nigeria` — the profile (figures + standardized context).
- `/profiles/?country=nigeria&view=deepdive` — the author deep dive, when one exists.

## How deep dives are discovered

A static site cannot list a folder at runtime, so
[`tools/build-deepdives-index.py`](../tools/build-deepdives-index.py) scans
`content/profiles/deepdives/` for `*.docx` (skipping `_`-prefixed files) and writes
`content/profiles/deepdives.json` at publish time (via [`tools/publish.py`](../tools/publish.py)). The
page reads that manifest to render a deep dive **and** to flag, in the selection tree, which countries
have one. A deep dive's slug comes from its filename and must match the country's slug in
`countries.json` (e.g. `Nigeria.docx` → `nigeria`).

## Status

The page is built as a working scaffold of the three-layer model: a **searchable country tree** (all
countries from `countries.json`, grouped by region, with a **deep-dive flag**); a **profile view**
with figures/tables placeholders plus the **standardized context** (rendered from Markdown, with the
AI-draft banner); and a **deep-dive view** that renders the author's `.docx`. The figures/tables and
real data are the remaining build-out.
