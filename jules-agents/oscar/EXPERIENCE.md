# 🧠 Memória Técnica - Oscar

> *Registro contínuo de aprendizados sobre o repositório `adibaldo.github.io`.*

---

## 2025-05-18 - Arquitetura Astro

*   **Estrutura do Repositório**:
    *   O projeto segue a estrutura padrão Astro v5.
    *   `src/content/config.ts` define coleções `blog` e `places`, utilizando `astro:content` e `astro:loaders` (glob).
    *   `src/pages/index.astro` utiliza `getCollection` para popular a grid de posts e locais.
    *   `src/pages/blog/index.astro` utiliza `getCollection` para popular a grid de posts.
    *   `src/pages/blog/[...slug].astro` é o template dinâmico para posts.

*   **Otimizações**:
    *   **Imagens**: O uso de `astro:assets` `<Image />` é fundamental. Substituir dimensões fixas (`width={1200}`) por `widths` e `sizes` responsivos é crítico para performance em grids.
    *   **Prefetch**: Habilitar `prefetch: true` em `astro.config.mjs` melhora drasticamente a percepção de velocidade entre páginas.
    *   **Componentização**: Scripts de terceiros (como Giscus) devem ser encapsulados em componentes para manter layouts limpos.

*   **Padrões Identificados**:
    *   Uso consistente de `BaseHead.astro` para meta tags.
    *   Uso de JSON-LD para SEO estruturado.
    *   Estilos globais em `src/styles/global.css` e CSS scoped nos componentes `.astro`.

*   **Notas**:
    *   A integridade visual e o conteúdo narrativo são prioridade máxima e não devem ser alterados.
    *   Qualquer script inline complexo deve ser movido para um componente dedicado se reutilizável ou extenso.
