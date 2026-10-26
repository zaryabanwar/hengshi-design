from pathlib import Path
import copy, hashlib, importlib.metadata, json
from jsonschema import Draft7Validator

root=Path.cwd(); out=root/'output/research/frontend-bundled-sbom-2026-10-08'
assert not (out/'validation.json').exists()
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
sbom=read(out/'supplemented.spdx.json'); graph=read(out/'graph.json'); bundle=read(out/'archive-metadata.json')
schema=read(out/'spdx-schema.json'); Draft7Validator.check_schema(schema)
validator=Draft7Validator(schema)
def endpoints(document):
    ids={'SPDXRef-DOCUMENT'}|{p['SPDXID'] for p in document['packages']}
    return [r for r in document['relationships'] if r['spdxElementId'] not in ids or r['relatedSpdxElement'] not in ids]
errors=list(validator.iter_errors(sbom))
assert not errors and not endpoints(sbom)
ids=[p['SPDXID'] for p in sbom['packages']]
assert len(ids)==len(set(ids))
by_id={p['SPDXID']:p for p in sbom['packages']}
contains=[r for r in sbom['relationships'] if r['relationshipType']=='CONTAINS']
named=[r for r in bundle['records'] if r['package']['name']!='@tailwindcss/oxide-wasm32-wasi']
expected={(r['package']['name'],r['package']['version']) for r in named}
actual={(by_id[r['relatedSpdxElement']]['name'],by_id[r['relatedSpdxElement']]['versionInfo']) for r in contains}
assert actual==expected and len(contains)==len(named)==6
for r in contains:
    child=by_id[r['relatedSpdxElement']]
    assert child['downloadLocation']=='NOASSERTION' and 'checksums' not in child
    assert child['packageFileName'].startswith('node_modules/@tailwindcss/oxide-wasm32-wasi/node_modules/')
all_edges=[(n,e) for n in graph['nodes'] for e in n['edges']]
absent=[{'from':n['location'],'name':e['name'],'type':e['type']} for n,e in all_edges if e['to'] is None]
assert len(absent)==21 and all(e['type']=='peerOptional' for e in absent)
invalid=[(n['location'],e['name']) for n,e in all_edges if e['error'] not in (None,'MISSING')]
assert not invalid
wrong_type=copy.deepcopy(sbom); wrong_type['relationships'][0]['relationshipType']='NOT_A_RELATIONSHIP'
type_rejected=bool(list(validator.iter_errors(wrong_type))); assert type_rejected
dangling=copy.deepcopy(sbom); dangling['relationships'][0]['relatedSpdxElement']='SPDXRef-does-not-exist'
assert not list(validator.iter_errors(dangling)) and endpoints(dangling)
prior=read(root/'output/research/frontend-supply-chain-2026-10-06/protected-before.json')
changed=[r['path'] for r in prior if hashlib.sha256((root/r['path']).read_bytes()).hexdigest()!=r['sha256']]
checkpoint_records={'DECISIONS.md','PROJECT_STATE.yaml','TASKS.md'}
assert set(changed)==checkpoint_records
assert not [p for p in changed if p not in checkpoint_records]
result={'product':'Hengshi Design v1','status':'DOING','scope':'Supplemented research candidate metadata and standard-format/relationship correlations only',
 'jsonschema_version':importlib.metadata.version('jsonschema'),'schema_errors':len(errors),'unique_spdx_ids':len(ids),'relationship_count':len(sbom['relationships']),
 'initial_virtual_locations':graph['initial_node_count'],'supplemented_virtual_locations':graph['final_node_count'],
 'required_or_invalid_edges_before':len(graph['initial_faults']),'required_or_invalid_edges_after':len(graph['final_faults']),
 'verified_bundled_contains':len(contains),'child_parent_checksum_inference':False,
 'unresolved_optional_peers':absent,'negative_relationship_type_rejected_by_schema':type_rejected,
 'negative_dangling_endpoint_accepted_by_schema_but_rejected_by_correlation':True,
 'historical_protected_inputs_checked':len(prior),'historical_unchanged_inputs':len(prior)-len(changed),
 'historical_checkpoint_records_changed_since_oct6':changed,'application_model_candidate_inputs_changed':[],
 'limits':['Original npm CLI virtual SBOM remains failed; no lock repair or new successful npm command claimed',
 'Complete for this lock-derived metadata plus named bundle occurrences, not all embedded code or actual platform artifacts',
 'No complete notice/attribution/provenance/advisory/compatibility clearance, D-072 isolation, full graph or MA-013 adoption',
 'Shape/correlation controls are not application or package-runtime tests']}
(out/'validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['schema_errors','unique_spdx_ids','relationship_count','supplemented_virtual_locations','required_or_invalid_edges_after','verified_bundled_contains','historical_protected_inputs_checked','historical_unchanged_inputs','historical_checkpoint_records_changed_since_oct6','application_model_candidate_inputs_changed']}))
