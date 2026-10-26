"""Inspect saved resolver metadata; no install or production selection."""
import gzip
import hashlib
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit

from packaging.markers import default_environment
from packaging.requirements import Requirement
from packaging.specifiers import SpecifierSet
from packaging.tags import sys_tags
from packaging.utils import canonicalize_name, parse_wheel_filename
from packaging.version import Version

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
ROOT = HERE.parents[3]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    raw = (HERE / 'pip-report.json').read_bytes()
    report = json.loads(raw)
    receipt = json.loads((HERE / 'receipt.json').read_text(encoding='utf-8'))
    assert receipt['exit_code'] == 0 and not receipt['installation_performed']
    assert sha(raw) == receipt['report_sha256']
    environment = report['environment']
    host = default_environment()
    assert all(host[key] == value for key, value in environment.items())
    records = {canonicalize_name(x['metadata']['name']): x for x in report['install']}
    assert len(records) == len(report['install']) == 40
    extras = {name: set(x.get('requested_extras', [])) for name, x in records.items()}
    edges = set()
    changed = True
    while changed:
        changed = False
        for name, record in records.items():
            for text in record['metadata'].get('requires_dist', []):
                req = Requirement(text)
                active = not req.marker or any(req.marker.evaluate({**environment, 'extra': extra})
                                              for extra in {''} | extras[name])
                if not active:
                    continue
                target = canonicalize_name(req.name)
                assert req.url is None and target in records, (name, text)
                version = records[target]['metadata']['version']
                assert req.specifier.contains(version, prereleases=False), (name, text, version)
                edges.add((name, target, text))
                added = set(req.extras) - extras[target]
                if added:
                    extras[target].update(added)
                    changed = True
    compatible_tags = set(sys_tags())
    observations = []
    requirements = []
    for name, record in sorted(records.items()):
        metadata = record['metadata']
        version = metadata['version']
        parsed = Version(version)
        assert not parsed.is_prerelease and not parsed.is_devrelease and not record['is_yanked']
        requires_python = metadata.get('requires_python')
        assert not requires_python or SpecifierSet(requires_python).contains(environment['python_full_version'])
        url = record['download_info']['url']
        assert urlsplit(url).scheme == 'https' and urlsplit(url).hostname == 'files.pythonhosted.org'
        filename = unquote(urlsplit(url).path.rsplit('/', 1)[1])
        wheel_name, wheel_version, _, tags = parse_wheel_filename(filename)
        assert canonicalize_name(wheel_name) == name and wheel_version == parsed
        assert tags & compatible_tags, filename
        digest = record['download_info']['archive_info']['hashes']['sha256']
        snapshot = BASE / 'primary' / (name + '-project.json.gz')
        if name == 'pydantic-core':
            snapshot = BASE / 'core-recovery/pydantic-core-project.json.gz'
        registry = json.loads(gzip.decompress(snapshot.read_bytes()))
        matches = [f for f in registry['releases'][version] if f['filename'] == filename and f['url'] == url]
        assert len(matches) == 1 and matches[0]['digests']['sha256'] == digest
        assert matches[0]['packagetype'] == 'bdist_wheel' and not matches[0]['yanked']
        token = name + ('[' + ','.join(sorted(extras[name])) + ']' if extras[name] else '')
        requirements.append(f'{token}=={version} --hash=sha256:{digest}')
        observations.append({'name': name, 'version': version, 'extras': sorted(extras[name]),
                             'wheel': filename, 'sha256': digest,
                             'registry_snapshot': str(snapshot.relative_to(BASE)).replace('\\', '/'),
                             'registry_snapshot_sha256': sha(snapshot.read_bytes())})
    old = json.loads((ROOT / 'output/research/compatibility-resolution-2026-10-04/backend-windows/pip-report.json').read_text(encoding='utf-8'))
    old_versions = {canonicalize_name(x['metadata']['name']): x['metadata']['version'] for x in old['install']}
    differences = [{'name': name, 'previous': old_versions.get(name), 'candidate': record['metadata']['version']}
                   for name, record in sorted(records.items()) if old_versions.get(name) != record['metadata']['version']]
    initial = json.loads((BASE / 'completed-registry-recheck.json').read_text(encoding='utf-8'))
    protected = initial['protected_inputs_after']
    assert protected, list(initial)
    current = {p: sha((ROOT / p).read_bytes()) if (ROOT / p).is_file() else None for p in protected}
    assert current == protected
    pins = '# Research-only Windows CPython 3.14.5 mixed runtime/test graph; not a production lock.\n'
    pins += '# Hashes match saved registry metadata; wheel content was not independently verified.\n'
    pins += '# A separately authorized replay needs --require-hashes --only-binary=:all:.\n'
    pins += '\n'.join(requirements) + '\n'
    (HERE / 'windows-study-hashed-requirements.txt').write_text(pins, encoding='utf-8')
    result = {'status': 'DOING', 'scope': 'Saved report/registry metadata and marker/extras closure only',
              'report_sha256': sha(raw), 'environment': environment, 'package_records': observations,
              'active_dependency_edges': [list(edge) for edge in sorted(edges)], 'changed_packages': differences,
              'protected_inputs_unchanged': True, 'hashed_requirements_sha256': sha(pins.encode('utf-8')),
              'installation_performed': False, 'wheel_content_verified': False, 'runtime_tested': False,
              'production_selection': False, 'independent_review': 'pending',
              'limits': ['Windows only; no Linux/provider selection', 'No native ABI/import/API/database tests',
                         'No complete release-channel, provenance, advisory or licence clearance',
                         'Earlier independent reviews do not cover these later bytes']}
    (HERE / 'closure-observations.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'packages': len(records), 'active_edges': len(edges), 'changes': differences,
                      'protected_inputs_unchanged': True, 'runtime_tested': False, 'independent_review': 'pending'}, indent=2))


if __name__ == '__main__':
    main()
