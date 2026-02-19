# Base de Conhecimento: Oscar (Otimização Astro)

## 2026-02-19
- **Scroll Behavior**: Implementei `scroll-behavior: smooth` e `scroll-padding-top` para melhorar a navegação interna e compensar o cabeçalho fixo.
- **Progress Bar**: Adicionei uma barra de progresso de leitura em `BlogPost.astro`. A barra é renderizada no topo da viewport com `position: fixed` e `z-index: 100` para ficar acima do cabeçalho.
- **Aprendizado**: `scroll-padding-top` é crucial quando se tem cabeçalhos fixos (`position: sticky`).
- **Filosofia**: Melhorias subtis de UX (como feedback de leitura) aumentam a retenção em textos longos sem poluir a interface.
