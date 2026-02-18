# Refino de Diagramação PDF - 18/02/2026

**Objetivo**: Transformar a saída do `md-to-pdf` em algo que se assemelhe a um livro impresso clássico.

## Alterações Realizadas

### 1. Estilo (CSS)
- **Tipografia**:
  - Habilitei `font-feature-settings: "liga", "kern"` para melhorar o kerning e ligaduras.
  - Defini `Source Serif 4` como fonte principal do corpo.
  - Defini `Playfair Display` para títulos.
- **Layout**:
  - Ajustei margens para `25mm` (topo/fundo) e `20mm` (lados).
  - Adicionei tratamento para viúvas e órfãs (`widows: 3`, `orphans: 3`).
  - Imagens agora têm `max-width: 100%`, `height: auto` e evitam quebras de página.
  - `blockquote` com estilo mais refinado (borda esquerda, itálico, fundo suave).
- **Capa**:
  - Centralização vertical completa usando `flexbox` e `height: 100vh`.
  - Títulos da capa com tipografia mais imponente.

### 2. Script (`generate-pdfs.mjs`)
- **Sumário**: Implementei a geração automática de um sumário (TOC) para o livro completo, linkando para os capítulos.
- **Rodapé**: Adicionei uma linha separadora e centralizei a numeração da página com a classe `.pageNumber`.
- **Estrutura**: Ajustei a estrutura HTML injetada para usar IDs nos títulos, facilitando a navegação interna.

## Próximos Passos
- Verificar se o TOC funciona corretamente em leitores de PDF (links internos).
- Ajustar espaçamentos finos conforme feedback visual (se possível).
