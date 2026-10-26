"""Resolve one B01 mode composition from approved tables and recorded sources."""
from pathlib import Path
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
bound = {}

def read(rel, csv_file=False):
    raw = (ROOT / rel).read_bytes()
    bound[rel] = {'path': rel, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}
    return list(csv.DictReader(raw.decode('utf-8-sig').splitlines())) if csv_file else json.loads(raw)

draft = read('output/research/b01-profile-allocation-2026-10-12/next-mode-candidates.json')
allocation = read('output/research/b01-profile-allocation-2026-10-12/allocation.json')
allocation_review = read('output/research/b01-profile-allocation-2026-10-12/independent-review-allocation-v1.json')
assert allocation_review['verdict'] == 'PASS'
responsive = read('output/research/b01-responsive-coverage-2026-10-11/attempt28-2026-10-12/input.json')
refusal = read('output/research/b01-ceiling-refusal-bindings-2026-10-09/execution-preparation/input.json')
refusal_receipt = read('output/research/b01-ceiling-refusal-bindings-2026-10-09/attempt25-2026-10-11/receipt.json')
templates = read('docs/phase-1-ui-reference-design/reference-template-inventory.csv', True)
matrix = read('docs/phase-1-ui-reference-design/responsive-state-mode-matrix.csv', True)
routes = read('docs/phase-1-foundation/06-canonical-route-inventory.json')
assert next(r for r in routes['routes'] if r['id'] == 'ROUTE-BOOK')['path'] == '/book'
sources = [s for s in responsive['sources'] if s['kind'] == 'narrow']
assert len(sources) == 12
masters = refusal['masters']
host_notes = {
 'TPL-GLOBAL-NAVIGATION': 'Services host; navigation open. Reading order: skip link, navigation, Book, breadcrumb, stream legend/options/Apply, privacy. Close returns to the navigation invoker; no focus trap.',
 'TPL-DIRECTORY-SEARCH': 'Services host; nonmodal Directory open. Reading order: heading, Close, labelled search, Search, status/browse links, stream group/Apply, privacy. Escape or Close returns to the directory invoker; no focus trap or live search ranking claim.',
 'TPL-SYSTEM-RECOVERY': 'Services host; confirmed pre-admission error. Prior eligible content and in-force stream remain. Status announcement does not take focus; safe directory recovery remains. No successful mutation, entitlement or staff presence is inferred.'
}
mode_notes = {
 'MODE-STANDARD': 'Inherited standard appearance. Each stream keeps its own readable current/pending labels and actions; this static frame does not measure contrast or target sizes.',
 'MODE-SCREEN-READER': 'Semantic specification only: use native links/buttons, a fieldset/legend and labelled radios. The legend announces the in-force choice; the checked radio is pending. Status uses a separate live region. Tab leaves the group for Apply; selecting a radio does not navigate or apply. This picture is not screen-reader execution.',
 'MODE-REDUCED-MOTION': 'Stable B01 DOM controls; no essential animated disclosure, travel or motion. Apply semantics and content remain. This is a reduced-motion design specification, not a browser preference probe.',
 'MODE-LOW-POWER': 'B01 controls and reading order remain complete without a canvas, decorative animation or optional media. In-force Simplified 3D is a peer stream; low power removes no destination. No measured battery/performance claim.',
 'MODE-SEMANTIC-SHELL': 'Quick Access is the in-force peer presentation. Content, Book, directory and stream controls remain semantic and independently operable; no failure title or error styling is added merely for this stream.',
 'MODE-FORCED-COLORS': 'Palette specimen only. Canvas/CanvasText and ButtonFace/ButtonText are mapped to inherited white/ink tokens; borders and current/pending text survive. LinkText, Highlight/HighlightText and focus outline remain implementation roles, not claimed OS colours. Preserve native control roles and do not opt the whole shell out of forced colours.',
 'MODE-GRAYSCALE': 'Grayscale paints are derived from inherited token RGB values. Current/pending choices, control purpose and recovery truth remain textual; meaning does not depend on colour. This is a static appearance specimen.',
 'MODE-UNAVAILABLE-FONT': 'Optional Inter unavailable fixture. This focused specimen substitutes verified Cascadia Mono Regular, preserves text and reflows the control. It is an approved Figma-only fallback illustration, not a website font installation, system-font guarantee or licence grant.',
 'MODE-UNAVAILABLE-IMAGE-ASSET': 'Optional approved brand mark unavailable fixture, authored as a focused region because the source hosts currently use text branding. The mark is omitted, the full Hengshi Design name and controls remain; no fabricated photograph or actual network/asset failure is claimed.',
 'MODE-PRINT': 'Printable fixture summary of this host and in-force Quick Access. Interactive controls are omitted; the pending choice remains explicitly unapplied. The online Services and Book paths are text references. No promise that search results, a transaction or a private conversation has been saved.'
}
references = []
for r in draft['candidates']:
    full = r['mode_id'] in ['MODE-STANDARD', 'MODE-FORCED-COLORS']
    t = next(t for t in templates if t['template_id'] == r['template_id'])
    assert r['mode_id'] in next(p for p in matrix if p['profile_id'] == t['mode_profile'])['required_values'].split(';')
    references.append({'sourceId': r['source_id'], 'templateId': r['template_id'], 'streamId': r['stream_id'],
        'stateId': r['state_id'], 'modeId': r['mode_id'], 'name': r['planned_name'],
        'kind': 'FRAME' if full else 'FOCUSED_FRAME', 'width': 320,
        'profileIds': [t['state_profile'], t['viewport_profile'], t['mode_profile'], 'DS-' + r['stream_id']]})
assert len(references) == 48 and len({r['name'] for r in references}) == 48
full_indices = [i for i, r in enumerate(references) if r['kind'] == 'FRAME']
focus_indices = [i for i, r in enumerate(references) if r['kind'] == 'FOCUSED_FRAME']
assert len(full_indices) == 15 and len(focus_indices) == 33
repairs = []
for r in draft['existing_name_repairs']:
    width, height = next((row[2], row[3]) for row in refusal_receipt['frames'] if row[0] == r['node_id'])
    repairs.append({**r, 'width': width, 'height': height, 'ancestorId': refusal_receipt['rootId']})
assert len(repairs) == 8
groups = [full_indices[:8], full_indices[8:], focus_indices[:11], focus_indices[11:22], focus_indices[22:]]
data = {'product': 'Hengshi Design v1', 'status': 'TODO', 'fileKey': responsive['fileKey'],
    'scope': '48 mode references:15 full hosts and33 focused regions,48 visible annotations,8 existing-name repairs and five native comparisons; no full B01 claim',
    'rootName': 'B01 / Mode references / v1', 'sources': sources, 'masters': masters,
    'labels': refusal['labels'], 'copy': refusal['copy'], 'references': references, 'nameRepairs': repairs,
    'hostNotes': host_notes, 'modeNotes': mode_notes,
    'fallbackFont': {'family': 'Cascadia Mono', 'style': 'Regular'},
    'optionalAssetReference': 'docs/phase-1-brand-identity/assets/mark-framework-relay.svg',
    'capture': {'groups': groups, 'maxWidth': 4800, 'maxHeight': 4800, 'maxTrackedCreatedIds': 10000,
                'maxReceiptBytes': 19000, 'scale': 1, 'expectedImages': 5},
    'discovery': {'codeConnect': 'No matching Code Connect files found in apps; no app implementation is produced.',
                  'components': 'Four exact existing file-local stream masters and12 inherited host frames; preflight resolves each source instance before mutation.',
                  'styles': 'Existing B01 reference heading/body/meta text styles and approved Figma-only fonts; preflight loads all inherited font runs.',
                  'tokens': 'Existing D035 colour/spacing variables; no new variables, libraries, publication or assets are created.',
                  'images': 'Source hosts are editable text/components, no external image capture. Asset-failure region omits only the approved optional mark as an authored fixture.'},
    'primarySources': [
      {'url': 'https://www.w3.org/TR/css-color-adjust-1/#forced-colors-mode', 'checked': '2026-10-12',
       'status': 'Candidate Recommendation Snapshot16 December2025; descriptive CSS guidance, not a selected preview dependency',
       'application': 'User-agent palette adaptation uses semantic roles. The Figma white/ink example is not a real user palette or browser test.'},
      {'url': 'https://www.w3.org/WAI/tutorials/images/decorative/', 'checked': '2026-10-12',
       'application': 'A decorative mark beside the full company name adds no essential content. Omitting it must not remove the textual identity.'},
      {'url': 'https://www.w3.org/WAI/ARIA/apg/patterns/radio/', 'checked': '2026-10-12',
       'application': 'Radio keyboard interaction informs the semantic specification; actual project controls remain native fieldset/legend/radios with separate Apply.'}
    ],
    'sourceHashes': list(bound.values()),
    'limitations': ['Prepared design source only; no external execution or accessibility/complete B01 acceptance.',
      'Focused references never replace the four full forced-colours recovery baselines or other complete viewport/state minima.',
      'Original frame names change only for the eight exact guarded REF repairs; other source appearance/order/positions remain preserved.',
      'Font groups report new-frame TEXT-node membership only, not exact spans, missing-font status, rights or editability census.',
      'No actual screen reader, forced-colours OS, reduced-motion preference, asset/font load failure, print browser, focus or action execution.',
      'Remaining states/intermediate widths/prototypes, contracted2x/SVG exports, native restore/EXIT and independent full design/accessibility reviews remain.',
      'One new Figma call needs founder immediate permission and one allowance exception; current28 attempts/25 conservatively metered; actual quota unknown. No retry or paid activation.']}
asset = ROOT / data['optionalAssetReference']
data['sourceHashes'].append({'path': data['optionalAssetReference'], 'bytes': asset.stat().st_size,
                            'sha256': hashlib.sha256(asset.read_bytes()).hexdigest()})
target = OUT / 'input.json'
assert not target.exists()
target.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'references': len(references), 'full_hosts': len(full_indices), 'focused': len(focus_indices),
                  'name_repairs': len(repairs), 'capture_groups': [len(g) for g in groups], 'external_calls': 0}))
