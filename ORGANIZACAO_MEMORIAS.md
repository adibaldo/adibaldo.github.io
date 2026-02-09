# ORGANIZAÇÃO DAS MEMÓRIAS (ESTRATÉGIA DO FUNES)

Este guia define como as memórias do seu Adi serão organizadas e processadas para manter a "memória de elefante" da família Funes sempre afiada.

## 1. O Baú Principal (Memória Bruta)
Toda informação nova vinda de áudios, textos ou documentos será centralizada no arquivo `MEMORIA_ADI.md`. 
- **Estrutura:** Dividida por "Fases da Vida" (Raízes, Paraná, Curitiba, Rondônia) e "Tópicos de Interesse" (Direito, Maçonaria, Música, Corinthians).
- **Processo:** Sempre que o seu Adi contar um detalhe novo, o Funes deve atualizar este arquivo imediatamente após a prosa.

## 2. A Biblioteca de Causos (Memória Publicada)
O que for polido e aprovado pelo seu Adi vai para o blog `adibaldo.github.io` em Astro.
- **Coleção `posts`:** Crônicas, memórias rápidas e ensaios.
- **Coleção `places`:** Navegação geográfica (Barão de Cotegipe, Curitiba, Rolim de Moura, etc.).

## 3. O Livro (Memória Estruturada)
Para o projeto do livro de memórias, usaremos a técnica de "Capitulação Gradual":
- **Drafts:** Capítulos em andamento ficam na pasta `src/content/blog/` com a tag `draft: true` até que ele dê o "ok" final.
- **Linha do Tempo:** Usaremos o campo `timeline` no frontmatter para que o Funes possa ordenar os fatos cronologicamente, facilitando a montagem do índice do livro no futuro.

## 4. Recuperação e Contexto (Memory Search)
Antes de cada conversa, o Funes utiliza a ferramenta `memory_search` para:
- Puxar fatos que tenham "parecência" com o assunto atual.
- Verificar nomes de pessoas e lugares citados anteriormente para evitar repetições ou confusão.
- Surpreender o seu Adi com detalhes sensoriais (ex: cheiro da terra vermelha, som da Rádio Colombo).

## 5. Etiquetas de Identidade (Tags)
Para facilitar a busca no blog e no livro, usaremos:
- `memórias`: Fatos vividos.
- `ensaios`: Reflexões filosóficas (estilo Riobaldo).
- `crônicas`: Causos curtos e divertidos.
- `história`: Pesquisa arqueológica ou regional.
