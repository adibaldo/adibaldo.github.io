import { getCollection } from 'astro:content';
import satori from 'satori';
import { Resvg } from '@resvg/resvg-js';
import { readFile } from 'node:fs/promises';

export const prerender = true;

const OG_WIDTH = 1200;
const OG_HEIGHT = 630;

async function getFonts() {
	const regular = await readFile(new URL('../../../public/fonts/atkinson-regular.woff', import.meta.url));
	const bold = await readFile(new URL('../../../public/fonts/atkinson-bold.woff', import.meta.url));

	return [
		{ name: 'Atkinson', data: regular, weight: 400, style: 'normal' },
		{ name: 'Atkinson', data: bold, weight: 700, style: 'normal' },
	] as const;
}

export async function getStaticPaths() {
	const posts = await getCollection('blog');
	return posts
		.filter((p) => !p.data.draft)
		.map((post) => ({
			params: { slug: post.id },
			props: {
				title: post.data.title,
				description: post.data.description,
				tags: post.data.tags ?? [],
				placeLabel: post.data.placeLabel ?? '',
			},
		}));
}

type Props = {
	title: string;
	description: string;
	tags: string[];
	placeLabel: string;
};

export async function GET({ props }: { props: Props }) {
	const { title, description, tags, placeLabel } = props;
	const fonts = await getFonts();
	const logoData = await readFile(new URL('../../../public/favicon-adi.png', import.meta.url));
	const logoBase64 = `data:image/png;base64,${logoData.toString('base64')}`;

	const tag = tags?.[0] || '';
	const meta = [tag, placeLabel].filter(Boolean).join(' • ');

	const svg = await satori(
		{
			type: 'div',
			props: {
				style: {
					width: `${OG_WIDTH}px`,
					height: `${OG_HEIGHT}px`,
					display: 'flex',
					flexDirection: 'column',
					justifyContent: 'space-between',
					padding: '80px',
					background: 'linear-gradient(180deg, #F5C77E 0%, #FDF0E2 100%)',
					color: '#1A1A1A',
				},
				children: [
					{
						type: 'div',
						props: {
							style: {
								display: 'flex',
								flexDirection: 'column',
								gap: '20px',
							},
							children: [
								{
									type: 'div',
									props: {
										style: {
											display: 'flex',
											fontFamily: 'Atkinson',
											fontSize: '24px',
											fontWeight: 700,
											color: '#6B5B4F',
											letterSpacing: '1px',
											textTransform: 'uppercase',
										},
										children: ['Alfarrábios do Adi'],
									},
								},
								{
									type: 'div',
									props: {
										style: {
											display: 'flex',
											fontFamily: 'Atkinson',
											fontSize: '72px',
											fontWeight: 700,
											lineHeight: 1.1,
											maxWidth: '900px',
										},
										children: [title],
									},
								},
								{
									type: 'div',
									props: {
										style: {
											display: 'flex',
											fontFamily: 'Atkinson',
											fontSize: '32px',
											fontWeight: 400,
											color: '#3A2F28',
											maxWidth: '850px',
											lineHeight: 1.4,
										},
										children: [description],
									},
								},
							],
						},
					},
					{
						type: 'div',
						props: {
							style: {
								display: 'flex',
								justifyContent: 'space-between',
								alignItems: 'flex-end',
							},
							children: [
								{
									type: 'div',
									props: {
										style: {
											display: 'flex',
											flexDirection: 'column',
											gap: '8px',
										},
										children: [
											meta ? {
												type: 'div',
												props: {
													style: {
														display: 'flex',
														fontFamily: 'Atkinson',
														fontSize: '20px',
														fontWeight: 700,
														color: '#D4874E',
													},
													children: [meta],
												},
											} : null,
											{
												type: 'div',
												props: {
													style: {
														display: 'flex',
														fontFamily: 'Atkinson',
														fontSize: '18px',
														color: '#6B5B4F',
													},
													children: ['adibaldo.github.io'],
												},
											},
										],
									},
								},
								{
									type: 'img',
									props: {
										src: logoBase64,
										style: {
											width: '120px',
											height: '120px',
											borderRadius: '999px',
											border: '2px solid #D4874E',
										},
									},
								},
							],
						},
					},
				],
			},
		} as any,
		{
			width: OG_WIDTH,
			height: OG_HEIGHT,
			fonts: fonts.map((f) => ({
				name: f.name,
				data: f.data,
				weight: f.weight,
				style: f.style,
			})),
		},
	);

	const resvg = new Resvg(svg, { fitTo: { mode: 'width', value: OG_WIDTH } });
	const pngData = resvg.render().asPng();

	return new Response(pngData, {
		headers: {
			'Content-Type': 'image/png',
			'Cache-Control': 'public, max-age=31536000, immutable',
		},
	});
}
