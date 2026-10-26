"""Separate installed-tree SBOM and detailed signature observations, retaining first attempts."""
import collect
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

if (collect.OUT / 'installed-sbom-receipt.json').exists():
    raise RuntimeError('Refusing overwrite')
env = {key: os.environ[key] for key in ('SystemRoot', 'WINDIR', 'COMSPEC', 'TEMP', 'TMP') if key in os.environ}
env['PATH'] = str(collect.RUNTIME) + os.pathsep + str(Path(env['SystemRoot']) / 'System32')
for name in ('audit', 'sbom'):
    url = f'https://docs.npmjs.com/cli/v12/commands/npm-{name}/'
    with urlopen(Request(url, headers={'User-Agent': 'Hengshi-definition-research/1.0'}), timeout=30) as response:
        data = response.read(4 * 1024 * 1024)
        (collect.OUT / f'official-npm12-{name}.html').write_bytes(data)
        collect.save(f'official-npm12-{name}-receipt.json', {'source': url, 'final_url': response.url,
            'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'status': response.status,
            'sha256': collect.sha(collect.OUT / f'official-npm12-{name}.html'),
            'scope': 'Public documentation; installed npm12 command sources retained separately.'})
collect.command('installed-sbom', ['sbom', '--sbom-format=spdx'], env)
collect.command('detailed-signatures', ['audit', 'signatures', '--json', '--include-attestations'], env)
frozen = json.loads((collect.BASE / 'review-inputs.json').read_text(encoding='utf-8'))
changed = [row['path'] for row in frozen if collect.sha(collect.ROOT / row['path']) != row['sha256']]
collect.save('post-follow-up-guard.json', {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
     'checked': len(frozen), 'mismatches': changed})
if changed:
    raise RuntimeError('Frozen inputs changed')
print('Detailed installed observations completed; first failure retained.', flush=True)
