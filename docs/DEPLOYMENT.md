# Deployment

The site is hosted on **GitHub Pages**, served from this repository, on the custom domain
**childhealth2050.org** (registered at GoDaddy). Deployment is "push to the repo; Pages
rebuilds." DNS/domain wiring happens later — this doc records the plan.

## One-time setup (when we're ready to go live)

1. **Push this repo to GitHub.** Read the ⚠️ note below *first* about repo visibility.
2. **Enable GitHub Pages** in the repo's Settings → Pages, serving from the default branch (root).
   The site appears at https://<org-or-user>.github.io/<repo> initially. The repo's
   [.nojekyll](../.nojekyll) file makes Pages serve every folder verbatim (no Jekyll build).
3. **Add the custom domain.** Set childhealth2050.org as the custom domain in Pages settings.
   GitHub writes a CNAME file to the repo (do not delete it).
4. **Point DNS at GoDaddy:**
   - Apex childhealth2050.org → GitHub Pages' four A records (and AAAA for IPv6), **or** an
     ALIAS/ANAME if available.
   - www → CNAME to <org-or-user>.github.io.
   - Use GitHub's current published Pages IPs at setup time (they can change).
5. **Enable "Enforce HTTPS"** once the certificate provisions.

Because everything is subfolders in one repo (see [DECISIONS ADR-001](DECISIONS.md)), this is a
**single** Pages site and a **single** CNAME — no per-tool DNS.

## Publishing routine content updates

Authors save their content into the Box folder. To push those changes live, a maintainer runs the
publish workflow:

```
python tools/publish.py
```

It regenerates the profiles list, commits any changes, and pushes — GitHub Pages rebuilds
automatically. The same workflow should also include any profile content or deep-dive link updates so
nothing is left stale between the main profile pages and their supporting materials.

## ⚠️ Publish from ONE machine (Box + git)

The repository lives inside a **Box-synced folder**, so its .git directory syncs too. File-sync tools
(Box, OneDrive, Dropbox) can **corrupt a git repo** if two machines run git operations against the
same synced .git at once. To stay safe:

- Designate **one** publish machine that runs the publish workflow / git commands.
- Each machine that does run git needs, once: a working GitHub sign-in for pushing, and (inside a
  Box folder) git config --global --add safe.directory "<repo path>".

**Use a *shared* Box folder** so everyone can open everything, including the raw data in
 data-processing/raw/. The public repo should never hold internal planning notes or other sensitive
 material.

## ⚠️ Keeping internal material out of the public repo

The repo is **public** (the simplest, free way to run Pages), which means **every committed file is
publicly viewable**. So nothing internal goes into git.

The broad context document/ folder holds internal planning notes that should not be published. It is
listed in [.gitignore](../.gitignore), so it stays local (and shared with the team via Box) but is
**never committed or pushed** — and never has been. Leave it that way.

## Shareable links & social cards

No special deploy config is needed — these are built into the pages themselves (URL query state +
per-page Open Graph tags). See [ARCHITECTURE.md](ARCHITECTURE.md).
