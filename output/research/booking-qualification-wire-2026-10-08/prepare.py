from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[3]
out = Path(__file__).resolve().parent
doc = root / 'docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md'
before = out / 'INTERFACE_CATALOG.before.md'
manifest = out / 'review-inputs.json'
assert not before.exists() and not manifest.exists()
raw = doc.read_bytes()
assert hashlib.sha256(raw).hexdigest() == 'f3fcda4c4eae880b11e33744e7a6a49ae583b45e0cfc86803c711f4639ff09a0'
addition = (out / 'wire-appendix.md').read_text(encoding='utf-8')
newline = '\r\n' if b'\r\n' in raw else '\n'
before.write_bytes(raw)
doc.write_bytes(raw + (newline + addition.replace('\n', newline)).encode('utf-8'))
assert doc.read_bytes().startswith(raw)
old_manifest = json.loads((root / 'output/research/booking-qualification-admission-2026-10-08/correction-1/review-inputs.json').read_text(encoding='utf-8'))
paths = [row['path'] for row in old_manifest['inputs']]
paths += [
    'docs/phase-1-architecture/contracts/booking-qualification.schema.json',
    'docs/phase-1-architecture/contracts/booking-creation-request.schema.json',
    'docs/phase-1-architecture/contracts/chat-creation-request.schema.json',
    'docs/phase-1-architecture/contracts/process-value.schema.json',
    'docs/phase-1-architecture/contracts/publication-preparation.schema.json',
    'docs/phase-1-architecture/contracts/publication-manifest.schema.json',
    'docs/phase-1-compatibility/backend-candidates-2026-10-04.json',
    'scripts/validation/test_booking_qualification_schema.py',
    'output/research/booking-qualification-wire-2026-10-08/email-observations.json',
    'output/research/booking-qualification-wire-2026-10-08/schema-tests.log',
]
rows = []
for i, rel in enumerate(paths):
    data = (root / rel).read_bytes()
    snapshot = out / 'snapshots' / f'{i:02d}-{Path(rel).name}'
    snapshot.parent.mkdir(exist_ok=True)
    assert not snapshot.exists()
    snapshot.write_bytes(data)
    rows.append({'path': rel, 'snapshot': snapshot.relative_to(root).as_posix(),
                 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
observations = json.loads((out / 'email-observations.json').read_text(encoding='utf-8'))
for source in observations['sources']:
    original = Path(source['path'])
    saved = Path(source['snapshot'])
    assert original.read_bytes() == saved.read_bytes()
    assert hashlib.sha256(original.read_bytes()).hexdigest() == source['sha256']
    rows.append({'path': original.relative_to(root).as_posix(),
                 'snapshot': saved.relative_to(root).as_posix(),
                 'bytes': source['bytes'], 'sha256': source['sha256']})
data = {'scope': 'Proposed IF-BOOK-02 directional shape, control/HTTP/numeric profile; no application or wire freeze',
        'inputs': rows, 'prefix': {'path': before.relative_to(root).as_posix(),
                                  'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}}
manifest.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'inputs': len(rows), 'manifest_sha256': hashlib.sha256(manifest.read_bytes()).hexdigest(),
                  'prefix_bytes': len(raw), 'catalogue_sha256': hashlib.sha256(doc.read_bytes()).hexdigest()}))
