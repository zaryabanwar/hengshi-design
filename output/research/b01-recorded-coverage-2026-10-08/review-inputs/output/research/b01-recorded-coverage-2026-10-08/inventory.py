"""Correlate recorded reference names, not live canvas or behavioral coverage."""
from pathlib import Path
import csv,hashlib,json,re
root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
sources={
 'preparation':'output/research/b01-coverage-preparation-2026-10-06/coverage-preparation.json',
 'navigation':'output/research/b01-navigation-composition-2026-10-06/state-ledger.json',
 'directory':'output/research/b01-directory-call19-2026-10-08/decoded-design-result.json',
 'initial_reflow':'output/research/b01-text-reflow-2026-10-06/retry-11/provider-result.json',
 'matrix':'docs/phase-1-ui-reference-design/responsive-state-mode-matrix.csv',
 'templates':'docs/phase-1-ui-reference-design/reference-template-inventory.csv',
 'batch':'docs/phase-1-ui-reference-design/design-batch-plan.csv',
 'ledger':'docs/phase-1-ui-reference-production/validation/mcp-call-ledger.csv',
 'recovery_preparation':'output/research/b01-recovery-composition-preparation-2026-10-07/preparation.json',
 'navigation_inspection':'output/research/b01-navigation-recovery-2026-10-07/inspection.json',
 'directory_review':'docs/phase-1-ui-reference-production/reviews/B01-directory-references-v1-2026-10-08.md',
 'brief':'docs/phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md',
}
identities=[]
def load(key):return json.loads((root/sources[key]).read_bytes())
prep=load('preparation')
for key in ['matrix','templates','batch']:
 old=next(x for x in prep['sources'] if x['path']==sources[key])
 assert hashlib.sha256((root/sources[key]).read_bytes()).hexdigest()==old['sha256']
nav=load('navigation'); directory=load('directory')
raw_initial=load('initial_reflow')
initial=json.loads(next(x['text'] for x in raw_initial['content'] if x['type']=='text'))
frames=[]
pattern=re.compile(r'^HSD_UIR_B01_(TPL_[A-Z_]+)_REF_(STATE_[A-Z_]+)_(VP_[A-Z0-9_]+)_(MODE_[A-Z_]+)_STREAM_(HIGH|LOW|MEDIUM|SEMANTIC)_V01$')
for family,items in [('initial_reflow',initial['frames']),('navigation',nav['frames']),('directory',directory['frames'])]:
 for f in items:
  name=f.get('name') or f['reference']['name']
  m=pattern.fullmatch(name)
  row={'source_family':family,'node_id':f['id'],'recorded_name':name,'width':f['width'],'height':f['height']}
  if m:
   row.update(dict(zip(['template_id','state_id','viewport_id','mode_id','stream_id'],[v.replace('_','-') for v in m.groups()[:4]]+['S-'+m.group(5)])))
  else: row['explicit_axis_binding']='not encoded by this recorded draft name; no inferred stream/state credit'
  frames.append(row)
assert len({f['node_id'] for f in frames})==len(frames)
required=prep['required_stream_state_focus']
def key(x):return tuple(x[k] for k in ['template_id','state_id','stream_id'])
assert len({key(x) for x in required})==len(required)
coverage=[]
for need in required:
 matches=[f for f in frames if 'template_id' in f and key(f)==key(need)]
 coverage.append({**need,'recorded_frame_ids':[f['node_id'] for f in matches],
   'evidence_scope':'Name/axis correlation only; not pixel, interaction, applicability or complete profile proof'})
profiles=list(csv.DictReader((root/sources['matrix']).read_text(encoding='utf-8-sig').splitlines()))
templates=list(csv.DictReader((root/sources['templates']).read_text(encoding='utf-8-sig').splitlines()))
profile_rows=[]
for template in templates:
 if template['template_id'] not in prep['batch']['primary_template_ids'].split(';'): continue
 authored=[f for f in frames if f.get('template_id')==template['template_id']]
 for field,axis in [('state_profile','state_id'),('viewport_profile','viewport_id'),('mode_profile','mode_id')]:
  profile=next(p for p in profiles if p['profile_id']==template[field])
  observed=sorted({f[axis] for f in authored})
  values=profile['required_values'].split(';')
  profile_rows.append({'template_id':template['template_id'],'profile_id':profile['profile_id'],
    'required_values':values,'recorded_name_values':observed,
    'values_not_encoded_in_recorded_names':[v for v in values if v not in observed],
    'minimum_evidence':profile['minimum_evidence'],'critical_distinct_frame_values':profile['critical_distinct_frame_values'],
    'limit':'Missing name is not proof that no annotation exists; only full governed profile adjudication can discharge a requirement'})
for keyname,rel in sources.items():
 raw=(root/rel).read_bytes()
 identities.append({'key':keyname,'path':rel,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
summary={'recorded_frames':len(frames),'explicit_axis_frames':sum('template_id' in f for f in frames),
 'required_stream_state_subset':len(coverage),'subset_with_recorded_names':sum(bool(c['recorded_frame_ids']) for c in coverage),
 'subset_without_recorded_names':sum(not c['recorded_frame_ids'] for c in coverage)}
result={'product':'Hengshi Design v1','status':'DOING','sources':identities,'summary':summary,
 'recorded_frames':frames,'stream_state_subset':coverage,'profile_name_inventory':profile_rows,
 'limits':['Recorded provider/reference receipts only, not a fresh Figma canvas read',
 'Six generic draft names receive no invented explicit-axis credit',
 '56 requirements are the stream/state focus subset, not complete B01 obligations or a Cartesian-product frame count',
 'Names and counts prove no pixel acceptance, prototype, focus, accessibility, browser/device behavior or full profile adjudication',
 'Prepared48 recovery grammar specimens are unexecuted and explicitly not full host/stream/profile coverage',
 'No external call, design change, production UI, package/runtime adoption, Git action, B01 EXIT, later-batch release or Phase1 acceptance']}
target=out/'recorded-coverage.json'
assert not target.exists()
target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'summary':summary,'missing_subset':[x for x in coverage if not x['recorded_frame_ids']]}))
