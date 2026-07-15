# Architecture

## The shape of it

A **single static site**, one repository, served on **GitHub Pages** at childhealth2050.org. The
repo root is the site root. Each tool is a **subfolder → URL path**. There is no backend and no
database; the browser loads pre-processed data files directly.

```
Browser ──GET──▶ GitHub Pages (childhealth2050.org)   [served from the repo root]
                 ├── /                      index.html (landing page)
                 ├── /profiles/             Country Profiles          }
                 ├── /data/                 Indicator Explorer        }  the four
                 ├── /countries-like-mine/  Countries Like Mine       }  subsites
                 ├── /trajectories/         Future Trajectories       }
                 ├── /assets/               shared css/js/img
                 └── /assets/data/          lean JSON/CSV, fetched on demand
```

The whole repo is served from its root (the standard zero-config GitHub Pages setup). Working
folders like [data-processing/](../data-processing/) and [docs/](.) are committed and therefore also
publicly reachable by URL, but nothing links to them and nothing sensitive is ever committed — see
[DECISIONS.md ADR-005](DECISIONS.md). A [.nojekyll](../.nojekyll) file at the root tells Pages to serve
every file verbatim (no Jekyll build), so all folders behave predictably.

Note the two “data” names: /data/ is the Indicator Explorer page; /assets/data/ is the folder of data
files the pages fetch. Different things.

See [DECISIONS.md](DECISIONS.md) for why subfolders (ADR-001), why static (ADR-002), and the repo
layout (ADR-005).

## Product experience model

The site should feel like a dashboard first, but with country profiles as a richer second layer:

- The **Indicator Explorer** should remain the main place for comparative data views and indicator
  switching.
- The **Country Profiles** page should present figures, tables, and concise background statistics for a
  selected country, plus a standardized narrative section that can be AI-generated at first and later
  rewritten by authors.
- When available, a **deep dive** should be linked prominently from the profile page without making the
  main profile page feel like a long-form document.
- The **Countries Like Mine** experience should offer a simple default comparator path and a compact
  customization panel for users who want to adjust the selection logic.

## Country selection and comparator defaults

A country picker is a first-class UX requirement:

- It should behave like a **searchable tree** so the user can find any country quickly (all countries,
  grouped — by region by default; see [DECISIONS.md ADR-008](DECISIONS.md)).
- Where an author **deep dive** exists for a country, the tree should **flag that country** (an
  indicator/badge) so users can spot the countries with richer content.
- It should keep the default path simple: the site selects a country and a small number of default
  comparator countries automatically (**the 3 closest by default**, user-changeable).
- Advanced choices — number of comparators, weighting logic, custom dimensions — should be available
  in a compact settings control rather than forced up front.
- The current selection state should live in the URL query string so copied links reproduce a view.

## Data loading strategy (keep visits light)

This is the core performance idea, carried over from the current dashboard:

- Data files are **small, pre-processed, and rounded** — not raw survey microdata.
- A file is **fetched only when the user opens the figure that needs it**, not up front.
- Data is **split across files** so each fetch stays small.
- Result: a typical visit transfers a modest amount of data, well within the GitHub Pages budget.

Practical rules of thumb:

- Prefer many small files over one big file; lazy-load.
- Round numbers to the precision the charts actually show.
- Keep anything the site never reads (raw/intermediate data) **out of the repo** entirely.

## Shared vs. per-tool code

- **Shared** (in [assets/](../assets/)): the design system, the header and navigation used by every
  tool, the country selection UI, shared chart helpers, and the social-preview image.
- **Per-tool** (in each tool folder): the page(s) and logic specific to that tool.

## Shareable links & social embedding (first-class)

- **Selection state lives in the URL query string** (for example, /profiles/?country=NGA).
- **Each page sets its own Open Graph / Twitter meta tags** so links unfurl nicely when shared.

## Responsive + light/dark (first-class)

Every page and every tool — including charts — must work well on **desktop and mobile** and in both
**light and dark mode**. Treat these as non-negotiable while building.

## Tooling: undecided, deliberately

The scaffold is framework-agnostic. Two realistic paths remain:

1. **Plain HTML/CSS/JS.** Closest to the current dashboard, minimal build step, easiest to inspect.
2. **A static-site generator** that renders the [content/](../content/) Markdown into pages.

Recommendation: start plain, revisit once there is enough real content to justify more structure.

## What is intentionally NOT here

No server, database, auth, or user-generated content. All computation (comparator matching,
forecasts, and cause breakdowns) is precomputed in [data-processing/](../data-processing/) or done
client-side. If a future feature truly needs a server, that will be a conscious re-architecture.
