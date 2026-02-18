# Gutemberg Experience Log

This log documents learnings and best practices for PDF generation and typography.

## PDF Generation (Puppeteer & md-to-pdf)

- **Paged Media Support**: CSS Paged Media works surprisingly well with Puppeteer/Chrome headless, especially properties like `orphans`, `widows`, and `page-break-inside`.
- **Page Numbers**: Use the `footerTemplate` option in Puppeteer/md-to-pdf. Styles can be injected, and `.pageNumber` is automatically populated.
- **TOC Generation**: `md-to-pdf` doesn't auto-generate a TOC for merged content easily. Injecting a custom HTML list with anchors (`#slug`) works, provided headers have matching IDs.
- **Font Rendering**: Always enable `font-feature-settings: "liga" 1, "kern" 1;` for better typography, especially with serif fonts like `Source Serif 4`.
- **Image Handling**: `page-break-inside: avoid` on `img` or container elements is crucial to prevent awkward splits. `max-width: 100%` prevents overflow.

## Typography Decisions

- **Body**: `Source Serif 4` provides excellent readability for long texts, both on screen and print.
- **Headings**: `Playfair Display` adds a touch of elegance and contrast.
- **Margins**: `25mm` (top/bottom) and `20mm` (sides) offer a good balance for A4.
- **Widows/Orphans**: Setting to `3` lines prevents single lines at the top/bottom of pages, maintaining rhythm.
