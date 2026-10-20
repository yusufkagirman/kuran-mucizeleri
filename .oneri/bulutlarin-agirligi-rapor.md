# Bulutların ağırlığı: içerik iyileştirme raporu

## Analiz
- "Ayetin indiği çağda bulut hafif bir buhar gibi görünürdü" ve "ifade bir benzetme gibi okundu" gibi tarihsel algı iddiaları kaynaksızdı; kaldırıldı.
- Warner 1955 "uçakla ölçüm" olarak anılıyordu; makalenin özetinde uçak bilgisi yok, kaldırıldı (aşağıda not).
- Keşif olgusu ile hesap (500 ton) ayrı ayrı kaynaklanmadı; USGS varsayımı açıkça yazıldı.
- Itiraz 2 cevabındaki "yükselen hava akımları damlacıkları tutar" iddiası USGS'te yoktu; USGS'in kaldırma açıklaması kullanıldı.

## Düzeltilen olgular
- "Asırlar boyunca ifade bir benzetme gibi okundu; bulutun ağırlığını tartmanın yolu yoktu" -> kaldırıldı; yerine "ölçülebildi" (20. yüzyıl) ve Warner 1955 atfı.
- "Uçakla bulutların içine girip ölçtü" -> "makalesinin özetinde 'Measurements have been made of liquid water content throughout many cumuliform clouds.'" -> https://tellusjournal.org/articles/10.3402/tellusa.v7i4.8917
- "Yüzlerce ton" ve "500 ton" -> USGS: 1 km³ için 0,5 g/m³ varsayımı, sonuç ~500.000 kg -> https://www.usgs.gov/special-topics/water-science-school/science/how-much-does-a-cloud-weigh

## Eklenen olgular
- Warner 1955 özet alıntısı (yukarıda). Makale: Tellus 7(4), 449–457.
- Bulut neden düşmez: USGS, bulutun çevresindeki kuru havadan daha az yoğun olması nedeniyle havada süzüldüğünü yazar. Alıntı: "clouds float on air because the moist air in clouds is less dense than dry air."
- 1 km³ = 1 milyar m³ ve 0,5 g/m³ varsayımı: USGS (yukarıdaki bağlantı).

## Denetim
- `py -3 .oneri/denetle.py bulutlarin-agirligi` -> TAMAM

## Ekibe soru
- `kesif.olay` alanı ("Uçakla yapılan ölçümler...") frontmatter'da sabit tutulmak zorunda (denetçi kesif satırını kontrol ediyor). Uçak ayrıntısı Warner özetinde yok; bu ifade kaynakla doğrulanamadı. Alan değiştirilmeli mi, karar gerekli.
- Warner 1955 makalesinin tam metni açılamadı (yalnız özet). Ölçümün uçakla yapılıp yapılmadığı tam metinle teyit edilmeli.
- USGS'in 500 ton hesabı metrik ton (500.000 kg); sayfa aynı hesabı "551 ton" olarak da veriyor. Metinde "500 ton" bırakıldı.
