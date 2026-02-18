---
name: alfarrabios-publisher
description: "Publish and maintain posts for the blog Alfarrábios do Adi (Astro + GitHub Pages). Use when the user asks to publish a post: polish Adi audio/text, choose tags + Locais da vida, generate a mandatory Nano Banana cover image, ensure per-post OG social card works, commit/push to the repo, and confirm deployment."
---

# Alfarrábios do Adi — Publicação (workflow)

## Workflow (sempre)

### 1) Captar o material
- Receber do Franklin/seu Adi: **áudio ou texto** + (se possível) o **local** e a **intenção** do texto (causo, ensaio, memória).
- Se vier áudio: transcrever, e devolver um rascunho curto pra confirmar o sentido.

### 2) Escrever o post final (o Funes assina o acabamento)
Entregar 2 opções quando couber:
- **Versão A (curta e direta)**
- **Versão B (mais caprichada/literária)**

Sempre incluir:
- Título (1–2 opções)
- Descrição curta (1 frase)
- Tags (1 principal + 0–2 secundárias)
- Local (quando fizer sentido)

### 3) Gerar capa obrigatória (Nano Banana)
- Todo post publicado **tem capa**.
- A capa deve ser **sem texto**, **sem pessoas**, estilo “varanda moderna” e legível como preview.
- Tamanho final: **1200×630** (PNG)
- Salvar em: `src/content/blog/images/<slug>-cover.png`
- Adicionar no frontmatter: `heroImage: ./images/<slug>-cover.png`

Use o script do skill:
```bash
python3 skills/alfarrabios-publisher/scripts/make_cover.py \
  --repo /home/franklin/.openclaw/workspace-adi/adibaldo.github.io \
  --slug "<slug>" \
  --prompt "<descrição da cena>"
```

### 4) Criar/editar o post no Astro
- Posts ficam em: `src/content/blog/<slug>.md`
- Frontmatter padrão (mínimo):
```yaml
title: "..."
description: "..."
pubDate: YYYY-MM-DD
tags: ["memórias"|"ensaios"|"crônicas"|"direito"|"história"]
place: "curitiba"          # opcional (slug)
placeLabel: "Curitiba"     # opcional
heroImage: ./images/<slug>-cover.png
```

### 5) Publicar (commit/push) e confirmar deploy
- Rodar build local se tiver mexido em componentes:
```bash
cd /home/franklin/.openclaw/workspace-adi/adibaldo.github.io
npm run build
```
- Commit/push:
```bash
python3 skills/alfarrabios-publisher/scripts/publish.py \
  --repo /home/franklin/.openclaw/workspace-adi/adibaldo.github.io \
  --message "Publish: <título>"
```

### 6) Confirmar com o Franklin
- Mandar os links:
  - Post: `https://adibaldo.github.io/textos/<slug>/`
  - Social card: `https://adibaldo.github.io/og/<slug>.png`
- Avisar sobre cache do WhatsApp/Telegram (se preciso usar `?v=2`).

## Recursos
- Referência de estrutura do blog e tags/locais: `references/blog.md`
- Prompts de capa (Nano Banana): `references/covers.md`
