# Staff-session generation and renewal — v1

Status: DOING. Logical mechanism proposal, 2026-10-17, under SEC-001/002/004/005.
The [security contract](SECURITY_PRIVACY_CONTRACT.md) retains sign-in mediation,
action/object/purpose authority, qualifying activity, cookie/CSRF and privacy
rules. This document proposes local session state, renewal, recovery and output
ordering within that boundary. [Staff channel semantics](HANDOFF_LIFECYCLE.md#staff-channel-initialization-and-control-proposal--2026-10-06)
and [operator-list dependencies](OPERATOR_READS.md#complete-output-dependency-fence)
remain controlling for those consumers. Visitor access clocks are separate.

The [logical review](../../../output/research/staff-session-mechanism-2026-10-17/independent-review-logical-v1.json)
has bounded PASS at 13 frozen inputs. The separate
[initial translation review](../../../output/research/staff-session-mechanism-2026-10-17/canonical-binding/independent-review-canonical-binding-v1.json)
identified SSBIND01; the [eight-input correction review](../../../output/research/staff-session-mechanism-2026-10-17/canonical-binding/correction-1/independent-review-binding-correction-v1.json)
has bounded PASS after restoring same-session successor protection. The initial
11 inputs and correction inputs are preserved. This later reference edit is
outside those inspected bytes; none of these verdicts certifies policy adoption,
exact encoding, physical output fencing, runtime security or integrated acceptance.
No session table, route, grant, key, account, migration or
application implementation is created. Exact encoding and integrated founder
adoption remain separate from logical consistency.

## Session authority and original clocks

Retain the accepted 30-minute idle and eight-hour absolute limits. Idle begins at
sign-in and advances only at the first guarded admission of an explicitly mapped
staff business command. An admitted pending command may count once; replay and
reconciliation do not count again. Reads, polling, heartbeat, socket readiness,
reconnect, CSRF/status reads, token maintenance, provider output and client input
gestures do not manufacture activity. Other business commands still need an
explicit activity mapping; no rule accepts any authenticated HTTP request.

At decision time require current principal eligibility, session authority,
identity-source freshness, token validity/currentness and boundary-specific
CSRF/action/object/purpose/consent/assignment/revision guards. Require
`now < min(last_qualifying_admission + 1800 seconds, original_issue + 28800 seconds)`.
Equality denies. No token leeway, retry, new channel, another tab or rotation
resets these anchors or revives a terminal session. Activity cannot move backward,
wrap a generation or update a session already expired/revoked.

Recommend PostgreSQL, already the architecture's durable authority, for private
principal/session security state and guarded transitions. Redis supplies required
rate-limit/invalidation assistance, not an independent session truth. This is a
store-family proposal, not a created table, retention adoption or deployment.
Unknown authority/clock/key/purpose/limiter or unsettled accounting denies affected
work; no JWT-only, stale-cache or unprotected Redis-outage fallback is admitted.

| Private logical record | Minimum proposed state and limits |
|---|---|
| Principal | Stable private principal reference, enabled/activation state and monotonic security epoch/current authority revision. Current grants and source-freshness evidence stay separate from JWT claims. |
| Session | Independent server identity bound to one principal/authentication source, original issue, last qualifying admission, absolute deadline, terminal revocation/replacement state, security epoch and current CSRF generation/protected secret reference. |
| Current token | Independent token ID and generation, original token issue/expiry, mandatory renewal due, signing-profile/key association and exact minimal claims bindings. No ordinary stored raw JWT. |
| Immediately prior token | At most one previous token ID/generation and original signing/claims associations, with fixed recovery-until. It is not a second business credential or unbounded bearer-history table. |

All records retain their existing identifying/credential classes and source/copy
policy. Retirement needs bounded recovery plus known settlement and mapped
disposition; this proposal grants no indefinite session/audit retention.

Recommend a deterministic guard order: principal, session, then required sorted
object/purpose/source guards. Principal disable/security-epoch changes serialize
against admission; session activity, renewal and revocation use the same current
session guard. Concrete lock/conditional-update forms, deadlock/rollback handling
and physical mappings remain to review. Evaluate trusted database time after
waiting for all required guards. A transaction-start timestamp from before a wait
is not current-time evidence. Clock rollback/unknown health fails closed; precision,
drift/failover health and exact comparison remain explicit bindings.

## Token renewal and immediate-prior recovery

Propose renewal due 900 seconds after token issue and immediate-prior recovery
for at most 60 seconds after cutover. These are unmeasured Hengshi security/usability
candidates requiring adoption, not approved policy or standards-prescribed values.
The original session clocks remain unchanged.

Token expiry is no later than the original session absolute boundary; an unexpired
signature is insufficient. The current server record and mandatory renewal due
additionally gate business use. This permits a still-idle-eligible session to use
bounded renewal after browser sleep, without accepting an expired JWT or adding
a separate long-lived browser refresh secret. This is not universal sleep recovery:
an expired JWT cannot renew even while the server session clock is still eligible.
Exact token expiry relative to renewal due remains a required encoding binding.

| Presented authority | Permitted use, subject to all current guards |
|---|---|
| Current token, before renewal due | Existing permitted business and session-control boundaries. |
| Current token, at/after renewal due but session still eligible | Only bounded session-control/status/CSRF retrieval/renewal/logout. No new business command, private business projection, provider effect or socket-ticket issuance. |
| Immediately prior authentic token, within its original recovery window | Only protected renewal recovery with the still-current session CSRF/source guards. No work reads, business command, ticket, clock renewal or successor fork. |
| Older/expired authentic token or prior token outside recovery | Deny. Do not restore it or extend recovery. Stale A presentation alone cannot automatically revoke legitimate current successor B in the same session, or any unrelated session. |
| Revoked/replaced/expired session or disabled principal | No protected admission; deliberate fresh sign-in and current eligibility are required. |
| Unknown required authority/source/clock/key/accounting | Safe unavailable/denial under the eventual boundary profile; no permissive fallback. |

Successful existing sign-in creates independent server session identity and
security/CSRF/token generations. Never preserve caller-chosen or visitor/pre-login
authority. Revoke an identified replaced current session under its guard before
a replacement becomes authoritative. Uncertain issue is reconciled, not repeated
as unbounded session creation.

Only the origin/CSRF-protected renewal control rotates a token; ordinary private
GETs retain no Set-Cookie. After current identity/session/freshness/clock and finite
work admission, serialize renewal on the session guard. When due, create one new
token ID/generation and fixed issue/expiry/key bindings. Move only the former
current record into the single recovery slot until the earliest of cutover + 60
seconds, its original token expiry and the current session idle/absolute bound.
Keep the same session and current CSRF generation; reset no activity/absolute clock.

A valid early renewal may re-deliver the same current token identity/claims and
original expiry, never create another generation or extend a clock. The frontend
normally waits for due status and cannot busy-loop. During prior recovery,
concurrent old-token calls re-deliver that same already-current generation and
original claims/times/key association; they never create another successor.
Recovery requires the existing current CSRF proof; absence or loss does not invent
another recovery credential or authorization fallback.

Retain only the protected metadata needed to reconstruct those same current
claims/identity with their original signing association. Never repair delivery
with changed claims/times or a raw JWT in ordinary session/audit records. Unknown
or unavailable safe signing material fails closed with reauthentication recovery.
Stale authentic reuse may produce a redacted security category under current
policy. Stale A presentation alone cannot automatically revoke the legitimate
same-session successor B or an unrelated session. Suspected compromise follows
its separately authorized workflow. Bearer possession cannot perfectly distinguish
an attacker from a delayed legitimate request.

## Cookie delivery and multiple tabs

Recommend a browser-session cookie on normal issue/re-delivery: omit Max-Age and
Expires, retaining the proposed exact host-prefixed Secure/HttpOnly/SameSite=Lax/
Path attributes. A fixed browser idle expiry cannot follow later admitted socket
activity and could otherwise remove a still-eligible credential. No persistent
variant is selected. The existing cap on any future selected persistent expiry
still applies. Browser close or restore is not server logout; original clocks,
token/generation eligibility and revocation remain authoritative. Explicit logout
expires the exact cookie identity. No JWT enters JS, response bodies or browser
local/session storage.

Before a credential/control reply is admitted, recheck principal/session/security
epoch, current token, source purpose and expiry. Cookie delivery is not exactly
once. An old delayed network response may overwrite a newer browser cookie;
server currentness prevents old authority from becoming valid again. Recovery or
fresh sign-in may be necessary. Do not claim perfect Set-Cookie ordering.

Use one bounded in-tab auth coordinator with at most one renewal in flight and
separate auth/session/navigation epochs. Cross-tab hints reduce duplicate work
but never elect a trusted global credential writer. The server serializes requests.
A visible current page may do one protected transport renewal when authoritative
status says due; it does not count as activity. No wake/reconnect catch-up storm,
unbounded timer/retry or automatic business-command replay. Unknown result follows
the one bounded current/prior recovery, then deliberate reauthentication.
Session-control status exposes no work/object/grant inventory.

## Effects, channels and private output

Token cutover fences old-token business admission and token-bound channels,
unused send tickets and queued private output under the existing staff-channel
rules. Reinitialize/reconcile under current session/token/assignment/consent before
fresh readiness. Never resend old text automatically. Rotation/session loss does
not create visitor End, reassignment, availability, delivery or booking outcomes.

A durably admitted intent keeps its immutable identity and independent lifecycle.
Session loss does not prove no effect or cancel a provider operation. Later work
and disclosure require their current actor/service/object/purpose guards; a worker
cannot keep a stale JWT as durable authorization.

One output admission covers one already-serialized bounded private projection or
ordered frame. Immediately before final writer handoff recheck every participating
principal/session/token/object/purpose/source and copy-expiry generation, including
operator lookahead/anchor dependencies. The verdict is not a reusable durable permit
for delayed output. Stale/unknown authority suppresses, never truncates into success
or discloses a private reason.

The final per-session writer admission must serialize with revocation/rotation
and trusted expiry across workers. Propose a session-guarded nonblocking handoff
of exactly that bounded projection, with no later queue reuse of its authority;
a delayed worker re-enters the current guard. Do not hold a database transaction
across unbounded provider/network I/O. A DB commit/cache notification alone proves
no output fence. Exact guard-to-writer linkage, expiry and bounded cancellation/
drain evidence remain necessary; without them this candidate cannot be adopted.
Bytes already admitted/handed off under earlier valid authority may arrive later
and cannot be recalled. Known revocation blocks later admissions, unused tickets
and not-yet-admitted queued data, not remote packet delivery or past effects.

## Logout, permission changes and recovery

Eligible same-origin CSRF-protected logout atomically revokes the exact session
and its CSRF/token/channel/output generations before acknowledging local
invalidation. Clear the exact cookie identity. Existing repeated-old-logout rules
remain harmless and cannot use a stale proof to revoke an eligible different
session. Uncertain acknowledgement is neither a new login nor cancelled consultation.

A currently authorized principal-disable/removal/security decision increments
the principal security epoch and fences affected sessions before later admission.
It cannot depend on enumerating sockets or waiting for JWT expiry. Who may perform
principal-wide action remains explicit existing policy, never administrator by
default. Privilege/security-context changes cannot silently elevate an existing
session; fence old authority and require fresh deliberate identity admission where
current policy requires it. Reissue alone approves no new grant. Object/purpose
permission reductions apply at every current guard regardless of token clocks.

Microsoft sign-out is separate. A verified supported front-channel/signal
integration may invoke only its reviewed exact local revocation binding; it is
not configured or guaranteed here. Never substitute a Microsoft redirect for local
invalidation or trust an arbitrary callback/session ID. Entra eligibility freshness
and outage/signal bindings remain required; unknown required freshness denies,
without inventing offline grace. No Graph scope or tenant change is authorized.

Restore/restart cannot resurrect old active epochs or copy cookies into new
authority. Deny old sessions until current principal/session/revocation/deletion
evidence is trustworthy; then follow reviewed recovery or fresh sign-in. Recover
only still-permitted retained work under current principal/object/assignment/
consent. Reconcile uncertain immutable operations before new commands. Do not
reconstruct lost ephemeral transcripts or revive expired proofs.

Retain accepted warnings, accessible sign-in/focus and TL-WARN-EXTEND/permitted
progress obligations. Token maintenance is not More time. During token-bound
channel recovery show reconnecting/unknown honestly and preserve only permitted
draft/reconciliation state. Complete-process interaction/accessibility is unqualified.

## Required qualification and remaining bindings

After implementation, test two-tab A-to-B renewal without a C fork or automatic
B revocation caused solely by stale A; lost/late
cookies after replacement/logout; exact idle/absolute/renewal/recovery boundaries;
post-lock time and clock rollback; once-only admitted activity; rotation during
pending text/effects; cross-worker output/revocation races; source-copy and
operator lookahead/anchor fences; authority/limiter/key outage and restore; and
actual token/cookie/CSRF/Origin, load/cancellation and accessible browser behavior.
No prose checks, token decode or schema fixtures prove these controls.

Numeric renewal/recovery adoption, actual security-state/copy policy, Entra
freshness, final-writer/clock mechanisms, claims/algorithm/key encodings, session
control endpoint IDs/paths/methods/schemas, precise raw HTTP/error/resource limits,
screens and complete stable graph remain required. Current logical functions do
not silently add routes to the catalogue. This proposal selects no provider,
cryptographic key or installed store and grants no implementation/Git permission.

Research checked 2026-10-17: Context7 `/jpadilla/pyjwt` and
[PyJWT API](https://pyjwt.readthedocs.io/en/stable/api.html),
[RFC8725](https://www.rfc-editor.org/rfc/rfc8725.html),
[OWASP session guidance](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html),
[PostgreSQL locks](https://www.postgresql.org/docs/18/explicit-locking.html) /
[current-time functions](https://www.postgresql.org/docs/18/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT),
[Microsoft OIDC sign-out](https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc#single-sign-out)
and [cookie behavior](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie).
These support verification/lifecycle primitives, not Hengshi's numeric periods,
state mappings or physical fence. PyJWT documentation's 2.15.1 label is an
observation, not a selected compatible version, installation or registry proof.
