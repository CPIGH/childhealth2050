# Standardized country-profile context — rubric & instructions

This file defines the **standardized written context** that appears on every Country Profile page,
above and around the figures. It is the same short structure for every country, so profiles stay
comparable and easy to scan.

The text is **AI-generated first** (so no country is blank on day one), clearly **labeled as an
AI-generated draft**, and later **reviewed and rewritten by authors**. See
[docs/CONTENT-EDITING.md](../../docs/CONTENT-EDITING.md) and
[DECISIONS ADR-007](../../docs/DECISIONS.md).

> This is **not** the country deep dive. Deep dives are the longer, fully author-written Word
> documents in [`deepdives/`](deepdives/). The standardized context here is short and structured.

## Where it lives

One Markdown file per country in [`standardized/`](standardized/), named by the country's slug —
e.g. `standardized/nigeria.md`, `standardized/kenya.md`. The slug must match the country's slug in
[`assets/data/countries.json`](../../assets/data/countries.json) so the profile page can find it.

## File format

Each file starts with a small metadata block, then the fixed sections below:

```markdown
---
country: Nigeria
slug: nigeria
status: ai-generated        # ai-generated  →  author-reviewed  (drives the on-page label)
generated: 2026-07-15
---

## At a glance
...
```

- `status: ai-generated` makes the page show a visible **"AI-generated draft"** banner.
- When an author has reviewed and rewritten the text, change it to `status: author-reviewed`
  (and the banner disappears). That is the *only* switch needed.

## Fixed sections (keep these headings, in this order)

Keep each section to a few short sentences or a couple of bullets — this is orientation, not an essay.

1. **## At a glance** — one or two sentences placing the country: region, rough scale, the single
   most important thing to know about its child-health situation.
2. **## Recent progress** — what the trend has done lately (improving / stalling / worsening) for the
   headline indicators (under-five and neonatal mortality especially), in plain language.
3. **## Equity** — who is being left behind: gaps by wealth, sex, and urban/rural, where known.
4. **## Financing & context** — a line on health financing and any contextual factors (income,
   fragility, major recent shocks) that shape outcomes.
5. **## Outlook to 2050** — the direction of travel toward 2050 and whether current trends are on
   track for the goals. Keep forecasts qualitative here; the numbers live in Future Trajectories.
6. **## Key caveats** — data limitations, recency of the last survey, or comparability issues a
   reader should keep in mind.

## Instructions for AI generation

- Fill **every** section, using only the indicators and figures the site actually has for that
  country; do not invent specific numbers you cannot source. Prefer directional, qualitative
  statements ("neonatal mortality has fallen more slowly than under-five mortality") over precise
  figures unless the figure is in the dataset.
- Keep it **short, neutral, and comparable** across countries — same tone and structure everywhere.
- Do not editorialize or make policy recommendations.
- Always leave `status: ai-generated` so the draft is labeled until an author reviews it.
