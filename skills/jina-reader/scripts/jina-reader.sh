#!/usr/bin/env bash
# jina-reader.sh - Fetch content or screenshot from a URL using Jina Reader API
# Usage: ./jina-reader.sh <url> [mode: markdown|screenshot] [output_file]

URL="$1"
MODE="${2:-markdown}"
OUTPUT="${3:-output.md}"

# Load API key from secrets if available
if [[ -f ~/.openclaw/secrets.env ]]; then
    source ~/.openclaw/secrets.env
fi

# Try JINA_API_KEY then check for specific key if not set
API_KEY="${JINA_API_KEY:-REDACTED_JINA_KEY}"

if [[ "$MODE" == "screenshot" ]]; then
    # Use r.jina.ai with screenshot mode.
    # Important for pages with lazy-loaded images:
    # - x-timeout: waits for fuller render
    # - x-wait-for-selector: waits until at least one <img> appears
    # - x-no-cache: avoids stale capture
    TMP_URL=$(mktemp)
    curl -s -H "Authorization: Bearer $API_KEY" \
         -H "X-Return-Format: screenshot" \
         -H "X-Timeout: 30" \
         -H "X-Wait-For-Selector: img" \
         -H "X-No-Cache: true" \
         "https://r.jina.ai/$URL" -o "$TMP_URL"

    SCREENSHOT_URL=$(cat "$TMP_URL")
    rm -f "$TMP_URL"

    if [[ "$SCREENSHOT_URL" == http* ]]; then
        curl -L "$SCREENSHOT_URL" -o "$OUTPUT"
        echo "✅ Screenshot saved to $OUTPUT"
        echo "MEDIA: $(realpath "$OUTPUT")"
    else
        echo "❌ Failed to get screenshot URL. Response: $SCREENSHOT_URL"
        exit 1
    fi
else
    # Default: markdown mode
    curl -s -H "Authorization: Bearer $API_KEY" \
         "https://r.jina.ai/$URL" -o "$OUTPUT"
    echo "✅ Content saved to $OUTPUT"
fi
