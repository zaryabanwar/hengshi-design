"""Freeze exact inputs for required bounded independent definition review."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[3]
packet = Path(__file__).resolve().parent
sources = [
    'AGENTS.md', '.specify/memory/constitution.md', 'PROJECT.md', 'DECISIONS.md',
    'TASKS.md', 'specs/001-platform-security-hardening/spec.md',
    'docs/software-definition/04-reconciliation-map.md',
    'docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md',
    'docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md',
    'docs/phase-1-architecture/contracts/HANDOFF_LIFECYCLE.md',
    'docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md',
    'docs/phase-1-architecture/contracts/DATA_CONTRACT.md',
    'docs/phase-1-architecture/contracts/CHAT_EVENT_PROTOCOL.md',
    'docs/phase-1-architecture/contracts/chat-event-control.schema.json',
    'docs/phase-1-architecture/contracts/chat-consent.schema.json',
    'docs/phase-1-architecture/contracts/chat-creation-request.schema.json',
    'docs/phase-1-architecture/contracts/chat-creation-response.schema.json',
    'docs/phase-1-architecture/contracts/booking-creation-request.schema.json',
    'docs/phase-1-architecture/contracts/booking-creation-response.schema.json',
    'docs/phase-1-architecture/contracts/process-value.schema.json',
    'docs/phase-1-architecture/contracts/publication-preparation.schema.json',
    'docs/phase-1-architecture/contracts/publication-manifest.schema.json',
    'scripts/validation/test_chat_event_control_schema.py',
    'scripts/validation/test_booking_creation_request_schema.py',
]
directory = packet / 'snapshots'
directory.mkdir(exist_ok=True)
manifest = []
for index, relative in enumerate(sources):
    data = (root / relative).read_bytes()
    destination = directory / f'{index:02d}-{Path(relative).name}'
    if destination.exists() and destination.read_bytes() != data:
        raise RuntimeError('Never overwrite an earlier frozen review input')
    destination.write_bytes(data)
    manifest.append({'path': destination.relative_to(root).as_posix(),
                     'original_path': relative, 'sha256': hashlib.sha256(data).hexdigest()})
target = packet / 'review-inputs.json'
encoded = (json.dumps(manifest, indent=2) + '\n').encode()
if target.exists() and target.read_bytes() != encoded:
    raise RuntimeError('Never replace the frozen manifest')
target.write_bytes(encoded)
print(json.dumps({'inputs': len(manifest), 'manifest_sha256': hashlib.sha256(encoded).hexdigest()}))
