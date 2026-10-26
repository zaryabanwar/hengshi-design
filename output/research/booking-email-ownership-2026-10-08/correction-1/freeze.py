from pathlib import Path
import hashlib
import json
import re

root=Path.cwd(); base=root/'output/research/booking-email-ownership-2026-10-08'; out=base/'correction-1'
old=json.loads((base/'review-inputs.json').read_bytes())
paths=[row['path'] for row in old['inputs']]
visual=root/'docs/software-definition/definition-walkthrough.html'
raw=visual.read_bytes(); before=(base/'definition-walkthrough.before.html').read_bytes()
start=raw.index(b'<details id="booking-email">'); end=raw.index(b'</details>\r\n',start)+len(b'</details>\r\n')
assert raw[:start]+raw[end:]==before, 'Unrelated visual content changed'
for target in re.findall(r'\]\(([^)]+)\)', (root/'docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md').read_text(encoding='utf-8').split('## Email ownership control proposal')[1]):
    if not target.startswith('https://'): assert (root/'docs/phase-1-architecture/contracts'/target.split('#')[0]).resolve().is_file()
report=dict(scope='Source/pixel inspection of explanatory documentation panel only',
    desktop=dict(viewport_width=1440,page_width=1440,panel_client_width=1124,panel_scroll_width=1124),
    narrow=dict(viewport_width=320,page_width=320,panel_client_width=276,panel_scroll_width=276),
    keyboard=dict(native_details_open_close=True,tab_enters_first_source_link=True),
    console=dict(errors=0,warnings=0), pixels_inspected=['desktop.png','narrow320.png','narrow-flow.png','narrow-recovery.png','narrow-limits.png'],
    unchanged_outside_panel=True,
    limits='No working form/email/booking control, complete WCAG or physical mobile proof')
dest=out/'visual-inspection.json'; assert not dest.exists(); dest.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
paths += ['docs/software-definition/definition-walkthrough.html']
paths += [str((base/name).relative_to(root)).replace('\\','/') for name in ['definition-walkthrough.before.html','desktop.png','narrow320.png','narrow-flow.png','narrow-recovery.png','narrow-limits.png','capture-visual.js','capture-narrow.js']]
paths += [str(dest.relative_to(root)).replace('\\','/')]
snaps=out/'snapshots'; snaps.mkdir(exist_ok=False); rows=[]
for i,name in enumerate(paths):
    path=root/name; data=path.read_bytes()
    if i<19 and name!='docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md':
        assert hashlib.sha256(data).hexdigest()==old['inputs'][i]['sha256'],name
    snap=snaps/f'{i:02d}-{path.name}'; snap.write_bytes(data)
    rows.append(dict(path=name,snapshot=str(snap.relative_to(root)).replace('\\','/'),bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
prefix=(root/old['prefix']['path']).read_bytes(); cat=(root/'docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md').read_bytes(); assert cat.startswith(prefix)
m=dict(scope=old['scope']+'; explanatory walkthrough source/pixels separately included',correction=1,inputs=rows,prefix=old['prefix'],findings_addressed=['EO01','EO02','EO03'])
data=(json.dumps(m,indent=2)+'\n').encode(); p=out/'review-inputs.json'; assert not p.exists(); p.write_bytes(data)
print(json.dumps(dict(inputs=len(rows),manifest_sha256=hashlib.sha256(data).hexdigest(),catalogue_sha256=hashlib.sha256(cat).hexdigest(),visual_sha256=hashlib.sha256(raw).hexdigest(),unchanged_other_initial_inputs=18,unchanged_prior_prefix_bytes=len(prefix))))
