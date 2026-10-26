"""Carry inspected bounded PASS into two navigation records only."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
receipt = ROOT / 'output/research/test-client-graph-2026-10-09/result-review/independent-review-native-notices-v1.json'
assert hashlib.sha256(receipt.read_bytes()).hexdigest() == '00f6b34840473e24150d1d8f8560bb1c609ef47dafeb8fcddedf58791fdc5f1d'
assert json.loads(receipt.read_bytes())['review_decision'] == 'PASS'
state = ROOT / 'PROJECT_STATE.yaml'
mapping = ROOT / 'docs/software-definition/04-reconciliation-map.md'
if (HERE / 'PROJECT_STATE.before-result-review.yaml').exists():
    raise SystemExit('Refuse repeat result-review navigation alignment')
for path in (state, mapping):
    (HERE / (path.stem + '.before-result-review' + path.suffix)).write_bytes(path.read_bytes())
raw = state.read_bytes()
assert raw.count(b'Result/60-notice review pending.') == 1
raw = raw.replace(b'Result/60-notice review pending.', b'Result/60-notice review has 299-input bounded PASS with no findings.')
old = b'Inspect authorized 48-package native-result/notice review, resolve findings within scope and reconcile compatibility references.'
new = b'Preferred-client trial and its authorized result/notice review pass; advance Phase1 definition and reference reconciliation within approved scope.'
assert raw.count(old) == 1
state.write_bytes(raw.replace(old, new))
assert len(state.read_bytes().splitlines()) <= 50
raw = mapping.read_bytes()
old = b'its authorized results/60-notice review is pending.'
new = b'its [299-input results/notice review](../../output/research/test-client-graph-2026-10-09/result-review/independent-review-native-notices-v1.json) has bounded PASS with no findings, covering discovered notice accuracy rather than legal/provenance clearance.'
assert raw.count(old) == 1
raw = raw.replace(old, new)
old = b'The newly frozen results/notice packet is under its authorized review; no review PASS is inferred.'
new = b'The [authorized independent results/notice review](../../output/research/test-client-graph-2026-10-09/result-review/independent-review-native-notices-v1.json) passes its frozen scope with no findings. Current reference links remain outside those inputs.'
assert raw.count(old) == 1
mapping.write_bytes(raw.replace(old, new))
print('Two checkpoint references now reflect inspected bounded PASS; Phase1 stays DOING.')
