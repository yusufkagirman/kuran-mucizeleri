# Editoryal yeniden yazımı dosyaya uygular; uzun bileşen satırlarını (AyetParca, Gorsel, export blokları) mevcut dosyadan aynen alır.
# Kullanım: py -3 .oneri/birlestir.py <slug> <taslak.mdx>
# Taslakta {{AYET1}}, {{AYET2}}... (sıradaki AyetParca satırı), {{GORSEL1}}... (sıradaki Gorsel bloğu), {{EXPORT}} (export const bloğu) yer tutucuları.
import re, sys, pathlib

slug, taslak = sys.argv[1], pathlib.Path(sys.argv[2]).read_text(encoding='utf-8')
f = pathlib.Path(f'src/content/mucizeler/{slug}.mdx')
s = f.read_text(encoding='utf-8').replace('\r\n', '\n')
ayetler = re.findall(r'^<AyetParca .*/>$', s, re.M)
gorseller = re.findall(r'^<Gorsel[\s\S]*?/>$', s, re.M)
export = re.search(r'^export const[\s\S]*?^\];$', s, re.M)
for i, a in enumerate(ayetler, 1): taslak = taslak.replace(f'{{{{AYET{i}}}}}', a)
for i, g in enumerate(gorseller, 1): taslak = taslak.replace(f'{{{{GORSEL{i}}}}}', g)
if export: taslak = taslak.replace('{{EXPORT}}', export.group(0))
# {{SABIT}}: konu'dan itirazlar'a kadar (konu, sureAdi, ayetler, vurgu, nuzul, kesif, vaat) mevcut dosyadan aynen
sabit = re.search(r'^konu:[\s\S]*?(?=^itirazlar:)', s, re.M)
taslak = taslak.replace('{{SABIT}}\n', sabit.group(0))
kalan = re.findall(r'\{\{[A-Z0-9]+\}\}', taslak)
if kalan: sys.exit(f'doldurulmamış yer tutucu: {kalan}')
f.write_text(taslak, encoding='utf-8')
print('yazıldı', f)
