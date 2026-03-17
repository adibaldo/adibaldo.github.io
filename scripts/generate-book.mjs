import { execSync } from 'child_process';
import { mkdirSync, existsSync, readFileSync, writeFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');

const htmlInput = join(ROOT, 'dist/book-export/index.html');
const htmlFixed = join(ROOT, 'dist/book-export/index-fixed.html');
const templateFile = join(ROOT, 'scripts/book-template.tex');
const outputDir = join(ROOT, 'public/pdfs');
const outputFile = join(outputDir, 'livro-completo.pdf');

mkdirSync(outputDir, { recursive: true });

if (!existsSync(htmlInput)) {
  console.error(`HTML não encontrado: ${htmlInput}`);
  process.exit(1);
}

// Substitui refs WebP por PNG equivalente (convertido no step anterior)
// e ajusta caminhos /_astro/ para o caminho absoluto no disco
let html = readFileSync(htmlInput, 'utf8');
const distPath = join(ROOT, 'dist');
html = html.replace(/src="(\/_astro\/[^"]+\.webp)"/gi, (_, p) => {
  const pngPath = join(distPath, p.replace('/_astro/', '/_astro/').replace(/\.webp$/, '.png'));
  return `src="${pngPath}"`;
});
html = html.replace(/src="(\/_astro\/[^"]+\.(jpg|jpeg|png|gif))"/gi, (_, p) => {
  return `src="${join(distPath, p.replace('/_astro/', '/_astro/'))}"`;
});

writeFileSync(htmlFixed, html);
console.log('✅ HTML preparado (imagens WebP → PNG)');
console.log('Gerando PDF com Pandoc + XeLaTeX...');

const distAstro = join(distPath, '_astro');
const cmd = [
  'pandoc',
  `"${htmlFixed}"`,
  '--pdf-engine=xelatex',
  `--template="${templateFile}"`,
  '-V lang=pt-BR',
  `--resource-path="${distPath}:${distAstro}"`,
  `-o "${outputFile}"`
].join(' ');

try {
  execSync(cmd, { stdio: 'inherit', cwd: ROOT });
  console.log(`✅ PDF gerado: ${outputFile}`);
} catch (err) {
  console.error('❌ Erro:', err.message);
  process.exit(1);
}
