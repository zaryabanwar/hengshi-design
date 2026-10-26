"""Inspect licence candidates inside preserved archive text without executing it."""
from pathlib import Path
import hashlib
import io
import json
import re
import tarfile

OUT = Path(__file__).resolve().parent
PRIOR = OUT.parent / 'optional-wasm-bundle-2026-10-06'


def main():
    target = OUT / 'embedded-notice-candidates.json'
    if target.exists():
        raise RuntimeError('Preserve previous observation')
    inventory_raw = (OUT / 'contents.json').read_bytes()
    inventory = json.loads(inventory_raw)
    raw = (PRIOR / 'oxide-wasm32-wasi-4.3.3.tgz').read_bytes()
    if hashlib.sha256(raw).hexdigest() != inventory['archive_sha256']:
        raise RuntimeError('Archive identity changed')
    expected = {item['path']: item for item in inventory['files']}
    records = []
    with tarfile.open(fileobj=io.BytesIO(raw), mode='r:gz') as archive:
        for member in archive:
            item = expected.pop(member.name)
            content = archive.extractfile(member).read(item['bytes'] + 1)
            if len(content) != item['bytes'] or hashlib.sha256(content).hexdigest() != item['sha256']:
                raise RuntimeError('Member identity changed')
            if member.name.endswith('.wasm'):
                continue
            try:
                text = content.decode('utf-8')
            except UnicodeDecodeError:
                records.append({'path': member.name, 'utf8_text': False})
                continue
            lines = text.splitlines()
            hits = []
            for number, line in enumerate(lines, 1):
                if re.search(r'copyright|licen[sc]e|SPDX', line, re.I):
                    hits.append({'line': number, 'characters': len(line), 'excerpt': line[:512]})
            # Bundler source-path comments are candidates only, not a resolved graph.
            source_paths = sorted(set(re.findall(r'^\s*//\s+(node_modules/[^\r\n]+)', text, re.M)))
            if hits or source_paths:
                records.append({'path': member.name, 'utf8_text': True, 'sha256': item['sha256'],
                                'metadata_owner': item['metadata_owner'], 'keyword_lines': hits,
                                'bundler_source_path_candidates': source_paths})
    if expected:
        raise RuntimeError('Missing preserved member')
    result = {'inventory_sha256': hashlib.sha256(inventory_raw).hexdigest(),
              'archive_sha256': inventory['archive_sha256'], 'records': records,
              'limits': ['Keyword and source-path candidates, not legal completeness or a resolved dependency graph',
                         'Long lines are truncated at 512 characters; original member identities remain in contents.json',
                         'WASM binary excluded from text scan; no package source or binary was executed']}
    target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'text_records_with_candidates': len(records),
                      'keyword_lines': sum(len(r.get('keyword_lines', [])) for r in records),
                      'bundler_source_paths': sum(len(r.get('bundler_source_path_candidates', [])) for r in records)}))


if __name__ == '__main__':
    main()
