# Deployment

The site is hosted on **GitHub Pages**, served from this repository, on the custom domain
**childhealth2050.org** (registered at GoDaddy). Deployment is "push to the repo; Pages
rebuilds." DNS/domain wiring happens later — this doc records the plan.

## One-time setup (when we're ready to go live)

1. **Push this repo to GitHub.** Read the ⚠️ note below *first* about repo visibility.
2. **Enable GitHub Pages** in the repo's Settings → Pages, serving from the default branch
   (root). The site appears at `https://<org-or-user>.github.io/<repo>` initially. The repo's
   [`.nojekyll`](../.nojekyll) file makes Pages serve every folder verbatim (no Jekyll build).
3. **Add the custom domain.** Set `childhealth2050.org` as the custom domain in Pages settings.
   GitHub writes a `CNAME` file to the repo (do not delete it).
4. **Point DNS at GoDaddy:**
   - Apex `childhealth2050.org` → GitHub Pages' four `A` records (and `AAAA` for IPv6), **or** an
     `ALIAS`/`ANAME` if available.
   - `www` → `CNAME` to `<org-or-user>.github.io`.
   - Use GitHub's current published Pages IPs at setup time (they can change).
5. **Enable "Enforce HTTPS"** once the certificate provisions.

Because everything is subfolders in one repo (see [DECISIONS ADR-001](DECISIONS.md)), this is a
**single** Pages site and a **single** `CNAME` — no per-tool DNS.

## Publishing routine content updates

Authors just save their Word files into the Box folder. To push those changes live, a maintainer
runs **one script**:

```
python tools/publish.py
```

It regenerates the profiles list (`profiles.json`), commits any changes, and pushes — GitHub Pages
rebuilds automatically. (On Windows you can make a one-line `publish.cmd` double-click wrapper if you
don't want to open a terminal.)

**Automation ladder — pick a level:**

1. **Manual (recommended start).** The maintainer runs `python tools/publish.py` when they want to
   publish. Full control, nothing to set up.
2. **Scheduled / hands-off.** A Windows Task Scheduler job runs `publish.py` every hour (or nightly).
   Authors save to Box; changes go live on the next run with nobody doing anything. Trade-off:
   commits happen automatically, and the scheduled machine must be on and able to push.

An optional git *pre-commit hook* can also regenerate `profiles.json` on every commit, so the list
is never stale even if someone commits without the script.

### ⚠️ Publish from ONE machine (Box + git)

The repository lives inside a **Box-synced folder**, so its `.git/` directory syncs too. File-sync
tools (Box, OneDrive, Dropbox) can **corrupt a git repo** if two machines run git operations against
the same synced `.git` at once. To stay safe:

- Designate **one** "publish machine" that runs `publish.py` / all git commands. Other people just
  edit content files in Box — they never run git.
- Each machine that *does* run git needs, once: a working GitHub sign-in for pushing, and (inside a
  Box folder) `git config --global --add safe.directory "<repo path>"`.
- If the repo ever shows odd git errors after a sync, that's the cause. The cleaner-but-more-work
  alternative is to keep the git clone **outside** Box and copy content in at publish time; only
  adopt that if the single-publish-machine rule proves hard to keep.

**GitHub is your backup.** Everything published lives on GitHub, so if the local `.git` inside Box
ever gets into a bad state, you can delete the local copy and re-clone from GitHub — nothing is lost.
That safety net is why the single-publish-machine rule is enough for a small team.

**Use a *shared* Box folder** (team members added as collaborators, or a group-owned folder — not one
person's personal Box) so everyone can open everything, including the raw data in
`data-processing/raw/`.

### Handing maintenance to someone else

Kept transferable by design: the shared Box folder already syncs to the team, and the GitHub repo
should be owned by an **organization** (not a personal account). To pass on the publish role: give the
new maintainer access to the Box folder + push rights on the repo, have them run once
`git config --global --add safe.directory "<repo path>"`, and they become the publish machine. Nothing
is tied to your machine or your account.

## ⚠️ Before making the repo public: internal docs

GitHub Pages is simplest (and free) on a **public** repo — but a public repo means **every file
is publicly viewable**, including anything not part of the site.

The [`broad context document/`](../broad%20context%20document/) folder contains the original
concept note and an **internal email thread** (names, addresses, internal discussion). It must
**not** be published. Current safeguard: that folder is listed in [`.gitignore`](../.gitignore),
so it stays local as context but is never committed/pushed.

Choose one before publishing:

- **Keep the repo private** (Pages on private repos needs a paid GitHub plan) → you *may* then
  track the context folder if you want it shared with collaborators (remove it from `.gitignore`).
- **Keep the repo public** → leave the context folder git-ignored (or move it out of the repo
  entirely). Double-check nothing else sensitive is committed.

When in doubt, keep it ignored. It's easy to start tracking a file later; it's hard to un-publish
one that was already pushed to a public repo.

## Shareable links & social cards

No special deploy config needed — these are built into the pages themselves (URL query state +
per-page Open Graph tags). See [ARCHITECTURE.md](ARCHITECTURE.md). Worth testing a few links in a
social-media / chat preview before announcing, since a broken preview image is easy to miss.
