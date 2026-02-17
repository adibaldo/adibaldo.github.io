# /// script
# requires-python = ">=3.10"
# dependencies = ["google-genai>=1.0.0", "pillow>=10.0.0"]
# ///
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = client.models.generate_images(
    model="imagen-4.0-fast-generate-001",
    prompt="A rustic porch scene with a framed oil painting of Noah's Ark on a mountain",
    config=types.GenerateImagesConfig(
        number_of_images=1,
        aspect_ratio="16:9",
    )
)

for i, generated_image in enumerate(response.generated_images):
    img = Image.open(BytesIO(generated_image.image.image_bytes))
    out = f"imagen-fast-test-{i+1}.png"
    img.save(out)
    print(f"saved {out}")
    print(f"MEDIA: {os.path.abspath(out)}")
