# Auditoria OG Images — Blog Adi (adibaldo.github.io)

**Data:** 2026-03-27
**Auditor:** Claude Code (despachado por Aparício Funes, ciclo 04:20 UTC)
**Total de posts:** 41
**Total de arquivos OG estáticos:** 42

---

## Resumo Executivo

**Resultado: OG images estão funcionais em produção.** O sistema usa geração dinâmica de cards OG via Satori (`src/pages/og/[slug].png.ts`), que gera imagens `.png` para todos os posts no build. Porém, há **debt técnico significativo** no frontmatter e arquivos estáticos.

### Achados Principais

| # | Severidade | Achado | Impacto |
|---|-----------|--------|---------|
| 1 | ⚠️ INFO | Campo `og:image` no frontmatter é **código morto** | Nenhum — campo ignorado pelo layout |
| 2 | ⚠️ AVISO | 19 posts com frontmatter `og:image` apontando `.jpg`, mas meta tag renderizada é sempre `.png` | Confusão para mantenedores |
| 3 | ⚠️ AVISO | 19 arquivos `.jpg` órfãos em `public/og/` | ~2MB de peso morto no repo |
| 4 | ⚠️ INFO | 1 arquivo `.png` órfão sem post correspondente | Arquivo residual |
| 5 | ℹ️ INFO | Possível duplicata: `a-final-e-natal.md` (Mar 12) vs `afinal-e-natal.md` (Feb 12) | Verificar se intencional |

---

## Detalhe 1: Campo `og:image` no frontmatter é ignorado

O layout `BlogPost.astro` (linha 20) gera a URL do OG image assim:

```js
const imageUrl = slug ? `/og/${slug}.png` : undefined;
```

O campo `og:image` do frontmatter **nunca é lido**. A URL é construída a partir do slug, sempre com extensão `.png`. O endpoint dinâmico `src/pages/og/[slug].png.ts` gera os cards via Satori no build.

**Recomendação:** Remover o campo `og:image` de todos os 41 posts para evitar confusão, ou documentar que é apenas referência.

---

## Detalhe 2: Frontmatter com extensão `.jpg` incorreta (19 posts)

Estes posts declaram `og:image` com extensão `.jpg`, mas o meta tag real será `.png`:

| Post | Frontmatter `og:image` | Meta tag real |
|------|----------------------|---------------|
| a-morte-do-gerente | `/og/a-morte-do-gerente.jpg` | `/og/a-morte-do-gerente.png` |
| a-primeira-carreteada | `/og/a-primeira-carreteada.jpg` | `/og/a-primeira-carreteada.png` |
| as-ultimas-campereadas-do-vovo-franquelim | `/og/…franquelim.jpg` | `/og/…franquelim.png` |
| cacaieiros | `/og/cacaieiros.jpg` | `/og/cacaieiros.png` |
| comedor-de-bananas | `/og/comedor-de-bananas.jpg` | `/og/comedor-de-bananas.png` |
| eleicao-na-oab-ro | `/og/eleicao-na-oab-ro.jpg` | `/og/eleicao-na-oab-ro.png` |
| festa-de-casamento | `/og/festa-de-casamento.jpg` | `/og/festa-de-casamento.png` |
| forte-principe-da-beira | `/og/forte-principe-da-beira.jpg` | `/og/forte-principe-da-beira.png` |
| historia-do-povo-ucraniano | `/og/…ucraniano.jpg` | `/og/…ucraniano.png` |
| miguel-e-a-feira-do-largo-da-ordem | `/og/…largo-da-ordem.jpg` | `/og/…largo-da-ordem.png` |
| nego-ingles | `/og/nego-ingles.jpg` | `/og/nego-ingles.png` |
| o-embalsamento | `/og/o-embalsamento.jpg` | `/og/o-embalsamento.png` |
| o-povo-esta-enfezado | `/og/…enfezado.jpg` | `/og/…enfezado.png` |
| o-primeiro-juri | `/og/o-primeiro-juri.jpg` | `/og/o-primeiro-juri.png` |
| pe-de-jaca | `/og/pe-de-jaca.jpg` | `/og/pe-de-jaca.png` |
| prefacio | `/og/prefacio.jpg` | `/og/prefacio.png` |
| rondonia-de-verdade | `/og/rondonia-de-verdade.jpg` | `/og/rondonia-de-verdade.png` |
| rondonia-por-ali-fui-e-por-aqui-estou | `/og/…por-aqui-estou.jpg` | `/og/…por-aqui-estou.png` |
| tudo-passa-por-guarapuava | `/og/…guarapuava.jpg` | `/og/…guarapuava.png` |

---

## Detalhe 3: Arquivos `.jpg` órfãos em `public/og/`

19 arquivos `.jpg` em `public/og/` que não são referenciados por nenhum meta tag (o layout só gera URLs `.png`):

```
public/og/a-morte-do-gerente.jpg
public/og/a-primeira-carreteada.jpg
public/og/as-ultimas-campereadas-do-vovo-franquelim.jpg
public/og/cacaieiros.jpg
public/og/comedor-de-bananas.jpg
public/og/eleicao-na-oab-ro.jpg
public/og/festa-de-casamento.jpg
public/og/forte-principe-da-beira.jpg
public/og/historia-do-povo-ucraniano.jpg
public/og/miguel-e-a-feira-do-largo-da-ordem.jpg
public/og/nego-ingles.jpg
public/og/o-embalsamento.jpg
public/og/o-povo-esta-enfezado.jpg
public/og/o-primeiro-juri.jpg
public/og/pe-de-jaca.jpg
public/og/prefacio.jpg
public/og/rondonia-de-verdade.jpg
public/og/rondonia-por-ali-fui-e-por-aqui-estou.jpg
public/og/tudo-passa-por-guarapuava.jpg
```

**Recomendação:** Deletar estes arquivos para reduzir tamanho do repo.

---

## Detalhe 4: Arquivo `.png` órfão

```
public/og/o-cavalo-javali-e-o-misterio-das-aboboras.png
```

Não existe post com slug `o-cavalo-javali-e-o-misterio-das-aboboras`. O post atual é `cavalo-javali.md`. Provável resíduo de renomeação.

---

## Detalhe 5: Possível duplicata de post

- `a-final-e-natal.md` — pubDate: 2026-03-12, título: "A Final é Natal"
- `afinal-e-natal.md` — pubDate: 2026-02-12, título: "Afinal, é Natal (ou o uso do cachimbo que entortou a boca)"

Podem ser versões diferentes do mesmo tema. Verificar se ambos são intencionais.

---

## Validação dos Critérios

| Critério | Resultado |
|----------|-----------|
| ✅ `og:image` presente no frontmatter | 41/41 posts |
| ✅ URL começa com `/` | 41/41 posts |
| ✅ URL não é localhost/placeholder | 41/41 posts |
| ✅ Endpoint dinâmico gera cards para todos os posts | Sim (`getStaticPaths` itera todos) |
| ⚠️ Frontmatter `og:image` é usado pelo layout | **NÃO** — campo ignorado |
| ⚠️ Extensão no frontmatter coincide com a real | 22/41 (.png) OK, 19/41 (.jpg) incorretos |

---

## Ações Recomendadas (PR)

1. **Remover campo `og:image` dos 41 posts** — é dead code que confunde mantenedores
2. **Deletar 19 arquivos `.jpg` órfãos** em `public/og/`
3. **Deletar 1 arquivo `.png` órfão** (`o-cavalo-javali-e-o-misterio-das-aboboras.png`)
4. **Adicionar comentário no `BlogPost.astro`** documentando que OG cards são gerados dinamicamente

---

*Relatório gerado automaticamente por Claude Code — Auditoria OG Images*
