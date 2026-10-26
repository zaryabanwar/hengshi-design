"""Freeze proposed definition inputs; this does not test application behavior."""
from pathlib import Path
import hashlib
import json
import re

root = Path.cwd()
out = root / 'output/research/booking-email-ownership-2026-10-08'
catalogue = root / 'docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md'
raw = catalogue.read_bytes()
prefix = (out / 'INTERFACE_CATALOG.before.md').read_bytes()
assert raw.startswith(prefix)
assert hashlib.sha256(prefix).hexdigest() == 'b86c2c3a56028b9c7e928e131ca7a06e818853f2c9a5a7ad9e4eb1e2164c5497'
appendix = raw[len(prefix):].decode('utf-8')
links = []
for target in re.findall(r'\]\(([^)]+)\)', appendix):
    if target.startswith('https://'):
        continue
    path_part = target.split('#')[0]
    resolved = (catalogue.parent / path_part).resolve()
    assert resolved.is_file(), target
    links.append(target)
sources = dict(checked='2026-10-08', context7='/python/cpython',
    scope='Official primary guidance and builtin primitive documentation, not prescribed Hengshi numerical limits or production graph selection',
    urls=['https://docs.python.org/3/library/secrets.html',
          'https://docs.python.org/3/library/hmac.html',
          'https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html',
          'https://pages.nist.gov/800-63-4/sp800-63b/authenticators/',
          'https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html',
          'https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html'],
    inspection=dict(prior_prefix_bytes=len(prefix), relative_links_resolve=links,
                    runtime_tests='None; logical definition only'))
source_path=out / 'primary-sources.json'
assert not source_path.exists()
source_path.write_text(json.dumps(sources, indent=2)+'\n', encoding='utf-8')
paths=['AGENTS.md', '.specify/memory/constitution.md', 'PROJECT.md', 'DECISIONS.md',
       'TASKS.md', 'MANUAL_ACTIONS.md',
       'docs/phase-1-ux-architecture/FLOWS.md',
       'docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md',
       'docs/phase-1-architecture/contracts/interface-catalog.csv',
       'docs/phase-1-architecture/contracts/process-fields.csv',
       'docs/phase-1-architecture/contracts/DATA_CONTRACT.md',
       'docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md',
       'docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md',
       'docs/phase-1-architecture/contracts/booking-status-response.schema.json',
       'docs/phase-1-architecture/contracts/booking-qualification.schema.json',
       'specs/001-platform-security-hardening/spec.md',
       'docs/phase-1-foundation/01-product-requirements.md',
       'output/research/booking-qualification-wire-2026-10-08/final-independent-review.json',
       str(source_path.relative_to(root)).replace('\\','/')]
snaps=out/'snapshots'; snaps.mkdir(exist_ok=False)
rows=[]
for i, name in enumerate(paths):
    path=root/name; data=path.read_bytes(); snap=snaps/f'{i:02d}-{path.name}'
    snap.write_bytes(data)
    rows.append(dict(path=name,snapshot=str(snap.relative_to(root)).replace('\\','/'),
                     bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
report=dict(scope='IF-BOOK-03/04 logical email ownership proposal; no wire freeze, implementation or integrated acceptance',
            inputs=rows, prefix=dict(path=str((out/'INTERFACE_CATALOG.before.md').relative_to(root)).replace('\\','/'),
                                     bytes=len(prefix),sha256=hashlib.sha256(prefix).hexdigest()))
dest=out/'review-inputs.json'; assert not dest.exists()
data=(json.dumps(report,indent=2)+'\n').encode(); dest.write_bytes(data)
print(json.dumps(dict(inputs=len(rows),manifest_sha256=hashlib.sha256(data).hexdigest(),
                     catalogue_sha256=hashlib.sha256(raw).hexdigest(),prefix_bytes=len(prefix),
                     relative_links=len(links))))
