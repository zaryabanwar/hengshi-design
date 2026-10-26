"""Bounded public-registry declaration history; no install or version selection."""
from pathlib import Path, PurePosixPath
import urllib.request
import json
import hashlib
import base64
import tarfile
import io
import re
from datetime import datetime, timezone

OUT = Path(__file__).resolve().parent

def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Hengshi-v1-isolated-source-observation'}), timeout=35) as response:
        return response.read()

def write(name, data):
    target = OUT / name
    if target.exists():
        raise RuntimeError(f'Refusing overwrite: {target}')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)

def json_bytes(value):
    return (json.dumps(value, indent=2) + '\n').encode('utf-8')

def main():
    metadata = fetch('https://registry.npmjs.org/@types%2fthree')
    write('types-three-registry.json', metadata)
    registry = json.loads(metadata)
    all_versions = list(registry['versions'])
    versions = []
    for minor in (186, 185, 184, 183, 182, 181):
        candidates = [v for v in all_versions if re.fullmatch(rf'0\.{minor}\.\d+', v)]
        if candidates:
            versions.append(max(candidates, key=lambda v: tuple(int(i) for i in v.split('.'))))
    observations = []
    for version in versions:
        record = registry['versions'][version]
        write(f'{version}/registry.json', json_bytes(record))
        archive = fetch(record['dist']['tarball'])
        algorithm, expected = record['dist']['integrity'].split('-', 1)
        actual = base64.b64encode(hashlib.new(algorithm, archive).digest()).decode()
        if actual != expected:
            raise RuntimeError('Archive integrity mismatch')
        # Retain archives and only the finite declarations used to compare contracts.
        write(f'{version}/types-three.tgz', archive)
        wanted = ('src/extras/core/ShapePath.d.ts', 'src/loaders/DataTextureLoader.d.ts')
        contents = {}
        with tarfile.open(fileobj=io.BytesIO(archive), mode='r:gz') as tar:
            for member in tar.getmembers():
                suffix = next((name for name in wanted if member.name.endswith('/' + name)), None)
                if not suffix:
                    continue
                if not member.isfile() or '..' in PurePosixPath(member.name).parts:
                    raise RuntimeError('Unsafe selected tar member')
                data = tar.extractfile(member).read()
                if suffix in contents:
                    raise RuntimeError('Duplicate selected declaration')
                contents[suffix] = data.decode('utf-8')
                write(f'{version}/{suffix}', data)
        if len(contents) != len(wanted):
            raise RuntimeError('Missing declaration')
        shape = contents[wanted[0]]
        loader = contents[wanted[1]]
        observations.append({'version': version, 'published_at': registry['time'].get(version),
            'archive_integrity_verified': True,
            'shape_path_user_data_lines': [s.strip() for s in shape.splitlines() if 'userData' in s],
            'data_texture_loader_parse_lines': [s.strip() for s in loader.splitlines() if 'parse(' in s],
            'limits': 'source history only; no compiler, resolved graph, runtime or production selection'})
    write('observations.json', json_bytes({'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'registry_latest': registry['dist-tags']['latest'], 'versions': observations}))
    print(json.dumps(observations, indent=2))

if __name__ == '__main__':
    main()
