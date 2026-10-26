"""Metadata-only coexistence evaluation; installs no candidate package."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASIS = ROOT / 'output/research/staff-identity-graph-2026-10-08'
if (HERE / 'receipt.json').exists() or (HERE / 'pip-report.json').exists():
    raise SystemExit('Refuse repeat resolver experiment')
protected = json.loads((ROOT / 'output/research/backend-crypto-graph-2026-10-08/proposal.json').read_bytes())['protected_inputs_before']
sha = lambda raw: hashlib.sha256(raw).hexdigest()
before = {p: sha((ROOT / p).read_bytes()) for p in protected}
assert before == protected
roots = (BASIS / 'candidate-roots.txt').read_bytes() + b'httpx2==2.13.1\n'
(HERE / 'candidate-roots.txt').write_bytes(roots)
command = [ROOT / 'apps/api/.venv/Scripts/python.exe', '-B', '-m', 'pip', '--isolated',
           'install', '--dry-run', '--ignore-installed', '--only-binary=:all:', '--no-cache-dir',
           '--disable-pip-version-check', '--progress-bar', 'off', '--index-url', 'https://pypi.org/simple',
           '--report', HERE / 'pip-report.json', '-r', HERE / 'candidate-roots.txt']
free_before = shutil.disk_usage(ROOT).free
assert free_before > 1073741824 + 268435456
environment = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PIP_NO_CACHE_DIR='1',
                   PIP_DISABLE_PIP_VERSION_CHECK='1', PIP_CONFIG_FILE=os.devnull)
started = time.monotonic()
exit_code = None
with (HERE / 'stdout.txt').open('xb') as out, (HERE / 'stderr.txt').open('xb') as err:
    try:
        exit_code = subprocess.run(command, cwd=ROOT, env=environment, stdout=out, stderr=err,
                                   timeout=180, check=False).returncode
    except subprocess.TimeoutExpired:
        pass
after = {p: sha((ROOT / p).read_bytes()) for p in protected}
report = HERE / 'pip-report.json'
receipt = {'product_release': 'v1', 'status': 'DOING' if exit_code == 0 else 'BLOCKED',
           'scope': 'Unselected Windows metadata graph adding HTTPX2 only as a candidate TestClient dependency; no HTTPX/Authlib alias or substitution',
           'command': [str(x) for x in command], 'exit_code': exit_code, 'deadline_seconds': 180,
           'elapsed_seconds': round(time.monotonic() - started, 3), 'installation_performed': False,
           'basis_report_sha256': sha((BASIS / 'pip-report.json').read_bytes()),
           'roots_sha256': sha(roots), 'report_sha256': sha(report.read_bytes()) if report.exists() else None,
           'protected_inputs_before': before, 'protected_inputs_after': after, 'protected_inputs_unchanged': before == after,
           'free_disk_before_bytes': free_before, 'free_disk_after_bytes': shutil.disk_usage(ROOT).free,
           'limits': 'No native import/TestClient type/policy/OIDC/TLS/OS-trust behavior or complete latest-compatible stable graph/adoption proof; enlarged installation needs its own reviewed plan and approval.'}
(HERE / 'receipt.json').write_bytes((json.dumps(receipt, indent=2) + '\n').encode())
print(json.dumps({k:v for k,v in receipt.items() if not k.startswith('protected_inputs') and k!='command'}, indent=2))
if exit_code != 0 or before != after:
    raise SystemExit(1)
