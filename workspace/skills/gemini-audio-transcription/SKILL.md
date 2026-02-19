# Gemini Audio Transcription

Transcreve áudio para texto usando a API do Google Gemini.

## Capabilities

- Transcrição de áudio em diversos formatos (OGG, MP3, WAV, etc.)
- Suporta português brasileiro com alta precisão
- Mantém gírias, sotaques regionais e características da fala
- Upload automático via API do Gemini
- Retorna apenas a transcrição literal, sem formatação extra

## Usage

```bash
./scripts/transcribe.sh <AUDIO_FILE_PATH>
```

### Exemplo

```bash
./scripts/transcribe.sh /path/to/audio.ogg
```

## Requirements

- `GEMINI_API_KEY` (variável de ambiente)
- `curl` (HTTP client)
- `python3` (para parsing JSON)
- `stat` (para obter tamanho do arquivo)

## API Model

- Modelo usado: `gemini-2.0-flash` (v1beta)
- Upload via protocolo resumable do Google
- Transcrição via generateContent

## Implementation Notes

O script realiza 3 etapas:

1. **Iniciar upload:** Obtém URL de upload via X-Goog-Upload-Protocol
2. **Upload do arquivo:** Envia o arquivo de áudio usando o URL retornado
3. **Transcrever:** Chama generateContent com o URI do arquivo

## Output

A transcrição é retornada como texto puro (stdout), facilitando integração com pipelines.

## Error Handling

- Verifica se `GEMINI_API_KEY` está definida
- Valida existência do arquivo de áudio
- Exibe mensagens de erro da API quando aplicável
