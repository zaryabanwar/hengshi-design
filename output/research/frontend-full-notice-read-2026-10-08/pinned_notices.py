"""Fetch small notice candidates at registry-declared Git revisions, not main."""
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request,urlopen
from urllib.error import HTTPError
import hashlib,json,re
out=Path(__file__).resolve().parent
root=out.parents[2]
registry=json.loads((out/'registry-source-associations.json').read_text(encoding='utf-8'))
prior=json.loads((root/'output/research/frontend-supply-chain-2026-10-06/licence-inventory.json').read_text(encoding='utf-8'))
installed={r['name']:r for r in prior['records'] if r['installed']}
for item in registry['records']:
    assert item['http_status']==200 and item['version']==installed[item['name']]['version']
    assert item['dist_integrity']==installed[item['name']]['integrity']
def fetch(item):
    repo=item['repository']['url'] if isinstance(item['repository'],dict) else item['repository']
    repo=repo.removeprefix('git+').removesuffix('.git')
    if repo.startswith('git://'):repo='https://'+repo.removeprefix('git://')
    assert re.fullmatch(r'https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',repo)
    assert re.fullmatch(r'[0-9a-f]{40}',item['gitHead'])
    result={'name':item['name'],'version':item['version'],'registry_url':item['url'],
      'registry_snapshot':item['snapshot'],'registry_gitHead':item['gitHead'],
      'repository':repo,'requests':[],'association':'Registry-declared pointer; not authenticated source-build/tarball provenance'}
    slug=item['name'].replace('@','').replace('/','__')
    for filename in ['LICENSE','LICENSE.txt','LICENSE.md','MIT-LICENSE.txt','MIT-LICENSE']:
        url='https://raw.githubusercontent.com/'+repo.removeprefix('https://github.com/')+'/'+item['gitHead']+'/'+filename
        attempt={'url':url,'checked_at_utc':datetime.now(timezone.utc).isoformat()}
        try:
            with urlopen(Request(url),timeout=20) as response:
                raw=response.read(262145)
                assert len(raw)<=262144
                raw.decode('utf-8',errors='strict')
                attempt.update({'http_status':response.status,'response_url':response.url,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
            target=out/'pinned-upstream-notices'/slug/(item['gitHead']+'-'+filename)
            target.parent.mkdir(parents=True,exist_ok=True)
            assert not target.exists()
            target.write_bytes(raw)
            attempt['snapshot']=target.relative_to(out).as_posix()
            result['requests'].append(attempt)
            break
        except HTTPError as exc:
            attempt['http_status']=exc.code
            result['requests'].append(attempt)
            if exc.code!=404:break
        except Exception as exc:
            attempt['error_type']=type(exc).__name__
            result['requests'].append(attempt)
            break
    return result
eligible=[r for r in registry['records'] if r.get('gitHead') and r.get('repository')]
with ThreadPoolExecutor(max_workers=4) as pool:records=list(pool.map(fetch,eligible))
target=out/'pinned-upstream-notice-associations.json'
assert not target.exists()
result={'product':'Hengshi Design v1','status':'DOING','records':records,
 'no_revision_pointer':[r['name'] for r in registry['records'] if not r.get('gitHead')],
 'limits':'Finite root-filename candidates at public registry-declared Git revisions only; no default-branch licence substitution, signature/attestation/source-build proof, complete notices or applicability/legal clearance'}
target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'eligible':len(eligible),'retained_notices':sum(any(q.get('snapshot') for q in r['requests']) for r in records),
 'results':[{'name':r['name'],'requests':r['requests']} for r in records],'no_revision_pointer':result['no_revision_pointer']},indent=2))
