"""Freeze correction 1 separately; initial REVISE bytes remain unchanged."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[4]
packet = Path(__file__).resolve().parent
prior = json.loads((packet.parent / 'review-inputs.json').read_text(encoding='utf-8'))
sources = [item['original_path'] for item in prior]
sources.append('docs/phase-1-architecture/contracts/reviews/chat-text-v1-2026-10-06.md')
directory = packet / 'snapshots'
directory.mkdir(exist_ok=True)
manifest = []
for index, relative in enumerate(sources):
    data = (root / relative).read_bytes()
    destination = directory / f'{index:02d}-{Path(relative).name}'
    if destination.exists() and destination.read_bytes() != data:
        raise RuntimeError('Frozen snapshot cannot be replaced')
    destination.write_bytes(data)
    manifest.append({'path': destination.relative_to(root).as_posix(),
                     'original_path': relative, 'sha256': hashlib.sha256(data).hexdigest()})
target = packet / 'review-inputs.json'
encoded = (json.dumps(manifest, indent=2) + '\n').encode()
if target.exists() and target.read_bytes() != encoded:
    raise RuntimeError('Frozen manifest cannot be replaced')
target.write_bytes(encoded)
print(json.dumps({'inputs': len(manifest), 'manifest_sha256': hashlib.sha256(encoded).hexdigest()}))
