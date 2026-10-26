from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[3]
out = Path(__file__).resolve().parent
path = out / 'review-inputs.json'
archive = out / 'review-inputs.initial32.json'
assert not archive.exists()
archive.write_bytes(path.read_bytes())
record = json.loads(path.read_text(encoding='utf-8'))
assert len(record['inputs']) == 32
additional = [
    'scripts/validation/test_process_value_schema.py',
    'scripts/validation/test_booking_creation_request_schema.py',
    'scripts/validation/test_chat_creation_request_schema.py',
    'output/research/booking-qualification-wire-2026-10-08/observe-email.py',
]
for rel in additional:
    raw = (root / rel).read_bytes()
    snap = out / 'snapshots' / f'{len(record["inputs"]):02d}-{Path(rel).name}'
    assert not snap.exists()
    snap.write_bytes(raw)
    record['inputs'].append({'path': rel, 'snapshot': snap.relative_to(root).as_posix(),
                             'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
record['unreviewed_initial_manifest_preserved'] = archive.relative_to(root).as_posix()
path.write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
for row in record['inputs']:
    raw = (root / row['path']).read_bytes()
    assert raw == (root / row['snapshot']).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == row['sha256']
print(json.dumps({'inputs': len(record['inputs']), 'manifest_sha256': hashlib.sha256(path.read_bytes()).hexdigest()}))
