"""Prepare design evidence allocation from saved receipts; no Figma execution."""
from pathlib import Path
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
sources = {}

def read(path, kind='json'):
    raw = (ROOT / path).read_bytes()
    sources[path] = {'path': path, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}
    if kind == 'csv':
        return list(csv.DictReader(raw.decode('utf-8-sig').splitlines()))
    if kind == 'text':
        return raw.decode('utf-8-sig')
    return json.loads(raw)

matrix = read('docs/phase-1-ui-reference-design/responsive-state-mode-matrix.csv', 'csv')
templates = read('docs/phase-1-ui-reference-design/reference-template-inventory.csv', 'csv')
batch = next(r for r in read('docs/phase-1-ui-reference-design/design-batch-plan.csv', 'csv') if r['batch_id'] == 'B01')
current = read('output/research/b01-profile-allocation-2026-10-12/current-stream-obligations.json')
for path in ['docs/phase-1-ui-reference-design/component-primitives.csv',
             'scripts/validation/ui-stream-mapping.ps1']:
    read(path, 'text')
for path in ['docs/phase-1-ui-reference-design/responsive-state-mode-matrix.csv',
             'docs/phase-1-ui-reference-design/reference-template-inventory.csv',
             'docs/phase-1-ui-reference-design/component-primitives.csv',
             'scripts/validation/ui-stream-mapping.ps1']:
    bound = next(r for r in current['sources'] if r['path'] == path)
    assert bound['sha256'] == sources[path]['sha256'], 'Current obligation derivation changed: ' + path
for path in ['AGENTS.md', '.specify/memory/constitution.md', 'DECISIONS.md',
             'docs/phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md',
             'docs/phase-1-ui-reference-production/UI_REFERENCE_PRODUCTION_CONTRACT.md',
             'docs/phase-1-ui-reference-production/evidence-capture-plan.csv',
             'scripts/validation/ui-exit-coverage.ps1']:
    read(path, 'text')

rows = []
def append(family, node, name, width, height, declared=None, kind='FRAME'):
    rows.append({'source_family': family, 'node_id': node, 'recorded_name': name,
                 'width': width, 'height': height, 'proposed_type': kind,
                 'declared_axes': declared})

nav = read('output/research/b01-navigation-composition-2026-10-06/state-ledger.json')
for r in nav['frames']:
    append('navigation', r['id'], r['name'], r['width'], r['height'])
directory = read('output/research/b01-directory-call19-2026-10-08/decoded-design-result.json')
for r in directory['frames']:
    append('directory', r['id'], r['reference']['name'], r['width'], r['height'])
rec = read('output/research/b01-recovery-stream-bindings-2026-10-08/attempt24-2026-10-11/receipt.json')
rec_input = read('output/research/b01-recovery-stream-bindings-2026-10-08/input.json')
for node, ordinal, width, height in rec['frames']:
    append('recovery_hosts', node, rec_input['planned_references'][ordinal]['planned_frame_name'], width, height)
ref = read('output/research/b01-ceiling-refusal-bindings-2026-10-09/attempt25-2026-10-11/receipt.json')
ref_input = read('output/research/b01-ceiling-refusal-bindings-2026-10-09/execution-preparation/input.json')
for node, ordinal, width, height, *_ in ref['frames']:
    case = ref_input['frames'][ordinal]['case']
    append('capability_refusal', node, case['planned_frame_name'], width, height, case)
grammar = read('output/research/b01-recovery-grammar-batched-capture-2026-10-11/attempt27-2026-10-11/receipt.json')['report']
grammar_input = read('output/research/b01-recovery-grammar-batched-capture-2026-10-11/input.json')
for node, state, surface, width, height in grammar['frames']:
    name = 'B01 shared recovery / ' + grammar_input['states'][state]['id'] + ' / ' + grammar_input['surfaces'][surface]['id'] + ' / v1'
    append('shared_grammar', node, name, width, height,
           {'state_id': grammar_input['states'][state]['id'], 'mode_id': grammar_input['surfaces'][surface]['mode'],
            'surface': grammar_input['surfaces'][surface]['id']}, 'FOCUSED_FRAME')
responsive = read('output/research/b01-responsive-coverage-2026-10-11/attempt28-2026-10-12/receipt.json')
responsive_input = read('output/research/b01-responsive-coverage-2026-10-11/attempt28-2026-10-12/input.json')
for node, ordinal, width, height in responsive['frames']:
    append('responsive', node, responsive_input['references'][ordinal]['name'], width, height)

pattern = re.compile(r'^HSD_UIR_B01_(TPL_[A-Z_]+)_REF_(STATE_[A-Z_]+)_(VP_[A-Z0-9_]+)_(MODE_[A-Z_]+)_STREAM_(HIGH|LOW|MEDIUM|SEMANTIC)_V01$')
for r in rows:
    match = pattern.fullmatch(r['recorded_name'])
    r['encoded_axes'] = dict(zip(['template_id', 'state_id', 'viewport_id', 'mode_id', 'stream_id'],
        [v.replace('_', '-') for v in match.groups()[:4]] + ['S-' + match.group(5)])) if match else None
assert len({r['node_id'] for r in rows}) == len(rows)
scoped = [r for r in rows if r['encoded_axes']]
profiles = {p['profile_id']: p for p in matrix}
own_templates = [t for t in templates if t['template_id'] in batch['primary_template_ids'].split(';')]
profile_gaps = []
for t in own_templates:
    own = [r for r in scoped if r['encoded_axes']['template_id'] == t['template_id']]
    for field, axis in [('state_profile','state_id'), ('viewport_profile','viewport_id'), ('mode_profile','mode_id')]:
        p = profiles[t[field]]
        observed = sorted({r['encoded_axes'][axis] for r in own})
        profile_gaps.append({'template_id': t['template_id'], 'profile_id': p['profile_id'],
            'encoded_values': observed, 'not_encoded': [v for v in p['required_values'].split(';') if v not in observed],
            'critical_distinct_frame_values': p['critical_distinct_frame_values'].split(';'),
            'minimum_evidence': p['minimum_evidence'], 'annotation_requirements': p['annotation_requirements'],
            'exception_rule': p['exception_rule']})

def focus_key(r):
    return tuple(r[k] for k in ['template_id', 'state_id', 'stream_id'])
focus = []
for need in current['obligations']:
    matches = [r['node_id'] for r in scoped if focus_key(r['encoded_axes']) == focus_key(need)]
    focus.append({**need, 'matching_recorded_ids': matches})
renames = []
for r in rows:
    if r['source_family'] == 'capability_refusal':
        case = r['declared_axes']
        correct = 'HSD_UIR_B01_' + case['template_id'].replace('-', '_') + '_REF_' + case['state_id'].replace('-', '_') + '_VP_320_MODE_KEYBOARD_STREAM_' + case['stream_id'][2:] + '_V01'
        assert pattern.fullmatch(correct)
        renames.append({'node_id': r['node_id'], 'expected_current_name': r['recorded_name'],
                        'proposed_name': correct, 'only_change': 'Existing frame name; no appearance, instance, layout or interaction edits'})

result = {'product': 'Hengshi Design v1', 'status': 'DOING', 'date': '2026-10-12',
    'purpose': 'Preparation input for the remaining B01 references; no external execution or acceptance',
    'summary': {'recorded_views_in_this_inventory': len(rows), 'strictly_named_stream_host_references': len(scoped),
                'shared_unscoped_grammar_specimens': len(grammar['frames']), 'refusal_names_missing_REF': len(renames),
                'generic_initial_drafts_not_credited': 6},
    'sources': list(sources.values()), 'recorded_views': rows, 'profile_name_gaps': profile_gaps,
    'required_stream_state_subset': focus, 'proposed_existing_frame_name_repairs': renames,
    'allocation': [
        {'id': 'B01-REMAINING-IDENTITY', 'status': 'TODO', 'output': 'Repair the eight existing refusal frame names with REF; retain IDs/pixels and rename no source master. Fresh approved call must guard exact current names first.'},
        {'id': 'B01-REMAINING-MODES', 'status': 'TODO', 'output': 'Use each assigned profile and stream minima, not a Cartesian product: standard and screen-reader for all four streams; reduced-motion S-HIGH; low-power S-LOW; forced-colours and print S-SEMANTIC; additional missing template modes once at their appropriate peer stream. Recovery baseline ERROR/320/FORCED-COLORS must be a full host in each of four streams. Build visual mode changes where needed, not renamed identical captures.'},
        {'id': 'B01-REMAINING-STATES', 'status': 'TODO', 'output': 'Use the complete profile gap list below. Critical states need distinct visual evidence; noncritical values may have truthful state/interaction annotations. Reuse existing recovery grammar only when visibly assembled with a named host, current stream and safe primary action; its 48 unscoped specimens alone earn no host/stream credit. Assess CLOSED navigation, directory STALE and 404/410 behavior explicitly.'},
        {'id': 'B01-REMAINING-VIEWPORTS', 'status': 'TODO', 'output': 'VP-NARROW and VP-TABLET may link actual 320/landscape/desktop bounds only after checking identical structure and reading/action order. VP-WIDE needs measured line length/control placement. Existing 320, landscape, desktop and reflow frames stay the bounding sources; no new frame merely to raise a count.'},
        {'id': 'B01-REMAINING-INTERACTIONS', 'status': 'TODO', 'output': 'Produce design PROTOTYPE and semantic specifications for disclosure open/close/invoker return, modal versus nonmodal search, clear/close/result actions, radio selection versus explicit Apply, preserved-context errors and expiry warning/extension. D078 controls: at least20 seconds warning, simple action, at least10 extension opportunities. Show each stream independently; no Figma animation is a native keyboard/screen-reader test.'},
        {'id': 'B01-REMAINING-EXIT', 'status': 'TODO', 'output': 'After coverage and interaction review: deterministic PNG@2x/SVG exports and prototype flow sheets, reconciled evidence manifest, native archive/restore and EXIT, separate independent design/accessibility reviews, then founder pilot acceptance. Later TEST_CAPTURE remains after implementation, outside MA025.'}
    ],
    'limits': ['Names/receipt correlations are preparation evidence, not a complete exit manifest or qualitative coverage adjudication.',
               'Missing encoded names do not establish that no inherited or separately recorded annotation exists; inspect those before authoring duplicate evidence.',
               'Shared grammar labels carry no explicit stream or host; no implicit S-SEMANTIC assignment.',
               'Eight refusal names omit REF in the executed input; confirmed live names require preflight. Existing scoped pixel reviews remain valid at their original inputs.',
               'No full canvas read, physical editability census, font-rights approval, runtime behavior, accessibility conformance or complete-process proof.',
               'No Figma call, source/master rename, paid action, application feature, later batch release, Git action or founder acceptance authorized by this preparation.']}
target = OUT / 'allocation.json'
assert not target.exists(), 'Preserve previous allocation evidence'
target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'summary': result['summary'], 'profile_name_gaps': [{k:r[k] for k in ['template_id','profile_id','not_encoded']} for r in profile_gaps],
                  'stream_subset_without_strict_names': [r for r in focus if not r['matching_recorded_ids']]}))
