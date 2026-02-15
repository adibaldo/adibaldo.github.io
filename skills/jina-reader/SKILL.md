---
name: jina-reader
description: "Fetch clean markdown content or screenshots from any URL using the Jina Reader API. Use when you need to read a web page without clutter, bypass anti-bot measures, or take a visual screenshot of a website."
---

# Jina Reader

This skill uses the Jina Reader API to extract clean content or visual snapshots from web pages.

## API Key
The skill uses the Jina API key provided in the workspace secrets.

## Workflows

### 1. Extract Clean Markdown
Use this for reading articles, blog posts, or documentation without ads/clutter.
```bash
bash skills/jina-reader/scripts/jina-reader.sh "https://example.com" markdown "output.md"
```

### 2. Take a Screenshot
Use this to see how a page looks or to capture a visual record.
```bash
bash skills/jina-reader/scripts/jina-reader.sh "https://example.com" screenshot "screenshot.png"
```

## Tips
- Jina Reader is excellent for bypassing complex JS-heavy sites where standard `web_fetch` might fail.
- Use screenshots to verify UI changes or visual elements (like blog hero images).
- Always include the protocol (http/https) in the URL.
