"""Bounded prose correction; preserve prior inputs and schema unchanged."""
from pathlib import Path
import hashlib
import json

root = Path.cwd()
base = root / 'output/research/booking-qualification-wire-2026-10-08'
out = base / 'correction-1'
out.mkdir(exist_ok=False)
manifest_path = base / 'review-inputs.json'
manifest_raw = manifest_path.read_bytes()
manifest = json.loads(manifest_raw)
for item in manifest['inputs']:
    raw = (root / item['path']).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == item['sha256'], item['path']
    assert raw == (root / item['snapshot']).read_bytes(), item['path']
initial = dict(result='REVISE', reviewer='/root/review_directory_references_v1',
    input_manifest_sha256=hashlib.sha256(manifest_raw).hexdigest(), input_count=36,
    findings=[dict(id='QW01', line=867, reason='Retain outcome and binding while authorized lost-acknowledgement reconciliation remains permitted; stale expected revision alone cannot retire that receipt.'),
              dict(id='QW02', line=743, reason='Blanket local-part case preservation conflicts with installed email-validator RFC 2142 reserved mailbox normalization.')],
    evidence=dict(initial_and_final_input_identity='36 live/snapshot pairs matched',
                  schema_validator_methods_passed=37, email_observations_replayed=10,
                  preserved_prefix_bytes=51824),
    limits='Definition/schema review only; no implementation enforcement, production graph or integrated acceptance.')
dest = base / 'initial-independent-review.json'
assert not dest.exists()
dest.write_text(json.dumps(initial, indent=2) + '\n', encoding='utf-8')
path = root / 'docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md'
raw = path.read_bytes()
(out / 'INTERFACE_CATALOG.before-correction.md').write_bytes(raw)
(out / 'review-inputs.before-correction.json').write_bytes(manifest_raw)
old = ('normal form is compared only inside this authorized lineage; preserve local-part\n'
       'case and plus tags rather than applying provider-specific mailbox alias rules or\n'
       'joining people/histories by email. Do not retain an extra raw spelling by default.')
new = ('normal form is compared only inside this authorized lineage. Preserve ordinary\n'
       'local-part case and plus tags, with the candidate library\'s explicit exception:\n'
       'its RFC 2142 reserved mailbox names are normalized to lowercase (for example,\n'
       '`POSTMASTER@example.org` becomes `postmaster@example.org`). The installed\n'
       '`CASE_INSENSITIVE_MAILBOX_NAMES` set and normalization branch define this\n'
       'bounded exception; [RFC 2142 section 2](https://www.rfc-editor.org/rfc/rfc2142.html#section-2)\n'
       'specifies case-independent recognition of these well-known names. Do not add\n'
       'provider-specific mailbox alias rules, drop plus tags, lowercase every\n'
       'customer local part or join people/histories by email. Do not retain an extra\n'
       'raw spelling by default.')
old2 = ('reconciliation available. A retired operation must remain unable to apply again:\n'
        'retain minimal necessary suppression until its proof/expected-revision scope can\n'
        'no longer admit it. Store cleanup is not permission to forget ambiguity, reset a\n'
        'revision or reexecute an old intent. Each binding/copy inherits its approved\n'
        'purpose/expiry; hash representations are not automatically anonymous. Finite')
new2 = ('reconciliation available. Retain the admitted outcome and necessary private\n'
        'binding throughout the current purpose/expiry-permitted reconciliation window,\n'
        'so an authorized visitor can recover a lost acknowledgement. An applied write\n'
        'makes its expected revision stale immediately; that alone cannot retire its\n'
        'receipt. Receipt retirement is separate from non-reexecution suppression:\n'
        'retire only when the lawful reconciliation window ends, retaining the minimum\n'
        'necessary suppression while an old intent could otherwise be admitted again.\n'
        'Expired or revoked authority cannot retrieve or restore a receipt. Store\n'
        'cleanup cannot forget unresolved ambiguity, reset revisions, renew access or\n'
        'reexecute an old intent; it also cannot create indefinite personal history.\n'
        'Each outcome/binding/copy inherits its approved purpose/expiry; hashes are not\n'
        'automatically anonymous. Finite')
for before, after in [(old, new), (old2, new2)]:
    before_b = before.replace('\n', '\r\n').encode()
    after_b = after.replace('\n', '\r\n').encode()
    assert raw.count(before_b) == 1
    raw = raw.replace(before_b, after_b, 1)
prefix = (base / 'INTERFACE_CATALOG.before.md').read_bytes()
assert raw.startswith(prefix) and len(prefix) == 51824
path.write_bytes(raw)
print(json.dumps(dict(catalogue_sha256=hashlib.sha256(raw).hexdigest(),
                     prefix_bytes=len(prefix), corrected_findings=['QW01', 'QW02'])))
