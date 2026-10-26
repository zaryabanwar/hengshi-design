"""Prepare an isolated design qualification recipe; no Figma/app mutation."""
from pathlib import Path
import hashlib
import json

ROOT = Path.cwd()
OUT = ROOT / 'output/research/b01-expanded-native-qualification-2026-10-14'
STREAMS = ['HIGH', 'MEDIUM', 'LOW', 'SEMANTIC']
LABELS = dict(zip(STREAMS, ['Detailed 3D', 'Balanced 3D', 'Simplified 3D', 'Quick Access']))
families = ['NAVIGATION', 'DIRECTORY', 'RECOVERY']
variants, edges, noops, frames = [], [], [], []

def symbol(family, active, pending, disclosure):
    return f'{family}/{active}/{pending}/{disclosure}'

for family in families:
    disclosures = ['OPEN', 'CLOSED'] if family != 'RECOVERY' else ['NOT_APPLICABLE']
    for active in STREAMS:
        for pending in STREAMS:
            for disclosure in disclosures:
                source = symbol(family, active, pending, disclosure)
                variants.append({
                    'symbol': source, 'active': active, 'pending': pending,
                    'active_caption': LABELS[active], 'checked_choice_caption': LABELS[pending],
                    'family': family, 'disclosure': disclosure,
                    'world_active': False, 'route_fixture': 'Services',
                    'query_fixture': 'design' if family == 'DIRECTORY' else None,
                    'recovery_fixture': 'Synthetic offline context retained' if family == 'RECOVERY' else None,
                    'width': 320, 'minimum_height': 1150,
                    'actual_owned_variant_id': None,
                    'layout': 'Fit all accepted text/four choices without clipping; determine one common content height per family from its tallest variant, minimum1150. Identical named scroll/context anchors. Closed Nav/Directory hide panel choices/Apply; Recovery never invents a disclosure.',
                    'semantics_limit': 'Rendered four-choice design reference, not native HTML radios or a real dialog.'
                })
                for choice in (STREAMS if disclosure != 'CLOSED' else []):
                    record = {'source': source, 'control': f'choose/{choice}', 'trigger': 'ON_CLICK',
                              'destination': symbol(family, active, choice, disclosure)}
                    if choice == pending:
                        noops.append(dict(record, expected='Checked choice unchanged; active and context unchanged; no reaction'))
                    else:
                        edges.append(dict(record, action='CHANGE_TO', expected='Only pending changes; in-force stream/context unchanged'))
                apply = {'source': source, 'control': 'Apply selection', 'trigger': 'ON_CLICK',
                         'destination': symbol(family, pending, pending, disclosure)}
                if disclosure == 'CLOSED':
                    pass  # No interaction attached to an invisible panel control.
                elif active == pending:
                    noops.append(dict(apply, expected='Current choice Apply is a no-op; context and scroll unchanged; no reaction'))
                else:
                    edges.append(dict(apply, action='CHANGE_TO', expected='New in-force caption equals pending; disclosure/Services/query/recovery context unchanged'))
                if family != 'RECOVERY':
                    opposite = 'CLOSED' if disclosure == 'OPEN' else 'OPEN'
                    edges.append({'source': source, 'control': 'Close' if disclosure == 'OPEN' else 'Open',
                        'trigger': 'ON_CLICK', 'action': 'CHANGE_TO',
                        'destination': symbol(family, active, pending, opposite),
                        'expected': 'Preserve active and pending; only disclosure changes'})
                    if disclosure == 'OPEN':
                        edges.append({'source': source, 'control': 'owned host', 'trigger': 'KEY_ESCAPE',
                            'action': 'CHANGE_TO', 'destination': symbol(family, active, pending, 'CLOSED'),
                            'expected': 'Close panel only; preserve active/pending/context. Host fixture trigger, not radio or form submission.'})
        initial = 'CLOSED' if family != 'RECOVERY' else 'NOT_APPLICABLE'
        entry = symbol(family, active, active, initial)
        boundary = f'BOUNDARY/{family}/{active}'
        preview = f'PREVIEW/{family}/{active}'
        frames.append({'symbol': preview, 'family': family, 'active': active, 'entry_variant': entry,
            'kind': 'preview', 'size': [320,560], 'clip_content': True,
            'background': 'D035/palette/paper; never transparent black',
            'overflow': 'VERTICAL', 'flow_entry': True, 'actual_owned_frame_id': None,
            'instance_id': None, 'view_label': 'Isolated mechanism qualification — synthetic data — no live staff or site'})
        frames.append({'symbol': boundary, 'family': family, 'active': active, 'kind': 'reset boundary',
            'size': [320,560], 'actual_owned_frame_id': None,
            'view_label': f'Simulated boundary for {LABELS[active]}; no real route or booking',
            'authored_instance_default': entry})
        edges.append({'source': entry, 'control': 'Private boundary probe', 'trigger': 'ON_CLICK',
            'action': 'NAVIGATE_TO', 'destination': boundary,
            'reset_component_state': True, 'reset_scroll_position': True,
            'expected': 'Enter authored same-active diagonal default. Private reset probe, not product navigation policy.'})
        edges.append({'source': boundary, 'control': 'Private return probe', 'trigger': 'ON_CLICK',
            'action': 'NAVIGATE_TO', 'destination': preview,
            'reset_component_state': True, 'reset_scroll_position': True,
            'expected': f'Fresh {entry} default, top scroll; do not carry another flow\'s cached state'})

inputs = [
    'output/research/b01-prototype-workflow-2026-10-13/native-qualification/qualification-plan-v1.json',
    'output/research/b01-prototype-workflow-2026-10-13/native-qualification/execution/fresh-section-admission-v1.json',
    'output/research/b01-prototype-workflow-2026-10-13/native-qualification/execution/native-qualification-accounting-successor-v1.json',
    'output/research/b01-prototype-workflow-2026-10-13/native-qualification/execution/review-native-successor/independent-review-native-successor-v1.json',
    'docs/phase-1-ui-reference-design/accessibility/UG-3_CONTROL_COPY_PROPOSAL.md',
    'output/research/b01-finite-stream-graph-2026-10-14/review-full-proposal/correction1/independent-review-full-proposal-v1.json',
    'output/research/b01-control-anatomy-2026-10-14/control-anatomy-bindings-v1.json',
    'output/research/b01-control-anatomy-2026-10-14/review-control-anatomy/independent-review-control-anatomy-v1.json',
] + [p.relative_to(ROOT).as_posix() for p in sorted((OUT/'source-observations').glob('*'))]
bindings = []
for name in inputs:
    data = (ROOT/name).read_bytes()
    bindings.append({'path': name, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})

plan = {
    'product': 'Hengshi Design v1', 'status': 'DOING', 'date': '2026-10-14',
    'purpose': 'Qualify four-stream host variants and deterministic reset behavior before full B01 construction. Not a substitute for all22 cases, full profile/anatomy/evidence or integrated Phase1 acceptance.',
    'release_state': 'Proposed external write; not authorized by the existing eight-state trial approval',
    'file_key': 'GOmLP6Cv96l768ueSrZ5Dg', 'expected_page_id': '0:1',
    'new_owned_root_name': 'B01 / Four-stream three-host qualification / v1',
    'write_scope': {'new_sections': 1, 'new_family_component_sets': 3,
        'new_variants': len(variants), 'new_preview_frames': 12, 'new_reset_boundary_frames': 12,
        'existing_node_edits': False, 'existing_node_deletion': False,
        'MCP_calls': 0, 'AI_prompts': 0, 'paid_features': False,
        'sharing_changes': False, 'new_files': False, 'application_changes': False, 'Git_actions': False},
    'source_candidates': {
        'owned_trial_section': '101:3204', 'owned_trial_set': '85:3174',
        'observed_trial_variants': [
            {'id': '85:3301', 'tuple': ['HIGH','HIGH','OPEN']},
            {'id': '85:3280', 'tuple': ['HIGH','HIGH','CLOSED']},
            {'id': '85:3259', 'tuple': ['MEDIUM','HIGH','CLOSED']},
            {'id': '85:3238', 'tuple': ['MEDIUM','HIGH','OPEN']},
            {'id': '85:3217', 'tuple': ['MEDIUM','MEDIUM','OPEN']},
            {'id': '85:3196', 'tuple': ['MEDIUM','MEDIUM','CLOSED']},
            {'id': '85:3175', 'tuple': ['HIGH','MEDIUM','CLOSED']},
            {'id': '85:3173', 'tuple': ['HIGH','MEDIUM','OPEN']}],
        'admission': 'Current set inspector and visible ownership/tuple observations only; no fresh whole-source property/font/reaction or preservation admission'},
    'execution_recipe': [
        'After applicable reviewed-plan release, verify the existing file/Page1/current section/set and current source tuple, descendant/text/font/token/reaction bindings before copying. Stop on drift; no guessed aliases or source substitution.',
        'Save a normal native editable PRE copy. Preserve its actual bytes/hash/ZIP integrity and existing receipts. This is backup evidence, not a proven restore.',
        'Create only the labelled new section. Copy the admitted owned HIGH/HIGH OPEN and CLOSED variant visuals into newly created family-owned components; discover and record their actual IDs. Never edit the source trial or original references.',
        'Build exactly the80 tabled family/active/pending/disclosure variants. Reuse admitted styling and D057 copy; four peer labels and independent Apply. Replace the source fixture\'s two-choice layout with four separate owned choice targets. Adapt visible menu/search/recovery context inside copies only.',
        'Strip inherited reactions only from owned copies before rewiring. Inspect every copied descendant: inherited source-set destination must never survive. No unreviewed detach or original-master edits.',
        'Each family has its own parent component set. All CHANGE_TO targets remain within that set. Every control is a distinct owned layer/target; observed current Label, not inherited layer name, decides identity.',
        'Nav open/closed keep explicit Menu/Close; Directory is the deliberate modal-reference body with visible Close and unwired covered background controls; Recovery keeps its offline context and has no invented close/open control. These are fixture graphics, not native dialog/radio semantics.',
        'Create the24 tabled preview/boundary frames. Previews have an opaque paper background to avoid the previous transparent-black ink limitation. Existing source layout/caption/style values remain untouched.',
        'Wire only the300 listed single-action edges, Instant transitions.60 deliberate visible no-op controls have no reaction. Closed panel choices/Apply have no reactions. All new actual control/parent/target IDs must be recorded after discovery. No variables, conditionals, Back, multiple-action chains, plugins, hidden APIs, Make, MCP or AI.',
        'Apply reset component/scroll options only to the24 private reset-boundary edges. Inspect actual editor option names/settings; if unavailable stop that mechanism without claiming qualification. Same-set choice/Apply/Close paths must be measured rather than assumed to preserve scroll.',
        'Assign12 explicit preview entry flows, each admitting its authored active/pending/default. Restart each before qualification. Repeated presentation state changes are ephemeral observations, not canvas source writes.',
        'Preserve after native editable archive and inspect source/copy ownership and named settings. Execute the tabled cases and save actual observations. Independent result review precedes any larger construction release. No automatic repair beyond this recipe.'
    ],
    'variants': variants, 'frames': frames, 'edges': edges, 'deliberate_noops': noops,
    'qualification_cases': [
        {'id':'ENQ01','scope':'All16 ordered active/pending pairs in each of3 families; open Nav/Directory and non-disclosed Recovery',
         'check':'Choose each peer separately; pending reflects choice, in-force caption/context unchanged until Apply; current selection remains a no-op. Closed states retain pairs through Close/reopen; hidden choices are not directly activated.'},
        {'id':'ENQ02','scope':'All48 variants with visible choices/Apply, with32 closed retention variants checked through Close/reopen',
         'check':'Apply12 non-diagonal pairs per family moves to matching diagonal target. Diagonal Apply does not change context. Repeat at least one full four-peer cycle per family.'},
        {'id':'ENQ03','scope':'Navigation and Directory all16 pairs',
         'check':'Close and reopen preserve active, checked pending and context; Escape closes once. Directory covered background activation does nothing. Nav closed destinations remain fixture-only.'},
        {'id':'ENQ04','scope':'Recovery all16 pairs',
         'check':'Choice/Apply retain synthetic offline route/status and visible help; never create an invented Recovery disclosure or live staff/World claim.'},
        {'id':'ENQ05','scope':'All12 family/active preview entries',
         'check':'Scroll to a visible nonzero position marker; current-choice no-op and a pending choice preserve the same visible anchor, then Apply preserves context/scroll. Record actual anchor position and screenshot; do not infer from duplicated geometry.'},
        {'id':'ENQ06','scope':'All12 entry/reset boundary pairs',
         'check':'Dirty the fixture via choice/Apply/disclosure/scroll, restore its authored active before boundary activation, Navigate to boundary and return. Actual reset settings yield authored active= pending and default disclosure/top scroll. Repeat after a different flow; cached state must not masquerade as defaults.'},
        {'id':'ENQ07','scope':'All3 families with LOW and SEMANTIC in-force',
         'check':'Record visible focus/Tab/Enter/Space behavior without assigning global Enter/Space Apply. If Presentation exposes no actual control focus/semantics, record that limitation; annotations never become native HTML/AT PASS.'},
        {'id':'ENQ08','scope':'Exact new section and original trial/reference safeguards',
         'check':'New layer manifest, all edge targets, no source-linked destinations or destructive actions, source selected properties/tuples unchanged, normal editable exports and observed default entry. ZIP CRC is not whole-file equality, tested restore or _EXIT.'}
    ],
    'not_qualified_here': ['P11 refusal chronology, failed Apply, unsaved preference, newer/unknown/terminal/timing lifetimes',
        'Full22 B01 scenarios, all public frame/profile/viewport/mode/context coverage and production visual acceptance',
        'Real DOM/AT/radio/form/dialog semantics, WCAG, browser/device runtime, application authorization/timing or publication',
        'Source whole-file preservation, tested native restore and B01_EXIT or founder integrated acceptance'],
    'official_guidance': [
        {'url':'https://help.figma.com/hc/en-us/articles/360040035874-Prototype-actions','checked':'2026-10-14','use':'Change to is for variants in a component set; Navigate to reaches another frame.'},
        {'url':'https://help.figma.com/hc/en-us/articles/14397859494295-State-management-for-prototypes','checked':'2026-10-14','use':'State persistence/reset is configurable; qualify observed instance defaults separately.'},
        {'url':'https://help.figma.com/hc/en-us/articles/360051747774-Preserve-scroll-position-in-prototypes','checked':'2026-10-14','use':'Current reset scroll terminology and state sharing/memorization; never assume equal geometry proves scroll continuity.'}],
    'input_bindings': bindings, 'independent_review': {'receipt': None, 'complete': False},
    'actual_external_execution': False
}
OUT.mkdir(parents=True, exist_ok=True)
(OUT/'qualification-plan-v1.json').write_text(json.dumps(plan,indent=2)+'\n', encoding='utf-8')
assert len(variants)==80 and len(frames)==24 and len(edges)==300 and len(noops)==60
assert len({v['symbol'] for v in variants})==80
nodes={v['symbol'] for v in variants}|{f['symbol'] for f in frames}
assert all(e['source'] in nodes and e['destination'] in nodes for e in edges)
assert len({(e['source'],e['control'],e['trigger']) for e in edges})==len(edges)
print('Prepared isolated qualification:80 variants,24 frames,300 single-action edges,60 visible no-op controls. Artifact shape only; no execution or qualification PASS.')
