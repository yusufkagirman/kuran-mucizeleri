# Dişi bal arısı: içerik iyileştirme raporu

## Analiz
- Hook "kral arı sanılıyordu" dediği halde kaynağı yoktu; Aristoteles'in kral arı görüşü (Butler makalesi, Wikipedia) eklendi.
- "Asırlar boyunca bu bir dil kuralı olarak okundu" ve "ayetin indiği dönemde kimse bilmiyordu" gibi kaynaksız genellemeler kaldırıldı.
- 1609 keşfi ile işçi arıların dişiliği tek cümlede karışıyordu; iki olgu ayrıldı.
- İşçi arıların dansı (von Frisch, Nobel 1973) gibi somut, görülebilir bir ayrıntı yoktu; eklendi.
- Itiraz cevaplarında "erkek arılar çiçeğe konmaz, petek örmez" gibi kaynaksız iddialar vardı; yalnız kaynaklı olanlar bırakıldı.

## Düzeltilen olgular
- "Arıların cinsiyetini kimse bilmiyordu" (619 adımı) -> "Aristoteles'ten beri arıların kovanında bir kral olduğu anlatılıyordu" -> https://en.wikipedia.org/wiki/Charles_Butler_(beekeeper) (makale Aristoteles'in king-bee görüşünden söz eder)
- "Erkek arılar bal yapmaz" -> "Erkek arıların iğnesi yoktur, kovayı savunmazlar ve esas işleri üremedir" -> https://en.wikipedia.org/wiki/Honey_bee (kaynak: "Drones are male... They do not defend the hive ... and do not have a stinger"; "primarily exist for reproduction")
- "Kovanı yöneten arının dişi olduğunu" (1609) değişmedi; Butler'ın kitabı "The Feminine Monarchie" olarak adlandırıldı. Kaynak: https://en.wikipedia.org/wiki/Charles_Butler_(beekeeper)

## Eklenen olgular
- Butler 1609, kitabın adı ve kral/kraliçe karşıtlığı: https://en.wikipedia.org/wiki/Charles_Butler_(beekeeper). Alıntı: "governed not by a king-bee, as Aristotle claimed, but by a queen-bee".
- Işçi arılar dişidir ve dans eder: https://en.wikipedia.org/wiki/Honey_bee. Alıntı: "Drones are male, while workers and queens are female."
- Kolonide 60.000'e kadar işçi: https://en.wikipedia.org/wiki/Honey_bee. Alıntı: "A typical colony may contain as many as 60,000 worker bees." (bu cümle metne alınmadı; kaynakta doğrulandı)
- Dans: https://en.wikipedia.org/wiki/Karl_von_Frisch. Alıntı: "The 'waggle dance' is used to relay information about more distant food sources." 1927 kitabı (Aus dem Leben der Bienen) ve 1973 Nobel ödülü aynı sayfadan.

## Denetim
- `py -3 .oneri/denetle.py bal-arisi` -> TAMAM

## Ekibe soru
- Bileşen `KovanTahmin.astro` "Erkek: Bal yapmaz, petek örmez, çiçeğe konmaz" diyor. Kaynakla yalnız "iğne yok, kovayı savunmaz, üreme" doğrulandı; "petek örmez" ve "çiçeğe konmaz" doğrulanmadı. Bileşen bu iddiayı taşıyor; düzeltme bileşen dosyasında gerekiyor (bu görev dışında).
- `Fiiller.astro` ve `ittehızî/kulî/fesülükî` dişil kip iddiası Arapça yazıdan okunuyor; ayrıca bir dilbilgisi kaynağıyla web'de doğrulanmadı.
- Itiraz 1'deki Hucurât 14 ("bedeviler dedi") atfı web'de ayrıca açılmadı.
