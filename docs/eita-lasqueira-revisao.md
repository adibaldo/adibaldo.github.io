# Eita Lasqueira — critérios e registro da publicação inicial

Autor: Adi Baldo. Estado: **VERSÃO EM REVISÃO**.

Fonte: `EITA LASQUEIRA VERSÃO 1.docx`, fornecido pelo autor. Os Markdown
preparados em conversa anterior não foram localizados. Esta importação parte
do manuscrito completo, sem incorporar versões alternativas de capítulos.

## Estrutura

Conteúdo em `src/content/eita-lasqueira`, separado de `src/content/blog`.
O campo `order` determina a ordem do sumário e das páginas anterior/próxima.
Não altera a coletânea existente em `/livro` nem o feed de textos do blog.

A Quarta Parte foi movida para antes da Quinta. A Sétima foi movida para antes
da Oitava. O título original “NONA PARTE” passa a “OITAVA PARTE”, conforme
orientação do autor. Os demais títulos de parte seguem os títulos aprovados,
incluindo “ENFRENTANDO A AMAZÔNIA” e “VOVÔ FRANQUELIM”.

O sumário do Word, com números de páginas, foi substituído pelo sumário web.
A capa original fica na página inicial do livro. Os demais textos, inclusive
os apontamentos finais “Contra capa.” e “Não tem”, foram preservados.

## Revisão editorial

Esta entrega organiza e publica o manuscrito. Não é uma revisão linguística
integral do livro. Revisar posteriormente por parte, com mudanças pequenas e
identificáveis no histórico do Git.

- Corrigir somente ortografia, digitação, concordância e pontuação evidente.
- Preservar regionalismos, humor, ironia, exageros e expressões próprias.
- Sugestões de redação não devem ser aplicadas automaticamente.
- Identificar cada proposta como **Sugestão do revisor**, junto ao trecho.
- Não excluir trechos repetidos sem decisão do autor.

**Sugestão do revisor:** conferir os trechos “O Caçador de Marajás”, “O Plano
Real” e “A Boiada e o Fim do Mundo”, presentes na Terceira e na Quarta Parte.
As duas ocorrências foram mantidas, pois escolher uma versão seria uma decisão
editorial além da organização autorizada.

Para uma futura anotação visível junto ao texto:

```html
<aside class="reviewer-note">
  <strong>Sugestão do revisor:</strong> Proposta de alteração a avaliar pelo autor.
</aside>
```

## Gravuras

As imagens foram extraídas sem cortes, redesenho ou substituição. Conservam
a posição junto ao texto e a largura indicada no Word, limitada pela largura
da tela e pela resolução original. Incluem descrições alternativas visuais.

Proposta para a revisão de diagramação, ainda a avaliar imagem por imagem:

| Uso | Tamanho sugerido no impresso |
| --- | --- |
| Abertura de parte | 2/3 de página ou página inteira |
| Cena principal com vários elementos | Cerca de 1/2 página |
| Objeto simples ou vinheta | Cerca de 1/3 de página |
| Imagem muito detalhada | Preferir tamanho maior |

Na web, tamanho de página não equivale a largura de coluna. As classes
`illustration-small`, `illustration-medium`, `illustration-large` e
`illustration-full` permitem larguras de 33%, 50%, 67% e 100% da coluna.
Para aplicar uma escolha, remover a largura inline importada e atribuir a
classe adequada. Não impor tamanho pequeno a gravuras detalhadas no celular.

## Rastreabilidade

`eita-lasqueira-importacao.json` registra o hash da fonte, as faixas de blocos,
as palavras e as ocorrências de imagens por parte. O importador verifica que
todos os blocos do corpo foram atribuídos uma vez e que os textos se mantêm
idênticos durante a adaptação. Os títulos estruturais aprovados são a exceção
registrada; URLs e textos alternativos não entram nessa comparação.

Na conferência adicional da conversão, o inventário de 42.073 palavras do
corpo do Word coincidiu integralmente com o texto extraído pelo Pandoc antes
da substituição dos títulos estruturais. Foram preservadas as 60 ocorrências
de imagens do corpo (58 arquivos distintos), além da capa na página inicial.

`scripts/import-eita-lasqueira.py` documenta a conversão inicial. Exige Pandoc
e Pillow; não é executado no build do site. Não reexecutar sobre revisões já
feitas, pois ele substitui os Markdown. Editar os arquivos por parte diretamente.
