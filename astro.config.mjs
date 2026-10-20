import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

export default defineConfig({
  integrations: [mdx()],
  // Rum'un kendi haritalı sunumu var
  redirects: { '/mucize/rum': '/sunum/rum.html' },
  server: { port: Number(process.env.PORT) || 4321 },
});
