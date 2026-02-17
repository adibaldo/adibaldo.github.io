# Jina Reader Skill

Access Single-Page Applications (SPAs) and JavaScript-heavy websites using Jina Reader API.

## Overview

Jina Reader (`https://r.jina.ai/`) renders SPAs and returns clean markdown, perfect for sites like Suno, Medium, etc. that don't work with simple HTTP fetch.

## Usage

Simply prefix any URL with `https://r.jina.ai/`:

```bash
# Original URL
https://suno.com/@franklinbaldo

# Jina Reader URL
https://r.jina.ai/https://suno.com/@franklinbaldo
```

Use with `web_fetch` tool:

```typescript
web_fetch({
  url: "https://r.jina.ai/https://example.com/spa-page"
})
```

## When to Use

- **SPAs**: React, Vue, Angular apps (Suno, Twitter, GitHub)
- **Dynamic content**: JavaScript-generated pages
- **Paywalls**: Sometimes bypasses soft paywalls
- **Clean extraction**: Better markdown than raw HTML scraping

## When NOT to Use

- Static sites (use `web_fetch` directly)
- APIs (use direct API calls)
- When you need browser interaction (use `browser` tool)

## Examples

```bash
# Suno profile
https://r.jina.ai/https://suno.com/@franklinbaldo

# GitHub PR
https://r.jina.ai/https://github.com/owner/repo/pull/123

# Medium article
https://r.jina.ai/https://medium.com/@user/article
```

## Notes

- Free service (no API key required)
- Rate limits apply (be respectful)
- Returns plain text markdown
- Timeout ~15-20 seconds for complex pages

## Related

- Official docs: https://jina.ai/reader
- Alternative: `browser` tool (for interaction)
- Fallback: `web_fetch` (for simple pages)
