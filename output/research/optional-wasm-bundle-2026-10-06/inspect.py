"""Read an existing integrity-addressed archive; no extraction or package execution."""
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone
import base64
import hashlib
import io
import json
import shutil
import tarfile

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
LOCK = ROOT / 'output/research/frontend-three-remedy-evaluation-2026-10-06/candidate/package-lock.json'
SOURCE = ROOT / 'output/research/frontend-supply-chain-2026-10-06/npm12-sbom.js'
KEY = 'node_modules/@tailwindcss/oxide-wasm32-wasi'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    result = OUT / 'observation.json'
    if result.exists():
        raise RuntimeError('Existing observation is immutable; do not overwrite')
    lock_bytes = LOCK.read_bytes()
    lock = json.loads(lock_bytes)
    entry = lock['packages'][KEY]
    algorithm, encoded = entry['integrity'].split('-', 1)
    if algorithm != 'sha512':
        raise RuntimeError('Unexpected integrity algorithm')
    expected = base64.b64decode(encoded, validate=True)
    hex_digest = expected.hex()
    cache = ROOT / 'output/research/frontend-build-evaluation-2026-10-06/metadata-cache/_cacache/content-v2/sha512'
    archive = cache / hex_digest[:2] / hex_digest[2:4] / hex_digest[4:]
    if not archive.is_file() or archive.stat().st_size > 8 * 1024 * 1024:
        raise RuntimeError('Existing archive missing or exceeds bounded inspection size')
    data = archive.read_bytes()
    if hashlib.sha512(data).digest() != expected:
        raise RuntimeError('Cached archive fails exact candidate-lock integrity')
    (OUT / 'oxide-wasm32-wasi-4.3.3.tgz').write_bytes(data)
    shutil.copyfile(LOCK, OUT / 'package-lock.observed.json')
    shutil.copyfile(SOURCE, OUT / 'npm12-sbom.observed.js')
    names = set()
    records = []
    package_records = []
    total = 0
    with tarfile.open(fileobj=io.BytesIO(data), mode='r:gz') as tar:
        for index, member in enumerate(tar):
            if index >= 10000:
                raise RuntimeError('Member count exceeds inspection cap')
            path = PurePosixPath(member.name)
            if path.is_absolute() or '..' in path.parts or not path.parts or path.parts[0] != 'package':
                raise RuntimeError('Unexpected archive path')
            if member.name in names:
                raise RuntimeError('Duplicate archive member')
            names.add(member.name)
            total += member.size
            if total > 64 * 1024 * 1024:
                raise RuntimeError('Declared unpacked bytes exceed inspection cap')
            records.append({'path': member.name, 'bytes': member.size, 'regular_file': member.isfile()})
            if not member.isfile() or path.name != 'package.json':
                continue
            if member.size > 1024 * 1024:
                raise RuntimeError('Package metadata exceeds inspection cap')
            raw = tar.extractfile(member).read(1024 * 1024 + 1)
            metadata = json.loads(raw.decode('utf-8'))
            filename = f'package-metadata-{len(package_records):02d}.json'
            (OUT / filename).write_bytes(raw)
            package_records.append({'archive_path': member.name, 'saved_path': filename,
                'sha256': digest(raw), 'name': metadata.get('name'), 'version': metadata.get('version'),
                'license': metadata.get('license'), 'dependencies': metadata.get('dependencies', {}),
                'bundleDependencies': metadata.get('bundleDependencies', metadata.get('bundledDependencies', []))})
    parent = next(item for item in package_records if item['archive_path'] == 'package/package.json')
    if parent['name'] != '@tailwindcss/oxide-wasm32-wasi' or parent['version'] != entry['version']:
        raise RuntimeError('Archive package identity mismatch')
    required = entry['dependencies']
    matched = []
    for name, version_range in required.items():
        item = next((item for item in package_records
            if item['archive_path'] == f'package/node_modules/{name}/package.json'), None)
        matched.append({'name': name, 'declared_range': version_range,
            'archive_package': item, 'lock_locations': [location for location in lock['packages']
                if location.endswith('node_modules/' + name)]})
    (OUT / 'archive-members.json').write_text(json.dumps(records, indent=2) + '\n', encoding='utf-8')
    observation = {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'package': parent['name'], 'version': parent['version'], 'archive_bytes': len(data),
        'archive_sha256': digest(data), 'archive_sha512_matches_lock': True,
        'lock_sha256': digest(lock_bytes), 'npm_source_sha256': digest(SOURCE.read_bytes()),
        'archive_member_count': len(records), 'declared_unpacked_bytes': total,
        'package_metadata_records': package_records, 'six_failed_edges': matched,
        'all_six_exact_metadata_paths_present': all(item['archive_package'] is not None for item in matched),
        'scope': 'Static archive metadata observation only. No semver acceptance, executable behavior, all-platform SBOM, licence clearance, attestation or production selection.',
        'network_or_install_or_extract_or_execute': False}
    result.write_text(json.dumps(observation, indent=2) + '\n', encoding='utf-8')
    if LOCK.read_bytes() != lock_bytes:
        raise RuntimeError('Observed candidate lock changed')
    print(json.dumps({'archive_bytes': len(data), 'integrity_matches': True,
        'members': len(records), 'metadata_records': len(package_records),
        'all_six_metadata_present': observation['all_six_exact_metadata_paths_present'],
        'bundled_versions': [(item['name'], item['archive_package']['version'] if item['archive_package'] else None) for item in matched]}))


if __name__ == '__main__':
    main()
