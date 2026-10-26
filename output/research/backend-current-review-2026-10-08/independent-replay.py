"""Read-only replay of frozen registry/source metadata; never installs or fetches."""
from pathlib import Path
import gzip
import hashlib
import json
import re
import sys
import tomllib
from urllib.parse import unquote, urlsplit
from packaging.requirements import Requirement
from packaging.specifiers import SpecifierSet
from packaging.tags import sys_tags
from packaging.utils import canonicalize_name, parse_wheel_filename
from packaging.version import Version

ROOT = Path(__file__).resolve().parent
manifest = json.loads((ROOT / 'review-inputs.json').read_text(encoding='utf-8'))
paths = {i['path']: Path(i['snapshot']) for i in manifest['inputs']}
P = 'output/research/backend-hash-inputs-2026-10-08/'

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def read(name):
    return paths[name].read_bytes()

def obj(name):
    return json.loads(read(name))

for i in manifest['inputs']:
    raw = read(i['path'])
    assert len(raw) == i['bytes'] and sha(raw) == i['sha256'], i['path']
    assert sha(Path(i['path']).read_bytes()) == i['sha256'], i['path']

oldpath = 'output/research/compatibility-resolution-2026-10-04/backend-windows/pip-report.json'
old, report = obj(oldpath), obj(P + 'latest-coupled-resolution/pip-report.json')
completed = obj(P + 'completed-registry-recheck.json')
original = obj(P + 'registry-recheck.json')
summary = obj(P + 'latest-coupled-resolution/closure-observations.json')
assert sha(read(oldpath)) == completed['source_report_sha256']
assert sha(read(P + 'latest-coupled-resolution/pip-report.json')) == summary['report_sha256']
assert len(old['install']) == len(report['install']) == 40
assert len(original['registry_results']) == 39 and len(original['errors']) == 1
assert len(completed['registry_results']) == 40 and completed['errors'] == []
assert completed['initial_refusal_preserved'] is True
raw_responses = []
project_data = {}
oldrecords = {canonicalize_name(x['metadata']['name']): x for x in old['install']}
for row in completed['registry_results']:
    n = canonicalize_name(row['name'])
    prior = oldrecords[n]
    assert row['resolved_version'] == prior['metadata']['version']
    sources = {}
    for field in ('exact_source', 'project_source'):
        receipt = row[field]
        raw = gzip.decompress(read(P + receipt['gzip_snapshot']))
        assert len(raw) == receipt['raw_bytes'] and sha(raw) == receipt['raw_sha256']
        sources[field] = json.loads(raw)
        raw_responses.append({'name': n, 'kind': field, 'bytes': len(raw), 'sha256': sha(raw)})
    exact, project = sources['exact_source'], sources['project_source']
    project_data[n] = project
    assert exact['info']['version'] == row['resolved_version']
    filename = unquote(urlsplit(prior['download_info']['url']).path).rsplit('/', 1)[-1]
    matches = [f for f in exact['urls'] if f['filename'] == filename]
    assert len(matches) == 1
    f = matches[0]
    assert f['url'] == prior['download_info']['url'] and not f['yanked']
    assert f['digests']['sha256'] == prior['download_info']['archive_info']['hashes']['sha256'] == row['artifact_sha256']
    assert f['size'] == row['artifact_size']
    stable = [Version(v) for v, files in project['releases'].items()
              if not Version(v).is_prerelease and not Version(v).is_devrelease
              and any(not f['yanked'] for f in files)]
    assert str(max(stable)) == row['latest_non_preview_registry_observation']

nodes = {canonicalize_name(x['metadata']['name']): x for x in report['install']}
assert len(nodes) == 40
roots = [Requirement(l) for l in read(P + 'latest-coupled-resolution/latest-root-study.txt').decode().splitlines()
         if l.strip() and not l.startswith('#')]
assert len(roots) == 12
requested = {n for n, x in nodes.items() if x['requested']}
assert requested == {canonicalize_name(r.name) for r in roots}
extras = {n: set() for n in nodes}
reached = set(requested)
for r in roots:
    n = canonicalize_name(r.name)
    assert r.specifier.contains(nodes[n]['metadata']['version'])
    assert set(r.extras) == set(nodes[n].get('requested_extras', []))
    extras[n].update(r.extras)
    assert str(max(Version(v) for v, fs in project_data[n]['releases'].items()
                   if not Version(v).is_prerelease and not Version(v).is_devrelease
                   and any(not f['yanked'] for f in fs))) == nodes[n]['metadata']['version']
env = dict(report['environment'])
assert env == old['environment'] and env['python_full_version'] == '3.14.5'
assert sys.version_info[:3] == (3, 14, 5) and sys.platform == 'win32'
edges = set()
while True:
    state = (frozenset(reached), tuple((n, tuple(sorted(extras[n]))) for n in sorted(nodes)))
    for n in tuple(reached):
        for text in nodes[n]['metadata'].get('requires_dist', []):
            r = Requirement(text)
            if r.marker and not any(r.marker.evaluate({**env, 'extra': e}) for e in {''} | extras[n]):
                continue
            target = canonicalize_name(r.name)
            assert target in nodes and r.specifier.contains(nodes[target]['metadata']['version']), (n, text)
            edges.add((n, target, text))
            reached.add(target)
            extras[target].update(r.extras)
    current = (frozenset(reached), tuple((n, tuple(sorted(extras[n]))) for n in sorted(nodes)))
    if state == current:
        break
assert reached == set(nodes)
assert edges == {tuple(e) for e in summary['active_dependency_edges']} and len(edges) == 45
tags = set(sys_tags())
for n, record in nodes.items():
    metadata = record['metadata']
    assert not record['is_yanked'] and not Version(metadata['version']).is_prerelease
    assert SpecifierSet(metadata.get('requires_python', '')).contains(env['python_full_version'])
    assert extras[n] <= set(metadata.get('provides_extra', [])), (n, extras[n])
    filename = unquote(urlsplit(record['download_info']['url']).path).rsplit('/', 1)[-1]
    wn, wv, _, wt = parse_wheel_filename(filename)
    assert wn == n and wv == Version(metadata['version']) and wt & tags
    files = project_data[n]['releases'][metadata['version']]
    match = [f for f in files if f['filename'] == filename]
    assert len(match) == 1 and not match[0]['yanked']
    assert match[0]['url'] == record['download_info']['url']
    assert match[0]['digests']['sha256'] == record['download_info']['archive_info']['hashes']['sha256']
    assert SpecifierSet(match[0].get('requires_python') or '').contains(env['python_full_version'])
    expected = next(x for x in summary['package_records'] if x['name'] == n)
    assert expected['version'] == metadata['version'] and set(expected['extras']) == extras[n]
    assert expected['wheel'] == filename and expected['sha256'] == match[0]['digests']['sha256']
    assert sha(read(P + expected['registry_snapshot'])) == expected['registry_snapshot_sha256']

changes = [{'name': n, 'previous': oldrecords[n]['metadata']['version'], 'candidate': nodes[n]['metadata']['version']}
           for n in sorted(nodes) if oldrecords[n]['metadata']['version'] != nodes[n]['metadata']['version']]
assert changes == summary['changed_packages'] and len(changes) == 6
for name, report_obj in [('windows-study-hashed-requirements.txt', old),
                         ('latest-coupled-resolution/windows-study-hashed-requirements.txt', report)]:
    pins = [l for l in read(P + name).decode().splitlines() if l.strip() and not l.startswith('#')]
    indexed = {canonicalize_name(x['metadata']['name']): x for x in report_obj['install']}
    assert len(pins) == len(indexed)
    for line in pins:
        requirement, digest = line.split(' --hash=sha256:')
        r = Requirement(requirement); x = indexed[canonicalize_name(r.name)]
        assert str(r.specifier) == '==' + x['metadata']['version']
        assert set(r.extras) == set(x.get('requested_extras', []))
        assert digest == x['download_info']['archive_info']['hashes']['sha256']
assert completed['protected_inputs_before'] == completed['protected_inputs_after']
for name, digest in completed['protected_inputs_after'].items():
    assert sha(read(name)) == digest
receipt = obj(P + 'latest-coupled-resolution/receipt.json')
for flag in ('--isolated', '--dry-run', '--ignore-installed', '--only-binary=:all:', '--no-cache-dir'):
    assert flag in receipt['command']
assert receipt['exit_code'] == 0 and not receipt['installation_performed']
assert sha(read(P + 'latest-coupled-resolution/latest-root-study.txt')) == receipt['requirements_sha256']

follow = P + 'source-channel-followup/'
initial, pinned = obj(follow + 'source-observations.json'), obj(follow + 'pinned-source-observations.json')
source_raw = {}
for evidence in (initial, pinned):
    for r in evidence['results']:
        raw = gzip.decompress(read(follow + r['snapshot']))
        assert sha(raw) == r['raw_sha256']
        if 'raw_bytes' in r:
            assert len(raw) == r['raw_bytes']
        source_raw[r['name']] = raw
for name in ('fastapi-release', 'pydantic-release', 'sqlalchemy-release'):
    r = json.loads(source_raw[name])
    assert not r['draft'] and not r['prerelease']
    described = next(x['release'] for x in initial['results'] if x['name'] == name)
    assert all(r[k] == v for k, v in described.items())
assert all(r['status'] == 404 for r in initial['results'] if r['name'].startswith('core-'))
tag, annotation = json.loads(source_raw['pydantic-tag']), json.loads(source_raw['pydantic-tag-object'])
assert tag['object']['type'] == 'tag' and tag['object']['sha'] == annotation['sha']
assert annotation['object']['type'] == 'commit' and annotation['object']['sha'] == pinned['commit']
assert annotation['verification'] == pinned['tag_verification']
assert annotation['verification']['verified'] is False and annotation['verification']['reason'] == 'unsigned'
pyproject = tomllib.loads(source_raw['pydantic-pyproject-pinned'].decode())
coreproject = tomllib.loads(source_raw['core-pyproject-pinned'].decode())
cargo = tomllib.loads(source_raw['core-cargo-pinned'].decode())
assert source_raw['pydantic-pyproject-pinned'] == source_raw['pydantic-pyproject']
assert re.search(r"^VERSION = '2.14.0'$", source_raw['pydantic-version-pinned'].decode(), re.M)
assert 'pydantic-core==2.50.0' in pyproject['project']['dependencies'] and cargo['package']['version'] == '2.50.0'
assert 'Development Status :: 5 - Production/Stable' in pyproject['project']['classifiers']
assert 'Development Status :: 3 - Alpha' in coreproject['project']['classifiers']
assert 'opt-in' in json.loads(source_raw['fastapi-release'])['body']
assert 'drops support for Python 3.9' in json.loads(source_raw['pydantic-release'])['body']
assert read('apps/api/app/main.py').decode().splitlines()[16] == 'app = FastAPI(title="Hengshi Design API")'
result = {'status': 'DOING', 'metadata_replay': 'PASS', 'manifest_inputs': len(manifest['inputs']),
          'old_and_new_wheel_records': [40, 40], 'registry_raw_responses_verified': len(raw_responses),
          'source_raw_responses_verified': sum(len(e['results']) for e in (initial, pinned)),
          'active_edges': len(edges), 'roots': len(roots), 'changes': changes,
          'propagated_extras': {n: sorted(es) for n, es in extras.items() if es},
          'protected_inputs_verified': len(completed['protected_inputs_after']),
          'pydantic_commit': pinned['commit'], 'unsigned_tag': True, 'core_404_preserved': True,
          'registry_responses': raw_responses,
          'limits': 'Metadata/source bytes only; no fetched wheel bytes, installation, provenance attestation, native/import/API/DB/full graph/adoption proof.'}
with (ROOT / 'independent-replay-results.json').open('x', encoding='utf-8') as f:
    json.dump(result, f, indent=2); f.write('\n')
print(json.dumps({k: v for k, v in result.items() if k != 'registry_responses'}, indent=2))
