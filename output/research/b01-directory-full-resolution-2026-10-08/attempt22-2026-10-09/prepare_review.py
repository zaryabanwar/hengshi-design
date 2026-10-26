"""Freeze the bounded full-resolution directory review without another Figma call."""
from pathlib import Path
import hashlib, json

here = Path(__file__).resolve().parent
root = here.parents[3]
destination = here / 'review-inputs.json'
assert not destination.exists()
prior_path = root / 'output/research/b01-directory-call19-2026-10-08/review-inputs.json'
prior = json.loads(prior_path.read_bytes())
paths = [prior_path]
for item in prior['inputs']:
    path = prior_path.parent / item['snapshot']
    data = path.read_bytes()
    assert len(data) == item['bytes'] and hashlib.sha256(data).hexdigest() == item['sha256']
    paths.append(path)
paths += [here / name for name in ('authorization.json', 'executed-call.js', 'provider-result.json', 'export-report.json', 'pixel-inventory.json', 'receipt.json', 'extract_export.py')]
paths += sorted(here.glob('sheet-*.png')) + sorted((here / 'tiles').glob('*.png')) + sorted((here / 'comparisons').glob('*.png'))
snapshots = here / 'review-inputs'
snapshots.mkdir()
for source in ('AGENTS.md', 'DECISIONS.md', 'docs/phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md'):
    target = snapshots / source
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes((root / source).read_bytes())
    paths.append(target)
inputs = [{'path': path.relative_to(root).as_posix(), 'bytes': path.stat().st_size, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()} for path in paths]
manifest = {'product_release': 'v1', 'status': 'DOING', 'review_authorized': False, 'scope': 'Independent review of all52 existing directory-reference full-resolution pixels, exact source-to-sheet/tile mapping and reported cleanup; earlier construction review keeps its scope. No Figma call, source correction, runtime/accessibility compliance, full B01 coverage or acceptance.', 'inputs': inputs}
destination.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'inputs': len(inputs), 'manifest_sha256': hashlib.sha256(destination.read_bytes()).hexdigest()}))
