"""One-command publish: refresh the generated list, commit, and push to GitHub.

Run this to put pending content changes onto the live site:

    python tools/publish.py

It (1) regenerates content/profiles/deepdives.json, (2) stages everything, (3) commits — only if
something actually changed — and (4) pushes. GitHub Pages then rebuilds within a minute or two.

One-time setup per machine:
  - A GitHub remote must exist and git must be allowed to push (sign in once via the credential
    prompt / browser, or use SSH).
  - If git complains about "dubious ownership" (common inside a Box/OneDrive folder), run once:
        git config --global --add safe.directory "<full path to this repo>"

IMPORTANT: publish from ONE machine only. Letting the synced .git folder be written by several
machines at once can corrupt the repo — see docs/DEPLOYMENT.md.
"""
import os
import subprocess
import sys
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, ".."))


def git(*args, check=True):
    return subprocess.run(["git", "-C", REPO, *args], check=check, capture_output=True, text=True)


def main():
    # 1. regenerate the deep-dives manifest
    print("· regenerating the country deep-dives list …")
    subprocess.run([sys.executable, os.path.join(HERE, "build-deepdives-index.py")], check=True)

    # 2. stage everything
    git("add", "-A")

    # 3. commit only if there is something staged
    status = git("status", "--porcelain").stdout.strip()
    if status:
        stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        git("commit", "-m", f"Publish content update ({stamp})")
        print("· committed these changes:")
        print("   " + status.replace("\n", "\n   "))
    else:
        print("· no new changes to commit.")

    # 4. push (also sends any earlier commit that wasn't pushed yet)
    print("· pushing to GitHub …")
    res = git("push", check=False)
    out = (res.stdout + res.stderr).strip()
    if res.returncode == 0:
        print("\n✓ Published. GitHub Pages will rebuild in a minute or two.")
        if out:
            print(out)
    else:
        print("\n✗ Push failed:\n" + out)
        print("\n(If this is the first push, set up the GitHub remote first — see docs/DEPLOYMENT.md.)")
        sys.exit(1)


if __name__ == "__main__":
    main()
