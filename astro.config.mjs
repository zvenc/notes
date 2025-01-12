// @ts-check
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import mdx from '@astrojs/mdx';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import remarkGfm from 'remark-gfm';

export default defineConfig({
	integrations: [tailwind(), mdx()],
	markdown: {
		remarkPlugins: [remarkMath, remarkGfm],
		rehypePlugins: [rehypeKatex],
	},
	site: 'https://zvenc.github.io',
	base: '/',
});
