from pathlib import Path
import hashlib,json,struct
root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
paths=[
 'AGENTS.md','.specify/memory/constitution.md','DECISIONS.md','PROJECT_STATE.yaml',
 'docs/software-definition/definition-walkthrough.html',
 'docs/phase-1-architecture/contracts/DATA_CONTRACT.md',
 'docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md',
 'docs/phase-1-architecture/contracts/reviews/record-purpose-binding-v1-2026-10-08.md',
 'output/research/record-policy-walkthrough-2026-10-08/definition-walkthrough.before.html',
 'output/research/record-policy-walkthrough-2026-10-08/update_walkthrough.py',
 'output/research/record-policy-walkthrough-2026-10-08/inspect.js',
 'output/playwright/record-policy-2026-10-08/desktop-inspection.txt',
 'output/playwright/record-policy-2026-10-08/mobile-inspection.txt',
 'output/playwright/record-policy-2026-10-08/console.txt',
 'output/playwright/record-policy-2026-10-08/record-policy-1440.png',
 'output/playwright/record-policy-2026-10-08/record-policy-320.png'
]
target=out/'review-inputs.json'
assert not target.exists()
inputs=[]
for rel in paths:
 raw=(root/rel).read_bytes()
 snap=out/'review-inputs'/rel
 snap.parent.mkdir(parents=True,exist_ok=True)
 assert not snap.exists()
 snap.write_bytes(raw)
 item={'source':rel,'snapshot':snap.relative_to(out).as_posix(),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
 if rel.endswith('.png'):
  assert raw[:8]==b'\x89PNG\r\n\x1a\n'
  item['width'],item['height']=struct.unpack('>II',raw[16:24])
 inputs.append(item)
observations=[]
for mode in ['desktop','mobile']:
 raw=(root/('output/playwright/record-policy-2026-10-08/'+mode+'-inspection.txt')).read_text(encoding='utf-8-sig')
 assert raw.startswith('### Result\n'),mode
 result=json.loads(raw.splitlines()[1])
 observations.append({'mode':mode,**result})
manifest={'product':'Hengshi Design v1','status':'DOING','scope':'Record-purpose visual translation and two static-browser widths only; no legal clearance, production UI, full accessibility, mobile hardware or processing runtime proof','inputs':inputs,'producer_observations':observations}
target.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'inputs':len(inputs),'manifest_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'image_dimensions':[(x['width'],x['height']) for x in inputs if 'width' in x]}))
