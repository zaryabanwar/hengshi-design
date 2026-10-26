"""Repair only our reference updates from exact predecessors; finish the checkpoint."""
from pathlib import Path
import ast
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent / 'reference-integration'
WORLD = ROOT / 'output/research/world-measurement-profile-2026-10-06/reference-integration'
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def text(path, encoding='utf-8'):
    return path.read_bytes().decode(encoding).replace('\r\n', '\n')
def encoded(value):
    return value.replace('\n', '\r\n').encode('utf-8')
def assignments(path):
    tree = ast.parse(path.read_text(encoding='utf-8'))
    pairs = []
    additions = []
    old = None
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
            if name in ('old', 'new') and isinstance(node.value, ast.Constant):
                if name == 'old':
                    old = node.value.value
                else:
                    pairs.append((old, node.value.value))
        if isinstance(node, ast.AugAssign) and isinstance(node.target, ast.Name) and node.target.id == 'text':
            additions.append(ast.literal_eval(node.value))
    return pairs, additions
if (OUT / 'encoding-repair.json').exists():
    raise RuntimeError('Refusing overwrite')
book_pairs, additions = assignments(OUT.parent / 'integrate-references.py')
world_pairs, unused = assignments(WORLD.parent / 'integrate-references.py')
assert len(book_pairs) == 4 and len(additions) == 2 and len(world_pairs) == 2
changes = []
def write_checked(relative, expected, desired, slice_number):
    path = ROOT / relative
    if path.read_bytes() != encoded(expected):
        raise RuntimeError('Current bytes differ from our expected update: ' + relative)
    (OUT / (path.name + '.encoding-error.before')).write_bytes(path.read_bytes())
    path.write_bytes(encoded(desired))
    changes.append({'path': relative, 'slice': slice_number, 'sha256': sha(path)})

# Slice 1: recover exact UTF-8 predecessors for our two ordinary reference documents.
proof = OUT / 'PRIVATE_PROCESS_PROOF.md.before'
old, new = book_pairs[0]
assert text(proof).count(old) == 1
write_checked('docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md',
    text(proof, 'cp1252').replace(old, new) + additions[0],
    text(proof).replace(old, new) + additions[0], 1)
catalogue = OUT / 'INTERFACE_CATALOG.md.before'
write_checked('docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md',
    text(catalogue, 'cp1252') + additions[1], text(catalogue) + additions[1], 1)

# Slice 2: correct the earlier map encoding, add the booking reference, verify state.
mapping_before = WORLD / '04-reconciliation-map.md.before'
old_world, new_world = world_pairs[1]
assert text(mapping_before).count(old_world) == 1
expected_map = text(mapping_before, 'cp1252').replace(old_world, new_world)
desired_map = text(mapping_before).replace(old_world, new_world)
old_book, new_book = book_pairs[3]
assert desired_map.count(old_book) == 1
write_checked('docs/software-definition/04-reconciliation-map.md', expected_map,
              desired_map.replace(old_book, new_book), 2)
state_before = OUT / 'PROJECT_STATE.yaml.before'
desired_state = text(state_before)
for old, new in book_pairs[1:3]:
    assert desired_state.count(old) == 1
    desired_state = desired_state.replace(old, new)
state = ROOT / 'PROJECT_STATE.yaml'
assert state.read_bytes() == encoded(desired_state)
assert len(desired_state.splitlines()) == 50
changes.append({'path': 'PROJECT_STATE.yaml', 'slice': 2, 'sha256': sha(state),
                'scope': 'Prior partial integration already wrote this intended ASCII-only checkpoint; verified unchanged.'})
guards = json.loads((OUT.parent / 'protected-before.json').read_text(encoding='utf-8'))
for row in guards:
    if row['path'] != 'PROJECT_STATE.yaml' and sha(ROOT / row['path']) != row['sha256']:
        raise RuntimeError('Protected input changed: ' + row['path'])
command = ['git', '-c', 'core.autocrlf=false', '-c',
    'core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol',
    'diff', '--check', '--'] + [row['path'] for row in changes]
result = subprocess.run(command, cwd=ROOT, capture_output=True, encoding='utf-8', timeout=20)
record = {'cause': 'Default Windows cp1252 decoding used by reference-update scripts, instead of explicit UTF-8; later map read failed after that update.',
          'changes': changes, 'state_lines': 50, 'other_guards_match': 77,
          'scope': 'Exact restored predecessor text plus intended later references only; frozen reviewed snapshots/receipts unchanged.',
          'whitespace': {'command': command, 'exit_code': result.returncode,
                         'stdout': result.stdout, 'stderr': result.stderr}}
(OUT / 'encoding-repair.json').write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'state_lines': 50, 'other_guards_match': 77,
                 'whitespace_exit_code': result.returncode, 'changed_documents': changes}))
raise SystemExit(result.returncode)
