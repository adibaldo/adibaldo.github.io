---
name: jules-api
description: Interage com a REST API do Jules para automatizar revisões de código, SEO e correções no blog.
metadata:
  {
    "openclaw":
      {
        "emoji": "🤖",
        "requires": { "bins": ["python3"], "env": ["JULES_API_KEY"] }
      },
  }
---

# Jules API Skill

Esta skill permite que o Aparício interaja diretamente com o Jules via API, facilitando a automação de tarefas no repositório do blog `adibaldo.github.io`.

## Comandos Disponíveis

Use o script `jules_client.py` com `uv run`:

### Listar Fontes (Repositórios)
```bash
uv run {baseDir}/jules_client.py list-sources
```

### Criar uma Nova Sessão de Trabalho
```bash
uv run {baseDir}/jules_client.py create-session --prompt "Analise o SEO do post X" --source "sources/github/franklinbaldo/adibaldo.github.io" --title "SEO Review"
```

### Verificar Status de uma Sessão
```bash
uv run {baseDir}/jules_client.py get-session --id "ID_DA_SESSAO"
```

### Listar Atividades da Sessão
```bash
uv run {baseDir}/jules_client.py list-activities --id "ID_DA_SESSAO"
```

### Enviar Mensagem para o Jules
```bash
uv run {baseDir}/jules_client.py send-message --id "ID_DA_SESSAO" --prompt "Pode ajustar os links internos também?"
```

## Configuração
Requer a variável de ambiente `JULES_API_KEY` configurada no OpenClaw.
