from pathlib import Path
import base64, hashlib, io, json, tarfile, urllib.request

root=Path.cwd()
out=root/'output/research/frontend-bundled-sbom-2026-10-08'
lock=root/'output/research/frontend-three-remedy-evaluation-2026-10-06/candidate/package-lock.json'
archive=root/'output/research/optional-wasm-bundle-2026-10-06/oxide-wasm32-wasi-4.3.3.tgz'
assert not (out/'archive-metadata.json').exists()
raw=archive.read_bytes()
entry=json.loads(lock.read_text(encoding='utf-8'))['packages']['node_modules/@tailwindcss/oxide-wasm32-wasi']
assert hashlib.sha512(raw).digest()==base64.b64decode(entry['integrity'].split('-',1)[1],validate=True)
prior=json.loads((root/'output/research/optional-wasm-contents-2026-10-06/contents.json').read_text(encoding='utf-8'))
metadata=[]
with tarfile.open(fileobj=io.BytesIO(raw),mode='r:gz') as tf:
    for record in prior['packages']:
        member=tf.getmember(record['path'])
        assert member.isfile() and member.size<1024*1024
        data=tf.extractfile(member).read()
        assert hashlib.sha256(data).hexdigest()==record['sha256']
        metadata.append({'archive_path':record['path'],'sha256':record['sha256'],'package':json.loads(data.decode('utf-8'))})
assert len(metadata)==7
(out/'archive-metadata.json').write_text(json.dumps({'archive_path':archive.relative_to(root).as_posix(),'archive_sha256':hashlib.sha256(raw).hexdigest(),'integrity_matches_lock':True,'lock_sha256':hashlib.sha256(lock.read_bytes()).hexdigest(),'records':metadata},indent=2)+'\n',encoding='utf-8')
url='https://raw.githubusercontent.com/spdx/spdx-spec/v2.3/schemas/spdx-schema.json'
with urllib.request.urlopen(url,timeout=30) as response:
    schema=response.read(256*1024)
json.loads(schema)
(out/'spdx-schema.json').write_bytes(schema)
(out/'schema-source.json').write_text(json.dumps({'url':url,'sha256':hashlib.sha256(schema).hexdigest(),'scope':'Official SPDX 2.3 JSON schema corresponding to npm12 exporter format; not production dependency selection'},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'metadata_packages':len(metadata),'archive_integrity_matches_lock':True,'schema_bytes':len(schema)}))
