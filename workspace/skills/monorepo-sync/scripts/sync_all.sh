#!/bin/bash
# Script de Sincronização Geral da Estância (Monorepo -> Individual Repos)

# 1. Atualizar Monorepo
echo "🧉 Atualizando o monorepo principal..."
git pull origin main

# 2. Sincronizar Blogs
BLOGS=("adibaldo.github.io" "ecos-do-pampa" "franklinbaldo.github.io")

for BLOG in "${BLOGS[@]}"; do
    if [ -d "$BLOG" ]; then
        echo "🚜 Sincronizando $BLOG..."
        cd "$BLOG"
        git push origin main
        
        # Tentar disparar o deploy via GH CLI
        # Detectar o owner do repo (adi ou franklin)
        REMOTE_URL=$(git remote get-url origin)
        if [[ $REMOTE_URL == *"adibaldo/adibaldo.github.io"* ]]; then 
            OWNER="adibaldo"
        else 
            OWNER="franklinbaldo"
        fi
        
        echo "🚀 Disparando deploy para $OWNER/$BLOG..."
        gh workflow run "Deploy to GitHub Pages" --repo "$OWNER/$BLOG"
        cd ..
    fi
done

echo "✅ Lida concluída! O gado está todo no pasto certo."
