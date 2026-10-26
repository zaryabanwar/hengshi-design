# Security, privacy and data-flow contract

Status: DOING. Proposed detailed definition, 2026-10-04. Sources: constitution VI,
D-015–D-019/D-065, foundation SEC-001–SEC-010, DATA-001–DATA-010 and AI-001–AI-009.
No authentication configuration, database migration or application change.

## Review coverage

The [later independent review](reviews/current-definition-amendments-2026-10-04.md)
records bounded PASS for this proposal and its action/object authorization
amendment at the receipt's exact hashes. The reviewed
[contract bytes](../../../output/research/contract-review-reference-reconciliation-2026-10-04/SECURITY_PRIVACY_CONTRACT.pre-status.md)
are preserved. In that earlier slice, only review references were reconciled; identity,
authorization and privacy obligations were not changed. Exact mechanisms,
operational grants, legal policies, founder acceptance and runtime proof remain
pending; the privacy/security alias owners remain undecided.
The later browser-resource proposal below is outside those earlier review inputs.
Its separate [independent review](reviews/browser-resource-security-v1-2026-10-05.md)
records bounded PASS at the [preserved producer bytes](../../../output/research/browser-security-definition-2026-10-05/SECURITY_PRIVACY_CONTRACT.reviewed.md).
This later reference edit does not replace that identity. The verdict accepts
proposal coherence and scoped source evidence, not browser/build enforcement,
selected origins/configuration, security certification or Phase 1 acceptance.

## Authority and implementation gap

The accepted requirements govern; the old security feature's eight-character
password, optional cookies, deferred MFA/roles/CSRF and single-process limiter
are historical proposals. They cannot select launch behavior. Current prototype
evidence includes browser token storage in `apps/web/src/lib/api.ts:63` and
`apps/web/src/admin/RequireAdmin.tsx:8`, Bearer extraction in
`apps/api/app/auth/deps.py:9`, and cookie-independent token issuance in
`apps/api/app/auth/routes.py:29`. These are observed gaps, not new instructions
to change the protected application before Phase 1 acceptance.

The [data-classification matrix](data-classification.csv) identifies technical
boundaries and unmapped retention classes. It is not a legal basis, approved
privacy notice, provider agreement or permission to process real visitor data.
An unresolved field/class or provider policy holds the affected persistence,
transfer and public claim; other approved semantic content remains available.

## Staff identity and authorization

Entra staff identity maps to server-enforced author, reviewer, founder approver
and administrator roles. Missing, disabled or ambiguous membership denies access.
An author cannot independently review or approve their own material; administrator
access does not grant publication approval. Jobs recheck authorized intent and
candidate identity rather than trusting a browser role or arbitrary queue payload.
Exact tenant/group mapping, privileged activation and account owners remain gated.

### Proposed action and object authorization

The following matrix refines SEC-001/SEC-002, PUB-002/PUB-003 and
[SOF-01 operator invariants](../../phase-1-ux-architecture/FLOWS.md#sof-01--staff-operator-information-architecture-and-operations).
It records the accepted separation constraints and proposed enforcement obligations;
it does not assign people, Entra groups or new operational privileges. The four
staff roles are not an inheritance ladder. Founder approval, administration,
content work and private conversation/booking operations have separate authority.
Holding several roles never defeats a same-object separation restriction.

| Catalogue action | Required authority | Object/state conditions and mandatory denial |
|---|---|---|
| IF-STAFF-01 — create candidate | Author role and approved content scope | Bind the actual principal and exact candidate revision; no activation, self-review or self-approval permission follows from creation. Editing an existing candidate also requires its separately approved write scope. |
| IF-STAFF-02 — evidence/SEO review | Reviewer role with the relevant approved review scope | Bind the exact candidate/checksum and sources. Deny a contributor's review of their own material, stale snapshots and unresolved rights/claims holds. Administration or founder status alone does not supply specialist-review authority. |
| IF-STAFF-03 — founder approval | Founder-approver role and candidate approval scope | Require independent required reviews of the current exact snapshot and no unresolved hold. Deny same-material author approval, even when that principal also has founder/administrator roles. A previous approval is not permission for changed content. |
| IF-STAFF-04 — activation | Explicit publication-operation authority, after exact eligible approval | The mapping of this operational authority to approved principals/jobs remains held. No author/reviewer/administrator role automatically grants it. Require the publication contract's verified artifacts, generation guard and definitive/reconciled outcome. |
| IF-STAFF-05 — inspect artifacts | Explicit candidate/artifact read scope for the authorized staff task | Author, reviewer or approver access is limited to the approved object/purpose. Administrator status is not a universal draft/private diagnostic read grant. Inspection never changes readiness or approval. |
| IF-STAFF-06 — assignment | Explicit assignment/reassignment authority and approved work scope | Require current item revision, consent/purpose and eligible owner/backup. Deny self-assignment or administrator override unless a later approved policy specifically permits it; no identity or availability can be fabricated. |
| IF-STAFF-07 — booking reconciliation | Explicit booking-operations authority for that lineage | Require authoritative local/provider evidence and current operation state. Deny manual email verification, guessed provider confirmation or fabricated slots. Publication/content roles and an alert alone grant no booking authority. |
| IF-STAFF-08 — audit inspection | Explicit audit/privacy/security read authority and approved query scope | Return only approved redacted event fields for bounded queries. Deny payload/secret disclosure, audit edits/deletion and export without its separate applicable approval. Reading the audit is itself audited. |

Named content roles above implement the existing separation requirements. The
operational authorities are permission requirements, not newly selected Entra
roles or grants. Exact group bindings, object scopes, delegated powers, export
policy and owners remain held. An unmapped action is denied; it must not be
implemented as an administrator fallback. Privacy/security email ownership remains
undecided and cannot be inferred from these functional responsibilities.

Every protected decision requires current authenticated identity, an explicit
action grant, permitted object/purpose scope and the action's valid state/revision.
All conditions must hold. Missing/disabled/ambiguous identity or grants deny access;
a role label, opaque ID, frontend route, cookie or submitted owner never grants it.
Response projection follows the same scope, including list/search/count and error
responses: a denied direct read cannot be recovered through another endpoint or
an existence-revealing error. Exact HTTP/error mappings remain interface inputs.

Recheck these conditions at the authoritative mutation boundary, not only when
the screen opens or a job is queued. Concurrent candidate edits invalidate old
review/approval; reassignment, consent withdrawal, identity revocation or release
withdrawal cannot be ignored because an earlier browser/queue check passed.
Jobs act on scoped durable intent under their approved service identity; they do
not impersonate a founder or gain broader authority from a payload. Revocation
does not erase the historical record of who actually approved an earlier snapshot.

Negative conformance must exercise each protected API/job boundary with a valid
but wrong role, missing scope, another object, stale revision, revoked identity
and prohibited combined-role self-approval. Also test list/projection leakage and
a permission/state change between initial check and mutation. These are future
behavior tests against approved exact contracts; this matrix is not executable
authorization or a passing security result. Its logical amendment has the later
bounded review identified above; integrated acceptance remains pending and prior
receipts retain their own scopes.

Exactly two local emergency accounts remain dormant during normal operations.
Approved activation, bcrypt verification and local MFA are all required, with
activation/use alerts, post-use review and rotation. Each credential is randomly
generated with at least 24 characters and approved entropy. This does not invent
an emergency bypass of role separation, MFA or legal/publication holds. Generator,
MFA method, custody, recovery procedure and alert recipient need separate evidence.

Browser staff sessions use rotating JWTs in Secure, HttpOnly, SameSite cookies,
30-minute idle and eight-hour absolute limits, CSRF protection and idempotent
server logout/revocation. Token rotation/reuse detection, issuer/audience/key
validation and Entra session revocation need exact reviewed implementation
contracts; token presence or a frontend guard cannot establish authorization.
Do not retain browser staff tokens in localStorage in the production design.
Cookie names, SameSite mode, signing algorithm and CSRF mechanism are not selected
by this document. Production CORS trusts explicit approved origins only.

## Staff sign-in mediation proposal

Status: DOING. Engineering recommendation, 2026-10-06; founder acceptance pending.
The [separate review](reviews/staff-signin-boundary-v1-2026-10-06.md#correction-2-disposition--superseding-bounded-pass)
records bounded proposal-consistency PASS after correction 2 at the preserved
[contract](../../../output/research/staff-signin-boundary-2026-10-06/SECURITY_PRIVACY_CONTRACT.correction2.reviewed.md)
and [catalogue](../../../output/research/staff-signin-boundary-2026-10-06/INTERFACE_CATALOG.reviewed.md)
inputs. This later review-reference edit is outside those inspected bytes; exact
mechanisms, legal/graph/runtime evidence and integrated acceptance remain held.
This refines SEC-001/004/005 and the existing staff
identity boundary. It adds no visitor account, role, endpoint or third deployable.
Earlier receipts do not cover this section. The unchanged predecessor is
[preserved](../../../output/research/staff-signin-boundary-2026-10-06/SECURITY_PRIVACY_CONTRACT.before.md).

Recommend server-mediated Entra authorization-code sign-in with OIDC and PKCE
S256. The FastAPI identity boundary owns the exchange and validation; React
receives a protected Hengshi session, never provider credentials. Use a maintained
supported client and verifier proven in the complete stable compatibility graph;
do not hand-build OAuth or adopt a package/version from illustrative documentation.
The account/app registration and exact tenant/client/callback remain held.

### Admission and token separation

1. Start creates a bounded, expiring, single-use server transaction with independent
   random state, nonce and PKCE verifier. Bind it to the initiating browser using
   an approved protected correlation mechanism. State alone is insufficient.
   Return navigation resolves to an allowlisted local staff destination; neither
   state nor query parameters may select an arbitrary redirect or issuer.
2. The registered backend callback accepts only the bound current transaction,
   consumes its code once and verifies the provider result. Require approved
   issuer/tenant, intended audience, signature/key/algorithm, validity and nonce.
   Reject missing, expired, mixed-issuer or mismatched inputs; no permissive
   decode-only path, guessed key URL or fallback tenant is allowed.
3. Map validated tenant/object identity (`tid`, `oid`) to an explicitly permitted
   staff principal. Email, display name and username are not identity keys or
   grants. Missing or ambiguous mapping, guest eligibility or group-overage
   resolution cannot be treated as authorization; exact membership policy stays held.
4. Issue the existing rotating Hengshi staff JWT cookie only after successful
   identity admission and current principal eligibility. Replace any pre-login
   context; a caller-chosen session ID cannot survive sign-in. Token kinds have
   mutually exclusive verifier rules: an Entra ID token proves sign-in, and a
   Graph access token authorizes its intended resource; neither is a Hengshi
   API credential. A visitor process cookie cannot become staff authority.
5. Every protected HTTP/job/socket action still requires the action/object/purpose
   and current-state guards above. Token role labels never replace them. Keep
   provider tokens, PKCE verifier and signing secrets server-side. The authorization
   code may transit the browser only to the registered, bound backend callback;
   do not persist it in JavaScript-readable storage, expose it in React response
   bodies, generated HTML or general logs. Apply the callback URL/referrer/cache
   controls below to that transient transport. Carry
   the Hengshi session JWT only in its Secure/HttpOnly/SameSite cookie; exclude it
   from JavaScript-readable storage and response bodies exposed to React. Exclude
   all these secrets from generated HTML and general logs. Any permitted
   server cache keeps the applicable secret/private classification and approved
   retention; no durable provider-token cache is assumed.

Initial sign-in requests only the reviewed OIDC scopes needed for identity; the
proposed object mapping needs `profile` for `oid`. It does not request calendar,
mail, presence, broad directory privileges or offline access by default. Separate
Outlook/Teams capabilities require MA-006 and their own permission/retention proof.
Azure/AWS hosting deferral and free client access do not establish those capabilities.

### Session, callback and failure obligations

The callback is a protocol-specific boundary: its transaction correlation is
distinct from later state-changing API CSRF proof. The accepted staff cookie and
CSRF requirements remain. Choose callback method, correlation-cookie SameSite
behavior and host/path rules together; cross-site return must work without
weakening the normal API policy. No names or modes are frozen by this proposal.
Callback handling must immediately remove sensitive protocol parameters from
subsequent navigation, prevent cache/referrer leakage and redact ingress/access
logs as well as application diagnostics. Do not log provider error payloads raw.

Successful sign-in creates no publication or private-operation grant. Session
rotation cannot extend the eight-hour absolute lifetime, revive a revoked principal
or ignore the 30-minute idle boundary. Local logout/revocation is authoritative
for Hengshi access; a provider sign-out redirect alone is insufficient. A valid
old ID token does not prove current Entra membership or immediate provider
revocation: the actual revalidation/invalidation path, freshness bounds and
outage policy need acceptance and runtime evidence before implementation.
Uncertain exchange, callback replay or lost session response must not mint another
grant from client inference; require authoritative reconciliation or a fresh
explicit sign-in under the accepted recovery policy. Entra loss never activates
the dormant local emergency accounts automatically.

Future behavior evidence must exercise a permitted mapped staff control and
wrong tenant/audience/nonce/browser, swapped token kind, replayed callback,
missing/disabled/ambiguous membership, malicious return destination, concurrent
callbacks, late logout/revocation and expired sessions. Inspect actual browser,
callback/proxy logs and response/cache behavior using synthetic identities only.
These are required public-boundary oracles, not executed tests or security proof.
Exact wire schemas, transaction/cache/time/work limits, JWT algorithms/keys,
rotation/replay mechanics, Entra freshness, MFA policy, hosts, retention/legal
mappings, compatible client, approved staff screens and founder acceptance remain.

Research checked 2026-10-06 through Context7
`/websites/learn_microsoft_en-us_entra_identity-platform` and primary
[authorization-code guidance](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow),
[ID-token validation](https://learn.microsoft.com/en-us/entra/identity-platform/id-tokens),
[claim semantics](https://learn.microsoft.com/en-us/entra/identity-platform/id-token-claims-reference),
[OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) and
[JWT security BCP](https://www.rfc-editor.org/rfc/rfc8725.html).
The [source receipt](../../../output/research/staff-signin-boundary-2026-10-06/source-receipt.json)
records scope only. No real sign-in, token, client registration, Graph consent,
MFA/credential/provider configuration, application or database change was performed.

## Data and provider boundaries

Visitors have no launch accounts or uploads. Public chat is treated as untrusted
input. Non-consented chat is ephemeral and must not be written to durable
application stores, general logs, analytics or training datasets. Provider
telemetry and service retention must also satisfy the approved route policy;
"ephemeral in our process" does not prove provider-side non-retention.

Consent is purpose-specific and versioned. Refusal does not remove access to
published information or approved help/booking alternatives. Consented chat,
brief and lead records have the approved 90-day expiry rule, with no extension
through derived traces or an unapproved active-client exception. The retention
clock anchor and collection-specific consent/legal wording require approval;
resuming, copying or restoring data must not silently reset the expiry.

PII/confidential AI processing requires the approved Azure Europe route with
verified region, agreement and no-training controls. NVIDIA initially accepts
only public or demonstrably de-identified material after its entitlement gates.
Removing an email alone does not establish de-identification. Unknown/unmapped
classifications, secrets/credentials, controlled/classified defense content and
other explicitly prohibited policy categories deny provider transfer. Approved
PII/confidential processing remains limited to the verified Azure Europe route;
a provider outage never authorizes a less protected route. Prohibited content receives refusal,
without echoing or retaining the sensitive value in evidence or logs.

Availability requires an explicit staff setting with expiry; Teams presence can
only suppress a false available state. Presence loss/staleness gives an honest
offline Contact/Book route. Handoff sends only consented, purpose-permitted
context; the private staff identity is not a public manifest field.

## Expiry, deletion and restoration

Deletion is an orchestrated operation with an auditable, non-content-bearing
outcome, not a claim based on removal of one database row. Map application rows,
derived traces, replicas/caches, index copies and applicable external records.
Stop new collection/transfer for the affected operation while it is unresolved.
Content excluded from public knowledge must never reappear as AI evidence.

Only classes mapped by approved policy can be deleted or retained under that
policy. Booking/calendar, consent proof, audit, operational copies and deletion
tombstones need explicit duration, legal authority and provider behavior. An
unmapped class or unknown provider result keeps deletion pending; never claim
"everything deleted" or retain an identifying tombstone indefinitely by default.

Before restoring a backup to serving traffic, enforce approved expiry/deletion
decisions and verify absence across derived copies. Exact backup expiry and the
minimal restore-suppression mechanism need a reviewed legal/data mapping. Until
that exists, restoration cannot be claimed privacy-complete. General operational
logs contain neither conversation content nor tokens, email or raw sensitive URLs.

## Threat and failure obligations

| Boundary / threat | Required control and negative evidence |
|---|---|
| Browser / role forgery, cross-site write, stolen session | Server permission and CSRF checks; expired/revoked/replayed session denies; frontend removal does not elevate rights. |
| Staff content / script or unsafe URL | Typed input validation and contextual safe rendering; rich content has a reviewed allowlist. Blanket string stripping is not proof of injection safety. |
| Publication / stale approval, delayed cutover, forged asset | Exact snapshot approval and fenced publication contract; immutable checksum/path/graph validation before serving. |
| World / malformed chunk, stalled load or hostile asset path | Only release-listed assets, bounded resource work and valid collision readiness; no arbitrary URL fetch, unloaded-ground traversal or draft panel. |
| Chat / prompt injection and unsupported commitment | Approved versioned evidence only; source checks, refusal and human/booking route. Model output grants no tool, publication or booking authority. |
| Booking / forged verification, replay, uncertain provider write | No slot eligibility before verified email; durable idempotent intent and reconciliation; no confirmation without authoritative evidence. |
| Presence / stale state or spoofed online signal | Server-controlled explicit availability with expiry; unknown state remains offline. |
| Redis loss / limiter bypass and indefinite retention | Distributed account/network protection must fail according to an approved outage policy; no unprotected login or privacy extension by default. |
| Analytics / re-identification and content leakage | First-party cookieless aggregate reporting, approved small-cohort suppression; no movement trail, chat, email or stable visitor profile. |
| Restore / resurrection of expired or deleted data | Quarantined restore, enforced approved deletion/expiry and proof before serving; no reset retention clock. |

Independent review must verify these requirements against identity, publication,
booking, AI and QA contracts. Exact rate thresholds, outage controls, algorithms,
resource ceilings, audit retention and provider operations remain specification
inputs, not numbers invented here. CSP/WAF, transit/at-rest encryption, least
privilege, redaction, alerts and secret scanning remain SEC-007/SEC-008 obligations.

## Browser-resource and serialized-content proposal

PROPOSED 2026-10-05 under SEC-007/008 and the
[publication serving/injection boundary](PUBLICATION_CONTRACT.md#determinism-injection-and-serving-boundaries).
This is the controlling security proposal for browser resource admission, not a
deployed CSP, selected hosting origin or approved production configuration. The
complete stable toolchain, exact resource list and browser/device evidence remain
required. Authoring approval never makes text, URLs or serialized data trusted code.

### Immutable public HTML and script admission

Prefer a deterministic, hash-based public-page policy: serve the reviewed HTML
bytes unchanged, externalize application code, and authorize any unavoidable
framework-generated inline executable block by its exact final-byte hash. Build
identity, eligible release/artifact identity and the serving policy's reviewed
association must agree; changing generated code or inline bytes requires new
artifacts and policy evidence. CSP script hashes and artifact digests have different
scopes and encodings and cannot be interchanged. Same-origin executable endpoints
must serve only controlled code with correct MIME/nosniff handling; same origin
alone does not make arbitrary content executable or release-eligible.

A symbolic baseline for semantic documents is:

```text
default-src 'none'; base-uri 'none'; object-src 'none'; frame-ancestors 'none';
script-src 'self' {exact_inline_hash_sources}; script-src-attr 'none';
style-src 'self' {exact_style_element_hash_sources}; style-src-attr 'none';
connect-src 'self' {approved_connection_sources}; worker-src 'none';
img-src 'self'; font-src 'self'; media-src 'self'; manifest-src 'self';
frame-src 'none'; form-action 'self'
```

This template is deliberately not deployable: omit empty hash/source slots and
resolve exact reviewed origins/resources before adoption. No wildcard, blanket
`https:`, executable `data:`/`blob:`, JavaScript `unsafe-inline` or `unsafe-eval`
is proposed. CSP does not replace object authorization, CSRF, serving eligibility,
output encoding, resource integrity, consent or withdrawal controls. Deliver the
enforced policy in the HTTP response, including `frame-ancestors`; report-only
evaluation is observation, not enforcement or permission to launch unprotected.

Do not set one static nonce for a cached publication. Vite's nonce placeholder is
intended for a fresh value per response; substituting it changes HTML bytes. A
dynamic nonce document would require a separately approved representation/digest/
caching contract, not a silent rewrite of an immutable artifact. React's renderer
can emit inline bootstrap/reveal code; inventory actual final output rather than
assuming external bootstrap URLs eliminate every inline block. Neither Vite's
development behavior nor a newer main-branch example proves the candidate build.

### Typed content, data blocks and styles

Prefer typed text/heading/list/link/media blocks rendered through reviewed React
components over author-supplied HTML. Treat any later rich-HTML capability as a
separate reviewed allowlist/sanitizer contract; do not copy arbitrary content into
`dangerouslySetInnerHTML`. Validate URLs by field purpose and parsed scheme/origin;
authoring or AI output cannot create script, worker, module or decoder URLs.

Serialization must keep public projections separate from private job/approval,
staff/process, consent and provider fields. `JSON.stringify` alone does not make
untrusted data safe inside HTML. Use a reviewed HTML-script-context serializer that
prevents literal closing-script and comment/parser transitions while preserving
the decoded value; external JSON still needs the closed public projection and
correct JSON MIME. Test data blocks and JSON-LD through the actual HTML parser and
hydration path, including quotes, angle brackets, ampersands, Unicode separators
and closing-tag payloads. Do not treat a CSP hash as validation of serialized data.

Prefer generated external CSS and reviewed classes. A nonce on a style element
does not authorize arbitrary style attributes. Inventory React/World overlays,
canvas sizing and animation writes; verify the actual APIs on supported browsers.
If the baseline blocks required behavior, reconcile the mechanism or obtain a
bounded reviewed style-policy adjustment; do not quietly add blanket allowances.
Vite may inline small image/font assets: prefer disabling that build behavior over
implicitly admitting unrestricted data URLs; prove the resulting production output.

### World decoders, worker policies and resource origins

The observed Three candidate's loaders can create Blob-backed workers and fetch
WASM/wrapper assets. Their tagged source is illustrative evidence, not exact patch
archive or source-to-binary proof. A restrictive policy cannot simply be declared
compatible with those paths. Prefer controlled same-origin, release-associated
decoder/transcoder artifacts, verified bytes and bounded worker ownership from the
[loading contract](../../phase-1-3d/CAMPUS_ASSET_BUILD_SPEC.md#loading-and-residency-contract).
No vendor/CDN default path, public URL from a visitor or arbitrary mirror is approved.

If the selected stable loader needs Blob workers, review the bounded `worker-src`
permission and worker code construction separately; this grants no Blob script
permission to the document. If WASM is required, review the narrower
`wasm-unsafe-eval` capability instead of JavaScript `unsafe-eval`, including its
effective policy inside the worker. Ordinary URL workers have their own response
policy; local-scheme inheritance also needs actual browser verification. No worker
or WASM permission is selected by this paragraph, and it does not enable WebGPU.

A client-side route change cannot replace the document's HTTP policy. If World
entry stays within the same document, its reviewed policy must accommodate the
approved World runtime from initial load while code/assets/audio remain gated by
entry and consent. Otherwise a separate document transition needs approved journey
and identity continuity. Do not assume policies can be relaxed on a React toggle.
Policy or decoder denial preserves semantic Quick Access and safe stationary/
exit recovery; it never admits unready terrain or relaxes protection automatically.

Resolve finite production connection, media/font/asset and worker origins when
the deployment/resource plan resumes. Browser grants do not select Azure/AWS or
permit direct private-provider calls. Treat a required cross-origin response,
redirect, import, CORS/MIME or integrity failure as a release/build constraint.
Policy reports are potentially identifying: do not collect script samples, private
URLs/query strings, raw content or secrets; report destination, minimization,
retention and access need the existing approved diagnostic/privacy mapping.

### Required evidence and primary research

After authorized implementation, test actual generated HTML and response headers,
allowlisted scripts/styles and blocked injection/eval/URL paths; hash mismatch,
cached/wrong-release policy, JSON parser/round-trip/private-field exclusion and
hydration parity; production module/preload/lazy-import behavior; worker start,
worker policy, WASM/decoder fetching, bounded disposal and failure recovery.
Repeat against the approved exact browser matrix and named devices. No such build,
browser or security tests have run for this proposal; documentation validation
cannot certify these controls. Exact style needs, resource origins, complete
toolchain and integrated/specialist/founder acceptance remain held.

Research checked 2026-10-05 through Context7 `/websites/react_dev_reference`,
`/vitejs/vite` and `/websites/threejs`, and primary
[React rendering](https://react.dev/reference/react-dom/server/renderToPipeableStream),
[Vite CSP guidance](https://vite.dev/guide/features.html#content-security-policy-csp),
[browser-vendor CSP guidance](https://developer.chrome.com/docs/privacy-security/csp),
[HTML script parsing](https://html.spec.whatwg.org/multipage/scripting.html#restrictions-for-contents-of-script-elements)
and [Three KTX2 loader documentation](https://threejs.org/docs/pages/KTX2Loader.html).
[CSP3](https://www.w3.org/TR/CSP3/) is currently a W3C Working Draft, not a final
Recommendation or blanket stable/interoperability proof for every keyword.
The proposal requires evidence for the particular features on supported stable
browsers; it adopts no draft-only/experimental browser requirement. Registry and
tagged-loader observations are retained in the
[source receipt](../../../output/research/browser-security-definition-2026-10-05/source-receipt.json).
No dependency/runtime, hosting, application or production asset was changed.

## Acceptance limits

Required tests include cross-role denial, self-approval denial, CSRF, session
rotation/expiry/logout, dormant-account/MFA controls, provider denial for unknown,
unmapped and prohibited classes and refusal of PII/confidential traffic on an
unapproved route, while permitting it only on its approved verified Azure route,
prompt injection, non-consented persistence absence, expiry/deletion and restore.
Use synthetic identifiers and payloads; never include real credentials in proof.
Passing definition checks is not a security certification or legal sign-off.
MA-002/MA-005/MA-006/MA-007/MA-011 and complete Phase 1 acceptance remain applicable.


## Staff session activity and consultation fencing proposal — 2026-10-06

Status: DOING. Definition only; no session mechanism, transport, renewal endpoint,
permission, provider configuration or application is created. This extends the
staff mediation proposal and [IF-STAFF-15 participant protocol](HANDOFF_LIFECYCLE.md#staff-channel-initialization-and-control-proposal--2026-10-06).
Prior reviewed bytes are preserved. D-018 and FSC-04's accepted 30-minute idle and
eight-hour absolute session bounds are retained, not reopened as numeric choices.

### Qualifying staff activity and original expiry

The server associates a staff channel with the actual Hengshi principal, session,
current token/session generation and selected conversation/handoff/ownership.
These are internal bindings, not additional client claims or bearer fields.
Resolve approved issuer/audience/signature/token-kind validity and current session
revocation before using that binding. Entra identity, a JWT signature or previous
successful upgrade cannot replace current admission and purpose/assignment checks.

Propose refreshing the staff idle timestamp only on the first guarded admission
of an explicitly permitted staff business command, under that command's current
action/object/purpose authority and single-operation identity. For consultation
this includes admitted accept, decline, end and staff text commands. An admitted
command may still be pending; idle activity certifies neither committed business
success nor delivery. Its replay/reconciliation cannot refresh the timestamp
again. Other staff commands need their own explicit mapping before being treated
as qualifying activity; no broad 'any authenticated request' rule is selected.

HTTP reads, queue/status polling, CSRF/token reads, socket initialization/readiness,
ping/pong, receipts, output, replay, reconnect, failed/denied commands, retries and
client mouse/keyboard/touch events do not refresh this proposed idle clock.
A request-arrival timestamp or caller 'user active' flag proves no deliberate
business activity. A distinct More-time or renewal action is not invented here.
Reading staff still need the accessible warning/reauthentication design below;
background machinery must not keep an abandoned workstation authorized.

For the original session, absolute expiry is issued-session time plus eight hours;
idle expiry is its last qualifying admission plus 30 minutes, initially anchored
at sign-in. The earlier boundary wins. At or beyond either boundary, reject new
private admission/output even if a token's exp claim extends farther. Rotation,
reconnection, a new channel, another tab, callback replay or late result cannot
reset the original absolute anchor. Concurrent commands cannot move idle backward
or touch it after expiry/revocation. Require a shared authoritative clock/state
and atomic expiry/activity/revocation ordering; uncertainty cannot extend access.
No concrete clock, drift allowance or store/Redis mechanism is selected here.

### Ordered revocation, expiry and consultation truth

Before every protected HTTP effect, socket command, replay and private output
admission, validate the current session and command-specific authority together
with handoff/ownership, source, purpose and consent. Queueing under a previously
valid session is not permission to deliver after a newer revocation or reassignment.
Use a current session-to-channel/work binding and ordered authority generation,
not a stale in-process connection list or an unexpired self-contained JWT alone.
The actual authoritative store, shared fencing and propagation mechanism remain
reviewed implementation inputs; losing their evidence denies private work.

When logout/revocation/expiry is known, fence all dependent channels, unused send
tickets, replay and queued private output for that session. Stop new dependent
effects before closing transports. A safe minimal control is optional only if
its disclosure is still permitted; otherwise close without a private body/reason,
under the existing [close/cleanup profile](CHAT_EVENT_PROTOCOL.md#transport-close-and-recovery-proposal--2026-10-06).
A timer or close callback does not release uncertain reservations, settle a text
operation or prove that already admitted external work was cancelled. Expiry
checks on relevant admission are required even when a proactive timer/notification
is delayed. Known local logout is server invalidation, not only clearing a cookie
or redirecting to Microsoft. Provider sign-out alone is not Hengshi revocation.

Session loss changes staff access, not the visitor's consultation lifecycle.
It does not itself create ended, declined, reassigned, staff available/unavailable,
a new owner, deleted, visitor-delivered or booked outcomes. The visitor retains
only the latest permitted authoritative lifecycle state and honest connection
uncertainty. Existing availability evidence may independently expire or be fenced;
a logout cannot fabricate its public status. Actual ending, reassignment and
consent/deletion remain their own guarded operations and evidence.

### Accessible reauthentication and permitted recovery

Before a predictable user-affecting expiry, the eventual UI must provide the
accepted warning/response time, operable accessible sign-in and stable focus,
without private data or credential hints in a return URL. Explain 'staff access
expired' separately from 'consultation ended'. TPL-STAFF-AUTH and TPL-STAFF-QUEUE
retain their accepted complete-process TL-WARN-EXTEND criteria; this proposal does
not claim that a warning or new login alone proves their extension/preservation
requirements. Exact accessible continuation behavior remains an acceptance input.

A fresh deliberate sign-in establishes a separately validated Hengshi session;
it does not revive the expired credential or automatically recover a stream,
assignment, text ticket or unresolved command. Recheck the mapped principal,
current action/object/purpose, assignment and consent before inspecting a permitted
record or issuing fresh channel readiness. Same-person identity is insufficient
if ownership or purpose changed. Lost ephemeral material stays unavailable; no
unconsented durable copy, browser transcript cache or log reconstruction follows.
Permitted retained state may be recovered only under its approved legal class and
fresh access. A new session must reconcile old unsettled operations under current
disclosure authority before a new text command; it cannot resend old intent.

### Evidence and remaining mechanisms

Checked 2026-10-06 through Context7 /websites/fastapi_tiangolo and official
[FastAPI WebSockets](https://fastapi.tiangolo.com/advanced/websockets/): dependency
and disconnect hooks are framework boundaries, not continuing staff authority or
cross-worker cleanup proof. Its query-token and broadcast examples are not adopted.
[OWASP WebSocket guidance](https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html)
requires session-expiry/logout handling and action-level authorization for long-lived
channels. [OWASP session guidance](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#session-expiration)
distinguishes idle, absolute and token-renewal clocks. Those sources do not select
Hengshi's activity allowlist, finite allocation, grants or exact freshness mechanism.

Required later boundary cases: initial sign-in idle anchor; exact 30-minute/eight-hour
expiry; first admitted pending command versus its retry; polling/heartbeat/replay
storms; two-tab activity and expiry races; expiry or logout between enqueue and
output; delayed callbacks from an old channel/session; reassignment versus staff
reauthentication; lost authority store; and reconciliation without text redispatch.
Inspect controlled-clock API/socket/store behavior, suppressed private canaries and
accessible browser reading/reauthentication using synthetic identities only.
No ordinary prose test, schema fixture, connection flag or token decode proves these.

Cookie/CSRF names/issuance, signing keys/algorithms, token rotation/reuse handling,
Entra freshness/outage policy, exact activity mappings beyond consultation, shared
clock/store/fencing, source/legal retention, finite physical transport/work limits,
production screens, independent review and founder/integrated acceptance remain
held. No staff session is built and no launch readiness is asserted.

## Authenticated staff cookie and CSRF transport proposal — 2026-10-06

Status: DOING. Researched mechanism recommendation for FSC-04/FSC-05, not a
selected deployment, package, credential or executable API. Independent security
review and founder acceptance are required. This additive profile preserves the
earlier sign-in and activity/fencing proposals. Exact JWT signing/rotation,
pre-authentication transaction,
Entra freshness, emergency MFA and legal/store mechanisms remain separate inputs.

### Recommended browser boundary

Recommend one approved HTTPS origin for the staff browser and its API paths,
while retaining the two deployables and their existing authority boundaries.
This is an ingress/origin recommendation, not an Azure/AWS, host, region or proxy
selection. If later deployment requires distinct origins, re-review cookie,
CORS/CSRF, callback and CSP behavior together; do not silently widen this profile.
The public semantic site, World and staff surface remain separate responsibilities.

| Proposed transport | Recommendation and limits |
|---|---|
| Staff credential cookie | Name `__Host-hsd_staff`; explicit `Secure; HttpOnly; SameSite=Lax; Path=/`, with no `Domain` and no `Partitioned` attribute. Value is only the approved Hengshi staff JWT, not an Entra/Graph token or a visitor proof. |
| Cookie lifetime | Derive any `Max-Age`/`Expires` from the token's already-approved validity, capped by the session's earlier idle/absolute boundary at issuance. Cookie expiry cannot authorize or extend server access. Reading a token or refreshing transport cannot count as qualifying activity. |
| Browser-held CSRF proof | Header `X-HSD-CSRF`, containing an opaque server-generated, session-bound synchronizer token. This intentionally JavaScript-readable request proof is distinct from the HttpOnly authentication credential, provider tokens and private work tickets. |
| Browser credential policy | No JWT response body, localStorage/sessionStorage/IndexedDB credential, URL token or browser Bearer fallback. Approved jobs/service callers retain their own scoped identity; this cookie does not become their credential. |

These names/attributes are proposed v1 protocol identifiers, not active configuration.
Explicit Lax supports the proposed top-level GET OIDC return; it is not sufficient
CSRF protection. The independent, browser-bound single-use state/nonce/PKCE
transaction remains necessary. A callback using `form_post` would not satisfy
that Lax return assumption and requires a separately reconciled correlation
profile; it must not trigger a switch to `SameSite=None` on every staff cookie.
The normal business-request proof is not applied to an OIDC callback in place
of the callback's own protocol validation. Exact callback mode/correlation cookie
and transaction lifetime stay held under the sign-in proposal.

A signed JWT is not encrypted merely because it is signed or HttpOnly. Limit
its claims to the reviewed minimum principal/session/token identity, type,
issuer/audience and validity requirements; keep roles, membership, grants,
conversation content, email, provider tokens and signing keys out of this
proposal's browser credential. Verify token kind/issuer/audience/algorithm/key
and current server session independently. No algorithm, claims schema, key
custody or rotation grace/reuse rule is selected here.

### Synchronizer proof and authority

Recommend a cryptographically random 32-byte token, encoded as canonical,
unpadded base64url: exactly 43 ASCII characters, no whitespace, padding or
alternative encoding. It carries no principal, session ID, claims or business
payload. Keep its canonical secret value and current CSRF generation in the authoritative
protected session context;
issuance, retrieval, retention, at-rest protection and finite physical accounting
must follow the approved session-store profile, not an unbounded in-process map.

The same login-session proof can serve permitted requests across tabs. Bind it
to the current session and its CSRF generation, never a static user/email or
browser-supplied identifier. A short JWT rotation within that same eligible
session does not reset the idle/absolute clocks or require a new CSRF generation.
Fresh sign-in, session replacement, logout/revocation or explicit invalidation
of the CSRF generation invalidates the old proof. An old proof cannot be admitted
under a fresh session; rotating it cannot revive expired access or unsettled work.

Issue/retrieve the proof through the reviewed session-initialization/read boundary
only after current identity/session admission. Return it in a minimal private
response with `Cache-Control: no-store`, no shared cache, no analytics/body logs
and no URL/referrer transport. Keep it in transient page memory. A legitimate
reload or new tab may retrieve the same current proof; retrieval is not idle
activity or a role/object grant. Recheck current authority before releasing that
private response. Exact endpoint, response schema, cache store and accounting
remain held; this profile invents no route or permission.

Before any authenticated browser business mutation, require all of:

1. The exact current staff credential kind and current eligible server session.
2. A permitted source origin, compared as parsed scheme/host/port against the
   configured approved origin, never substring matching or client-controlled
   Host/Forwarded headers. Use Origin when present; if absent, a parsed Referer
   may establish that exact origin. Null, malformed, untrusted or missing both
   denies this profile. A trusted proxy must overwrite untrusted forwarded input.
3. Exactly one bounded canonical `X-HSD-CSRF` value, matched in constant time to
   this session's current proof. Missing, duplicate, cross-session, stale or
   incorrectly encoded values deny before an effect; never take a token from
   a query, cookie or unexpected JSON field as fallback.
4. The existing action/object/purpose/revision, consent/assignment and ordered
   mutation/work guards. A CSRF proof permits none of those authorities itself.

Require the existing closed private JSON intake for these API commands. Reject
simple form/text content types at those JSON-only boundaries; a future native
form requires its own equivalent reviewed proof/body contract, not automatic
acceptance. Safe reads perform no business mutation. Fetch Metadata, when
available, is additional defense; `same-site` alone cannot trust a sibling
subdomain, and missing Fetch Metadata cannot remove the origin/proof guards.
CORS never substitutes for any guard; disallow wildcard/reflective credentialed
origins and do not grant permissions merely because a preflight succeeds.

This is not a one-use business-operation ticket. Reusing the valid per-session
CSRF proof does not reauthorize retries or redispatch unknown work: existing
idempotency, token/work generations, current authority and reconciliation still
control. HTTP header/parser limits, rejection response taxonomy and actual proxy
enforcement remain covered by the separate raw-admission/interface definitions.

### Logout, recovery and unresolved boundaries

Logout of an eligible session uses the same source/proof guards, invalidates the
authoritative session and its CSRF generation, fences HTTP/jobs/socket output and
expires the exact cookie name/path/domain identity. Clearing a browser cookie
alone is not logout. A repeated same-origin logout after that session is invalid
may return a generic logged-out result and expire its cookie without reading
private data or changing another session; it must not treat a missing/stale proof
as authority to revoke any currently eligible different session.

Late Set-Cookie or private responses cannot make an old session current after
revocation/replacement. The server rejects their obsolete generation even if the
browser retained stale bytes. Concurrent response ordering, multi-tab refresh,
lost cookie responses and JWT reuse/grace behavior require the still-held
rotation/reconciliation design and actual tests; no perfect browser delivery or
automatic preservation is claimed.

Pre-login Entra start, callback, controlled local emergency activation/sign-in and
credential recovery need their own bounded pre-authentication correlation/CSRF,
MFA and abuse/resource profiles. They cannot bypass this authenticated profile
or accept a staff synchronizer proof before a staff session exists. Session
expiry still follows the separate activity/fencing profile; accessible warning,
extension/reauthentication and permitted-state preservation remain held.
This recommendation does not resolve the visitor's two-hour timing conflict.

### Research and future behavior evidence

Checked 2026-10-06 through Context7 `/websites/fastapi_tiangolo` and
`/kludex/starlette`. [FastAPI cookie handling](https://fastapi.tiangolo.com/advanced/response-cookies/)
supplies transport primitives; extraction/set-cookie helpers do not themselves
validate JWTs, provide current session revocation or enforce CSRF. The
[Starlette middleware source](https://github.com/kludex/starlette/blob/main/docs/middleware.md)
describes readable signed cookie sessions and lists third-party CSRF middleware.
Do not place provider secrets in its readable cookie session or infer that a
listed double-submit implementation meets this synchronizer recommendation.
No middleware/client package or exact release is selected.

The recommendation applies the
[OWASP CSRF guidance](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
on stateful session-bound proof, exact-origin checks and defense in depth;
[MDN cookie semantics](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie)
on host-prefix restrictions, explicit Lax and browser expiry limits; and
[RFC 8725](https://www.rfc-editor.org/rfc/rfc8725.html)
on token-kind separation and mutually exclusive validation. Proposed names,
encoding, origin topology and lifecycle bindings above are Hengshi engineering
recommendations, not claims that these sources select our protocol or deployment.

Future public-boundary cases must cover valid control plus wrong-origin/sibling
subdomain, null/missing origin and valid Referer fallback, duplicate header,
missing/cross-session/stale proof, simple content type, wrong token kind, absent
current grant, concurrent revocation, replay/unknown operation, reload/multiple
tabs, exact cookie deletion and late response. Exercise the actual browser,
ASGI ingress, shared session store and mutation boundary using synthetic identities.
Definition/integrity checks, example code and this research are not executed
CSRF/session, compatibility, accessibility or security proof.
