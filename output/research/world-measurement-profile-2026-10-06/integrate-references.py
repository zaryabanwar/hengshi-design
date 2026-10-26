"""Link reviewed proposal, then checkpoint separately; never extend receipt scope."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent / 'reference-integration'
OUT.mkdir(exist_ok=False)
CORRECTION = Path(__file__).resolve().parent / 'correction-1'
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
for row in json.loads((CORRECTION / 'review-inputs.json').read_text()):
    if sha(ROOT / row['path']) != row['sha256']:
        raise RuntimeError('Reviewed input changed: ' + row['path'])
receipt = ROOT / 'docs/phase-1-3d/reviews/world-measurement-profile-v1-2026-10-06.md'
if sha(receipt) != 'ab205fd68efc89ad47afb59d51972ec73a3d786d26c4397400779e5fd85b2410':
    raise RuntimeError('Review receipt changed')

changes = []
def append(path, text, slice_number):
    path = ROOT / path
    (OUT / (path.name + '.before')).write_bytes(path.read_bytes())
    with path.open('ab') as file:
        file.write(text.replace('\n', '\r\n').encode())
    changes.append({'path': path.relative_to(ROOT).as_posix(), 'sha256': sha(path), 'slice': slice_number})

append('docs/phase-1-3d/WORLD_MEASUREMENT_PROFILE.md', '''
Review reference added 2026-10-06: [correction-1 independent review PASS](reviews/world-measurement-profile-v1-2026-10-06.md#correction-1-disposition--superseding-bounded-pass)
covers the corrected measurement proposal at its exact frozen inputs. The
[inspected profile](../../output/research/world-measurement-profile-2026-10-06/correction-1/WORLD_MEASUREMENT_PROFILE.md.reviewed)
is preserved; this later reference is outside those bytes. Numerical values remain
unmeasured engineering targets requiring integrated/founder acceptance, named
workloads/devices and actual qualification. No runtime or appearance proof follows.
''', 1)
append('docs/phase-1-3d/CAMPUS_ASSET_BUILD_SPEC.md', '''
The [correction-1 measurement review](reviews/world-measurement-profile-v1-2026-10-06.md#correction-1-disposition--superseding-bounded-pass)
now records bounded PASS for the exact numerical profile proposal and this
appendix. Completed CPU render-submission cycles, missed/boundary/no-progress gaps
and separate transfer/resident accounting are defined; they are not GPU execution
or measured device fitness. Inspected [specification bytes](../../output/research/world-measurement-profile-2026-10-06/CAMPUS_ASSET_BUILD_SPEC.md.reviewed)
remain preserved, and this later reference is outside reviewed inputs. Targets,
implementation, production asset and integrated/founder acceptance stay separate.
''', 1)

state = ROOT / 'PROJECT_STATE.yaml'
mapping = ROOT / 'docs/software-definition/04-reconciliation-map.md'
for path in (state, mapping):
    (OUT / (path.name + '.before')).write_bytes(path.read_bytes())
text = state.read_text()
old = 'registration_actual_build_HTML_policy_association_format_acceptance_extensions_decoders_collision_format_acceptance_geometry_rights_numeric_profiles_runtime_held'
new = 'World_numeric_measurement_profile_correction1_bounded_review_PASS_unmeasured_targets_registration_actual_build_HTML_policy_association_formats_geometry_rights_named_device_probe_calibration_and_runtime_held'
assert text.count(old) == 1
text = text.replace(old, new)
assert len(text.splitlines()) == 50
state.write_bytes(text.replace('\n', '\r\n').encode())
text = mapping.read_text()
old = 'All three normal model revisions are used; acceptance grants no further substantial composition exception. |'
new = 'All three normal model revisions are used; acceptance grants no further substantial composition exception. The [numerical measurement/loading profile](../phase-1-3d/WORLD_MEASUREMENT_PROFILE.md) has [correction-1 bounded review PASS](../phase-1-3d/reviews/world-measurement-profile-v1-2026-10-06.md#correction-1-disposition--superseding-bounded-pass): complete CPU World-frame submission sampling, actual transfer versus resident inventory, finite cost/work targets and sustained qualification method. Numerical values remain unmeasured proposals; named devices/workloads/calibration, approved references and actual runtime qualification remain. |'
assert text.count(old) == 1
mapping.write_bytes(text.replace(old, new).replace('\n', '\r\n').encode())
for path in (state, mapping):
    changes.append({'path': path.relative_to(ROOT).as_posix(), 'sha256': sha(path), 'slice': 2})
guards = json.loads((ROOT / 'output/research/world-measurement-profile-2026-10-06/protected-before.json').read_text())
for row in guards:
    if row['path'] != 'PROJECT_STATE.yaml' and sha(ROOT / row['path']) != row['sha256']:
        raise RuntimeError('Protected input changed: ' + row['path'])
(OUT / 'reference-integration.json').write_text(json.dumps({'changes': changes,
    'scope': 'Two ordinary reference edits, then separate two-document checkpoint slice; later links are outside reviewed bytes.',
    'state_lines': 50, 'other_guards_match': 77}, indent=2) + '\n')
print('Reviewed-profile references and separate checkpoint integrated; 50 state lines, 77 other guards match.')
