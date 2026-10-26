"""Update dated navigation references without changing design authority."""
from pathlib import Path
import json, hashlib
root = Path(__file__).resolve().parents[3]
out = Path(__file__).resolve().parent
target = root / 'docs/software-definition/04-reconciliation-map.md'
raw = target.read_bytes()
text = raw.decode('utf-8')
newline = '\r\n' if '\r\n' in text else '\n'
lines = text.splitlines()
rows = [i for i, line in enumerate(lines) if line.startswith('| Production UI references |')]
assert len(rows) == 1
before = out / 'reconciliation-map.before.md'
assert not before.exists()
before.write_bytes(raw)
lines[rows[0]] = '| Production UI references | [Reference design](../phase-1-ui-reference-design/README.md), [production contract](../phase-1-ui-reference-production/README.md) and [B01 brief](../phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md#current-directory-checkpoint--2026-10-08) | DOING. D-075 approves execution, not acceptance. Native PRE/archive and six initial draft pixel inspections are verified. Inter is Figma-only; website system fonts remain. Approved call16 recovered the thirteen missing navigation previews; [all20 navigation views are inspected](../../output/research/b01-navigation-recovery-2026-10-07/inspection.json), with temporary-node cleanup and source geometry/text, positions and parent order checked unchanged. Corrected call19 created52 directory/search views and two file-local components; [independent15-input bounded review](../phase-1-ui-reference-production/reviews/B01-directory-references-v1-2026-10-08.md) covers construction, decoded structure and visible composition in two scaled previews. All52 full-resolution directory pixels remain held. A [prepared five-sheet batched export](../../output/research/b01-directory-full-resolution-2026-10-08/preparation.json) awaits fresh immediate per-call approval. Four ceiling-refusal fixtures remain TODO without invented device facts. October attempts19/conservatively metered16, actual balance unknown; [ledger](../phase-1-ui-reference-production/validation/mcp-call-ledger.csv) controls counts. Complete coverage, interaction/accessibility, post-write editable exports, restore/_EXIT and founder pilot acceptance remain unfinished. |'
start = next(i for i, line in enumerate(lines) if line.startswith("B01's [read-only navigation inspection]"))
end = next(i for i in range(start + 1, len(lines)) if lines[i] == '')
lines[start:end] = [
    'B01 call16 recovered the thirteen navigation views missing from call14; all20',
    'now have [producer pixel inspection](../../output/research/b01-navigation-recovery-2026-10-07/inspection.json).',
    'The [successful corrected call19 checkpoint](../phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md#current-directory-checkpoint--2026-10-08)',
    'adds52 directory/search views and two components. Its bounded independent review',
    'covers source/decoded structure and two scaled previews; all52 full-resolution',
    'directory pixels still need inspection. A prepared single export awaits fresh',
    'CB-06/CB-07 approval. October attempts19/conservatively metered16; actual quota',
    'balance is unknown. Later reference updates do not expand earlier review receipts.',
    'Visual acceptance will be requested when the complete package is reviewable.',
    'Hosting/cost, alias ownership and production records remain explicitly deferred.',
]
updated = (newline.join(lines) + newline).encode('utf-8')
target.write_bytes(updated)
print(json.dumps({'document': target.relative_to(root).as_posix(), 'prior_sha256': hashlib.sha256(raw).hexdigest(), 'updated_sha256': hashlib.sha256(updated).hexdigest(), 'reference_only': True}))
