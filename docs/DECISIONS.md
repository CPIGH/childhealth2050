# Decision log

Short records of choices that shape the project, so we remember *why* later. Newest at the top.
Each entry: the decision, the context, and what would make us revisit it.

---

## ADR-006 — Country profiles authored in Word (.docx), rendered client-side

**Decision:** Country-profile authors edit ordinary **Word documents** in
[`content/profiles/`](../content/profiles/) (`<country>.docx`). The site fetches the `.docx` and
renders it in the browser with [mammoth.js](https://github.com/mwilliamson/mammoth.js) (vendored at
`assets/js/mammoth.browser.min.js`). No Markdown for profiles, and **no conversion step** — the
`.docx` is the single source of truth. A `_TEMPLATE.docx` seeds new profiles.

**Context:** The profile authors are non-technical and unlikely to want Markdown or GitHub. Omar's
email already floated keeping Word files with a `.docx → .md` conversion. Two sub-problems were
separated: (a) *authoring format* and (b) *publishing to GitHub* — authors are shielded from both.

**Why this over the alternatives:**

- **vs. plain Markdown:** authors never learn `.md` syntax; they stay in Word.
- **vs. Word → pandoc → Markdown:** no conversion step for anyone to run, and no risk of the source
  `.docx` and a generated `.md` diverging (there is no generated `.md`). Rendering happens in the
  browser instead.
- **vs. a WYSIWYG Markdown editor (Obsidian/Mark Text):** no new app for authors to adopt.

Cost accepted: mammoth is a ~600 KB vendored library, and each visit converts the `.docx` in the
browser. Both are fine at this scale (a handful of small profiles). Authors must use Word's built-in
**Heading 1/2/3 styles** and bullet lists for structure to map cleanly — mammoth keeps structure and
drops fussy formatting; the `_TEMPLATE.docx` is set up correctly.

**Auto-discovery via a generated manifest:** a static site can't list a folder at runtime, so
authors can't have "drop a file → link appears" for free. Bridged with a small manifest:
[`tools/build-profiles-index.py`](../tools/build-profiles-index.py) scans `content/profiles/` for
`*.docx`, skips `_`-prefixed files (template, instructions), and writes `profiles.json` (link label
= file name; `slug` = url-safe id). The Profiles page reads that manifest. The script runs at publish
time, so an author only drops a `.docx` named as they want the link to read — no list to hand-edit.

**Publishing (separate concern):** the shared Box folder distributes files among the team, but the
live GitHub Pages site still needs a `git push`. That is centralized to a maintainer (or a scheduled
auto-commit/push) who also runs the manifest script, so authors only ever save into Box. See
[CONTENT-EDITING](CONTENT-EDITING.md).

**Revisit if:** per-visit conversion gets heavy (precompute `.docx → HTML` at publish time with the
same engine), profiles need richer formatting than mammoth preserves, or authors turn out to prefer
Markdown after all. Site copy / indicator notes remain Markdown for now and could adopt the same
Word approach later.

---

## ADR-005 — Flat repo served from root; subsites at root, workshop kept separate

**Decision:** Serve the whole repository from its **root** (the default GitHub Pages setup). The four
tools stay at the **top level** (`/profiles`, `/data`, …) for short, shareable URLs — they are *not*
nested inside a `tools/` folder. Working files stay in clearly-named top-level folders
([`data-processing/`](../data-processing/), [`docs/`](.), [`content/`](../content/)) but are simply
never linked. Cleaned data files go in [`assets/data/`](../assets/data/).

**Context:** Once the folder layout settled, the open question was whether to *separate* the
published site from the working/tooling files — e.g. put the site in a `site/` subfolder and deploy
only that. That's a real and standard pattern for bigger projects.

**Why keep it flat for now:**

- **Simplest, and matches the plan.** Serving from root is the zero-config GitHub Pages setup Omar
  described. A `site/`-only deploy needs either the confusingly-named `/docs` publishing option or a
  GitHub Actions workflow — a moving part we don't need yet.
- **The only thing separation buys is "tooling files aren't publicly downloadable."** On a static
  host every committed file is fetchable by URL regardless; the safeguard that actually matters is
  *keeping sensitive things out of git*, which we already do (raw data + internal docs are
  git-ignored). The pipeline scripts and project docs being publicly reachable-but-unlinked is
  harmless.
- **It stays coherent with no-build + runtime Markdown.** With a plain (no-generator) site, the
  `content/` Markdown is fetched at runtime, so it has to be inside the served tree anyway. A clean
  "site vs. everything else" split really wants a static-site generator — the more elaborate path
  we're deliberately deferring (ADR-002).
- **Don't nest the subsites.** A `tools/profiles` layout would just add a pointless URL segment and
  muddy the shareable links Omar cares about.

A [`.nojekyll`](../.nojekyll) file makes Pages serve every folder verbatim (no Jekyll build), so
storage folders behave predictably.

**Revisit if** we want working files genuinely unpublished, or adopt a static-site generator — at
that point move the site into a `site/` folder and add a small GitHub Actions deploy (any folder
name), and/or move the pipeline to its own repo.

---

## ADR-001 — Subfolders, not subdomains, for the four tools

**Decision:** Serve the tools as **path subfolders** of one domain and one repository
(`childhealth2050.org/profiles`, `/data`, …) rather than as **subdomains** across separate
repositories (`profiles.childhealth2050.org`, `data.childhealth2050.org`, …).

**Status:** Adopted for the foreseeable future. Reversible (see migration path).

### Why (the reasoning behind the recommendation)

The original email floated per-tool subdomains, mainly because they read a little nicer and make
tidy links to share. Those are real but small benefits, and none of them are actually *lost* by
using subfolders. The things that matter here point clearly at subfolders:

1. **One repo with dependencies between the tools is the whole premise.** The tools share a
   design system, a navigation bar, utility code, and — importantly — the same data files (in
   `assets/data/`).
   With subfolders those are plain relative paths and imports. With subdomains, GitHub Pages
   gives **one custom domain per repository**, so each subdomain becomes its *own repo*, and the
   shared code/data turns into a cross-repo dependency (a published package, a git submodule, or
   copy-paste). That is exactly the coupling we were trying to keep simple.

2. **The two things Omar flagged as important — shareable links and social embedding — are
   path-agnostic.** `childhealth2050.org/profiles/?country=NGA` is just as shareable as
   `profiles.childhealth2050.org/?country=NGA`, and Open Graph / Twitter preview cards are set
   per-page (per-path), not per-domain. We give up nothing on either front.

3. **One deploy, one certificate, one DNS record.** Subfolders mean a single GitHub Pages build
   and a single `CNAME`. Subdomains mean N repos, N Pages configs, N `CNAME` records, and N TLS
   certificates to keep healthy — more moving parts for a small team.

4. **Easier for non-technical collaborators.** Everything — every tool, all the editable text —
   is in one place they can browse, instead of scattered across repositories.

5. **Cross-tool navigation stays instant and same-origin.** Moving from a profile to the
   data explorer is a same-site link, with no cross-origin quirks.

The main genuine advantage of subdomains is **independent storage and bandwidth budgets**: on
GitHub Pages each repo gets its own ~1 GB and its own soft bandwidth limit, so splitting tools
across repos multiplies headroom. But we are nowhere near those limits (current dashboard ~100 MB;
a visit loads ~5–20 MB), and the email itself notes we can "split subdomains across repositories
if we need more space." So this is a *future scaling lever*, not a reason to start complex.

### Migration path (so this isn't a one-way door)

If a tool later outgrows the shared repo, or we simply want the prettier `profiles.` links:

- **Split later:** move that tool to its own repo + subdomain and add a redirect from the old
  `/path`. URL query-based share links can be preserved.
- **Have both:** point a vanity subdomain (`profiles.childhealth2050.org`) at the subfolder
  (`childhealth2050.org/profiles`) via a redirect. We get the nicer shareable link without
  splitting the repo.

Because selection state lives in the **query string**, share links survive these moves.

### Revisit if

Any single tool approaches the ~1 GB repo limit or the Pages bandwidth soft cap; a tool needs an
independent deploy cadence or separate access control; or a partner wants to host one tool
themselves.

---

## ADR-002 — Static site on GitHub Pages (no backend)

**Decision:** Build a **static** site (HTML/CSS/JS + pre-processed data files) hosted on
**GitHub Pages**. No application server, no database.

**Context:** The original 90-day concept note sketched a full stack — Next.js/React frontend,
Python/FastAPI backend, PostgreSQL, DuckDB, deployed on Vercel. Omar's follow-up email
consciously simplified this: "as a starting point, GitHub Pages linked to the childhealth2050
url would be enough." The existing dashboard already works this way — small, rounded data files
loaded on demand when a figure is opened.

**Why:** It's the least infrastructure that meets the requirement, it's free, it matches what
already works, and it removes servers/databases as things to run and secure. The data is
low-frequency (annual at most) and read-only for visitors, so a live backend buys us little.

**Consequences:** All computation the "Countries Like Mine" comparator, forecasts, cause
breakdowns is done **ahead of time** in [`data-processing/`](../data-processing/) and shipped as
static files, or done **client-side** in the browser. Anything that genuinely needs a server (e.g.
heavy on-the-fly computation, private data, user accounts) would force a rethink — but nothing
in the current scope does.

**Revisit if** we need server-side computation, authentication, or write operations.

---

## ADR-003 — Human text as Markdown; raw data outside the repo

**Decision:** All written content lives as Markdown under [`content/`](../content/), editable
without code. Raw and intermediate data stay **off git**; only the cleaned lean files are committed,
under [`assets/data/`](../assets/data/); processing scripts live in
[`data-processing/`](../data-processing/). See ADR-004/005 for the folder specifics.

**Why:** Directly from Omar's email — let section owners edit their own text (optionally via a
`.docx → .md` step) without a developer, and keep the repo lean by never committing bulky raw
data. See [CONTENT-EDITING](CONTENT-EDITING.md) and [DATA-PIPELINE](DATA-PIPELINE.md).

---

## ADR-004 — Naming: `/data` is the Indicator Explorer; data *files* live in `assets/data/`

**Decision:** The four tool folders are `profiles`, **`data`** (Indicator Explorer),
`countries-like-mine`, `trajectories`. The cleaned data *files* the site fetches live in
**`assets/data/`**, not in a top-level `data/`.

**Why:** The email used `data.childhealth2050.org` as the example share link for the indicator tool,
so `/data` reads naturally as "the data section" people visit. That leaves the *files* needing a
different home; putting them under `assets/data/` (with the other served static assets — css, js,
img) keeps the finished data with the site and avoids any collision with the `/data` page. So:

- **`/data/`** = a page (subsite) — the Indicator Explorer.
- **`/assets/data/`** = the JSON/CSV files that page (and the others) fetch.

The two are easy to tell apart because of the `assets/` prefix.

**Still provisional:** `data`, `countries-like-mine`, `trajectories` are cheap to rename now and
expensive once links are shared publicly — worth a final confirmation before launch.
