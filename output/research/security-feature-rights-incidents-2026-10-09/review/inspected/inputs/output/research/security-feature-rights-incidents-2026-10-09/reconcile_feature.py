from pathlib import Path
import hashlib, json

root=Path.cwd()
base=root/'output/research/security-feature-rights-incidents-2026-10-09'
spec_path='specs/001-platform-security-hardening/spec.md'
check_path='specs/001-platform-security-hardening/checklists/requirements.md'
before_spec=(root/spec_path).read_bytes()
before_check=(root/check_path).read_bytes()
assert not (base/'review/review-inputs.json').exists(), 'Do not rerun a completed producer.'
if (base/'before').exists():
    assert (base/'before/spec.md').read_bytes()==before_spec
    assert (base/'before/requirements.md').read_bytes()==before_check
else:
    (base/'before').mkdir()
    (base/'before/spec.md').write_bytes(before_spec)
    (base/'before/requirements.md').write_bytes(before_check)
edits=[]

def replace(raw, old, new):
    newline='\r\n' if raw.count(old.replace('\n','\r\n').encode())==1 else '\n'
    a=old.replace('\n',newline).encode()
    b=new.replace('\n',newline).encode()
    assert raw.count(a)==1, old[:90]
    edits.append({'old':a.decode(),'new':b.decode()})
    return raw.replace(a,b)

spec=replace(before_spec,'| Created / last updated | 2026-10-04 / 2026-10-07 |','| Created / last updated | 2026-10-04 / 2026-10-09 |')
spec=replace(spec,
    'No test count, documentation pass or new login latency number certifies security.',
    '| Handle rights and incidents | Verified purpose-limited rights handling and evidence-based incident decisions follow the controlling workflows; receipt/awareness, actual response/delivery and deletion/recovery remain distinct | Authorized synthetic operator rehearsals and actual protected read/action, clock, copy and delivery boundaries after implementation |\n\nNo test count, documentation pass or new login latency number certifies security.')
spec=replace(spec,
    '## Non-Functional Requirements',
    'The following detailed bindings refine the existing D-076 EU privacy baseline;\nno earlier feature PASS covers these additions. The controlling contracts own the\nworkflow details rather than this feature creating a second policy.\n\n| ID | Requirement | Priority | Verification |\n|---|---|---|---|\n| FSC-15 | Follow [rights intake and verified response](../../docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md#rights-intake-and-verified-response-proposal--2026-10-09): preserve original receipt, proportionate verification and explicit case/object authority; apply the assessed mixed-data response, applicable calendar-month deadline and secure recipient-bound delivery; rights response is distinct from completed scoped deletion | Must | Authorized synthetic rights handling plus actual protected read/delivery/deletion/copy boundaries; no default ID upload, visitor account or automatic destructive action |\n| FSC-16 | Follow [incident assessment/escalation/recovery](../../docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md#incident-assessment-escalation-and-recovery--v1): distinguish alert/awareness/interruption; assess privacy impact, actual processing role and competent recipients; preserve applicable notification/communication duties, minimal case evidence and separate recovery/delivery outcomes | Must | [Defined synthetic rehearsal scenarios](../../docs/phase-1-architecture/contracts/QA_RECOVERY.md#incident-response-rehearsal--v1) after separate execution approval; actual boundary/clock/authority and qualified channel evidence, not a tabletop-only runtime claim |\n\n## Non-Functional Requirements')
spec=replace(spec,
    '| Diagnostic/aggregate evidence |',
    '| Rights-case and incident evidence | Restricted personal/security material as mapped | Explicit case-specific privacy/security purpose and actual grants; contact alone grants no data access | Approved purpose/copy policy and finite necessity reviews; no blanket 90-day or unlimited investigation archive | Separate protected handling and safe audit references; no transcript/credential payload in general diagnostics | No unverified mailbox, transfer, authority or notification route |\n| Diagnostic/aggregate evidence |')
spec=replace(spec,
    'No default monitoring/triage recipient or response SLA is\ncreated.',
    'No default monitoring/triage recipient or response SLA is\ncreated. Rights receipt does not wait for staff opening a message; incident\nawareness follows evidence-supported certainty without waiting for complete\nforensics. The workflows retain different deadlines and qualified grounds; no\ngeneric 30-day response clock, automatic legal exception or new role is added.')
spec=replace(spec,
    '| Immutable publication contract |',
    '| Rights/incident workflow bindings | Scoped privacy/security handlers and qualified operating contacts | FSC-15/16 incorporate the existing security/data/interface and QA definitions; new routes, tables, grants or automatic notification are not selected | Original receipt/awareness and attributable decisions persist; unknown delivery, deletion and recovery cannot be labelled complete |\n| Immutable publication contract |')
spec=replace(spec,
    'These are future behavior oracles from requirements, not executed tests.',
    '20. **Given** a recognized rights request through privacy or another provided official channel, **when** authorized handling verifies and scopes it, **then** original receipt and the applicable calendar-month deadline remain, case-specific control and recipient authorization precede disclosure, and replying does not imply completed deletion. Names/emails, mailbox access, old process proofs or absence of visitor accounts cannot replace the controlling verification/limitation rules.\n21. **Given** a scoped access request involving mixed personal data or another person\'s interests, **when** the handler prepares a response, **then** concrete impact and balancing determine proportionate measures and useful remaining access; no blanket exclusion, whole database dump or disclosure of unrelated credentials. Exact approved privacy operations and copy/deletion policies still apply.\n22. **Given** evolving incident facts, affected people and uncertain notification/recovery outcomes, **when** scoped handlers assess and respond, **then** the controlling incident workflow preserves supported awareness, actual controller/processor duties, all competent recipients and distinct authority/individual decisions; incomplete counts, weekends, owner changes or an RTO result cannot silently extend/reset legal clocks or certify delivery. The incorporated rehearsal catalogue supplies the detailed cases, including breach-nature description for individual notices and assessed exception conditions; no actual communication is authorized by this feature.\n\nThese are future behavior oracles from requirements, not executed tests.')
spec=replace(spec,
    '| Exact alert/diagnostic recipients and channel readiness |',
    '| Qualified rights/incident handling and communication | Privacy/legal/security operating authorities, not assigned here | Before live collection and authorized operating rehearsal | Exact recipient control, notification routes, secure case/evidence copies and scoped primary/backup coverage required; no ordinary content approval may postpone a mandatory incident communication |\n| Exact alert/diagnostic recipients and channel readiness |')
spec=replace(spec,
    '- [ ] Applicable legal/public-content and accessibility review complete.',
    '- [ ] Current FSC-15/16 rights/incident bindings and checklist independently reviewed; prior contract reviews do not certify this feature edit.\n- [ ] Applicable legal/public-content and accessibility review complete.')
spec=replace(spec,
    '- [Security/privacy contract](../../docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md).',
    '- [Security/privacy contract](../../docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md), including its rights intake and incident response definitions. Their separately frozen reviews establish bounded consistency, not feature adoption, legal clearance or operational assurance.')

spec_edit_count=len(edits)
check=replace(before_check,
    'Status: DOING. Created/inspected 2026-10-04 by the specification producer.',
    'Status: DOING. Created 2026-10-04; rights/incident binding inspected 2026-10-09.')
check=replace(check,
    'implementation approval.',
    'implementation approval. The current rights/incident feature additions need a\nseparate scoped review; neither their contract reviews nor earlier feature PASS\nare transferred to these edits.')
check=replace(check,
    '- [x] Alias ownership stays explicitly undecided; no monitoring recipient inferred.',
    '- [x] FSC-15/16 bind rights/incident handling to the owning workflows with future boundary/rehearsal evidence, separate receipt/awareness clocks, assessed notice/exception scope and truthful unknown outcomes.\n- [x] No visitor account/upload, role, endpoint, schema, owner, retention period or execution authority is added; alias ownership remains undecided.')
check=replace(check,
    '- [ ] Applicable legal/accessibility and final specialist evidence complete.',
    '- [ ] Independent review of the current rights/incident feature bindings complete.\n- [ ] Applicable legal/accessibility and final specialist evidence complete.')
(root/spec_path).write_bytes(spec)
(root/check_path).write_bytes(check)
(base/'exact-edits.json').write_text(json.dumps({'status':'DOING','spec_edits':spec_edit_count,'checklist_edits':len(edits)-spec_edit_count,'edits':edits},indent=2)+'\n',encoding='utf-8')
paths=[spec_path,check_path,'AGENTS.md','.specify/memory/constitution.md','DECISIONS.md','TASKS.md',
       'docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md',
       'docs/phase-1-architecture/contracts/QA_RECOVERY.md',
       'docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md',
       'docs/phase-1-architecture/contracts/DATA_CONTRACT.md',
       'docs/software-definition/06-entity-and-public-contact.md',
       'output/research/rights-intake-2026-10-09/review/independent-review-rights-intake-v1.json',
       'output/research/rights-intake-2026-10-09/review/correction-1/independent-review-correction-1-v1.json',
       'output/research/incident-response-definition-2026-10-09/review/independent-review-incident-response-v1.json',
       'output/research/incident-response-definition-2026-10-09/review/correction-1/independent-review-correction-1-v1.json']
paths += [p.relative_to(root).as_posix() for p in base.iterdir() if p.is_file()]
paths += [p.relative_to(root).as_posix() for p in (base/'before').iterdir()]
review=base/'review'
inputs=[]
for rel in paths:
    raw=(root/rel).read_bytes()
    snap=review/'inputs'/rel
    snap.parent.mkdir(parents=True,exist_ok=True)
    snap.write_bytes(raw)
    inputs.append({'path':rel,'snapshot':snap.relative_to(root).as_posix(),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
manifest=review/'review-inputs.json'
manifest.write_text(json.dumps({'status':'DOING','revision_cycle':0,'scope':'Security feature rights/incident binding and producer checklist only; canonical workflows unchanged','inputs':inputs},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'inputs':len(inputs),'manifest_sha256':hashlib.sha256(manifest.read_bytes()).hexdigest(),'spec_edits':spec_edit_count,'checklist_edits':len(edits)-spec_edit_count}))
