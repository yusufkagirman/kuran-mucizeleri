import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

export default defineConfig({
  integrations: [mdx()],
  // GitHub Pages alt yolu: yalnız yayında (TABAN), yerelde '/'
  site: process.env.TABAN ? 'https://yusufkagirman.github.io' : undefined,
  base: process.env.TABAN || '/',
  // Rum'un kendi haritalı sunumu var
  redirects: { '/mucize/rum': '/sunum/rum.html' },
  server: { port: Number(process.env.PORT) || 4321 },
});
