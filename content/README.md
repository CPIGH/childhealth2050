# content/  ·  the website's editable text

Human-written content lives here so section owners can edit it without touching code. Full guide:
[docs/CONTENT-EDITING.md](../docs/CONTENT-EDITING.md).

## Layout

```
content/
├── site/         landing-page copy, About, shared blurbs   (Markdown .md)
├── profiles/     one Word document per country (Nigeria.docx); plus _TEMPLATE.docx,
│                 _READ-ME-FIRST.docx (instructions), and profiles.json (generated list)
└── indicators/   description & methodology note per indicator (Markdown .md)
```

The Country Profiles list is generated: [`tools/build-profiles-index.py`](../tools/build-profiles-index.py)
scans `profiles/` for `.docx`, skips `_`-prefixed files, and writes `profiles.json` (the list the
site reads). Authors just drop a Word file in; the link appears on the next publish.

Two formats, on purpose:

- **Country profiles are Word documents (`.docx`).** Non-technical authors edit them in Word; the
  site renders them directly (via mammoth.js). No Markdown, no conversion step. Start from
  `profiles/_TEMPLATE.docx`.
- **Site copy and indicator notes are Markdown (`.md`).** Lighter text, currently authored as `.md`
  (optionally in a WYSIWYG editor). Can move to the same Word approach later if useful.

## Rules of thumb

- **One file per section**, named after the thing it describes (`nigeria.docx`, `stunting.md`).
- Keep the folder each file belongs in — pages look for content by path.
- **Don't rename/move** a file without flagging it; something may point at it.
- The file in `content/` is the **single source of truth** — don't keep a second copy elsewhere.
- Images referenced from text go in [`assets/img/`](../assets/img/), not here.

Mostly empty for now. Placeholders demonstrate the structure: `site/about.md`, a Word
`profiles/_TEMPLATE.docx` + `profiles/_READ-ME-FIRST.docx`, and two country stubs
(`profiles/Nigeria.docx`, `profiles/Kenya.docx`) the Country Profiles page renders. Real content
gets added as the profiles and five-indicator write-ups mature.
