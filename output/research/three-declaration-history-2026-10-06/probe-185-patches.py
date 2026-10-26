"""Check all earlier stable 185 declaration patches before proposing a fallback."""
from pathlib import Path
from datetime import datetime, timezone
import urllib.request
import hashlib
import base64
import json
import tarfile
import io

OUT=Path(__file__).resolve().parent

def main():
    registry=json.loads((OUT/'types-three-registry.json').read_text(encoding='utf-8'))
    observations=[]
    for version in ('0.185.0','0.185.1','0.185.2','0.185.3'):
        target=OUT/version
        if target.exists():raise RuntimeError('Already observed')
        target.mkdir()
        record=registry['versions'][version]
        (target/'registry.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
        with urllib.request.urlopen(record['dist']['tarball'],timeout=45) as response:data=response.read()
        algorithm,expected=record['dist']['integrity'].split('-',1)
        if base64.b64encode(hashlib.new(algorithm,data).digest()).decode()!=expected:raise RuntimeError('Integrity mismatch')
        (target/'types-three.tgz').write_bytes(data)
        wanted=('src/extras/core/ShapePath.d.ts','src/loaders/DataTextureLoader.d.ts')
        sources={}
        with tarfile.open(fileobj=io.BytesIO(data),mode='r:gz') as tar:
            for member in tar.getmembers():
                relative=next((name for name in wanted if member.name.endswith('/'+name)),None)
                if relative:
                    if not member.isfile() or relative in sources:raise RuntimeError('Invalid selected member')
                    payload=tar.extractfile(member).read()
                    sources[relative]=payload.decode('utf-8')
                    destination=target/relative;destination.parent.mkdir(parents=True,exist_ok=True);destination.write_bytes(payload)
        if len(sources)!=2:raise RuntimeError('Missing selected declarations')
        observations.append({'version':version,'shape_path_user_data_lines':[s.strip() for s in sources[wanted[0]].splitlines() if 'userData' in s],
            'data_texture_loader_parse_lines':[s.strip() for s in sources[wanted[1]].splitlines() if 'parse(' in s],
            'limits':'Source contracts only; no full compiler, runtime, lock or compatibility proof.'})
    (OUT/'185-earlier-patch-observations.json').write_text(json.dumps({'checked_at_utc':datetime.now(timezone.utc).isoformat(),'versions':observations},indent=2)+'\n',encoding='utf-8')
    print(json.dumps(observations,indent=2))

if __name__=='__main__':main()
