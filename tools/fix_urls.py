"""
fix_urls.py
Walks the workspace and replaces occurrences of '' with site-root relative paths.
Usage: python tools/fix_urls.py
This script creates a backup copy of each file it edits (same folder, .bak appended).
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PATTERN = ''

exts = ['.html', '.py']

changed = []
for p in ROOT.rglob('*'):
    if p.is_file() and p.suffix.lower() in exts:
        text = p.read_text(encoding='utf-8')
        if PATTERN in text:
            new = text.replace(PATTERN, '')
            # small post-fix: ensure we didn't accidentally leave 'http(s)://' broken elsewhere
            new = new.replace('https://', 'https:///')
            # write backup then new content
            bak = p.with_suffix(p.suffix + '.bak')
            bak.write_text(text, encoding='utf-8')
            p.write_text(new, encoding='utf-8')
            changed.append(str(p.relative_to(ROOT)))

print('Updated files:', len(changed))
for c in changed:
    print(c)

if not changed:
    print('No files needed changes.')
