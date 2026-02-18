---
name: memory-graph
description: "Audita e conecta arquivos de memória desgarrados (órfãos) no workspace. Inspirado no conceito de Grafo do Obsidian, garante que todo registro de memória tenha um rastro de origem ou referência."
---

# 🕸️ Memory Graph (A Skill do Rastreador de Rastro)

Na nossa estância, arquivo solto é que nem rês desgarrada: se perde no mato e ninguém mais acha. Esta skill serve para garantir que nossa memória seja um tecido firme, onde cada fio está amarrado em outro.

## 🕵️ O que é um "Arquivo Desgarrado"?
É qualquer arquivo dentro de `memory/` ou `jules-agents/` que não possui links apontando para ele (referências) em arquivos centrais como:
- `MEMORY.md` (O Índice)
- `memory/prosa/roteiro-adi.md` (O Mapa de Conversas)
- `HEARTBEAT.md` (A Ronda Diária)

## 📑 Protocolo de Auditoria (Workflow)

Sempre que a tropa do Jules terminar uma lida ou eu mesmo criar uma anotação, devo seguir este rastro:

### 1. Localizar o Gado Solto
Use o script `skills/memory-graph/scripts/find_orphans.sh` para listar arquivos que não são mencionados em nenhum outro lugar.

### 2. Amarrar o Rastro
Para cada arquivo solto encontrado:
- Se for uma memória valiosa: Crie um link para ele no `MEMORY.md` ou na sua respectiva categoria (ex: `memory/rolim-de-moura.md`).
- Se for um relatório de agente: Adicione ao `memory/prosa/roteiro-adi.md` para ser conversado com o seu Adi.
- Se for rascunho sem uso: Avalie se deve ser guardado em um "Baú de Retalhos" ou descartado pelo Zelador.

### 3. Verificar o Grafo
Use o rastro de `[[links]]` (estilo Obsidian/Wiki) para facilitar a conexão visual e a busca semântica.

## 🛠️ Automação (Scripts)

Use o script `skills/memory-graph/scripts/connect_all.py` para gerar um relatório de conectividade.

## 🌸 Filosofia
"Se não tem rastro, não aconteceu. Se tá solto, não é lembrança, é esquecimento."
