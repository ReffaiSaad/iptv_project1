#!/usr/bin/env python3
# generate_sitemap.py - scans folder for .html files and writes sitemap.xml
import os
from datetime import date
root = os.path.dirname(__file__)
base = 'https://streamplanettv.online'
urls = []
for dirpath, dirnames, filenames in os.walk(root):
    # skip hidden directories
    if '.git' in dirpath:
        continue
    for f in filenames:
        if f.endswith('.html'):
            rel = os.path.relpath(os.path.join(dirpath, f), root).replace('\\','/')
            if rel == 'index.html':
                loc = base + '/'
            else:
                loc = base + '/' + rel
            urls.append((loc, date.today().isoformat()))

sitemap_path = os.path.join(root, 'sitemap.xml')
with open(sitemap_path, 'w', encoding='utf-8') as s:
    s.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    s.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for loc, lastmod in sorted(urls):
        s.write('  <url>\n')
        s.write('    <loc>{}</loc>\n'.format(loc))
        s.write('    <lastmod>{}</lastmod>\n'.format(lastmod))
        s.write('  </url>\n')
    s.write('</urlset>\n')
print('Wrote', sitemap_path)
