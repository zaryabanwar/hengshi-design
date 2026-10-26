"""Frozen navigation integrity only; no producer execution or runtime testing."""
from pathlib import Path
import json, hashlib, re, urllib.parse, csv, io
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
sha=lambda b:hashlib.sha256(b).hexdigest()
raw=(HERE/'review-inputs.json').read_bytes()
assert sha(raw)=='e097345394a27b01e6fe124802df409218cb13eb1f0081890d1a06159749a1f3'
manifest=json.loads(raw)
assert len(manifest['inputs'])==89
paths={}
for i in manifest['inputs']:
    b=(ROOT/i['snapshot']).read_bytes()
    assert len(b)==i['bytes'] and sha(b)==i['sha256'] and (ROOT/i['path']).read_bytes()==b,i['path']
    paths[i['path']]=ROOT/i['snapshot']
base=HERE/'inputs/output/research/reconciliation-consolidation-2026-10-09'
old_raw=(base/'before/04-reconciliation-map.md').read_bytes()
new_raw=paths['docs/software-definition/04-reconciliation-map.md'].read_bytes()
assert len(old_raw)==94449 and len(new_raw)==26655
old=old_raw.decode().replace('\r\n','\n')
new=new_raw.decode().replace('\r\n','\n')
index=json.loads((base/'prior-subject-index.json').read_text(encoding='utf-8'))
assert len(index)==46
for i in index:
    assert '| '+i['subject']+' | '+i['entry']+' | '+i['prior_context']+' |' in old
    assert '| '+i['subject']+' | '+i['entry']+' |' in new
subjects=re.findall(r'^\| ([^|]+) \| ([^\n]+) \|$',new.split('## One controlling source per subject\n',1)[1].split('\n## ',1)[0],re.M)
assert len(subjects)==48 and subjects[-1][0]=='Rights intake and verified response'
statuses=lambda t:[(m.group(1),m.group(2)) for m in re.finditer(r'^\| (\d+\. [^|]+) \| (TODO|DOING|DONE|BLOCKED) \|',t,re.M)]
assert statuses(old)==statuses(new) and len(statuses(new))==14
headings=lambda t:re.findall(r'^#{1,6} (.+)$',t,re.M)
assert sorted(headings(old))==sorted(headings(new)) and len(headings(old))==11
old_readme=(base/'before/README.md').read_bytes()
current_readme=paths['docs/software-definition/README.md'].read_bytes()
before='retain the detailed review navigation. A receipt applies to its frozen inputs and\nscope; later edits do not replace its hashes or inherit its PASS. Definition,\n'
after='direct readers to the controlling documents and their scoped review receipts. The\nmap preserves its exact earlier evidence history as supporting material, without\nmaintaining another live review journal. A receipt applies to its frozen inputs\nand scope; later edits do not replace its hashes or inherit its PASS. Definition,\n'
newline='\r\n' if b'\r\n' in old_readme else '\n'
before=before.replace('\n',newline).encode()
after=after.replace('\n',newline).encode()
assert old_readme.count(before)==1 and current_readme==old_readme.replace(before,after,1)
def anchors(text):
    result=set(re.findall(r'\bid=[\"\x27]([^\"\x27]+)',text))
    seen={}
    for h in re.findall(r'^#{1,6}\s+(.+?)\s*#*$',text,re.M):
        slug=re.sub(r'[^\w\-\s]','',re.sub(r'<[^>]+>','',h).strip().lower()).replace(' ','-')
        count=seen.get(slug,0); seen[slug]=count+1
        result.add(slug+(f'-{count}' if count else ''))
    return result
links=[]; outside=set()
for rel in ('docs/software-definition/04-reconciliation-map.md','docs/software-definition/README.md'):
    for dest in re.findall(r'\[[^\]]*\]\(([^)]+)\)',paths[rel].read_text(encoding='utf-8')):
        if '://' in dest or dest.startswith('mailto:'):continue
        url=urllib.parse.urlsplit(dest)
        target=((ROOT/rel).parent/url.path if url.path else ROOT/rel).resolve()
        assert target.is_file(),dest
        target_rel=target.relative_to(ROOT).as_posix(); source=paths.get(target_rel,target)
        if target_rel not in paths:outside.add(target_rel)
        if url.fragment:assert urllib.parse.unquote(url.fragment) in anchors(source.read_text(encoding='utf-8')),dest
        links.append({'source':rel,'target':target_rel,'fragment':url.fragment,'frozen':target_rel in paths})
# Nested-target existence only; no broader contract content re-review.
backend=ROOT/'docs/phase-1-compatibility/backend-evidence-2026-10-04.md'
assert 'staff-identity-candidate-dependency-closure--2026-10-08' in anchors(backend.read_text(encoding='utf-8'))
batch=list(csv.DictReader(io.StringIO(paths['docs/phase-1-ui-reference-design/design-batch-plan.csv'].read_text(encoding='utf-8'))))
assert [x['batch_id'] for x in batch]==[f'B{i:02}' for i in range(1,10)]
result={'status':'DOING','scope':'Navigation integrity only','manifest_sha256':sha(raw),'frozen_live_inputs':89,
        'old_map_bytes':len(old_raw),'new_map_bytes':len(new_raw),'prior_index_contexts_exact':46,'retained_subject_entries':46,
        'new_rights_entry':1,'deliverable_status_pairs':statuses(new),'original_headings_preserved':11,'readme_exact_single_segment':True,
        'map_old_crlf_new_lf_observed':True,'readme_original_line_endings_preserved':True,'local_link_occurrences':len(links),'links':links,
        'unchanged_readme_targets_outside_packet_existence_anchor_only':sorted(outside),
        'nested_backend45_anchor_existence_only':{'path':backend.relative_to(ROOT).as_posix(),'sha256_at_check':sha(backend.read_bytes())},
        'batch_ids':[x['batch_id'] for x in batch],
        'limits':'Counts/hashes/link anchors establish artifact integrity only. No underlying contract/metadata/runtime/accessibility tests or whole-package acceptance.'}
(HERE/'independent-navigation-observations-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ('frozen_live_inputs','retained_subject_entries','original_headings_preserved','local_link_occurrences')}))
