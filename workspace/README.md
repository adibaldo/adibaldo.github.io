# Workspace do Aparício Funes

Este é o workspace de trabalho do Aparício Funes, agente do OpenClaw responsável por preservar as memórias do Adi Baldo.

## Estrutura

```
workspace/
├── AGENTS.md           # Configuração do ecossistema de agentes
├── SOUL.md            # Identidade e persona do Aparício
├── TOOLS.md           # Ferramentas e especificações
├── USER.md            # Informações sobre os usuários (Adi e Franklin)
├── secrets.env        # Credenciais e API keys (git-ignored)
├── SECRETS.template   # Template para configuração de secrets
├── jules-agents/      # Agentes Jules especializados
├── memory/            # Snapshots de memória
├── scripts/           # Scripts utilitários
└── skills/            # Skills especializadas
```

## Configuração de Secrets

API keys e credenciais são armazenadas em `secrets.env`, que é ignorado pelo Git.

### Setup Inicial

1. Copie o template:
   ```bash
   cp SECRETS.template secrets.env
   ```

2. Edite com suas credenciais:
   ```bash
   vim secrets.env  # ou seu editor preferido
   ```

3. Carregue as variáveis antes de usar scripts que precisam de API keys:
   ```bash
   source secrets.env
   ```

### Secrets Protegidos

O `.gitignore` protege os seguintes padrões:
- `*.env`
- `.env.*`
- `secrets.*`
- `credentials.*`

## Skills Disponíveis

### Gemini Audio Transcription
Transcreve áudio para texto usando Google Gemini API.

```bash
source secrets.env
./skills/gemini-audio-transcription/scripts/transcribe.sh audio.ogg
```

Ver documentação completa em: `skills/gemini-audio-transcription/SKILL.md`

## Jules Agents

Agentes especializados que trabalham em conjunto com o Aparício:
- **Garimpo (Candido):** Curador de links e referências
- **Mosqueteiro:** Monitor de notícias e atualizações
- **Pioneiro:** Explorador de temas históricos de Rondônia

Ver quadro de avisos: `jules-agents/quadro-de-avisos/`

## Segurança

- ✅ Secrets protegidos pelo .gitignore
- ✅ Template de exemplo versionado (sem dados sensíveis)
- ✅ Sessões JSONL versionadas no repositório privado
- ❌ Nunca commitar secrets.env ou arquivos *.env
