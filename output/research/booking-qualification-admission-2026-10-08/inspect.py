from pathlib import Path
import hashlib
import json
import re
import unicodedata

root = Path(__file__).resolve().parents[3]
out = Path(__file__).resolve().parent
manifest = json.loads((out / 'review-inputs.json').read_text(encoding='utf-8'))
checks = []
for row in manifest['inputs']:
    source = (root / row['path']).read_bytes()
    saved = (root / row['snapshot']).read_bytes()
    checks.append({'path': row['path'], 'matches': source == saved
                   and len(source) == row['bytes']
                   and hashlib.sha256(source).hexdigest() == row['sha256']})
doc = root / 'docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md'
old = (out / 'INTERFACE_CATALOG.before.md').read_bytes()
current = doc.read_bytes()
appendix = current[len(old):].decode('utf-8')

def anchor(title):
    title = title.lower().strip().replace(' ', '-')
    return ''.join(c for c in title if c in '-_' or unicodedata.category(c)[0] in 'LN')

links = []
for href in re.findall(r'\]\(([^)]+)\)', appendix):
    if href.startswith('https://'):
        continue
    path, _, fragment = href.partition('#')
    target = (doc.parent / path).resolve() if path else doc
    exists = target.is_file()
    fragments = []
    if exists and fragment:
        text = target.read_text(encoding='utf-8')
        fragments = [anchor(h) for h in re.findall(r'^#{1,6}\s+(.+)$', text, re.M)]
    links.append({'href': href, 'exists': exists, 'fragment_exists': not fragment or fragment in fragments})
result = {'scope': 'artifact identity/prefix/local reference inspection only; no behavioral tests',
          'frozen_inputs': checks, 'predecessor_exact_prefix': current.startswith(old),
          'appendix_occurrences': current.count(b'## Qualification admission and correction proposal'),
          'local_links': links,
          'runtime_tests': 'not run; no application implementation or UI change'}
assert all(c['matches'] for c in checks)
assert result['predecessor_exact_prefix'] and result['appendix_occurrences'] == 1
assert all(link['exists'] and link['fragment_exists'] for link in links), links
dest = out / 'producer-inspection.json'
assert not dest.exists(), 'Do not overwrite evidence'
dest.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'matching_inputs': len(checks), 'prefix': True, 'local_links': len(links)}))
