import sys
import os
import re
import subprocess
import time

def download_suno_with_jina(song_url, output_dir="franklinbaldo.github.io/public/audio/", jina_key="jina_46b86c5daef847f5859564b1126e96be-qOH32WhvzfTM0zKSpzuc2kMviaB"):
    # Extrair o ID da música da URL
    match = re.search(r'song/([a-f0-9\-]+)', song_url)
    if not match:
        print(f"Erro: ID da música não encontrado na URL.")
        return

    song_id = match.group(1)
    
    print(f"--- Iniciando resgate da música {song_id} ---")
    
    # 1. Usar Jina Reader para pegar os metadados e, quem sabe, a URL direta
    print("Pedindo ajuda ao Jina Reader para localizar o rastro do arquivo...")
    jina_url = f"https://r.jina.ai/{song_url}"
    headers = {
        "Authorization": f"Bearer {jina_key}",
        "X-With-Links-Summary": "true",
        "X-Wait-For": "audio"
    }
    
    try:
        response = subprocess.run([
            "curl", "-s", "-H", f"Authorization: Bearer {jina_key}", 
            "-H", "X-With-Links-Summary: true",
            jina_url
        ], capture_output=True, text=True)
        
        content = response.stdout
        
        # Procurar por URLs de áudio (mp3 ou webm) no conteúdo retornado pelo Jina
        audio_matches = re.findall(r'https?://[^\s\)]+\.(?:mp3|webm)[^\s\)]*', content)
        
        # Filtrar apenas as do CDN do Suno
        cdn_links = [link for link in audio_matches if "cdn" in link and "suno" in link]
        
        if not cdn_links:
            # Tentativa desesperada: montar a URL padrão
            cdn_links = [f"https://cdn1.suno.ai/{song_id}.mp3", f"https://cdn1.suno.ai/{song_id}.webm"]
            print("Jina não achou link direto, tentando rastro padrão...")
        else:
            print(f"Jina localizou {len(cdn_links)} possíveis arquivos!")

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        success = False
        for audio_url in cdn_links:
            ext = "mp3" if ".mp3" in audio_url else "webm"
            filepath = os.path.join(output_dir, f"{song_id}.{ext}")
            
            print(f"Tentando baixar: {audio_url}")
            
            # Usar curl com User-Agent de respeito
            dl_command = [
                "curl", "-L", 
                "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
                "-o", filepath, 
                audio_url, 
                "--fail"
            ]
            
            dl_result = subprocess.run(dl_command, capture_output=True)
            
            if dl_result.returncode == 0 and os.path.exists(filepath) and os.path.getsize(filepath) > 1000:
                print(f"Sucesso! A música está salva em: {filepath}")
                success = True
                break
            else:
                print(f"Porteira fechada para {audio_url} (Erro {dl_result.returncode})")

        if not success:
            print("\n[!] O Suno está com a segurança alta. O Jina Reader não conseguiu abrir a porteira do áudio.")
            print("O rastro mais seguro ainda é o download manual no site.")

    except Exception as e:
        print(f"Erro na lida: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 scripts/download_suno.py <URL>")
    else:
        download_suno_with_jina(sys.argv[1])
