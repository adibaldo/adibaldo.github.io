/**
 * Gera PDFs dos posts do blog Alfarrábios do Adi.
 *
 * - livro-completo.pdf  → todos os textos em ordem cronológica
 * - posts/<slug>.pdf    → um PDF por post
 *
 * Uso: node scripts/generate-pdfs.mjs
 */

import { mdToPdf } from 'md-to-pdf';
import matter from 'gray-matter';
import { readFileSync, readdirSync, mkdirSync } from 'node:fs';
import { writeFile } from 'node:fs/promises';
import { join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

// ── Caminhos ──

const ROOT = resolve(fileURLToPath(import.meta.url), '../..');
const BLOG_DIR = join(ROOT, 'src/content/blog');
const IMAGES_DIR = join(BLOG_DIR, 'images');
const FONTS_DIR = join(ROOT, 'public/fonts');
const STYLE_PATH = join(ROOT, 'scripts/pdf-style.css');
const OUTPUT_DIR = join(ROOT, 'public/pdfs');
const POSTS_DIR = join(OUTPUT_DIR, 'posts');

// ── URL base canônica ──
const BLOG_BASE_URL = 'https://adibaldo.github.io';

// ── Fontes ──

const FONT_FACES = [
  ['Playfair Display', 600, 'playfair-display-latin-600-normal.woff2'],
  ['Playfair Display', 600, 'playfair-display-latin-ext-600-normal.woff2'],
  ['Playfair Display', 700, 'playfair-display-latin-700-normal.woff2'],
  ['Playfair Display', 700, 'playfair-display-latin-ext-700-normal.woff2'],
  ['Playfair Display', 700, 'playfair-display-latin-700-italic.woff2', 'italic'],
  ['Playfair Display', 700, 'playfair-display-latin-ext-700-italic.woff2', 'italic'],
  ['Playfair Display', 900, 'playfair-display-latin-900-normal.woff2'],
  ['Playfair Display', 900, 'playfair-display-latin-ext-900-normal.woff2'],
  ['Source Serif 4', 400, 'source-serif-4-latin-400-normal.woff2'],
  ['Source Serif 4', 400, 'source-serif-4-latin-ext-400-normal.woff2'],
  ['Source Serif 4', 400, 'source-serif-4-latin-400-italic.woff2', 'italic'],
  ['Source Serif 4', 400, 'source-serif-4-latin-ext-400-italic.woff2', 'italic'],
  ['Source Serif 4', 600, 'source-serif-4-latin-600-normal.woff2'],
  ['Source Serif 4', 600, 'source-serif-4-latin-ext-600-normal.woff2'],
  ['Source Serif 4', 700, 'source-serif-4-latin-700-normal.woff2'],
  ['Source Serif 4', 700, 'source-serif-4-latin-ext-700-normal.woff2'],
  ['Source Sans 3', 400, 'source-sans-3-latin-400-normal.woff2'],
  ['Source Sans 3', 400, 'source-sans-3-latin-ext-400-normal.woff2'],
  ['Source Sans 3', 500, 'source-sans-3-latin-500-normal.woff2'],
  ['Source Sans 3', 500, 'source-sans-3-latin-ext-500-normal.woff2'],
  ['Source Sans 3', 600, 'source-sans-3-latin-600-normal.woff2'],
  ['Source Sans 3', 600, 'source-sans-3-latin-ext-600-normal.woff2'],
];

function buildFontFaceCss() {
  return FONT_FACES.map(
    ([family, weight, file, style = 'normal']) =>
      `@font-face {
  font-family: '${family}';
  font-style: ${style};
  font-weight: ${weight};
  src: url('file://${join(FONTS_DIR, file)}') format('woff2');
}`
  ).join('\n');
}

// ── Helpers ──

function formatDate(date) {
  return new Date(date).toLocaleDateString('pt-BR', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
  });
}

function readPosts() {
  const files = readdirSync(BLOG_DIR).filter(
    (f) => f.endsWith('.md') || f.endsWith('.mdx')
  );

  return files
    .map((file) => {
      const raw = readFileSync(join(BLOG_DIR, file), 'utf-8');
      const { data, content } = matter(raw);
      const slug = file.replace(/\.mdx?$/, '');
      return { slug, data, content };
    })
    .filter((p) => !p.data.draft)
    .sort((a, b) => new Date(a.data.pubDate) - new Date(b.data.pubDate));
}

// ── Pré-processamento de conteúdo (Bug 1B + Bug 2) ──

function resolveImagePaths(content) {
  // Converte ./images/xxx → file:// absoluto para que o Puppeteer resolva
  return content.replace(
    /\(\.\/images\//g,
    `(file://${IMAGES_DIR}/`
  );
}

function resolveInternalLinks(content) {
  // Converte links internos /blog/slug/ → https://adibaldo.github.io/blog/slug/
  return content.replace(
    /\]\(\/((?:blog|locais|tags|sobre)[^)]*)\)/g,
    `](${BLOG_BASE_URL}/$1)`
  );
}

function preprocessContent(content) {
  return resolveImagePaths(resolveInternalLinks(content));
}

// ── Hero image do frontmatter (Bug 1A) ──

function heroImageMarkdown(post) {
  if (!post.data.heroImage) return '';
  const absPath = resolve(BLOG_DIR, post.data.heroImage.replace(/^\.\//, ''));
  const alt = post.data.heroImageAlt || post.data.title;
  return `\n\n![${alt}](file://${absPath})\n\n`;
}

function postHeader(post) {
  const date = formatDate(post.data.pubDate);
  const place = post.data.placeLabel ? ` — ${post.data.placeLabel}` : '';
  const hero = heroImageMarkdown(post);
  return `# ${post.data.title}\n\n<p class="post-meta">${date}${place}</p>\n\n---\n${hero}\n`;
}

// ── Opções do md-to-pdf ──

function pdfOptions(css, title = 'Alfarrábios do Adi') {
  return {
    css,
    document_title: title,
    body_class: [],
    pdf_options: {
      format: 'A4',
      margin: { top: '30mm', right: '25mm', bottom: '30mm', left: '25mm' },
      printBackground: true,
      displayHeaderFooter: true,
      headerTemplate: '<div></div>',
      footerTemplate: `
        <div style="font-size: 9px; color: #999; text-align: center; width: 100%;">
          <span class="pageNumber"></span>
        </div>`,
    },
    launch_options: {
      args: ['--no-sandbox', '--disable-setuid-sandbox'],
    },
    marked_options: {
      breaks: false,
    },
  };
}

// ── Geração ──

async function generatePostPdf(post, css) {
  const md = postHeader(post) + preprocessContent(post.content);
  const result = await mdToPdf({ content: md }, pdfOptions(css, post.data.title));
  const outPath = join(POSTS_DIR, `${post.slug}.pdf`);
  await writeFile(outPath, result.content);
  console.log(`  posts/${post.slug}.pdf`);
}

async function generateBookPdf(posts, css) {
  const today = formatDate(new Date());

  const parts = [
    // Capa
    `<div class="cover">

# Alfarrábios do Adi

<p class="subtitle">Memórias, causos e ensaios — sem pressa.</p>

<p class="date">${today}</p>

</div>`,
  ];

  // Índice (Melhoria 3)
  const tocLines = posts.map((post, i) => {
    const date = formatDate(post.data.pubDate);
    const place = post.data.placeLabel ? ` — ${post.data.placeLabel}` : '';
    return `${i + 1}. **${post.data.title}** <span class="toc-meta">${date}${place}</span>`;
  });

  parts.push(`<div class="toc">

## Índice

${tocLines.join('\n')}

</div>`);

  // Capítulos
  for (const post of posts) {
    const date = formatDate(post.data.pubDate);
    const place = post.data.placeLabel ? ` — ${post.data.placeLabel}` : '';
    const hero = heroImageMarkdown(post);
    const content = preprocessContent(post.content);

    parts.push(
      `<div class="chapter">\n\n# ${post.data.title}\n\n<p class="post-meta">${date}${place}</p>\n\n---\n${hero}\n${content}\n\n</div>`
    );
  }

  const md = parts.join('\n\n');
  const result = await mdToPdf({ content: md }, pdfOptions(css, 'Alfarrábios do Adi — Livro Completo'));
  const outPath = join(OUTPUT_DIR, 'livro-completo.pdf');
  await writeFile(outPath, result.content);
  console.log('  livro-completo.pdf');
}

// ── Main ──

async function main() {
  console.log('Gerando PDFs...\n');

  mkdirSync(POSTS_DIR, { recursive: true });

  const styleCss = readFileSync(STYLE_PATH, 'utf-8');
  const fontsCss = buildFontFaceCss();
  const css = fontsCss + '\n' + styleCss;

  const posts = readPosts();
  console.log(`${posts.length} posts encontrados.\n`);

  // PDFs individuais
  console.log('PDFs individuais:');
  for (const post of posts) {
    await generatePostPdf(post, css);
  }

  // Livro completo
  console.log('\nLivro completo:');
  await generateBookPdf(posts, css);

  console.log('\nPronto!');
}

main().catch((err) => {
  console.error('Erro ao gerar PDFs:', err);
  process.exit(1);
});
