#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "google-genai>=1.0.0",
# ]
# ///
import argparse
import os
import sys
import time
from google import genai

def transcribe_audio(file_path, api_key):
    client = genai.Client(api_key=api_key)
    
    print(f"Subindo arquivo: {file_path}...")
    audio_file = client.files.upload(file=file_path)
    
    # Aguarda o processamento do arquivo
    while audio_file.state.name == "PROCESSING":
        print(".", end="", flush=True)
        time.sleep(2)
        audio_file = client.files.get(name=audio_file.name)

    if audio_file.state.name == "FAILED":
        raise Exception("Falha no processamento do arquivo de áudio.")

    print("\nIniciando transcrição...")
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            "Transcreva este áudio fielmente para o português brasileiro. "
            "Se houver gírias ou expressões informais, mantenha-as conforme falado.",
            audio_file
        ]
    )
    
    # Limpa o arquivo após o uso
    client.files.delete(name=audio_file.name)
    
    return response.text

def main():
    parser = argparse.ArgumentParser(description="Transcreve áudios usando Gemini 2.0 Flash Lite")
    parser.add_argument("--file", required=True, help="Caminho para o arquivo de áudio (.ogg, .mp3, .wav, etc.)")
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Erro: Variável de ambiente GEMINI_API_KEY não configurada.")
        sys.exit(1)

    try:
        transcript = transcribe_audio(args.file, api_key)
        print("\n--- TRANSCRIÇÃO ---\n")
        print(transcript)
        print("\n-------------------")
    except Exception as e:
        print(f"Erro: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
