"""Prospective 48-wheel runner; invoke only after explicit new founder approval."""
import hashlib
import json
import os
import re
import sys
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import time
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PLAN_PATH = HERE / 'qualification-plan.json'
PLAN = json.loads(PLAN_PATH.read_bytes())
TRIAL = ROOT / PLAN['target']
BASE_PYTHON = ROOT / 'apps/api/.venv/Scripts/python.exe'
BUDGET = PLAN['limits']['new_output_budget_bytes']
FLOOR = PLAN['limits']['minimum_free_disk_bytes']
DEADLINE = PLAN['limits']['command_deadline_seconds']
PIN_FILE = HERE / PLAN['candidate']
PROBE = ROOT / PLAN['probe_files'][0]['path']
EXTRA_PROBE = ROOT / PLAN['probe_files'][1]['path']
ENVIRONMENT = dict(os.environ, PYTHONDONTWRITEBYTECODE='1',
                   PYTEST_DISABLE_PLUGIN_AUTOLOAD='1', PIP_NO_CACHE_DIR='1',
                   PIP_DISABLE_PIP_VERSION_CHECK='1')
PROTECTED = json.loads((HERE / 'receipt.json').read_bytes())['protected_inputs_before']
STEPS = []


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def footprint():
    return sum(p.stat().st_size for p in TRIAL.rglob('*') if p.is_file()) if TRIAL.exists() else 0


def measure():
    return {'retained_bytes': footprint(), 'free_disk_bytes': shutil.disk_usage(ROOT).free}


def admit(remaining=0):
    reading = measure()
    if reading['retained_bytes'] + remaining > BUDGET or reading['free_disk_bytes'] < FLOOR + remaining:
        raise RuntimeError('Research disk budget/reserve admission failed: ' + json.dumps(reading))
    return reading


def protected_unchanged():
    return all(sha((ROOT / p).read_bytes()) == h for p, h in PROTECTED.items())


def write_json(path, data):
    path.write_bytes((json.dumps(data, indent=2) + '\n').encode())


def run(label, command):
    before = admit()
    print(label, flush=True)
    start = time.monotonic()
    record = {'step': label, 'command': [str(x) for x in command], 'before': before}
    try:
        with (TRIAL / (label + '.stdout.txt')).open('wb') as stdout, (TRIAL / (label + '.stderr.txt')).open('wb') as stderr:
            process = subprocess.run(command, cwd=TRIAL, env=ENVIRONMENT, stdout=stdout, stderr=stderr,
                                     timeout=DEADLINE, check=False)
        record['exit_code'] = process.returncode
    except subprocess.TimeoutExpired:
        record['timeout'] = True
        record['exit_code'] = None
    finally:
        record['elapsed_seconds'] = round(time.monotonic() - start, 3)
        record['after'] = measure()
        STEPS.append(record)
        write_json(TRIAL / 'commands.json', STEPS)
    admit()
    if record['exit_code'] != 0:
        raise RuntimeError('Command failed or exceeded deadline: ' + label)


if len(sys.argv) != 2 or not sys.argv[1].strip():
    raise SystemExit('Explicit actual founder approval text argument required; no execution permission is inferred')
if TRIAL.exists():
    raise SystemExit('Refuse existing trial target')
if not protected_unchanged():
    raise SystemExit('Protected manifest/lock/runtime changed before execution')
review_inputs = json.loads((HERE / 'review-inputs.json').read_bytes())
plan_input = next(x for x in review_inputs['inputs'] if x['path'] == PLAN_PATH.relative_to(ROOT).as_posix())
for entry in PLAN['probe_files']:
    if sha((ROOT / entry['path']).read_bytes()) != entry['sha256']:
        raise SystemExit('Reviewed probe file changed')
if sha(PLAN_PATH.read_bytes()) != plan_input['sha256'] or sha(PIN_FILE.read_bytes()) != PLAN['candidate_sha256']:
    raise SystemExit('Reviewed plan or exact candidate changed')
if shutil.disk_usage(ROOT).free <= BUDGET + FLOOR:
    raise SystemExit('Insufficient disk for complete trial allowance and free reserve')
TRIAL.mkdir()
write_json(TRIAL / 'authorization.json', {'product_release': 'v1', 'status': 'DOING',
           'founder_approval': sys.argv[1], 'approved_package_count': 48,
           'plan_sha256': sha(PLAN_PATH.read_bytes()), 'requirements_sha256': sha(PIN_FILE.read_bytes()),
           'probe_sha256': sha(PROBE.read_bytes()), 'protected_inputs_before': PROTECTED,
           'limits': PLAN['limits'], 'frozen_plan_retained': True})
result = {'product_release': 'v1', 'status': 'DOING', 'qualification': 'not_finished',
          'scope': 'Isolated 48-wheel library/type/lifecycle coupling only; no actual Hengshi route, OIDC flow, database/provider/TLS or stack adoption',
          'limits': ['Admission and boundary checks are not an OS-enforced disk quota.',
                     'Synthetic library tests do not prove application identity, authorization, PostgreSQL, OIDC, provider delivery, load or recovery.',
                     'Independent results review, complete latest-compatible graph/provenance/licences/locks and founder adoption remain separate.']}
try:
    run('01-host-identity', [BASE_PYTHON, '-B', '-c',
        'import sys,pip,json; assert sys.version_info[:3]==(3,14,5); assert pip.__version__=="26.1.1"; print(json.dumps({"python":sys.version,"pip":pip.__version__}))'])
    env_path = TRIAL / 'environment'
    run('02-create-pipless-venv', [BASE_PYTHON, '-B', '-m', 'venv', '--without-pip', env_path])
    python = env_path / 'Scripts/python.exe'
    wheels = TRIAL / 'wheelhouse'; wheels.mkdir()
    run('03-download-exact-wheels', [BASE_PYTHON, '-B', '-m', 'pip', '--isolated', 'download',
        '--require-hashes', '--only-binary=:all:', '--no-deps', '--no-cache-dir', '--disable-pip-version-check',
        '--progress-bar', 'off', '--index-url', 'https://pypi.org/simple', '--dest', wheels, '-r', PIN_FILE])
    expected = json.loads((HERE / 'closure-observations.json').read_bytes())['package_records']
    if len(expected) != 48 or {x['wheel'] for x in expected} != {p.name for p in wheels.iterdir()}:
        raise RuntimeError('Downloaded file set differs from frozen 48-wheel inventory')
    inventory = []
    for entry in expected:
        wheel = wheels / entry['wheel']; raw = wheel.read_bytes()
        if len(raw) != entry['bytes'] or sha(raw) != entry['sha256']:
            raise RuntimeError('Wheel size/hash mismatch: ' + wheel.name)
        with zipfile.ZipFile(wheel) as archive:
            items = archive.infolist(); names = [x.filename for x in items]
            if len(set(names)) != len(names):
                raise RuntimeError('Duplicate wheel entries')
            if any(PurePosixPath(n).is_absolute() or '..' in PurePosixPath(n).parts or '\\' in n for n in names):
                raise RuntimeError('Unexpected archive path')
            expanded = sum(x.file_size for x in items)
        inventory.append({'wheel': wheel.name, 'bytes': len(raw), 'sha256': sha(raw), 'expanded_declared_bytes': expanded})
    expanded = sum(x['expanded_declared_bytes'] for x in inventory)
    write_json(TRIAL / 'wheel-inspection.json', inventory)
    remaining = 2 * expanded + PLAN['limits']['additional_installer_output_reservation_bytes']
    admission = admit(remaining)
    write_json(TRIAL / 'installation-admission.json', {**admission, 'expanded_wheel_bytes': expanded,
        'remaining_reserved_bytes': remaining, 'conservative_total_bytes': admission['retained_bytes'] + remaining,
        'budget_bytes': BUDGET, 'free_floor_bytes': FLOOR, 'os_hard_quota': False})
    run('04-offline-install', [BASE_PYTHON, '-B', '-m', 'pip', '--isolated', '--python', python, 'install',
        '--no-index', '--find-links', wheels, '--require-hashes', '--only-binary=:all:', '--no-deps',
        '--no-cache-dir', '--no-compile', '--disable-pip-version-check', '--progress-bar', 'off', '-r', PIN_FILE])
    run('05-pip-check', [BASE_PYTHON, '-B', '-m', 'pip', '--isolated', '--python', python, 'check', '--disable-pip-version-check'])
    run('06-installed-identities', [python, '-B', '-c',
        'import importlib.metadata as m,json; from pathlib import Path; d={x.metadata["Name"].lower():x.version for x in m.distributions()}; Path("installed-identities.json").write_text(json.dumps(d,sort_keys=True,indent=2)+"\\n"); print(json.dumps(d,sort_keys=True))'])
    identities = json.loads((TRIAL / 'installed-identities.json').read_bytes())
    normalize = lambda name: re.sub(r'[-_.]+', '-', name).lower()
    actual = {normalize(k): v for k, v in identities.items()}
    desired = {normalize(x['name']): x['version'] for x in expected}
    if len(identities) != 48 or len(actual) != 48 or len(desired) != 48 or actual != desired:
        raise RuntimeError('Installed identities differ from frozen candidate')
    config = TRIAL / 'pytest.ini'
    config.write_text('[pytest]\nasyncio_mode = strict\nasyncio_default_fixture_loop_scope = function\n', encoding='utf-8')
    run('07-library-probes', [python, '-B', HERE / 'run_probes.py', '-c', config, '--noconftest',
        '-p', 'no:cacheprovider', '-p', 'pytest_asyncio.plugin', '-q', '--junitxml', TRIAL / 'library-probes.xml', PROBE, EXTRA_PROBE])
    run('08-native-libpq-identity', [python, '-B', '-c',
        'from psycopg import pq; import json; print(json.dumps({"implementation":pq.__impl__,"runtime_libpq":pq.version(),"build_libpq":pq.__build_version__}))'])
    result['qualification'] = 'PASS_synthetic_library_boundaries'
    result['package_count'] = 48
except Exception as error:
    result['status'] = 'BLOCKED'
    result['qualification'] = 'stopped_on_failure'
    result['error'] = str(error)
finally:
    result['measurements'] = measure()
    result['protected_inputs_unchanged'] = protected_unchanged()
    result['steps'] = len(STEPS)
    write_json(TRIAL / 'receipt.json', result)
    print(json.dumps(result, indent=2), flush=True)
if result['qualification'] != 'PASS_synthetic_library_boundaries' or not result['protected_inputs_unchanged']:
    raise SystemExit(1)
