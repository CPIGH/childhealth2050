"""Regenerate content/profiles/deepdives.json — the manifest of country deep dives.

A static site can't list a folder at runtime, so this small manifest stands in for that. The
Country Profiles page reads it to (a) render a country's deep dive and (b) flag, in the country
selection tree, which countries have one.

It scans content/profiles/deepdives/ for *.docx, SKIPS any file whose name starts with "_"
(e.g. a _TEMPLATE.docx placed there), and derives each entry from the file name:
  file  -> the exact .docx filename the site fetches (relative to content/profiles/deepdives/)
  label -> the file name without .docx — used as the link text
  slug  -> a url-safe id; must match the country's slug in assets/data/countries.json so the
           profile page can line the deep dive up with the right country

Run it whenever deep dives are added/renamed, as part of publishing (tools/publish.py calls it).

Usage:  python tools/build-deepdives-index.py
No dependencies (standard library only).
"""
import json, re, glob, os

HERE = os.path.dirname(os.path.abspath(__file__))
DEEPDIVES_DIR = os.path.normpath(os.path.join(HERE, "..", "content", "profiles", "deepdives"))
OUT_PATH = os.path.normpath(os.path.join(HERE, "..", "content", "profiles", "deepdives.json"))


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.strip().lower()).strip("-")


entries = []
for path in glob.glob(os.path.join(DEEPDIVES_DIR, "*.docx")):
    name = os.path.basename(path)
    if name.startswith("_"):
        continue  # helper/template files are not deep dives
    label = os.path.splitext(name)[0]
    entries.append({"file": name, "label": label, "slug": slugify(label)})

entries.sort(key=lambda e: e["label"].lower())

with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(entries, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"wrote {OUT_PATH} with {len(entries)} deep dive(s): {[e['label'] for e in entries]}")
