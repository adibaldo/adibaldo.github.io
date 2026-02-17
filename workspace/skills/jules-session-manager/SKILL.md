---
name: jules-session-manager
description: "Cria e gerencia sessões do Jules AI usando os perfis (SOUL.md) dos agentes locais. Use para delegar tarefas autônomas ao Jules, garantindo que ele receba a 'alma' e a 'missão' corretas para atuar no repositório."
---

# 🤖 Jules Session Manager

Esta skill é a ponte entre as almas dos nossos agentes locais (`jules-agents/`) e a força de execução do Jules AI.

## 🏗️ Como Criar uma Sessão com Alma

Sempre que precisar despachar um agente Jules (como a Mari Kondo ou o Vitrine), siga este rastro:

### 1. Preparar a Alma
Leia o arquivo `SOUL.md` do agente em `jules-agents/{nome}/SOUL.md`. Este arquivo contém a identidade, o protocolo e os limites do vivente.

### 2. Definir a Missão
Não dê ordens mecânicas passo-a-passo. Defina o **OBJETIVO** e a **MISSÃO** da run, permitindo que o agente use a autonomia descrita na sua alma. Lembre o agente de ler seu `EXPERIENCE.md` e os últimos 3 logs para garantir a continuidade.

### 3. Disparar via API
Use o `jules-api` para criar a sessão, concatenando a Alma com a Missão.

**Exemplo de comando:**
```bash
export JULES_API_KEY=$(cat ~/.openclaw/secrets.env | grep JULES_API_KEY | cut -d'=' -f2)

python3 skills/jules-api/jules_client.py create-session \
  --prompt "$(cat jules-agents/marikondo/SOUL.md) \n\n --- \n # MISSÃO: [Descreva o objetivo aqui]" \
  --source "sources/github/franklinbaldo/aparicio-funes" \
  --title "Nome da Sessão"
```

## 📑 Protocolo de Acompanhamento
- **ID da Sessão:** Guarde o ID retornado para consultas futuras.
- **URL:** Forneça a URL para o Franklin poder espiar o serviço.
- **PR:** Avise que o resultado final será uma Pull Request no GitHub.

## 🚫 Limites
- **Nunca** envie apenas a missão sem a alma (SOUL.md).
- **Nunca** envie instruções que tirem a autonomia do agente definida no framework.
- **Sempre** verifique se o repositório está sincronizado (`git push`) antes de criar a sessão.

## 🌸 Filosofia
"O Jules é o motor, a Alma é o rumo, e a Missão é o destino."
