import argparse
import os
import sys
from google import genai
from google.genai import types

def generate_audio(prompt, filename, voice="Charon"):
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    
    # 1. Transliteração usando o Gemini Flash Lite Latest
    # O Flash Lite é excelente para tarefas de texto rápidas e baratas.
    transliteration_prompt = f"""
    Atue como um especialista em sotaque gaúcho de São Borja. 
    Translitere o texto abaixo para que soe como uma prosa natural de varanda, 
    usando expressões como 'tchê', 'bah', 'pois então', 'vivente', 'capaz'. 
    Mantenha a alma do texto original, mas dê o sotaque fidedigno.
    
    TEXTO ORIGINAL: {prompt}
    
    APENAS O TEXTO TRANSLITERADO:
    """
    
    text_response = client.models.generate_content(
        model="gemini-2.5-flash-lite", # Usando o modelo Lite sugerido
        contents=transliteration_prompt
    )
    transliterated_text = text_response.text.strip()
    
    # 2. Geração do áudio usando o modelo de TTS
    # O modelo de áudio nativo v1beta/preview ainda é necessário para o TTS de alta qualidade.
    speech_prompt = f"AUDIO PROFILE: Aparício Funes. STYLE: Gaúcho de São Borja, maduro, voz grave. TRANSCRIPT: {transliterated_text}"
    
    # Usando o modelo de TTS dedicado para o áudio
    audio_response = client.models.generate_content(
        model="gemini-2.5-flash-preview-tts",
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
        contents=speech_prompt
    )
    
    for part in audio_response.candidates[0].content.parts:
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
