"""Disambiguate missing root filenames from unavailable registry revision pointers."""
from pathlib import Path
from datetime import datetime,timezone
from urllib.request import Request,urlopen
from urllib.error import HTTPError
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,re
out=Path(__file__).resolve().parent
prior=json.loads((out/'pinned-upstream-notice-associations.json').read_text(encoding='utf-8'))
eligible=[r for r in prior['records'] if not any(q.get('snapshot') for q in r['requests'])]
def fetch(item):
    repo=item['repository'].removeprefix('https://github.com/')
    url='https://api.github.com/repos/'+repo+'/git/trees/'+item['registry_gitHead']+'?recursive=1'
    result={'name':item['name'],'version':item['version'],'requested_revision':item['registry_gitHead'],
       'url':url,'checked_at_utc':datetime.now(timezone.utc).isoformat()}
    try:
        with urlopen(Request(url,headers={'Accept':'application/vnd.github+json','User-Agent':'Hengshi-ReadOnly-Notice-Assessment'}),timeout=25) as response:
            raw=response.read(2097153)
            assert len(raw)<=2097152
            data=json.loads(raw)
            assert isinstance(data.get('tree'),list)
            result.update({'http_status':response.status,'response_url':response.url,
               'returned_tree_sha':data.get('sha'),'truncated':data.get('truncated'),
               'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
               'notice_name_paths':[x['path'] for x in data['tree'] if x['type']=='blob' and re.search(r'licen[cs]e|notice|copying|copyright|third[-_]party',x['path'],re.I)]})
        target=out/'revision-trees'/(item['name'].replace('@','').replace('/','__')+'-'+item['registry_gitHead']+'.json')
        target.parent.mkdir(exist_ok=True)
        assert not target.exists()
        target.write_bytes(raw)
        result['snapshot']=target.relative_to(out).as_posix()
    except HTTPError as exc:result['http_status']=exc.code
    except Exception as exc:result['error_type']=type(exc).__name__
    return result
with ThreadPoolExecutor(max_workers=4) as pool:records=list(pool.map(fetch,eligible))
result={'product':'Hengshi Design v1','status':'DOING','records':records,
 'limits':'Dated public revision-tree request results, not publisher/source-build proof. HTTP404 does not distinguish unavailable/private/deleted repositories or commits; returned tree SHA may differ from requested commit SHA.'}
target=out/'revision-tree-observations.json'
assert not target.exists()
target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(records,indent=2))
