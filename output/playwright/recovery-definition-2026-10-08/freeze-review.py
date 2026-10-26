import hashlib, json, shutil, struct
from pathlib import Path

root = Path.cwd()
out = root / 'output/playwright/recovery-definition-2026-10-08'
def dimensions(name):
    return list(struct.unpack('>II', (out / name).read_bytes()[16:24]))

observations = {
    'product': 'Hengshi Design v1', 'status': 'DOING',
    'scope': 'Producer inspection of one documentation disclosure; no application or recovery drill evidence',
    'browser': 'Chrome 154.0.8037.98',
    'desktop_viewport': [1440,1100], 'desktop_document_width': 1440,
    'narrow_viewport': [320,900], 'narrow_document_width': 320,
    'native_summary_space_collapses': True, 'native_summary_enter_reopens': True,
    'source_links_HTTP': [200,200], 'console_errors': 0, 'console_warnings': 0,
    'stable_captures': {n: dimensions(n) for n in ['desktop-1440-stable.png','narrow-320-stable.png']},
    'capture_conditions': 'Browser reduced-motion preference; screenshot animations disabled. No capture CSS changes. Initial narrow-320.png is incomplete/misaligned and excluded. Stable narrow bounds identical before/after; desktop horizontal position changed 7.5px during element capture; supplied complete pixels require independent inspection.',
    'not_proven': ['physical phone','whole-page WCAG','backup completeness','actual RPO/RTO','restore operation','integrated acceptance']
}
(out/'observations.json').write_text(json.dumps(observations,indent=2)+'\n',encoding='utf-8')
paths = [
 'docs/software-definition/definition-walkthrough.html',
 'docs/phase-1-architecture/contracts/QA_RECOVERY.md',
 'docs/phase-1-architecture/contracts/reviews/recovery-measurement-v1-2026-10-08.md',
 'docs/phase-1-foundation/01-product-requirements.md', 'DECISIONS.md', 'AGENTS.md',
 'output/playwright/recovery-definition-2026-10-08/definition-walkthrough.before.html',
 'output/playwright/recovery-definition-2026-10-08/observations.json',
 'output/playwright/recovery-definition-2026-10-08/desktop-1440-stable.png',
 'output/playwright/recovery-definition-2026-10-08/narrow-320-stable.png'
]
snapshots=out/'review-snapshots'
snapshots.mkdir(exist_ok=False)
inputs=[]
for i,p in enumerate(paths):
    src=root/p
    dest=snapshots/f'{i:02d}-{src.name}'
    shutil.copyfile(src,dest)
    data=src.read_bytes()
    inputs.append({'source':p,'snapshot':dest.relative_to(root).as_posix(),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
manifest=out/'review-inputs.json'
manifest.write_text(json.dumps({'product':'Hengshi Design v1','status':'DOING','scope':'New recovery disclosure source and two supplied stable captures only; observations are producer evidence','inputs':inputs},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'manifest_sha256':hashlib.sha256(manifest.read_bytes()).hexdigest(),'captures':observations['stable_captures']}))
