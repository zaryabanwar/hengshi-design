from pathlib import Path
import hashlib, json

root = Path.cwd()
base = root / 'output/research/incident-response-definition-2026-10-09'
receipt = base / 'review/independent-review-incident-response-v1.json'
assert hashlib.sha256(receipt.read_bytes()).hexdigest() == '75b1fcfc14653e8a193a1af7482a605ac5c07f760fe1377dd0416fd06326bc91'
assert json.loads(receipt.read_bytes())['verdict'] == 'REVISE'
prior = base / 'review/review-inputs.json'
manifest = json.loads(prior.read_bytes())
assert all((root / item['path']).read_bytes() == (root / item['snapshot']).read_bytes() for item in manifest['inputs'])
path = 'docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md'
p = root / path
before = p.read_bytes()
old = b'Individual communication\r\nuses clear language and useful protective advice with the required contact,\r\nconsequences and measures.'
new = b'Individual communication\r\nuses clear language to describe the nature of the breach and give useful\r\nprotective advice, with the required contact, consequences and measures.'
assert before.count(old) == 1
after = before.replace(old, new)
correction = base / 'review/correction-1'
assert not correction.exists(), 'Preserve existing correction evidence.'
correction.mkdir()
(correction / 'SECURITY_PRIVACY_CONTRACT.before.md').write_bytes(before)
p.write_bytes(after)
paths = [path, 'docs/phase-1-architecture/contracts/QA_RECOVERY.md',
         prior.relative_to(root).as_posix(), receipt.relative_to(root).as_posix(),
         (correction / 'SECURITY_PRIVACY_CONTRACT.before.md').relative_to(root).as_posix(),
         'output/research/rights-intake-2026-10-09/gdpr.raw.gz',
         (base / 'edpb-breach.raw.gz').relative_to(root).as_posix(),
         (base / 'prepare_correction.py').relative_to(root).as_posix()]
inputs = []
for rel in paths:
    raw = (root / rel).read_bytes()
    snap = correction / 'inputs' / rel
    snap.parent.mkdir(parents=True, exist_ok=True)
    snap.write_bytes(raw)
    inputs.append({'path': rel, 'snapshot': snap.relative_to(root).as_posix(), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
out = correction / 'review-inputs.json'
out.write_text(json.dumps({'status':'DOING','revision_cycle':1,'finding':'INCIDENT01','scope':'Individual communication nature-of-breach correction only; all earlier scope retained','inputs':inputs},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'inputs':len(inputs),'manifest_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'only_exact_paragraph_changed':after.replace(new,old)==before}))
