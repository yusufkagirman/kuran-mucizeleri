# İçerik iyileştirme denetimi. Kullanım: py -3 .oneri/denetle.py <slug>
# Korunması gerekenler: AyetParca satırları (Arapça + Diyanet meali), etkileşimli/görsel bileşenler, frontmatter'ın sabit alanları.
# Kontroller: Hikaye/Adim dengesi, tüm kaynak anahtarları kaynaklar.json'da, kalıp söz yok.
import re, sys, json, pathlib
sys.stdout.reconfigure(encoding="utf-8")

slug = sys.argv[1]
yedek_kok = sorted(pathlib.Path('surumler').glob('mucizeler v2 (*'))[-1]
eski = (yedek_kok / f'{slug}.mdx').read_text(encoding='utf-8')
yeni = pathlib.Path(f'src/content/mucizeler/{slug}.mdx').read_text(encoding='utf-8')
kaynaklar = json.loads(pathlib.Path('src/data/kaynaklar.json').read_text(encoding='utf-8'))
hata = []

def fm(s): return s.split('---')[1]
def alan(s, ad):
    m = re.search(rf'^{ad}:.*$', fm(s), re.M); return m.group(0) if m else None

# 1) Ayet satırları birebir (Arapça ve meal değişmez)
for satir in re.findall(r'^<AyetParca .*/>\s*$', eski, re.M):
    if satir.strip() not in yeni: hata.append(f'AyetParca değişmiş/silinmiş: {satir[:80]}')
# 2) Etkileşimli ve görsel bileşenler korunur (sayı olarak)
for ad in set(re.findall(r'^<([A-Z][A-Za-z]+)', eski, re.M)) - {'Hikaye', 'Adim', 'AyetParca', 'Alinti'}:
    if len(re.findall(rf'<{ad}[\s/>]', yeni)) < len(re.findall(rf'<{ad}[\s/>]', eski)): hata.append(f'bileşen eksik: <{ad}>')
# 3) Sabit frontmatter alanları
for ad in ('baslik', 'konu', 'sureAdi', 'vurgu', 'nuzul', 'kesif', 'vaat', 'durum', 'ornek'):
    if alan(eski, ad) != alan(yeni, ad): hata.append(f'frontmatter alanı değişmiş: {ad}')
blok = lambda s: re.search(r'^konu:[\s\S]*?(?=^itirazlar:)', s.replace('\r\n', '\n'), re.M).group(0)
if blok(eski) != blok(yeni): hata.append('sabit blok (konu…kesif/vaat, ayetler dahil) değişmiş')
if 'durum: taslak' not in yeni: hata.append('durum taslak kalmalı')
# 4) Yapı
if yeni.count('<Hikaye') != 1 or yeni.count('</Hikaye>') != 1: hata.append('tek <Hikaye> ... </Hikaye> olmalı')
if len(re.findall(r'^<Adim[ >]', yeni, re.M)) != yeni.count('</Adim>'): hata.append('Adim açılış/kapanış sayısı tutmuyor')
for m in re.finditer(r'^(<Adim[^>]*>|</Adim>|<Hikaye[^>]*>|</Hikaye>)[ \t]*\r?$', yeni, re.M):
    once, sonra = yeni[:m.start()], yeni[m.end():]
    if not once.endswith('\n\n') and not once.endswith('\r\n\r\n'): hata.append(f'etiketten önce boş satır yok: {m.group(1)[:30]}')
    if not re.match(r'\r?\n\r?\n', sonra): hata.append(f'etiketten sonra boş satır yok: {m.group(1)[:30]}')
# 5) Kaynak anahtarları
for k in set(re.findall(r'<Atif k="([^"]+)"', yeni)) | set(re.findall(r'kaynak:\s*([a-z0-9]+)', fm(yeni))):
    if k not in kaynaklar: hata.append(f'kaynaklar.json\'da yok: {k}')
m = re.search(r'^kaynaklar:\s*\[(.*)\]', fm(yeni), re.M)
liste = lambda s: {x.strip() for x in (re.search(r'^kaynaklar:\s*\[(.*)\]', fm(s), re.M) or [None, ''])[1].split(',') if x.strip()}
for k in liste(eski) - liste(yeni): hata.append(f'kaynak silinmiş (Yusuf: tefsir/kaynak silinmez): {k}')
for k in [x.strip() for x in (m.group(1).split(',') if m else []) if x.strip()]:
    if k not in kaynaklar: hata.append(f'kaynaklar listesinde bilinmeyen: {k}')
# 6) Kalıp sözler (Kurallar: lafza takılma)
for kalip in [r'yıl önce (haber verdi|söyledi|bildirdi)', r'tek kelimeyle', r"Kur'an(?:'da)? (?:bunu )?\w+ dedi\b", r'1\.?400 yıl', r'bilim(in)? (sonunda )?doğruladı', r'EKİP', r'TODO']:
    for x in re.findall(kalip, yeni, re.I): hata.append(f'kalıp/yasak ifade: "{x if isinstance(x, str) else kalip}"')

for x in re.findall(r"Kur'an\b[^.\n]{0,40}?\bdedi\b", yeni): hata.append(f'kalıp: "{x}"')
for x in re.findall(r"[İi]['’]c[aâ]z\w*|beyânî|gaybî|te['’]sir|teşrîî", yeni, re.I): hata.append(f'halkın anlamayacağı terim: "{x}"')
if re.search(r'[Ѐ-ӿ]', yeni): hata.append('Kiril harfi var (görünüşte Latin)')

print('\n'.join(hata) if hata else 'TAMAM')
sys.exit(1 if hata else 0)
