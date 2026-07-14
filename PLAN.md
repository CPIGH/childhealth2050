# Child Health 2050 — Website Plan

> Working title of the platform: **Compass by Child Health 2050**.
> Public URL: **childhealth2050.org** (GoDaddy domain, DNS to be pointed at GitHub Pages later).
>
> This is a living plan. We are "building the ship as we sail it" — expect this file
> to change. It supersedes the more elaborate infrastructure in the original 90-day
> concept note (see [`broad context document/`](broad%20context%20document/)); where the two
> disagree, this plan and the [decision log](docs/DECISIONS.md) win.

---

## 1. What we are building

A public dashboard that helps people answer one core question:

> **"What can I learn from countries like mine that achieved better child health outcomes?"**

The goal is **not** a perfect platform. It is the smallest genuinely useful version that
demonstrates that comparative-learning value, then grows.

The site is organized as a **landing page** that routes to four tools:

| # | Tool | Path | What it does |
|---|------|------|--------------|
| 1 | **Country Profiles** | [`/profiles`](profiles/) | Per-country scorecard: indicators, equity, financing, future outlook, and a short "what makes this country unique" narrative. |
| 2 | **Indicator Explorer** | [`/data`](data/) | Browse and compare indicators across countries and time; historical trends and indicator switching. |
| 3 | **Countries Like Mine** | [`/countries-like-mine`](countries-like-mine/) | Find comparator countries by baseline indicator, income, poverty, governance, health spending — and surface "positive deviants" that did better. |
| 4 | **Future Trajectories** | [`/trajectories`](trajectories/) | Baseline forecasts to 2050 with uncertainty and historical comparison. |

A **Cause Explorer** (cause-specific burden: e.g. neonatal prematurity/sepsis/asphyxia;
under-five pneumonia/malaria/diarrhea; stunting drivers) is called out in the concept note
as a "major differentiator." It starts as a feature inside Country Profiles / Indicator
Explorer and can graduate to its own tool later.

**Two things are treated as first-class requirements** (from Omar's email):

1. **Shareable links** — a user can copy a URL that reproduces their exact selection
   (country, indicator, year). Selection state lives in the URL query string.
2. **Social embedding** — pasting a tool link into social media / chat shows a good
   preview card (Open Graph / Twitter card image + title + description).

Both work identically whether we use subfolders or subdomains — see [DECISIONS](docs/DECISIONS.md).

---

## 2. Indicators (initial set)

From the concept note's master indicator inventory:

- **Mortality** — under-five mortality, neonatal mortality
- **Nutrition** — stunting, wasting
- **Coverage** — DTP3, MCV1
- **Burden** — major causes of death, major causes of DALYs
- **Equity** — by wealth, sex, urban/rural

**Sources** — IGME, GBD, World Bank, DHS/MICS, WHO. Almost all update annually at most, so
data refresh is a manual, low-frequency task (see [DATA-PIPELINE](docs/DATA-PIPELINE.md)).

Much of the initial content is expected to come from Gavin's and Ipchita's country-profile
work and from the forthcoming five-indicators paper.

---

## 3. How it's hosted (architecture in one paragraph)

A **static site on GitHub Pages**, served from this single repository at `childhealth2050.org`.
No backend server, no database. Each tool is a **subfolder** that maps directly to a URL path
(`/profiles`, `/data`, …). The site loads small, pre-processed, rounded **data files only
when a figure is opened**, keeping each visit light (~5–20 MB typical). GitHub Pages gives
~1 GB storage and enough bandwidth for roughly a few thousand visits/month at these sizes —
plenty to start, and repos can be split later if we outgrow it.

Full detail: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).
Why subfolders instead of subdomains: [docs/DECISIONS.md](docs/DECISIONS.md).

---

## 4. How content gets edited (without touching code)

Human-written text lives under [`content/`](content/), organized so each author edits only their
section:

- **Country profiles are Word documents** (`content/profiles/<country>.docx`). Non-technical authors
  edit them in Word; the site renders the `.docx` directly in the browser (via mammoth.js) — no
  Markdown, no conversion step. ([ADR-006](docs/DECISIONS.md).)
- **Site copy and indicator notes are Markdown** (`content/site/`, `content/indicators/`) — lighter
  text, optionally edited in a WYSIWYG Markdown app.

Authors are also shielded from GitHub: the Box folder shares files, and a maintainer (or a scheduled
auto-push) publishes to the live site. This removes the pressure to polish everything before shipping
and avoids pulling in a developer for small edits.

Guide for editors: [docs/CONTENT-EDITING.md](docs/CONTENT-EDITING.md).

---

## 5. How data gets processed

Raw and intermediate data stay **off git** — kept locally in [`data-processing/`](data-processing/)
(`raw/` and `intermediate/`), never committed. The **processing scripts** in
[`data-processing/scripts/`](data-processing/) *are* committed, and their output — the **cleaned,
lean data files** the site actually reads — is written to [`assets/data/`](assets/data/) and
committed. Because sources update at most annually, the pipeline is run manually when a new release
lands — no automation required to start.

Detail: [docs/DATA-PIPELINE.md](docs/DATA-PIPELINE.md).

---

## 6. Repository structure

```
childhealth2050/                 repo root = site root (served at childhealth2050.org)
├── index.html                   landing page → links to the four tools
├── PLAN.md                      this file
├── README.md                    developer-facing overview
├── assets/                      shared CSS / JS / images + assets/data/ (cleaned data files)
├── content/                     editable Markdown text, grouped by section
├── data-processing/             pipeline scripts (committed); raw/ + intermediate/ stay OFF git
├── profiles/                    Tool 1 — Country Profiles
├── data/                        Tool 2 — Indicator Explorer (a subsite, not storage)
├── tools/                       maintainer scripts (e.g. regenerate the profiles list)
├── countries-like-mine/         Tool 3 — Countries Like Mine
├── trajectories/                Tool 4 — Future Trajectories
├── docs/                        architecture, decisions, editing & deployment guides
└── broad context document/      original concept note + email (context; not published)
```

Every folder above contains a `README.md` describing its purpose and conventions.

---

## 7. Roadmap

The original concept note laid out a 12-week schedule. We keep its **feature sequence** but
adapt the **infrastructure** to the simpler static approach above. Treat weeks as ordering,
not deadlines.

**Phase 0 — Skeleton (this scaffold).** Repo structure, docs, decisions recorded. No data yet.

**Phase 1 — Foundation & data.** Finalize MVP scope and navigation; build the master indicator
inventory + data dictionary; acquire and harmonize the first datasets into `data/`; stand up the
landing page and a working shell for one tool.

**Phase 2 — Core tools.** Country Profiles (scorecard + narrative), Indicator Explorer
(trends + indicator switching), Cause Explorer views, and the "Countries Like Mine" comparator.

**Phase 3 — Comparative learning & trajectories.** Positive-deviant rankings, a compare-countries
workspace, baseline 2050 forecasts with uncertainty, then internal + stakeholder testing toward a
Version 1.0.

**Documentation deliverables** across phases: user guide, technical docs, data dictionary,
methodology note.

---

## 8. Explicitly out of scope (Version 2+)

Do **not** build these yet: strategy simulator, AI recommendation engine, full policy database,
automated briefing generation, budget optimization. The objective is to validate the core
comparative-learning workflow first.

---

## 9. Open questions / decisions still pending

- **Static tooling.** Plain HTML/CSS/JS vs. a static-site generator that renders the `content/`
  Markdown (e.g. Astro, Eleventy, Jekyll). Leaning toward starting plain and adopting a generator
  only if the content volume justifies it. See [DECISIONS](docs/DECISIONS.md).
- **Charting library** for the interactive figures (whatever the current dashboard already uses is
  the natural default).
- **Exact folder/URL names** — `data`, `countries-like-mine`, `trajectories` are provisional
  and cheap to rename now, expensive after we share links publicly.
- **Repo visibility.** If the repo is public (simplest free Pages), the `broad context document/`
  folder (internal email) must not be published — currently git-ignored for safety. See
  [DEPLOYMENT](docs/DEPLOYMENT.md).
- **Timing.** Omar's preference was to wait until related papers/profile materials mature and a
  Claude Code subscription is in place before investing heavily. This scaffold is deliberately
  content-free so it's ready when that content arrives.
