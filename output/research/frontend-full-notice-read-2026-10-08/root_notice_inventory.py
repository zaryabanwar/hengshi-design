"""Repair the earlier root prefix-only inventory, without interpreting licences."""
from pathlib import Path
import hashlib,json,re
root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
prior_file=root/'output/research/frontend-supply-chain-2026-10-06/licence-inventory.json'
prior=json.loads(prior_file.read_text(encoding='utf-8'))
base=root/'output/research/frontend-three-remedy-evaluation-2026-10-06/candidate'
lock=(base/'package-lock.json').read_bytes()
digest=lambda b:hashlib.sha256(b).hexdigest()
assert digest(lock)==prior['lock_sha256']
name_match=re.compile(r'licen[cs]e|notice|copying|copyright|third[-_]party|thirdparty',re.I)
records=[]
for item in prior['records']:
    if not item['installed']:continue
    folder=base/item['lock_path']
    metadata=(folder/'package.json').read_bytes()
    assert digest(metadata)==item['metadata_sha256']
    known={Path(x['path']).name:x for x in item['top_level_licence_and_notice_files']}
    found=[]
    for path in sorted(folder.iterdir()):
        if not path.is_file() or not name_match.search(path.name):continue
        assert not path.is_symlink(),str(path)
        raw=path.read_bytes()
        try:raw.decode('utf-8',errors='strict'); utf8=True
        except UnicodeDecodeError:utf8=False
        if path.name in known:
            assert digest(raw)==known[path.name]['sha256'] and len(raw)==known[path.name]['bytes']
        target=out/'root-notice-copies'/item['lock_path']/path.name
        target.parent.mkdir(parents=True,exist_ok=True)
        assert not target.exists()
        target.write_bytes(raw)
        found.append({'source':path.relative_to(root).as_posix(),'name':path.name,
           'bytes':len(raw),'sha256':digest(raw),'utf8':utf8,
           'already_in_prefix_inventory':path.name in known,'snapshot':target.relative_to(out).as_posix()})
    assert set(known)<=set(x['name'] for x in found)
    records.append({'name':item['name'],'version':item['version'],'lock_path':item['lock_path'],
                    'metadata_sha256':digest(metadata),'notice_name_candidates':found})
for item in records:
    assert digest((base/item['lock_path']/'package.json').read_bytes())==item['metadata_sha256']
    for file in item['notice_name_candidates']:
        raw=(root/file['source']).read_bytes()
        assert len(raw)==file['bytes'] and digest(raw)==file['sha256']
assert (base/'package-lock.json').read_bytes()==lock
result={'product':'Hengshi Design v1','status':'DOING','records':records,
 'prior_inventory_sha256':digest(prior_file.read_bytes()),'candidate_lock_sha256':digest(lock),
 'limits':'Immediate files only, broader filename heuristic; not a recursive distribution/bundled-notice classifier, applicability/attribution decision, archive provenance, all-platform/deployed inventory or clearance'}
target=out/'root-notice-name-inventory.json'
assert not target.exists()
target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
all_files=[f for p in records for f in p['notice_name_candidates']]
print(json.dumps({'installed_locations':len(records),'notice_name_candidates':len(all_files),
 'previously_copied':sum(f['already_in_prefix_inventory'] for f in all_files),
 'newly_retained':[{'source':f['source'],'bytes':f['bytes'],'utf8':f['utf8']} for f in all_files if not f['already_in_prefix_inventory']],
 'candidate_lock_unchanged':True},indent=2))
