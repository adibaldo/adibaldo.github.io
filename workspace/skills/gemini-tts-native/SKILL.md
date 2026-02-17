---
name: gemini-tts-native
description: Gera áudio nativo (.wav) usando o modelo Gemini 2.5 Flash TTS com o estilo do Aparício Funes.
metadata:
  {
    "openclaw":
      {
        "emoji": "🎙️",
        "requires": { "bins": ["uv"], "env": ["GEMINI_API_KEY"] }
      },
  }
---

# Gemini TTS Native (Estilo Aparício)

Esta skill gera arquivos de áudio no formato `.wav` usando o modelo nativo do Gemini, aplicando automaticamente o estilo e a transliteração gauchesca do Aparício Funes.

## Como usar

```bash
uv run --with google-genai {baseDir}/generate.py --prompt "Seu texto aqui" --filename "saida.wav" --voice "Charon"
```

## Notas
- O prompt é automaticamente enriquecido com instruções de estilo gauchesco.
- A voz padrão é "Charon" (madura/grave).
- Gera arquivos `.wav` compatíveis com a maioria dos dispositivos.
