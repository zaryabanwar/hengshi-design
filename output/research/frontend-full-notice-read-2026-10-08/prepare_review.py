"""Freeze bounded evidence for independent read-only review."""
from pathlib import Path
import hashlib, json

root = Path(__file__).resolve().parents[3]
out = Path(__file__).resolve().parent
target = out / 'review-inputs.json'
assert not target.exists()
paths = [
    'AGENTS.md', '.specify/memory/constitution.md', 'PROJECT.md',
    'DECISIONS.md', 'PROJECT_STATE.yaml', 'TASKS.md',
    'docs/software-definition/README.md',
    'docs/phase-1-compatibility/README.md',
    'docs/phase-1-compatibility/refresh-evidence-2026-10-04.md',
    'docs/phase-1-compatibility/reviews/installed-notice-discovery-v1-2026-10-08.md',
    'docs/phase-1-compatibility/reviews/frontend-supply-chain-v1-2026-10-06.md',
    'output/research/frontend-supply-chain-2026-10-06/licence-inventory.json',
    'output/research/frontend-notice-discovery-2026-10-08/observations.json',
    'output/research/frontend-three-remedy-evaluation-2026-10-06/candidate/package-lock.json',
]
excluded = {'prepare_review.py', 'review-inputs.json'}
paths += [p.relative_to(root).as_posix() for p in out.rglob('*')
          if p.is_file() and p.name not in excluded and 'review-inputs' not in p.parts]
inputs = []
for rel in sorted(set(paths)):
    source = root / rel
    assert not source.is_symlink()
    raw = source.read_bytes()
    snap = out / 'review-inputs' / rel
    snap.parent.mkdir(parents=True, exist_ok=True)
    assert not snap.exists()
    snap.write_bytes(raw)
    inputs.append({'source': rel, 'snapshot': snap.relative_to(out).as_posix(),
                   'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
manifest = {
    'product': 'Hengshi Design v1', 'status': 'DOING',
    'scope': 'Full text notice discovery, immediate root-name inventory and fixed registry/source pointer associations only; no licence applicability, provenance, full graph or adoption approval',
    'candidate_base': 'output/research/frontend-three-remedy-evaluation-2026-10-06/candidate',
    'inputs': inputs,
}
target.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
for item in inputs:
    for path in (root / item['source'], out / item['snapshot']):
        raw = path.read_bytes()
        assert len(raw) == item['bytes'] and hashlib.sha256(raw).hexdigest() == item['sha256']
print(json.dumps({'inputs': len(inputs), 'manifest_sha256': hashlib.sha256(target.read_bytes()).hexdigest()}))
