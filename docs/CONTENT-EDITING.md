# Editing the website's text (no coding required)

You do not need to know code, Markdown, or GitHub to write content. There are two separate things,
and section authors are shielded from both:

1. **Writing** — country profiles and deep dives are authored in Word or structured text, depending on
   the section.
2. **Publishing** — getting your change onto the live website is a maintainer's job (see the last
   section). You never touch GitHub.

---

## Country profiles — use a simple, standardized structure

The main country profile page should stay fairly concise and structured. It should include:

- figures and tables for the selected country,
- standardized background statistics,
- a short narrative section that is AI-generated at first and clearly labeled as an AI draft,
- a prominent link to a deeper country deep dive when one exists.

The main profile copy is meant to be easy to populate and easy to revise. The first pass can be
AI-generated from a simple rubric, and authors can later review and rewrite it. The content should
always be labeled clearly so readers know when they are looking at a draft.

### Authoring workflow for the main profile page

- Start from a standard rubric with fixed headings such as context, recent progress, equity, and key
  takeaways.
- Let AI populate the draft from the rubric and available data.
- Add a visible label such as “AI-generated draft” until the author has reviewed it.
- When an author is ready, they rewrite the copy and remove the label.

### Deep dives

Deep dives are the fuller, more narrative pieces. They should be linked prominently from the main
profile page when available, but they should not replace the concise profile page itself.

The current repository still supports Word-based profile documents, and that remains a good fit for
deep dives. The main profile page can still be assembled from structured content and linked deep-dive
files as the workflow matures.

---

## Other text (landing page, About, indicator notes)

Site-wide copy and per-indicator notes still live as Markdown files under [content/site/](../content/site/)
and [content/indicators/](../content/indicators/). Markdown is just text with a few light symbols.
If you would rather not see even that, edit it in a WYSIWYG Markdown app where it looks like Word.

---

## How your edit reaches the live website

Saving your file updates the copy in the shared **Box** folder, which syncs to the rest of the team.
But the public website is hosted on GitHub Pages, and it only updates when someone publishes. That is
still a maintainer's task — authors never do it.

For the maintainer, publishing means running the usual publish workflow and making sure updated profile
content, deep-dive links, and any generated manifests are included before the push.

## Good habits

- Keep the main profile copy short, structured, and easy to revise.
- Label AI-generated text clearly until it has been reviewed.
- Keep deep dives as separate, fuller authoring pieces rather than stuffing everything onto the main
  profile page.
- Use the same file names and folder structure consistently so links remain stable.
