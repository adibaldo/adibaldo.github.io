import os
import asyncio
import wave
import argparse
from google import genai
from google.genai import types

MODEL = "models/gemini-2.5-flash-native-audio-preview-12-2025"

async def generate_audio(prompt, filename, voice="Zephyr"):
    client = genai.Client(
        http_options={"api_version": "v1beta"},
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    config = types.LiveConnectConfig(
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=voice)
            )
        )
    )

    try:
        async with client.aio.live.connect(model=MODEL, config=config) as session:
            await session.send(input=prompt, end_of_turn=True)
            
            # Create a wave file to store the output
            # Gemini returns 24kHz mono 16-bit PCM
            with wave.open(filename, 'wb') as wav_file:
                wav_file.setnchannels(1)
                wav_file.setsampwidth(2)
                wav_file.setframerate(24000)

                async for response in session.receive():
                    if response.data:
                        wav_file.writeframes(response.data)
                    if response.server_content and response.server_content.turn_complete:
                        break
        print(f"MEDIA: {os.path.abspath(filename)}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--filename", required=True)
    parser.add_argument("--voice", default="Zephyr")
    args = parser.parse_args()
    
    asyncio.run(generate_audio(args.prompt, args.filename, args.voice))
