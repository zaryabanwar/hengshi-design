"""Read-only installed notice discovery; no licence interpretation or clearance."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
PRIOR = ROOT / 'output/research/frontend-supply-chain-2026-10-06/licence-inventory.json'
BASE = ROOT / 'output/research/frontend-three-remedy-evaluation-2026-10-06/candidate'
digest = lambda data: hashlib.sha256(data).hexdigest()
prior = json.loads(PRIOR.read_text(encoding='utf-8'))
lock_before = (BASE / 'package-lock.json').read_bytes()
assert digest(lock_before) == prior['lock_sha256']
records = []
terms = re.compile(r'copyright|spdx-license|licen[cs]e|permission is hereby|redistribution', re.I)
text_suffixes = {'.js', '.mjs', '.cjs', '.ts', '.json', '.md', '.txt', '.html', '.css'}
for item in prior['records']:
    if not item['installed'] or item['top_level_licence_and_notice_files']:
        continue
    folder = BASE / item['lock_path']
    metadata = (folder / 'package.json').read_bytes()
    assert digest(metadata) == item['metadata_sha256'], item['name']
    files, hits, excluded = [], [], []
    for path in sorted(folder.rglob('*')):
        rel = path.relative_to(folder)
        if 'node_modules' in rel.parts:
            continue  # separately inventoried dependencies are not parent notices
        if path.is_symlink():
            excluded.append({'path': rel.as_posix(), 'reason': 'symlink not followed'})
            continue
        if not path.is_file():
            continue
        raw = path.read_bytes()
        files.append({'path': rel.as_posix(), 'bytes': len(raw), 'sha256': digest(raw)})
        if path.suffix.lower() not in text_suffixes:
            excluded.append({'path': rel.as_posix(), 'reason': 'non-text content not interpreted'})
            continue
        head = raw[:8192].decode('utf-8', errors='replace')
        matching = [{'line': n, 'excerpt': line[:240]}
                    for n, line in enumerate(head.splitlines(), 1) if terms.search(line)]
        if matching:
            hits.append({'path': rel.as_posix(), 'inspected_prefix_bytes': min(len(raw), 8192),
                         'prefix_truncated': len(raw) > 8192, 'matches': matching[:12]})
    # Re-read each observed own file; no moving-file claim is accepted.
    for file in files:
        raw = (folder / file['path']).read_bytes()
        assert len(raw) == file['bytes'] and digest(raw) == file['sha256']
    records.append({'name': item['name'], 'version': item['version'],
                    'lock_path': item['lock_path'], 'metadata_sha256': digest(metadata),
                    'own_files': files, 'header_or_readme_hits': hits,
                    'uninterpreted': excluded})
assert len(records) == 11
assert (BASE / 'package-lock.json').read_bytes() == lock_before
result = {'product': 'Hengshi Design v1', 'status': 'DOING',
          'checked_at_utc': datetime.now(timezone.utc).isoformat(),
          'prior_inventory_sha256': digest(PRIOR.read_bytes()),
          'candidate_lock_sha256': digest(lock_before), 'records': records,
          'limits': ['Read-only own-file discovery in the existing isolated candidate',
                     'Only first 8192 bytes of each eligible text file inspected for notice terms',
                     'Term matches are not necessarily complete applicable licence notices',
                     'Nested node_modules are separate inventory items and excluded',
                     'Binary contents, full bundled notices, archive integrity/provenance and legal interpretation unproven',
                     'No installation, script execution, application change, graph selection or clearance']}
target = OUT / 'observations.json'
assert not target.exists(), 'Preserve previous observation; choose a new evidence directory'
target.write_text(json.dumps(result, indent=2, ensure_ascii=True) + '\n', encoding='utf-8')
print(json.dumps({'packages': len(records),
                  'packages_with_term_hits': sum(bool(x['header_or_readme_hits']) for x in records),
                  'own_files_observed': sum(len(x['own_files']) for x in records),
                  'candidate_lock_unchanged': True}))
