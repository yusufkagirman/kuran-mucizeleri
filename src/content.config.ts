import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';
import { konular } from './taksonomi';
import kaynaklar from './data/kaynaklar.json';

// Anlatı kuralı: vault 10-Projeler/Kuran-Mucizeleri/Anlati-Kurali.md. Hikâye MDX gövdesinde, burası altyapı verisi.
const anahtar = z.string().refine((k) => k in kaynaklar, { message: 'kaynaklar.json içinde yok' });

const mucizeler = defineCollection({
  loader: glob({ pattern: '**/*.mdx', base: './src/content/mucizeler' }),
  schema: z
    .object({
      baslik: z.string(),
      hook: z.string(), // giriş: konuyu bilmeyeni yakalayan çarpıcı 2-4 cümle; paragraflar boş satırla
      kart: z.string(), // paylaşım kartındaki tek cümle
      konu: z.array(z.enum(Object.keys(konular) as [string, ...string[]])).min(1),
      sureAdi: z.string(),
      ayetler: z.array(z.object({ sure: z.number().int().min(1).max(114), ayet: z.number().int().min(1) })).min(1),
      vurgu: z.string().optional(), // ayette vurgulanacak kelime (Uthmani yazımıyla)
      nuzul: z.object({ donem: z.string(), yil: z.number() }),
      kesif: z.object({ yil: z.number(), olay: z.string(), kaynak: anahtar.optional() }),
      vaat: z.object({ enAz: z.number(), enCok: z.number(), ifade: z.string() }).optional(), // gelecek haberlerinde ayetteki süre
      itirazlar: z.array(z.object({ itiraz: z.string(), cevap: z.string(), kaynak: anahtar.optional() })).default([]),
      kaynaklar: z.array(anahtar).default([]),
      ornek: z.boolean().default(false), // prototip için yer tutucu veri
      durum: z.enum(['taslak', 'yayinda']),
      // Yalnız Yusuf yazar.
      karar: z.object({ hukum: z.enum(['girer', 'girmez']), tarih: z.coerce.date() }).optional(),
    })
    .refine((d) => d.durum !== 'yayinda' || d.karar?.hukum === 'girer', {
      message: "Yayına almak için Yusuf'un 'girer' kararı gerekli",
      path: ['karar'],
    }),
});

export const collections = { mucizeler };
