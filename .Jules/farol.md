## 2026-02-17 - Missing Hero Image Alt
**Learning:** The `heroImage` field in the blog schema (`src/content.config.ts`) only accepts an image object/path and lacked an `alt` text field, causing generic fallback alt text in layouts.
**Action:** Added `heroImageAlt` to the schema and updated `src/layouts/BlogPost.astro` to use it. Future posts should always include this field.
