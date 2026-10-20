# Azalıp artan rahim: iyileştirme raporu

## Analiz (eski metnin zayıf yanları)
- Hook, Ra'd 8'deki "eksiltip artırma" sözünü, rahim iç zarının aylık döngüsüyle doğrudan eşleyerek sundu. Klasik okuma bu eşleşmeye dayanmıyordu; bağlantı metinde hüküm gibi kuruluyordu.
- "Kanama bilinmiyordu, eski tıp fazla kanın atılması sanıyordu" iddiası kaynaksızdı.
- "Bu döngü bugün gün gün izlenebiliyor" (`noyes1950`) iddiası: kaynağa ulaşılamadı (ScienceDirect 403), dolayısıyla doğrulanamadı.
- "Viyanalı hekimler" ifadesi açılmış bir kaynaktan gelmiyordu.
- İtiraz cevabı "bu bilgi bugün de insana kapalıdır" bir hükümdü.

## Düzeltilen olgular
- Hook: "Rahmin iç zarındaki bu aylık azalıp artış ise ancak 20. yüzyılın başında mikroskopla gösterildi" → ayet ve aylık değişim iki ayrı olgu olarak yan yana. Ayetin klasik okuması: çocuğun erken ya da geç doğması ve sayısı. Kaynak: https://www.kuranvemeali.com/rad-suresi/8-ayeti-tefsiri ("erken mi, geç mi, yoksa tam vaktinde mi doğacağını"; "bir tane mi, ikiz mi veya daha fazla mı").
- "Ayetteki tağîdu fiili suyun çekilip azalmasını, tezdâdu ise artmasını anlatır. Asırlar boyunca bu ifade düşük, erken doğum ve gebeliğin uzaması diye anlaşıldı." → "Ayetteki iki fiil ... Klasik tefsirde ... çocuğun erken ya da geç doğması ve tek ya da çoklu olması biçiminde okunması yaygındır." (Aynı kaynak.) "Suyun çekilmesi" yorumu kaynaksızdı, kaldırıldı.
- "Viyanalı hekimler Hitschmann ve Adler" → "1908'de Hitschmann ve Adler, rahim iç zarının her ay kalınlaşıp döküldüğünü gösteren bir çalışma yayımladı." Kaynak: `hitschmann1908` (kaynaklar.json, mevcut).
- "Bu döngü bugün gün gün izlenebiliyor" (`noyes1950`) → kaldırıldı; `noyes1950` kaynak listesinden çıkarıldı.
- Yeni cümle: "Bu çalışmanın esas sonuçları, sonraki araştırmacılar tarafından doğrulandı." Kaynak: https://jamanetwork.com/journals/jama/article-abstract/231766 ("The investigations of Hitschmann and Adler ... confirmed in all essential respects by subsequent workers").
- İtiraz 1 cevabı: "Rahmin iç zarının ... ancak mikroskopla görüldü" + "eski tıp ... sanıyordu" → kaynaksız kısım kaldırıldı; yalnızca kanamanın görüldüğü ve iç zarın döngüsünün 1908'de mikroskopla ortaya konduğu bırakıldı.
- İtiraz 2 cevabı: "Ayet her an ve eksiksiz bilmekten söz eder; bu bilgi bugün de insana kapalıdır" → yorum kaldırıldı. Yerine: ultrason ve testlerin belli bir anda ve belli araçlarla bilgi verdiği ve klasik tefsirde ayetin konusunun doğum zamanı ve sayısı olduğu.
- Hikâye sonu: "Peki bu, kelimeye sonradan yüklenmiş bir anlam olabilir mi?" → "Peki ayetin klasik okuması ile bu aylık döngü arasında nasıl bir bağ var?" (soru, hüküm yok.)
- Son söz: "bir insan onun durmadan azalıp arttığını nereden bilebilirdi?" → "bu aylık değişimin gözlemi hangi araçla mümkün olacaktı?" (soru.)
- Gorsel ve Dongu bileşenleri, nuzul, kesif ve diğer sabit frontmatter alanları aynen kaldı.

## Eklenen olgular
- Klasik tefsir okuması (Ra'd 8): https://www.kuranvemeali.com/rad-suresi/8-ayeti-tefsiri . Alıntı (Türkçe, tefsirden): "erken mi, geç mi, yoksa tam vaktinde mi doğacağını". Anahtar: `diyanetrad`. Not: Diyanet portalının tefsir sayfası açılamadı, metin kuranvemeali.com üzerinden okundu.
- Hitschmann ve Adler'in sonuçlarının sonraki çalışmalarla doğrulanması: https://jamanetwork.com/journals/jama/article-abstract/231766 . Alıntı: "confirmed in all essential respects by subsequent workers". Anahtar: `jamaendo`. Yayın yılı sayfadaki atıftan (1924) alındı; bu yıl 1908 çalışmasının yılı değil, JAMA özetinin yılı.

## Ekibe soru
1. Hook ile ayetin klasik okuması arasındaki fark. Ra'd 8'in klasik okuması çocuğun doğum zamanı ve sayısı; aylık rahim döngüsü ayrı bir gözlem. Metin ikisini yan yana koyuyor, bağı hüküm olarak kurmuyor. Bu bağı kurmak mı, yan yana bırakmak mı istediğinize karar verin. Bu bağın kaynağı, eski metinde de dahil, bulunamadı.
2. Hitschmann ve Adler'in öncelik tarihi: Thieme özetinin arama özetinde (açılamadı) 1907 ile 1908 tartışması geçiyor ve "ilk tarif" iddiası var. Metinde yalnızca 1908 yayını ve sonraki doğrulama kullanıldı; "ilk" ifadesi yok.
3. `noyes1950` kaynağı açılamadı; kaynak listesinden çıkarıldı. Anahtar `kaynaklar.json`'da duruyor, ancak bu metinde kullanılmıyor.
4. Görsel künyeleri (DESIDERIUS, Dr. Roshan Nasimudeen) Commons sayfaları açılarak doğrulanmadı; eski metinden aynen alındı.

Denetim: `py -3 .oneri/denetle.py rahim-bilgisi` → TAMAM
