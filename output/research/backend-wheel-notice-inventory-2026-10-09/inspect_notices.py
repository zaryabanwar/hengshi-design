"""Read exact wheel data/notice bytes; no package installation or import."""
from email.parser import BytesParser
import gzip
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
import zipfile
from packaging.utils import canonicalize_name

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
GRAPH = ROOT / 'output/research/test-client-graph-2026-10-09'
if (HERE / 'observations.json').exists():
    raise SystemExit('Refuse repeat inventory')
graph = json.loads((GRAPH / 'closure-observations.json').read_bytes())
report = json.loads((GRAPH / 'pip-report.json').read_bytes())
entries = {canonicalize_name(x['metadata']['name']): x for x in report['install']}
protected = json.loads((ROOT / 'output/research/backend-crypto-graph-2026-10-08/proposal.json').read_bytes())['protected_inputs_before']
sha = lambda b: hashlib.sha256(b).hexdigest()
assert all(sha((ROOT / p).read_bytes()) == h for p,h in protected.items())
records = []
for package in graph['package_records']:
    name, filename = package['name'], package['wheel']
    previous = ROOT / 'output/research/backend-crypto-graph-2026-10-08/native-trial/wheelhouse' / filename
    if previous.exists():
        raw = previous.read_bytes(); origin = previous.relative_to(ROOT).as_posix()
    elif name in ('authlib', 'joserfc'):
        previous = ROOT / f'output/research/staff-identity-distribution-2026-10-09/{name}/wheel.gz'
        raw = gzip.decompress(previous.read_bytes()); origin = previous.relative_to(ROOT).as_posix()
    else:
        assert name in ('httpx2', 'httpcore2', 'truststore')
        url = entries[name]['download_info']['url']
        assert urlsplit(url).scheme == 'https' and urlsplit(url).hostname == 'files.pythonhosted.org'
        with urlopen(Request(url, headers={'User-Agent': 'Hengshi-Phase1-Evidence/1.0'}), timeout=25) as response:
            raw = response.read(package['bytes'] + 1)
        folder = HERE / name; folder.mkdir(exist_ok=False)
        previous = folder / 'wheel.gz'; previous.write_bytes(gzip.compress(raw, mtime=0))
        origin = previous.relative_to(ROOT).as_posix()
    assert len(raw) == package['bytes'] and sha(raw) == package['sha256']
    folder = HERE / name; folder.mkdir(exist_ok=True)
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        names = archive.namelist()
        assert len(names) == len(set(names))
        assert not any(PurePosixPath(n).is_absolute() or '..' in PurePosixPath(n).parts or '\\' in n for n in names)
        assert archive.testzip() is None
        meta_members = [n for n in names if n.endswith('.dist-info/METADATA')]
        assert len(meta_members) == 1
        meta_raw = archive.read(meta_members[0]); meta = BytesParser().parsebytes(meta_raw)
        assert canonicalize_name(meta['Name']) == name and meta['Version'] == package['version']
        (folder / 'METADATA').write_bytes(meta_raw)
        prefix = meta_members[0].rsplit('/',1)[0]
        declared = meta.get_all('License-File') or []
        declaration_bindings = []
        for declaration in declared:
            matches = [n for n in names if n in (prefix + '/licenses/' + declaration, prefix + '/' + declaration)]
            declaration_bindings.append({'declaration': declaration, 'matches': matches,
                                         'binding': 'unique' if len(matches)==1 else 'missing_or_ambiguous'})
        selected = []
        for member in names:
            if member.endswith('/'):
                continue
            basename = PurePosixPath(member).name.lower()
            if '/licenses/' in member.lower() or any(basename.startswith(term) for term in ('license','notice','copying','copyright','authors')):
                selected.append(member)
        for binding in declaration_bindings:
            selected.extend(binding['matches'])
        saved = []
        for member in sorted(set(selected)):
            data = archive.read(member)
            assert len(data) <= 1048576
            target = folder / 'notice-bytes' / member
            target.parent.mkdir(parents=True,exist_ok=True); target.write_bytes(data)
            saved.append({'member': member, 'bytes': len(data), 'sha256': sha(data),
                          'saved': target.relative_to(ROOT).as_posix()})
        binary = [n for n in names if n.lower().endswith(('.pyd','.dll','.so','.dylib','.a','.lib'))]
    records.append({'name': name, 'version': package['version'], 'wheel': filename,
                    'wheel_bytes': len(raw), 'wheel_sha256': sha(raw), 'wheel_source': origin,
                    'metadata_sha256': sha(meta_raw), 'metadata_license_expression': meta.get('License-Expression'),
                    'metadata_license': meta.get('License'), 'license_file_bindings': declaration_bindings,
                    'notice_files': saved, 'binary_members': binary,
                    'limits': 'Full saved notice bytes and declared-path bindings only; no legal applicability, complete embedded/transitive inventory or provenance assertion.'})
assert len(records) == 48
observation = {'product_release': 'v1', 'status': 'DOING',
                'scope': 'Exact 48 Windows wheel identities, metadata licence declarations and full discovered notice byte inventory; no install/import',
                'graph_sha256': sha((GRAPH / 'closure-observations.json').read_bytes()),
                'packages': records, 'package_count': len(records),
                'notice_file_count': sum(len(x['notice_files']) for x in records),
                'no_discovered_notices': [x['name'] for x in records if not x['notice_files']],
                'non_unique_declared_license_bindings': [{'name':x['name'],'binding':b} for x in records for b in x['license_file_bindings'] if b['binding']!='unique'],
                'packages_with_binary_members': [x['name'] for x in records if x['binary_members']],
                'retained_bytes_before_receipt': sum(p.stat().st_size for p in HERE.rglob('*') if p.is_file()),
                'protected_inputs_unchanged': all(sha((ROOT/p).read_bytes())==h for p,h in protected.items()),
                'limits': ['Name/path discovery can miss embedded notices; saved text was not interpreted as legal clearance.',
                           'Metadata expressions and redistribution applicability require review against full texts and delivered release contents.',
                           'Binary member inventory does not identify every linked/bundled library or its licence/provenance.',
                           'No cryptographic attestations, advisories, release notice delivery, runtime or graph adoption proof.']}
(HERE / 'observations.json').write_text(json.dumps(observation,indent=2)+'\n')
print(json.dumps({k:v for k,v in observation.items() if k!='packages'},indent=2))
