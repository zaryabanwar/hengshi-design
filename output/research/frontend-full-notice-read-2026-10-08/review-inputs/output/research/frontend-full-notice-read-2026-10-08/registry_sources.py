"""Public exact-version metadata GETs only; no package execution or installation."""
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request,urlopen
from urllib.parse import quote
import hashlib,json
out=Path(__file__).resolve().parent
observations=json.loads((out/'observations.json').read_text(encoding='utf-8'))
def fetch(item):
    url='https://registry.npmjs.org/'+quote(item['name'],safe='@')+'/'+quote(item['version'],safe='')
    result={'name':item['name'],'version':item['version'],'url':url,
            'checked_at_utc':datetime.now(timezone.utc).isoformat()}
    try:
        with urlopen(Request(url,headers={'Accept':'application/json'}),timeout=30) as response:
            raw=response.read(1048577)
            assert len(raw)<=1048576,'Metadata response exceeds finite byte limit'
            data=json.loads(raw)
            assert data['name']==item['name'] and data['version']==item['version'],'Wrong metadata identity'
            result.update({'http_status':response.status,'response_url':response.url,
               'raw_sha256':hashlib.sha256(raw).hexdigest(),'raw_bytes':len(raw),
               'license':data.get('license'),'gitHead':data.get('gitHead'),'repository':data.get('repository'),
               'homepage':data.get('homepage'),'dist_integrity':data.get('dist',{}).get('integrity')})
        name=item['name'].replace('@','').replace('/','__')+'-'+item['version']+'.json'
        target=out/'registry'/name
        target.parent.mkdir(exist_ok=True)
        assert not target.exists()
        target.write_bytes(raw)
        result['snapshot']=target.relative_to(out).as_posix()
    except Exception as exc:
        result['error_type']=type(exc).__name__
        if hasattr(exc,'code'):result['http_status']=exc.code
    return result
with ThreadPoolExecutor(max_workers=4) as pool:
    records=list(pool.map(fetch,observations['records']))
target=out/'registry-source-associations.json'
assert not target.exists()
target.write_text(json.dumps({'product':'Hengshi Design v1','status':'DOING','records':records,
 'limits':'Public version metadata/source associations only; no tarball fetch, registry signature/attestation verification, source build provenance or applicable-licence clearance'},indent=2)+'\n',encoding='utf-8')
print(json.dumps(records,indent=2))
