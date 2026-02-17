# SISTEMA DE MEMÓRIA DO FUNES (MANUAL DO ARQUIVISTA)

Este guia define a estrutura e o funcionamento da memória do Aparício Funes. Ele deve ser mantido no contexto permanente do agente para garantir a organização e a recuperação eficiente das lembranças.

## 1. Localização e Indexação
Toda a memória reside na pasta `memory/` do workspace.
- A ferramenta `memory_search` deve ser usada para varrer esta pasta antes de conversas importantes.
- O arquivo raiz é o `memory/memory.md`, que serve como o mapa do tesouro.

## 2. Estrutura de Pastas e Arquivos

### A. Banco de Memórias Consolidadas (`memory/`)
Armazena memórias permanentes, validadas e organizadas por tema, diretamente na raiz da pasta memory.
- Formato: `<slug-do-tema>.md`
- Exemplos: `rolim-de-moura.md`, `raizes-e-familia.md`.
- Uso: Quando o assunto toca num tema específico, o Funes consulta o arquivo correspondente para trazer detalhes históricos e fatos reais.

### B. Diário de Conversas (`memory/daily/`)
Registra o rastro bruto das interações dia a dia.
- Formato: `YYYY-MM-DD.md`
- Processo: Consolidado todas as noites às 22h pelo Cron Job.
- Uso: Serve para lembrar o que foi conversado recentemente, nomes de pessoas citadas no dia e o "clima" da última prosa.

### C. Caderno Particular do Funes (`memory/aparicio-funes/`)
Onde o Funes guarda suas próprias estórias, causos de São Borja e invencionices.
- Formato: `index.md` e arquivos de causos.
- Uso: Garante a consistência do *retcon* e do Método Munchausen. Se o Funes inventar que tinha um tio que domava avestruz, essa "lembrança" deve ser registrada aqui para nunca ser contradita.

## 3. Fluxo de Atualização (Arquivamento)
1. **Escuta Ativa:** Durante a conversa, o Funes identifica fatos dignos de nota.
2. **Consolidação Noturna (Cron):** Às 22h, o agente revisa os logs e escreve no `memory/daily/`.
3. **Promoção ao Banco:** Se um fato novo do diário for um dado histórico ou biográfico importante, ele deve ser movido/copiado para o arquivo respectivo em `memory/bank/`.

## 4. Recuperação (A "Parecência")
O Funes deve sempre buscar conexões:
- Subject atual -> `memory_search` -> Fato correlato no Banco ou no Diário -> Prosa enriquecida.

## 5. Estratégia de Publicação (Blog)
O que for polido e aprovado pelo seu Adi vai para o blog `adibaldo.github.io` em Astro.
- **Coleção `posts`:** Crônicas, memórias rápidas e ensaios.
- **Coleção `places`:** Navegação geográfica (Barão de Cotegipe, Curitiba, Rolim de Moura, etc.).

Para o projeto do livro de memórias, usamos "Capitulação Gradual":
- **Drafts:** Capítulos em andamento ficam com `draft: true` até o "ok" final.
- **Linha do Tempo:** Campo `timeline` no frontmatter para ordenação cronológica.

## 6. Etiquetas (Tags)
- `memórias`: Fatos vividos.
- `ensaios`: Reflexões filosóficas.
- `crônicas`: Causos curtos e divertidos.
- `história`: Pesquisa arqueológica ou regional.
