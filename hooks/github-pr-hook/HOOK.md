---
name: github-pr-hook
description: "Anzol para Pull Requests: Acorda o Aparício quando uma nova PR surge no GitHub (via Atom/RSS/Webhook)."
metadata:
  {
    "openclaw": {
      "emoji": "🪝",
      "events": ["webhook:github-pr"]
    }
  }
---

# Pull Request Hook (O Anzol do Aparício)

Este anzol serve para me puxar pela manga sempre que um agente Jules (ou o Franklin) abre uma Pull Request nova lá no GitHub.

## Como funciona
1. O GitHub avisa o OpenClaw via Webhook (ou a gente configura o RSS).
2. O anzol fisga o evento e me acorda com uma instrução de "Ronda de PR".
3. Eu já pulo no cercado pra ver o que o Jules aprontou e te aviso aqui na prosa.

## Configuração
O OpenClaw precisa estar com o Webhook habilitado e o token configurado no `openclaw.json`.
