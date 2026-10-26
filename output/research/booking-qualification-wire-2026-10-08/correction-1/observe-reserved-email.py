"""Read-only synthetic normalization observations; no DNS, mail or app import."""
from pathlib import Path
import importlib.metadata
import json
from email_validator import validate_email
from email_validator.rfc_constants import CASE_INSENSITIVE_MAILBOX_NAMES

out = Path(__file__).parent / 'reserved-email-observations.json'
assert not out.exists()
options = dict(check_deliverability=False, allow_display_name=False,
               allow_quoted_local=False, allow_domain_literal=False,
               allow_empty_local=False, allow_smtputf8=True, strict=True,
               test_environment=False)
values = [name.upper() + '@EXAMPLE.ORG' for name in CASE_INSENSITIVE_MAILBOX_NAMES]
values += ['Customer+TAG@EXAMPLE.ORG', 'POSTMASTER+TAG@EXAMPLE.ORG']
rows = []
for value in values:
    result = validate_email(value, **options)
    rows.append(dict(input=value, normalized=result.normalized,
                     ascii_email=result.ascii_email, smtputf8=result.smtputf8))
report = dict(scope='Installed library observations only; no application enforcement or selected production graph',
              installed=importlib.metadata.version('email-validator'),
              options=options, reserved_names=CASE_INSENSITIVE_MAILBOX_NAMES,
              observations=rows, network='No network access or delivery')
out.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps(dict(cases=len(rows), version=report['installed'])))
