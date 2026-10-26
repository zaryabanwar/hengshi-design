"""Freeze proposed wire/profile and validator evidence, not application readiness."""
from pathlib import Path
from datetime import datetime, timezone
from urllib.request import Request, urlopen
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
PROOF = ROOT / 'docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md'
SCHEMA = ROOT / 'docs/phase-1-architecture/contracts/booking-creation-response.schema.json'
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def save(name, data):
    with (OUT / name).open('x', encoding='utf-8') as file:
        json.dump(data, file, indent=2)
        file.write('\n')
if (OUT / 'review-inputs.json').exists():
    raise RuntimeError('Refusing overwrite')
guards = json.loads((ROOT / 'output/research/world-measurement-profile-2026-10-06/protected-before.json').read_text())
for row in guards:
    if row['path'] != 'PROJECT_STATE.yaml' and sha(ROOT / row['path']) != row['sha256']:
        raise RuntimeError('Protected input changed: ' + row['path'])
current = [{'path': row['path'], 'sha256': sha(ROOT / row['path'])} for row in guards]
save('protected-before.json', current)
# Pre-existing logical proposal retained as an exact byte prefix.
if not PROOF.read_bytes().startswith((OUT / 'PRIVATE_PROCESS_PROOF.md.before').read_bytes()):
    raise RuntimeError('Predecessor changed')
for path in (PROOF, SCHEMA):
    (OUT / (path.name + '.reviewed')).write_bytes(path.read_bytes())
urls = {
    'fastapi-cookies': 'https://fastapi.tiangolo.com/advanced/response-cookies/',
    'mdn-set-cookie': 'https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie',
    'owasp-csrf': 'https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html',
    'owasp-session': 'https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html',
    'rfc6265': 'https://www.rfc-editor.org/rfc/rfc6265.html',
    'rfc9110': 'https://www.rfc-editor.org/rfc/rfc9110.html',
}
rows = []
for name, url in urls.items():
    try:
        with urlopen(Request(url, headers={'User-Agent': 'Hengshi-definition-research/1.0'}), timeout=15) as response:
            data = response.read(4 * 1024 * 1024)
            path = OUT / (name + '.html')
            path.write_bytes(data)
            rows.append({'name': name, 'url': url, 'final_url': response.url,
                         'status': response.status, 'bytes': len(data), 'sha256': sha(path)})
    except Exception as error:
        rows.append({'name': name, 'url': url, 'error_type': type(error).__name__,
                     'error': str(error), 'scope': 'Failed direct saved retrieval; web observations are separate.'})
save('source-observations.json', {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
    'context7_library': '/websites/fastapi_tiangolo', 'sources': rows,
    'scope': 'Primary primitives/constraints only; numerical/security/operating profile is a proposed Hengshi definition, unimplemented and unmeasured.'})
paths = {ROOT / row['path'] for row in current}
paths.update(ROOT / ('docs/phase-1-architecture/contracts/' + name) for name in
    ('PRIVATE_PROCESS_PROOF.md', 'booking-creation-response.schema.json',
     'booking-creation-request.schema.json', 'process-value.schema.json',
     'publication-preparation.schema.json', 'publication-manifest.schema.json',
     'DATA_CONTRACT.md', 'SECURITY_PRIVACY_CONTRACT.md', 'INTERFACE_CATALOG.md',
     'interface-catalog.csv', 'process-fields.csv', 'data-classification.csv'))
paths.update(ROOT / ('scripts/validation/' + name) for name in
    ('test_booking_creation_response_schema.py', 'test_booking_creation_request_schema.py',
     'test_process_value_schema.py'))
paths.update(ROOT / path for path in ('TASKS.md', 'DECISIONS.md',
    'docs/phase-1-foundation/01-product-requirements.md',
    'specs/001-platform-security-hardening/spec.md'))
paths.update(path for path in OUT.iterdir() if path.is_file())
packet = [{'path': path.relative_to(ROOT).as_posix(), 'sha256': sha(path)}
          for path in sorted(paths, key=lambda value: value.as_posix())]
save('review-inputs.json', packet)
print(json.dumps({'inputs': len(packet), 'packet_sha256': sha(OUT / 'review-inputs.json'),
                  'guards_match': len(current), 'prose_or_runtime_tests': False}))
