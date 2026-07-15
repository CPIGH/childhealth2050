# Decision log

Short records of choices that shape the project, so we remember *why* later. Newest at the top.
Each entry: the decision, the context, and what would make us revisit it.

---

## ADR-007 — Standardized, AI-generated profile text with clear labeling

**Decision:** The main country profile page should use standardized, rubric-based narrative text that
can be populated by AI at first and later reviewed and rewritten by authors. The text should always
be labeled clearly as an AI-generated draft until it has been reviewed.

**Context:** The project now needs a scalable way to produce country-profile context for many countries
without waiting for fully authored prose for every page. The goal is to provide usable background
context quickly while still leaving room for author refinement.

**Why this over the alternatives:**

- **vs. waiting for full author copy for every country:** it lets the site launch with usable content
  faster.
- **vs. treating the main profile page as a full long-form document:** it keeps the page concise,
  structured, and easier to compare across countries.
- **vs. hiding the AI origin:** clear labeling preserves trust and makes revision easier.

**Revisit if:** the profile page needs to become a fully authored narrative experience, or the AI draft
workflow proves too unreliable for the intended use.

---

## ADR-008 — Searchable country tree and default-first comparator flow

**Decision:** Country selection should be implemented as a searchable tree, and the "Countries Like
Mine" tool should have a simple default path that uses an automated similarity match while still
offering a manual customization panel for advanced users.

**Context:** The site needs to support a large set of countries without making selection feel like a
long dropdown. The comparator also needs to remain simple for first-time visitors while still giving
experts a way to adjust the logic.

**Why this over the alternatives:**

- **vs. a single flat country list:** a searchable tree is easier to navigate as the country set grows.
- **vs. forcing the user to choose every comparator setting up front:** default-first flows reduce the
  cognitive load and keep the experience approachable.
- **vs. a fully manual comparator only:** automated defaults make the value proposition clearer at a
  glance.

**Default behavior:** the automated flow should show a small number of comparator countries by default
(for example, the three closest matches), while the user can change the number and the selection
logic through a compact settings control.

---

## ADR-006 — Deepdives authored in Word (.docx), rendered client-side

> **Scope narrowed (see ADR-007).** This originally covered the *whole* Country Profile. The model has
> since split: the main profile page is figures + tables + standardized short text (ADR-007), and the
> Word-document workflow below now applies only to the optional, richer country **deepdives** — not to
> the base profile. The .docx mechanism itself is unchanged; only *what* it authors is narrower.

**Decision:** Country **deepdive** authors edit ordinary **Word documents** in
[content/profiles/deepdives/](../content/profiles/) (<country>.docx). The site fetches the .docx and
renders it in the browser with mammoth.js. No Markdown for deepdives, and no conversion step — the
.docx is the single source of truth. A _TEMPLATE.docx seeds new deepdives. A deepdive is optional per
country; where one exists, the profile shows a prominent link to it and the country is flagged in the
selection tree.

**Context:** The deepdive authors are non-technical and unlikely to want Markdown or GitHub. The
initial plan already floated keeping Word files with a .docx → .md conversion. Two sub-problems
were separated: (a) authoring format and (b) publishing to GitHub — authors are shielded from both.

**Why this over the alternatives:**

- **vs. plain Markdown:** authors never learn .md syntax; they stay in Word.
- **vs. Word → pandoc → Markdown:** no conversion step for anyone to run, and no risk of the source
  .docx and a generated .md diverging.
- **vs. a WYSIWYG Markdown editor:** no new app for authors to adopt.

**Revisit if:** per-visit conversion gets heavy, profiles need richer formatting than mammoth preserves,
or authors turn out to prefer Markdown after all. Site copy and indicator notes remain Markdown for
now and could adopt the same Word approach later.

---

## ADR-005 — Flat repo served from root; subsites at root, workshop kept separate

**Decision:** Serve the whole repository from its **root** (the default GitHub Pages setup). The four
tools stay at the **top level** (/profiles, /data, …) for short, shareable URLs — they are *not*
nested inside a tools/ folder. Working files stay in clearly-named top-level folders
[data-processing/](../data-processing/), [docs/](.), [content/](../content/) but are simply never
linked. Cleaned data files go in [assets/data/](../assets/data/).

**Reason:** This is the simplest way to maintain one shared site and one shared data store without a
build step or a more complicated deployment setup.

---

## ADR-001 — Subfolders, not subdomains, for the four tools

**Decision:** Serve the tools as **path subfolders** of one domain and one repository rather than as
subdomains across separate repositories.

**Reason:** One repo, one deployment, one shared design system, and simple shareable links all point
strongly toward subfolders.

---

## ADR-002 — Static site on GitHub Pages (no backend)

**Decision:** Build a **static** site (HTML/CSS/JS + pre-processed data files) hosted on **GitHub Pages**.
No application server, no database.

**Reason:** It meets the current requirements with the least infrastructure.

---

## ADR-003 — Human text as Markdown; raw data outside the repo

**Decision:** Written content lives as Markdown under [content/](../content/), editable without code.
Raw and intermediate data stay **off git**; only the cleaned lean files are committed under
[assets/data/](../assets/data/); processing scripts live in [data-processing/](../data-processing/).

---

## ADR-004 — Naming: /data is the Indicator Explorer; data files live in assets/data/

**Decision:** The four tool folders are profiles, data (Indicator Explorer), countries-like-mine,
and trajectories. The cleaned data files the site fetches live in assets/data/, not in a top-level
data/.

**Reason:** /data reads naturally as the indicator tool, while assets/data is the data store the pages
fetch.
