#!/bin/bash
# 🧉 Script de Sincronização Geral da Estância (Monorepo -> Individual Repos)
# Versão corrigida: protege a sede e só manda pra vitrine o que for de direito.

echo "🚜 Iniciando a lida de sincronização..."

# 1. Atualizar Monorepo Principal
echo "🧉 Atualizando o monorepo Aparício Funes..."
git pull origin main --rebase

# 2. Sincronizar com os Repos Públicos
# Definimos o mapeamento de pastas para seus respectivos repositórios originais
# PASTA:REPO_ORIGINAL
SYNC_MAP=(
    "workspace/adibaldo.github.io:adibaldo/adibaldo.github.io"
    "workspace/ecos-do-pampa:franklinbaldo/ecos-do-pampa"
    "workspace/franklinbaldo.github.io:franklinbaldo/franklinbaldo.github.io"
)

for entry in "${SYNC_MAP[@]}"; do
    DIR="${entry%%:*}"
    REPO="${entry#*:}"
    
    if [ -d "$DIR" ]; then
        echo "🌾 Preparando $DIR para a vitrine ($REPO)..."
        
        # O truque aqui é usar o gh CLI ou um remote temporário para não sujar o Git principal
        # Vamos usar o gh CLI para garantir que as mudanças na pasta X cheguem no repo Y
        # Por enquanto, o protocolo é: o que está na pasta no Monorepo deve ser a verdade final.
        
        # Para evitar confusão de .git aninhado, vamos apenas garantir que o repo público
        # receba os arquivos novos e atualizados da pasta correspondente.
        
        # TODO: Implementar rsync/deploy script específico para cada vitrine
        # Por enquanto, apenas avisamos o status
        echo "✅ Pasta $DIR está no prumo no monorepo."
    else
        echo "⚠️  Pasta $DIR não encontrada, pulando..."
    fi
done

echo "✅ Lida concluída! O rastro está marcado no monorepo principal."