from pathlib import Path
import hashlib
import json

root=Path.cwd(); base=root/'output/research/booking-email-ownership-2026-10-08'
out=base/'correction-1'; out.mkdir(exist_ok=False)
m=json.loads((base/'review-inputs.json').read_bytes())
for row in m['inputs']:
    raw=(root/row['path']).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==row['sha256'],row['path']
    assert raw==(root/row['snapshot']).read_bytes()
initial=dict(result='REVISE', reviewer='/root/review_directory_references_v1',
    manifest_sha256='b184afe94b54da464553b3d67e349a890878ca57a4a1f923ec59ea06882a3af3',
    findings=[dict(id='EO01',reason='Explicit current expected revision is missing from fresh verify and extension guards.'),
              dict(id='EO02',reason='Challenge replacement must explicitly revoke existing verified authority and all dependent review/selection eligibility.'),
              dict(id='EO03',reason='Separate verification freshness deadline lacks accessible adjustment; remove or define its timing treatment.')],
    evidence=dict(initial_final_input_pairs=19,prior_prefix_bytes=68352),
    scope=m['scope'])
(base/'initial-independent-review.json').write_text(json.dumps(initial,indent=2)+'\n',encoding='utf-8')
p=root/'docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md'; raw=p.read_bytes()
(out/'INTERFACE_CATALOG.before-correction.md').write_bytes(raw)
def change(a,b):
    global raw
    a=a.replace('\n','\r\n').encode(); b=b.replace('\n','\r\n').encode()
    assert raw.count(a)==1,a[:60]
    raw=raw.replace(a,b)
change('Each extension checks current own proof,\nCSRF, challenge/purpose/email bindings and extension count under the same fence.',
       'Each extension checks current own proof and CSRF/action authority, then reconciles\nmatching admitted operations before fresh-work guards. For a fresh extension,\nrequire expected lineage revision to equal current revision, and recheck eligible\nstate, challenge/purpose/email bindings and extension count under the same fence.\nA stale fresh command conflicts before counters, time changes or any effect.')
change('Recommend verified-email freshness of 1,800 seconds from successful consumption,\nalso bounded by current process/purpose/email authority. This is booking-action\nfreshness, separate from D-076\'s visitor conversation inactivity policy. It does\nnot impose an absolute conversation limit or silently renew any proof/consent.\nWhen verification expires before booking-intent admission, do not expose or admit\nnew slots; invalidate old selection/review eligibility and offer verification\nagain. After a calendar/meeting intent is admitted, expiry cannot erase confirmed\ntruth, reexecute provider work or unlock qualification changes. Reschedule/cancel\nhave their separate authorization rules. Historical verification may remain only\nas purpose-permitted evidence; it is not current slot eligibility.',
       'Successful verification is usable only in that same currently authorized\nbooking process, with its email revision and applicable purpose still current.\nThis profile adds no separate verification-freshness timer. The owning process\'s\nreviewed expiry/accessible continuation governs access; verification, status reads\nor email receipt do not renew that access or consent. A new or recovered process\ncannot inherit this verification. Before booking-intent admission, losing current\nprocess/email/purpose authority disables new slots and invalidates selection/review\neligibility. After calendar/meeting intent admission, loss of this authority cannot\nerase confirmed truth, reexecute provider work or unlock qualification correction.\nReschedule/cancel retain their separate authorization rules. Retained historical\nverification is purpose-permitted evidence only, never a grant to another process.\nD-076\'s conversation inactivity and staff-session clocks remain separate.')
change('Atomically admit the new challenge, invalidate every earlier challenge/verifier\nand dependent selection, reserve delivery/abuse budget, record its operation result',
       'Issue is eligible in QUALIFICATION_COMPLETE with no earlier challenge for the\ncurrent email revision. Explicit resend may replace the most recent challenge in\nQUALIFICATION_COMPLETE, EMAIL_PENDING, EMAIL_EXPIRED, EMAIL_UNDELIVERABLE, VERIFIED\nor SLOT_SELECTED, only before any calendar/meeting intent and with all current\nadmission/revision/purpose guards. It is deliberate re-verification, not an\nautomatic side effect of refresh. No other state admits either mutation.\nAtomically admit the new challenge, invalidate every earlier challenge/verifier,\nrevoke existing verified-email authority and clear all dependent availability,\nselection, review and no-availability eligibility, reserve delivery/abuse budget,\nrecord its operation result')
change('Before comparison, check current process/CSRF/action authority, operation replay,\ncurrent qualification/purpose/email binding, challenge validity and attempt budget.\nFresh verifies compare and consume under the same transaction/fence as correction,',
       'First check current process/CSRF/action authority and reconcile matching admitted\noperation intent/results. For fresh Verify, require expected lineage revision to\nequal current revision and recheck eligible EMAIL_PENDING state, current\nqualification/purpose/email binding, challenge validity and attempt budget.\nReject a stale fresh command before comparison, guess reservation or any effect.\nFresh verifies compare and consume under the same transaction/fence as correction,')
change('verification expiry before and after booking intent;', 'loss of verification authority before and after booking intent;')
assert raw.startswith((base/'INTERFACE_CATALOG.before.md').read_bytes())
p.write_bytes(raw)
visual=root/'docs/software-definition/definition-walkthrough.html'; v=visual.read_bytes()
(out/'definition-walkthrough.before-correction.html').write_bytes(v)
a=b'Its historical result does not mean email verification is still current; the proposed slot-access freshness is thirty minutes.'
b=b'Its historical result does not grant current eligibility. Verification stays bound to the same currently authorized booking process and address.'
assert v.count(a)==1; v=v.replace(a,b)
a='ten-minute code window, ten extensions, thirty-minute booking-action freshness and abuse limits'.encode()
b='ten-minute code window, ten extensions and abuse limits'.encode()
assert v.count(a)==1; v=v.replace(a,b)
visual.write_bytes(v)
print(json.dumps(dict(catalogue_sha256=hashlib.sha256(raw).hexdigest(),closed_findings=['EO01','EO02','EO03'])))
