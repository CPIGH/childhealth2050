# Child Health 2050 — Website Plan

> Working title of the platform: **Compass by Child Health 2050**.
> Public URL: **childhealth2050.org** (GoDaddy domain, DNS to be pointed at GitHub Pages later).
>
> This is a living plan. We are "building the ship as we sail it" — expect this file
> to change. It supersedes the more elaborate infrastructure in the original 90-day
> concept note (kept in the team's internal planning notes); where the two
> disagree, this plan and the [decision log](docs/DECISIONS.md) win.

---

## 1. What we are building

A public site that helps people answer one core question:

> **"What can I learn from countries like mine that achieved better child health outcomes?"**

At its core this is a **data dashboard**. The four tools are not four separate products — they
are four **ways to slice, compare, and emphasize the same underlying data**. Each subdirectory just
frames the numbers differently: one country at a glance, one indicator across countries, a country
against statistically-similar peers, or a country's path to 2050.

But it is **not *only* a dashboard.** Country Profiles, in particular, wraps the figures in a small
amount of **standardized written context** (see below), and some countries will get a richer
author-written **deepdive**. So think of it as a dashboard first, with light editorial context layered
on top.

The goal is **not** a perfect platform. It is the smallest genuinely useful version that
demonstrates that comparative-learning value, then grows.

The site is organized as a **landing page** that routes to four tools:

| # | Tool | Path | What it does |
|---|------|------|--------------|
| 1 | **Country Profiles** | [`/profiles`](profiles/) | Per-country dashboard: figures, tables and background statistics, plus a little standardized written context — and a prominent link to an author **deepdive** where one exists. |
| 2 | **Indicator Explorer** | [`/data`](data/) | Browse and compare indicators across countries and time; historical trends and indicator switching. |
| 3 | **Countries Like Mine** | [`/countries-like-mine`](countries-like-mine/) | Find statistically-similar countries (GDP, mortality, life expectancy, location, …) — automatically or on dimensions you choose — and surface "positive deviants" that did better. |
| 4 | **Future Trajectories** | [`/trajectories`](trajectories/) | Baseline forecasts to 2050 with uncertainty and historical comparison. |

A **Cause Explorer** (cause-specific burden: e.g. neonatal prematurity/sepsis/asphyxia;
under-five pneumonia/malaria/diarrhea; stunting drivers) is called out in the concept note
as a "major differentiator." It starts as a feature inside Country Profiles / Indicator
Explorer and can graduate to its own tool later.

### How the tools relate — one dataset, shared controls

Because the tools share one dataset, they also share the controls that pick what you look at:

- **Country selection is a searchable tree of *all* countries** (grouped, with a search box), used
  everywhere a country is chosen. Where an author **deepdive** exists, that country is flagged in the
  tree so users can find it. See [ARCHITECTURE](docs/ARCHITECTURE.md).
- **Defaults first, customization optional.** The site should be easy to navigate, so we never force
  a user through a wall of selections. Every control has a sensible **default**; deeper customization
  lives behind a **pop-up / drop-down** the user opens only if they want it. Defaults are encoded in
  the URL so shareable links still reproduce a view. This is a site-wide rule — see §1.1.

### 1.1 Design principle: defaults over decisions

Treat this as non-negotiable, alongside the four requirements below:

- Landing on any tool shows something useful **immediately**, with no required setup — a sensible
  default country / indicator / comparison is already applied.
- Anything beyond the default (change the comparison basis, add countries, switch indicator, tune the
  number of comparators, …) is **available but tucked away** — a drop-down, a "Customize" pop-up, an
  "Advanced" panel — not in the user's face.
- Whatever the user *does* choose is written to the **URL**, so the customized view is shareable and
  the default view stays clean.

**These are first-class requirements** — treated as non-negotiable from the start, on every page and
in every tool:

1. **Shareable links** — a user can copy a URL that reproduces their exact selection
   (country, indicator, year). Selection state lives in the URL query string.
2. **Social embedding** — pasting a tool link into social media / chat shows a good
   preview card (Open Graph / Twitter card image + title + description).
3. **Responsive** — works well on both desktop and mobile.
4. **Light and dark mode** — respects the visitor's system theme, and is legible in both.

Shareable links and social embedding work identically whether we use subfolders or subdomains — see
[DECISIONS](docs/DECISIONS.md). Notes on building for responsive + light/dark are in
[ARCHITECTURE](docs/ARCHITECTURE.md).

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

The site carries three *kinds* of text, and they are authored differently. Two of them live in a
Country Profile:

1. **Standardized profile context (AI-generated first, then rewritten by authors).** Each Country
   Profile includes a little written context under **fixed rubrics** — the same headings and prompts
   for every country (e.g. a one-line orientation, what's notable in the trend, key caveats). Because
   the rubrics are standardized and instruction-driven, we **seed every country's text with AI** so
   nothing is blank on day one, and **label it clearly as AI-generated**. Authors then work through
   countries and **rewrite** the AI draft; once a section is human-written, the AI label comes off.
   This is stored as structured text per country (not a Word doc). ([ADR-007](docs/DECISIONS.md).)
2. **Country deepdives (Word documents, by non-technical authors).** Some countries get a richer,
   longer, human-written **deepdive**. *These* are the Word documents non-technical authors edit
   (`content/profiles/deepdives/<country>.docx`), rendered in the browser via mammoth.js — no
   Markdown, no conversion step. A deepdive is **optional per country**; where one exists, the profile
   shows a **prominent link** to it and the country is flagged in the selection tree.
   ([ADR-006](docs/DECISIONS.md).)
3. **Site copy and indicator notes are Markdown** (`content/site/`, `content/indicators/`) — lighter
   text, optionally edited in a WYSIWYG Markdown app.

So the *main* profile page does **not** require the Word-document workflow — its context is the
standardized AI/authored text plus figures. The Word-document workflow is specifically for **deepdives**.

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
├── tools/                       maintainer scripts (e.g. regenerate the deepdive list)
├── countries-like-mine/         Tool 3 — Countries Like Mine
├── trajectories/                Tool 4 — Future Trajectories
├── docs/                        architecture, decisions, editing & deployment guides
└── broad context document/      internal planning notes (kept local, never published)
```

Every folder above contains a `README.md` describing its purpose and conventions.

Inside `content/profiles/` the two profile text kinds are kept apart (see §4):

```
content/profiles/
├── standardized/    per-country standardized context (AI-generated first, then author-rewritten)
├── deepdives/       optional per-country Word deepdives (.docx, rendered via mammoth.js)
├── rubrics.md       the fixed rubric headings + AI-generation instructions (shared by all countries)
├── _TEMPLATE.docx   starting point for a new deepdive
└── deepdives.json   generated manifest of which countries have a deepdive (drives the tree flag)
```

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
- **Country-tree grouping** — the searchable selection tree needs a grouping. Default assumption is
  **by region**; income-group grouping (or a toggle between them) is a possible refinement. See
  [ADR-008](docs/DECISIONS.md).
- **Comparator defaults** — "Countries Like Mine" defaults to the **closest 3** countries via an
  automated composite (GDP, mortality, life expectancy, location, …), user-changeable. The exact
  similarity method and dimension weights are a data-processing decision to finalize.
  See [ADR-008](docs/DECISIONS.md).
- **Repo visibility — settled.** The repo is public (free GitHub Pages); the internal planning
  notes stay git-ignored and were never committed. See [DEPLOYMENT](docs/DEPLOYMENT.md).
- **Timing.** The plan is to wait until related papers and profile materials mature before
  investing heavily. This scaffold is deliberately content-free so it's ready when that content
  arrives.
