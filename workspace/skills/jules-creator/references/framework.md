# Daily Autonomous Jules Agents — Prompt Design Framework (Aparício Funes Edition)

Este framework é o guia para criar agentes que trabalham no ecossistema Aparício Funes. O princípio fundamental é que o repositório Git é a única memória do agente e a continuidade é garantida pela leitura de logs passados.

## 1. Regras de Ouro (Obrigatórias)

### A. Memória e Continuidade
O agente acorda "zerado" todo dia. Para manter o fio da meada, ele DEVE:
1. **Ler o `EXPERIENCE.md`**: Localizado em `.jules/{agente}/EXPERIENCE.md`, contém aprendizados de longo prazo sobre o projeto.
2. **Ler os últimos 3 Logs**: Localizados em `.jules/{agente}/YYYY-MM-DD-tipo-slug.md`, para saber o que foi feito nas sessões anteriores.

### B. Registro de Atividade (Append-Only)
Cada run deve produzir obrigatoriamente um novo arquivo de log:
- **Formato**: `.jules/{agente}/YYYY-MM-DD-{tipo}-{slug}.md`.
- **Conteúdo**: O que foi feito, por que foi feito, o que foi aprendido e sugestões para a próxima run.
- **Deduplicação**: Nunca edite arquivos de logs passados.

### C. Aprendizado de Longo Prazo
O arquivo `EXPERIENCE.md` deve ser atualizado apenas quando o agente descobre algo fundamental que deve ser lembrado para sempre (ex: um padrão de erro recorrente, uma preferência específica do autor).

### D. Quadro de Avisos (Pasta de Comunicação)
Para evitar conflitos de merge, o "Quadro de Avisos" não é um arquivo único, mas uma pasta em `jules-agents/quadro-de-avisos/`.
- Cada novo aviso deve ser um arquivo único: `YYYYMMDD-HHMMSS-{agente}-{assunto}.md`.

## 2. Estrutura Padrão do SOUL.md

Todo SOUL.md deve seguir esta ordem:
1. **IDENTIDADE**: Metáfora e Missão.
2. **CONTEXTO**: Repositórios e Tecnologias.
3. **PROTOCOLO DE EXECUÇÃO**:
   - **Step 0 — Inventário Mental (Obrigatório)**: Ler PRs abertas, `EXPERIENCE.md` e os 3 últimos logs da sua pasta.
   - **Step 1 — Mapeamento**: Investigar o estado atual do repositório alvo.
   - **Step 2 — Escolha de Foco**: Prioridade clara baseada na autonomia do agente.
   - **Step 3 — Execução**: Realizar a tarefa técnica.
   - **Step 4 — Relatórios**: Escrever o log da sessão, atualizar o Quadro de Avisos (novo arquivo) e, se necessário, o `EXPERIENCE.md`.
   - **Step 5 — Pull Request**: Abrir a PR com o label correto.

## 3. Acesso ao GitHub (REST API via Curl)
Como o Jules não possui `gh` CLI, utilize exemplos de `curl` com `$GITHUB_TOKEN` para:
- Listar arquivos.
- Criar novos arquivos (logs e avisos).
- Atualizar arquivos existentes (usando o SHA).
- Abrir Pull Requests.

## 4. Filosofia
"A ordem gera clareza. O registro gera memória. A autonomia gera valor."
