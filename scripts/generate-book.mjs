import puppeteer from 'puppeteer';
import { mkdirSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');

const htmlInput = join(ROOT, 'dist/book-export/index.html');
const outputDir = join(ROOT, 'public/pdfs');
const outputFile = join(outputDir, 'livro-completo.pdf');

mkdirSync(outputDir, { recursive: true });

if (!existsSync(htmlInput)) {
  console.error(`HTML não encontrado: ${htmlInput}`);
  process.exit(1);
}

console.log('Iniciando Puppeteer...');
const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
const page = await browser.newPage();

// Carrega o HTML local com file:// para que as imagens relativas funcionem
await page.goto(`file://${htmlInput}`, { waitUntil: 'networkidle0' });

console.log('Gerando PDF KDP (6x9 polegadas)...');
await page.pdf({
  path: outputFile,
  width: '6in',
  height: '9in',
  printBackground: true,
  margin: { top: '19mm', bottom: '19mm', left: '22mm', right: '13mm' },
});

await browser.close();
console.log(`✅ PDF gerado: ${outputFile}`);
