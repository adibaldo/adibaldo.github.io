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

## 🔄 Ciclo de Revisão e Feedback (Iteração)

O trabalho do Jules não termina quando a PR é aberta. Se o serviço não estiver perfeito, você deve atuar como o capataz da lida:

1. **Analisar a PR**: Use `gh pr view {numero} --json body,files` para ver o que o agente fez.
2. **Dar Feedback via Comentários**: Se algo precisar de ajuste, não feche a PR imediatamente. Use `gh pr comment {numero} --body "Sua instrução aqui"`.
   - **O Segredo**: O Jules está configurado para ler comentários nas PRs que ele abriu e retomar o trabalho (resumir a sessão) para aplicar as correções solicitadas.
3. **Iterar**: Você pode comentar quantas vezes for necessário até que o serviço esteja do seu agrado.
4. **Finalizar**: 
   - Se ficou bom: `gh pr merge {numero} --merge --delete-branch`.
   - Se não tem conserto: `gh pr close {numero}`.

## 📥 Sincronização Local
Após dar o merge no GitHub, não esqueça de trazer as melhorias para o seu galpão local:
```bash
git pull origin main
```

## 🔗 Referência sobre Repetição (Link over Repeat)

Para manter a consistência e evitar conflitos de instruções, dê preferência a **referenciar** arquivos existentes em vez de repetir comandos ou regras no prompt:

1. **Aponte o Caminho**: Em vez de copiar um protocolo de `SOUL.md`, diga: "Siga o protocolo de execução descrito em `jules-agents/{nome}/SOUL.md`".
2. **Contexto do Projeto**: Em vez de descrever a estrutura do repositório toda vez, aponte para o `jules-agents/README.md`.
3. **Evite Drift**: Repetir instruções cria o risco de uma versão ficar desatualizada. Referenciar garante que o agente sempre use a "fonte da verdade" mais recente do repositório.

## ⚔️ Gerenciamento de Conflitos

O Jules AI não é bom para resolver conflitos de merge. Se uma PR entrar em conflito (status `CONFLICTING`):

1. **Não peça para o Jules consertar**: Ele provavelmente se perderá no rastro.
2. **Comece do Zero**: O caminho mais rápido e limpo é fechar a PR conflitante e abrir uma **nova sessão** baseada na branch `main` atualizada.
3. **Resolva Manualmente**: Se for um ajuste simples, você (Aparício) pode fazer o conserto direto no arquivo e dar o push.

## 🚫 Limites
- **Nunca** envie apenas a missão sem a alma (SOUL.md).
- **Nunca** envie instruções que tirem a autonomia do agente definida no framework.
- **Sempre** verifique se o repositório está sincronizado (`git push`) antes de criar a sessão.

## 🌸 Filosofia
"O Jules é o motor, a Alma é o rumo, e a Missão é o destino."
