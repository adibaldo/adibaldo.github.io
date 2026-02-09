#!/usr/bin/env python3
"""Commit + push changes for Alfarrábios do Adi repo.

Usage:
  python3 skills/alfarrabios-publisher/scripts/publish.py \
    --repo /path/to/adibaldo.github.io \
    --message "Publish: Título"

This script does:
- git add (content files only — not secrets or env files)
- git commit (if there are changes)
- git push

It intentionally does NOT manage credentials.
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

# Only stage content directories (never secrets, env files, etc.)
SAFE_PATHS = [
    "src/",
    "public/",
    "astro.config.*",
    "package.json",
    "package-lock.json",
    "tsconfig.json",
]


def run(cmd: list[str], cwd: Path) -> str:
    out = subprocess.check_output(cmd, cwd=cwd, text=True)
    return out.strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--message", required=True)
    args = ap.parse_args()

    repo = Path(args.repo)

    status = run(["git", "status", "--porcelain"], cwd=repo)
    if not status:
        print("No changes to publish.")
        return 0

    # Stage only known-safe content paths instead of -A
    for pattern in SAFE_PATHS:
        subprocess.run(["git", "add", pattern], cwd=repo, check=False)

    # Verify something was actually staged
    staged = run(["git", "diff", "--cached", "--name-only"], cwd=repo)
    if not staged:
        print("No content files to publish (only ignored/untracked files changed).")
        return 0

    subprocess.run(["git", "commit", "-m", args.message], cwd=repo, check=True)
    subprocess.run(["git", "push"], cwd=repo, check=True)
    print("Pushed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
