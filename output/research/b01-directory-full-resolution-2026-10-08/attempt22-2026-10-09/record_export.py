"""Record the single consumed permission and bounded pixel inspection."""
from pathlib import Path
import csv, json

here = Path(__file__).resolve().parent
root = here.parents[3]
ledger = root / 'docs/phase-1-ui-reference-production/validation/mcp-call-ledger.csv'
brief = root / 'docs/phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md'
assert ledger.read_bytes() == (here / 'ledger.before.csv').read_bytes()
assert brief.read_bytes() == (here / 'brief.before.md').read_bytes()
receipt = json.loads((here / 'receipt.json').read_bytes())
assert receipt['october_attempt'] == 22 and not receipt['is_error']
receipt['visual_inspection'] = 'PASS — producer static pixels only'
receipt['inspection'] = {'source_ids': [item['source_id'] for item in json.loads((here / 'pixel-inventory.json').read_bytes())], 'comparison_groups_inspected': list(range(1, 14)), 'findings': [], 'observations': ['All 48 narrow references and four wide references are legible without observed clipping or overlapping text.', 'Search states distinguish empty, results, no results, pending, unavailable, offline, error and stale results.', 'All four streams retain equivalent department/navigation actions; current versus pending choice is distinct before Apply.', 'Preference read/write failure and applied-stream states display their respective recovery information.'], 'limits': 'Screenshots cannot prove keyboard operation, links, announcements, focus behavior, accessibility compliance, full B01 coverage or acceptance.'}
(here / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
with ledger.open('a', encoding='utf-8', newline='') as handle:
    csv.writer(handle).writerow(['24', '2026-10-09', 'use_figma', 'B01', 'Founder-approved single reconnected retry of existing52 directory comparison export', 'metered_assumed', 'no', 'October attempt22 conservative metered19; isError false; five scale-one PNG sheets and all52 exact tile crops preserved and producer-inspected; geometry/text/positions/parent-order preservation and removal1173 temporary nodes reported PASS; source corrections none; exact response script report inventory and receipt in output/research/b01-directory-full-resolution-2026-10-08/attempt22-2026-10-09; permission consumed actual debit/balance unknown; independent pixels/interaction/full B01 coverage/native restore EXIT/acceptance held; no additional call authorized'])
raw = brief.read_bytes()
old = b'Approved attempt20 and its single approved retry attempt21 both returned reauthentication errors and no images/design receipt; source changes were not verified. Reconnect and obtain fresh per-call permission before another call. See the [latest failed attempt receipt](../../output/research/b01-directory-full-resolution-2026-10-08/attempt21-2026-10-09/receipt.json); the preceding attempt remains preserved separately.'
new = b'Attempts20/21 returned reauthentication errors; both are preserved. After the founder confirmed reconnection and approved one retry, attempt22 exported five scale-one sheets covering all52 existing directory views. All52 exact crops were producer-inspected with no observed clipping or overlapping text. Source geometry/text/positions/parent order were preserved and all1,173 temporary nodes removed. See the [successful export and bounded inspection receipt](../../output/research/b01-directory-full-resolution-2026-10-08/attempt22-2026-10-09/receipt.json). Independent pixel review, interaction, full B01 coverage and native restore/_EXIT/acceptance remain held; permission is consumed and no additional call is authorized.'
assert raw.count(old) == 1
raw = raw.replace(old, new).replace(b'October attempts 21, conservatively metered 18', b'October attempts 22, conservatively metered 19')
raw = raw.replace(b'Status: DOING. Six initial and twenty navigation views inspected;52 directory views created with full-resolution inspection held. Full B01 exit remains held.', b'Status: DOING. Six initial, twenty navigation and52 directory views producer-inspected; independent pixel review and full B01 exit remain held.')
raw = raw.replace(b'the later directory export attempts20/21 failed authentication and another call requires reconnection and fresh approval.', b'the later directory export attempts20/21 failed authentication; approved attempt22 subsequently recovered all52 full-resolution views, with no further call authorized.')
raw = raw.replace(b'separate reauthentication/fresh-retry gate after attempt21;', b'the subsequent authorized attempt22 export is recorded above;')
brief.write_bytes(raw)
print('One successful attempt recorded in the two controlling documents; no further Figma call authorized.')
