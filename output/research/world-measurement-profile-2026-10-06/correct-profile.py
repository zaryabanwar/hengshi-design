"""Correct the reviewed prose ambiguity, retaining initial inputs and all guards."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
INITIAL = Path(__file__).resolve().parent
OUT = INITIAL / 'correction-1'
PROFILE = ROOT / 'docs/phase-1-3d/WORLD_MEASUREMENT_PROFILE.md'
RECEIPT = ROOT / 'docs/phase-1-3d/reviews/world-measurement-profile-v1-2026-10-06.md'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

initial = json.loads((INITIAL / 'review-inputs.json').read_text())
guards = json.loads((INITIAL / 'protected-before.json').read_text())
for row in initial + guards:
    if sha(ROOT / row['path']) != row['sha256']:
        raise RuntimeError('Initial input changed: ' + row['path'])
if sha(RECEIPT) != 'b9d85f3bb0f30f091ceb84fe6c8652a6f930812d3bbcceb8131bd54273e5b464':
    raise RuntimeError('Initial review changed')
OUT.mkdir(exist_ok=False)
(OUT / 'WORLD_MEASUREMENT_PROFILE.md.before').write_bytes(PROFILE.read_bytes())
(OUT / 'initial-review.md').write_bytes(RECEIPT.read_bytes())
text = PROFILE.read_text(encoding='utf-8')
old = '''additional dependencies and background prefetch triggered by it. Count shared
already-resident dependencies once for that sample, with their ownership visible.
Also report cumulative visit transfer so repeated traversal is not masked.'''
new = '''additional dependencies and background prefetch triggered by it. Attribute each
newly transferred shared body once to the demand that initiated it; record other
consumers' ownership separately. Already-resident dependencies stay visible once
in the sample's residency inventory, but add no network body bytes without a new
transfer. Report actual cached-body consumption separately from new transfer;
neither resource reuse nor cache revalidation permits fabricated zero-size data.
Also report cumulative visit transfer so repeated traversal is not masked.'''
assert text.count(old) == 1
text = text.replace(old, new)
old = '''Cadence is a preference; actual display scheduling can differ. Frame intervals
are timestamp deltas during the identified foreground active World sample, not
average FPS or asserted GPU execution duration. Percentiles use sorted observations
and the nearest-rank rule: rank ceil(p × n), with p 0.95/0.99. Keep sample counts,
duration and raw interval evidence. Do not remove stalls caused by loading,
decode/upload, controls, board use or resize from an active sample. Report
background/pause/reentry periods separately; they are not fast-frame samples.'''
new = '''Cadence is a preference; actual display scheduling can differ. The observation
population is completed CPU submission cycles for a complete active World frame,
including every required render pass. Record one monotonic-clock timestamp at the
end of each such cycle; a bare requestAnimationFrame callback, React update or
individual pass is not a frame observation. This measures submission progress,
not GPU completion, physical display presentation or GPU execution duration.

Use timestamp deltas between successive complete cycles. Include the active
sample's start-to-first-cycle and last-cycle-to-end gaps in the raw observations;
the interval containing late or missed cycles is not divided into invented fast
frames. Deliberate callback skipping for a 30 Hz render cadence consequently
measures approximately 33 ms submission intervals on a 60 Hz display, rather than
counting unused 16 ms callbacks. The sample workload must require ongoing World
rendering (for example traversal/camera movement); intentional idle or pause is
identified separately and cannot certify active performance. Do not mark a stall
as idle merely because no new frame was submitted.

Percentiles use sorted interval observations and the nearest-rank rule: rank
ceil(p × n), with p 0.95/0.99. Keep cycle count, sample duration, raw intervals,
boundary-gap labels and any observation loss. Do not remove stalls caused by
loading, decode/upload, controls, board use or resize from an active sample.
A five-second active window with no complete submission is no-progress, not a
passing empty or callback-only sample; it fails qualification and is a failing
window for the degradation guard below. Missing instrumentation makes the result
unavailable, never passing. Report background/pause/reentry periods separately;
they are not fast-frame samples. The sustained comparison uses this same event
population and ongoing-workload requirement in both matched windows.'''
assert text.count(old) == 1
text = text.replace(old, new)
PROFILE.write_bytes(text.replace('\n', '\r\n').encode('utf-8'))
(OUT / 'WORLD_MEASUREMENT_PROFILE.md.reviewed').write_bytes(PROFILE.read_bytes())
note = {'recorded_at_utc': datetime.now(timezone.utc).isoformat(), 'correction_cycle': 1,
        'canonical_changes': ['docs/phase-1-3d/WORLD_MEASUREMENT_PROFILE.md'],
        'required_finding': 'Explicit complete CPU World-frame submission events, cadence skip/miss/boundary gaps, active workload, no-progress and unavailable samples; no GPU presentation claim.',
        'accounting_clarification': 'Shared actual newly transferred body bytes and separately owned already-resident/cached inventory.',
        'unchanged': 'All numerical targets, accepted caps, layout/model, other canonical documents and protected inputs.',
        'scope': 'Prose definition correction only; no runtime, benchmark, model change or phrase test.'}
(OUT / 'correction.json').write_text(json.dumps(note, indent=2) + '\n', encoding='utf-8')
for row in guards:
    if sha(ROOT / row['path']) != row['sha256']:
        raise RuntimeError('Protected input changed: ' + row['path'])
paths = {ROOT / row['path'] for row in initial}
paths.update(path for path in OUT.iterdir() if path.is_file())
paths.add(Path(__file__).resolve())
packet = [{'path': path.relative_to(ROOT).as_posix(), 'sha256': sha(path)}
          for path in sorted(paths, key=lambda p: p.as_posix())]
(OUT / 'review-inputs.json').write_text(json.dumps(packet, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'inputs': len(packet), 'packet_sha256': sha(OUT / 'review-inputs.json'),
                  'guards_match': len(guards), 'profile_sha256': sha(PROFILE)}))
