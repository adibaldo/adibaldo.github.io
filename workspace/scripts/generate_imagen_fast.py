#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["google-genai>=1.0.0", "pillow>=10.0.0"]
# ///

import argparse
import os
from io import BytesIO
from pathlib import Path
from google import genai
from google.genai import types
from PIL import Image


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--prompt", required=True)
    p.add_argument("--filename", required=True)
    p.add_argument("--api-key", default=os.environ.get("GEMINI_API_KEY", ""))
    p.add_argument("--aspect", default="16:9")
    args = p.parse_args()

    if not args.api_key:
        raise SystemExit("Missing GEMINI_API_KEY")

    client = genai.Client(api_key=args.api_key)
    out = Path(args.filename)
    out.parent.mkdir(parents=True, exist_ok=True)

    response = client.models.generate_images(
        model="imagen-4.0-fast-generate-001",
        prompt=args.prompt,
        config=types.GenerateImagesConfig(number_of_images=1, aspect_ratio=args.aspect),
    )

    img_bytes = response.generated_images[0].image.image_bytes
    img = Image.open(BytesIO(img_bytes)).convert("RGB")
    img.save(out, "PNG")
    print(f"Image saved: {out.resolve()}")
    print(f"MEDIA: {out.resolve()}")


if __name__ == "__main__":
    main()
