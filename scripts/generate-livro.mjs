import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import matter from 'gray-matter';
import PDFDocument from 'pdfkit';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const BLOG_DIR = path.join(__dirname, '../src/content/blog');
const OUTPUT_DIR = path.join(__dirname, '../public/pdfs');
const OUTPUT_FILE = path.join(OUTPUT_DIR, 'livro-completo.pdf');

// Ensure output dir exists
fs.mkdirSync(OUTPUT_DIR, { recursive: true });

// Read and parse all posts
const files = fs.readdirSync(BLOG_DIR).filter(f => f.endsWith('.md'));
const posts = [];

for (const file of files) {
  const content = fs.readFileSync(path.join(BLOG_DIR, file), 'utf-8');
  const { data, content: body } = matter(content);
  if (!data.pubDate) continue;
  posts.push({
    title: data.title || file.replace('.md', ''),
    date: new Date(data.pubDate),
    description: data.description || '',
    body: body.trim(),
    file,
  });
}

// Sort chronologically (oldest first)
posts.sort((a, b) => a.date - b.date);

console.log(`Generating PDF with ${posts.length} posts...`);

const doc = new PDFDocument({
  size: 'A4',
  margins: { top: 72, bottom: 72, left: 72, right: 72 },
  info: {
    Title: 'Alfarrábios do Adi — Coletânea de Memórias',
    Author: 'Adi Baldo',
    Subject: 'Memórias, causos e lições de vida',
    CreationDate: new Date(),
  },
});

const stream = fs.createWriteStream(OUTPUT_FILE);
doc.pipe(stream);

const PAGE_WIDTH = doc.page.width;
const MARGIN = 72;
const TEXT_WIDTH = PAGE_WIDTH - MARGIN * 2;
const compilationDate = new Date().toLocaleDateString('pt-BR', { day: '2-digit', month: 'long', year: 'numeric' });

// Footer helper
function addFooter(doc, pageNum) {
  const bottom = doc.page.height - 36;
  doc.fontSize(9).fillColor('#888888');
  doc.text('Alfarrábios do Adi — Coletânea de Memórias', MARGIN, bottom, { width: TEXT_WIDTH, align: 'center' });
  doc.text(`${pageNum}`, MARGIN, bottom + 12, { width: TEXT_WIDTH, align: 'center' });
  doc.fillColor('#000000');
}

let pageNum = 1;

// ── COVER PAGE ──
doc.fontSize(32).fillColor('#2c3e50').font('Helvetica-Bold');
doc.text('Alfarrábios do Adi', MARGIN, 180, { width: TEXT_WIDTH, align: 'center' });

doc.fontSize(22).fillColor('#555555').font('Helvetica');
doc.text('Coletânea de Memórias', MARGIN, 240, { width: TEXT_WIDTH, align: 'center' });

doc.moveDown(3);
doc.fontSize(14).fillColor('#777777');
doc.text('por Adi Baldo', MARGIN, 310, { width: TEXT_WIDTH, align: 'center' });

doc.fontSize(11).fillColor('#999999');
doc.text(`Compilado em ${compilationDate}`, MARGIN, 360, { width: TEXT_WIDTH, align: 'center' });

doc.fontSize(10).fillColor('#aaaaaa');
doc.text(`${posts.length} histórias`, MARGIN, 390, { width: TEXT_WIDTH, align: 'center' });

// Decorative line
doc.moveTo(MARGIN + 60, 430).lineTo(PAGE_WIDTH - MARGIN - 60, 430).strokeColor('#cccccc').lineWidth(1).stroke();

addFooter(doc, pageNum);

// ── TABLE OF CONTENTS ──
doc.addPage();
pageNum++;

doc.fontSize(20).fillColor('#2c3e50').font('Helvetica-Bold');
doc.text('Sumário', MARGIN, MARGIN, { width: TEXT_WIDTH, align: 'center' });
doc.moveDown(1);

doc.fontSize(11).font('Helvetica').fillColor('#333333');
let tocY = doc.y;

for (let i = 0; i < posts.length; i++) {
  const post = posts[i];
  const dateStr = post.date.toLocaleDateString('pt-BR', { month: 'long', year: 'numeric' });
  const line = `${i + 1}. ${post.title}`;
  
  if (tocY > doc.page.height - 120) {
    addFooter(doc, pageNum);
    doc.addPage();
    pageNum++;
    tocY = MARGIN;
  }
  
  doc.fontSize(10).fillColor('#333333');
  doc.text(line, MARGIN, tocY, { width: TEXT_WIDTH - 80, continued: false });
  doc.fontSize(9).fillColor('#888888');
  doc.text(dateStr, MARGIN, tocY + 1, { width: TEXT_WIDTH, align: 'right' });
  
  tocY += 18;
}

addFooter(doc, pageNum);

// ── POSTS ──
for (let i = 0; i < posts.length; i++) {
  const post = posts[i];
  doc.addPage();
  pageNum++;

  // Chapter header
  doc.fontSize(9).fillColor('#888888').font('Helvetica');
  const dateStr = post.date.toLocaleDateString('pt-BR', { day: '2-digit', month: 'long', year: 'numeric' });
  doc.text(dateStr, MARGIN, MARGIN, { width: TEXT_WIDTH, align: 'right' });

  doc.fontSize(22).fillColor('#2c3e50').font('Helvetica-Bold');
  doc.text(post.title, MARGIN, MARGIN + 20, { width: TEXT_WIDTH });

  if (post.description) {
    doc.moveDown(0.5);
    doc.fontSize(12).fillColor('#666666').font('Helvetica-Oblique');
    doc.text(post.description, { width: TEXT_WIDTH });
  }

  // Divider
  doc.moveDown(0.8);
  const divY = doc.y;
  doc.moveTo(MARGIN, divY).lineTo(PAGE_WIDTH - MARGIN, divY).strokeColor('#dddddd').lineWidth(0.5).stroke();
  doc.moveDown(0.8);

  // Body text — strip markdown syntax roughly
  const cleanBody = post.body
    .replace(/^#{1,6}\s+/gm, '')       // headings
    .replace(/\*\*(.*?)\*\*/g, '$1')   // bold
    .replace(/\*(.*?)\*/g, '$1')       // italic
    .replace(/!\[.*?\]\(.*?\)/g, '')   // images
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') // links
    .replace(/^[\-\*]\s+/gm, '• ')    // bullets
    .replace(/\n{3,}/g, '\n\n')        // excess blank lines
    .trim();

  doc.fontSize(12).fillColor('#1a1a1a').font('Helvetica');
  doc.text(cleanBody, { width: TEXT_WIDTH, align: 'justify', lineGap: 3 });

  addFooter(doc, pageNum);
}

// ── COLOPHON ──
doc.addPage();
pageNum++;

doc.fontSize(12).fillColor('#555555').font('Helvetica');
const colophon = `Esta coletânea reúne ${posts.length} histórias publicadas no blog "Alfarrábios do Adi" entre ${posts[0].date.toLocaleDateString('pt-BR', { month: 'long', year: 'numeric' })} e ${posts[posts.length-1].date.toLocaleDateString('pt-BR', { month: 'long', year: 'numeric' })}.\n\nCompilado automaticamente por Aparício Funes em ${compilationDate}.\n\n"A memória é o único jardim que nunca murcha."`;
doc.text(colophon, MARGIN, 250, { width: TEXT_WIDTH, align: 'center' });

addFooter(doc, pageNum);

doc.end();

stream.on('finish', () => {
  const size = fs.statSync(OUTPUT_FILE).size;
  console.log(`✅ PDF gerado: ${OUTPUT_FILE}`);
  console.log(`   Tamanho: ${(size / 1024 / 1024).toFixed(2)} MB`);
  console.log(`   Páginas estimadas: ${pageNum}`);
  console.log(`   Posts incluídos: ${posts.length}`);
});

stream.on('error', (err) => {
  console.error('❌ Erro ao gerar PDF:', err);
  process.exit(1);
});
