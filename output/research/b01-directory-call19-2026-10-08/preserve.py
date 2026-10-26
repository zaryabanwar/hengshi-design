from pathlib import Path
import base64,csv,hashlib,json,shutil
from PIL import Image
root=Path(__file__).resolve().parents[3]
packet=Path(__file__).resolve().parent
source=root/'output/research/b01-directory-return-recovery-2026-10-08/figma-call.js'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='5a84f47c0b09d8d2ac3d922840db2a2e2a480a151a4c9b5d501950db6a1af404'
shutil.copyfile(source,packet/'executed-call.js')
provider=json.loads((packet/'provider-result.json').read_text(encoding='utf-8'))
assert provider['isError'] is False
texts=[c['text'] for c in provider['content'] if c['type']=='text']
reports=[json.loads(t) for t in texts if t.startswith('{')]
assert len(reports)==1
report=reports[0]
def decode(packed):
    assert packed['encoding']=='prefix-inclusive-ranges-v1'
    ids=list(packed['literalIds'])
    for prefix,ranges in packed['groups']:
        for span in ranges:
            ids.extend(prefix+str(n) for n in (range(span[0],span[1]+1) if isinstance(span,list) else [span]))
    assert len(ids)==len(set(ids))==packed['count']
    return ids
ids=decode(report['createdNodeIds'])
annotation_ids=decode(report['annotationIds'])
assert len(ids)==2674 and len(annotation_ids)==52
script=source.read_text(encoding='utf-8')
start=script.index('const input = ')+len('const input = ')
inputs,_=json.JSONDecoder().raw_decode(script[start:])
frames=[dict(zip(report['frameFields'],row)) for row in report['frames']]
assert len(frames)==52 and {f['inputIndex'] for f in frames}==set(range(52))
for frame in frames:
    frame['reference']=inputs['frames'][frame['inputIndex']]
    assert frame['width']==frame['reference']['width']
    assert frame['height']>0 and frame['id'] in ids
assert sum(f['width']==320 for f in frames)==48
assert sum(f['width']==1440 for f in frames)==4
assert len(report['componentIds'])==2 and set(report['componentIds'])<=set(ids)
findings=[]
for group in report['boundsFindings']:
    issue,parent=group['context']
    for node in decode(group['nodeIds']):
        record={'id':node,'issue':issue}
        if parent is not None:record['parentId']=parent
        findings.append(record)
assert len(findings)==report['boundsFindingCount']
images=[]
for index,content in enumerate(c for c in provider['content'] if c['type']=='image'):
    filename=['narrow-results.png','wide-open.png'][index]
    data=base64.b64decode(content['data'],validate=True)
    (packet/filename).write_bytes(data)
    with Image.open(packet/filename) as im:
        im.verify()
    with Image.open(packet/filename) as im:
        dims=list(im.size)
    images.append({'path':filename,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'pixels':dims})
assert len(images)==2
normalized={'product':'Hengshi Design v1','status':'DOING','createdNodeIds':ids,
 'mutatedNodeIds':report['mutatedNodeIds'],'createdVariableIds':report['createdVariableIds'],
 'createdStyleIds':report['createdStyleIds'],'sourceId':report['sourceId'],
 'compositionId':report['compositionId'],'componentIds':report['componentIds'],
 'frames':frames,'annotationIds':annotation_ids,'boundsFindings':findings,
 'B01Complete':report['B01Complete'],'coveredScope':report['coveredScope'],'limitations':report['limitations']}
(packet/'decoded-design-result.json').write_text(json.dumps(normalized,indent=2)+'\n',encoding='utf-8')
receipt={'product':'Hengshi Design v1','status':'DOING','approval':'Approve one corrected retry',
 'fileKey':'GOmLP6Cv96l768ueSrZ5Dg','attempt':19,'conservative_metered_attempt':16,
 'script_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'isError':False,
 'returned_report_utf8_bytes':len(texts[0].encode('utf-8')),
 'created_node_count':len(ids),'frames':len(frames),'narrow_frames':48,'wide_frames':4,
 'componentIds':report['componentIds'],'sourceId':report['sourceId'],'compositionId':report['compositionId'],
 'bounds_finding_count':len(findings),'previews':images,'approval_consumed':True,
 'actual_provider_debit_and_balance':'unknown','further_calls':0,
 'full_B01_acceptance':False,'inspection':'Two returned representative previews only; remaining50 view pixels not supplied'}
(packet/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
ledger=root/'docs/phase-1-ui-reference-production/validation/mcp-call-ledger.csv'
rows=list(csv.reader(ledger.read_text(encoding='utf-8').splitlines()))
assert rows[-1][0]=='20'
shutil.copyfile(ledger,packet/'mcp-call-ledger.before.csv')
with ledger.open('a',encoding='utf-8',newline='') as stream:
    csv.writer(stream,lineterminator='\n').writerow(['21','2026-10-08','use_figma','B01',
      'Founder-approved corrected52 directory references and two file-local components',
      'metered_assumed','no',
      f'October attempt19 conservative metered16; isError false; complete compact report{receipt["returned_report_utf8_bytes"]} bytes losslessly decoded2674 unique created IDs52 frames52 annotations and two components;48 narrow and4 wide; bounds findings{len(findings)}; two native PNG previews preserved; no separate checking call; exact executed script provider result decoded result and receipt in output/research/b01-directory-call19-2026-10-08; remaining50 directory view pixels interaction complete B01 profiles independent reviews restore EXIT acceptance held; permission consumed actual debit/balance unknown no further calls'])
print(json.dumps(receipt))
