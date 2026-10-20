# İki denizin karışmaması: iyileştirme raporu

## Analiz (eski metnin zayıf yanları)
- Açılış ("suyun suya karıştığı sanılırdı") 614 yılındaki genel kabulü kaynaksız anlatıyordu; kaynak bulunamadığı için çıkarıldı.
- "Görünmez bir sınır" ifadesi ayette yok; kart ve hook ayetin "berzah" (engel) sözüne sadık hale getirildi.
- Gövde, 1961 keşfini Cebelitarık akıntılarıymış gibi anlatıyordu; bu iddia doğrulanamadı (aşağıda ekibe soru).
- Itiraz 2 ("nehir ağızlarında dalgıçlar görürdü") kaynaksızdı; yerine tefsir kaynaklı bir itiraz (hangi iki deniz?) kondu.
- Olgusal ayrıntı azdı: tuzluluk, yoğunluk ve akış yönü somut sayılarla verilmedi.

## Düzeltilen olgular
- "Ayetin indiği yıllarda iki su buluştuğunda tek su olduğu düşünülürdü" → kaldırıldı (kaynaksız). Yerine: Rahmân 55:20 ve İbn Kesîr'in okuması.
- "Ayetteki berzah 'iki şey arasındaki engel' demektir; müfessirler kara parçası dedi, sınırın nasıl oluştuğunu bilen yoktu" → İbn Kesîr'in kara parçası okuması, "sınırın nasıl oluştuğunu bilen yoktu" ifadesi kaldırıldı (kaynaksız hüküm).
- "Wüst 1961'de Cebelitarık'ta iki akıntı halinde yer değiştirdiğini gösterdi" → gövdede yalnızca "Akdeniz'in dikey dolaşımını yaklaşık 600 istasyonun verisiyle inceleyen çalışma" olarak yazıldı. Kaynak: https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/JZ066i010p03261 (arama özetinde görüldü; tam metin 403).
- "Denizler sonunda karışır; sular zamanla geçer" itirazı: "Cebelitarık'ta iki su kütlesi geçiş tabakasıyla ayrı akar" cevabına çevrildi. Kaynak: Sanchez-Román ve ark. (2018).
- Kart ve hook "tuzlu ve tatlı sular" ile "Cebelitarık Akdeniz/Atlantik" ayrımını karıştırmıyor; ikisi itirazlarda ayrı tutuldu.

## Eklenen olgular
1. Atlantik yüzey suyu tuzluluğu ≈36,2 psu; Akdeniz çıkış suyu ≈38,4 psu, alt katmanda Atlantik'e doğru akar, yaklaşık 0,8 Sv. Kaynak: Sánchez-Román, A., Jordà, G., Sannino, G., Gomis, D. (2018), Ocean Science 14, 1547–1566, https://os.copernicus.org/articles/14/1547/2018/ . Alıntı: "of cold and salty (S_M≈38.4) MOW flows towards the Atlantic Ocean in the lower layer" (sayfa özetinden, kısaltılmış).
2. Yoğunluk farkı yaklaşık 1,1–1,2 kg/m³ (Cádiz ve Alboran kesitleri). Kaynak: aynı makale. Alıntı: "The density difference between layers is about −1.18 kg m⁻³ at the Gulf of Cádiz section and about −1.09 kg m⁻³ at the Alboran section" (özetten).
3. Akdeniz'de buharlaşmanın yağış ve nehir girdisinden fazla olması, suyun kaybı ve tuzun kalması. Kaynak: https://en.wikipedia.org/wiki/Strait_of_Gibraltar (ansiklopedi, ikincil; bkz. ekibe soru).
4. İbn Kesîr: iki deniz tatlı ve tuzlu su; tatlı suyun kaynağı akan nehirler; aralarındaki engel kara parçası. Kaynak: İbn Kesîr, Rahmân 55:19–20 tefsiri, https://quran.com/en/55:20/tafsirs/en-tafisr-ibn-kathir (İngilizce kısaltılmış metin). Alıntı: "a barrier of land between these two types of waters, so that they do not transgress upon each other" (kısaltılmış; tam Tefsîr'e erişilemedi).

## Ekibe soru
1. **kesif.olay (değişmez alan) Wüst 1961 iddiası doğrulanamadı.** Erişebildiğim özet, çalışmanın Akdeniz'in derin dolaşımını ele aldığını gösteriyor; Cebelitarık'ta iki akıntı ifadesini bulamadım. Tam metin (Wiley) 403 verdi. `kesif` sabit alan olduğu için dokunmadım, ama `ZamanCizelgesi` bu metni 1961 kartında gösteriyor. Karar gerekli: olay metni değiştirilsin mi, yoksa 1961 kaldırılıp 2018 Sanchez-Román gösterilsin mi?
2. **Britannica ve NOAA erişilemedi** (403 / 404). Gibraltar için akademik Sanchez-Román (2018) ve Wikipedia kullanıldı. NOAA veya Britannica sayfasıyla teyit edilirse Wikipedia kaynağı değiştirilebilir.
3. **Tefsir kaynağı kısaltılmış.** İbn Kesîr'in Rahmân 55:19–20 yorumu quran.com'un İngilizce kısaltmasından okundu. Tam Arapça/Türkçe metinle kontrol edilmeli.
4. **Gibraltar ayet ilişkisi:** Tefsirde ayetin Cebelitarık'ı kastettiğine dair ifade yok. Metin bu ayrımı yapıyor; yayın çizgisi onaylanmalı.
5. Nuzul "Mekke dönemi (tartışmalı)" ve kesif alanları sabit olduğu için değiştirilmedi.

Denetim: `py -3 .oneri/denetle.py iki-denizin-karismamasi` → TAMAM.
