# childhealth2050

Source for the **Child Health 2050 / Compass** public dashboard, served as a static site on
GitHub Pages at **childhealth2050.org**.

New here? Start with **[PLAN.md](PLAN.md)** for what we're building and why, then
[docs/](docs/) for the details.

## What this is

A single-repository, static **data dashboard**. The four tools are different ways to slice and
compare one shared dataset — one country at a glance, one indicator across countries, a country
against statistically-similar peers, or a country's path to 2050. Country Profiles also carry a
little standardized written context (AI-generated first, then author-rewritten) and, where available,
a link to a richer author **deep dive**. A landing page routes to four tools, each living in its own
subfolder that maps to a URL path:

| Folder | URL | Tool |
|--------|-----|------|
| [`profiles/`](profiles/) | `/profiles` | Country Profiles |
| [`data/`](data/) | `/data` | Indicator Explorer |
| [`countries-like-mine/`](countries-like-mine/) | `/countries-like-mine` | Countries Like Mine |
| [`trajectories/`](trajectories/) | `/trajectories` | Future Trajectories |

Supporting folders:

| Folder | Purpose |
|--------|---------|
| [`assets/`](assets/) | Shared CSS, JS, images, favicon, social card — and [`assets/data/`](assets/data/), the cleaned data files the site reads |
| [`content/`](content/) | Editable Markdown text, grouped by section |
| [`data-processing/`](data-processing/) | Pipeline scripts; `raw/` + `intermediate/` stay **off git**, output goes to `assets/data/` |
| [`docs/`](docs/) | Architecture, decision log, editing & deployment guides |

> Note: `data/` is the **Indicator Explorer page** (a subsite), not data storage. The data *files*
> live in `assets/data/`. See [docs/DECISIONS.md](docs/DECISIONS.md).

## View it locally

It's a static site — any local web server works. From the repo root:

```bash
python -m http.server 8000
```

then open <http://localhost:8000>. (Opening `index.html` directly via `file://` also works for
plain pages, but a server is needed once pages fetch data files.)

## Edit the words (no coding needed)

Human-written text lives under [`content/`](content/): site copy and indicator notes as Markdown,
per-country **standardized profile context** as structured text (AI-generated first, clearly labeled,
then authors rewrite it), and optional richer **deep dives** as Word (`.docx`) files. Find the file
for your section, edit it, save. See [docs/CONTENT-EDITING.md](docs/CONTENT-EDITING.md).

## Update the data

Raw data is processed in [`data-processing/`](data-processing/) (raw + intermediate stay off git);
only the cleaned final files land in [`assets/data/`](assets/data/), which the site reads.
See [docs/DATA-PIPELINE.md](docs/DATA-PIPELINE.md).

## Deploy

Public GitHub repo → GitHub Pages; the custom domain `childhealth2050.org` gets added once DNS
access is available. Routine content updates publish with `python tools/publish.py` (or
double-click `tools/publish.cmd`). See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md), including the note
on keeping internal material out of the public repo.

## Status

Early scaffold. The structure, docs, and a click-through skeleton exist — a landing page and four
placeholder tool pages with shared nav/styling. The current Country Profiles page is a placeholder
that renders a Word (`.docx`) file in the browser via mammoth.js; under the new plan that mechanism
moves to the optional **deep dives**, while the main profile page becomes figures + tables +
standardized (AI-labeled) text with a searchable country tree — not yet built. There's no real data
or finished tool yet; the structure is ready for content as the related papers and profile materials
mature. Every page must stay **responsive (desktop + mobile)** and **light/dark‑mode aware** — see
[PLAN.md](PLAN.md).
