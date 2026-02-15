# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "google-genai>=1.0.0",
# ]
# ///
from google import genai
import os

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
for m in client.models.list():
    if "image" in m.name or "flash" in m.name:
        print(f"Model: {m.name}")
