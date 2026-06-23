import os, re, json
root = r"c:\Users\RYZEN\OneDrive\Documenti\iptv_website1"
report = {}
for dirpath, dirs, files in os.walk(root):
    for f in files:
        if not f.lower().endswith('.html'):
            continue
        path = os.path.join(dirpath, f)
        relpath = os.path.relpath(path, root).replace('\\','/')
        try:
            with open(path, 'r', encoding='utf-8') as fh:
                txt = fh.read()
        except Exception as e:
            txt = ''
        canonical = None
        m = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']', txt, re.IGNORECASE)
        if m:
            canonical = m.group(1)
        alternates = re.findall(r'<link[^>]+rel=["\']alternate["\'][^>]*hreflang=["\']([^"\']+)["\'][^>]*href=["\']([^"\']+)["\']', txt, re.IGNORECASE)
        alternates = [{'hreflang':h, 'href':href} for (h, href) in alternates]
        report[relpath] = {'canonical': canonical, 'alternates': alternates}

# analyze
issues = {}
for p, data in report.items():
    c = data.get('canonical')
    alts = data.get('alternates', [])
    alt_hrefs = [a['href'] for a in alts]
    flags = []
    if not c:
        flags.append('missing_canonical')
    else:
        if c not in alt_hrefs:
            flags.append('canonical_not_in_hreflangs')
    has_self = any(a['href']==c for a in alts) if c else False
    if c and not has_self:
        flags.append('missing_self_referencing_hreflang')
    if flags:
        issues[p] = {'flags': flags, 'canonical': c, 'alternates': alts}

out = {'report': report, 'issues': issues}
with open(os.path.join(root, 'hreflang_report.json'), 'w', encoding='utf-8') as outfh:
    json.dump(out, outfh, ensure_ascii=False, indent=2)
print('Wrote hreflang_report.json with {} pages, {} issues'.format(len(report), len(issues)))