"""Continue only unexecuted approved probes after a name-comparison harness error.

No download, installation, environment replacement or original receipt overwrite.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TRIAL = HERE / 'native-trial'
PLAN = json.loads((HERE / 'qualification-plan.json').read_bytes())
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTEST_DISABLE_PLUGIN_AUTOLOAD='1',
           PIP_NO_CACHE_DIR='1', PIP_DISABLE_PIP_VERSION_CHECK='1')
PROTECTED = json.loads((HERE / 'proposal.json').read_bytes())['protected_inputs_before']
STEPS = []


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, value):
    path.write_bytes((json.dumps(value, indent=2) + '\n').encode())


def reading():
    return {'retained_bytes': sum(p.stat().st_size for p in TRIAL.rglob('*') if p.is_file()),
            'free_disk_bytes': shutil.disk_usage(ROOT).free}


def protected():
    return all(digest(ROOT / p) == h for p, h in PROTECTED.items())


def admit():
    value = reading()
    if value['retained_bytes'] > PLAN['limits']['new_output_budget_bytes'] or value['free_disk_bytes'] < PLAN['limits']['minimum_free_disk_bytes']:
        raise RuntimeError('Disk budget/free floor exceeded')
    return value


def command(label, args):
    item = {'step': label, 'command': [str(a) for a in args], 'before': admit()}
    print(label, flush=True)
    started = time.monotonic()
    try:
        with (TRIAL / (label + '.stdout.txt')).open('xb') as out, (TRIAL / (label + '.stderr.txt')).open('xb') as err:
            item['exit_code'] = subprocess.run(args, cwd=TRIAL, env=ENV, stdout=out, stderr=err,
                                               timeout=PLAN['limits']['command_deadline_seconds'], check=False).returncode
    except subprocess.TimeoutExpired:
        item.update(exit_code=None, timeout=True)
    finally:
        item.update(elapsed_seconds=round(time.monotonic() - started, 3), after=reading())
        STEPS.append(item)
        write(TRIAL / 'continuation-commands.json', STEPS)
    admit()
    if item.get('exit_code') != 0:
        raise RuntimeError('Approved remaining probe failed: ' + label)


if (TRIAL / 'continuation-receipt.json').exists() or (TRIAL / 'continuation-correction.json').exists():
    raise SystemExit('Refuse repeat continuation')
original = json.loads((TRIAL / 'receipt.json').read_bytes())
authorization = json.loads((TRIAL / 'authorization.json').read_bytes())
steps = json.loads((TRIAL / 'commands.json').read_bytes())
if original.get('error') != 'Installed identities differ from frozen candidate' or len(steps) != 6 or any(s.get('exit_code') != 0 for s in steps):
    raise SystemExit('Not the diagnosed harness-only stop')
if not protected() or digest(HERE / 'qualification-plan.json') != authorization['plan_sha256'] or digest(HERE / PLAN['candidate']) != PLAN['candidate_sha256'] or digest(HERE / 'native-probes/test_libraries.py') != authorization['probe_sha256']:
    raise SystemExit('Frozen/protected inputs changed')
actual = json.loads((TRIAL / 'installed-identities.json').read_bytes())
expected = json.loads((HERE / 'closure-observations.json').read_bytes())['package_records']
normalize = lambda name: re.sub(r'[-_.]+', '-', name).lower()
a = {normalize(k): v for k, v in actual.items()}
e = {normalize(x['name']): x['version'] for x in expected}
if len(actual) != 43 or len(a) != 43 or len(expected) != 43 or len(e) != 43 or a != e:
    raise SystemExit('Actual canonical package/version mismatch; do not continue')
admit()
write(TRIAL / 'continuation-correction.json', {
    'product_release': 'v1', 'status': 'DOING', 'founder_approval': authorization['founder_approval'],
    'scope': 'Remaining original approved synthetic probes; no reinstall or dependency selection',
    'cause': 'Runner lowercased names without the mandated separator normalization',
    'observed_aliases': ['pydantic_core == pydantic-core', 'typing_extensions == typing-extensions'],
    'reference': 'https://packaging.python.org/en/latest/specifications/name-normalization/',
    'exact_normalized_package_versions_match': True, 'original_receipt_sha256': digest(TRIAL / 'receipt.json'),
    'original_commands_sha256': digest(TRIAL / 'commands.json'), 'script_sha256': digest(Path(__file__)),
    'plan_unchanged': True, 'candidate_unchanged': True, 'probes_unchanged': True})
result = {'product_release': 'v1', 'status': 'DOING', 'qualification': 'not_finished',
          'scope': original['scope'], 'limits': original['limits'], 'package_count': 43,
          'prior_harness_failure_preserved': True, 'downloads_or_installs_repeated': False}
try:
    python = TRIAL / 'environment/Scripts/python.exe'
    config = TRIAL / 'pytest.ini'
    with config.open('x', encoding='utf-8') as file:
        file.write('[pytest]\nasyncio_mode = strict\nasyncio_default_fixture_loop_scope = function\n')
    command('07-library-probes', [python, '-B', '-m', 'pytest', '-c', config, '--noconftest',
            '-p', 'no:cacheprovider', '-p', 'pytest_asyncio.plugin', '-q', '--junitxml', TRIAL / 'library-probes.xml',
            HERE / 'native-probes/test_libraries.py'])
    command('08-native-libpq-identity', [python, '-B', '-c',
            'from psycopg import pq; import json; print(json.dumps({"implementation":pq.__impl__,"runtime_libpq":pq.version(),"build_libpq":pq.__build_version__}))'])
    result['qualification'] = 'PASS_synthetic_library_boundaries'
except Exception as error:
    result.update(status='BLOCKED', qualification='stopped_on_failure', error=str(error))
finally:
    result.update(measurements=reading(), protected_inputs_unchanged=protected(), continuation_steps=len(STEPS))
    write(TRIAL / 'continuation-receipt.json', result)
    print(json.dumps(result, indent=2), flush=True)
if result['qualification'] != 'PASS_synthetic_library_boundaries' or not result['protected_inputs_unchanged']:
    raise SystemExit(1)
