// Alt yolda (GitHub Pages) yayınlarken koda gömülü "/img/..." gibi kök yollarına base ekler.
import { readdirSync, readFileSync, writeFileSync, statSync } from 'node:fs';
import { join } from 'node:path';

const taban = (process.env.TABAN || '').replace(/\/$/, '');
if (!taban) process.exit(0);
const re = /(["'`(=])\/(img|veri|sunum|mucize|hakkinda)(?=[/."'`)#?]|$)/g;
let n = 0;
(function gez(d) {
  for (const f of readdirSync(d)) {
    const p = join(d, f);
    if (statSync(p).isDirectory()) gez(p);
    else if (/\.(html|js|css|json|svg)$/.test(f)) {
      const s = readFileSync(p, 'utf8');
      const t = s.replace(re, (_, q, k) => `${q}${taban}/${k}`).replaceAll('href="/"', `href="${taban}/"`);
      if (t !== s) { writeFileSync(p, t); n++; }
    }
  }
})('dist');
console.log(`taban eklendi: ${n} dosya`);
