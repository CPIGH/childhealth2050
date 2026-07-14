# Editing the website's text (no coding required)

You don't need to know code, Markdown, or GitHub to write content. There are two separate things,
and section authors are shielded from both:

1. **Writing** — country profiles are ordinary **Word documents**. You edit the `.docx` and save.
2. **Publishing** — getting your change onto the live website is a maintainer's job (see the last
   section). You never touch GitHub.

---

## Country profiles — just edit a Word file

Each country's profile is a Word document in the [`content/profiles/`](../content/profiles/) folder.
The website reads the Word file directly and renders it as a page (using
[mammoth.js](https://github.com/mwilliamson/mammoth.js)). There is **no Markdown and no conversion
step** — the `.docx` is the real thing. The full instructions also live in that folder as
`_READ-ME-FIRST.docx`, so authors see them right where they work.

**To edit an existing profile:** open its `.docx` from the Box folder, make your changes in Word,
save. Done.

**To add a new country:**

1. Copy [`_TEMPLATE.docx`](../content/profiles/) and rename the copy to the country name **exactly as
   you want it to appear as a link** — e.g. `Ethiopia.docx`, or `Democratic Republic of the Congo.docx`.
   The file name becomes the link text.
2. Write the content in Word and save it in the folder.
3. That's it — the link appears on the Country Profiles page the next time the site is **published**
   (a script re-scans the folder; you don't edit any list yourself).

Files whose name starts with an underscore (`_TEMPLATE.docx`, `_READ-ME-FIRST.docx`) are **ignored**
by the site — handy for helper files you don't want to show up as links.

### Make it render nicely — use Word's Heading styles

The site keeps your document's **structure** (headings, lists, bold) and drops fussy formatting
(fonts, colours, sizes). So structure it with Word's built-in tools, not by hand:

- Use the **Heading 1 / Heading 2 / Heading 3** styles (the Styles gallery on Word's Home tab) for
  titles and section headings — *not* just big bold text.
- Use the **bullet-list** button for lists.
- **Bold** and *italic* work as usual.
- Keep it simple. (Images and tables can come later — check with the maintainer first.)

The `_TEMPLATE.docx` is already set up this way; starting from it is the easiest path.

---

## Other text (landing page, About, indicator notes)

Site-wide copy and per-indicator notes currently live as **Markdown** (`.md`) files under
[`content/site/`](../content/site/) and [`content/indicators/`](../content/indicators/). Markdown is
just text with a few light symbols (`# Heading`, `- bullet`, `**bold**`). If you'd rather not see
even that, edit it in a WYSIWYG Markdown app (Obsidian or Mark Text, both free) where it looks like
Word. The same Word-document approach used for profiles can be extended to these later if it's
helpful — ask the maintainer.

---

## How your edit reaches the live website

Saving your file updates the copy in the shared **Box** folder, which syncs to the rest of the team.
But the *public* website is hosted on GitHub Pages, and it only updates when someone **publishes**.
That's a maintainer's task — authors never do it. In practice:

- A maintainer publishes pending changes periodically, **or**
- we set up an automatic publish (a scheduled job on one machine that watches the Box folder and
  pushes changes).

Either way: **you just save your Word file into Box and let the maintainer know it's ready.**

**For the maintainer:** publishing means running `python tools/build-profiles-index.py` (which
regenerates `content/profiles/profiles.json`, the list the site reads) and then committing + pushing.
This can be wired into a git pre-commit hook or the auto-push job so it's automatic.

## Good habits

- One Word file per country; the file name is the link text. Don't rename without flagging it — the
  site links to files by name.
- Don't keep two copies of the same profile; the `.docx` in `content/profiles/` is the single source
  of truth.
