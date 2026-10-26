from pathlib import Path
import csv, hashlib, json, shutil

root = Path(__file__).resolve().parents[3]
packet = Path(__file__).resolve().parent
source = root / 'output/research/b01-directory-preflight-refresh-2026-10-07/figma-call.js'
raw = source.read_bytes()
assert hashlib.sha256(raw).hexdigest() == '4c811c9122bc049af4b5a01561a97b563c5eed849e9fab20809cdb54b67b62b8'
shutil.copyfile(source, packet / 'approved-prepared-script.js')
result = json.loads((packet / 'provider-result.json').read_text(encoding='utf-8'))
assert result['isError'] is True
assert result['structuredContent']['safeToRetryWithoutCanvasRead'] is True
assert result['structuredContent']['error']['message'] == 'Return value exceeds the 20480-byte limit (43790 bytes). Canvas edits from this run were not committed.'
receipt = {
    'product': 'Hengshi Design v1', 'status': 'DOING',
    'approval': 'reconnected—approve one retry.',
    'scope': 'one attempt18 for the same 52 directory/search references and two file-local components with preflight and representative previews',
    'fileKey': 'GOmLP6Cv96l768ueSrZ5Dg', 'attempt': 18,
    'conservative_metered_attempt': 15,
    'result': result['structuredContent'],
    'canvas_edits_committed': False, 'canvas_statement_basis': 'provider explicit error; no independent canvas reread',
    'design_result_returned': False, 'created_ids_returned': False, 'preview_returned': False,
    'actual_provider_debit_and_balance': 'unknown', 'approval_consumed': True,
    'retry_performed': False, 'script_sha256': hashlib.sha256(raw).hexdigest()
}
(packet / 'receipt.json').write_text(json.dumps(receipt, indent=2, ensure_ascii=True) + '\n', encoding='utf-8')
ledger = root / 'docs/phase-1-ui-reference-production/validation/mcp-call-ledger.csv'
rows = list(csv.reader(ledger.read_text(encoding='utf-8').splitlines()))
assert rows[-1][0] == '19', 'Do not duplicate or overwrite later calls'
shutil.copyfile(ledger, packet / 'mcp-call-ledger.before.csv')
with ledger.open('a', encoding='utf-8', newline='') as stream:
    csv.writer(stream, lineterminator='\n').writerow([
        '20', '2026-10-08', 'use_figma', 'B01',
        'Founder-approved one retry of 52 directory references and two file-local components',
        'metered_assumed', 'no',
        'October attempt18 conservative metered15; provider INVALID_ARGUMENT says returned data43790 bytes exceeds20480 limit and canvas edits not committed; safeToRetryWithoutCanvasRead true; no design IDs or previews returned; exact approved script and provider receipt preserved in output/research/b01-directory-call18-2026-10-08; approval consumed no retry; actual debit/balance unknown; preserve52 views and two components while preparing a lossless compact receipt before requesting another call; full B01 acceptance held'
    ])
cap = root / 'docs/phase-1-ui-reference-production/validation/capability-evidence.md'
shutil.copyfile(cap, packet / 'capability-evidence.before.md')
with cap.open('a', encoding='utf-8', newline='') as stream:
    stream.write('''

## B01 directory call 18 — return-size rejection, 2026-10-08

Status: DOING. Founder said **“reconnected—approve one retry.”** One attempt ran
the same prepared 52 directory/search references and two file-local components,
with preflight and representative previews in that call. The script SHA256 remains
`4c811c9122bc049af4b5a01561a97b563c5eed849e9fab20809cdb54b67b62b8`.
The [exact provider result](../../../output/research/b01-directory-call18-2026-10-08/provider-result.json)
is `INVALID_ARGUMENT`: return value 43,790 bytes exceeds 20,480 bytes. The provider
explicitly says **canvas edits were not committed** and returns
`safeToRetryWithoutCanvasRead: true`. No design IDs or preview images were returned.
This is provider rollback evidence, not an independent subsequent canvas reread.

The [receipt](../../../output/research/b01-directory-call18-2026-10-08/receipt.json)
records October attempt18 / conservative metered15; actual debit/balance unknown.
Permission is consumed; no retry, separate inspection or identity call followed.
Prepare a smaller lossless returned report without reducing the approved visual
scope; another call still needs fresh CB-06/CB-07 approval. Previous designs retain
their own evidence. Full coverage, inspection, independent review, native
exports/restore, _EXIT and founder pilot acceptance remain held.
''')
print(json.dumps({'attempt': 18, 'ledger_sequence': 20, 'provider_rollback_statement': True, 'retry': False}))
