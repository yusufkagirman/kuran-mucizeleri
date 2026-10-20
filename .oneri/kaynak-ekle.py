# Paralel ajanlar için kilitli kaynak ekleme: src/data/kaynaklar.json'a tek kayıt ekler (anahtar varsa dokunmaz).
# Kullanım: py -3 .oneri/kaynak-ekle.py <anahtar> '<json>'
#   json: {"yazar": "...", "yil": 1957, "baslik": "...", "yayin": "...", "doi": "..." | "url": "https://..."}
import json, os, sys, time, pathlib

anahtar, kayit = sys.argv[1], json.loads(sys.argv[2])
for alan in ('yazar', 'yil', 'baslik', 'yayin'):
    if alan not in kayit: sys.exit(f'eksik alan: {alan}')
if not (kayit.get('doi') or kayit.get('url')) and kayit['yil'] > 1900:
    sys.exit('1900 sonrası kaynakta doi ya da url zorunlu')

kilit = pathlib.Path('.oneri/.kilit')
for _ in range(200):
    try: os.mkdir(kilit); break
    except FileExistsError: time.sleep(0.1)
else: sys.exit('kilit alınamadı')
try:
    f = pathlib.Path('src/data/kaynaklar.json')
    veri = json.loads(f.read_text(encoding='utf-8'))
    if anahtar in veri: print('zaten var:', anahtar)
    else:
        veri[anahtar] = kayit
        satirlar = ',\n'.join(f'  {json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False)}' for k, v in veri.items())
        f.write_text('{\n' + satirlar + '\n}\n', encoding='utf-8')
        print('eklendi:', anahtar)
finally:
    os.rmdir(kilit)
