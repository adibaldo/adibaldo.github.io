# Gemini Audio Transcription

Transcreve áudio para texto usando a API do Google Gemini.

## Capabilities

- Transcrição de áudio em diversos formatos (OGG, MP3, WAV, etc.)
- Suporta português brasileiro com alta precisão
- Mantém gírias, sotaques regionais e características da fala
- Upload automático via API do Gemini
- **Retorna DUAS versões da transcrição:**
  - **RAW:** Transcrição literal com hesitações, repetições e pausas
  - **INTERPRETED:** Versão limpa e interpretada, mantendo apenas o sentido pretendido

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

### Configuração da API Key

A chave da API está armazenada em `workspace/secrets.env` (protegido pelo .gitignore).

Para carregar a chave antes de executar o script:

```bash
source workspace/secrets.env
./scripts/transcribe.sh /path/to/audio.ogg
```

Ou em uma única linha:

```bash
source workspace/secrets.env && ./scripts/transcribe.sh /path/to/audio.ogg
```

## API Model

- Modelo usado: `gemini-flash-lite-latest` (v1beta)
- Upload via protocolo resumable do Google
- Transcrição via generateContent
- Modelo "lite" oferece boa precisão com menor custo/latência

## Implementation Notes

O script realiza 3 etapas:

1. **Iniciar upload:** Obtém URL de upload via X-Goog-Upload-Protocol
2. **Upload do arquivo:** Envia o arquivo de áudio usando o URL retornado
3. **Transcrever:** Chama generateContent com o URI do arquivo

## Output

A transcrição é retornada como texto formatado em markdown (stdout), com duas seções distintas:

```markdown
## RAW

Elas devem ser comitadas para esse repositório, repositório privado, entendeu? Elas precisam ser comitadas.

## INTERPRETED

Elas devem ser comitadas para esse repositório, repositório privado. Elas precisam ser comitadas.
```

### Formato de Output

- **RAW:** Mantém características exatas da fala (hesitações, repetições, "né?", "entendeu?", etc.)
- **INTERPRETED:** Versão editada mantendo apenas o conteúdo essencial da mensagem
- Ambas preservam gírias e sotaques regionais
- Facilita integração com pipelines e processamento posterior

## Error Handling

- Verifica se `GEMINI_API_KEY` está definida
- Valida existência do arquivo de áudio
- Exibe mensagens de erro da API quando aplicável
