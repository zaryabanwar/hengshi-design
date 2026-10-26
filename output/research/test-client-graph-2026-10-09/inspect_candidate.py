"""Inspect exact saved metadata closure and public primary snapshots; no imports."""
import gzip
import hashlib
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen
from packaging.markers import default_environment
from packaging.requirements import Requirement
from packaging.specifiers import SpecifierSet
from packaging.tags import sys_tags
from packaging.utils import canonicalize_name, parse_wheel_filename
from packaging.version import Version

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASIS = ROOT / 'output/research/staff-identity-graph-2026-10-08'
if (HERE / 'closure-observations.json').exists():
    raise SystemExit('Refuse repeated closure observation')
sha = lambda raw: hashlib.sha256(raw).hexdigest()
receipt = json.loads((HERE / 'receipt.json').read_bytes())
assert receipt['exit_code'] == 0 and not receipt['installation_performed']
report_raw = (HERE / 'pip-report.json').read_bytes()
assert sha(report_raw) == receipt['report_sha256']
report = json.loads(report_raw)
records = {canonicalize_name(x['metadata']['name']): x for x in report['install']}
old = {canonicalize_name(x['metadata']['name']): x for x in json.loads((BASIS / 'pip-report.json').read_bytes())['install']}
assert len(records) == len(report['install']) == 48
assert set(records) - set(old) == {'httpx2', 'httpcore2', 'truststore'}
assert set(old) <= set(records)
assert all(records[k]['metadata'] == old[k]['metadata'] and records[k]['download_info'] == old[k]['download_info'] for k in old)
environment = report['environment']
assert all(default_environment()[k] == v for k, v in environment.items())
extras = {k: set(v.get('requested_extras', [])) for k, v in records.items()}
edges = set(); changed = True
while changed:
    changed = False
    for name, entry in records.items():
        for clause in entry['metadata'].get('requires_dist', []):
            req = Requirement(clause)
            if req.marker and not any(req.marker.evaluate({**environment, 'extra': x}) for x in {''} | extras[name]):
                continue
            target = canonicalize_name(req.name)
            assert req.url is None and target in records
            assert req.specifier.contains(records[target]['metadata']['version'], prereleases=False)
            edges.add((name, target, clause))
            added = set(req.extras) - extras[target]
            if added:
                extras[target].update(added); changed = True
sources = []


def fetch(name, url):
    path = HERE / (name + '.gz')
    if path.exists():
        raise RuntimeError('Refuse overwriting primary source ' + name)
    with urlopen(Request(url, headers={'User-Agent': 'Hengshi-Phase1-Evidence/1.0'}), timeout=25) as response:
        raw = response.read(4000001); assert len(raw) <= 4000000
    path.write_bytes(gzip.compress(raw, mtime=0))
    sources.append({'url': url, 'snapshot': path.relative_to(ROOT).as_posix(),
                    'raw_bytes': len(raw), 'raw_sha256': sha(raw), 'snapshot_sha256': sha(path.read_bytes())})
    return raw


registries = {}; release_status = {}
for name in sorted(set(records) - set(old)):
    version = records[name]['metadata']['version']
    raw = fetch(name + '-exact.json', f'https://pypi.org/pypi/{name}/{version}/json')
    exact = json.loads(raw)
    latest = json.loads(fetch(name + '-latest.json', f'https://pypi.org/pypi/{name}/json'))
    assert canonicalize_name(exact['info']['name']) == name and exact['info']['version'] == version
    assert sorted(str(Requirement(x)) for x in exact['info'].get('requires_dist') or []) == sorted(str(Requirement(x)) for x in records[name]['metadata'].get('requires_dist') or [])
    registries[name] = exact
    release_status[name] = {'evaluated': version, 'registry_latest_observed': latest['info']['version'],
                            'classifiers': [x for x in exact['info']['classifiers'] if x.startswith('Development Status')],
                            'latest_observation_is_not_selection': True}
tags = set(sys_tags()); packages = []
old_packages = {x['name']: x for x in json.loads((BASIS / 'closure-observations.json').read_bytes())['package_records']}
for name, entry in sorted(records.items()):
    metadata = entry['metadata']; version = Version(metadata['version'])
    assert not version.is_prerelease and not version.is_devrelease and not entry['is_yanked']
    assert not metadata.get('requires_python') or SpecifierSet(metadata['requires_python']).contains(environment['python_full_version'])
    info = entry['download_info']; parsed = urlsplit(info['url'])
    assert parsed.scheme == 'https' and parsed.hostname == 'files.pythonhosted.org'
    filename = unquote(parsed.path.rsplit('/', 1)[1])
    wn, wv, _, wheel_tags = parse_wheel_filename(filename)
    assert wn == name and wv == version and tags & wheel_tags
    digest = info['archive_info']['hashes']['sha256']
    if name in old_packages:
        prior = old_packages[name]
        assert prior['wheel'] == filename and prior['sha256'] == digest
        byte_length = prior['bytes']
    else:
        item = next(x for x in registries[name]['urls'] if x['filename'] == filename)
        assert not item['yanked'] and item['digests']['sha256'] == digest
        byte_length = item['size']
    packages.append({'name': name, 'version': str(version), 'wheel': filename,
                     'sha256': digest, 'bytes': byte_length, 'extras': sorted(extras[name])})
releases = json.loads(gzip.decompress((HERE / 'httpx2-releases.json.gz').read_bytes()))
release = next(x for x in releases if x['tag_name'] == 'v2.13.1')
assert not release['draft'] and not release['prerelease']
ref = json.loads(fetch('httpx2-tag-ref.json', 'https://api.github.com/repos/pydantic/httpx2/git/ref/tags/v2.13.1'))
obj = ref['object']
if obj['type'] == 'tag':
    obj = json.loads(fetch('httpx2-annotated-tag.json', obj['url']))['object']
assert obj['type'] == 'commit'
commit = obj['sha']
tree = json.loads(fetch('httpx2-tree.json', f'https://api.github.com/repos/pydantic/httpx2/git/trees/{commit}?recursive=1'))
assert not tree['truncated']
migration = [x['path'] for x in tree['tree'] if x['path'].endswith('/migration.md')]
assert len(migration) == 1
fetch('httpx2-migration.md', f'https://raw.githubusercontent.com/pydantic/httpx2/{commit}/{migration[0]}')
observations = {'product_release': 'v1', 'status': 'DOING', 'scope': 'Producer-only metadata/source observation, not native or graph adoption',
                'report_sha256': sha(report_raw), 'package_count': len(packages), 'edge_count': len(edges),
                'previous_45_package_records_unchanged': True, 'release_observations': release_status,
                'httpx2_source_commit': commit, 'httpx2_release': {'tag': release['tag_name'], 'draft': release['draft'], 'prerelease': release['prerelease']},
                'package_records': packages, 'edges': [list(x) for x in sorted(edges)],
                'compressed_registry_bytes': sum(x['bytes'] for x in packages), 'installation_performed': False,
                'protected_inputs_unchanged': all(sha((ROOT/p).read_bytes()) == h for p,h in receipt['protected_inputs_before'].items()),
                'limits': ['Stable-looking versions/classifiers, source tags and peer/marker closure do not prove full support, provenance, licence or native compatibility.',
                           'HTTPX and HTTPX2 remain distinct type hierarchies; no alias or global TLS injection selected.',
                           'The approved executed native trial remains 43 packages; this enlarged graph has no installation permission.',
                           'No complete latest-mutually-compatible graph, OIDC, TLS trust behavior or Hengshi adoption acceptance.']}
(HERE / 'registry-source-observations.json').write_text(json.dumps(sources, indent=2)+'\n')
(HERE / 'closure-observations.json').write_text(json.dumps(observations, indent=2)+'\n')
pins = ['# Research-only 48-package Windows metadata candidate, not a production lock.']
pins += [x['name'] + ('['+','.join(x['extras'])+']' if x['extras'] else '') + '=='+x['version']+' --hash=sha256:'+x['sha256'] for x in packages]
(HERE / 'candidate-hashed-requirements.txt').write_text('\n'.join(pins)+'\n')
print(json.dumps({k:v for k,v in observations.items() if k not in ('package_records','edges')},indent=2))
