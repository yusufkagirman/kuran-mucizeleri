# İçerik iyileştirme yönergesi (her ajan önce bunu okur)

Site: Kur'an mucizelerini Türkçe, kaynaklı, kaydırmalı sunumlarla anlatan site. Kitle: gençler, çoğu telefondan.
Proje kökü: `C:\Users\getdi\OneDrive\Belgeler\Projext\Kuran-Mucizeleri`. Komutları proje kökünde çalıştır.

## Amaç
Her sunumu **içerik olarak** daha iyi yap: doğru, kaynaklı, sürükleyici, dikkat çekici. Konuyu hiç bilmeyen biri baştan sona
merakla okumalı ve sonunda mucizeyi kendi başına birine anlatabilmeli. Ana önerme basit kalır; araştırma iki iş içindir:
(1) metindeki her olguyu doğrulamak, yanlışı düzeltmek; (2) anlatıya kaynaklı, somut, canlı ayrıntı katmak.

## Mutlak kurallar (site sahibinin kuralları, çiğneme)
1. **Yorum ve hüküm yok.** Kendi yorumunu, çıkarımını katma; mucizenin "sağlam/zayıf" olduğuna karar verme. Yalnız kaynakta
   olanı, sitenin üslubunda yaz. Tefsir, i'caz eserleri, akademik yayın, ansiklopedi, müze/kurum sayfası.
2. **Her yeni olgu kaynaklı.** Eklediğin her yıl, isim, sayı, yer için web'de bir kaynak bul ve OKU (WebSearch + WebFetch).
   Bulamadığın bilgiyi yazma. Atıf: cümle sonuna `<Atif k="anahtar" />`. Yeni kaynağı ekle:
   `py -3 .oneri/kaynak-ekle.py anahtar '{"yazar":"...","yil":1957,"baslik":"...","yayin":"...","url":"https://..."}'`
   (doi varsa url yerine "doi"). Anahtar: küçük harf + rakam, ör. `britannica2024ari`. Frontmatter `kaynaklar: [...]` listesine de ekle.
3. **Kalıp söz yok.** "Kur'an X dedi", "tek kelimeyle", "1400 yıl önce haber verdi", "bilim doğruladı", kelime oyunu yok.
   Mucizenin anlattığı gerçeği ve hayreti doğrudan söyle (örnek: demirde "demir bu dünyaya ait değil, yıldızlardan geldi").
4. **Halkın anlamayacağı terim yok** (i'caz, beyânî, gaybî vb.). Bilimsel terimi kullanırsan aynı cümlede açıkla.
5. **Dokunma:** `<AyetParca .../>` satırları (Arapça + Diyanet meali) birebir kalır. Etkileşimli ve görsel bileşenler
   (`<Gorsel>`, `<Sahne />`, `<KovanTahmin />` vb.) silinmez; yerleri hikâyede mantıklı yere taşınabilir. Frontmatter'da
   `baslik, konu, sureAdi, vurgu, nuzul, kesif, vaat, durum, ornek` değişmez. `durum: taslak` kalır.
6. **Değiştirebileceklerin:** `hook` (giriş), `kart` (tek cümle, 140 karakteri geçmesin), `itirazlar` (soru ve cevapları
   netleştir, doğrula, `kaynak:` ekle; yeni sağlam itiraz eklenebilir), `kaynaklar` listesi, MDX gövdesindeki tüm anlatı
   paragrafları, `<Adim>` bölünmesi/yil/etiket, köprü soru ("Peki ...?") ve `<MeydanOkuma>` son sözü.

## Anlatı kalıbı (sırayla, tek parça akan hikâye)
1. **Hook (frontmatter):** 2-4 cümle. İlk paragraf tek çarpıcı cümle (girişte büyük yazılır). Mucizenin manasını söyler,
   merak uyandırır. Soru ya da şaşırtıcı bir gerçekle aç.
2. **O gün:** Ayetin indiği dönemde insanlar bu konuda ne biliyor/sanıyordu? Somut sahne (Mekke/Medine, dönemin genel kabulü).
   Uzak felsefi alıntı yığma; en fazla bir somut örnek, kaynaklı.
3. **Ayet:** `<AyetParca>` (değişmez). Hemen sonra ayetteki ifadenin ne anlattığını sade bir cümleyle açıkla.
4. **Uzun sessizlik:** Asırlarca nasıl anlaşıldı, neden tam anlaşılamadı (kaynaklı: bir müfessir ya da dönemin bilgisi).
5. **Keşif:** Ne zaman, kim, nasıl buldu. Kişiyi ve anı canlı anlat (1-3 kısa paragraf): neye bakıyordu, ne gördü.
   Kaynaklı. Mümkünse orijinal çalışmadan kısa alıntı için mevcut `<Alinti>` bileşeni kullanılabilir (bkz. diğer dosyalar).
6. **Bağlama:** Bugün bilinenle ayetin anlattığını yan yana koyan 1-2 cümle (hüküm değil, gözlem).
7. `<ZamanCizelgesi>` (varsa yerinde kalır), sonra `</Hikaye>`.
8. Hikaye dışında: köprü soru paragrafı ("Peki ama ...?"), `<Itirazlar liste={frontmatter.itirazlar} />`, `<MeydanOkuma>`.

## Üslup
- Belgesel anlatıcısı; okura dönünce "siz". Kısa cümleler. Her paragraf tek fikir, bir öncekine bağlanır.
- Her `<Adim>` kartı telefonda bir ekrana sığmalı: **en fazla ~70 kelime**. Uzun paragrafı iki adıma böl.
- Somut ol: sayılar, yerler, isimler, duyulabilir/görülebilir ayrıntılar. Sıfat yığma, abartma yok.
- Toplam gövde ~500-900 kelime; konunun yoğunluğuna göre. Dolgu yok, tekrar yok.

## Adım biçimi (MDX, aynen uy)
- Hikâye `<Hikaye veri={frontmatter}>` ... `</Hikaye>` içinde. Her öğe bir `<Adim>`:
  metin → `<Adim>` (ilk adım ve ayet adımına `yil={nuzul.yil}`, yıl veren paragrafa o yıl; MÖ negatif),
  ayet → `<Adim tur="genis" etiket="<Sure> suresi">`, görsel/etkileşim → `<Adim tur="sahne">`, ZamanCizelgesi → `<Adim tur="genis" yil={kesif.yil}>`.
- `etiket`: yalnız metindeki yıl/yer/sure adından ("1609 · İngiltere", "619 civarı · Mekke").
- Her `<Adim ...>`, `</Adim>`, `<Hikaye ...>`, `</Hikaye>` kendi satırında; önünde ve arkasında birer boş satır.
- Örnek tam dosya: `src/content/mucizeler/demir.mdx` (yapı için; içeriği de iyileştirilecek).

## Bitirince
1. `py -3 .oneri/denetle.py <slug>` → `TAMAM` olmalı. Hata varsa düzelt. (Build çalıştırma; paralel ajanlar var.)
2. `.oneri/<slug>-rapor.md` yaz:
   - **Analiz:** eski metnin zayıf yanları (3-6 madde: anlaşılırlık, sürükleyicilik, eksik/yanlış olgu).
   - **Düzeltilen olgular:** eski ifade → yeni ifade → kaynak URL.
   - **Eklenen olgular:** her biri için kaynak URL ve kaynaktan kısa alıntı (kelimesi kelimesine, 25 kelimeyi geçmesin).
   - **Ekibe soru:** kaynakta çelişki/şüphe olan yerler (hüküm vermeden).
Yalnız kendi dosyalarına dokun; başka mucizeye, bileşenlere, kaynaklar.json'a elle (betik dışında) dokunma.
