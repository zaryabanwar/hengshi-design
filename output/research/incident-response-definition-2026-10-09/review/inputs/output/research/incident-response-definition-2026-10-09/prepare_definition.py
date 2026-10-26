from pathlib import Path
import hashlib, json

root = Path.cwd()
base = root / 'output/research/incident-response-definition-2026-10-09'
before_dir = base / 'before'
assert not before_dir.exists(), 'Do not overwrite frozen predecessor evidence.'
before_dir.mkdir()
security = root / 'docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md'
qa = root / 'docs/phase-1-architecture/contracts/QA_RECOVERY.md'
before_security, before_qa = security.read_bytes(), qa.read_bytes()
assert hashlib.sha256(before_security).hexdigest() == 'ab972920e58f7da3c0990b573e1e2a18121f4b6d7c57f8615b7e7e624e3cbec0'
(before_dir / security.name).write_bytes(before_security)
(before_dir / qa.name).write_bytes(before_qa)
old = '''Maintain breach assessment and records, containment and controller/processor
escalation. Notify the competent authority without undue delay and, where feasible,
within 72 hours of awareness unless unlikely to risk individuals; communicate to
affected people when the required high-risk threshold applies. Incomplete facts
do not authorize waiting for the entire investigation. This is a legal-response
obligation, not an advertised sales/support SLA. See [EDPB breach guidance](https://www.edpb.europa.eu/sme/assess-the-risks/data-breaches_en).
'''.replace('\n', '\r\n').encode()
new = '''The [incident response definition](#incident-assessment-escalation-and-recovery--v1)
binds detection, awareness, containment, assessment, applicable notification and
recovery. Legal-response duties are conditional on applicable law and actual
processing role; they are not an advertised support SLA or permission to send
reports. Dedicated alias ownership remains deferred under D-076.
'''.replace('\n', '\r\n').encode()
anchor = b'## Visitor proof encoding reference'
assert before_security.count(old) == 1 and before_security.count(anchor) == 1
section = (base / 'incident-section.md').read_text(encoding='utf-8').replace('\n', '\r\n').encode()
after_security = before_security.replace(old, new).replace(anchor, section + b'\r\n' + anchor, 1)
qa_section = (base / 'rehearsal-section.md').read_text(encoding='utf-8').replace('\n', '\r\n').encode()
after_qa = before_qa + b'\r\n' + qa_section
assert after_security.replace(new, old).replace(section + b'\r\n', b'', 1) == before_security
assert after_qa[:len(before_qa)] == before_qa
security.write_bytes(after_security)
qa.write_bytes(after_qa)
paths = [
    'AGENTS.md', '.specify/memory/constitution.md', 'DECISIONS.md', 'TASKS.md',
    'docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md',
    'docs/phase-1-architecture/contracts/QA_RECOVERY.md',
    'docs/phase-1-architecture/contracts/DATA_CONTRACT.md',
    'docs/phase-1-architecture/contracts/data-entities.csv',
    'docs/phase-1-architecture/contracts/reviews/eu-privacy-retention-v1-2026-10-07.md',
    'docs/software-definition/06-entity-and-public-contact.md',
    'output/research/rights-intake-2026-10-09/primary-sources.json',
    'output/research/rights-intake-2026-10-09/gdpr.raw.gz',
]
paths += [p.relative_to(root).as_posix() for p in base.iterdir() if p.is_file()]
paths += [p.relative_to(root).as_posix() for p in before_dir.iterdir()]
review = base / 'review'
inputs = []
for path in paths:
    raw = (root / path).read_bytes()
    target = review / 'inputs' / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(raw)
    inputs.append({'path': path, 'snapshot': target.relative_to(root).as_posix(), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
manifest = {'status': 'DOING', 'revision_cycle': 0, 'scope': 'Incident assessment and response definition plus future synthetic rehearsal scenarios; two canonical documents only', 'inputs': inputs}
target = review / 'review-inputs.json'
target.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'inputs':len(inputs),'manifest_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'security_bytes':len(after_security),'qa_bytes':len(after_qa),'exact_edit_scope':True}))
