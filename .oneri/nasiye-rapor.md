# nasiye: içerik iyileştirme raporu

## Analiz
- Hook ve kart aynı cümleyi tekrarlıyordu; ilk cümle "karar veren yer" diye genel kaldı.
- "Planlamayı ve karar vermeyi yürüten prefrontal korteks" iddiası kaynaksızdı; karar verme kısmı kaynakla doğrulanamadı.
- Gövde Gage olayını anlatmıyordu; 1848 kazası, 1868 raporu ve sonrası tek bir çizgide değildi.
- "Kalp düşüncenin yeri sayılırdı" ve "müfessirler deyim dedi" gibi tarihsel iddialar kaynaksızdı; çıkarıldı.
- Itiraz 2 cevabı ("kişiliği ve kararları bu yüzden değişti") kaynağın izin verdiğinden fazlasını söylüyordu.

## Düzeltilen olgular
- "Prefrontal korteks planlamayı ve karar vermeyi yürütür, 19. yüzyılda anlaşılmaya başladı" → "Kişiliği ve davranışı düzenleyen bölge alnın hemen arkasında; bu yıllarda görülmeye başlandı." Kaynak: https://bps.org.uk/psychologist/phineas-gage-unravelling-myth
- "Harlow ... karar verme biçiminin değiştiğini rapor etti" (gövde) → Harlow'un 1868 ifadesi: "the balance between his intellectual faculties and animal propensities seems to have been destroyed" ve "no longer Gage". Kaynak: https://bps.org.uk/psychologist/phineas-gage-unravelling-myth
- "Bugün planlama ve karar vermenin ... alın lobunda yürütüldüğü biliniyor" (Damasio 1994 atfı) → kaldırıldı; yerine Ferrier 1873 ve hasar sınırının tartışmalı olduğu yazıldı. Kaynak: https://bps.org.uk/psychologist/phineas-gage-unravelling-myth
- Itiraz 2 cevabı: "Bu bölgesi zarar gören Gage'in kişiliği ve kararları bu yüzden değişti" → hasar bölgesinin kafatası ölçümüne dayandığı ve tartışmalı olduğu. Kaynak: https://bps.org.uk/psychologist/phineas-gage-unravelling-myth
- "Ayet ... perçeminden tutmak ... boyun eğdirme" ve "müfessirler deyim dedi" → yalnız deyim anlamı, ayet metni üzerinden.
- Kart, kesif dışındaki frontmatter alanları, AyetParca satırları ve bileşenler değişmedi (kesif sabit alan olduğu için olduğu gibi bırakıldı).

## Eklenen olgular
- 1868, Harlow ve "artık eski Gage değil" (Harlow'un raporundan). Kaynak: https://bps.org.uk/psychologist/phineas-gage-unravelling-myth. Alıntı: "no longer Gage" (Harlow 1868, BPS makalesinde aktarılır).
- 1873, David Ferrier maymun deneyleri: "demonstrated that prefrontal damage caused profound personality changes" (BPS makalesi). Kaynak: https://bps.org.uk/psychologist/phineas-gage-unravelling-myth
- 1848 kazası (13 Eylül 1848, Vermont, sol yanağın altından giriş, tepeden çıkış). Kaynak: https://www.damninteresting.com/phineas-gages-brain-injury/ (sayfa açıldı; alıntı: "13 September 1848", "entered through the bottom of his left cheekbone", "exited through the top of his head"). Bu paragrafa atıf eklenmedi; aşağıdaki "Ekibe soru" bölümüne bakın.
- Itiraz 2 yeni kaynak: "The Psychologist" (Macmillan, 2008). Yazar ve tarih BPS sayfasında yazılı: Malcolm Macmillan, 03 Eylül 2008.

Yeni kaynak anahtarları (kaynak-ekle.py ile): `macmillan2008gage`, `albalushi2021sulb`, `manickam2018testis` (sulb-teraib için de kullanıldı), `damninteresting2008gage` (bkz. aşağı).

## Ekibe soru
1. **damninteresting2008gage kaydının yılı yanlış.** Sayfanın yılı doğrulanmadan "2008" yazıldı. Bu kayıt metinde kullanılmadı, ama `src/data/kaynaklar.json` içinde duruyor. Yıl düzeltilmeli ya da kayıt silinmeli (betik dışından; bu ajan dokunmadı). Olay ayrıntıları için kaynak olarak yerinde kalması, yılı netleşince atıf verilebilir.
2. **Tabanca ölçüsü kaynaklarda farklı.** Damninteresting "3 feet, 14 pound" diyor; Britannica özeti 13.25 lb ve 3.58 feet (Britannica sayfası açılamadı, 403). Bu yüzden metinde ölçü verilmedi.
3. **Prefrontal korteksin karar vermedeki rolü.** Açılan kaynaklarda (BPS) karar verme geçmiyor; PubMed özetleri açılamadı. "Karar verme" kavramı metinden çıkarıldı. Ekip bir kaynakla geri koymak isterse hook'un "karar" ifadesi yeniden değerlendirilmeli.
4. **Gage'in hasar bölgesi.** Harlow 1868 "left frontal and middle left lobes" dedi (BPS). Damasio 1994 (PubMed özeti aranmıştır, sayfa açılamadı) hem sağ hem sol prefrontali önerdi; Ratiu sonradan yalnız sol hemisferi savundu (ikincil kaynak). Hüküm verilmedi.
5. **Hûd 56 atfı.** Ayet metninden alındı, web'de açılmış bir sayfa yok.
6. **Kaza paragrafı** atıfsız bırakıldı: tek açılan kaynak damninteresting, yılı yanlış kayıtta.
7. **kesif olay metni** ("karar verme davranışı") sabit alan olduğu için değiştirilmedi; BPS makalesi karar verme dilini kullanmıyor.

Denetim: `py -3 .oneri/denetle.py nasiye` -> TAMAM
