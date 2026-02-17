import argparse
import os
import sys
from google import genai
from google.genai import types

def generate_audio(prompt, filename, voice="Charon"):
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"), http_options={'api_version': 'v1beta'})
    
    # Enriquecer o prompt com estilo gaúcho
    style_prompt = f"Fale como um gaúcho veterano de São Borja, use sotaque natural e expressões como 'tchê', 'bah', 'pois então'. Texto: {prompt}"
    
    response = client.models.generate_content(
        model="gemini-1.5-flash", 
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name=voice
                    )
                )
            )
        ),
        contents=style_prompt
    )
    
    for part in response.candidates[0].content.parts:
        if part.inline_data:
            with open(filename, "wb") as f:
                f.write(part.inline_data.data)
            print(f"MEDIA: {os.path.abspath(filename)}")
            return True
    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--filename", required=True)
    parser.add_argument("--voice", default="Charon")
    args = parser.parse_args()
    
    generate_audio(args.prompt, args.filename, args.voice)
