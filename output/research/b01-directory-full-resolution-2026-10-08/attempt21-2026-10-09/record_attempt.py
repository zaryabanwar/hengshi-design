"""Record one terminal Figma attempt in its two controlling records."""
from pathlib import Path
import csv
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
receipt = json.loads((HERE / 'receipt.json').read_bytes())
assert receipt['october_attempt'] == 21 and receipt['is_error']
ledger = ROOT / 'docs/phase-1-ui-reference-production/validation/mcp-call-ledger.csv'
brief = ROOT / 'docs/phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md'
if (HERE / 'brief.before.md').exists():
    raise SystemExit('Refuse repeat terminal call recording')
rows = list(csv.reader(ledger.read_text(encoding='utf-8-sig').splitlines()))
assert rows[-1][0] == '22'
(HERE / 'brief.before.md').write_bytes(brief.read_bytes())
assert (HERE / 'ledger.before.csv').read_bytes() == ledger.read_bytes()
with ledger.open('a', newline='', encoding='utf-8') as handle:
    csv.writer(handle).writerow(['23','2026-10-09','use_figma','B01',
        'Founder-approved single retry of existing52 directory comparison export','metered_assumed','no',
        'October attempt21 conservative metered18; provider isError true reauthentication required; no exported images or design receipt returned; exact script and provider response preserved in output/research/b01-directory-full-resolution-2026-10-08/attempt21-2026-10-09; approval consumed actual debit/balance unknown; no further call before reconnection and fresh immediate approval; source changes unverified; full B01 scope held'])
raw = brief.read_bytes()
old = b'Approved attempt20 returned a reauthentication error and no images/design receipt; source changes were not verified. Reconnect and obtain fresh per-call permission before a retry. See the [failed attempt receipt](../../output/research/b01-directory-full-resolution-2026-10-08/attempt20-2026-10-09/receipt.json).'
new = b'Approved attempt20 and its single approved retry attempt21 both returned reauthentication errors and no images/design receipt; source changes were not verified. Reconnect and obtain fresh per-call permission before another call. See the [latest failed attempt receipt](../../output/research/b01-directory-full-resolution-2026-10-08/attempt21-2026-10-09/receipt.json); the preceding attempt remains preserved separately.'
assert raw.count(old) == 1
raw = raw.replace(old, new)
assert raw.count(b'October attempts 20, conservatively metered 17') == 1
raw = raw.replace(b'October attempts 20, conservatively metered 17', b'October attempts 21, conservatively metered 18')
raw = raw.replace(b'the later directory export attempt20 failed authentication and a retry requires fresh approval.', b'the later directory export attempts20/21 failed authentication and another call requires reconnection and fresh approval.')
raw = raw.replace(b'separate reauthentication/fresh-retry gate after attempt20;', b'separate reauthentication/fresh-retry gate after attempt21;')
brief.write_bytes(raw)
print('Attempt21 recorded in ledger and B01 brief; zero images, retry held, no source-state assertion.')
