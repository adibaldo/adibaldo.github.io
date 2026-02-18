import os
import sys
from google import genai
from google.genai import types

def analyze_audio(file_path):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )
    
    # Upload do arquivo
    print(f"Subindo {file_path} para o Gemini...")
    audio_file = client.files.upload(file=file_path)
    
    prompt = """
    Você é um crítico musical da revista Rolling Stone. 
    Analise este áudio gerado por IA (Suno) para o blog 'A Crônica de Franklin Baldo'.
    
    Descreva:
    1. O ritmo e estilo predominante.
    2. O que uma pessoa sente ao ouvir essa música (atmosfera).
    3. O que você acha que o autor (Franklin Baldo) estava pensando ou qual era a intenção intelectual por trás dessa composição.
    4. Use um tom sofisticado, rítmico e intelectual, compatível com o blog.
    
    Seja breve, mas impactante.
    """
    
    print("Analisando...")
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            types.Content(
                role="user",
                parts=[
                    types.Part.from_uri(file_uri=audio_file.uri, mime_type="audio/mpeg"),
                    types.Part.from_text(text=prompt)
                ]
            )
        ]
    )
    
    return response.text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 analyze_songs.py <audio_dir>")
        sys.exit(1)
        
    audio_dir = sys.argv[1]
    files = [f for f in os.listdir(audio_dir) if f.endswith(".mp3")]
    
    analyses = []
    for f in files:
        path = os.path.join(audio_dir, f)
        analysis = analyze_audio(path)
        analyses.append(f"### Arquivo: {f}\n\n{analysis}\n")
        
    with open("audio_analysis.md", "w") as out:
        out.write("# Análise Crítica da Vitrine Sonora\n\n")
        out.write("\n".join(analyses))
    
    print("Análise concluída e salva em audio_analysis.md")
