from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

def replace_once(text, old, new):
    if text.count(old) != 1:
        raise SystemExit('Expected exactly one source block; no write made.')
    return text.replace(old, new, 1)

proof_path = ROOT / 'docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md'
handoff_path = ROOT / 'docs/phase-1-architecture/contracts/HANDOFF_LIFECYCLE.md'
proof_bytes = proof_path.read_bytes()
handoff_bytes = handoff_path.read_bytes()
for path, data in [(proof_path, proof_bytes), (handoff_path, handoff_bytes)]:
    preserved = Path(__file__).parent / (path.name + '.before')
    if preserved.read_bytes() != data:
        raise SystemExit('Predecessor differs; inspect before editing.')

proof = proof_bytes.decode('utf-8').replace('\r\n', '\n')
handoff = handoff_bytes.decode('utf-8').replace('\r\n', '\n')
proof = replace_once(proof,
    'HTTP/browser/store/socket enforcement remain required.\n',
    'HTTP/browser/store/socket enforcement remain required.\n\n'
    'The 2026-10-07 visitor-lifetime amendment below implements the definition\n'
    'direction in [D-076](../../../DECISIONS.md#d-076--visitor-inactivity-eu-privacy-baseline-and-production-data-deferrals).\n'
    'It is outside earlier frozen review inputs and requires fresh independent\n'
    'security/accessibility review; no prior PASS covers these changed bytes.\n')
proof = replace_once(proof, '''Use Secure, HttpOnly, SameSite=Lax, Path=/, no Domain, with finite Max-Age capped
to remaining absolute server validity. Its cookie is the bearer; only the separate
current `X-Hengshi-CSRF` header and exact Origin complete create authorization.''',
'''Use Secure, HttpOnly, SameSite=Lax, Path=/, no Domain. The five-minute provisional
credential may have Max-Age capped to its remaining setup validity. On promotion,
propose a new-generation browser-session cookie with neither Max-Age nor Expires;
its server authorization remains subject to the 30-minute inactivity/End profile
below. Do not inherit the provisional cookie's expiry or introduce a hard maximum
conversation age. Browser closure/restore is not evidence of server ending or
continued authority. The cookie is the bearer; only the separate current
`X-Hengshi-CSRF` header and exact Origin complete create authorization.''')
proof = replace_once(proof, '''Independently propose chat provisional validity of five minutes absolute and
created chat access of 30 minutes idle/two hours absolute from successful
promotion. These happen to match the initial booking numbers but are separate
chat clocks, not inherited ownership or an approved SLA. Only a deliberately
admitted permitted user business action may refresh idle within absolute expiry.
Creation replay, polling, CSRF reads, provider replies, socket heartbeats,
reconnection and failures cannot. CSRF ends with its bound current proof; current
source, consent, withdrawal and authorization can deny earlier. Clock uncertainty
cannot extend an expiry; shared time/fencing must be specified and measured.''',
'''Reconciled 2026-10-07 under D-076: retain the proposed five-minute absolute
provisional setup validity. After successful promotion, the visitor conversation
has **30 minutes of inactivity and no absolute conversation duration**. Deliberate
authorized End conversation closes access earlier. The former two-hour visitor
limit is withdrawn; booking and staff sign-in clocks are separate and unchanged.
Proof rotation, cookie expiry, provider limits or a hidden maximum process age
must not recreate that rejected conversation limit.

Propose one server-authoritative activity deadline and terminal fence for the
conversation, shared across tabs and channels. Start the idle clock at promotion;
reset it to server admission time plus 30 minutes only for a new, deliberate,
currently authorized visitor message, eligible consent/business change or More
time action. During an active human consultation, a new message from its current
authorized assigned staff member also counts as genuine conversation activity;
it does not extend that staff member's authentication session or grant access to
the visitor's private AI context. Activity requires all current proof, role,
assignment, source/purpose and operation guards. Local reading/typing is not
covert telemetry: the visitor can explicitly choose More time while reading.

Creation replay, duplicate message/change/More time operations, polling, CSRF
reads, provider output, socket heartbeats, reconnection, failed/denied requests
and automated activity cannot reset the clock. Reconciliation reports the original
admission and deadline, rather than creating a second extension. Client timestamps
cannot backdate activity. At admission time equal to or later than the current
deadline, access is expired; a late renewal cannot resurrect it. Serialize activity,
expiry, ending and output admission through the same authoritative generation/fence.
Once ending/expiry is committed, no later activity restores that conversation.

Before idle expiry, warn accessibly with at least 20 seconds of usable response
time and a simple keyboard/touch-operable More time action. Show the current
server-derived deadline, preserve focus and permitted progress, and confirm an
extension only after server admission under current authority. More time resets
the idle window to 30 minutes; it is available repeatedly, with no absolute-age
or extension-count cutoff. Late/lost replies reconcile the same operation and
cannot display a fresh success or silently share selected text. The accepted
D-062/D-063 `extension_factor_min: 10` remains distinct from W3C's minimum ten
extension opportunities; the complete-process mapping/preservation needs review.
Unbounded legitimate continuation is not proof of accessibility conformance and
does not authorize five hours of unattended access or longer source retention.

An End conversation intent requires the visitor's current own-process proof or,
for the human consultation only, its currently authorized assigned staff member
and explicit ending permission. Apply the existing ending/ordered-suppression
guards; revoke the relevant conversation proof/CSRF and fence new messages,
preview sharing, replay and output when ending is authoritative. Expiry likewise
denies access server-side even if physical socket/cookie cleanup is delayed.
Unknown ending work remains unresolved rather than a fabricated completed End.
Do not end a booking, disable staff availability or grant general staff access
to private AI conversations. Visitor End needs its own directional control/error
contract before implementation; no endpoint is introduced by this prose.

CSRF ends with its bound current proof. Earlier source, consent, withdrawal,
assignment or authorization loss can deny a dependent action without creating
new access. Clock uncertainty fails closed; shared time/fencing must be specified
and measured. Cookie/proof rotation alone is not genuine activity and cannot
renew idle, revive terminal authority or silently reset the conversation age.''')
proof = replace_once(proof, '''[MDN Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie)
documents cookie transport/prefix behavior; [OWASP sessions](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
supports server-controlled idle/absolute expiry and privilege-transition renewal;''',
'''[MDN Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie)
documents cookie transport/prefix behavior. Rechecked 2026-10-07: omitting cookie
expiry attributes produces a browser-session cookie, which browser session restore
may retain; server authorization must still expire independently. [OWASP sessions](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#session-expiration)
recommends both idle and absolute timeouts. D-076's no-absolute visitor conversation
policy is an explicit product choice requiring a scoped security review, not a
claim that OWASP recommends indefinite anonymous credentials. Least privilege,
server invalidation, bounded admission and current revocation remain required;''')
proof = replace_once(proof, '''only an admitted deliberate permitted user change may refresh idle within the
existing absolute limit.''',
'''only newly admitted genuine activity under the D-076 profile above can refresh
the visitor idle deadline; there is no absolute visitor conversation cutoff.''')

handoff = replace_once(handoff,
    'and the exact implementation contracts remain required.\n',
    'and the exact implementation contracts remain required.\n\n'
    'The 2026-10-07 D-076 timing reconciliation at the end of this document is\n'
    'outside earlier frozen review inputs. Its founder-selected inactivity policy\n'
    'is recorded; the revised control/security/accessibility mechanism remains\n'
    'DOING pending fresh independent review. Earlier PASS receipts cover only\n'
    'their preserved inputs, not this amendment.\n')
handoff = replace_once(handoff, '''renewal endpoint or UI is implemented. Prior reviewed bytes remain intact.
This section records an affected conflict, not an amendment to accepted timing
criteria or a production numeric selection.''',
'''renewal endpoint or UI is implemented. Frozen predecessors remain preserved.
The 2026-10-07 amendment records D-076's resolved visitor-lifetime direction;
it does not amend the accepted accessibility criteria or approve the proposed
resource numbers/implementation. Fresh review of this amendment remains required.''')
handoff = replace_once(handoff, '''its finite lifetime is subordinate to the finite permitted conversation/source
profile, which remains held below. Numerical resource targets are unmeasured and
require independent acceptance plus actual allocation/clock/load evidence.''',
'''its validity is subordinate to the current permitted conversation/source
profile. D-076 selects inactivity/explicit End, with no absolute conversation
age; it does not extend source retention. Continuing a valid conversation does
not permit unlimited transcript/buffer growth. Refuse new work at capacity rather
than silently deleting an active conversation to admit another. Numerical resource
targets are unmeasured and require independent acceptance plus actual allocation,
clock and load evidence.''')
start = handoff.index('### Timing conflict requiring a scoped decision\n')
end = handoff.index('### Review presentation and implementation exit\n', start)
handoff = handoff[:start] + '''### Timing conflict requiring a scoped decision

Resolved direction 2026-10-07: [D-076](../../../DECISIONS.md#d-076--visitor-inactivity-eu-privacy-baseline-and-production-data-deferrals)
selects 30 minutes of inactivity or deliberate authorized End, with no absolute
visitor conversation time limit. The old two-hour proposal and its twenty-hour
planning consequence are superseded; this heading is retained for existing links.
No further founder duration choice is pending. The revised mechanism still needs
independent security/accessibility review and eventual implementation evidence.

D-062/D-063 accepts the complete-process timing criteria in
[column authority](../../phase-1-ui-reference-design/COLUMN_AUTHORITY_PROPOSAL.md).
TPL-AI-CONCIERGE and TPL-HUMAN-HANDOFF each select TL-WARN-EXTEND when a user limit
is introduced: at least 20 seconds warning, extension_factor_min 10, preservation
of permitted data/authoritative state and accessible reauthentication when needed.
No accepted record permits TL-EXCEPTION. D-076 retains these obligations.

The [revised chat access profile](PRIVATE_PROCESS_PROOF.md#access-lifetime-retention-and-pending-cleanup)
defines genuine server-admitted activity, repeated explicit More time, shared
cross-tab idle deadlines and current visitor/assigned-staff ending authority.
Reading a preview, polling, automated replies or credential rotation cannot renew
access. A newly admitted More time action before expiry resets the 30-minute idle
window without an absolute-age or extension-count ceiling. Confirmation reflects
authoritative admission; unknown responses reconcile the same operation. Continuing
access never extends consent, source entitlement, legal retention, revoked assignment
or permission for a provider transfer. Preserve still-permitted progress while
authority remains valid; expired proof cannot resurrect lost ephemeral state.

Rechecked 2026-10-07: [W3C SC 2.2.1](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html)
distinguishes adjustment to ten times a default from a simple extension action
offered at least ten times with at least 20 seconds to respond. The accepted
project `extension_factor_min: 10` is distinct and must not be replaced by an
extension count. Propose mapping repeated continuation to a complete process
that can remain usable beyond ten times its default interval, while each unattended
idle window stays 30 minutes. The mapping, preservation and usable response-time
evidence remain for independent review; no conformance follows from unlimited
continuation alone. No arbitrary new twenty-hour envelope or exception is selected.

[OWASP session guidance](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#session-expiration)
recommends absolute as well as idle timeouts; the founder explicitly selects a
different visitor conversation policy. Review that risk and the bounded proof,
revocation, rotation and admission mechanisms without silently restoring a hard
conversation cap. Staff authentication clocks, booking lifetimes and class-specific
retention remain separate. Work deadlines and source/buffer ceilings bound resources,
not the total duration of a legitimately continuing visitor conversation.

''' + handoff[end:]
handoff = replace_once(handoff, '''Exact continuation duration, proof/clock mechanism, permitted state preservation,
class-specific retention/deletion and warning screens remain held for the scoped
decision and independent review. Test later at actual admission, storage, clock,
revocation and browser boundaries: deadline exhaustion without reservation release,
source loss, cross-tab limits, stale preview, near-expiry extension, late/lost
continuation responses, disabled/replayed sharing and assistive-technology reading.''',
'''The founder duration choice is resolved; proof/clock/End controls, permitted-state
preservation, class-specific retention/deletion and warning screens remain DOING
for independent review and later implementation. Test at actual admission, storage,
clock, revocation and browser boundaries: an active conversation beyond the old
two-hour mark; warning/More time and retained permitted progress; repeated extension
and stale duplicate denial; exact idle-boundary/End-versus-message races; authorized
visitor and assigned-staff ending versus unassigned-staff denial; retained cookie
after expiry; deadline exhaustion without reservation release; source loss;
cross-tab limits; stale preview; near-expiry extension; late/lost continuation
responses; disabled/replayed sharing; and assistive-technology reading.''')

for path, original, content in [(proof_path, proof_bytes, proof), (handoff_path, handoff_bytes, handoff)]:
    newline = '\r\n' if b'\r\n' in original else '\n'
    path.write_bytes(content.replace('\n', newline).encode('utf-8'))
print('Reconciled two definition contracts; prior bytes preserved; no application change.')
