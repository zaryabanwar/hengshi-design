"""Use the existing B01 authority for changing call state in two task indexes."""
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
tasks = ROOT / 'TASKS.md'
actions = ROOT / 'MANUAL_ACTIONS.md'
if (HERE / 'TASKS.before.md').exists():
    raise SystemExit('Refuse repeat task/action consolidation')
for path in (tasks, actions):
    (HERE / (path.stem + '.before.md')).write_bytes(path.read_bytes())
raw = tasks.read_bytes()
start = raw.index(b'D-075 B01 execution/native PRE')
ending = b'Full coverage/review/restore/pilot acceptance remain.'
finish = raw.index(ending, start) + len(ending)
replacement = b'D-075 B01 execution/native PRE and initial/navigation/directory references retain scoped evidence. The [B01 brief](docs/phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md#current-directory-checkpoint--2026-10-08) owns current coverage, reference IDs and review limits; its [call ledger](docs/phase-1-ui-reference-production/validation/mcp-call-ledger.csv) owns running usage and attempt outcomes. Latest comparison-export attempt21 also failed reauthentication, with no images/design receipt and unverified source changes. Renew the connection and provide fresh immediate call approval before further Figma execution. Full-resolution inspection, complete coverage/interaction/accessibility, restore/_EXIT and pilot acceptance remain; later batches stay gated.'
tasks.write_bytes(raw[:start] + replacement + raw[finish:])
lines = actions.read_bytes().splitlines(keepends=True)
for index, line in enumerate(lines):
    if line.startswith(b'| B01; CB-06/CB-07 |'):
        ending = b'\r\n' if line.endswith(b'\r\n') else b'\n'
        lines[index] = b'| B01; CB-06/CB-07 | DOING | Full pilot exit held; export connection requires renewal | D-075 grants execution, with private sharing, zero spend and fresh immediate approval for each call. Current coverage, source IDs/review scope and running usage belong to the [B01 brief](docs/phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md#current-directory-checkpoint--2026-10-08) and [call ledger](docs/phase-1-ui-reference-production/validation/mcp-call-ledger.csv), not duplicated counts here. Latest export retry attempt21 returned reauthentication error, no images/design receipt and unverified source changes; permission consumed. | [Latest receipt](output/research/b01-directory-full-resolution-2026-10-08/attempt21-2026-10-09/receipt.json). Renew Figma connection and explicitly approve one call before another attempt. Full-resolution inspection, missing states/axes, interactions/accessibility, editable native exports/restore/_EXIT and founder pilot acceptance remain; later batches gated. |' + ending
actions.write_bytes(b''.join(lines))
assert len(actions.read_bytes().splitlines()) <= 50
print('Task/action indexes point to one B01 call authority; no repeated running counts or new approval.')
