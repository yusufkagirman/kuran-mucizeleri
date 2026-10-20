# Göğün genişlemesi: iyileştirme raporu

## Analiz
- Eski metin iki tekrar taşıyordu: "gök durmuyor, evren genişliyor" fikri hem hook'ta hem sahnede tekrar ediyordu.
- İtiraz cevapları kaynaksızdı. "1900'lere kadar genişletmeye gücümüz yeter diye çevrildi" iddiası ve Taberî / İbn Kesîr'den aktarılan tefsir cümleleri doğrulanamadı; Taberî ve İbn Kesîr sayfalarının metni açılamadı.
- Eski "mecazdır, akışla uyuşmaz" itirazı hüküm içeriyordu (yorum yasağı).
- "Bu dönemde gök kubbe sanılıyordu" çerçevesi genel bir tarihsel iddia; kaynaksız bırakıldı (aşağıda soru).
- Telefonda okunabilir ama "Bugün" tarafı zayıftı: 2004 Hubble görüntüsüne dair somut ayrıntı yoktu.

## Düzeltilen olgular
- Eski: "Bu ayet 1900'lere kadar 'genişletmeye gücümüz yeter' diye çevriliyordu" → kaldırıldı (doğrulanamadı).
- Eski: "Taberî ... İbn Zeyd'in 'onu genişletti' dediğini aktarır; İbn Kesîr 'göğün etrafını genişlettik' der" → kaldırıldı. Kaynak: doğrulanamadı; Taberî metni çevrimiçi açılmadı, sorularlaislamiyet.com sayfası bu iki ismi anmıyor.
- Eski: "Ayetin 'genişleticiyiz' ifadesi mecaz olabilir mi?" itirazı, hüküm içerdiği için yeniden yazıldı.
- Eski: "Bilim de uzun süre evreni durağan sandı" → "evrenin değişmediğini düşündü" (anlam aynı, sadeleştirildi).
- Hook ve kart değişmedi (hook'ta kaynaksız iddia yok).

## Eklenen olgular
1. Hubble Ultra Deep Field, 2004: yaklaşık 10.000 gökada, görünür ışıkla çekilmiş en derin görüntü. Kaynak: ESA/Hubble, heic0406, https://esahubble.org/images/heic0406a/ (açıldı). Alıntı: "This view of nearly 10,000 galaxies is the deepest visible-light image of the cosmos." Yayın tarihi: 9 Mart 2004. Anahtar: `esa2004hudf`.
- Galeri açıklamasındaki "neredeyse hepsi birer gökada" ifadesi "yaklaşık 10.000 gökada" ile değiştirildi.
- Kaynak sayısı: 1 yeni kaynak (`esa2004hudf`).

## Denetim
`py -3 .oneri/denetle.py gogun-genislemesi` → TAMAM

## Ekibe soru
1. Hubble 1929 (PNAS, doi 10.1073/pnas.15.3.168) sayfası 403 verdi; "uzaklaştıkça daha hızlı kaçtı" iddiası mevcut kaynağa dayanıyor, açılıp doğrulanmadı. Erişilebilir bir kopya ile kontrol edilmeli.
2. Lemaître 1927 kaynağı açılamadı; "1927'de evrenin genişleyebileceğini hesapladı" iddiası kontrol edilmedi.
3. "Ayetin indiği yıllarda gök başın üstünde duran, değişmeyen bir kubbe olarak bilinirdi" cümlesi (612 civarı) kaynaksız. Bir kaynak bulunmazsa cümle yumuşatılmalı.
4. `kaynaklar.json` içindeki `taberi` ve `ibnkesir` kayıtları artık bu dosyada kullanılmıyor; "İbn Zeyd" yorum kaydı doğrulanmadan bu kayıtlara güvenilmemeli.
