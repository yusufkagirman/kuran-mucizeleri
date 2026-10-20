# Petrol: iyileştirme raporu

## Analiz (eski metnin zayıf yanları)
- Açılış ("bir zamanlar güneşte yeşeren canlılardan doğdu") kesin bir sonucu cümle olarak veriyordu; hangi bulgunun bu sonuca gittiği belirsizdi.
- Hikâyede "Ayetin indiği yıllarda petrol ... nereden geldiğini kimse bilmezdi" gibi kaynaksız bir dönem sahnesi vardı.
- Treibs'in ne bulduğu ("bitkilerin klorofilinden türeyen moleküller") somut değildi: metal içeren porfirin ve klorofile benzerlik eksikti.
- Itiraz 1, İbn Abbas'ı "ilk müfessirler" diye genelleyerek kaynaksız bir atıf yapıyordu.
- Itiraz 2'nin cevabı "dönüşümün özü aynıdır" diyerek hüküm veriyordu; kaynaklı ayrıntı ("alg ve plankton" ile "otlak" farkı) yoktu.

## Düzeltilen olgular
- "Kapkara petrol bir zamanlar güneşte yeşeren canlılardan doğdu" (kart/hook) → "Petrolde, yeşil bitkilerin klorofiline benzeyen moleküller bulundu" (kart). Hook'ta 1936 ve Treibs açıkça yer aldı.
- "1936'da Treibs, petrolün içinde bitkilerin klorofilinden türeyen moleküller buldu" → "1936'da Treibs, petrolde metal içeren porfirin moleküller buldu; bunlar klorofile çok benzer bir yapıdaydı." Kaynak: https://en.wikipedia.org/wiki/Alfred_E._Treibs ve https://www.researchgate.net/publication/230427445_Chlorophyll-_und_Haminderivate_in_organischen_Mineralstoffen (Angewandte Chemie 49(38), 682–686).
- "Ayetin indiği yıllarda petrol ... bilinirdi" → kaldırıldı (kaynaksız).
- "İbn Abbas ve ilk müfessirler" → "İbn Abbas'a göre ayet 'kurudu ve değişti' anlamındadır; İbn Kesîr de bu rivayeti aktarır." Kaynak: https://quran.com/al-ala/5/tafsirs/en-tafisr-ibn-kathir.
- "Petrol çoğunlukla plankton ve alglerden" itirazına cevap: hüküm yerine kaynaklı tablo (zooplankton ve alg; bir kısmı odunsu bitki; ayet "otlak" der, alg ve plankton aynı şey değildir). Kaynak: https://en.wikipedia.org/wiki/Petroleum .
- Gövdeye eklenen süreç: önce kerojen, sonra ısıyla sıvı ve gaz hidrokarbon. Kaynak: aynı Wikipedia sayfası.
- Son söz: "bir insanın bilgisinden mi doğdu?" (hüküm-yakın soru) → "Yeşil bir canlının kapkara bir sıvıya dönüşebileceğini, 7. yüzyılda kim söyleyebilirdi?"

## Eklenen olgular
1. Treibs 1936: petrolde metalloporfirinler; klorofile benzer yapı; petrolün biyolojik kökeninin o dönemde tartışmalı olduğu ve bulgunun bu görüşü destekleyip güçlendirdiği. Kaynak: https://en.wikipedia.org/wiki/Alfred_E._Treibs ; Angewandte Chemie 1936 kaydı: https://www.researchgate.net/publication/230427445_Chlorophyll-_und_Haminderivate_in_organischen_Mineralstoffen . Alıntı (Wikipedia özeti): "This discovery helped confirm the biological origin of petroleum, which was previously controversial."
2. Petrolün oluşumu: önce kerojen, sonra ısıyla sıvı ve gaz hidrokarbonlar; kaynak organizmalar zooplankton, algler ve odunsu bitkiler. Kaynak: https://en.wikipedia.org/wiki/Petroleum . Alıntı: "first into a waxy material known as kerogen", "then with more heat into liquid and gaseous hydrocarbons".
3. İbn Abbas'ın A'lâ 87:5 yorumu: "Dried up and altered." Kaynak: İbn Kesîr, https://quran.com/al-ala/5/tafsirs/en-tafisr-ibn-kathir (kısaltılmış İngilizce metin).

## Ekibe soru
1. **Britannica ve akademik Treibs metni erişilemedi.** Britannica petrol sayfası 403 verdi; Treibs 1936'nın tam metni ve ACS/MDPI makaleleri de açılamadı. Treibs bilgisi Wikipedia ve ResearchGate bibliyografik sayfasından alındı. Teyit için Britannica ya da tam makale gerekir.
2. **Kaynak kalitesi:** Petrol oluşumu ve Treibs ayrıntıları Wikipedia'ya dayanıyor (ikincil). Kuran–bilim sitesinin kuralı "akademik/Britannica" olduğu için bu iki kaynağın yerine akademik bir kaynak bulunması önerilir (ör. Kvenvolden 2006, USGS sayfası; 500 hatası verdi).
3. **Ayet ile petrol arasındaki bağ:** Ayet "yeşillik" ve "otlak"tan söz ediyor; petrolün kaynağı çoğunlukla alg ve planktonlar. Metin bu farkı açıkça yazıyor. Yayın çizgisi için karar gerekli: bu ayrım metinde kalsın mı?
4. Gorsel bileşenindeki "Treibs molekülü" ve vanadyum yazısı (`petrol.mdx` içinde) değiştirilmedi; görsel kaynağının (Wikimedia Commons, "Treibs&Chlorophyll.png") iddiası doğrulanmadı.
5. `kesif` ve `nuzul` sabit alanlar; değiştirilmedi.

Denetim: `py -3 .oneri/denetle.py petrol` → TAMAM.
