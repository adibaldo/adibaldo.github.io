#!/usr/bin/env python3
"""Importação inicial do manuscrito (Pandoc + Pillow).

Uso, na raiz do repositório:
  python3 scripts/import-eita-lasqueira.py /caminho/manuscrito.docx

Não executar novamente sobre partes já revisadas: substitui os Markdown.
Não faz revisão de redação. Os marcadores de parte são substituídos pelos
títulos aprovados; o sumário paginado do Word é substituído pelo sumário web.
"""
import argparse
import copy
import hashlib
import html
import json
from pathlib import Path
import re
import subprocess
from collections import Counter
from PIL import Image

PARTS = [
    ('00-abertura', 'Abertura', 'Abertura', None, None),
    ('01-primeira-parte', 'PRIMEIRA PARTE', 'MARCO ZERO', 'PRIMEIRA PARTE.', 'MARCO ZERO'),
    ('02-segunda-parte', 'SEGUNDA PARTE', 'O CAMINHÃOZINHO DE MUDANÇA', 'SEGUNDA PARTE', 'O CAMINHÃOZINHO DE MUDANÇA'),
    ('03-terceira-parte', 'TERCEIRA PARTE', 'ENFRENTANDO A AMAZÔNIA', 'TERCEIRA PARTE', 'ENFENTANDO A ANAZONIA'),
    ('04-quarta-parte', 'QUARTA PARTE', 'DESCOBRINDO O BRASIL', 'QUARTA PARTE', 'DESCOBRINDO O BRASIL'),
    ('05-quinta-parte', 'QUINTA PARTE', 'VOVÔ FRANQUELIM / UM GAUDÉRIO FORA DO TEMPO', 'QUINTA PARTE', 'Vovó Franquelim'),
    ('06-sexta-parte', 'SEXTA PARTE', 'OUTROS CAUSOS', 'SEXTA PARTE', 'OUTROS CAUSOS.'),
    ('07-setima-parte', 'SÉTIMA PARTE', 'FALANDO DE MIM', 'SETIMA PARTE', 'FALANDO DE MIM.'),
    ('08-oitava-parte', 'OITAVA PARTE', 'COVIDE E MUITO MAIS', 'NONA PARTE.', 'COVIDE E MUITO MAIS.'),
    ('09-epilogo', 'Epílogo', 'EPÍLOGO', 'EPILOGO', None),
]

# Descrições visuais conferidas nas imagens extraídas, sem identificar retratados.
ALTS = [
    'Capa de Eita Lasqueira, com um cavalo dando um coice e espalhando lascas de madeira.',
    'Ilustração de um homem ajoelhado em oração.',
    'Fotografia de um médico sentado, usando jaleco e estetoscópio.',
    'Retrato de uma mulher com traje de formatura.',
    'Ilustração de uma arca de madeira, pessoas e animais.',
    'Fotografia de uma roda de pedra ao lado de um tronco.',
    'Ilustração de uma multidão diante de uma cidade antiga.',
    'Ilustração de um jovem com uma funda diante de um guerreiro de armadura.',
    'Ilustração de um homem com vestes antigas diante de uma mesa com livros.',
    'Ilustração de dois homens conversando diante de inscrições e figuras geométricas.',
    'Ilustração de soldados e moradores em uma vila.',
    'Ilustração de soldados junto a um homem deitado sobre uma cruz.',
    'Ilustração de um homem escrevendo à luz de uma vela, em uma caverna.',
    'Ilustração de crianças brincando ao redor de uma árvore.',
    'Ilustração de um caminhão antigo carregado com a mudança de uma família.',
    'Ilustração de uma estrada de terra entre pinheiros.',
    'Ilustração de pessoas dançando em um salão.',
    'Ilustração de homens conversando em uma bodega.',
    'Ilustração de um homem armado em uma bodega, diante de outras pessoas.',
    'Ilustração de uma confusão entre pessoas em um velório.',
    'Ilustração de um professor e alunos em uma sala de aula.',
    'Ilustração de um menino com expressão triste.',
    'Ilustração de um alfaiate trabalhando em uma máquina de costura.',
    'Ilustração de um vendedor de jornais junto a uma banca na cidade.',
    'Ilustração de uma manifestação em uma rua movimentada.',
    'Imagem de um avião antigo com a inscrição TABA.',
    'Ilustração de uma rua de terra com casas e comércios.',
    'Ilustração de uma família diante de casas de madeira.',
    'Ilustração de uma casa rústica cercada pela vegetação.',
    'Ilustração de homens trabalhando em um escritório com livros e papéis.',
    'Ilustração de uma reunião em uma sala com mesa central.',
    'Ilustração de um avião em uma pista de terra, junto à mata.',
    'Ilustração de um ancião deitado em uma cama conversando com um homem sentado.',
    'Ilustração de um cavaleiro de chapéu e pala em uma paisagem rural.',
    'Ilustração de dois aviões antigos voando sobre uma paisagem rural.',
    'Ilustração de homens montados em cavalos.',
    'Ilustração de uma bolsa de couro com fivelas.',
    'Ilustração de homens descansando à sombra de uma árvore, com uma mula e um pássaro.',
    'Ilustração de homens sentados sob uma jaqueira carregada de frutos.',
    'Ilustração de pessoas aguardando em um consultório.',
    'Ilustração do interior de uma caverna com objetos e adornos.',
    'Ilustração de um homem sentado junto a uma mesa em uma casa rústica.',
    'Ilustração de um gato comendo sobre uma mesa posta.',
    'Ilustração de um cavalo junto a uma carroça carregada.',
    'Ilustração de embarcações antigas no mar.',
    'Ilustração de um homem junto a uma cachoeira.',
    'Ilustração de uma canoa em um rio cercado por mata.',
    'Ilustração de uma cidade à margem de um rio.',
    'Ilustração de dois homens conversando na mata.',
    'Imagem de uma manifestação política em uma avenida.',
    'Ilustração de um homem de máscara diante da porta de um comércio fechado.',
    'Ilustração de homens descansando junto a uma casa rural.',
    'Ilustração de um homem com uma placa pedindo trabalho.',
    'Ilustração de um homem com trajes antigos e edifícios ao fundo.',
    'Ilustração de uma trilha estreita entre árvores e vegetação.',
    'Ilustração de uma família viajando em uma carroça carregada.',
    'Ilustração de uma carroça carregada em um caminho acidentado.',
    'Fotografia de um caminhão antigo em uma estrada de terra.',
    'Ilustração de uma cobra sobre um galho na mata.',
]


def words(node):
    """Texto autoral apenas, sem atributos, URLs e textos alternativos."""
    if isinstance(node, list):
        return ''.join(words(x) for x in node)
    if not isinstance(node, dict):
        return ''
    kind = node.get('t')
    if kind == 'Str':
        return node['c']
    if kind in ('Space', 'SoftBreak', 'LineBreak'):
        return ' '
    if kind in ('Image', 'RawInline', 'RawBlock'):
        return ''
    return words(node.get('c', [])) + ('\n' if kind in ('Para', 'Plain', 'Header', 'BlockQuote') else '')


def images(node):
    if isinstance(node, list):
        return [image for x in node for image in images(x)]
    if isinstance(node, dict):
        if node.get('t') == 'Image':
            return [node['c'][2][0]]
        return images(node.get('c', []))
    return []


def adapt(node):
    if isinstance(node, list):
        return [adapt(x) for x in node]
    if not isinstance(node, dict):
        return node
    if node.get('t') == 'Image':
        attrs, _, target = node['c']
        path = Path(target[0])
        number = int(re.search(r'image(\d+)', path.name).group(1))
        with Image.open(path) as im:
            width, height = im.size
        original_width = dict(attrs[2]).get('width', '')
        # Respeita a largura diagramada no Word, limitada à tela e à resolução.
        display_width = min(width, float(original_width[:-2]) * 96) if original_width.endswith('in') else width
        src = '/' + path.as_posix().removeprefix('public/')
        tag = (f'<img src="{src}" alt="{html.escape(ALTS[number-1], quote=True)}" '
               f'width="{width}" height="{height}" style="width: {display_width:.2f}px; max-width: 100%;" '
               'loading="lazy" decoding="async" />')
        return {'t': 'RawInline', 'c': ['html', tag]}
    result = {**node, 'c': adapt(node['c'])} if 'c' in node else node
    if result.get('t') == 'Header':
        # Um único h1 (título da parte) fica a cargo do layout.
        result['c'][0] = 2
        result['c'][1] = ['', [], []]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manuscript', type=Path)
    args = parser.parse_args()
    source = args.manuscript.resolve()
    raw = subprocess.check_output(['pandoc', str(source), '-f', 'docx', '-t', 'json', '--extract-media=public/eita-lasqueira'])
    document = json.loads(raw)
    blocks = document['blocks']
    opening = next(i for i,b in enumerate(blocks) if b['t'] == 'Header' and words(b).strip() == 'INTROITO OU PROLEGÔMENOS')
    starts = {0: opening}
    for order, part in enumerate(PARTS[1:], 1):
        candidates = [i for i,b in enumerate(blocks) if i >= opening and words(b).strip() == part[3]]
        assert len(candidates) == 1, (part[3], candidates)
        starts[order] = candidates[0]
    physical = sorted(starts.values()) + [len(blocks)]
    output = Path('src/content/eita-lasqueira')
    output.mkdir(parents=True, exist_ok=True)
    log = {'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(), 'parts': []}
    accounted = []
    removed = []
    image_refs = []
    for order, (slug, label, title, marker, subtitle) in enumerate(PARTS):
        start = starts[order]
        end = physical[physical.index(start)+1]
        accounted.extend(range(start,end))
        selected = copy.deepcopy(blocks[start:end])
        if marker:
            removed.append(words(selected.pop(0)).strip())
        if subtitle:
            assert words(selected[0]).strip() == subtitle
            removed.append(words(selected.pop(0)).strip())
        if order == 5:
            assert words(selected[0]).strip() == 'Um Gauderio Fora do Tempo'
            removed.append(words(selected.pop(0)).strip())
        # Vazios de diagramação do Word não são títulos no site.
        selected = [b for b in selected if b['t'] != 'Header' or words(b).strip()]
        before = words(selected)
        refs = images(selected)
        image_refs.extend(refs)
        transformed = adapt(selected)
        assert words(transformed) == before, f'Texto alterado em {slug}'
        converted = {**document, 'blocks': transformed}
        md = subprocess.check_output(['pandoc', '-f', 'json', '-t', 'gfm', '--wrap=none'], input=json.dumps(converted).encode()).decode()
        # Quebra de linha explícita, sem depender de espaços invisíveis no Git.
        md = '\n'.join(line.rstrip() if line.startswith('#') else (line.rstrip() + '<br />' if line.endswith('  ') else line) for line in md.split('\n'))
        frontmatter = '\n'.join(['---', f'title: {json.dumps(title,ensure_ascii=False)}', f'partLabel: {json.dumps(label,ensure_ascii=False)}', f'order: {order}', '---', ''])
        (output / f'{slug}.md').write_text(frontmatter+'\n'+md, encoding='utf-8')
        log['parts'].append({'file': f'{slug}.md', 'source_block_start': start, 'source_block_end_exclusive': end, 'words': len(before.split()), 'image_occurrences': len(refs), 'text_preserved': True})
    assert sorted(accounted) == list(range(opening,len(blocks)))
    assert len(accounted) == len(set(accounted))
    # A capa é exibida na página inicial. Nenhuma gravura do corpo é retirada.
    assert Counter(image_refs) == Counter(images(blocks[opening:]))
    log['replaced_part_markers'] = removed
    log['body_coverage'] = 'Todos os blocos após o sumário do Word, exatamente uma vez.'
    log['cover'] = 'public/eita-lasqueira/media/image1.png'
    log['unique_body_images'] = len(set(image_refs))
    log['body_image_occurrences'] = len(image_refs)
    Path('docs/eita-lasqueira-importacao.json').write_text(json.dumps(log, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(log,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
