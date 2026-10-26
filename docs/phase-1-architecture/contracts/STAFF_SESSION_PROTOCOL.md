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
The control/claims candidate below proposes the exact expiry binding; it remains
unadopted and does not change the original session clocks.

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
freshness, final-writer/clock mechanisms, selected algorithm/key inventory,
catalogue/data registration, screens and complete stable graph remain required.
The following control candidate now supplies prospective IDs, paths, claims,
directional shapes and finite HTTP/resource targets, separately from their
adoption and physical enforcement. It does not silently add deployed routes.
This proposal selects no provider,
cryptographic key or installed store and grants no implementation/Git permission.

## Own-session controls and minimal claims proposal — 2026-10-17

Status: DOING. Four candidate registrations for existing SEC-004/005 functions,
not deployed endpoints or new grants. The [initial control review](../../../output/research/staff-session-controls-2026-10-17/independent-review-controls-v1.json)
identified SSCTRL01. The [corrected logical proposal](../../../output/research/staff-session-controls-2026-10-17/correction-1/proposal-v1.json)
has [bounded independent PASS](../../../output/research/staff-session-controls-2026-10-17/correction-1/independent-review-controls-correction-v1.json)
at 17 frozen inputs after correcting shared-network exclusion. Those reviewed
inputs are preserved. This canonical translation and its
[directional schema](staff-session-control.schema.json) have a separate
[17-input bounded review PASS](../../../output/research/staff-session-controls-2026-10-17/canonical-binding/independent-review-canonical-controls-v1.json),
including independently replayed24 representation methods. Exact reviewed bytes
are preserved; this later reference edit is outside them. No runtime security,
catalogue/data adoption or integrated acceptance follows.

| Candidate | Request and successful projection |
|---|---|
| IF-AUTH-01 `GET /api/v1/staff/session` | Current eligible cookie, no query/body/selectors. `200` closed own snapshot: `kind: staff_session`, `context_id` equal own server session reference, positive `authority_revision`, `state: current` or `renewal_required`, and `server_time_ms`, `idle_deadline_ms`, `absolute_deadline_ms`, `renewal_due_ms`, `token_expires_ms`. No JWT, CSRF, principal/name/email, roles/grants or work inventory. |
| IF-AUTH-02 `GET /api/v1/staff/session/csrf` | Same current-only read admission; no CSRF header needed for this bootstrap. `200` closed `kind: staff_csrf`, own `context_id`, positive `csrf_generation`, canonical `csrf_token`. Prior-token tabs cannot bootstrap it. |
| IF-AUTH-03 `POST /api/v1/staff/session/renewals` | No query; exactly empty JSON `{}`, current or permitted prior-recovery cookie, current CSRF and mutation source guards. `204`, no JSON, one current staff Set-Cookie. Before due re-delivers the same claims/identity/times; due creates one successor; prior recovery re-delivers that existing successor. No activity, original-clock, CSRF-generation or recovery-window reset. |
| IF-AUTH-04 `POST /api/v1/staff/session/logout` | No query; exactly `{}`; current cookie including renewal-due current, current CSRF and mutation source guards for eligible revocation. `204` only after exact-session authority invalidation, followed by clearing the exact cookie identity. No provider redirect or all-device claim. |

Status is one coherent guarded snapshot. Its revision advances on relevant
session-authority changes, never reads. Context/revision are transient UI hints,
not client selectors or authorization. Times are exact UTC Unix milliseconds in
`0..253402300799999`; require canonical raw integer spelling. Deadline ordering,
currentness, precision and eligibility remain actual semantic checks. Reads do
not Set-Cookie, manufacture activity, rotate a generation or create missing state.
Unknown current CSRF/secret state is unavailable, never recreated under GET.
The proof reuses the existing 43-character canonical unpadded base64url profile
for 32 random bytes; it is an intentional transient JS synchronizer secret,
never the HttpOnly JWT. Guard its current context/generation before output.

Renewal retains the logical current/prior rules above. Recheck security/session/
token/output eligibility before Set-Cookie. A prepared output overtaken by a
known context/token change is fixed `409 session_changed/check_session`;
unknown authoritative outcome is `503`, not another successor. A successful
response does not prove browser storage. Neither JavaScript nor a response body
receives the JWT. Use Secure, HttpOnly, SameSite=Lax, Path=/, no Domain/Partitioned;
normal issue/re-delivery omits Max-Age/Expires. Logout clears that exact
`__Host-hsd_staff` identity with Max-Age=0 and the same host/path attributes.

Under valid source/control/framing, absent-cookie logout may return generic204
and clear only the local cookie, revoking no server session. An authentic,
unexpired same-kind token with complete authoritative lookup to a known terminal
or absent session may do the same harmless no-op. A prior/retired token resolving
to an eligible current successor, or eligible current cookie with missing/stale
CSRF, gets403 with no Set-Cookie or revocation. Expired, malformed, wrong-kind or
invalid-signature tokens also get403; decode-only data cannot authorize logout.
Required store/key/clock uncertainty gets503, never acknowledged server revocation.
No submitted selector can target another session. Deliberate logout clears the
private UI; uncertain response means logout pending, not cancelled consultation.
Late cookies/clears may force reauthentication but cannot revive server authority.

### Source, raw framing and response directions

All four require exactly one `X-HSD-Session-Control: 1`, a public non-simple
protocol marker, not secret identity proof. Missing/duplicate/other values deny.
Use same-origin HTTPS credentialed fetch, no-store, redirect error; no CORS,
JSONP, HTML or alternative Bearer/body/query credential. Present Origin must
exactly match configured trusted scheme/host/port; hostile/null/malformed denies.
Only when absent may a parsed same-origin Referer establish source. For GET only,
both absent retain current cookie + custom header + SOP/no-CORS guards. POST with
both absent denies. Available Fetch Metadata must be same-origin; its absence
removes no other guard. Eligible renewal/logout require one current `X-HSD-CSRF`.
The harmless absent/terminal logout no-op exception cannot act on an eligible
session. Pre-login/OIDC callbacks stay outside this profile.

Accept exactly one unquoted staff JWT cookie, at most2048 ASCII bytes; reject
percent/whitespace/padding/ambiguous duplicates without selecting the last value.
Request target is at most256 bytes, aggregate decoded headers16384 including
Cookie8192, at most64 fields and receive at most5 seconds. GET has no body/type/
encoding/Transfer-Encoding; optional Content-Length is unambiguous zero. POST
is application/json, with no parameter or one charset=utf-8, identity JSON at
most64 bytes, nesting at most1, exactly empty object; no encoding/Transfer-Encoding/
trailers. Trusted ingress rejects/closes ambiguous framing before collecting a
body or permitting divergent parsers. Raw names/integers/duplicates require
checks before lossy parsing; the schema cannot prove them.

Body-bearing200/errors are strict UTF-8 JSON, no BOM/content encoding, at most1024
emitted bytes, fully serialized before headers. `204` has zero body, no Content-Type
or Content-Length and no JSON instance. No-store/nosniff apply to all complete
route-owned responses; no validator/304/redirect/HTML. Only successful renewal/
logout may Set-Cookie. Missing Accept permits JSON; effective media quality and
specificity control negotiation. Fixed closed code/recovery pairs are:

| HTTP | Code / recovery | Direction |
|---|---|---|
| 400 | invalid_request / correct_request | All four |
| 403 | request_denied / check_access | All four; no private reason/existence/source/proof echo |
| 409 | session_changed / check_session | Renewal prepared-output race only |
| 413 | request_too_large / correct_request | Safely framed POST body only |
| 415 | unsupported_media_type / correct_request | POST media only; GET's forbidden framing/type is400 |
| 429 | request_limited / wait | Applicable finite control counter/capacity policy |
| 503 | service_unavailable / check_session | Required authority/accounting unknown |
| 500 | internal_error / check_session | Fixed unexpected failure |

405 with Allow exact method,501/406/414/431 are object-independent bodyless
refusals before private lookup. HEAD gets405 with no hypothetical GET length.
An ingress/proxy failure is observation failure, not an authentication outcome.
Schema directions are `status_response`, `csrf_response`, `renewal_request`,
`logout_request`, `renewal_error`, `logout_error` and `private_claims`; root rejects.
No JSON null/object is used to simulate204. Status/CSRF accept only their own
success projection or listed read error; no read may expose the other secret.

### Private token claims

Propose exactly `iss`, `aud`, `sub`, `sid`, `jti`, `iat`, `nbf`, `exp`. Issuer is
case-sensitive `hengshi-design-staff-v1`; audience is the single string
`hengshi-design-staff-api-v1`, never an array/wildcard. Subject is the mapped
private Hengshi principal UUID; session and token IDs are independently issued
UUIDs. No provider tid/oid/email, name, role/grant, CSRF, purpose/content or
generation enters claims; current server records supply those bindings.

`iat = nbf = floor(trusted token issue UTC seconds)`;
`exp = floor(original session absolute deadline UTC seconds)`, unchanged on
renew/re-delivery. Canonical raw unsigned integers lie in`0..253402300799`.
Require equality/current issued-record bindings and `iat <= now < exp`, plus
precise original session idle/absolute and mandatory renewal checks. Rounddown
cannot extend access; do not issue/recover with no positive representable lifetime.
The schema does not compare dates or validate a signed JWT.

Require explicit `typ: hsd-staff+jwt` and a bounded trusted kid/algorithm mapping.
The selected algorithm/key family, exact closed header and signature bound remain
held for key custody and full graph qualification. Never derive allowed algorithms
or key URLs from an untrusted header, mix key families or accept none, jku/x5u/
jwk/x5c, extensions, decode-only verification or provider/visitor token confusion.
Compact JWS is at most2048 ASCII, three canonical unpadded base64url components;
strict UTF-8 JSON header at most128 decoded bytes and claims768. Reject duplicate
names, BOM, invalid scalars, unknown members and numeric aliases before lossy
dictionaries. Qualified library built-ins verify signatures/required claims;
extra canonical/current-authority checks do not replace crypto. Current token
records match exact issued claims/signing association; jti alone grants nothing.
Trusted verified principal/session UUID mappings may feed operator cursor MAC
bindings; raw browser claims before verified current mapping cannot.

### Finite control work and shared-network exclusion

Propose one shared32-control pool across all four routes, reserved before receive/
crypto/lookup and held through output/drain/known settlement. No hidden queue,
extra per-path pool, borrowed operator capacity or cancellation-based early release.
After eligibility require at most one admitted control per session on that same
permit. Candidate rates are10 starts per rolling60 seconds/session and30/principal,
across tabs, token rotations and workers; network counts120 attempted starts per
rolling60 seconds, including invalid/absent/retired traffic. These are unmeasured
Hengshi targets requiring adoption, not standard-prescribed or proven capacity.

Network excess/block alone NEVER refuses a verified eligible current/permitted
prior-recovery control within its own session/principal budgets. On the same
global permit, perform bounded framing/source/header checks and trusted crypto/
current authority verification even during network excess. Only then allocate
eligible identity-keyed counters and apply their own limits; still count each
start against the network. Network excess/backoff applies to invalid, absent,
retired/out-of-recovery, ineligible or known-terminal no-op requests, without
granting identity or an effect. Unknown required accounting/verification is503.
This avoids network-counter-only perpetual exclusion of unrelated eligible
accounts; it does not promise service under finite global or infrastructure
saturation. No new admission lane, credential or unbounded verification path.

Counter caps are1024 live session keys,256 principal keys and4096 network keys.
Never allocate identity state from unverified selectors, poison successor budgets
with stale tokens, evict/reset live state or release uncertain reservations.
Capacity refuses new keys; retire after the applicable window/block and known
settlement. Trusted network grouping/pseudonymization/proxy mapping and physical
counter memory remain held; caller Forwarded/Host is not network or identity truth.
Propose progressive429 Retry-After10,20,30 seconds capped30, on applicable
session/principal excess or network excess for requests not verified eligible.
Requests during a block cannot extend it. Reset a stage only after a full
no-excess window and known settlement; no server sleep, permanent account lock,
automatic retry or network block that skips bounded eligibility verification.
Crypto/current lookup/mutation/serialization target at most2 seconds after admitted
headers, delivery5 seconds and client observation10 seconds. Unknown cutover/
delivery means reconciliation, not a second successor or false logout result.

One bounded in-tab coordinator obtains status/current CSRF once per eligible
context. No polling except one visible scheduled status at authoritative renewal
due, then at most one renewal and confirming status. Unknown renewal permits at
most one same-context recovery with retained CSRF and one status check, then
deliberate reauthentication. No catch-up/429 auto-retry, business resend or
activity manufactured by sleep/visibility/network restore/tab hints. Context loss
clears transient secrets/status/private UI and drops late replies. Cross-tab hints
and context/revisions cannot authorize work. Complete-process UI remains unqualified.

Before adoption, register catalogue and exact data/source/copy bindings; qualify
header/key/tenant/freshness/network/physical clock/guard/writer/limiter mechanisms,
actual HTTP/crypto/renewal/logout/races/abuse and accessible behavior under the
separately approved implementation phase. Test shared-network invalid traffic
while unrelated eligible sessions retain own budgets, as well as global saturation
and uncertain accounting. No schema/prose/hash result proves these behaviors.

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
