# Güneş ve Ay'ın yörüngeleri: iyileştirme raporu

## Analiz
- Hook'taki "Kopernik'ten sonra Güneş bir süre evrenin merkezinde kıpırdamayan bir yıldız sanıldı" cümlesi yanlış yönlendiriyordu: Kopernik Güneş'i gezegen sisteminin merkezine koydu, evrenin merkezine değil.
- Gövde 1927 Oort'a kadar gidip "bugün ne biliyoruz" kısmını hiç açmıyordu; hız ve dönüş süresi eksikti.
- İtiraz cevapları kaynaksız ya da doğrulanmamış tarihsel iddialar içeriyordu ("Batlamyus'ta ayrı küreler", hadisin iki yorumu). Bunlar yeniden yazıldı.
- Eski "Müfessirler iki anlam aktarır" cümlesi kaynaksızdı; kaldırıldı.

## Düzeltilen olgular
- Eski hook: "Kopernik'ten sonra Güneş bir süre evrenin merkezinde kıpırdamayan bir yıldız sanıldı" → "Kopernik Güneş'i gezegenlerin merkezine koyduktan sonra Güneş uzun süre hareketsiz bir merkez sanıldı." (Kopernik görseli 1543 olarak zaten kaynaklı.)
- Eski hook: "saatte 800 bin kilometreyi aşan" → "saatte yaklaşık 828 bin kilometre". Kaynak: NASA StarChild, 828.000 km/sa.
- Eski: "Güneş'in bütün ... ayrı birer küresi vardı" (itiraz 1) → kaldırıldı; yerine Oort 1927 ile "hareketin gökadaya göre ölçülmesi" yazıldı.
- Eski: "Müfessirler bu ifade için iki anlam aktarır" (itiraz 2) → hadis Buhârî 3199 üzerinden yeniden yazıldı; hüküm yok.
- Eski: "yesbehûn fiili 'yüzerler' demektir; iki ayet önce de Güneş'in akıp gittiğini söyler" → iki ayet önce iddiası kaldırıldı (ayet 36:38'in meali doğrulanmadan kullanılmadı).

## Eklenen olgular
1. Güneş'in hızı ve gökada merkezi çevresindeki turu. Kaynak: NASA StarChild (2000), https://starchild.gsfc.nasa.gov/docs/StarChild/questions/question18.html (açıldı). Alıntılar: "We are moving at an average velocity of 828,000 km/hr." ve "it still takes us about 230 million years to make one complete orbit around the Milky Way!" Merkeze uzaklık: "about 28,000 light-years". Anahtar: `nasastarchild2000`.
2. Tur süresinin ikinci kaynakla teyidi: NRAO (16 Eylül 2015), https://public.nrao.edu/ask/orbital-period-of-the-sun-in-the-milky-way-galaxy/ (açıldı). Alıntılar: "the Sun takes about 226 million years to orbit the center of our Galaxy" ve "it orbits at a speed of about 230 km/s". Anahtar: `nrao2015`.
3. Hadis: Buhârî 3199 (Ebû Zerr rivayeti), İngilizce metin tohed.com üzerinden açıldı, https://en.tohed.com/hadith/bukhari/3199. Güneş'in Arş altında secde edip izin istediği anlatılıyor ve Yâsîn 36:38 ile bağlanıyor. Anahtar: `buhari3199`. Not: tohed.com ikincil bir hadis sitesi; Sahih Buhârî'nin asıl metni için ayrı bir kontrol önerilir.
- Kaynak sayısı: 3 yeni kaynak (`nasastarchild2000`, `nrao2015`, `buhari3199`).

## Denetim
`py -3 .oneri/denetle.py gunes-ve-ay-yorungeleri` → TAMAM

## Ekibe soru
1. Oort 1927 (ADS, `1927BAN.....3..275O`) sayfası 405 verdi; "gökadamızın döndüğü" iddiası mevcut kaynağa dayanıyor, açılıp doğrulanmadı.
2. Ayetin meali için (36:38, 36:39): AyetParca yalnız 36:40 ile kullanılıyor; frontmatter'da 38 ve 39 var. Diyanet meali doğrulanmadan eklenmedi. Bu iki ayetin de eklenip eklenmeyeceği karar gerektiriyor.
3. Hadis yorumu: Sahih Buhârî'nin asıl kaynağı ve "li-müstekarrin lehâ" ifadesinin tefsirleri ayrı bir kontrol gerektiriyor; mevcut metin hükümsüz tutuldu.
4. Kopernik 1543 ve Batlamyus haritası görsel açıklamalarından geliyor; bu iki tarih dışında yeni bir olgu eklenmedi.
