# UI Spec — Caderno do seu Adi

## 1. Visão Geral

**Conceito:** Blog pessoal de memórias, crônicas e ensaios com estética de caderno envelhecido — acolhedor, nostálgico e intimista. O autor ("seu Adi") compartilha reflexões sobre lugares, vivências e o passar do tempo. Um mapa interativo conecta os textos aos locais que marcaram sua jornada.

**Público-alvo:** Leitores de crônicas e memórias; familiares e amigos do autor; pessoas interessadas em narrativas de vida ligadas ao interior do Paraná, Santa Catarina e Rondônia.

**Tom visual:** Quente, orgânico, analógico. Evoca papel envelhecido, café, tardes de varanda. Nada frio nem corporativo.

**Plataforma:** Web responsivo (mobile-first). Sem necessidade de app nativo.

---

## 2. Design System

### 2.1 Paleta de Cores

| Token               | Hex       | Uso                                      |
|----------------------|-----------|------------------------------------------|
| `--bg-primary`       | `#FDF0E2` | Fundo principal (creme claro)            |
| `--bg-gradient-start`| `#F5C77E` | Início do gradiente hero (pêssego)       |
| `--bg-gradient-end`  | `#FDF0E2` | Fim do gradiente hero                    |
| `--bg-card`          | `#FFFFFF` | Fundo dos cards                          |
| `--bg-dark`          | `#1A1A1A` | Fundo modo leitura noturno               |
| `--text-primary`     | `#1A1A1A` | Texto principal                          |
| `--text-secondary`   | `#6B5B4F` | Texto secundário / datas                 |
| `--text-muted`       | `#9B8B7F` | Texto terciário / placeholders           |
| `--text-dark-mode`   | `#E8DDD0` | Texto no modo noturno                    |
| `--accent-primary`   | `#D4874E` | Botões CTA, links ativos, destaques      |
| `--accent-hover`     | `#C07640` | Hover do accent                          |
| `--tag-bg`           | `#F0E6D8` | Background das tags de categoria         |
| `--tag-text`         | `#6B5B4F` | Texto das tags                           |
| `--border-light`     | `#E8DDD0` | Bordas sutis dos cards                   |
| `--border-card`      | `#D4C4B0` | Borda dos cards no hover                 |
| `--map-pin`          | `#D4874E` | Pins do mapa                             |
| `--map-bg`           | `#F5E6D0` | Fundo estilizado do mapa                 |

### 2.2 Gradientes

- **Hero gradient:** `linear-gradient(180deg, #F5C77E 0%, #FDF0E2 100%)`
- **Modo noturno hero:** `linear-gradient(180deg, #2A2218 0%, #1A1A1A 100%)`
- **Overlay sutil em imagens:** `linear-gradient(180deg, rgba(253,240,226,0) 0%, rgba(253,240,226,0.8) 100%)`

### 2.3 Tipografia

| Elemento             | Família                         | Peso   | Tamanho (desktop) | Tamanho (mobile) |
|----------------------|---------------------------------|--------|--------------------|-------------------|
| Título do blog       | **Playfair Display** (serif)    | 900    | 72px               | 40px              |
| H1 (hero)            | **Playfair Display**            | 700    | 32px               | 24px              |
| H2 (seções)          | **Playfair Display**            | 700    | 24px               | 20px              |
| H3 (cards)           | **Playfair Display**            | 600    | 18px               | 16px              |
| Corpo                | **Source Serif 4** (serif)      | 400    | 16px               | 15px              |
| Corpo (leitura)      | **Source Serif 4**              | 400    | 19px               | 17px              |
| Navegação            | **Source Sans 3** (sans-serif)  | 500    | 15px               | 14px              |
| Tags / metadados     | **Source Sans 3**               | 400    | 13px               | 12px              |
| Botões               | **Source Sans 3**               | 600    | 14px               | 14px              |

**Line-height:** Corpo 1.7 · Títulos 1.3 · Navegação 1.0

**Fallback stack:** `'Playfair Display', Georgia, 'Times New Roman', serif` / `'Source Sans 3', -apple-system, sans-serif`

### 2.4 Espaçamento

| Token       | Valor  | Uso                         |
|-------------|--------|-----------------------------|
| `--space-xs`  | 4px    | Gaps mínimos                |
| `--space-sm`  | 8px    | Padding interno de tags     |
| `--space-md`  | 16px   | Padding de cards            |
| `--space-lg`  | 24px   | Gap entre cards             |
| `--space-xl`  | 40px   | Margem entre seções         |
| `--space-2xl` | 64px   | Padding do hero             |
| `--space-3xl` | 96px   | Margem superior do conteúdo |

**Max-width do conteúdo:** 1120px (container) · 720px (texto de leitura)

### 2.5 Bordas e Sombras

- **Card radius:** `12px`
- **Button radius:** `24px` (pill)
- **Tag radius:** `16px` (pill)
- **Card shadow (repouso):** `0 1px 3px rgba(0,0,0,0.06)`
- **Card shadow (hover):** `0 4px 12px rgba(0,0,0,0.1)`
- **Card border:** `1px solid var(--border-light)`
- **Navbar shadow (ao scroll):** `0 1px 8px rgba(0,0,0,0.05)`

### 2.6 Ícones

Conjunto: **Lucide** ou **Phosphor** (estilo outline, stroke 1.5px). Tamanho padrão: 20×20px. Usados em: navegação, redes sociais (footer), toggle modo leitura, busca, setas de paginação.

---

## 3. Componentes

### 3.1 Navbar

```
┌──────────────────────────────────────────────────────────┐
│  Início   Textos   Locais   Sobre   Buscar  [☽ ☀ Toggle]│
│  ─────                                                   │
└──────────────────────────────────────────────────────────┘
```

- **Posição:** Sticky top, background transparente que ganha `--bg-primary` + blur no scroll
- **Active state:** Underline de 2px com `--accent-primary` abaixo do item ativo
- **Hover:** Cor muda para `--accent-primary`
- **Toggle modo leitura:** Pílula com ícone sol/lua, slide suave (300ms ease)
- **Mobile:** Hambúrguer à direita, menu desliza de cima com overlay semitransparente
- **Logo/título:** Não aparece na navbar (o título principal fica no hero). Em páginas internas, o nome "Caderno do seu Adi" aparece como texto pequeno à esquerda da navbar

### 3.2 Hero Section

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│          Caderno do seu Adi                               │
│          (título grande, serif bold)                      │
│                                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │ Navbar                                              │  │
│  └────────────────────────────────────────────────────┘  │
│                                                          │
│  Bem-vindo ao meu canto de reflexões                     │
│  Compartilho histórias, pensamentos e lugares            │
│  que marcaram minha jornada.                             │
│                                                          │
│  [ Ler meu diário ]                                      │
│                                                          │
└──────────────────────────────────────────────────────────┘
  (fundo: gradiente peach → creme)
```

- **Título do blog:** Centralizado, `font-size: 72px`, peso 900, com leve `text-shadow` para profundidade
- **Subtítulo (H1):** Alinhado à esquerda dentro do container, peso 700
- **Descrição:** 2 linhas, `--text-secondary`, max-width 480px
- **CTA "Ler meu diário":** Botão pill, background `--accent-primary`, texto branco, padding `12px 28px`, hover escurece 10%
- **Animação de entrada:** Fade-in + translate-up escalonado (título → subtítulo → descrição → botão), 400ms each, 100ms delay entre elementos

### 3.3 Card de Post

```
┌──────────────────────────┐
│ O cheiro do café          │  ← H3, Playfair Display 600
│ na varanda                │
│                           │
│ 11/08/2023  ┌─────────┐  │
│             │ Memórias │  │  ← Tag pill
│             └─────────┘  │
│                           │
│ Compartilho histórias,    │  ← Descrição truncada (3 linhas)
│ pensamentos e lugares     │
│ que marcaram minha jo...  │
│                           │
│ ┌──────────┐              │
│ │ Ler mais │              │  ← Botão outline
│ └──────────┘              │
└──────────────────────────┘
```

**Anatomia:**
- **Container:** Background branco, border `1px solid --border-light`, border-radius `12px`, padding `24px`
- **Título (H3):** Playfair Display 600, `--text-primary`, max 2 linhas com `line-clamp: 2`
- **Metadados:** Data em `--text-muted` (formato DD/MM/YYYY) + Tag de categoria como pill (`--tag-bg`, `--tag-text`)
- **Descrição:** `--text-secondary`, `line-clamp: 3`, font-size 14px
- **Botão "Ler mais":** Outline, border `1px solid --border-card`, border-radius `16px`, padding `6px 16px`, font-size 13px
- **Hover do card:** Sombra aumenta, borda muda para `--border-card`, transição 200ms
- **Categorias possíveis:** Memórias, Ensaios, Crônicas (cada uma pode ter cor de tag levemente diferente no futuro)

**Grid layout:** 4 colunas no desktop (280px min) · 2 no tablet · 1 no mobile (card ocupa largura total com padding lateral)

### 3.4 Seção "Locais da Vida" (Mapa)

```
┌──────────────────────────────────────────────────────────┐
│  Locais da vida                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │                                                     │  │
│  │    📍 Barão de Cotegipe    📍 Francisco Beltrão     │  │
│  │                                                     │  │
│  │         📍 Itapejara         📍 Jaborá              │  │
│  │                                                     │  │
│  │                    📍 Curitiba    📍 Rolim de Moura  │  │
│  │                                                     │  │
│  └────────────────────────────────────────────────────┘  │
│  (mapa estilizado, tons terrosos)                        │
└──────────────────────────────────────────────────────────┘
```

- **Mapa base:** Estilo custom com tons terrosos (Mapbox ou Leaflet com tiles customizados). Sem o visual padrão do Google Maps — deve parecer um mapa antigo/ilustrado
- **Pins:** Ícone de gota em `--map-pin`, com label de texto ao lado
- **Interação pin:** Hover mostra tooltip com nome do local + nº de textos associados. Click abre modal/sidebar com lista dos textos daquele local
- **Borda do mapa:** `border-radius: 12px`, overflow hidden, leve sombra
- **Altura:** 400px desktop · 300px mobile
- **Na home:** Mapa mostra todos os locais. Na página "Locais" dedicada: mapa em tela cheia com painel lateral

### 3.5 Footer

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│              [fb] [tw] [ig] [yt]                          │
│                                                          │
│      © Caderno do seu Adi · All rights reserved.         │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

- **Ícones sociais:** 24×24px, `--text-muted`, hover `--accent-primary`, gap de 16px
- **Copyright:** `--text-muted`, font-size 13px
- **Padding:** `40px 0`
- **Separador:** Nenhum (o fundo contínuo do gradiente cria separação natural)

### 3.6 Toggle Modo Leitura

- **Visual:** Pílula com fundo `--tag-bg`, contendo ícone lua + sol, com slider circular que se move entre eles
- **Comportamento:** Alterna entre tema claro (padrão) e tema escuro
- **Tema escuro:** Fundo `--bg-dark`, texto `--text-dark-mode`, cards com fundo `#252525`, bordas `#333`, accent permanece o mesmo
- **Transição:** 400ms ease em `background-color`, `color` e `border-color` de todos os elementos via `transition` no `:root`
- **Persistência:** `prefers-color-scheme` como default, depois persiste escolha via `localStorage`

### 3.7 Botões

| Variante      | Background          | Texto        | Borda                    | Uso                     |
|---------------|----------------------|--------------|--------------------------|--------------------------|
| Primary       | `--accent-primary`   | `#FFFFFF`    | Nenhuma                  | CTA principal (hero)     |
| Outline       | Transparente         | `--text-secondary` | `1px solid --border-card` | "Ler mais" nos cards    |
| Ghost         | Transparente         | `--accent-primary` | Nenhuma                  | Links internos de texto  |

**Estados:** Hover (escurece 10%) · Focus (outline `2px solid --accent-primary` offset 2px) · Active (escurece 15%) · Disabled (opacity 0.5)

---

## 4. Páginas

### 4.1 Início (Home)

Composição vertical das seções:

1. **Hero** — título do blog + boas-vindas + CTA
2. **Últimas prosas** — grid de 4 cards dos posts mais recentes
3. **Locais da vida** — mapa com os locais do autor
4. **Footer**

### 4.2 Textos (Listagem)

- **Header:** Título "Textos" (H1) + subtítulo descritivo
- **Filtros:** Linha de pills clicáveis para filtrar por categoria (Todos · Memórias · Ensaios · Crônicas). Active state: fundo `--accent-primary`, texto branco
- **Ordenação:** Dropdown discreto "Mais recentes / Mais antigos"
- **Grid:** 3 colunas desktop, 2 tablet, 1 mobile. Cards idênticos ao componente 3.3
- **Paginação:** Botões "← Anteriores" e "Próximos →" no fundo, ou infinite scroll com indicador de carregamento
- **Estado vazio (filtro sem resultado):** Ilustração suave + "Nenhum texto encontrado nessa categoria"

### 4.3 Texto (Leitura Individual)

```
┌──────────────────────────────────────────────────────────┐
│  [← Voltar]                                              │
│                                                          │
│  O cheiro do café na varanda                              │
│  11/08/2023 · Memórias · 5 min de leitura                │
│  📍 Francisco Beltrão                                     │
│                                                          │
│  ─────────────────────────────────────────                │
│                                                          │
│  Lorem ipsum dolor sit amet, consectetur adipiscing       │
│  elit. Sed do eiusmod tempor incididunt ut labore...     │
│                                                          │
│  (texto corrido, max-width 720px, centralizado)          │
│                                                          │
│  ─────────────────────────────────────────                │
│                                                          │
│  ← Post anterior          Próximo post →                 │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

- **Max-width do texto:** 720px, margem auto
- **Tipografia de leitura:** Source Serif 4, 19px, line-height 1.8, `--text-primary`
- **Metadados:** Data + categoria + tempo estimado de leitura + local (clicável, leva ao mapa)
- **Separadores:** Linha fina `1px solid --border-light` antes e depois do corpo
- **Navegação entre posts:** Setas com título do post anterior/próximo
- **Imagens inline:** Max-width 100%, border-radius 8px, legenda em itálico abaixo
- **Blockquotes:** Borda esquerda 3px `--accent-primary`, padding-left 24px, itálico
- **Drop cap (opcional):** Primeira letra do texto em Playfair Display, 4 linhas de altura, float left

### 4.4 Locais (Mapa Expandido)

- **Layout:** Split view — mapa ocupa 60% à direita, lista de locais 40% à esquerda
- **Lista de locais:** Cards compactos com nome do local, nº de textos, minidescrição
- **Interação:** Click no local da lista centraliza o mapa no pin e abre tooltip. Click no pin filtra a lista
- **Mobile:** Mapa full-width no topo (250px), lista abaixo
- **Cada local expande:** Lista dos textos escritos sobre/naquele lugar

### 4.5 Sobre

- **Layout:** Coluna única, max-width 720px
- **Conteúdo:** Foto do autor (circular, 120px, border 3px `--accent-primary`) + bio em prosa
- **Tom:** Pessoal, escrito em primeira pessoa
- **Abaixo da bio:** Links para redes sociais em botões outline

### 4.6 Buscar

- **Acesso:** Click em "Buscar" na navbar abre overlay full-screen com campo de busca centralizado
- **Input:** Grande (font-size 24px), sem borda, apenas underline, autofocus
- **Resultados:** Aparecem abaixo em tempo real (debounce 300ms), mostrando título + trecho com match highlighted em `--accent-primary`
- **Tecla Escape:** Fecha o overlay
- **Sem resultado:** "Nenhum texto encontrado para '[query]'"

---

## 5. Responsividade

### Breakpoints

| Nome     | Range           | Colunas grid | Comportamento principal          |
|----------|-----------------|--------------|-----------------------------------|
| Mobile   | < 640px         | 1            | Menu hambúrguer, cards empilhados |
| Tablet   | 640px – 1024px  | 2            | Navbar compacta, grid 2 cols      |
| Desktop  | > 1024px        | 3–4          | Layout completo, mapa split-view  |

### Adaptações Mobile

- Título do blog: 40px (vs 72px)
- Hero padding reduzido: 32px (vs 64px)
- Cards de post: full-width, scroll horizontal opcional como alternativa ao empilhamento
- Mapa: altura 250px, pins com labels menores
- Footer: ícones maiores (touch target 44×44px)
- Busca: abre como página inteira ao invés de overlay

---

## 6. Interações e Microanimações

### 6.1 Transições Globais

| Propriedade        | Duração | Easing         |
|--------------------|---------|----------------|
| color, background  | 200ms   | ease           |
| box-shadow         | 200ms   | ease-out       |
| transform          | 300ms   | ease-out       |
| modo leitura       | 400ms   | ease-in-out    |
| overlay busca      | 300ms   | ease-out       |

### 6.2 Scroll Animations

- **Cards:** Fade-in + translate-y (20px → 0) conforme entram no viewport. Escalonamento de 80ms entre cards. Trigger: `IntersectionObserver` a 20% de visibilidade
- **Mapa:** Fade-in suave quando scroll atinge a seção
- **Seção "Últimas prosas":** Título faz slide-in da esquerda

### 6.3 Hover States

- **Cards:** Sombra aumenta, leve translate-y (-2px)
- **Botão CTA:** Escurece, leve scale(1.02)
- **Links de texto:** Underline animado da esquerda para direita
- **Pins do mapa:** Scale(1.2) + tooltip fade-in

### 6.4 Loading States

- **Skeleton screens:** Para cards e conteúdo de texto, usando gradiente animado em `--tag-bg` → `--bg-primary` → `--tag-bg`
- **Mapa:** Placeholder com fundo `--map-bg` e texto "Carregando mapa..."

---

## 7. Modo Leitura (Dark Mode)

### Mapeamento de Tokens

| Token Light          | Valor Dark   |
|----------------------|--------------|
| `--bg-primary`       | `#1A1A1A`    |
| `--bg-card`          | `#252525`    |
| `--text-primary`     | `#E8DDD0`    |
| `--text-secondary`   | `#B8A898`    |
| `--text-muted`       | `#7A6E62`    |
| `--border-light`     | `#333333`    |
| `--border-card`      | `#444444`    |
| `--accent-primary`   | `#E8A060`    |
| `--tag-bg`           | `#2A2520`    |
| `--map-bg`           | `#2A2218`    |

- O gradiente hero vira tons escuros quentes (marrom escuro → preto quente)
- Imagens recebem leve `filter: brightness(0.9)` para não agredir
- O toggle reflete o estado atual com ícone sol/lua

---

## 8. Acessibilidade

- **Contraste:** Todos os pares texto/fundo atendem WCAG AA (mínimo 4.5:1 para texto, 3:1 para texto grande)
- **Focus visible:** Outline de 2px `--accent-primary` com offset 2px em todos os elementos interativos
- **Skip link:** "Pular para o conteúdo" visível no focus, antes da navbar
- **Alt text:** Todas as imagens com alt descritivo; pins do mapa com `aria-label`
- **Semântica:** `<nav>`, `<main>`, `<article>`, `<aside>`, `<footer>` corretamente usados
- **Redução de movimento:** `@media (prefers-reduced-motion: reduce)` desabilita animações de scroll e transições complexas
- **Tamanho de toque:** Mínimo 44×44px para todos os alvos de toque no mobile

---

## 9. Stack Técnico Sugerido

| Camada          | Tecnologia                           | Justificativa                                      |
|-----------------|--------------------------------------|-----------------------------------------------------|
| Framework       | **Astro** ou **Next.js (SSG)**       | Blog estático, SEO excelente, performance           |
| Estilização     | **Tailwind CSS** + CSS custom props  | Design system consistente, tema fácil               |
| Mapa            | **Leaflet** + tiles Stamen/Stadia    | Open source, tiles estilizáveis com tom terroso      |
| Fontes          | **Google Fonts** (Playfair + Source)  | Gratuitas, CDN rápido                               |
| CMS             | **Markdown** ou **Sanity**           | Simples para o autor, flexível para o desenvolvedor |
| Busca           | **Pagefind** ou **Fuse.js**          | Client-side, sem servidor, rápido                   |
| Deploy          | **Vercel** ou **Netlify**            | Deploy automático, CDN global                       |
| Animações       | **CSS nativo** + IntersectionObserver| Performance, sem dependência pesada                  |

---

## 10. Estrutura de Dados (Content Model)

### Post

```
{
  title: string,
  slug: string,
  date: Date,
  category: "Memórias" | "Ensaios" | "Crônicas",
  location?: {
    name: string,
    lat: number,
    lng: number
  },
  excerpt: string,       // máx 160 chars
  body: markdown,
  readingTime: number,    // calculado automaticamente
  coverImage?: string     // opcional
}
```

### Local

```
{
  name: string,
  slug: string,
  lat: number,
  lng: number,
  description?: string,
  posts: Post[]           // relação reversa
}
```

---

## 11. Referência Visual Rápida

### Hierarquia cromática da página (top → bottom)

```
🟠 Gradiente pêssego forte (topo do hero)
     ↓ fade
🟡 Creme claro (corpo da página)
     ↓
⬜ Cards brancos (conteúdo em destaque)
     ↓
🟤 Mapa em tons terrosos
     ↓
🟡 Creme (footer)
```

### Hierarquia tipográfica

```
Caderno do seu Adi ─── Playfair 900, 72px (identidade)
  └── Bem-vindo ao... ─── Playfair 700, 32px (chamada)
       └── Últimas prosas ─── Playfair 700, 24px (seção)
            └── O cheiro do café ─── Playfair 600, 18px (card)
                 └── Corpo do texto ─── Source Serif 400, 16px
                      └── 11/08/2023 ─── Source Sans 400, 13px (meta)
```
