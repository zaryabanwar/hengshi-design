"""Read-only installed library observations; no DNS/mail, install or app import."""
from pathlib import Path
import hashlib
import importlib.metadata as metadata
import json
import sys
import urllib.request

import email_validator
from email_validator import validate_email, EmailNotValidError

out = Path(__file__).resolve().parent
dest = out / 'email-observations.json'
assert not dest.exists()
options = dict(check_deliverability=False, allow_display_name=False,
               allow_quoted_local=False, allow_domain_literal=False,
               allow_empty_local=False, allow_smtputf8=True, strict=True,
               test_environment=False)
cases = ['User+tag@EXAMPLE.ORG', 'user@bücher.example.org', 'ü@example.org',
         ' user@example.org ', 'Name <user@example.org>', 'not-an-email',
         'user@example.org\r\nBcc: x@example.org', '"a b"@example.org',
         'user@[127.0.0.1]', 'a' * 65 + '@example.org']
observations = []
for value in cases:
    try:
        result = validate_email(value, **options)
        observations.append({'input': value, 'accepted': True,
                             'normalized': result.normalized,
                             'ascii_email': result.ascii_email,
                             'smtputf8': result.smtputf8})
    except EmailNotValidError as error:
        observations.append({'input': value, 'accepted': False,
                             'error_class': type(error).__name__})
with urllib.request.urlopen('https://pypi.org/pypi/email-validator/json', timeout=30) as response:
    registry = json.load(response)
version = registry['info']['version']
release = registry['releases'][version]
package_dir = Path(email_validator.__file__).parent
sources = []
for path in sorted(package_dir.glob('*.py')):
    raw = path.read_bytes()
    snap = out / 'email-source' / path.name
    snap.parent.mkdir(exist_ok=True)
    assert not snap.exists()
    snap.write_bytes(raw)
    sources.append({'path': str(path), 'snapshot': str(snap), 'bytes': len(raw),
                    'sha256': hashlib.sha256(raw).hexdigest()})
report = {'scope': 'Existing library syntax/normalization observations, not application enforcement or selected production graph',
          'python': sys.version, 'installed': metadata.version('email-validator'),
          'registry': {'source': 'https://pypi.org/pypi/email-validator/json',
                       'observed': '2026-10-08', 'latest': version,
                       'requires_python': registry['info']['requires_python'],
                       'requires_dist': registry['info']['requires_dist'],
                       'all_latest_files_not_yanked': all(not row['yanked'] for row in release)},
          'options': options, 'observations': observations, 'sources': sources,
          'network': 'Only official registry GET; no DNS deliverability check or SMTP/API delivery'}
dest.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({'installed': report['installed'], 'registry_latest': version,
                  'cases': len(observations), 'accepted': sum(c['accepted'] for c in observations),
                  'sources': len(sources)}))
