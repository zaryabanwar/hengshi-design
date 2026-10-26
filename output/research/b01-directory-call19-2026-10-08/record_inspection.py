from pathlib import Path
import hashlib,json,shutil
root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
report=json.loads((out/'decoded-design-result.json').read_text(encoding='utf-8'))
inspection={'product':'Hengshi Design v1','status':'DOING','attempt':19,
 'producer_structure':{'created_ids':2674,'unique':True,'views':52,'components':2,
   'widths':{'320':48,'1440':4},'returned_bounds_findings':0,'report_utf8_bytes':15080},
 'inspected_previews':['narrow-results.png','wide-open.png'],
 'visible_findings':'No obvious horizontal clipping, overlap or missing major region in the two returned previews. Current delivery and pending selection are separately displayed; Apply remains distinct. Synthetic fixture marking and canonical department labels/paths are visible.',
 'pixel_limit':'Narrow image132x1024 and wide720x829 are scaled. Full-resolution typography, all52 views and other profile interactions remain unverified.',
 'remaining_pixels':'50 views not returned at all; all52 full-resolution pixels still needed',
 'independent_review':'15 frozen inputs commissioned separately; verdict pending',
 'scope':'Producer returned-data and representative pixel inspection only; no working search/radios/focus, screen-reader, physical-device, full B01, final branding or Phase1 acceptance'}
(out/'inspection.json').write_text(json.dumps(inspection,indent=2)+'\n',encoding='utf-8')
cap=root/'docs/phase-1-ui-reference-production/validation/capability-evidence.md'
shutil.copyfile(cap,out/'capability-evidence.before.md')
with cap.open('a',encoding='utf-8',newline='') as stream:
    stream.write('''

## B01 directory call 19 — corrected return succeeded, 2026-10-08

Status: DOING. Founder approved one corrected retry. The [exact executed source](../../../output/research/b01-directory-call19-2026-10-08/executed-call.js)
SHA256 is `5a84f47c0b09d8d2ac3d922840db2a2e2a480a151a4c9b5d501950db6a1af404`.
Construction bytes match the prior prepared scope; only the returned report is
losslessly compacted. The [provider result](../../../output/research/b01-directory-call19-2026-10-08/provider-result.json)
returned `isError: false`, a complete 15,080-byte report and two native PNGs.

The [decoded result](../../../output/research/b01-directory-call19-2026-10-08/decoded-design-result.json)
contains 2,674 unique created IDs, 52 frame/annotation pairs, two components,
48 narrow320 and four wide1440 views, with zero reported invalid-size or horizontal
overflow findings. Composition is `27:381`; sources `27:372`; components
`27:374` / `27:377`. Existing Page1/style/variable/component preflight ran in the
same call. No separate identity, metadata, font or checking call was used.

[Producer inspection](../../../output/research/b01-directory-call19-2026-10-08/inspection.json)
finds no obvious clipping/overlap in the two returned previews, but they are
scaled: narrow132x1024 and wide720x829. The other fifty view pixels were not
returned; all52 full-resolution typography/layout inspection remains held.
Two illustrative screenshots establish no working search, focus, radio, storage,
keyboard, screen-reader or physical-device behavior. Required design/accessibility
review is separately commissioned at fifteen frozen inputs, not complete yet.

The [receipt](../../../output/research/b01-directory-call19-2026-10-08/receipt.json)
records October attempt19 / conservative metered16; actual debit/balance unknown.
Permission is consumed. No further call, new page/library, sharing change,
application implementation or full B01/Phase1 acceptance follows. Native
post-write exports/restore, _EXIT, complete coverage and founder acceptance remain.
''')
print(json.dumps({'inspection':'two representative scaled previews','structural_bounds_findings':0,'full_resolution_held':True}))
