"""Keep current call state in the B01 authority rather than duplicating its ledger."""
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
state = ROOT / 'PROJECT_STATE.yaml'
mapping = ROOT / 'docs/software-definition/04-reconciliation-map.md'
if (HERE / 'PROJECT_STATE.before.yaml').exists():
    raise SystemExit('Refuse repeat state/map consolidation')
for path in (state, mapping):
    (HERE / (path.stem + '.before' + path.suffix)).write_bytes(path.read_bytes())
lines = state.read_bytes().splitlines(keepends=True)
for index, line in enumerate(lines):
    ending = b'\r\n' if line.endswith(b'\r\n') else b'\n'
    if line.startswith(b'  figma_calls:'):
        lines[index] = b'  figma_calls: "Current authority: docs/phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md and validation/mcp-call-ledger.csv. Latest export attempt21 also returned reauthentication error, no images/design receipt; source changes unverified. Approval consumed; renewed connection and fresh immediate permission required before another call. Exact receipt: output/research/b01-directory-full-resolution-2026-10-08/attempt21-2026-10-09/receipt.json."' + ending
    elif line.startswith(b'next_safe_action:'):
        lines[index] = b'next_safe_action: "Preferred-client trial/result-notice review pass; continue remaining Phase1 definitions and successor alignment. Figma full-resolution inspection needs renewed connection and fresh call approval under its B01 authority. Complete visual coverage, stable graph and integrated acceptance remain; commits/pushes deferred."' + ending
state.write_bytes(b''.join(lines))
assert len(state.read_bytes().splitlines()) <= 50
raw = mapping.read_bytes()
start = raw.index(b'The founder approved the three prepared actions.')
finish = raw.index(b'\n\r\n## Route to a coherent checkpoint', start) if b'\n\r\n## Route to a coherent checkpoint' in raw[start:] else raw.index(b'\n\n## Route to a coherent checkpoint', start)
replacement = '''Current Figma state is controlled by the [B01 brief](../phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md#calls-costs-and-authority) and [call ledger](../phase-1-ui-reference-production/validation/mcp-call-ledger.csv), rather than another changing count here. The [latest approved export retry, attempt21](../../output/research/b01-directory-full-resolution-2026-10-08/attempt21-2026-10-09/receipt.json), also failed reauthentication and returned no images/design receipt. Source changes remain unverified; all 52 directory pixels still need full-resolution inspection. Renew the connection and provide fresh immediate approval before another call. Founder visual acceptance follows complete reviewable evidence.

The [preferred-client native result](../phase-1-compatibility/backend-evidence-2026-10-04.md#preferred-client-native-result-and-wheel-notices--2026-10-09) has 18 passing library cases and [bounded results/notice review PASS](../../output/research/test-client-graph-2026-10-09/result-review/independent-review-native-notices-v1.json). Earlier 43-package and distribution evidence remains preserved there. These scoped results select no production graph and grant no new Figma call, other installation or Phase 1 acceptance. Later navigation links remain outside frozen review inputs.'''.encode()
mapping.write_bytes(raw[:start] + replacement + raw[finish:])
print('Two current navigation records consolidated to the B01 call authority; no duplicated running count.')
