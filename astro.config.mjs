// @ts-check
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import mdx from '@astrojs/mdx';
import fastGlob from 'fast-glob';

// https://astro.build/config
export default defineConfig({
	integrations: [tailwind(), mdx(), fastGlob()],
});
