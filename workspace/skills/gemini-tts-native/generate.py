import argparse
import os
import struct
import sys
from pathlib import Path
from google import genai
from google.genai import types

def parse_audio_mime_type(mime_type: str) -> dict[str, int]:
    bits_per_sample = 16
    rate = 24000
    parts = mime_type.split(";")
    for param in parts:
        param = param.strip()
        if param.lower().startswith("rate="):
            try:
                rate = int(param.split("=", 1)[1])
            except (ValueError, IndexError):
                pass
        elif param.startswith("audio/L"):
            try:
                bits_per_sample = int(param.split("L", 1)[1])
            except (ValueError, IndexError):
                pass
    return {"bits_per_sample": bits_per_sample, "rate": rate}

def convert_to_wav(audio_data: bytes, mime_type: str) -> bytes:
    parameters = parse_audio_mime_type(mime_type)
    bits_per_sample = parameters["bits_per_sample"]
    sample_rate = parameters["rate"]
    num_channels = 1
    data_size = len(audio_data)
    bytes_per_sample = bits_per_sample // 8
    block_align = num_channels * bytes_per_sample
    byte_rate = sample_rate * block_align
    chunk_size = 36 + data_size
    
    header = struct.pack(
        "<4sI4s4sIHHIIHH4sI",
        b"RIFF", chunk_size, b"WAVE", b"fmt ", 16, 1,
        num_channels, sample_rate, byte_rate, block_align, bits_per_sample,
        b"data", data_size
    )
    return header + audio_data

def generate(prompt, filename, voice="Charon"):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not set")
        sys.exit(1)

    client = genai.Client(api_key=api_key)
    model = "gemini-2.5-flash-preview-tts"
    
    # Adicionando o estilo canônico do Aparício ao prompt se não estiver presente
    style_prefix = "[Estilo: Gaúcho de São Borja, maduro, fala pausada, calorosa. Use entonação de quem está contando um causo na varanda. Use transliteração gauchesca para o sotaque.] "
    if style_prefix[:20] not in prompt:
        prompt = style_prefix + prompt

    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        response_modalities=["audio"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=voice)
            )
        ),
    )

    full_audio = b""
    last_mime = "audio/L16;rate=24000"

    try:
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=prompt,
            config=generate_content_config,
        ):
            if chunk.parts:
                for part in chunk.parts:
                    if part.inline_data:
                        full_audio += part.inline_data.data
                        last_mime = part.inline_data.mime_type
        
        if full_audio:
            wav_data = convert_to_wav(full_audio, last_mime)
            with open(filename, "wb") as f:
                f.write(wav_data)
            print(f"MEDIA: {os.path.abspath(filename)}")
        else:
            print("No audio generated")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--filename", required=True)
    parser.add_argument("--voice", default="Charon")
    args = parser.parse_args()
    generate(args.prompt, args.filename, args.voice)
