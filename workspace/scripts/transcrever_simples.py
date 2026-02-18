import sys
from google import genai
from google.genai import types
import os

def transcribe(file_path):
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    audio_file = client.files.upload(file=file_path)
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=[
            "Transcreva este áudio fielmente para o português brasileiro.",
            audio_file
        ]
    )
    print(response.text)

if __name__ == "__main__":
    transcribe(sys.argv[1])
