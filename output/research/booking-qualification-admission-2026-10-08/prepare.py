from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[3]
out = Path(__file__).resolve().parent
target = root / 'docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md'
before = out / 'INTERFACE_CATALOG.before.md'
manifest = out / 'review-inputs.json'
assert not before.exists() and not manifest.exists(), 'Do not overwrite evidence'
old = target.read_bytes()
addition = (out / 'qualification-appendix.md').read_text(encoding='utf-8')
assert '## Qualification admission and correction proposal' not in old.decode('utf-8')
newline = '\r\n' if b'\r\n' in old else '\n'
before.write_bytes(old)
target.write_bytes(old + (newline + addition.replace('\n', newline)).encode('utf-8'))
assert target.read_bytes().startswith(old)
inputs = [
    'AGENTS.md', '.specify/memory/constitution.md', 'PROJECT.md', 'DECISIONS.md',
    'docs/phase-1-ux-architecture/FLOWS.md',
    'docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md',
    'docs/phase-1-architecture/contracts/interface-catalog.csv',
    'docs/phase-1-architecture/contracts/process-fields.csv',
    'docs/phase-1-architecture/contracts/DATA_CONTRACT.md',
    'docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md',
    'docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md',
    'docs/phase-1-architecture/contracts/booking-status-response.schema.json',
    'specs/001-platform-security-hardening/spec.md',
]
rows = []
for index, rel in enumerate(inputs):
    raw = (root / rel).read_bytes()
    snap = out / 'snapshots' / f'{index:02d}-{Path(rel).name}'
    snap.parent.mkdir(exist_ok=True)
    assert not snap.exists()
    snap.write_bytes(raw)
    rows.append({'path': rel, 'snapshot': snap.relative_to(root).as_posix(),
                 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
record = {'scope': 'IF-BOOK-02 logical admission/correction only; no wire freeze or application',
          'inputs': rows,
          'predecessor': {'path': before.relative_to(root).as_posix(), 'bytes': len(old),
                          'sha256': hashlib.sha256(old).hexdigest()}}
manifest.write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'inputs': len(rows), 'predecessor_bytes': len(old),
                  'appended_bytes': len(target.read_bytes()) - len(old),
                  'manifest_sha256': hashlib.sha256(manifest.read_bytes()).hexdigest()}))
