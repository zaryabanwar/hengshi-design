from pathlib import Path
import hashlib
import json
import urllib.request

root = Path.cwd()
out = root / 'output/research/b01-preflight-2026-10-06'
assert not (out / 'review-inputs.json').exists(), 'Already frozen; do not overwrite'
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
sources = [
    ('rates', 'https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/'),
    ('plugin-api', 'https://developers.figma.com/docs/plugins/api/figma/'),
    ('node-exports', 'https://developers.figma.com/docs/plugins/api/properties/nodes-exportasync/'),
]
records = []
for name, url in sources:
    request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; HengshiDefinitionResearch/1.0)'})
    with urllib.request.urlopen(request, timeout=25) as response:
        path = out / (name + '.html')
        path.write_bytes(response.read())
        records.append({'url': url, 'status': response.status, 'file': path.relative_to(root).as_posix(), 'sha256': digest(path)})
(out / 'official-sources.json').write_text(json.dumps(records, indent=2) + '\n', encoding='utf-8')
prior = json.loads((root / 'output/research/private-json-profile-2026-10-06/protected-before.json').read_text(encoding='utf-8'))
guards = [{'path': x['path'], 'sha256': digest(root / x['path'])} for x in prior]
unexpected = [x['path'] for x, before in zip(guards, prior) if x['sha256'] != before['sha256'] and x['path'] != 'PROJECT_STATE.yaml']
assert not unexpected, unexpected
assert digest(root / 'PROJECT_STATE.yaml') == 'bda358a26c7c3ba78265e6542f52132b1a5c88f886918f4aa0def1d3d6cb6431'
(out / 'protected-current.json').write_text(json.dumps(guards, indent=2) + '\n', encoding='utf-8')
paths = [
    'docs/phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md',
    'docs/phase-1-ui-reference-production/validation/capability-evidence.md',
    'docs/phase-1-ui-reference-production/UI_REFERENCE_PRODUCTION_CONTRACT.md',
    'docs/phase-1-ui-reference-production/README.md',
    'docs/phase-1-ui-reference-production/batch-production-plan.csv',
    'docs/phase-1-ui-reference-production/external-write-scope.csv',
    'docs/phase-1-ui-reference-production/stop-conditions.csv',
    'docs/phase-1-ui-reference-production/validation/mcp-call-budget.csv',
    'docs/phase-1-ui-reference-production/validation/mcp-call-ledger.csv',
    'docs/phase-1-ui-reference-design/design-batch-plan.csv',
    'docs/phase-1-ui-reference-design/reference-template-inventory.csv',
    'docs/phase-1-ui-reference-design/component-primitives.csv',
    'docs/phase-1-ui-reference-design/responsive-state-mode-matrix.csv',
    'docs/phase-1-ui-reference-design/accessibility/UG-3_CONTROL_COPY_PROPOSAL.md',
    'MANUAL_ACTIONS.md', 'DECISIONS.md', 'PROJECT_STATE.yaml', 'TASKS.md',
]
inputs = [{'path': x, 'sha256': digest(root / x)} for x in paths]
inputs.extend({'path': p.relative_to(root).as_posix(), 'sha256': digest(p)} for p in sorted(out.iterdir()) if p.is_file())
packet = {'scope': 'B01 execution read-back and current-host prerequisite clarification only; no pilot release, new design, call, runtime test or waiver.', 'inputs': inputs}
(out / 'review-inputs.json').write_text(json.dumps(packet, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'inputs': len(inputs), 'guards': len(guards), 'unchanged_other_guards': len(prior)-1, 'brief_lines': len((root / paths[0]).read_text(encoding='utf-8').splitlines()), 'packet_sha256': digest(out / 'review-inputs.json')}, indent=2))
