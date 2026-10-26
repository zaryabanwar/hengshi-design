"""Add a source-linked visual explanation without changing application behavior."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
p=root/'docs/software-definition/definition-walkthrough.html'
raw=p.read_bytes()
before=out/'definition-walkthrough.before.html'
assert not before.exists()
before.write_bytes(raw)
text=raw.decode('utf-8')
assert 'id="record-retention"' not in text
section='''<details id="record-retention"><summary>How each record gets a purpose and expiry</summary>
<p><span class="tag proposed">Reviewed engineering proposal</span> The logical mapping covers all 22 record types. These examples explain that proposal; they do not approve new retention periods, enable collection or certify legal compliance.</p>
<ol class="flow"><li><strong>Identify the exact purpose</strong>A saved chat, booking, staff permission and security event serve different jobs. Each identifying field needs its own permitted purpose; a record name alone is not enough.</li><li><strong>Bind the approved policy</strong>Before collecting, saving or sharing, resolve the permitted policy, basis, notice and consent where required. Missing or unapproved bindings deny that affected action.</li><li><strong>Keep the original clock</strong>Edits and new IDs cannot renew copied personal content. A derived record keeps its source boundary. Mixed-purpose fields are separated or removed at their respective limits.</li><li><strong>Clear the permitted copies</strong>Expiry stops ordinary access. Deletion checks the mapped stores and recipients; recovery applies expiry and deletion suppression before serving. Unknown vendor copies cannot be called deleted.</li></ol>
<div class="grid two"><article class="card"><h3>Chat and a saved brief</h3><p>Without retention consent, chat stays ephemeral. Consented retained messages and a saved brief use their own proposed anchors under the accepted 90-day rule. A brief copied from earlier chat cannot extend that source content's expiry.</p><p class="small">Ending access is separate from stored-record retention. An active conversation has no absolute age limit; older retained messages can expire while it continues.</p></article><article class="card"><h3>A booking and its email proof</h3><p>Necessary scheduling information follows the booking purpose. The temporary email-verification proof has a separate short security lifetime; it does not become meeting history. Unknown provider work retains only justified reconciliation state.</p><p class="small">The proposed booking schedule still needs adoption. Exact post-expiry proof-store cleanup remains open; uncertainty cannot keep every personal field forever.</p></article><article class="card"><h3>Staff and review evidence</h3><p>Current staff eligibility, a login credential and a publication-review decision are separate field purposes. Removing staff access does not remove their Microsoft account. Audit references cannot inherit the longest period by default.</p><p class="small">Publication-accountability retention remains unresolved. An immutable release is not permission to serve withdrawn personal content.</p></article><article class="card"><h3>Availability and deletion</h3><p>A settled expired availability intent follows the proposed cleanup rule; uncertain on/off work stays restricted. A deletion request may need a minimal suppression key until recoverable copies are handled.</p><p class="small">That key is still personal when linkable. A completed rights-case outcome and a recovery-suppression key have separate purposes and disposal rules.</p></article></div>
<p class="callout">The definition is reviewed; exact legal bases, notice/provider bindings, proof cleanup and release-accountability retention remain open. The new periods and recovery window are proposals. Physical enforcement and integrated founder acceptance come later.</p>
<div class="source-links"><a href="../phase-1-architecture/contracts/DATA_CONTRACT.md#record-purpose-retention-binding-proposal--2026-10-08">All 22 record-purpose bindings</a><a href="../phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md#proposed-retention-schedule-and-immutable-clocks">Controlling proposed retention schedule</a><a href="../phase-1-architecture/contracts/reviews/record-purpose-binding-v1-2026-10-08.md">Bounded independent definition review</a></div>
<p class="small">This visual translation awaits its own review. The linked definition review does not accept this presentation, a production screen or actual enforcement.</p>
</details>
'''
needle='<details id="privacy-policy"><summary>'
assert text.count(needle)==1
start=text.index(needle)
end=text.index('</details>',start)+len('</details>')
nl='\r\n' if '\r\n' in text else '\n'
text=text[:end]+nl+section.replace('\n',nl)+text[end:]
needle='<a href="#system">System boundaries</a>'
assert text.count(needle)==1
text=text.replace(needle,needle+'<a href="#record-retention">Data and privacy</a>')
text=text.replace('Founder review · 7 October 2026','Founder review · 8 October 2026',1)
needle='New detailed controls/policies remain unreviewed; complete Phase 1 acceptance is pending.'
assert text.count(needle)==1
text=text.replace(needle,'Detailed controls and policies retain their separate review scopes; complete Phase 1 acceptance is pending.',1)
p.write_bytes(text.encode('utf-8'))
print(json.dumps({'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'presentation_only':True,'section':'record-retention'}))
