"""Rebuild local Figma input; validate artifact identity without executing Figma."""
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
FIXTURE = ROOT / 'output/research/b01-recovery-preparation-2026-10-06/fixture-inputs.json'
DIRECTORY = ROOT / 'output/research/b01-directory-preparation-2026-10-06/input.json'
LEDGER = ROOT / 'output/research/b01-navigation-composition-2026-10-06/state-ledger.json'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

fixture = json.loads(FIXTURE.read_text(encoding='utf-8'))
directory = json.loads(DIRECTORY.read_text(encoding='utf-8'))
ledger = json.loads(LEDGER.read_text(encoding='utf-8'))
with (ROOT / 'docs/phase-1-ui-reference-design/responsive-state-mode-matrix.csv').open(encoding='utf-8-sig', newline='') as file:
    profiles = [r for r in csv.DictReader(file) if r['profile_id'] == 'SP-SYSTEM-RECOVERY']
assert len(profiles) == 1 and fixture['profile'] == profiles[0], 'Changed accepted state profile'
assert [s['id'] for s in fixture['states']] == profiles[0]['required_values'].split(';')
assert len({s['id'] for s in fixture['states']}) == 16
assert [s['id'] for s in fixture['surfaces']] == ['light', 'dark', 'forced-colours-specimen']
assert len(fixture['streams']) == 4

current = []
for original in fixture['source_hashes']:
    path = ROOT / original['path']
    actual = digest(path)
    current.append({'path': original['path'], 'sha256': actual,
                    'matches_historical_fixture_input': actual == original['sha256']})
assert current[-1]['matches_historical_fixture_input'], 'Changed navigation checkpoint'
masters = [r for r in directory['streamMasters'] if r['stream_id'] == 'S-SEMANTIC'
           and r['state_id'] in {'STATE-STREAM-CHANGED', 'STATE-PREFERENCE-WRITE-FAILED'}]
assert {r['state_id'] for r in masters} == {'STATE-STREAM-CHANGED', 'STATE-PREFERENCE-WRITE-FAILED'}
assert all(r['id'] in ledger['componentIds'] for r in masters), 'Unknown master identity'

data = dict(fixture)
data['status'] = 'DOING'
data['scope'] = 'Prepared shared recovery composition only; no Figma execution'
data['source_hashes'] = current
data['historical_fixture_source_hashes'] = fixture['source_hashes']
data['fileKey'] = directory['fileKey']
data['streamMasters'] = masters
data['limitations'] = [s for s in fixture['limitations'] if s != 'No Figma construction script or created nodes are claimed by this fixture preparation']
data['limitations'] += [
    'Construction script is prepared locally, unexecuted and independently unreviewed. No created Figma nodes are claimed.',
    'Historical fixture hashes are preserved separately. Current file identities do not establish independent re-review of all current source documents.',
    '48 narrow shared grammar specimens supplement host coverage. Focus rings, forced-colours execution and complete-process behavior remain separate obligations.'
]
write('input.json', data)
template = (OUT / 'figma-template.js').read_text(encoding='utf-8')
assert template.count('/*RECOVERY_INPUT*/ null') == 1
script = template.replace('/*RECOVERY_INPUT*/ null', json.dumps(data, ensure_ascii=False))
(OUT / 'figma-call.js').write_text(script, encoding='utf-8')
write('preparation.json', {
    'product': 'Hengshi Design v1', 'status': 'DOING', 'external_calls': 0,
    'created_figma_nodes': 0, 'independent_review': 'TODO',
    'scope': '48 shared narrow grammar specimens; not complete host-template coverage',
    'fixture_count': 16, 'surface_count': 3, 'annotation_count_planned': 48,
    'new_components_planned': 0, 'new_variables_planned': 0, 'new_styles_planned': 0,
    'input_path': str(FIXTURE.relative_to(ROOT)).replace('\\', '/'),
    'fixture_sha256': digest(FIXTURE), 'directory_input_sha256': digest(DIRECTORY),
    'script_sha256': digest(OUT / 'figma-call.js'), 'current_source_identities': current,
    'historical_source_identity_changes': [r['path'] for r in current if not r['matches_historical_fixture_input']],
    'prerequisites': [
        'Inspect remaining eighteen navigation previews; existing call 14 approval is still pending.',
        'Inspect any relevant changed/partial Figma checkpoint before execution; guards refuse an existing recovery root.',
        'Independent review and immediate CB-06/CB-07 permission remain required; no future call number is assigned here.',
        'The directory composition remains a separate unexecuted batch with its own immediate permission.',
        'Full host/profile coverage, visual inspection, required reviews, exports, restore/_EXIT and founder pilot acceptance remain.'
    ],
    'artifact_validation': 'Source profile, state identities, surfaces and inherited master identities agree. JavaScript parsing is separate; no Figma/API/browser behavior is exercised.'
})
print('Prepared 48 shared specimens; no Figma execution. Historical source identity changes: ' +
      ', '.join(r['path'] for r in current if not r['matches_historical_fixture_input']))
