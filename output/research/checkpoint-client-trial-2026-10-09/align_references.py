"""Update two navigation records; retain exact preceding bytes."""
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
state = ROOT / 'PROJECT_STATE.yaml'
mapping = ROOT / 'docs/software-definition/04-reconciliation-map.md'
if (HERE / 'PROJECT_STATE.before.yaml').exists():
    raise SystemExit('Refuse repeating checkpoint alignment')
for path in (state, mapping):
    (HERE / (path.stem + '.before' + path.suffix)).write_bytes(path.read_bytes())
raw = state.read_bytes()
lines = raw.splitlines(keepends=True)
for index, line in enumerate(lines):
    ending = b'\r\n' if line.endswith(b'\r\n') else b'\n'
    if line.startswith(b'    compatibility:'):
        lines[index] = b'    compatibility: "Scoped backend evidence: earlier 43-package/14-case native PASS and 90-input review retained. Preferred 48-package graph has 47-input proposal PASS; newly authorized isolated trial passes all 18 library cases with verified warning-error filters, six protected inputs unchanged. Result/60-notice review pending. OSV exact PyPI lookup has no returned matches, producer-only, not security clearance. Full graph/platform/provenance/licences/locks/adoption remain held."' + ending
    elif line.startswith(b'next_safe_action:'):
        lines[index] = b'next_safe_action: "Inspect authorized 48-package native-result/notice review, resolve findings within scope and reconcile compatibility references. Figma attempt20 needs reconnection and fresh retry approval. Continue Phase1 definitions and consolidation; complete visuals, graph and integrated acceptance remain, commits/pushes deferred."' + ending
state.write_bytes(b''.join(lines))
assert len(state.read_bytes().splitlines()) <= 50
raw = mapping.read_bytes()
old = b'The 45-package identity dry run does not expand it. Original npm CLI SBOM failure remains separate from the bounded supplement.'
new = b'The later [48-package preferred-client trial](../phase-1-compatibility/backend-evidence-2026-10-04.md#preferred-client-native-result-and-wheel-notices--2026-10-09) separately passes all 18 library cases with effective warning-error filters; its authorized results/60-notice review is pending. The [dated exact-version OSV lookup](../../output/research/test-client-advisories-2026-10-09/receipt.json) returned no PyPI matches, producer-only and not security clearance or embedded/native coverage. Original npm CLI SBOM failure remains separate from the bounded supplement.'
assert raw.count(old) == 1
raw = raw.replace(old, new)
old = b'These approvals/results grant no new Figma call, expanded installation, package selection or Phase1 acceptance.'
new = b'The founder subsequently approved the separate 48-package trial and one results/notice review: [all 18 library cases pass](../../output/research/test-client-graph-2026-10-09/native-trial/receipt.json), with no protected input changes. The newly frozen results/notice packet is under its authorized review; no review PASS is inferred. These approvals/results grant no new Figma call, other installation, package selection or Phase1 acceptance.'
assert raw.count(old) == 1
mapping.write_bytes(raw.replace(old, new))
print('Two navigation records aligned; status stays DOING and root state is 50 lines or fewer.')
