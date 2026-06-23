import json, os
root = r"c:\Users\RYZEN\OneDrive\Documenti\iptv_website1"
json_path = os.path.join(root, 'hreflang_report.json')
html_path = os.path.join(root, 'hreflang_report.html')
with open(json_path, 'r', encoding='utf-8') as fh:
    data = json.load(fh)
report = data.get('report', {})
issues = data.get('issues', {})
lines = []
lines.append('<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">')
lines.append('<title>Hreflang Report</title>')
lines.append('<style>body{font-family:Arial,Helvetica,sans-serif;padding:24px}table{border-collapse:collapse;width:100%}th,td{border:1px solid #ddd;padding:8px}th{background:#f4f4f4;text-align:left} .small{font-size:0.9rem;color:#555}</style>')
lines.append('</head><body>')
lines.append(f'<h1>Hreflang Report — {len(report)} pages</h1>')
lines.append(f'<p class="small">Issues found: {len(issues)}</p>')
if issues:
    lines.append('<h2>Pages with issues</h2><ul>')
    for p, info in issues.items():
        flags = ', '.join(info.get('flags', []))
        lines.append(f'<li><strong>{p}</strong> — {flags}</li>')
    lines.append('</ul>')
lines.append('<h2>All pages</h2>')
lines.append('<table><thead><tr><th>Page</th><th>Canonical</th><th>Hreflangs</th></tr></thead><tbody>')
for p, info in sorted(report.items()):
    c = info.get('canonical') or ''
    alts = info.get('alternates', [])
    if alts:
        alt_str = '<br>'.join([f"{a.get('hreflang')}: {a.get('href')}" for a in alts])
    else:
        alt_str = ''
    lines.append(f'<tr><td>{p}</td><td>{c}</td><td>{alt_str}</td></tr>')
lines.append('</tbody></table>')
lines.append('</body></html>')
with open(html_path, 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(lines))
print('Wrote', html_path)
