---
name: monorepo-sync
description: "Sincroniza mudanças do Monorepo Aparício Funes para os repositórios individuais (blogs) e vice-versa. Essencial para publicar posts do seu Adi e do Franklin que foram editados via Jules no monorepo."
---

# 🔄 Monorepo Sync (O Protocolo do Capataz)

Esta skill resolve o dilema do "gado em dois pastos": as mudanças que acontecem no nosso monorepo (`franklinbaldo/aparicio-funes`) precisam chegar nos pastos individuais (os blogs `adibaldo.github.io`, `ecos-do-pampa`, etc.) para serem publicadas.

## 🏗️ A Estrutura da Sede

Nosso repositório principal é a sede operacional onde tudo é preparado.
As pastas de vitrine vivem dentro dele:
- `workspace/adibaldo.github.io/` -> Blog do seu Adi
- `workspace/ecos-do-pampa/` -> Eco do Pampa
- `workspace/franklinbaldo.github.io/` -> Blog do Franklin

## 🚧 REGRA DE OURO (NÃO QUEBRAR!)
**NUNCA** crie um repositório Git (`.git`) dentro dessas pastas de vitrine. O Git é gerido apenas na raiz do Aparício (`/agents/aparicio`).

## 🚜 Protocolo de Publicação

Sempre que um conteúdo estiver pronto para ir para a vitrine pública:

1. **Consolidação:** Garanta que os arquivos estão na pasta correta dentro do monorepo e faça o commit/push para a sede (`aparicio-funes`).
2. **Despacho Seletivo:** Use ferramentas de sincronização (como `gh` ou scripts de deploy) para enviar apenas os arquivos necessários para o repositório público correspondente.
3. **Deploy:** Acione o workflow de deploy no repositório de destino:
   ```bash
   gh workflow run "Deploy to GitHub Pages" --repo adibaldo/adibaldo.github.io
   ```

## 🛠️ Automação (Scripts)

O script `./workspace/skills/monorepo-sync/scripts/sync_all.sh` faz a lida de atualizar a sede, mas o despacho para o público deve ser feito com "pé no freio" e supervisão.

## 🌸 Filosofia
"A sede é o galpão de lida; a vitrine é o jardim da frente. Não se entra no jardim com a bota suja de barro."
