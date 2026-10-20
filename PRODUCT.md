# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users
Birincil: 15-25 yaş gençler, çoğunlukla telefondan, sosyal medyada paylaşılan bir mucize bağlantısıyla gelir ve konuyu ilk kez öğrenir. İkincil: imanını güçlendirmek isteyen Müslümanlar ve "gerçekten mucize mi?" diye kaynak arayan şüpheci okur. Masaüstü de desteklenir. Önce Türkçe.

## Product Purpose
Kur'an'daki sağlam mucizeleri, konuyu hiç bilmeyen birine kendi başına anlatan, kaynaklı ve etkileşimli sayfalarla tek yerde toplamak. Başarı: ziyaretçi bir sayfanın sonunda mucizenin ne olduğunu, neden o gün bilinemeyeceğini ve kaynağını anlar; sayfayı paylaşır.

## Positioning
İddia önce değil kaynak önce. Her mucize kendi alanına özgü bir etkileşimle (harita, ölçek, kesit, zaman sayacı vb.) hiç bilmeyene yaşatılarak anlatılır; itirazlar açıkça cevaplanır; yalnız sağlam mucizeler girer. Benzer siteler (kuranmucizeler.com, Harun Yahya) iddiayı kaynaktan önce koyar ve düz metin sunar.

## Operating Context
Her mucize bir MDX dosyası; metinleri Yusuf'un ekibi yazar, ajan yalnız sunuşu yapar ve yorum/çıkarım eklemez. Sayfa akışı: açılış, o gün bilinen, ayet anı (Arapça + meal), keşif, bir bakışta özet, itirazlar ("Peki ama..."), meydan okuma, kaynaklar. Sağlamlık kararını ve yayın onayını Yusuf verir.

## Capabilities and Constraints
- Astro 7 + MDX, statik; ücretsiz barındırma hedefi (Cloudflare Pages). Mucize başına özel etkileşim bileşeni.
- Ayet metni Arapça (Uthmani) + Türkçe meal (Diyanet esaslı); tilavet ileride.
- Arayüzde halkın anlamayacağı terim yok (i'caz, gaybî, beyânî, te'sir, teşrîî).
- Canlı (insan/hayvan) tasviri yok: geometri, nesne, kesit, harita, lisanslı fotoğraf.
- Lafza takılmayan dil: "Kur'an X dedi", "1400 yıl önce haber verdi" gibi kalıp sözler yok.
- Koyu ve açık tema, cihaz ayarı varsayılan (mevcut karar; görsel kimlik değişebilir).
- Undecided: alan adı, tilavet kaynağı izni, ekip/hoca onay süreci.

## Brand Commitments
Ad: "Kur'an Mucizeleri". Görsel kimlik sıfırdan (Yusuf, 2026-10-16: mevcut görünüm yapay zekâyı andırıyor, dört deneme yönü de reddedildi). Esnek ama tutarlı: her mucizenin anlatım biçimi farklı olabilir, marka kiti ve tipografi ortak.

## Evidence on Hand
17 mucize taslağı (`src/content/mucizeler/*.mdx`), birleşik kaynakça (`src/data/kaynaklar.json`), künyeli Wikimedia/NASA görselleri (`public/img/<slug>/`), Rum etkileşimli sunumu (`public/sunum/rum.html`). Metinler taslak, ekip/hoca onayı yok. Kullanıcı yorumu, istatistik, basın yok; uydurulmaz.

## Product Principles
1. Hiç bilmeyene anlatır gibi: her sahne tek fikir, açıklayan görsel.
2. Kaynak önce, iddia sonra; itiraz saklanmaz.
3. Mananın kendisi ve hayret, kelime oyunu değil.
4. Esnek sahne, sabit kabuk: mucizeler farklı anlatılır ama aynı aileden görünür.
5. Telefonda akıcı: yüklenme ve kaydırma pürüzsüz.

## Accessibility & Inclusion
Telefon öncelikli okunabilirlik; Arapça metin büyük ve net; azaltılmış hareket desteği; renk tek başına anlam taşımaz.

## Marka kiti (onaylı, bağlayıcı)

Tüm üretimler (site, sunum, paylaşım kartı, sosyal görsel) tek kiti kullanır: değerler `src/styles/tokens.css`, canlı örnek ve kurallar `public/sunum/marka-kiti.html`. Figtree + Amiri Quran, nötr gri + tek zümrüt vurgu, ayet vurgusu fosfor, her yerde 8 px köşe; degrade, cam bulanıklığı, büyük harfli üst etiket yok.
