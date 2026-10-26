"""Read complete existing own-file text and embedded map sources; never execute them."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re

root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
prior_path=root/'output/research/frontend-notice-discovery-2026-10-08/observations.json'
prior=json.loads(prior_path.read_text(encoding='utf-8'))
base=root/'output/research/frontend-three-remedy-evaluation-2026-10-06/candidate'
lock=base/'package-lock.json'
lock_before=lock.read_bytes()
digest=lambda b:hashlib.sha256(b).hexdigest()
assert digest(lock_before)==prior['candidate_lock_sha256']
text_extensions={'.js','.mjs','.cjs','.ts','.json','.md','.txt','.html','.css','.map'}
terms=re.compile(r'copyright|spdx-license|licen[cs]e|permission is hereby|redistribution',re.I)
comments=re.compile(r'/\*[\s\S]*?\*/|(?m:^[ \t]*//[^\n]*(?:\n[ \t]*//[^\n]*)*)')
records,candidates,maps=[],[],[]
def scan_text(text,origin,whole_readme=False):
    matches=[{'start_character':m.start(),'end_character':m.end(),'term':m.group(0)} for m in terms.finditer(text)]
    if whole_readme and matches:
        candidates.append({'origin':origin,'kind':'complete README containing notice terms',
            'text':text,'text_sha256':digest(text.encode('utf-8'))})
    else:
        for match in comments.finditer(text):
            if terms.search(match.group(0)):
                candidates.append({'origin':origin,'kind':'comment-shaped candidate; not parsed JS',
                    'start_character':match.start(),'end_character':match.end(),
                    'text':match.group(0),'text_sha256':digest(match.group(0).encode('utf-8'))})
    return matches

for item in prior['records']:
    folder=base/item['lock_path']
    observed={f['path']:f for f in item['own_files']}
    enumerated=[]
    exclusions=[]
    for parent,dirs,files in folder.walk(top_down=True,follow_symlinks=False):
        retained=[]
        for name in dirs:
            p=parent/name
            if name=='node_modules':exclusions.append({'path':p.relative_to(folder).as_posix(),'reason':'separately inventoried nested dependency subtree'})
            elif p.is_symlink() or p.is_junction():raise AssertionError('Unexpected linked directory: '+str(p))
            else:retained.append(name)
        dirs[:]=retained
        for name in files:
            p=parent/name
            assert not p.is_symlink(),str(p)
            enumerated.append(p.relative_to(folder).as_posix())
    assert set(enumerated)==set(observed),item['name']
    files=[]
    for rel in sorted(enumerated):
        path=folder/rel
        raw=path.read_bytes()
        before=observed[rel]
        assert len(raw)==before['bytes'] and digest(raw)==before['sha256'],str(path)
        origin={'package':item['name'],'version':item['version'],'path':rel,'file_sha256':digest(raw)}
        record={'path':rel,'bytes':len(raw),'sha256':digest(raw)}
        if path.suffix.lower() not in text_extensions:
            record['scope']='outside text extension allowlist; contents not interpreted'
        else:
            text=raw.decode('utf-8',errors='strict')
            record['scope']='complete UTF8 text read'
            record['term_matches']=scan_text(text,origin,'readme' in path.name.lower())
            if path.suffix.lower()=='.map':
                mapping=json.loads(text)
                assert isinstance(mapping,dict)
                names=mapping.get('sources',[])
                embedded=mapping.get('sourcesContent')
                assert isinstance(names,list)
                assert embedded is None or isinstance(embedded,list)
                if embedded is not None:assert len(embedded)==len(names)
                sources=[]
                for i,name in enumerate(names):
                    value=embedded[i] if embedded is not None else None
                    entry={'index':i,'name':name,'embedded':isinstance(value,str)}
                    if value is not None:
                        assert isinstance(value,str)
                        entry['utf8_bytes']=len(value.encode('utf-8'))
                        entry['sha256']=digest(value.encode('utf-8'))
                        entry['term_matches']=scan_text(value,{**origin,'embedded_source_index':i,'embedded_source_name':name,'embedded_source_sha256':entry['sha256']})
                    sources.append(entry)
                maps.append({'origin':origin,'sources':sources,'sourceRoot':mapping.get('sourceRoot'),
                    'sections_present':'sections' in mapping,'external_sources_not_fetched':True})
        files.append(record)
    records.append({'name':item['name'],'version':item['version'],'lock_path':item['lock_path'],
                    'files':files,'excluded_subtrees':exclusions})

for item in records:
    for file in item['files']:
        raw=(base/item['lock_path']/file['path']).read_bytes()
        assert len(raw)==file['bytes'] and digest(raw)==file['sha256']
assert lock.read_bytes()==lock_before
assert digest(prior_path.read_bytes())==digest((root/'output/research/frontend-notice-discovery-2026-10-08/review-inputs/output/research/frontend-notice-discovery-2026-10-08/observations.json').read_bytes())
result={'product':'Hengshi Design v1','status':'DOING','checked_at_utc':datetime.now(timezone.utc).isoformat(),
 'prior_observations_sha256':digest(prior_path.read_bytes()),'candidate_lock_sha256':digest(lock_before),
 'records':records,'source_maps':maps,'notice_candidates':candidates,
 'limits':['Only eleven named installed own-file distributions, not all dependencies or deployed files',
 'Full reads remove prior8192-byte/12-match/240-character discovery caps; term/comment heuristics are not a language parser or applicable-licence classifier',
 'Complete README and comment-shaped text is candidate evidence only; string/template/regex content can match comment heuristics',
 'Embedded map sources are strings, not executed/resolved paths; null/missing contents and indexed sections are recorded without external fetch',
 'Binary/outside-allowlist content, archive integrity/provenance, all bundled notices and legal interpretation remain unproven',
 'No installation, package script execution, candidate/source/lock mutation, stack adoption, public attribution assembly or legal clearance']}
target=out/'observations.json'
assert not target.exists()
target.write_text(json.dumps(result,indent=2,ensure_ascii=True)+'\n',encoding='utf-8')
print(json.dumps({'packages':len(records),'own_files':sum(len(r['files']) for r in records),
 'full_text_files':sum(f['scope']=='complete UTF8 text read' for r in records for f in r['files']),
 'maps':len(maps),'embedded_sources':sum(s['embedded'] for m in maps for s in m['sources']),
 'notice_candidates':len(candidates),'candidate_lock_unchanged':True}))
