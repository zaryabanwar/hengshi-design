from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[3]
out = Path(__file__).resolve().parent
correction = out / 'correction-1'
assert not correction.exists(), 'Do not overwrite a correction cycle'
correction.mkdir()
doc = root / 'docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md'
old = doc.read_bytes()
(correction / 'INTERFACE_CATALOG.before-correction.md').write_bytes(old)
text = old.decode('utf-8')
newline = '\r\n' if '\r\n' in text else '\n'
original_dispatch = '''Any older challenge result or queued dispatch must fail its current revision/purpose
guard; issuing a new challenge remains IF-BOOK-03, not an incidental PATCH effect.
The corrected qualification can be QUALIFICATION_COMPLETE, never VERIFIED merely
because its syntax is valid. Resend is not this correction action.'''
new_dispatch = '''Any older challenge result must fail its current revision/purpose guard. Queued
delivery work not yet admitted to provider dispatch must recheck its bound email
revision/purpose and reject stale dispatch admission. Correction cannot recall
email already dispatched or stop delivery already admitted/in flight; those known
or unknown effects remain under IF-BOOK-03's delivery reconciliation before safe
retry/resend. Address correction alone is not proof of delivery failure. The old
challenge remains invalid even if that email arrives. Issuing a new challenge
remains IF-BOOK-03, not an incidental PATCH effect. The corrected qualification can
be QUALIFICATION_COMPLETE, never VERIFIED merely because its syntax is valid.
Resend is not this correction action.'''
original_fence = '''Once a booking/provider intent is admitted or its outcome is unresolved, refuse
qualification replacement until that intent's current authority has established
that replacement is safe under its approved state policy. In particular, a
timeout, expired lease, RECONCILIATION_ERROR or missing provider read cannot unlock
correction. Neither confirmed bookings nor reschedule/cancel transitions are'''
new_fence = '''Once a calendar/meeting booking intent is admitted or its outcome is unresolved,
refuse qualification replacement until that intent's current authority has
established that replacement is safe under its approved state policy. A timeout,
expired lease, RECONCILIATION_ERROR or missing calendar/meeting provider read cannot
unlock correction. This fence concerns booking mutations, not verification-email
delivery. Before booking-intent admission, an otherwise authorized address
correction remains possible even while earlier verification delivery is unknown;
the current challenge is invalidated, and delivery reconciliation/retry rules
remain separate. An old email delivery cannot become a permanent correction lock.
Neither confirmed bookings nor reschedule/cancel transitions are'''
original_dispatch_bytes = original_dispatch.replace('\n', newline).encode('utf-8')
new_dispatch_bytes = new_dispatch.replace('\n', newline).encode('utf-8')
original_fence_bytes = original_fence.replace('\n', newline).encode('utf-8')
new_fence_bytes = new_fence.replace('\n', newline).encode('utf-8')
assert old.count(original_dispatch_bytes) == 1 and old.count(original_fence_bytes) == 1
new = old.replace(original_dispatch_bytes, new_dispatch_bytes).replace(original_fence_bytes, new_fence_bytes)
assert new.startswith((out / 'INTERFACE_CATALOG.before.md').read_bytes())
doc.write_bytes(new)
base = json.loads((out / 'review-inputs.json').read_text(encoding='utf-8'))
rows = []
for index, row in enumerate(base['inputs']):
    source = root / row['path']
    raw = source.read_bytes()
    if row['path'] != doc.relative_to(root).as_posix():
        assert hashlib.sha256(raw).hexdigest() == row['sha256']
    snap = correction / 'snapshots' / f'{index:02d}-{source.name}'
    snap.parent.mkdir(exist_ok=True)
    snap.write_bytes(raw)
    rows.append({'path': row['path'], 'snapshot': snap.relative_to(root).as_posix(),
                 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
record = {'scope': base['scope'], 'correction_cycle': 1, 'inputs': rows,
          'predecessor': base['predecessor'],
          'initial_manifest_sha256': hashlib.sha256((out / 'review-inputs.json').read_bytes()).hexdigest()}
manifest = correction / 'review-inputs.json'
manifest.write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'inputs': len(rows), 'other_input_identities_unchanged': len(rows)-1,
                  'manifest_sha256': hashlib.sha256(manifest.read_bytes()).hexdigest(),
                  'catalogue_sha256': hashlib.sha256(new).hexdigest()}))
