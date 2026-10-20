// Konular: ekranda yalnız bu sade adlar görünür. Yeni konu yalnız burada açılır (renk: tokens.css --konu-<anahtar>).
export const konular = {
  gokyuzu: { ad: 'Gökyüzü', raf: 'Gökyüzünden' },
  yeryuzu: { ad: 'Yeryüzü', raf: 'Yeryüzünden' },
  canlilar: { ad: 'Canlılar', raf: 'Canlılardan' },
  insan: { ad: 'İnsan', raf: 'İnsandan' },
  tarih: { ad: 'Tarih', raf: 'Tarihten' },
  gelecek: { ad: 'Gelecek haberleri', raf: 'Gelecekten haber' },
  dil: { ad: 'Dil ve anlatım', raf: 'Sözden' },
  sayilar: { ad: 'Sayılar', raf: 'Sayılardan' },
} as const;

export type Konu = keyof typeof konular;
