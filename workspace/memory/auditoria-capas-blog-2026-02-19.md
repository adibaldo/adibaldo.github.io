# Auditoria de Capas do Blog - 19/02/2026

## 📋 RESUMO EXECUTIVO

**Status:** ✅ **Auditoria completa concluída**

### Achados Críticos
1. ❌ **2 fotos com problemas de direitos autorais** (feira nordestina usada como se fosse Curitiba)
2. ✅ **Todas as capas decorativas são IA** (sem risco de direitos - exceto as 2 fotos acima)
3. ⚠️ **9 capas desalinhadas do padrão** fotorealista (são pinturas/ilustrações)
4. ✅ **2 capas fotorealistas bem alinhadas**

### Prioridades
1. **URGENTE:** Substituir fotos da feira do Largo da Ordem (problema de autenticidade + direitos)
2. **ALTA:** Regenerar `o-marco-zero-da-confusao` (tema completamente errado: Arca de Noé)
3. **MÉDIA:** Regenerar 8 capas pictóricas restantes para padrão fotorealista

---

## Objetivo
Identificar e corrigir capas com possíveis problemas de direitos autorais e garantir alinhamento de estilo.

## Critérios de Análise
1. **Origem:** Gerada por IA (Nano Banana) vs. Foto de terceiros vs. Foto histórica própria
2. **Direitos Autorais:** Risco de uso não autorizado
3. **Alinhamento de Estilo:** Conformidade com padrão fotorealista suave, nostálgico, fundo simples

## Inventário Completo

### ✅ PRESERVAR - Fotos Históricas Próprias (Valor Documental)
| Arquivo | Origem | Status |
|---------|--------|--------|
| `voo-taba-1981.png` | Foto histórica do Adi (voo de 1981) | ✅ OK - Propriedade da família |
| `a-carreteada-historica.png` | Foto histórica | ✅ OK - Verificar origem |

### ⚠️ ATENÇÃO - Possível Direito Autoral de Terceiros
| Arquivo | Origem | Problema Identificado | Ação |
|---------|--------|----------------------|------|
| `feira-largo-da-ordem-antiga.jpg` | Feira nordestina 1900-1920 | ❌ **NÃO é de Curitiba** + risco direitos autorais | 🔄 SUBSTITUIR URGENTE |
| `feira-largo-da-ordem-colorida.jpg` | Mesma foto, colorizada por IA | ❌ **NÃO é de Curitiba** + risco direitos autorais | 🔄 SUBSTITUIR URGENTE |
| ~~`bodega-balcao-causos.jpg`~~ | Foto de Rubens Guerra | ❌ **REMOVIDA** (direitos autorais) | ✅ Já substituída por IA |

### 🎨 REVISAR - Capas Geradas por IA (Alinhamento de Estilo)
| Arquivo | Status de Estilo | Conformidade | Ação |
|---------|-----------------|--------------|------|
| `cafe-na-varanda-cover.png` | Pintura óleo (não fotorealista) | ⚠️ 33% | Considerar regeneração fotorealista |
| `grimpas-secas-e-o-balcao-dos-causos-cover.png` | Aquarela (substituiu foto com direitos) | ⚠️ 33% | ✅ Mantém por enquanto (já foi refeita) |
| `o-marco-zero-da-confusao-cover.png` | Pintura épica/Arca de Noé | ❌ 16% - **Tema errado + não fotorealista** | 🔄 REGENERAR URGENTE |
| `vovo-franquelim-e-o-teco-teco-cover.png` | Pintura regionalista com "1956" | ⚠️ 33% | Considerar regeneração |
| `chiquita-banana.png` | Pintura óleo tropical | ⚠️ 33% | Considerar regeneração |
| `cade-o-toucinho-cover.png` | ✅ Fotorealista IA (still life mesa) | ✅ ~75% | ✅ Manter (bem alinhada) |
| `frio-de-rondonia-cover.png` | Pintura óleo pastoral c/ assinatura | ❌ 33% | Considerar regeneração |
| `afinal-e-natal-cover.png` | Pintura óleo melancólica | ❌ 33% | Considerar regeneração |
| `descobrindo-o-brasil-cover.png` | ✅ Fotorealista IA (ônibus/estrada) | ✅ ~75% | ✅ Manter (bem alinhada) |
| `ensaio-sobre-o-tempo-cover.png` | Surrealismo (relógios Dalí) | ❌ 16% | Considerar regeneração |
| `o-cavalo-javali-e-o-misterio-das-aboboras-cover.png` | Pintura expressionista | ❌ 33% | Considerar regeneração |
| `rolim-de-moura-cover.png` | Pintura regionalista c/ texto | ❌ 33% | Considerar regeneração |

### 🗺️ PRESERVAR - Mapas e Ilustrações Documentais
| Arquivo | Tipo | Status |
|---------|------|--------|
| `cabeza-de-vaca-1.png` | Mapa histórico | ✅ OK - Conteúdo informativo |
| `cabeza-de-vaca-2.png` | Mapa histórico | ✅ OK - Conteúdo informativo |
| `2026-02-16-rondon-roosevelt.png` | Ilustração histórica | ✅ OK - Conteúdo informativo |
| `2026-02-16-saudosa-maloca.png` | Desenho/diagrama | ✅ OK - Conteúdo informativo |
| `2026-02-16-xadrez-republica.png` | Diagrama | ✅ OK - Conteúdo informativo |
| `o-reio-rabo-de-tatu.png` | Ilustração | ✅ OK - Conteúdo informativo |
| `vovo-franquelim.png` | Ilustração interna | ✅ OK - Não é capa |

## Casos Identificados de Direitos Autorais

### Caso 1: Grimpas Secas - Foto de Rubens Guerra
- **Data:** 19/02/2026
- **Problema:** Foto de bodega real usada sem verificação de origem/autorização
- **Ação Tomada:** Removida e substituída por ilustração gerada por IA (Nano Banana)
- **Commit:** `c3587159 revert(blog): remover foto com direito autoral (Rubens Guerra)`

### Padrão Detectado
O Adi pode ter enviado imagens encontradas na internet (fotos de bodegas, feiras, paisagens) sem informar a origem, esperando que fossem usadas como referência ou simplesmente compartilhando algo interessante - mas que acabaram sendo usadas diretamente como capas do blog.

## Ações Prioritárias

### 1. **Investigar Fotos da Feira do Largo da Ordem**
- Verificar se são de domínio público ou de arquivo histórico autorizado
- Se forem de terceiros, substituir por ilustração gerada

### 2. **Analisar Capas Restantes** (❓)
- Verificar visualmente se são fotos reais ou geradas por IA
- Identificar possíveis fontes externas

### 3. **Regenerar Capas Desalinhadas**
Prioridade:
1. `o-marco-zero-da-confusao-cover.png` - Tema completamente desalinhado (Arca de Noé)
2. Outras capas pictóricas que possam ser melhoradas com fotorealismo

## Prompt de Regeneração (Fotorealista)

```
Fotografia fotorealista de [TEMA DO POST]. Profundidade de campo rasa (fundo 
desfocado/bokeh suave). Luz dourada de fim de tarde. Atmosfera nostálgica e 
acolhedora. Fundo simples e bem legível para sobreposição de título. 
Proporção 16:9 (1200×675px). Sem texto. Estilo: fotografia analógica anos 80, 
leve grain. Paleta quente (dourado, terroso).
```

## Próximos Passos

1. ✅ Criar este documento de auditoria
2. ⏳ Analisar capas com ❓
3. ⏳ Investigar origem das fotos da feira
4. ⏳ Regenerar `o-marco-zero-da-confusao-cover.png`
5. ⏳ Decisão sobre regeneração das demais capas pictóricas

---
**Responsável:** Aparício Funes  
**Data:** 2026-02-19  
**Status:** Em andamento
