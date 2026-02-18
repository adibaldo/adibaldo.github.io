---
name: monorepo-sync
description: "Sincroniza mudanças do Monorepo Aparício Funes para os repositórios individuais (blogs) e vice-versa. Essencial para publicar posts do seu Adi e do Franklin que foram editados via Jules no monorepo."
---

# 🔄 Monorepo Sync (A Skill do Capataz)

Esta skill resolve o dilema do "gado em dois pastos": as mudanças que acontecem no nosso monorepo (`franklinbaldo/aparicio-funes`) precisam chegar nos pastos individuais (os blogs `adibaldo.github.io`, `ecos-do-pampa`, etc.) para serem publicadas.

## 🏗️ A Estrutura da Estância

Nosso workspace é organizado assim:
- `workspace/` (Raiz do Monorepo)
  - `adibaldo.github.io/` (Subdiretório sincronizado com o repo do seu Adi)
  - `ecos-do-pampa/` (Subdiretório sincronizado com o blog do Funes)
  - `franklinbaldo.github.io/` (Subdiretório sincronizado com o blog do Franklin)

## 🚜 Protocolo de Sincronização (Workflow)

Sempre que uma PR for mergeada no Monorepo que altere arquivos dentro das pastas `*.github.io` ou `ecos-do-pampa`, siga este rastro:

### 1. Sincronização Local (Trazer pro Galpão)
Certifique-se de que o monorepo está atualizado:
```bash
git pull origin main
```

### 2. Despachar para os Repos de Destino
Para cada pasta de blog alterada, entre nela e empurre as mudanças para o seu repositório original:

**Exemplo para o blog do seu Adi:**
```bash
cd workspace/adibaldo.github.io
git push origin main
```

*Nota: O `origin` dentro dessas pastas aponta para os repositórios individuais, enquanto na raiz ele aponta para o monorepo.*

### 3. Disparar a Prensa (Deploy)
Após o push, dispare o workflow de deploy para garantir que a tinta seque no papel:
```bash
gh workflow run "Deploy to GitHub Pages" --repo adibaldo/adibaldo.github.io
```

## 🛠️ Automação (Scripts)

Use o script `skills/monorepo-sync/scripts/sync_all.sh` para fazer a lida completa de uma vez.

## 🚫 Limites & Cuidados
- **Conflitos:** Se houver conflito entre o monorepo e o blog individual, resolva primeiro no blog individual, dê o push, e depois traga de volta para o monorepo.
- **Segredos:** Nunca deixe arquivos com segredos (API Keys) nas pastas dos blogs públicos.

## 🌸 Filosofia
"Mudança feita num canto, notícia espalhada em todo canto."
