const replacements = [
	['Rabugices a parte', 'Rabugices à parte'],
	['Desde o ano de 1950, quando, comecei', 'Desde o ano de 1950, quando comecei'],
	['Folguedos, Disciplina, trabalho e amigos.', 'Folguedos, disciplina, trabalho e amigos.'],
	['Aos 75 anos vejo que dessas três coisas, ainda resta alguns amigos.', 'Aos 75 anos vejo que dessas três coisas, ainda restam alguns amigos.'],
	['Assim, com eles convivo. na certeza', 'Assim, com eles convivo, na certeza'],
	['Aqui constitui família', 'Aqui constituí família'],
	['Sobe tudo isso', 'Sobre tudo isso'],
	['temas espaços', 'temas esparsos'],
	['PUBLICO OU NÃO PUBLIC0', 'PUBLICO OU NÃO PUBLICO'],
	['Ha uma pesquisa', 'Há uma pesquisa'],
	['Até memo', 'Até mesmo'],
	['último senso', 'último censo'],
	['dez anos atras', 'dez anos atrás'],
	['porem ninguém', 'porém ninguém'],
	['rescrevendo', 'reescrevendo'],
	['Taime is Money', 'Time is Money'],
];

function applyReplacements(value) {
	return replacements.reduce(
		(text, [from, to]) => text.replaceAll(from, to),
		value,
	);
}

function walk(node) {
	if (node?.type === 'text' && typeof node.value === 'string') {
		node.value = applyReplacements(node.value);
	}

	if (Array.isArray(node?.children)) {
		for (const child of node.children) walk(child);
	}
}

export default function eitaLasqueiraRevisao() {
	return (tree, file) => {
		const path = String(file?.path ?? '').replaceAll('\\', '/');
		if (!path.endsWith('src/content/eita-lasqueira/00-abertura.md')) return;
		walk(tree);
	};
}
