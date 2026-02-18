#!/bin/bash
# Script para encontrar "reses desgarradas" (arquivos órfãos) na memória

echo "🕵️ Rastreado arquivos desgarrados em memory/ e jules-agents/..."

# Lista todos os arquivos markdown que queremos monitorar
ALL_FILES=$(find memory jules-agents -name "*.md")

for FILE in $ALL_FILES; do
    # Pega apenas o nome do arquivo ou o caminho relativo
    FILENAME=$(basename "$FILE")
    
    # Ignora arquivos mestre
    if [[ "$FILENAME" == "MEMORY.md" || "$FILENAME" == "HEARTBEAT.md" ]]; then
        continue
    fi

    # Procura se esse nome de arquivo é mencionado em algum outro arquivo md
    COUNT=$(grep -r "$FILENAME" . --include="*.md" | grep -v "$FILE" | wc -l)

    if [ "$COUNT" -eq 0 ]; then
        echo "⚠️  DESGARRADO: $FILE (Ninguém aponta para este arquivo)"
    fi
done

echo "✅ Fim da ronda. O que estiver marcado com ⚠️ precisa de um nó no rastro."
