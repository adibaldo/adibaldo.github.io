# Capas e Social Cards (por post)

Este blog gera automaticamente um **social card (Open Graph)** para cada texto, no formato 1200×630.

- Link do card: `/og/<slug>.png`
- Quando você compartilha um texto no WhatsApp/Telegram, ele usa esse card.

## Capa (heroImage) por post — ideia do “Nano Banana”

Cada texto pode ter uma **capa** (imagem no topo do post e na listagem) usando o campo `heroImage`.

A capa é opcional — mas quando tem, deixa o texto com mais “cara de jornal/álbum”.

### Jeito simples de usar
1) Pense no tema do texto (ex.: "café na varanda", "estrada para Rondônia", "Curitiba em dia de frio").
2) Peça pro Aparício/Funes gerar uma imagem **no Nano Banana** com esse tema.
3) Salve a imagem em `src/content/blog/images/`.
4) No frontmatter do post, adicione:

```yaml
heroImage: ./images/minha-capa.png
```

### Prompt base (pra pedir a capa)

> "Crie uma capa para um post do blog 'Alfarrábios do Adi'. Estilo: varanda moderna, quente, nostálgico, fotorealista suave. Sem texto na imagem. Assunto: <DESCREVA A CENA>. Fundo simples e bem legível."

Dica: capas ficam melhores em **2:1** (ex.: 1200×600) ou **16:9**.
