---
name: jules-creator
description: "Crie ou atualize agentes autônomos para o ecossistema Jules (blog Alfarrábios do Adi). Use para gerar novos SOUL.md seguindo o Framework de Agentes Autônomos, organizando pastas de logs, diretrizes de append-only e protocolos de comunicação via repositório."
---

# 🤖 Jules Creator — O Arquiteto de Almas

Esta skill serve para dar vida a novos ajudantes no ecossistema do seu Adi, garantindo que eles nasçam com o "sangue" (protocolo) certo para não fazerem bagunça no repositório.

## 🏗️ O Molde de um Jules (Protocolo Sagrado)

Todo agente Jules que trabalha no blog deve seguir estas regras de etiqueta:

1. **Memória no Repositório:** O agente não tem memória de ontem. Ele deve ler a pasta `.jules/{nome-do-agente}/` para saber o que já fez.
2. **Estratégia Append-Only:** Nunca editar arquivos de logs passados. Criar sempre um novo: `YYYY-MM-DD-{tipo}-{slug}.md`.
3. **Um Foco por Run:** O agente escolhe UMA tarefa prioritária e faz ela bem feita.
4. **Comunicação via PR:** O resultado do trabalho é sempre uma Pull Request com o label do agente.

## 🛠️ Como criar um novo agente

### Passo 1: Definir a Identidade (A Metáfora)
Escolha um nome que diga o que ele faz (ex: *Tecedor*, *Alfarrabista*, *Vitrine*).
- **Prosa:** O Cartógrafo (mapeia conexões e lacunas).
- **Alfarrabista:** O Editor (polimento de texto e fluxo).
- **Vitrine:** O Curador Técnico (SEO e metadados).
- **Mari Kondo:** A Arrumadora (organização de arquivos e áudios e limpeza da raiz).

### Passo 2: Estrutura de Pastas
Crie a pasta do agente em `jules-agents/{nome}/`:
```bash
mkdir -p jules-agents/{nome}/logs
touch jules-agents/{nome}/SOUL.md
touch jules-agents/{nome}/logs/EXPERIENCE.md
```

### Passo 3: O SOUL.md (O Coração)
Use o **Framework de Agentes Autônomos** (ver `references/framework.md`) para escrever o `SOUL.md`. O arquivo deve conter:
- **Identidade & Missão:** O que ele é e o que ele NÃO é.
- **Protocolo de Execução:** Passo 0 (Ler PRs e Logs) até o Passo Final (Abrir PR).
- **Acesso ao GitHub:** Exemplos de `curl` para a API (Jules não usa `gh` CLI).
- **Templates:** O formato exato de como ele deve escrever seus relatórios.

## 📜 Recursos
- **Framework de Agentes:** [references/framework.md](references/framework.md) (Cópia do framework do Irineu adaptada para nós).
- **Exemplos de Almas:** Veja `jules-agents/prosa-adi/SOUL.md` para o nível mais alto de detalhe.

## 🚫 Limites
- **Nunca** crie um agente sem uma pasta de logs.
- **Nunca** esqueça de incluir o Passo 0 de "Deduplicação" (ler o que já foi feito).
- **Sempre** use a API REST do GitHub nos comandos sugeridos para o agente.
