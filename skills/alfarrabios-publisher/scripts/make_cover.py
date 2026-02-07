#!/usr/bin/env python3
"""Generate a mandatory cover image for a blog post using Nano Banana, then crop/resize to 1200x630.

Usage:
  python3 skills/alfarrabios-publisher/scripts/make_cover.py \
    --repo /path/to/adibaldo.github.io \
    --slug o-cheiro-do-cafe-na-varanda \
    --prompt "cafe na varanda..."

Notes:
- Requires: uv, GEMINI_API_KEY (Nano Banana), Pillow installed.
- Output:
  <repo>/src/content/blog/images/<slug>-cover.png
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

from PIL import Image

NANO_BANANA_SCRIPT = Path(
    "/home/franklin/.nvm/versions/node/v22.22.0/lib/node_modules/openclaw/skills/nano-banana-pro/scripts/generate_image.py"
)


def crop_to_1200x630(in_path: Path, out_path: Path) -> None:
    im = Image.open(in_path).convert("RGB")
    w, h = im.size
    target_ratio = 1200 / 630
    cur_ratio = w / h
    if cur_ratio > target_ratio:
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        im = im.crop((left, 0, left + new_w, h))
    else:
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        im = im.crop((0, top, w, top + new_h))
    im = im.resize((1200, 630), Image.LANCZOS)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    im.save(out_path, format="PNG", optimize=True)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--slug", required=True)
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--keep-raw", action="store_true")
    args = ap.parse_args()

    repo = Path(args.repo)
    raw = repo / "src/content/blog/images" / f"{args.slug}-cover_raw.png"
    final = repo / "src/content/blog/images" / f"{args.slug}-cover.png"

    cmd = [
        "uv",
        "run",
        str(NANO_BANANA_SCRIPT),
        "--prompt",
        args.prompt,
        "--filename",
        str(raw),
        "--resolution",
        "2K",
    ]
    subprocess.run(cmd, check=True)

    crop_to_1200x630(raw, final)

    if not args.keep_raw and raw.exists():
        raw.unlink()

    print(f"Wrote: {final}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
