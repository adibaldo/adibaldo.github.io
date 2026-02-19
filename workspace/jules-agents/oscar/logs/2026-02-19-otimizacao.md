# Relatório de Sessão Oscar: Otimização de Leitura - Barra de Progresso & Smooth Scroll

**Data:** 2026-02-19
**Foco:** Usabilidade de Leitura Longa (Gwern.net philosophy)

## Resumo das Alterações
1.  **Reading Progress Indicator**:
    -   Implementada uma barra de progresso fixa no topo da viewport (`#progress-container`) em `BlogPost.astro`.
    -   Estilo minimalista: altura de 4px, cor `var(--accent-primary)`, `z-index: 100`.
    -   Lógica JS: Calcula a porcentagem de rolagem baseada em `scrollHeight - innerHeight` e atualiza a largura da barra.
    -   Objetivo: Fornecer feedback visual imediato sobre o progresso da leitura em textos longos.

2.  **Smooth Scrolling**:
    -   Adicionado `scroll-behavior: smooth;` ao seletor `html` em `global.css`.
    -   Adicionado `scroll-padding-top: 80px;` para compensar o cabeçalho fixo (`.site-header`) ao navegar por links internos (âncoras).
    -   Objetivo: Melhorar a experiência de navegação interna e "table of contents" (se houver).

## Observações
A barra de progresso é uma adição subtil mas poderosa para blogs de conteúdo denso. O smooth scroll moderniza a sensação de navegação. Ambas as alterações respeitam a identidade visual existente e não requerem dependências externas.

## Próximos Passos Sugeridos
-   Considerar adicionar "Sidenotes" (notas laterais) no futuro, se o conteúdo justificar.
-   Avaliar a possibilidade de um "Table of Contents" gerado automaticamente para posts longos.
