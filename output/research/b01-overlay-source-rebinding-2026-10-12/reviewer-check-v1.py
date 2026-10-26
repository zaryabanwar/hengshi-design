"""Independent frozen-input audit; writes temporary evidence only."""
import sys
sys.dont_write_bytecode = True
import copy, csv, hashlib, importlib.util, io, json, re, shutil
from collections import Counter
from pathlib import Path

folder = Path(__file__).resolve().parent
workspace = folder.parents[2]
manifest_path = folder / 'review-inputs-v1.json'
manifest = json.loads(manifest_path.read_text(encoding='utf-8-sig'))
sha = lambda data: hashlib.sha256(data).hexdigest()
def load(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            assert key not in result, ('duplicate JSON key', key)
            result[key] = value
        return result
    return json.loads(path.read_text(encoding='utf-8-sig'), object_pairs_hook=unique)

bindings = []
for item in manifest['inputs']:
    raw = (folder / item['snapshot']).read_bytes()
    assert len(raw) == item['bytes'] and sha(raw) == item['sha256'], item['snapshot']
    live = workspace / item['source']
    bindings.append(dict(item, verified=True, current_bytes=len(live.read_bytes()), current_sha256=sha(live.read_bytes()), current_matches_snapshot=live.read_bytes()==raw))
assert len(bindings) == 24 and len({i['snapshot'] for i in bindings}) == 24
paths = {i['source']: folder / i['snapshot'] for i in manifest['inputs'][:14]}
old = load(folder / manifest['inputs'][14]['snapshot'])
candidate = load(folder / manifest['inputs'][15]['snapshot'])
reported = load(folder / manifest['inputs'][16]['snapshot'])
assert set(paths) == {p['path'] for p in candidate['source_snapshots']}

def walk(a, b, route=()):
    assert type(a) is type(b), route
    if isinstance(a, dict):
        assert a.keys() == b.keys(), route
        for key in a:
            yield from walk(a[key], b[key], route+(key,))
    elif isinstance(a, list):
        assert len(a) == len(b), route
        for key, (x, y) in enumerate(zip(a,b)):
            yield from walk(x,y,route+(key,))
    elif a != b:
        yield (route, a, b)

leaves = list(walk(old,candidate))
quotes, processes, pins = [], [], []
for route, before, after in leaves:
    if route[0]=='records' and route[2]=='sources' and route[4]=='quoted_fact' and len(route)==5:
        i,j=route[1],route[3]
        quotes.append(dict(record_index=i, source_index=j, before=old['records'][i]['sources'][j], after=candidate['records'][i]['sources'][j]))
    elif route[0]=='records' and route[2:] == ('timing_criterion','process_source','quoted_fact'):
        i=route[1]
        processes.append(dict(record_index=i,before=old['records'][i]['timing_criterion']['process_source'],after=candidate['records'][i]['timing_criterion']['process_source']))
    elif route[0]=='source_snapshots' and route[2:] == ('raw_sha256',):
        i=route[1]
        pins.append(dict(path=old['source_snapshots'][i]['path'],before=before,after=after))
    else:
        raise AssertionError(('unauthorized diff',route))
assert len(quotes)==41 and len({q['record_index'] for q in quotes})==33 and len(processes)==3 and len(pins)==3
assert reported['quote_changes']==quotes
assert reported['copied_process_source_changes']==processes
assert reported['snapshot_changes']==pins
assert reported['declared_value_changes']==0 and reported['timing_policy_changes']==0
assert reported['canonical_registry_sha256']==sha((folder/manifest['inputs'][14]['snapshot']).read_bytes())
assert reported['candidate_sha256']==sha((folder/manifest['inputs'][15]['snapshot']).read_bytes())

cache={}
def norm(x): return x.replace('\r\n','\n').replace('\r','\n')
def resolve(w):
    path=w['path']; sel=w['selector']; k=sel['kind']
    raw=paths[path].read_text(encoding='utf-8-sig')
    if k=='csv_record':
        if path not in cache: cache[path]=list(csv.DictReader(io.StringIO(raw,newline='')))
        rows=[r for r in cache[path] if r.get(sel['key_field'])==sel['key_value']]
        assert len(rows)==1 and sel['field'] in rows[0]
        return rows[0][sel['field']]
    if k=='json_pointer':
        value=load(paths[path])
        for token in sel['pointer'].split('/')[1:]:
            token=token.replace('~1','/').replace('~0','~')
            value=value[int(token)] if isinstance(value,list) else value[token]
        return value if isinstance(value,str) else json.dumps(value,ensure_ascii=False,separators=(',',':'))
    if k=='markdown_table_id':
        rows=[line for line in raw.splitlines() if line.lstrip().startswith('|') and line.strip().split('|')[1].strip()==sel['id']]
        assert len(rows)==1
        return rows[0]
    if k=='markdown_section':
        lines=raw.splitlines(); headings=[]; ancestry=[]; fenced=False
        for number,line in enumerate(lines):
            if re.match(r'^\s{0,3}(```|~~~)',line): fenced=not fenced
            match=None if fenced else re.match(r'^(#{1,6})\s+(.+?)(?:\s+#+)?\s*$',line)
            if match:
                level=len(match[1]); ancestry=[v for v in ancestry if v[0]<level]+[(level,match[2])]
                headings.append((number,[v[1] for v in ancestry]))
        matches=[i for i,(_,h) in enumerate(headings) if h==sel['heading_path']]
        assert len(matches)==1
        idx=matches[0]; start=headings[idx][0]; end=headings[idx+1][0] if idx+1<len(headings) else len(lines)
        return '\n'.join(lines[start:end])
    raise AssertionError(k)

all_sources=Counter(); selector_kinds=Counter(); total=0; unique_witnesses=set(); original_bad=[]
for i,record in enumerate(candidate['records']):
    assert record['declared_value']==old['records'][i]['declared_value']
    if 'timing_criterion' in record:
        assert record['timing_criterion']['process_source'] in record['sources']
        assert {k:v for k,v in record['timing_criterion'].items() if k!='process_source'}=={k:v for k,v in old['records'][i]['timing_criterion'].items() if k!='process_source'}
    for j,w in enumerate(record['sources']):
        content=resolve(w)
        assert norm(w['quoted_fact']) in norm(content), (i,j)
        unique_witnesses.add(json.dumps(w,sort_keys=True))
        all_sources[w['path']]+=1; selector_kinds[w['selector']['kind']]+=1; total+=1
        prior=old['records'][i]['sources'][j]
        if norm(prior['quoted_fact']) not in norm(resolve(prior)): original_bad.append((i,j))
assert set(original_bad)=={(q['record_index'],q['source_index']) for q in quotes}
for q in quotes:
    assert norm(q['after']['quoted_fact'])==norm(resolve(q['after'])).rstrip(), (q['record_index'],q['source_index'])
for pin in candidate['source_snapshots']:
    assert pin['raw_sha256']==sha(paths[pin['path']].read_bytes()).upper()

frozen=folder/'reviewer-frozen14-source-root-v1'
frozen.mkdir(exist_ok=False)
for relative,path in paths.items():
    dest=frozen/relative; dest.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(path,dest)
spec=importlib.util.spec_from_file_location('pinned_authority_validator',folder/manifest['inputs'][18]['snapshot'])
module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
verified=module.validate_registry(frozen,candidate)
def rejection(obj):
    try: module.validate_registry(frozen,obj)
    except (ValueError,KeyError,TypeError,OSError) as error: return str(error)
    raise AssertionError('Expected fail-closed rejection')
probes={'original_registry':rejection(old)}
bad=copy.deepcopy(candidate); bad['source_snapshots'][0]['raw_sha256']='0'*64
probes['stale_pin']=rejection(bad)
bad=copy.deepcopy(candidate); bad['records'][quotes[0]['record_index']]['sources'][quotes[0]['source_index']]['quoted_fact']='REVIEWER_NONEXISTENT_FACT_9b72a3'
probes['stale_quote']=rejection(bad)
bad=copy.deepcopy(candidate); i=processes[0]['record_index']; bad['records'][i]['timing_criterion']['process_source']=old['records'][i]['timing_criterion']['process_source']
probes['stale_copied_process_source']=rejection(bad)
bad=copy.deepcopy(candidate); bad['records'][0]['declared_value']='REVIEWER_INVALID_VALUE'
probes['declared_value_mismatch']=rejection(bad)
bad=copy.deepcopy(candidate); bad['records'].pop()
probes['missing_record']=rejection(bad)
bad=copy.deepcopy(candidate); bad['reviewer_bypass']=True
probes['unknown_top_level_field']=rejection(bad)
shutil.copyfile(folder/manifest['inputs'][21]['snapshot'],frozen/'DECISIONS.md')
regpath='docs/phase-1-ui-reference-design/column-authority.json'
(frozen/regpath).write_bytes((folder/manifest['inputs'][15]['snapshot']).read_bytes())
try: module.validate_approval(frozen,regpath,'D-063')
except ValueError as error: probes['candidate_under_predecessor_approval']=str(error)
else: raise AssertionError('Candidate unexpectedly approved')

summary={
 'manifest_sha256':sha(manifest_path.read_bytes()),'bindings':bindings,
 'records':len(candidate['records']),'columns':len(candidate['columns']),'source_pins':len(candidate['source_snapshots']),
 'witnesses':total,'unique_witnesses':len(unique_witnesses),'witnesses_by_source':dict(all_sources),'selector_kinds':dict(selector_kinds),
 'diff_leaves':len(leaves),'quote_changes':len(quotes),'changed_record_indices':sorted({q['record_index'] for q in quotes}),
 'copied_process_source_indices':[p['record_index'] for p in processes],'pin_changes':pins,
 'changed_witness_groups':[dict(path=k[0],selector=json.loads(k[1]),occurrences=n) for k,n in Counter((q['after']['path'],json.dumps(q['after']['selector'],sort_keys=True)) for q in quotes).items()],
 'verified_records':len(verified),'fail_closed_probes':probes,
 'all24_live_sources_match':all(b['current_matches_snapshot'] for b in bindings),
 'changed_records':[dict(index=i,file=candidate['records'][i]['file'],row_id=candidate['records'][i]['row_id'],column=candidate['records'][i]['column'],declared_value=candidate['records'][i]['declared_value']) for i in sorted({q['record_index'] for q in quotes})]
}
(folder/'reviewer-check-results-v1.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ('bindings','witnesses_by_source','changed_records')},ensure_ascii=False,indent=2))
