# sulb-teraib: içerik iyileştirme raporu

## Analiz
- Hook'taki "böbreklerin hizasında şekillenir" ve "bel ile kaburgalar arasında" ifadeleri kaynaksızdı; embriyoloji kaynağı ("mesonefros yanında") bunu tam öyle söylemiyor.
- Gövde, testis atardamarının ve sinirin "bugün de bel ile kaburgalar arasından çıktığını" iddia ediyordu. Bunu doğrulayan açık bir kaynak bulunamadı.
- Ayet kelimelerinin anlamı (sulb/terâib) tartışmalı ama metin bunu tek yorum gibi veriyordu.
- 1677 ve 1786 adımlarında "ilk kez görüldü" ve "böbrek hizasında" gibi iddialar kesin dil kullanıyordu.
- Kart ve itiraz 1 cevabı, testis ve üretim yerini karıştırıyordu.

## Düzeltilen olgular
- "Testisler anne karnında böbrek hizasında şekillenir" → "karın arka duvarında, mesonefros yanındaki bir kabartıdan gelişir; doğuma doğru aşağı iner." Kaynak: https://radiopaedia.org/articles/testicular-descent?lang=us (alıntı: "derived from the gonadal ridge medial to the mesonephric ridge")
- "Suyun içindeki canlı hücreler 1677'de ilk kez görüldü" → "1677'de Leeuwenhoek, mikroskopuyla insan meninde ... spermleri gördü ve bildirdi." Öncelik tartışması ekibe soruya bırakıldı.
- "Bugün de geldikleri yerden, bel ile kaburgalar arasından çıkar" (atardamar ve sinir) → kaldırıldı. Bkz. Ekibe soru 1.
- Itiraz 1 cevabı: "Testisler bel ile kaburgalar arasında oluşur" → "Ayet suyun nereden çıkıp atıldığını anlatır; testislerin gelişimi karın arka duvarında başlar."
- Kart: "anne karnında bel ile kaburgalar arasında şekillenir" → "anne karnında karın arka duvarında oluşur, sonra aşağı iner."
- Sulb/terâib adımı: tek çeviri yerine tartışmalı okumalar yazıldı (Al-Balushi 2021).

## Eklenen olgular
- 1677, Leeuwenhoek mikroskopla spermi gördü ve bildirdi. Kaynak: `leeuwenhoek1677` (kaynaklar.json'da DOI var). Bu kaynak açılmadı; atıf anahtarı eski listeden. Yeni ayrıntı (Johan Ham) metne alınmadı.
- Sulb/terâib tartışması: Al-Balushi, R., QURANICA, 13(2), 2021. https://ijps.um.edu.my/index.php/quranica/article/view/34307 . Alıntı: "ʾaṣ-ṣulb may refer to the 'tailbone', and ʾat-tarāʾib may be interpreted to refer to 'the rest of the human body'."
- Testis gelişimi: Manickam, A. ve ark., Radiopaedia, "Testicular development and descent". https://radiopaedia.org/articles/testicular-descent?lang=us . Alıntı: "derived from the gonadal ridge medial to the mesonephric ridge"; "the gubernaculum ... to the lower abdominal wall in the inguinal region".
- Hunter 1786: kitap başlığı ve testis inişi içeriği, kütüphane kaydından (arama sonucu, sayfa açılmadı). Metinde yalnızca "1786'da yayımlanan kitabında inişi anlattı" yazıldı.

## Ekibe soru
1. **Atardamar ve sinir iddiası.** Sayfa açılamadı (PMC/StatPearls 403 ya da yönlendirme). Arama özetinde testis atardamarının aortadan, böbrek atardamarının hemen altından (yaklaşık L2) çıktığı yazıyordu; bu metinde "bel ile kaburgalar arası" ile örtüşmüyor. Bu cümleyi ya da "bel" çevirisini kaynakla yeniden değerlendirmek gerekir.
2. **kesif.olay metni** ("testislerin böbrek hizasında geliştiğini ... tarif etti") sabit alan olduğu için dokunulmadı. Hunter'in bu ifadeyi kullandığı doğrulanamadı; alan değişikliğine izin verilirse düzeltilmeli.
3. **Hunter kesifi.** Kütüphane kaydı testis inişini gösteriyor, böbrek ilişkisi değil; "kesif" adımı bu yüzden kaynaklı değil.
4. **Leeuwenhoek öncelik.** "İlk kez" gözlemi tartışmalı: 1677'de medikal öğrenci Johan Ham'in ilk dikkatini çektiği, Hartsoeker'in sonradan öncelik iddia ettiği aktarılıyor (lensonleeuwenhoek.net arama özeti; sayfa açılmadı). Metin "ilk" demiyor; ekip istediğinde Ham atfı eklenebilir.
5. **Gorsel (Gray 1918).** Yeni ifade yok; bileşen olduğu gibi kaldı.
6. **Tefsir "kadının göğsü" okuması.** Açılmış kaynak yok; metne alınmadı.

Denetim: `py -3 .oneri/denetle.py sulb-teraib` -> TAMAM
