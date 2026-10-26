"""Registry recheck and hashed research inputs; never install or select production."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import gzip
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import quote, urlsplit, unquote
from urllib.request import Request, urlopen

from packaging.utils import canonicalize_name
from packaging.version import Version, InvalidVersion

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / 'output/research/compatibility-resolution-2026-10-04/backend-windows/pip-report.json'
OUT = ROOT / 'output/research/backend-hash-inputs-2026-10-08'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def protect():
    paths = ('package.json', 'package-lock.json', 'apps/web/package.json',
             'apps/web/package-lock.json', 'apps/api/requirements.txt', 'apps/api/.venv/pyvenv.cfg')
    return {p: sha((ROOT / p).read_bytes()) if (ROOT / p).is_file() else None for p in paths}


def fetch(name, version=None):
    assert re.fullmatch(r'[a-z0-9][a-z0-9-]*', name)
    route = name + ('/' + quote(version, safe='') if version else '')
    url = 'https://pypi.org/pypi/' + route + '/json'
    request = Request(url, headers={'Accept': 'application/json',
                                   'User-Agent': 'Hengshi-Phase1-ReadOnly-Research/1'})
    with urlopen(request, timeout=20) as response:
        assert urlsplit(response.url).scheme == 'https' and urlsplit(response.url).hostname == 'pypi.org'
        raw = response.read(8 * 1024 * 1024 + 1)
        if len(raw) > 8 * 1024 * 1024:
            raise ValueError('Registry response exceeds research receive cap')
    data = json.loads(raw.decode('utf-8'))
    assert canonicalize_name(data['info']['name']) == name
    filename = name + ('-exact' if version else '-project') + '.json.gz'
    (OUT / 'primary' / filename).write_bytes(gzip.compress(raw, mtime=0))
    return data, {'url': url, 'observed_at': datetime.now(timezone.utc).isoformat(),
                  'raw_bytes': len(raw), 'raw_sha256': sha(raw), 'gzip_snapshot': 'primary/' + filename}


def inspect(record):
    name = canonicalize_name(record['metadata']['name'])
    version = record['metadata']['version']
    exact, source = fetch(name, version)
    url = record['download_info']['url']
    assert urlsplit(url).scheme == 'https' and urlsplit(url).hostname == 'files.pythonhosted.org'
    filename = unquote(urlsplit(url).path.rsplit('/', 1)[1])
    expected = record['download_info']['archive_info']['hashes']['sha256']
    assert re.fullmatch('[0-9a-f]{64}', expected)
    matches = [f for f in exact['urls'] if f['filename'] == filename and f['url'] == url]
    assert len(matches) == 1, (name, 'Exact recorded wheel absent or ambiguous')
    artifact = matches[0]
    assert artifact['digests']['sha256'] == expected, (name, 'Registry/report digest mismatch')
    assert artifact['packagetype'] == 'bdist_wheel' and not artifact['yanked'], (name, 'Artifact unavailable')
    parsed = Version(version)
    assert not parsed.is_prerelease and not parsed.is_devrelease
    project, latest_source = fetch(name)
    candidates = []
    for key, files in project['releases'].items():
        try:
            candidate = Version(key)
        except InvalidVersion:
            continue
        if not candidate.is_prerelease and not candidate.is_devrelease and any(not f.get('yanked') for f in files):
            candidates.append(candidate)
    assert candidates, name
    latest = str(max(candidates))
    extras = sorted(record.get('requested_extras', []))
    token = name + ('[' + ','.join(extras) + ']' if extras else '')
    requirement = token + '==' + version + ' --hash=sha256:' + expected
    return {'name': name, 'resolved_version': version, 'requested': bool(record.get('requested')),
            'requested_extras': extras, 'artifact_filename': filename, 'artifact_sha256': expected,
            'artifact_size': artifact['size'], 'exact_artifact_unyanked': True,
            'latest_non_preview_registry_observation': latest,
            'newer_release_observed': Version(latest) > parsed,
            'latest_is_not_a_selected_compatible_version': True,
            'requires_python': exact['info'].get('requires_python'),
            'maturity_classifiers': [x for x in exact['info'].get('classifiers', []) if x.startswith('Development Status')],
            'requirement': requirement, 'exact_source': source, 'project_source': latest_source}


def main():
    OUT.mkdir(exist_ok=False)
    (OUT / 'primary').mkdir()
    before = protect()
    raw = REPORT.read_bytes()
    assert sha(raw) == 'b9a135fa96ee978af2011ea4e4b8f848fd44235db46349caed74cc61ecc2c8f6'
    report = json.loads(raw.decode('utf-8'))
    assert report['version'] == '1' and len(report['install']) == 40
    names = [canonicalize_name(r['metadata']['name']) for r in report['install']]
    assert len(set(names)) == len(names)
    results, errors = [], []
    with ThreadPoolExecutor(max_workers=4) as pool:
        tasks = {pool.submit(inspect, record): record['metadata']['name'] for record in report['install']}
        for future in as_completed(tasks):
            try:
                results.append(future.result())
            except Exception as exc:
                errors.append({'name': tasks[future], 'error_type': type(exc).__name__, 'message': str(exc)[:250]})
    results.sort(key=lambda r: r['name'])
    after = protect()
    assert before == after, 'Protected application input changed during read-only registry study'
    receipt = {'status': 'DOING', 'scope': 'Exact October4 Windows CPython3.14.5 mixed runtime/test resolver study; research requirements only',
               'production_selection': False, 'install_performed': False, 'dry_run_replay_performed': False,
               'source_report_sha256': sha(raw), 'source_environment': report['environment'],
               'source_pip_version': report['pip_version'], 'protected_inputs_before': before,
               'protected_inputs_after': after, 'registry_results': results, 'errors': errors,
               'limits': ['No wheel content downloaded or verified against bytes',
                          'Registry hashes and compressed response identity are not publisher attestations',
                          'No imported/native ABI, API, database, license or security qualification',
                          'No production OS/provider selection or production/dev graph separation',
                          'Independently newer versions are observations, not the selected graph',
                          'No selected production lock or compatibility acceptance'],
               'primary_documentation': ['https://pip.pypa.io/en/stable/topics/secure-installs/',
                                         'https://pip.pypa.io/en/stable/reference/installation-report/']}
    if not errors:
        header = ['# Research only: NOT a selected or tested production lock.',
                  '# Exact October4 Windows CPython3.14.5 wheel graph; not portable to other platforms.',
                  '# Mixed runtime/test families; preserve uvicorn standard and psycopg binary extras.',
                  '# Replay requires --require-hashes --only-binary=:all:; no install is authorized here.',
                  '# New registry versions are recorded separately and require a coupled graph re-evaluation.']
        lock = OUT / 'windows-study-hashed-requirements.txt'
        lock.write_text('\n'.join(header + [r['requirement'] for r in results]) + '\n', encoding='utf-8')
        receipt['research_requirements_sha256'] = sha(lock.read_bytes())
    (OUT / 'registry-recheck.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'completed_registry_checks': len(results), 'errors': errors,
                      'newer_observations': [(r['name'], r['resolved_version'], r['latest_non_preview_registry_observation'])
                                             for r in results if r['newer_release_observed']],
                      'protected_inputs_unchanged': before == after,
                      'production_selection': False}, indent=2), flush=True)
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
