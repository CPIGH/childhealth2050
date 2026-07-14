# Architecture

## The shape of it

A **single static site**, one repository, served on **GitHub Pages** at `childhealth2050.org`.
The repo root is the site root. Each tool is a **subfolder → URL path**. There is no backend and
no database; the browser loads pre-processed data files directly.

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
folders like [`data-processing/`](../data-processing/) and [`docs/`](.) are committed and therefore
also publicly reachable by URL, but nothing links to them and nothing sensitive is ever committed —
see [DECISIONS.md ADR-005](DECISIONS.md). A [`.nojekyll`](../.nojekyll) file at the root tells Pages
to serve every file verbatim (no Jekyll build), so all folders behave predictably.

Note the two "data" names: **`/data/`** is the Indicator Explorer *page*; **`/assets/data/`** is the
folder of data *files* the pages fetch. Different things.

See [DECISIONS.md](DECISIONS.md) for *why* subfolders (ADR-001), *why* static (ADR-002), and the
repo layout (ADR-005).

## Data loading strategy (keep visits light)

This is the core performance idea, carried over from the current dashboard:

- Data files are **small, pre-processed, and rounded** — not raw survey microdata.
- A file is **fetched only when the user opens the figure that needs it**, not up front.
- Data is **split across files** (by outcome today; by location too, if needed) so each fetch is
  small. The five indicator figures are <1 MB each; mortality line charts usually <4 MB.
- Result: a typical visit transfers ~5–20 MB. Even a heavy 25 MB visit leaves room for a few
  thousand visits/month before approaching the Pages bandwidth soft limit.

Practical rules of thumb:

- Prefer many small files over one big one; lazy-load.
- Round numbers to the precision the charts actually show.
- Keep anything the site never reads (raw/intermediate data) **out of the repo** entirely.

## Shared vs. per-tool code

- **Shared** (in [`assets/`](../assets/)): the design system (colors, type, spacing), the header
  and navigation used by every tool, common chart helpers, the favicon and the social-preview
  image. Because everything is one origin, tools reference these with plain relative paths.
- **Per-tool** (in each tool folder): the page(s) and logic specific to that tool.

Keeping the nav and design tokens shared is a large part of why the single-repo/subfolder layout
pays off — one change updates all four tools.

## Shareable links & social embedding (first-class)

- **Selection state lives in the URL query string** (e.g. `/profiles/?country=NGA&indicator=u5mr`).
  Reading state from the URL on load, and writing it back as the user changes selections, is what
  makes a copied link reproduce a view. Design tools this way from the start — retrofitting is
  painful.
- **Each page sets its own Open Graph / Twitter meta tags** (title, description, and a preview
  image from `assets/`) so links unfurl nicely when shared. These are per-page, so subfolders vs.
  subdomains makes no difference here.

## Tooling: undecided, deliberately

The scaffold is framework-agnostic. Two realistic paths:

1. **Plain HTML/CSS/JS.** Closest to the current dashboard, zero build step, easiest for anyone to
   inspect. Good default for the MVP.
2. **A static-site generator** that renders the [`content/`](../content/) Markdown into pages
   (e.g. Astro — nice for interactive "islands" like charts; Eleventy; or Jekyll, which Pages
   builds natively). Worth adopting **if/when** the volume of written content makes hand-maintained
   HTML tedious.

Recommendation: start plain, revisit once there's real content. Whatever charting library the
current dashboard already uses is the natural default for figures. Tracked as an open question in
[PLAN.md](../PLAN.md) and [DECISIONS.md](DECISIONS.md).

## What is intentionally NOT here

No server, database, auth, or user-generated content. All "computation" (comparator matching,
forecasts, cause breakdowns) is precomputed in [`data-processing/`](../data-processing/) or done
client-side. If a future feature truly needs a server, that's a conscious re-architecture, recorded
as a new ADR.
