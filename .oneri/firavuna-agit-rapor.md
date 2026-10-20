# Firavuna ağıt: iyileştirme raporu

## Analiz (eski metnin zayıf yanları)
- Hook ve metin iki ayrı iddiayı karıştırıyordu: Mısır ağıtı ile ayet arasında "aynı kartın iki yüzü" benzerliği kaynaksız kuruluyordu. Okur bunu gerçek sanır.
- "Gök ve yer senin için ağlar, çünkü sen tanrılardan büyüksün" sözü kaynakta doğrulanamadı. Faulkner çevirisinde gök ve yer ağlamıyor; "gök senin ba'nı taşır, yer senin biçimini" satırı var.
- "Mısır yazısını okuyabilen tek bir insan yoktu" ve "Araplar bu ağıtı bilmiyordu" gibi ifadeler kaynaksızdı.
- Rosetta Taşı'nın bulunuş yeri ve kimin bulduğu eksikti; bu ayrıntılar anlatıyı canlandırır.
- Itiraz cevapları yorum ve kaynaksız iddialarla doluydu (Arapça deyim, "tersine çevirdi").

## Düzeltilen olgular
- "Mısırlılar ölen firavunlarını 'gök ve yer senin için ağlar' diye uğurlardı" -> kaldırıldı. Yerine: ağıtta gök ve yer ölen krala ruh ve biçim taşıyan imge olarak geçer. Kaynak: https://www.worldhistory.org/article/878/the-lamentations-of-isis-and-nephthys/
- "Bu ağıt ... yazılmıştı ve Duhân suresinin indiği gün bu yazıyı okuyabilen tek bir insan yoktu" -> "Bilinen son hiyeroglif yazıt MS 394'te Philae'de yazıldı; ardından yazıyı akıcı okuyan yazıcılar tükendi." Kaynak: https://en.wikipedia.org/wiki/Egyptian_hieroglyphs
- "Bremner-Rhind papirüsü MÖ 4. yüzyıl" itirazı -> Berlin Papirüsü 3008, Ptolemaios dönemi (MÖ 323-30). Kaynak: https://www.worldhistory.org/article/878/the-lamentations-of-isis-and-nephthys/
- Rosetta Taşı: "1799'da Mısır'da bulundu" -> "1799'da Rashid (Rosetta) yakınında, Fransız subayı Pierre-François Bouchard buldu; üç yazı: hiyeroglif, demotik, Yunanca." Kaynak: https://en.wikipedia.org/wiki/Rosetta_Stone
- Champollion: "1822'de çözdü" -> "27 Eylül 1822'de Académie'ye sundu; Dacier'ye mektup." Kaynak: https://en.wikipedia.org/wiki/Rosetta_Stone

## Eklenen olgular
- Rosetta Taşı'nın bulunuşu (1799, Bouchard, Rashid): https://en.wikipedia.org/wiki/Rosetta_Stone. Kısa alıntı: "found there in July 1799 by French army officer Pierre-François Bouchard"
- Son hiyeroglif yazıt MS 394, Philae; yazıcıların tükenmesi 5. yüzyıl: https://en.wikipedia.org/wiki/Egyptian_hieroglyphs. Alıntı: "the last known inscription is from Philae"
- Ağıtta Osiris'e ölen kral olarak seslenilmesi ve "Gök senin ba'nı taşır, yer senin biçimini": https://www.worldhistory.org/article/878/the-lamentations-of-isis-and-nephthys/. Alıntı: "Heaven has your ba, earth your form,"

## Ekibe soru
1. **Ayna bileşeni (kritik):** `src/components/firavuna-agit-Ayna.astro` içindeki "Gök ve yer senin için ağlar, çünkü sen tanrılardan büyüksün" alıntısı ve "Aynı söz, iki yüzü" açıklaması kaynakla doğrulanamadı. Bileşen bu görevde değiştirilmedi. Sayfa yayına alınmadan önce bu alıntı, doğrulanan satırla ("Gök senin ba'nı taşır, yer senin biçimini") değiştirilmeli ya da Ayna kaldırılmalı.
2. **Rosetta kaynağı:** British Museum ve Britannica sayfaları 403 verdi. Şu an kaynak Wikipedia; müze sayfası açılınca `rosettawiki` kaydı değiştirilmeli.
3. **Parkinson 1999 ve Champollion 1822** kaynak listesinde kaldı ama açılıp okunamadı; yalnız `champollion1822` (kesif alanı sabit olduğu için) tutuldu.
4. **Musa'nın firavunu** bu sayfada tartışılmıyor; hüküm verilmedi.

Doğrulama: `py -3 .oneri/denetle.py firavuna-agit` -> TAMAM.
