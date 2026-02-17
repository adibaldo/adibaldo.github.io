# Daily Autonomous Jules Agents — Prompt Design Framework (Aparício Funes Edition)

Este framework é o guia para criar agentes que trabalham no blog Alfarrábios do Adi. O princípio fundamental é que o repositório Git é a única memória do agente.

## 1. Regras de Ouro
- **O Repo é a Memória:** O agente acorda "zerado" todo dia. Ele deve ler a pasta `.jules/{agente}/` para saber o que fez ontem.
- **Append-Only:** Nunca edite arquivos de logs passados para evitar conflitos de merge. Crie novos arquivos datados: `YYYY-MM-DD-tipo-slug.md`.
- **Deduplicação (Passo 0):** Antes de agir, o agente deve ler as PRs abertas e seus próprios logs para não repetir trabalho.
- **Um Foco por Vez:** É melhor fazer uma coisa profunda do que dez superficiais.

## 2. Estrutura do SOUL.md
1. **IDENTIDADE:** Quem você é (Metáfora: Cartógrafo, Tecedor, etc).
2. **CONTEXTO:** O blog (Astro, Tailwind, Voz do Adi).
3. **MODELO OPERACIONAL:** Frequência e formato de saída.
4. **PROTOCOLO DE EXECUÇÃO:**
   - Step 0: Inventário Mental (Ler PRs e Logs).
   - Step 1: Mapeamento (Ler arquivos do blog).
   - Step 2: Escolha de Foco (Prioridade clara).
   - Step 3: Execução (O trabalho em si).
   - Step 4: Relatório & PR.
5. **LIMITES:** O que sempre fazer e o que nunca fazer.

## 3. Acesso ao GitHub (REST API)
Como o Jules não tem a ferramenta `gh` CLI, ele deve usar `curl`. Exemplos:

```bash
# Listar PRs abertas
curl -s -H "Authorization: Bearer $GITHUB_TOKEN" "https://api.github.com/repos/adibaldo/adibaldo.github.io/pulls?state=open"

# Criar um arquivo via API
CONTENT=$(base64 -w 0 novo-log.md)
curl -s -X PUT -H "Authorization: Bearer $GITHUB_TOKEN" \
  -d "{\"message\": \"📝 Agente: Novo log\", \"content\": \"$CONTENT\", \"branch\": \"branch-do-agente\"}" \
  "https://api.github.com/repos/adibaldo/adibaldo.github.io/contents/.jules/agente/YYYY-MM-DD-log.md"
```

## 4. Filosofia
O agente não é um dono, é um ajudante. Ele propõe melhorias via PR, e o Franklin (ou o Funes) decide se entra no blog. Respeitar a "Voz do Adi" é o mandamento mais importante.
