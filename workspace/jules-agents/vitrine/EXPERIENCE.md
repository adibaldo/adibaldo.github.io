## 2026-02-17 - Missing Hero Image Alt
**Learning:** The `heroImage` field in the blog schema (`src/content.config.ts`) only accepts an image object/path and lacked an `alt` text field, causing generic fallback alt text in layouts.
**Action:** Added `heroImageAlt` to the schema and updated `src/layouts/BlogPost.astro` to use it. Future posts should always include this field.

## 2026-02-18 - Batch Metadata & SEO Fix
**Learning:** Found that `heroImage` was defined in frontmatter but not passed to the `Layout` component in `[...slug].astro`, rendering it useless for OpenGraph.
**Action:** Updated `[...slug].astro` to pass `image={post.data.heroImage}`.
**Strategy:** When images are missing, created placeholder files (copies of an existing one) to ensure valid paths in metadata and prevent broken links or build warnings, while signaling to the Design agent exactly which files need to be created.
