"""Inspect two frozen public wheel artifacts without installing or importing them."""
import base64
import csv
import gzip
import hashlib
import io
import json
from datetime import datetime, timezone
from email.parser import BytesParser
from pathlib import Path, PurePosixPath
from urllib.error import HTTPError
from urllib.request import Request, urlopen
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASIS = ROOT / 'output/research/staff-identity-graph-2026-10-08'
OPTIONS = ROOT / 'output/research/staff-identity-client-options-2026-10-08'
MAX_RESPONSE = 1024 * 1024
MAX_EXPANDED = 16 * 1024 * 1024


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def save(relative, raw):
    target = HERE / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open('xb') as stream:
        stream.write(raw)
    return {'path': target.relative_to(ROOT).as_posix(), 'bytes': len(raw), 'sha256': sha(raw)}


def fetch(url, relative):
    request = Request(url, headers={'User-Agent': 'Hengshi-Phase1-Public-Artifact-Inspection'})
    try:
        response = urlopen(request, timeout=20)
    except HTTPError as error:
        response = error
    with response:
        raw = response.read(MAX_RESPONSE + 1)
        if len(raw) > MAX_RESPONSE:
            raise ValueError('Response exceeds inspection cap')
        record = {'url': url, 'final_url': response.url, 'http_status': response.status,
                  'observed_utc': datetime.now(timezone.utc).isoformat(),
                  'raw_bytes': len(raw), 'raw_sha256': sha(raw),
                  'snapshot': save(relative, gzip.compress(raw, mtime=0))}
    return raw, record


def inspect(name, report_record, registry, source_commit):
    version = report_record['metadata']['version']
    url = report_record['download_info']['url']
    filename = url.rsplit('/', 1)[1]
    declared = next(x for x in registry['urls'] if x['filename'] == filename)
    expected = report_record['download_info']['archive_info']['hashes']['sha256']
    if declared['digests']['sha256'] != expected or declared['size'] > MAX_RESPONSE:
        raise ValueError('Frozen artifact identity or size mismatch')
    raw, artifact = fetch(url, name + '/wheel.gz')
    if artifact['http_status'] != 200 or sha(raw) != expected or len(raw) != declared['size']:
        raise ValueError('Downloaded wheel does not match frozen registry and resolver')
    with zipfile.ZipFile(io.BytesIO(raw)) as wheel:
        entries = wheel.infolist()
        paths = [x.filename for x in entries]
        if len(set(paths)) != len(paths) or sum(x.file_size for x in entries) > MAX_EXPANDED:
            raise ValueError('Duplicate members or excessive expanded size')
        for path in paths:
            if PurePosixPath(path).is_absolute() or '..' in PurePosixPath(path).parts or '\\' in path:
                raise ValueError('Unexpected archive member path')
        files = {x.filename for x in entries if not x.is_dir()}
        record_path, = [x for x in files if x.endswith('.dist-info/RECORD')]
        metadata_path, = [x for x in files if x.endswith('.dist-info/METADATA')]
        rows = list(csv.reader(io.StringIO(wheel.read(record_path).decode('utf-8'))))
        if any(len(x) != 3 for x in rows) or len({x[0] for x in rows}) != len(rows):
            raise ValueError('Malformed or duplicate RECORD entries')
        if {x[0] for x in rows} != files:
            raise ValueError('Archive and RECORD members differ')
        verified = 0
        for path, digest, size in rows:
            content = wheel.read(path)
            if path == record_path:
                if digest or size:
                    raise ValueError('Unexpected self-hashed RECORD')
                continue
            if not digest.startswith('sha256=') or int(size) != len(content):
                raise ValueError('Missing hash or length mismatch')
            actual = base64.urlsafe_b64encode(hashlib.sha256(content).digest()).rstrip(b'=').decode()
            if digest != 'sha256=' + actual:
                raise ValueError('RECORD content digest mismatch')
            verified += 1
        metadata_raw = wheel.read(metadata_path)
        metadata = BytesParser().parsebytes(metadata_raw)
        if metadata['Name'].lower() != name or metadata['Version'] != version:
            raise ValueError('Unexpected wheel metadata identity')
        licences = []
        for declared_path in metadata.get_all('License-File', []):
            candidate = metadata_path.rsplit('/', 1)[0] + '/licenses/' + declared_path
            content = wheel.read(candidate)
            licences.append({'archive_path': candidate, 'declared_path': declared_path,
                             'content': save(name + '/licenses/' + declared_path, content)})
        save(name + '/METADATA', metadata_raw)
        save(name + '/RECORD', wheel.read(record_path))
        inventory = [{'path': x.filename, 'bytes': x.file_size, 'compressed_bytes': x.compress_size}
                     for x in entries]
    licence_url = f'https://raw.githubusercontent.com/authlib/{name}/{source_commit}/LICENSE'
    source_raw, source = fetch(licence_url, name + '/source-LICENSE.gz')
    if source['http_status'] != 200:
        raise ValueError('Could not read source license at exact tag commit')
    provenance_url = f'https://pypi.org/integrity/{name}/{version}/{filename}/provenance'
    provenance_raw, provenance = fetch(provenance_url, name + '/provenance.json.gz')
    observation = {'http_status': provenance['http_status'], 'cryptographically_verified': False}
    if provenance['http_status'] == 200:
        bundles = json.loads(provenance_raw)['attestation_bundles']
        observation['publishers'] = [b['publisher'] for b in bundles]
        statements = []
        for bundle in bundles:
            for attestation in bundle['attestations']:
                statement = json.loads(base64.b64decode(attestation['envelope']['statement'], validate=True))
                statements.append({'predicate_type': statement.get('predicateType'),
                                   'subjects': statement.get('subject'),
                                   'exact_artifact_subject_match': any(
                                       s.get('name') == filename and s.get('digest', {}).get('sha256') == expected
                                       for s in statement.get('subject', []))})
        observation['unverified_statements'] = statements
    elif provenance['http_status'] != 404:
        observation['unresolved_http_error'] = True
    return {'name': name, 'version': version, 'filename': filename, 'wheel': artifact,
            'archive_entries': inventory, 'record_verified_files': verified,
            'record_self_entry_unhashed': record_path,
            'metadata_license': metadata.get('License'),
            'metadata_license_expression': metadata.get('License-Expression'),
            'license_files': licences, 'source_commit': source_commit, 'source_license': source,
            'source_license_matches_wheel': any(x['content']['sha256'] == sha(source_raw) for x in licences),
            'provenance_response': provenance, 'provenance_observation': observation}


if (HERE / 'observations.json').exists():
    raise SystemExit('Refuse to overwrite a completed inspection')
report_raw = (BASIS / 'pip-report.json').read_bytes()
receipt = json.loads((BASIS / 'receipt.json').read_bytes())
if sha(report_raw) != receipt['report_sha256']:
    raise SystemExit('Frozen resolver report changed')
for path, digest in receipt['protected_inputs_after'].items():
    if sha((ROOT / path).read_bytes()) != digest:
        raise SystemExit('Protected input changed: ' + path)
report = json.loads(report_raw)
records = {x['metadata']['name'].lower(): x for x in report['install']}
source_authlib = next(x for x in json.loads((OPTIONS / 'primary-sources.json').read_bytes())
                      if x['name'] == 'authlib')['source_commit']
tag_raw, tag_response = fetch('https://api.github.com/repos/authlib/joserfc/git/ref/tags/1.7.5',
                              'joserfc/source-tag.json.gz')
tag = json.loads(tag_raw)
if tag_response['http_status'] != 200 or tag['object']['type'] != 'commit':
    raise SystemExit('Tag did not resolve directly to a commit; inspect before proceeding')
commits = {'authlib': source_authlib, 'joserfc': tag['object']['sha']}
observations = []
for name in ('authlib', 'joserfc'):
    registry = json.loads(gzip.decompress((BASIS / (name + '-exact.json.gz')).read_bytes()))
    observations.append(inspect(name, records[name], registry, commits[name]))
for path, digest in receipt['protected_inputs_after'].items():
    if sha((ROOT / path).read_bytes()) != digest:
        raise SystemExit('Protected input changed during inspection: ' + path)
result = {'product_release': 'v1', 'status': 'DOING',
          'observed_utc': datetime.now(timezone.utc).isoformat(),
          'scope': 'Read-only public inspection of two exact frozen candidate wheels; no install or import',
          'basis_report_sha256': sha(report_raw), 'joserfc_source_tag': tag_response,
          'distributions': observations, 'protected_inputs_unchanged': True,
          'limits': ['RECORD is artifact self-consistency, not publisher authenticity or reproducible build provenance.',
                     'Attestation response and decoded statement are observations only; signatures, certificate identity and transparency proofs not verified.',
                     'Source license equality does not prove the full wheel was built from that source commit.',
                     'Two license files only; no complete dependency/embedded-code rights clearance, advisories, runtime qualification or production selection.',
                     'Pending 43-package native trial is untouched and not executed. No application, environment, lock, model, account, Figma or Git changes.']}
save('observations.json', (json.dumps(result, indent=2) + '\n').encode())
print(json.dumps({'packages': [{k: x[k] for k in ('name', 'version', 'record_verified_files', 'metadata_license', 'source_license_matches_wheel', 'provenance_observation')} for x in observations],
                  'retained_bytes': sum(p.stat().st_size for p in HERE.rglob('*') if p.is_file()),
                  'protected_inputs_unchanged': True}, indent=2))
