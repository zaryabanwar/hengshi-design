from pathlib import Path
import difflib
import hashlib
import json

root = Path.cwd()
out = root / 'output/research/b01-preflight-2026-10-06/bootstrap-proposal'
out.mkdir(exist_ok=False)
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
contract = 'docs/phase-1-ui-reference-production/UI_REFERENCE_PRODUCTION_CONTRACT.md'
scope = 'docs/phase-1-ui-reference-production/external-write-scope.csv'
original = (root / contract).read_text(encoding='utf-8')
old = '''- **Path B — agent-performed.** A Figma MCP server or equivalent authorized API
  path is configured in the canonical inventory, authenticated by a person through
  an official flow, and **capability-tested read-only first** (list file, read node
  inventory) before any write. The test result and its date are recorded in
  `validation/capability-evidence.md`.

Under either path, the following must be recorded before `WS-P-01`: provider,
account type, plan tier, date, the read-only capability result, and the
`[MUST VERIFY AT GATE]` items in §7.2. **Capability must never be assumed.**'''
new = '''- **Path B — agent-performed.** A Figma MCP server or equivalent authorized API
  path is configured in the canonical inventory and authenticated by a person
  through an official flow. For an existing file, perform an individually approved
  read-only file/node capability check before any write and record its date/result.

  **First-file bootstrap exception — requires explicit founder acceptance.** If
  this new project has no file, record the authenticated identity, selected plan
  and account type/tier first. The founder may then separately authorize one
  create_new_file call for one empty Design file named `Hengshi Design v1 — UI
  References`, in an approved existing project or, only if explicitly selected,
  the authenticated account's Drafts. Creating the empty file does not establish
  file/canvas capability or release design work. Obtain the next immediate call
  approval for a read-only file/node check of that returned target. Verify its
  private access/sharing state and a supported named-version/full-editable-archive
  path before writing any design or project content. Retain a dated empty-file
  creation receipt and its single target; do not retry an uncertain creation by
  creating another file. Inspect/reconcile the first outcome under fresh approval.
  If privacy, inventory or archive support cannot be verified, stop design work.
  Neither bootstrap acceptance nor file creation accepts/releases the B01 pilot.

Under either path record provider, account type, plan tier, date, read-only
capability results and the `[MUST VERIFY AT GATE]` items in §7.2. Under the
first-file exception, identify file/archiving items as unverified until tested;
do not label capability complete from whoami. Every external call, including
bootstrap and failed calls, retains CB-06/CB-07 approval and ledger requirements.
No project creation, sharing change, seat/billing change or later-batch release
follows from this exception. **Capability must never be assumed.**'''
assert original.count(old) == 1
changed = original.replace(old, new)
old_operation = '| `WS-P-01` | Create one Figma project and one design file dedicated to Hengshi Design UI reference production |'
new_operation = '| `WS-P-01` | Create one dedicated Design file in an approved existing project or explicitly approved Drafts under §3.5; creating a project requires its own explicit operation approval |'
assert changed.count(old_operation) == 1
changed = changed.replace(old_operation, new_operation)
old_checkpoint = '''1. **Pre-write checkpoint.** Before the first write of a batch: create a named
   Figma version `HSD_UIR_<BATCH>_PRE`, export the file archive, and record its
   SHA-256 in the batch manifest.'''
new_checkpoint = '''1. **Pre-write checkpoint.** Before the first design/content write of a batch:
   create a named Figma version `HSD_UIR_<BATCH>_PRE`, export the full editable
   file archive, and record its SHA-256 in the batch manifest. The individually
   authorized empty first-file bootstrap in §3.5 precedes this checkpoint; it
   permits no design/content write and cannot substitute for the _PRE archive.'''
assert changed.count(old_checkpoint) == 1
changed = changed.replace(old_checkpoint, new_checkpoint)
original_scope = (root / scope).read_text(encoding='utf-8')
old_scope = 'WS-P-01,permitted,Create one project and one design file dedicated to Hengshi Design UI reference production,figma_single_approved_file,Only once and only after section 3.5 capability evidence is recorded,The contracted work needs one durable system of record'
new_scope = 'WS-P-01,permitted,Create one dedicated Design file in an approved existing project or explicitly approved Drafts,figma_single_approved_file,Only once with explicit operation approval and section 3.5 first-file ordering where applicable; project creation needs separate explicit approval,One durable target; no design work before private file inventory and named-version editable-archive capability and _PRE checkpoint'
assert original_scope.count(old_scope) == 1
changed_scope = original_scope.replace(old_scope, new_scope)
patch = ''.join(difflib.unified_diff(original.splitlines(keepends=True), changed.splitlines(keepends=True), fromfile='a/' + contract, tofile='b/' + contract))
patch += ''.join(difflib.unified_diff(original_scope.splitlines(keepends=True), changed_scope.splitlines(keepends=True), fromfile='a/' + scope, tofile='b/' + scope))
(out / 'first-file-ordering.patch').write_text(patch, encoding='utf-8')
(out / 'contract.proposed.md').write_text(changed, encoding='utf-8')
(out / 'scope.proposed.csv').write_text(changed_scope, encoding='utf-8')
for src, label in [(contract, 'contract.before.md'), (scope, 'scope.before.csv')]:
    (out / label).write_bytes((root / src).read_bytes())
guards = json.loads((out.parent / 'protected-current.json').read_text(encoding='utf-8'))
assert all(digest(root / g['path']) == g['sha256'] for g in guards)
inputs = [{'path': x, 'sha256': digest(root / x)} for x in [contract, scope, 'docs/phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md', 'docs/phase-1-ui-reference-production/validation/capability-evidence.md', 'docs/phase-1-ui-reference-production/validation/mcp-call-budget.csv', 'docs/phase-1-ui-reference-production/validation/mcp-call-ledger.csv', 'docs/phase-1-ui-reference-production/reviews/b01-preflight-v1-2026-10-06.md', 'AGENTS.md', '.specify/memory/constitution.md', 'DECISIONS.md']]
inputs.extend({'path': p.relative_to(root).as_posix(), 'sha256': digest(p)} for p in sorted(out.iterdir()) if p.is_file())
inputs.append({'path': (out.parent / 'protected-current.json').relative_to(root).as_posix(), 'sha256': digest(out.parent / 'protected-current.json')})
packet = {'scope': 'Proposed two-document first-file ordering amendment only; not applied or accepted. No calls, file creation, quota use, design work, privacy/archiving claims or pilot release.', 'inputs': inputs}
(out / 'review-inputs.json').write_text(json.dumps(packet, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'inputs': len(inputs), 'guards_unchanged': len(guards), 'patch_lines': len(patch.splitlines()), 'packet_sha256': digest(out / 'review-inputs.json')}, indent=2))
