"""Freeze two proposed definition documents and primary sources; no performance test."""
from pathlib import Path
from datetime import datetime, timezone
from urllib.request import Request, urlopen
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
SPEC = ROOT / 'docs/phase-1-3d/CAMPUS_ASSET_BUILD_SPEC.md'
PROFILE = ROOT / 'docs/phase-1-3d/WORLD_MEASUREMENT_PROFILE.md'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def save(name, data):
    with (OUT / name).open('x', encoding='utf-8') as file:
        json.dump(data, file, indent=2)
        file.write('\n')

if (OUT / 'CAMPUS_ASSET_BUILD_SPEC.md.before').exists():
    raise RuntimeError('Refusing overwrite')
guards = json.loads((ROOT / 'output/research/frontend-supply-chain-2026-10-06/protected-before.json').read_text(encoding='utf-8'))
# Permit only the completed, separately recorded state reference integration.
for row in guards:
    if row['path'] != 'PROJECT_STATE.yaml' and sha(ROOT / row['path']) != row['sha256']:
        raise RuntimeError(f'Protected input changed: {row["path"]}')
current_guards = [{'path': row['path'], 'sha256': sha(ROOT / row['path'])} for row in guards]
save('protected-before.json', current_guards)
(OUT / 'CAMPUS_ASSET_BUILD_SPEC.md.before').write_bytes(SPEC.read_bytes())
text = '''
## Numerical measurement profile proposal — 2026-10-06

The separate [World measurement/loading profile](WORLD_MEASUREMENT_PROFILE.md)
now proposes finite frame, pixel/submission, CPU/GPU reservation and concurrency/
queue targets, decimal transfer accounting, matched sustained-degradation checks
and qualification categories under NFR-007. It retains the accepted transfer
ceilings, composition, safe-ground/ownership and stream-lock boundaries.
These are engineering starting targets, not benchmarks, accepted device fitness
or portable readings of total memory/temperature. Exact named devices/network/
probe/workload settings, cost calibration, rights/appearance, stable graph,
independent review and founder acceptance remain; no runner, runtime selector,
production model or measured performance follows from the definition.
Earlier inspected specification bytes remain preserved and are not extended
to this addition. No additional study/model revision is performed.
'''
with SPEC.open('ab') as file:
    file.write(text.replace('\n', '\r\n').encode('utf-8'))
for path in (SPEC, PROFILE):
    (OUT / (path.name + '.reviewed')).write_bytes(path.read_bytes())
sources = {
    'webgl-best-practices': 'https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/WebGL_best_practices',
    'request-animation-frame': 'https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame',
    'encoded-body-size': 'https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming/encodedBodySize',
    'transfer-size': 'https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming/transferSize',
    'three-renderer': 'https://threejs.org/docs/pages/WebGLRenderer.html',
}
source_rows = []
for name, url in sources.items():
    try:
        with urlopen(Request(url, headers={'User-Agent': 'Hengshi-definition-research/1.0'}), timeout=30) as response:
            raw = response.read(4 * 1024 * 1024)
            path = OUT / (name + '.html')
            path.write_bytes(raw)
            source_rows.append({'name': name, 'requested_url': url, 'final_url': response.url,
                'status': response.status, 'sha256': sha(path), 'bytes': len(raw)})
    except Exception as error:
        source_rows.append({'name': name, 'requested_url': url, 'error_type': type(error).__name__,
                            'error': str(error), 'scope': 'Direct saved retrieval failed; do not fabricate it. Web-tool observations are separate.'})
save('source-observations.json', {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
    'context7_library': '/websites/threejs', 'sources': source_rows,
    'scope': 'Primary platform constraints only; all proposed numerical thresholds/durations are engineering targets without executed measurement.'})
paths = {SPEC, PROFILE, ROOT / 'docs/phase-1-foundation/01-product-requirements.md',
         ROOT / 'docs/phase-1-architecture/contracts/QA_RECOVERY.md', ROOT / 'docs/phase-1-3d/WORLD_EXPERIENCE.md',
         ROOT / 'docs/phase-1-3d/SCENE_ASSEMBLY_CONTRACT.md', ROOT / 'docs/phase-1-architecture/MOVEMENT_STREAMING_ADDENDUM.md',
         ROOT / 'TASKS.md', ROOT / 'DECISIONS.md', ROOT / 'docs/software-definition/04-reconciliation-map.md'}
paths.update(ROOT / row['path'] for row in current_guards)
paths.update(path for path in OUT.iterdir() if path.is_file())
packet = [{'path': path.relative_to(ROOT).as_posix(), 'sha256': sha(path)}
          for path in sorted(paths, key=lambda value: value.as_posix())]
save('review-inputs.json', packet)
print(f'{len(packet)} inputs SHA256 {sha(OUT / "review-inputs.json")}; no measurement, model change or prose test performed.')
