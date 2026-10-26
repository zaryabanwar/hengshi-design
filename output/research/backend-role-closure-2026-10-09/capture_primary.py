"""Save public PyPA specification bytes; no candidate execution or installation."""
import datetime
import gzip
import hashlib
import json
from pathlib import Path
from urllib.request import Request, urlopen

HERE = Path(__file__).resolve().parent
if (HERE / 'primary-guidance.json').exists():
    raise SystemExit('Refuse repeated primary capture')
records = []
for name in ('dependency-specifiers', 'dependency-groups'):
    url = 'https://raw.githubusercontent.com/pypa/packaging.python.org/main/source/specifications/' + name + '.rst'
    path = HERE / (name + '.rst.gz')
    if path.exists():
        raise SystemExit('Refuse overwriting captured source')
    with urlopen(Request(url, headers={'User-Agent': 'Hengshi-Phase1-readonly/1'}), timeout=25) as response:
        raw = response.read(1024 * 1024 + 1)
        assert len(raw) <= 1024 * 1024 and response.status == 200
    compressed = gzip.compress(raw, mtime=0)
    path.write_bytes(compressed)
    records.append({'url': url, 'captured_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    'raw_bytes': len(raw), 'raw_sha256': hashlib.sha256(raw).hexdigest(),
                    'saved': path.name, 'saved_sha256': hashlib.sha256(compressed).hexdigest()})
(HERE / 'primary-guidance.json').write_bytes((json.dumps(records, indent=2) + '\n').encode())
print('Two public specification snapshots captured as dated mutable-branch observations, not signed source.')
