// Konular: ekranda yalnız bu sade adlar görünür. Yeni konu yalnız burada açılır (renk: tokens.css --konu-<anahtar>).
// grup: ana sayfadaki sade tasnif; yakın konular tek başlıkta toplanır (mucizenin ilk konusu belirler).
export const konular = {
  gokyuzu: { ad: 'Gökyüzü', raf: 'Gökyüzünden', grup: 'Gökyüzü ve evren' },
  yeryuzu: { ad: 'Yeryüzü', raf: 'Yeryüzünden', grup: 'Yeryüzü ve canlılar' },
  canlilar: { ad: 'Canlılar', raf: 'Canlılardan', grup: 'Yeryüzü ve canlılar' },
  insan: { ad: 'İnsan', raf: 'İnsandan', grup: 'İnsan bedeni' },
  tarih: { ad: 'Tarih', raf: 'Tarihten', grup: 'Tarih ve gelecek haberleri' },
  gelecek: { ad: 'Gelecek haberleri', raf: 'Gelecekten haber', grup: 'Tarih ve gelecek haberleri' },
  dil: { ad: 'Dil ve anlatım', raf: 'Sözden', grup: "Kur'an'ın dili" },
  sayilar: { ad: 'Sayılar', raf: 'Sayılardan', grup: "Kur'an'ın dili" },
} as const;

export type Konu = keyof typeof konular;
