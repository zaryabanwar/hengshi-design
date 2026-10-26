"""Reconcile existing failed-call evidence in two task/action indexes only."""
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
tasks = ROOT / 'TASKS.md'
actions = ROOT / 'MANUAL_ACTIONS.md'
if (HERE / 'TASKS.before.md').exists():
    raise SystemExit('Refuse repeat task/action alignment')
for path in (tasks, actions):
    (HERE / (path.stem + '.before.md')).write_bytes(path.read_bytes())
raw = tasks.read_bytes()
old = b'October attempts19/conservative metered16; actual balance unknown; permission consumed, no further call.'
new = b'Later approved [attempt20](output/research/b01-directory-full-resolution-2026-10-08/attempt20-2026-10-09/receipt.json) failed reauthentication and returned no images/design receipt; source changes are unverified. October attempts20/conservative metered17; actual debit/balance unknown. Permission consumed; reconnect and freshly approve one retry before any call.'
assert raw.count(old) == 1
tasks.write_bytes(raw.replace(old, new))
raw = actions.read_bytes()
lines = raw.splitlines(keepends=True)
for index, line in enumerate(lines):
    if line.startswith(b'| B01; CB-06/CB-07 |'):
        ending = b'\r\n' if line.endswith(b'\r\n') else b'\n'
        lines[index] = b'| B01; CB-06/CB-07 | DOING | Directory construction succeeded; full pilot exit held | D-075 grants execution. PRE/six initial drafts/twenty navigation views retain evidence. Call19 created52 directory views/two local components; its15-input review passes bounded construction/structure/visible-preview scope. Approved attempt20 failed reauthentication and returned no images/design receipt, so all52 full-resolution pixels remain uninspected. Source changes are unverified. October attempts20/conservative metered17; actual debit/balance unknown. Permission consumed; no further call or spend. | [Attempt20 receipt](output/research/b01-directory-full-resolution-2026-10-08/attempt20-2026-10-09/receipt.json), [bounded construction review](docs/phase-1-ui-reference-production/reviews/B01-directory-references-v1-2026-10-08.md), [prepared full-resolution export](output/research/b01-directory-full-resolution-2026-10-08/preparation.json) and [ledger](docs/phase-1-ui-reference-production/validation/mcp-call-ledger.csv). Reconnect and explicitly approve one retry under CB-06/CB-07 before execution; five temporary sheets require checked cleanup and no original correction. Full coverage, interactions, native exports/restore/_EXIT and pilot acceptance remain; later batches gated. |' + ending
actions.write_bytes(b''.join(lines))
assert len(actions.read_bytes().splitlines()) <= 50
print('Task and founder-action indexes match retained attempt20 evidence; no Figma call made.')
