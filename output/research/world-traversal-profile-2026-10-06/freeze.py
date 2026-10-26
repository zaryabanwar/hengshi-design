"""Freeze the proposed controls/clearance profile; no ordinary prose/runtime tests."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def save(name, data):
    with (OUT / name).open('x', encoding='utf-8') as file:
        json.dump(data, file, indent=2)
        file.write('\n')
guards = json.loads((ROOT / 'output/research/booking-creation-http-2026-10-06/protected-before.json').read_text(encoding='utf-8'))
for row in guards:
    if row['path'] != 'PROJECT_STATE.yaml' and sha(ROOT / row['path']) != row['sha256']:
        raise RuntimeError('Protected input changed: ' + row['path'])
current = [{'path': row['path'], 'sha256': sha(ROOT / row['path'])} for row in guards]
save('protected-before.json', current)
documents = [ROOT / 'docs/phase-1-3d/WORLD_EXPERIENCE.md',
             ROOT / 'docs/phase-1-3d/CAMPUS_ASSET_BUILD_SPEC.md']
for path in documents:
    if not path.read_bytes().startswith((OUT / (path.name + '.before')).read_bytes()):
        raise RuntimeError('Predecessor changed: ' + path.name)
    if path.read_bytes() != (OUT / (path.name + '.reviewed')).read_bytes():
        raise RuntimeError('Snapshot changed: ' + path.name)
command = ['git', '-c', 'core.autocrlf=false', '-c',
    'core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol',
    'diff', '--check', '--'] + [str(path.relative_to(ROOT)) for path in documents]
result = subprocess.run(command, cwd=ROOT, capture_output=True, encoding='utf-8', timeout=20)
save('scope-observations.json', {'recorded_at_utc': datetime.now(timezone.utc).isoformat(),
    'scope': 'Additive two-document World controls/traversal definition; targets unmeasured, no schema/prose/runtime/model tests.',
    'protected_inputs': len(current), 'predecessor_prefixes_match': True,
    'whitespace': {'command': command, 'exit_code': result.returncode,
                   'stdout': result.stdout, 'stderr': result.stderr}})
if result.returncode:
    raise RuntimeError('Whitespace inspection failed')
paths = {ROOT / row['path'] for row in current}
paths.update(documents)
paths.update(ROOT / path for path in ('TASKS.md', 'DECISIONS.md',
    'specs/003-3d-experience-completion/spec.md',
    'docs/phase-1-3d/WORLD_MEASUREMENT_PROFILE.md',
    'docs/phase-1-3d/SCENE_ASSEMBLY_CONTRACT.md',
    'docs/phase-1-3d/SPATIAL_STORYBOARD.md',
    'docs/phase-1-architecture/MOVEMENT_STREAMING_ADDENDUM.md',
    'docs/phase-1-ux-architecture/FLOWS.md',
    'docs/phase-1-ux-architecture/STATES_AND_RECOVERY.md',
    'docs/phase-1-foundation/01-product-requirements.md'))
paths.update(path for path in OUT.iterdir() if path.is_file())
packet = [{'path': path.relative_to(ROOT).as_posix(), 'sha256': sha(path)}
          for path in sorted(paths, key=lambda path: path.as_posix())]
save('review-inputs.json', packet)
print(json.dumps({'inputs': len(packet), 'packet_sha256': sha(OUT / 'review-inputs.json'),
                  'guards_match': len(current), 'whitespace_exit_code': result.returncode}))
