from pathlib import Path
import difflib
import hashlib
import json

root = Path.cwd()
base = root / 'output/research/b01-preflight-2026-10-06/bootstrap-proposal'
out = base / 'correction-1'
out.mkdir(exist_ok=False)
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
packet = json.loads((base / 'review-inputs.json').read_text(encoding='utf-8'))
assert all(digest(root / x['path']) == x['sha256'] for x in packet['inputs'])
guards = json.loads((base.parent / 'protected-current.json').read_text(encoding='utf-8'))
assert all(digest(root / x['path']) == x['sha256'] for x in guards)
snapshots = out / 'snapshots'
snapshots.mkdir()
inputs = []
for i, source in enumerate(packet['inputs']):
    p = snapshots / (str(i) + '-' + Path(source['path']).name)
    p.write_bytes((root / source['path']).read_bytes())
    inputs.append({'path': p.relative_to(root).as_posix(), 'sha256': digest(p), 'original_path': source['path']})
old = (base / 'contract.proposed.md').read_text(encoding='utf-8')
clause = '6. No write occurs until §3.5 capability enablement is completed and recorded.'
repair = '''6. No design/content write occurs until §3.5 capability enablement is completed
   and recorded. Only the separately founder-approved empty first-file bootstrap
   specified in §3.5 may precede file/archiving verification; it grants no pilot
   execution, design/content write or waiver of private inventory and _PRE gates.'''
assert old.count(clause) == 1
new = old.replace(clause, repair)
(out / 'contract.proposed.md').write_text(new, encoding='utf-8')
(out / 'scope.proposed.csv').write_bytes((base / 'scope.proposed.csv').read_bytes())
original = (base / 'contract.before.md').read_text(encoding='utf-8')
original_scope = (base / 'scope.before.csv').read_text(encoding='utf-8')
new_scope = (out / 'scope.proposed.csv').read_text(encoding='utf-8')
contract_path = 'docs/phase-1-ui-reference-production/UI_REFERENCE_PRODUCTION_CONTRACT.md'
scope_path = 'docs/phase-1-ui-reference-production/external-write-scope.csv'
patch = ''.join(difflib.unified_diff(original.splitlines(keepends=True), new.splitlines(keepends=True), fromfile='a/' + contract_path, tofile='b/' + contract_path))
patch += ''.join(difflib.unified_diff(original_scope.splitlines(keepends=True), new_scope.splitlines(keepends=True), fromfile='a/' + scope_path, tofile='b/' + scope_path))
(out / 'first-file-ordering.patch').write_text(patch, encoding='utf-8')
receipt = root / 'docs/phase-1-ui-reference-production/reviews/first-file-ordering-proposal-v1-2026-10-06.md'
assert digest(receipt) == 'c1d51eaedff5d54e8f11f8b68a4745c801cbbf7d90ba813544d91c9460a58c3d'
for p in [out / 'contract.proposed.md', out / 'scope.proposed.csv', out / 'first-file-ordering.patch', Path(__file__), receipt, base / 'review-inputs.json', base.parent / 'protected-current.json']:
    inputs.append({'path': p.relative_to(root).as_posix(), 'sha256': digest(p)})
review = {'scope': 'Correction 1 closes only §11.1 no-write conflict in a proposed, unapplied amendment. Prior canonical inputs are frozen snapshots; later approved whoami ledger/capability updates are outside these bytes. No design or external creation release.', 'inputs': inputs}
(out / 'review-inputs.json').write_text(json.dumps(review, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'inputs': len(inputs), 'guards': len(guards), 'packet_sha256': digest(out / 'review-inputs.json')}, indent=2))
