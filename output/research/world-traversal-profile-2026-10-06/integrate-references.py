"""Add ordinary review references, then a separate two-document checkpoint slice."""
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent / 'reference-integration'
OUT.mkdir(exist_ok=False)
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
for row in json.loads((OUT.parent / 'review-inputs.json').read_text(encoding='utf-8')):
    if sha(ROOT / row['path']) != row['sha256']:
        raise RuntimeError('Reviewed input changed: ' + row['path'])
receipt = ROOT / 'docs/phase-1-3d/reviews/world-traversal-profile-v1-2026-10-06.md'
assert sha(receipt) == 'dc478551def8602bbef0d4e4bcbc8654a2dd277885e081c650217dca46c6d85a'
changes = []
def append(relative, addition):
    path = ROOT / relative
    (OUT / (path.name + '.before')).write_bytes(path.read_bytes())
    with path.open('ab') as file:
        file.write(addition.replace('\n', '\r\n').encode('utf-8'))
    changes.append({'path': relative, 'slice': 1, 'sha256': sha(path)})
append('docs/phase-1-3d/WORLD_EXPERIENCE.md', '''
Review reference added 2026-10-06: [traversal profile review PASS](reviews/world-traversal-profile-v1-2026-10-06.md)
covers the exact additive control/camera/body/movement proposal and asset-spec
reference. The [inspected World bytes](../../output/research/world-traversal-profile-2026-10-06/WORLD_EXPERIENCE.md.reviewed)
are preserved; this later reference is outside them. Targets remain unmeasured,
touch-pad cancellation mapping and approved screens remain held, and no runtime,
physical-device/accessibility, model, adapter or founder acceptance follows.
''')
append('docs/phase-1-3d/CAMPUS_ASSET_BUILD_SPEC.md', '''
The [traversal profile review](reviews/world-traversal-profile-v1-2026-10-06.md)
records bounded PASS for this exact reference and the controlling World proposal.
The [inspected asset specification](../../output/research/world-traversal-profile-2026-10-06/CAMPUS_ASSET_BUILD_SPEC.md.reviewed)
is preserved; this later reference is outside reviewed bytes. Proposed human-scale
and camera targets need acceptance/actual geometry and comfort evidence; D-071
composition and consumed model revision cycles remain unchanged.
''')

def update(relative, old, new):
    path = ROOT / relative
    (OUT / (path.name + '.before')).write_bytes(path.read_bytes())
    text = path.read_text(encoding='utf-8')
    assert text.count(old) == 1
    text = text.replace(old, new)
    if relative == 'PROJECT_STATE.yaml':
        assert len(text.splitlines()) == 50
    path.write_bytes(text.replace('\n', '\r\n').encode('utf-8'))
    changes.append({'path': relative, 'slice': 2, 'sha256': sha(path)})
update('PROJECT_STATE.yaml',
    'World_numeric_measurement_profile_correction1_bounded_review_PASS_unmeasured_targets_registration_actual_build_HTML_policy_association_formats_geometry_rights_named_device_probe_calibration_and_runtime_held',
    'World_measurement_correction1_and_mouse_touch_traversal_body_camera_profile_bounded_reviews_PASS_unmeasured_targets_pad_mapping_registration_build_formats_authored_geometry_rights_screens_named_device_calibration_runtime_and_acceptance_held')
update('docs/software-definition/04-reconciliation-map.md',
    'Numerical values remain unmeasured proposals; named devices/workloads/calibration, approved references and actual runtime qualification remain. |',
    'Numerical values remain unmeasured proposals; named devices/workloads/calibration, approved references and actual runtime qualification remain. The [mouse/touch body/camera/traversal profile](../phase-1-3d/WORLD_EXPERIENCE.md#mouse-touch-traversal-and-camera-profile-proposal--2026-10-06) also has [bounded independent review PASS](../phase-1-3d/reviews/world-traversal-profile-v1-2026-10-06.md): no-drag/keyboard alternatives, finite human/camera/speed/clearance targets, stalled-frame handling and current swept support/readiness. These are proposed definitions; pad cancellation mapping, production screens/geometry, physical comfort/accessibility, selected adapter/runtime and integrated/founder acceptance remain. |')
guards = json.loads((OUT.parent / 'protected-before.json').read_text(encoding='utf-8'))
for row in guards:
    if row['path'] != 'PROJECT_STATE.yaml' and sha(ROOT / row['path']) != row['sha256']:
        raise RuntimeError('Protected input changed: ' + row['path'])
command = ['git', '-c', 'core.autocrlf=false', '-c',
    'core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol',
    'diff', '--check', '--'] + [row['path'] for row in changes]
result = subprocess.run(command, cwd=ROOT, capture_output=True, encoding='utf-8', timeout=20)
(OUT / 'reference-integration.json').write_text(json.dumps({'changes': changes,
    'state_lines': 50, 'other_guards_match': 77,
    'scope': 'Two ordinary reference docs followed by two checkpoint docs; inspected bytes remain separately preserved.',
    'whitespace': {'exit_code': result.returncode, 'stdout': result.stdout,
                   'stderr': result.stderr}}, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'state_lines': 50, 'other_guards_match': 77,
                  'whitespace_exit_code': result.returncode}))
raise SystemExit(result.returncode)
