# 🤖 Ecossistema de Agentes Jules (Aparício Funes Edition)

Este diretório contém as definições de "alma" (SOUL.md) e o rastro de aprendizado (EXPERIENCE.md) da nossa tropa de ajudantes eletrônicos. Eles são despachados via API do Jules para atuar no blog e nos nossos repositórios.

---

## 🏗️ O Framework Operacional (A Regra da Estância)

Todo agente Jules deve seguir rigorosamente este protocolo para garantir a continuidade e evitar bagunça no Git:

1.  **Memória de Curto Prazo (Logs):** Antes de agir, o agente lê os últimos 3 logs de sua pasta para saber o que foi feito ontem.
2.  **Memória de Longo Prazo (Experience):** O arquivo `EXPERIENCE.md` guarda aprendizados definitivos sobre o repositório ou as preferências do autor.
3.  **Comunicação (Quadro de Avisos):** Para evitar conflitos de merge, os avisos são arquivos individuais na pasta `quadro-de-avisos/`.
4.  **Autonomia:** O agente deve mapear o campo e encontrar sua própria lida dentro de sua missão principal.

---

## 👥 Nosso Roster (A Tropa)

| Agente | Missão Principal | Especialidade |
| :--- | :--- | :--- |
| **Alfarrabista** | Edição de Texto | Polimento de fluxo, títulos e sotaque do seu Adi. |
| **Biógrafo** | Resgate de Memória | Escavação de arquivos (Telegram) e consolidação de causos. |
| **Mari Kondo** | Ordem do Repo | Organização de arquivos, áudios e limpeza da raiz. |
| **Mosqueteiro** | Crônica Esportiva | Notícias e análises do dia a dia do Corinthians. |
| **Oscar** | Interface (UI/UX) | Legibilidade e estética inspirada no site `gwern.net`. |
| **Prosa-Adi** | Cartografia | Mapeamento de conexões e unificação de fragmentos. |
| **Rastreador** | Fiscal de Pendências | Auditoria de conversas para cobrar promessas não cumpridas. |
| **Veritas** | Fiscal da Verdade | Fact-checking histórico e factual para o blog. |
| **Vitrine** | SEO & Metadados | Otimização de frontmatter, tags e visibilidade. |
| **Tecedor** | Conexões Internas | Criação de links entre os posts das memórias. |

---

## 🛠️ Como Despachar um Agente

Use a skill `jules-session-manager` no Aparício. O fluxo básico é:
1.  Sincronizar o repositório (`git push`).
2.  Preparar o prompt concatenando o `SOUL.md` do agente com a missão da run.
3.  Disparar via `jules-api`.

---

## 🚫 Limites Sagrados
- Nunca retire a autonomia do agente dando ordens de passo-a-passo.
- Nunca mande um agente para o campo sem a sua alma (SOUL.md).
- Respeite sempre a "Voz do Adi" acima de qualquer regra técnica.
