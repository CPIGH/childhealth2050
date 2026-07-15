"""Regenerate content/profiles/profiles.json — the list the Country Profiles page reads.

A static site can't list a folder at runtime, so this small manifest stands in for that.
Run it whenever profiles are added/renamed, as part of publishing (e.g. before `git push`,
as a git pre-commit hook, or in the auto-push job).

It scans content/profiles/ for *.docx, SKIPS any file whose name starts with "_"
(e.g. _TEMPLATE.docx, _READ-ME-FIRST.docx), and derives each link from the file name:
  file  -> the exact .docx filename the site fetches
  label -> the file name (without .docx) — what shows as the link text
  slug  -> a url-safe id used in the shareable URL (?country=<slug>)

Usage:  python tools/build-profiles-index.py
No dependencies (standard library only).
"""
import json, re, glob, os

HERE = os.path.dirname(os.path.abspath(__file__))
PROFILES_DIR = os.path.normpath(os.path.join(HERE, "..", "content", "profiles"))


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.strip().lower()).strip("-")


entries = []
for path in glob.glob(os.path.join(PROFILES_DIR, "*.docx")):
    name = os.path.basename(path)
    if name.startswith("_"):
        continue  # helper/instruction files are not country links
    label = os.path.splitext(name)[0]
    entries.append({"file": name, "label": label, "slug": slugify(label)})

entries.sort(key=lambda e: e["label"].lower())

out_path = os.path.join(PROFILES_DIR, "profiles.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(entries, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"wrote {out_path} with {len(entries)} profile(s): {[e['label'] for e in entries]}")
