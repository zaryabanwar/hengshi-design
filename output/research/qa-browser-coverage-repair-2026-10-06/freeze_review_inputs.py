"""Freeze the exact founder-approved one-word correction for independent review."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[3]
packet = Path(__file__).resolve().parent / 'independent-recheck'
directory = packet / 'snapshots'
directory.mkdir(parents=True, exist_ok=True)
inputs = [
    'AGENTS.md', '.specify/memory/constitution.md', 'PROJECT.md', 'DECISIONS.md',
    'specs/002-testing-and-monitoring/spec.md',
    'specs/002-testing-and-monitoring/checklists/requirements.md',
    'specs/002-testing-and-monitoring/reviews/qa-feature-v1-2026-10-04.md',
    'docs/phase-1-foundation/01-product-requirements.md',
    'docs/phase-1-architecture/contracts/QA_RECOVERY.md',
    'docs/phase-1-architecture/contracts/acceptance-matrix.csv',
    'output/research/qa-browser-coverage-repair-2026-10-06/spec.md.before',
    'output/research/qa-browser-coverage-repair-2026-10-06/spec.md.corrected',
    'output/research/qa-browser-coverage-repair-2026-10-06/application-observation.json',
]
manifest = []
for index, relative in enumerate(inputs):
    raw = (root / relative).read_bytes()
    destination = directory / f'{index:02d}-{Path(relative).name}'
    if destination.exists() and destination.read_bytes() != raw:
        raise RuntimeError('Frozen inputs cannot be replaced')
    destination.write_bytes(raw)
    manifest.append({'original_path': relative, 'path': destination.relative_to(root).as_posix(),
                     'sha256': hashlib.sha256(raw).hexdigest()})
encoded = (json.dumps(manifest, indent=2) + '\n').encode()
target = packet / 'review-inputs.json'
if target.exists() and target.read_bytes() != encoded:
    raise RuntimeError('Frozen manifest cannot be replaced')
target.write_bytes(encoded)
print(json.dumps({'input_count': len(manifest), 'manifest_sha256': hashlib.sha256(encoded).hexdigest()}))
