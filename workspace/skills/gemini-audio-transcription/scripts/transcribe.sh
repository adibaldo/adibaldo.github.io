#!/bin/bash
set -e

# Gemini Audio Transcription Script
# Transcreve áudio para texto usando Google Gemini API

AUDIO_FILE="$1"

# Validações
if [ -z "$GEMINI_API_KEY" ]; then
  echo "ERRO: Variável GEMINI_API_KEY não está definida" >&2
  exit 1
fi

if [ -z "$AUDIO_FILE" ]; then
  echo "Uso: $0 <AUDIO_FILE_PATH>" >&2
  exit 1
fi

if [ ! -f "$AUDIO_FILE" ]; then
  echo "ERRO: Arquivo não encontrado: $AUDIO_FILE" >&2
  exit 1
fi

# Obter tamanho do arquivo (compatível com Linux e macOS)
FILE_SIZE=$(stat -c%s "$AUDIO_FILE" 2>/dev/null || stat -f%z "$AUDIO_FILE")

# Detectar tipo MIME do arquivo
MIME_TYPE="audio/ogg"
case "$AUDIO_FILE" in
  *.mp3) MIME_TYPE="audio/mpeg" ;;
  *.wav) MIME_TYPE="audio/wav" ;;
  *.m4a) MIME_TYPE="audio/mp4" ;;
  *.flac) MIME_TYPE="audio/flac" ;;
  *.ogg) MIME_TYPE="audio/ogg" ;;
esac

# Step 1: Iniciar upload resumable
UPLOAD_URL=$(curl -sD - -X POST \
  "https://generativelanguage.googleapis.com/upload/v1beta/files?key=${GEMINI_API_KEY}" \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${FILE_SIZE}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{\"file\": {\"display_name\": \"audio_transcription\"}}" | \
  grep -i "x-goog-upload-url" | cut -d' ' -f2 | tr -d '\r')

if [ -z "$UPLOAD_URL" ]; then
  echo "ERRO: Não foi possível iniciar upload" >&2
  exit 1
fi

# Step 2: Fazer upload do arquivo
UPLOAD_RESPONSE=$(curl -s -X POST "$UPLOAD_URL" \
  -H "Content-Length: ${FILE_SIZE}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary @"$AUDIO_FILE")

# Extrair URI do arquivo
FILE_URI=$(echo "$UPLOAD_RESPONSE" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    print(data.get('file', {}).get('uri', ''))
except Exception as e:
    print('', file=sys.stderr)
    exit(1)
")

if [ -z "$FILE_URI" ]; then
  echo "ERRO no upload do arquivo. Resposta da API:" >&2
  echo "$UPLOAD_RESPONSE" >&2
  exit 1
fi

# Step 3: Transcrever usando Gemini Flash Lite
TRANSCRIPTION_RESPONSE=$(curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-lite-latest:generateContent?key=${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "{
    \"contents\": [{
      \"parts\": [
        {\"text\": \"Transcreva este áudio em português brasileiro com alta precisão. Mantenha gírias, sotaques regionais e características da fala como foram pronunciadas. Se houver pausas ou hesitações significativas, indique com [...]. Retorne APENAS a transcrição literal, sem comentários ou formatação adicional.\"},
        {\"file_data\": {\"mime_type\": \"${MIME_TYPE}\", \"file_uri\": \"$FILE_URI\"}}
      ]
    }]
  }")

# Extrair e exibir transcrição
echo "$TRANSCRIPTION_RESPONSE" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    if 'candidates' in data and len(data['candidates']) > 0:
        text = data['candidates'][0]['content']['parts'][0]['text']
        print(text)
    elif 'error' in data:
        print('ERRO da API Gemini:', data['error']['message'], file=sys.stderr)
        exit(1)
    else:
        print('ERRO: Resposta inesperada da API', file=sys.stderr)
        print(json.dumps(data, indent=2), file=sys.stderr)
        exit(1)
except Exception as e:
    print('ERRO ao processar resposta:', str(e), file=sys.stderr)
    exit(1)
"
