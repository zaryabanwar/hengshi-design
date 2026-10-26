from pathlib import Path
import hashlib,json,shutil
root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
manifest=out/'review-inputs.json'
assert hashlib.sha256(manifest.read_bytes()).hexdigest()=='a49bc53a70d29228f125e9bb401ce0f2604e68a2bafa48111405b84fc9863d82'
items=json.loads(manifest.read_text(encoding='utf-8'))['inputs']
for item in items:
    for file in [root/item['source'],out/item['snapshot']]:
        raw=file.read_bytes()
        assert len(raw)==item['bytes'] and hashlib.sha256(raw).hexdigest()==item['sha256'],str(file)
brief=root/'docs/phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md'
shutil.copyfile(brief,out/'B01_EXECUTION_BRIEF.before.md')
raw=brief.read_bytes().decode('utf-8')
raw=raw.replace('## Current retry boundary — 2026-10-08','## Earlier return-size retry boundary — 2026-10-08')
raw=raw.replace('October attempts 18, conservatively metered 15.','October attempts 19, conservatively metered 16.')
needle='## Calls, costs and authority'
assert raw.count(needle)==1
raw=raw.replace(needle,'''## Current directory checkpoint — 2026-10-08

Approved corrected call19 succeeded: [exact receipt](../../output/research/b01-directory-call19-2026-10-08/receipt.json),
52 editable references (48 narrow320/four wide1440), two file-local components,
2,674 unique returned node IDs, 52 annotations and zero reported bounds findings.
Composition [27:381](https://www.figma.com/design/GOmLP6Cv96l768ueSrZ5Dg?node-id=27-381)
is present. The compact report is15,080 UTF-8 bytes. No separate checking call ran.

[Independent fifteen-input review](reviews/B01-directory-references-v1-2026-10-08.md)
passes construction/decoded structure and visible composition in the two supplied
scaled PNGs. The narrow132x1024 preview cannot establish320px legibility; fifty
other view pixels were not supplied. All52 full-resolution inspection and full
B01 coverage, interaction, native restore/_EXIT and founder acceptance remain.
A [prepared single batched full-resolution export](../../output/research/b01-directory-full-resolution-2026-10-08/preparation.json)
uses five temporary clone sheets, scale1 images, lossless IDs and checked cleanup
without correcting originals. It is unexecuted and requires fresh per-call approval.

'''+needle)
brief.write_bytes(raw.encode('utf-8'))
inspection=json.loads((out/'inspection.json').read_text(encoding='utf-8'))
inspection['independent_review']='Separate15-input bounded PASS preserved; full-resolution and remaining50 pixels and runtime/full B01 held'
(out/'inspection.json').write_text(json.dumps(inspection,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'review_input_identities_checked':15,'review':'bounded PASS','brief_updated':True}))
