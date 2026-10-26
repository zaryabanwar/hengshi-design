from pathlib import Path
import hashlib
import json

root = Path.cwd()
base = root / 'output/research/booking-qualification-wire-2026-10-08'
out = base / 'correction-1'
old = json.loads((base / 'review-inputs.json').read_bytes())
paths = [item['path'] for item in old['inputs']]
paths += [str((out / name).relative_to(root)).replace('\\', '/')
          for name in ['observe-reserved-email.py', 'reserved-email-observations.json']]
paths += [str((base / 'tooling-environments.json').relative_to(root)).replace('\\', '/')]
snaps = out / 'snapshots'
snaps.mkdir(exist_ok=False)
rows = []
for i, name in enumerate(paths):
    path = root / name
    raw = path.read_bytes()
    if i < 36 and name != 'docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md':
        assert hashlib.sha256(raw).hexdigest() == old['inputs'][i]['sha256'], name
    snap = snaps / f'{i:02d}-{path.name}'
    snap.write_bytes(raw)
    rows.append(dict(path=name, snapshot=str(snap.relative_to(root)).replace('\\', '/'),
                     bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest()))
prefix = (root / old['prefix']['path']).read_bytes()
catalogue = (root / 'docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md').read_bytes()
assert catalogue.startswith(prefix)
report = dict(scope=old['scope'], correction=1, inputs=rows, prefix=old['prefix'],
              prior_manifest='output/research/booking-qualification-wire-2026-10-08/review-inputs.json',
              addressed_findings=['QW01', 'QW02'])
dest = out / 'review-inputs.json'
assert not dest.exists()
raw = (json.dumps(report, indent=2) + '\n').encode()
dest.write_bytes(raw)
print(json.dumps(dict(inputs=len(rows), manifest_sha256=hashlib.sha256(raw).hexdigest(),
                     catalogue_sha256=hashlib.sha256(catalogue).hexdigest(),
                     prior_other_inputs_unchanged=35, prefix_bytes=len(prefix))))
