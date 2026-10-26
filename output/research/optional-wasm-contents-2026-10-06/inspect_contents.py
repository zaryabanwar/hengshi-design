"""Bounded supplemental archive inventory; no extraction, installs or execution."""
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone
import base64
import hashlib
import io
import json
import re
import tarfile

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
PRIOR = ROOT / 'output/research/optional-wasm-bundle-2026-10-06'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    if (OUT / 'contents.json').exists():
        raise RuntimeError('Preserve existing evidence; refusing overwrite')
    archive_bytes = (PRIOR / 'oxide-wasm32-wasi-4.3.3.tgz').read_bytes()
    lock_bytes = (PRIOR / 'package-lock.observed.json').read_bytes()
    lock = json.loads(lock_bytes)
    parent = lock['packages']['node_modules/@tailwindcss/oxide-wasm32-wasi']
    algorithm, encoded = parent['integrity'].split('-', 1)
    if algorithm != 'sha512' or hashlib.sha512(archive_bytes).digest() != base64.b64decode(encoded, validate=True):
        raise RuntimeError('Archive does not match preserved lock integrity')
    if len(archive_bytes) > 8 * 1024 * 1024:
        raise RuntimeError('Archive byte cap exceeded')
    files, metadata, names = [], [], set()
    notices = []
    total = 0
    with tarfile.open(fileobj=io.BytesIO(archive_bytes), mode='r:gz') as archive:
        for index, member in enumerate(archive):
            path = PurePosixPath(member.name)
            if index >= 10000 or path.is_absolute() or '..' in path.parts or path.parts[0] != 'package':
                raise RuntimeError('Unsafe path or member limit')
            if member.name in names or not member.isfile() or member.size < 0:
                raise RuntimeError('Duplicate or non-regular member')
            names.add(member.name)
            total += member.size
            if total > 64 * 1024 * 1024 or member.size > 16 * 1024 * 1024:
                raise RuntimeError('Unpacked/member byte cap exceeded')
            raw = archive.extractfile(member).read(member.size + 1)
            if len(raw) != member.size:
                raise RuntimeError('Member length mismatch')
            files.append({'path': member.name, 'bytes': len(raw), 'sha256': sha(raw)})
            if path.name == 'package.json':
                if len(raw) > 1024 * 1024:
                    raise RuntimeError('Metadata byte cap exceeded')
                record = json.loads(raw.decode('utf-8'))
                metadata.append({'path': member.name, 'root': str(path.parent), 'name': record.get('name'),
                                 'version': record.get('version'), 'license': record.get('license'),
                                 'dependencies': record.get('dependencies', {}), 'sha256': sha(raw)})
            if re.fullmatch(r'(licen[sc]e|notice|copying|copyright)(\..+)?', path.name, re.I):
                if len(raw) > 1024 * 1024:
                    raise RuntimeError('Notice byte cap exceeded')
                saved = f'notice-{len(notices):02d}.txt'
                (OUT / saved).write_bytes(raw)
                notices.append({'archive_path': member.name, 'saved_path': saved, 'bytes': len(raw), 'sha256': sha(raw)})
    packages = [record for record in metadata if record['name'] and record['version']]
    for record in files:
        owners = [pkg for pkg in packages if record['path'].startswith(pkg['root'] + '/')]
        if not owners:
            raise RuntimeError('File has no metadata owner')
        owner = max(owners, key=lambda pkg: len(pkg['root']))
        record['metadata_owner'] = owner['name']
        record['metadata_owner_version'] = owner['version']
    by_name = {pkg['name']: pkg for pkg in packages}
    if len(by_name) != len(packages):
        raise RuntimeError('Duplicate named package needs explicit location resolution')
    edges = []
    for pkg in packages:
        for name, declared_range in pkg['dependencies'].items():
            target = by_name.get(name)
            edges.append({'from': pkg['name'], 'to': name, 'declared_range': declared_range,
                          'archive_metadata_version': target['version'] if target else None,
                          'metadata_found': target is not None})
    result = {'product': 'Hengshi Design v1', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
              'archive_sha256': sha(archive_bytes), 'lock_sha256': sha(lock_bytes),
              'archive_integrity_matches_lock': True, 'regular_files': len(files), 'total_member_bytes': total,
              'packages': packages, 'unnamed_package_metadata': [pkg for pkg in metadata if not pkg['name']],
              'files': files, 'declared_dependency_edges': edges, 'dedicated_notice_files': notices,
              'limits': ['Supplemental contents inventory, not a repaired or complete all-platform/deployed SBOM',
                        'Metadata owner is nearest named manifest path, not legal authorship or licence inheritance',
                        'Dependency-name correlations are not Node resolution or range/conformance proof',
                        'Dedicated notice search does not inspect embedded notices or establish legal completeness',
                        'No source-to-binary, advisory, attestation or production-selection claim'],
              'network_install_extraction_or_package_execution': False}
    (OUT / 'contents.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'regular_files': len(files), 'named_packages': len(packages),
                      'declared_edges': len(edges), 'all_edge_targets_have_metadata': all(edge['metadata_found'] for edge in edges),
                      'dedicated_notice_files': len(notices), 'archive_integrity_matches_lock': True}))


if __name__ == '__main__':
    main()
