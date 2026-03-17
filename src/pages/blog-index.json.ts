import { getCollection } from 'astro:content';

export async function GET() {
  const posts = (await getCollection('blog'))
    .filter((p) => !p.data.draft)
    .sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());

  const data = posts.map((p) => ({
    id: p.id,
    title: p.data.title,
    description: p.data.description ?? '',
    pubDate: p.data.pubDate.toISOString(),
    tags: p.data.tags ?? [],
    placeLabel: p.data.placeLabel ?? null,
    heroImage: p.data.heroImage
      ? `/blog/images/${p.data.heroImage.src.split('/').pop()}`
      : null,
  }));

  return new Response(JSON.stringify(data), {
    headers: { 'Content-Type': 'application/json' },
  });
}
