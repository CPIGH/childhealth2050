# assets/  ·  shared front-end assets

Everything shared across all four tools lives here, so one change updates the whole site. Because
the site is a single origin, tools reference these with plain relative paths (e.g.
`/assets/css/site.css`).

```
assets/
├── css/    design system: colors, type, spacing; shared layout & the site header/nav
├── js/     shared helpers + vendored libs (mammoth.browser.min.js renders authors' .docx)
├── img/    logo, favicon, and the social-preview (Open Graph) card image
└── data/   cleaned data files the site fetches (JSON/CSV) — output of data-processing/
```

## What belongs here

- The **navigation bar / header** used by every tool (a big reason the single-repo layout pays off).
- **Design tokens** (colors, fonts, spacing) so the tools look like one product.
- The **favicon** and the **social-preview image** referenced by pages' Open Graph tags.
- Shared JS utilities — notably the **URL query-string ↔ selection state** logic that makes links
  shareable (see [docs/ARCHITECTURE.md](../docs/ARCHITECTURE.md)).

## About `assets/data/`

These are the **cleaned, final** data files the charts fetch on demand — the *output* of
[`data-processing/`](../data-processing/). They live here (with the other served static assets)
rather than in the `data-processing/` workshop, so the finished product sits with the site and the
raw/intermediate inputs stay out of the repo. Note: `/data` (a top-level folder) is the **Indicator
Explorer subsite** — a different thing from `assets/data/` (the files).

## What does not belong here

- Editable prose → [`content/`](../content/). (Images *used by* prose do go in `assets/img/`.)

So far: `css/site.css` (shared styles) and `js/mammoth.browser.min.js` (vendored — renders Word
docs) exist; `img/` and `data/` are still empty placeholders.
