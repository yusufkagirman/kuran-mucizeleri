# Sunum dönüşümü denetimi: Hikaye/Adim sarmalayıcıları çıkarılınca her MDX'in metni yedekle birebir aynı mı?
# Kullanım: py -3 .metin-denetim.py "surumler/mucizeler v1 (...)"  → farklı dosyaları ve ilk farkı yazar.
import re, sys, pathlib
yedek = pathlib.Path(sys.argv[1]); hata = 0
def norm(s, yeni):
    if yeni:
        s = re.sub(r"^import (Hikaye|Adim) from .*\n", "", s, flags=re.M)
        s = re.sub(r"^<Hikaye[^>]*>\s*$|^</Hikaye>\s*$|^<Adim[^>]*>\s*$|^</Adim>\s*$", "", s, flags=re.M)
    return [l.strip() for l in s.splitlines() if l.strip()]
for f in sorted(pathlib.Path('src/content/mucizeler').glob('*.mdx')):
    a, b = norm((yedek / f.name).read_text(encoding='utf-8'), False), norm(f.read_text(encoding='utf-8'), True)
    if a != b:
        hata += 1
        i = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
        print(f'FARK {f.name} satır {i}:\n  eski: {a[i][:120] if i < len(a) else "-"}\n  yeni: {b[i][:120] if i < len(b) else "-"}')
    elif '<Hikaye' in f.read_text(encoding='utf-8'): print('tamam', f.name)
print('hata', hata)
