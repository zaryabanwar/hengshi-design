"""Retain an actual closed-error schema failure, fix it, then run affected checks."""
from pathlib import Path
import json
import os
import subprocess
import sys

from scripts.validation.test_booking_creation_response_schema import BookingCreationResponseShapeTests

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
PATH = ROOT / 'docs/phase-1-architecture/contracts/booking-creation-response.schema.json'
if (OUT / 'response-schema-before-local-fix.json').exists():
    raise RuntimeError('Refusing overwrite')
(OUT / 'response-schema-before-local-fix.json').write_bytes(PATH.read_bytes())
BookingCreationResponseShapeTests.setUpClass()
value = {'state': 'unavailable', 'code': 'INVALID_REQUEST', 'recovery': 'correct_request'}
errors = list(BookingCreationResponseShapeTests.validator.iter_errors(value))
if not errors:
    raise RuntimeError('Expected original closed-error failure not reproduced')
(OUT / 'closed-error-failure.json').write_text(json.dumps({'instance': value,
    'errors': [error.message for error in errors],
    'cause': 'The error object declared only state in properties while additionalProperties=false; code and recovery were accidentally closed out.'}, indent=2) + '\n')
schema = json.loads(PATH.read_text())
schema['$defs']['error']['properties'].update({'code': {'type': 'string'},
                                            'recovery': {'type': 'string'}})
PATH.write_bytes((json.dumps(schema, indent=2) + '\n').replace('\n', '\r\n').encode())
environment = {key: value for key, value in os.environ.items()
               if key in ('SYSTEMROOT', 'WINDIR', 'PATH', 'PATHEXT', 'TEMP', 'TMP', 'USERPROFILE')}
environment.update({'PYTHONUTF8': '1', 'PYTHONDONTWRITEBYTECODE': '1',
                    'PYTHONNOUSERSITE': '1', 'PYTHONPATH': str(ROOT)})
command = [sys.executable, '-m', 'unittest',
           'scripts.validation.test_booking_creation_response_schema',
           'scripts.validation.test_booking_creation_request_schema',
           'scripts.validation.test_process_value_schema', '-v']
result = subprocess.run(command, cwd=ROOT, env=environment, capture_output=True,
                        encoding='utf-8', timeout=60)
(OUT / 'validator-results.json').write_text(json.dumps({'command': command,
    'exit_code': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr,
    'scope': 'Actual jsonschema boundary only; no application HTTP/auth/promotion/lifetime enforcement.'}, indent=2) + '\n')
print(result.stderr)
raise SystemExit(result.returncode)
