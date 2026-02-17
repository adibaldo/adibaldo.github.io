# TOOLS.md — Especificações da Estância do Aparício

Este arquivo guarda as notas sobre as nossas ferramentas locais e como elas devem ser usadas no dia a dia. Enquanto as "skills" explicam o _como_ a ferramenta funciona no geral, o `TOOLS.md` explica o _onde_ e o _quais_ são os detalhes da nossa casa.

---

### 🎙️ Áudio e Voz (TTS)

- **Voz Padrão:** "Charon" (tom grave, maduro, ideal para o Aparício).
- **Modelo de Áudio Nativo:** `gemini-2.5-flash-preview-tts`.
- **Modelo de Transliteração:** `gemini-2.5-flash-lite` (usado para dar o sotaque de São Borja antes de gerar o áudio).
- **Script de Confiança:** `scripts/gemini_tts_wav.py`.
- **Caminho dos Áudios:** `workspace/assets/audio/`.
- **Caminho das Transcrições:** `workspace/assets/audio/transcripts/`.

### 🍌 Geração de Imagens (Nano Banana)

- **Modelo:** Gemini 3 Pro Image (Nano Banana Pro).
- **Estilo Preferido:** "Varanda Moderna" ou "Pintura Biográfica" (conforme a vontade do seu Adi).
- **Resolução de Capa:** 1200x630 (PNG).
- **Script de Capas:** `skills/alfarrabios-publisher/scripts/make_cover.py`.

### 🤖 Agentes Jules (API)

- **Repositório Base:** `franklinbaldo/aparicio-funes`.
- **Repositório do Blog:** `adibaldo/adibaldo.github.io`.
- **Skill de Gerenciamento:** `jules-session-manager`.
- **Regra de Ouro:** Sempre enviar o `SOUL.md` completo do agente junto com a missão da run.

### 🐙 GitHub e Versionamento

- **Identidade Local (Git):** 
  - Nome: Aparício Funes
  - Email: franklinbaldo@users.noreply.github.com
- **Ferramenta de PRs:** `gh` CLI (para o Aparício) e `curl` (para os agentes Jules).

---
*Nota: Este arquivo é apenas orientação para o agente e não controla a disponibilidade técnica das ferramentas.*
