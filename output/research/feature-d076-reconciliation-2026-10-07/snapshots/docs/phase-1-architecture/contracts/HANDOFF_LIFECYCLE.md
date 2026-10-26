# Governed human consultation lifecycle — v1 proposal

Status: DOING. Prepared 2026-10-05. Definition only; no handler, grant, record,
account, adapter or production screen is created. Integrated Phase 1 acceptance
and the exact implementation contracts remain required.

The 2026-10-07 D-076 timing reconciliation at the end of this document is
outside earlier frozen review inputs. Its founder-selected inactivity policy
is recorded; the revised control/security/accessibility mechanism remains
DOING pending fresh independent review. Earlier PASS receipts cover only
their preserved inputs, not this amendment.

## Authority and purpose

This refines FR-009–FR-011/FR-016 and DATA-004–DATA-006/DATA-010 in the
[accepted foundation](../../phase-1-foundation/01-product-requirements.md),
[AF-02 and SOF-01](../../phase-1-ux-architecture/FLOWS.md), the
[logical data contract](DATA_CONTRACT.md),
[action/object authorization](SECURITY_PRIVACY_CONTRACT.md#proposed-action-and-object-authorization),
and [availability decision guard](AVAILABILITY_CONSISTENCY.md).
The existing [interface catalogue](INTERFACE_CATALOG.md) owns proposed routes:
IF-CHAT-04 requests help; IF-STAFF-10/11 inspect; IF-STAFF-12/13 accept or decline;
IF-STAFF-06 assigns; IF-STAFF-14 ends; IF-CHAT-03/IF-STAFF-15 carry separately
authorized visitor/staff events. No additional route or visitor account follows.

The visitor sees approved department information, chooses human help, reviews
what would be shared and consents where required. They see a waiting request until
an eligible authorized person actually accepts it. Text opens in the Hengshi
console; a Teams alert never constitutes acceptance. Book/Contact remains usable.
Separate opt-in and applicable accessible alternatives govern later voice/video.

Named owners/backups, assignment powers, legal notices/purposes and data-class
retention remain MA-002/MA-003/MA-006 inputs. This proposal defines safe transition
obligations without supplying those choices or authorizing real visitor data.

## Keep independent facts independent

| Fact | Meaning | Prohibited inference |
|---|---|---|
| Public live offer | Current explicit availability plus valid eligibility and required fresh signals | Reserved person, guaranteed attendance or accepted request. |
| Durable request | One authorized, consented request and its recorded outcome | Alert delivered, human response or active media. |
| Assignment | One current authorized owner for the permitted object/purpose | Availability declaration, content-role inheritance or unrestricted transcript access. |
| Human acceptance | Eligible assigned operator accepted the current request | A first reply, visitor delivery acknowledgement or media consent. |
| Text delivery | The event reached its specifically defined application boundary | Human read, response SLA or booking confirmation. |
| Alert attempt | Notification intent and observed delivery outcome | Conversation truth, calendar success or permission to copy more context. |

`alert_failed` is an alert condition beside the request lifecycle; it cannot
replace or roll back `queued`, `accepted` or `text_active`. `request_pending`
describes an unresolved request operation, not a second request. A stale public
indicator may lead to honest `staff_unavailable`; it cannot authorize acceptance.

## Lifecycle and guarded transitions

The following labels retain AF-02's vocabulary. The table defines logical
meaning, not a frozen wire enum, timeout, routing algorithm or database schema.
The server guards the current conversation, handoff, consent and assignment
identities/revisions together. Expected versions alone are insufficient: current
identity/action/object authority and permitted transition must also hold.

| Transition | Required evidence | Failure and recovery |
|---|---|---|
| Visitor chooses help → `requested` / unresolved `request_pending` | Own-process proof; eligible department/release context; current consent for the specific shared projection and its storage/transfer; valid request identity | Refused consent preserves ephemeral help/browsing/Book. Unknown admission reconciles the same operation; no second durable request. |
| `requested` → `queued` | Durable request admitted under its approved data policy; current eligibility and approved queue scope; independently recoverable alert intent | Queue/eligibility failure is visible as pending or `staff_unavailable` as authoritative evidence permits. Alert failure alone does not remove the request. |
| `queued` → `accepted` | Current consent, process validity, eligible available operator, explicit acceptance permission, approved assignment and current revision; one guarded owner/outcome | Concurrent or stale accept loses without a second owner. Unknown commit reconciles before retry or routing. Assignment policy is held; queue visibility cannot self-assign. |
| `accepted` → `text_active` | Known acceptance and current scoped text authorization for each participant; the application can establish the governed text session | Disconnect or channel failure reports accepted/not connected truthfully; no fabricated first reply. Resume only the same still-valid process and assignment. |
| Eligible queued request → `declined` | Authorized assigned operator, current revision and later-approved bounded reason/recovery policy | Pending decline preserves last known truth. No automatic reassignment, deletion, fresh availability or visitor identity follows. |
| `text_active` → `ended` | Authorized active operator, guarded current conversation/assignment and known committed ending | Unknown outcome remains ending/pending in the UI until reconciled. `ended` stops new text delivery but does not prove deletion or cancellation of booking. |
| Eligible process → `expired` | Expiry under its approved class-specific policy and authoritative clock | A disconnect, empty queue, alert failure or Redis loss is not expiry. Required expiry/notice/resume limits remain held. |

`accepted` and `text_active` may be recorded together only if the later contract
proves both obligations; a transport handshake alone proves neither. Terminal
requests are not reopened by a retry, restored alert or returning staff member.
Whether another request may be created afterward requires explicit visitor intent
and approved lineage/retention rules; automatic replacement is not selected here.

## One owner, one request outcome

Each repeated mutation binds its operation identity to the same principal/process,
target, action and immutable intent. Same identity with changed intent conflicts.
A matching known outcome is historical evidence, not permission to renew consent,
expiry, availability or a current assignment. Reads and retries recheck current
disclosure authority before returning that outcome.

Creation needs a guarded current handoff binding for the permitted conversation
and purpose. Simultaneous submissions using different identities must not produce
two simultaneously routable requests for that binding. Acceptance and reassignment
need one durable current ownership binding, not independent per-operator locks.
Current binding uniqueness, lifecycle generation, operation history and outcome
must be enforced at the authoritative transaction boundary. Their physical
constraints and terminal-history retention are still held.

The accept/decline/end/assignment operation and its outcome must agree atomically
in PostgreSQL. Alert dispatch/fan-out is separate approved recoverable work. A
timeout, worker crash, socket close or lost reply cannot establish rollback;
unknown acceptance must reconcile before another operator receives ownership.
If an older operation might still commit, a newer transition must order, fence or
resolve it; a timer or lease expiry alone is no proof it cannot change the state.

Proposed implementation direction: serialize transitions on a shared durable
aggregate guard and enforce unique current bindings, with consistent lock order
and guarded revisions. A successful row lock is not a complete consistency proof:
it protects selected existing rows, not absent-binding inserts, Redis, Entra or
Teams state. The acceptance decision also needs the availability protocol's
current-authority guard. Exact cross-authority admission/revocation guarantees,
constraints and isolation choice require later reviewed implementation evidence.
Do not hold a database transaction open for a person or provider response.

## Assignment changes, off and revocation

Availability off or suppressive presence prevents new positive routing/acceptance
according to its decision guard. It does not silently end an already accepted
conversation, delete a request or cancel a booking. Continuing an active session
still requires current identity, assignment, consent and approved session policy.
Staff unavailable is not permission to invent an owner or promise a callback.

Reassignment requires the separate IF-STAFF-06 authority, eligible approved target
and current object revision. Self-assignment/administrator override stays denied
unless a later approved policy permits it. A change produces a new ownership
generation; the old operator's sockets, replay and queued deliveries cannot keep
the old generation's access. No automatic backup or inherited content-role grant.

Consent withdrawal, identity/scope revocation, request expiry and ending block
disallowed new collection/transfer at the authoritative decision boundary. Old
socket authentication, queue admission or previously valid assignment is not a
continuing grant. Delayed work must recheck the current permitted projection and
generation before delivery; suppression completion needs proof against relevant
in-flight work, not a best-effort disconnect. Already disclosed content cannot be
recalled by closing a socket; deletion follows its separate policy and evidence.
Unknown current authority fails closed for further private text. Exact revocation
signal freshness, ordering, drain/fencing and acknowledgement mechanisms remain
held; this proposal claims no instantaneous cross-system revocation.

Urgent public-source withdrawal invalidates that source as evidence without
inventing a private conversation/booking outcome. Stop new use of affected source
content and explain the change; retention and permitted private handling follow
their own policies. Switching stream, leaving the World or changing public release
does not create another handoff or silently erase valid private process truth.

## Text, reconnect and separate media consent

Visitor and staff protocols remain separate closed directional contracts. The
server derives actual sender and permitted object from current authority; a
client-supplied sender kind, owner, role, source or sequence cannot impersonate a
person or confer evidence approval. Treat text as untrusted data for safe rendering.
Staff queue/detail views expose only permitted minimal context, not contact lists,
unconsented transcripts or private payload through counts/errors/diagnostics.

Authorize the browser Origin, session/process and conversation scope at upgrade,
then authorize relevant messages and replay at their current application boundary.
An open WebSocket and transport ordering are not business authorization or durable
exactly-once delivery. Application message identity/sequence, duplicate outcomes,
bounded replay and resume expiry require their own approved directional schemas.
No cursor can widen assignment, recover lost non-consented content or renew expiry.

Disconnect leaves known durable process truth intact; reconnect offers only the
same authorized, valid state. Where ephemeral content was lost, say unavailable
or expired as the relevant policy permits, without reconstructing a hidden copy.
Slow clients require bounded queues/reassembly/work, truthful gap/recovery handling
and no silent dropping followed by a delivery/read claim. Numeric limits and
application acknowledgement meanings remain held before wire freeze.

No audio/video capture begins from text acceptance, ambience enablement, browser
permission already being present, or a staff request alone. Separate visitor
opt-in, approved media routing and applicable captions/transcripts/descriptions
are required. Decline, unsupported media and permission failure preserve text
and Book. This selects no media provider, recording or retention permission.

## Privacy and alerts

Show exactly the approved projection and purpose before sharing it. Handoff
consent cannot retroactively authorize persistence of an earlier ephemeral chat;
an approved subsequent sharing operation must identify which context is included.
Retention consent and transfer/media permissions are distinct decisions. If the
current notice or required data-class policy is unapproved, hold that durable
request/transfer and preserve browsing, ephemeral guidance and direct Book.

An outbox, retry payload, replay buffer, trace and operator console copy retain
the source data's restrictions. Use references and approved minimal metadata
where possible, but a linkable reference is still subject to its mapped policy.
Do not dump the transcript into Teams, general logs or analytics. Resolve context
only after current authority/purpose checks. Alert deduplication, reconciliation,
retry budget and closure depend on the chosen account/API's verified contract;
this document neither guarantees exactly-once external alerts nor activates them.

End, decline and receipt acknowledgement do not reset expiry or complete deletion.
The approved 90-day chat/brief/lead scope is not automatically handoff, assignment,
consent-proof, operation history, alert, audit or provider retention. Mapped expiry,
exceptions, deletion and restore behavior remain required before persistence.

## Evidence required before implementation and acceptance

Actual API/transaction/WebSocket tests must exercise approved requirements at
their public boundary: wrong process/object/role; queue unavailable versus empty;
simultaneous different request identities; accept versus accept/decline/reassign;
accept versus availability off/consent withdrawal; uncertain commit and late worker;
old-owner delivery/replay after reassignment; reconnect without hidden ephemeral
reconstruction; ending versus late messages; revoked-source use; alert failure
without lost request; and media denial without broken text/Book. Include actual
PostgreSQL constraints and fan-out/admission mechanisms; mocked permission or
provider success cannot prove these invariants.

Browser journeys must verify honest waiting/accepted/connected/ending states,
preserved process across stream/World changes, accessible status/error recovery,
separate media opt-in and equivalent Quick Access. Approved screen references,
physical-device/accessibility checks and specialist/founder acceptance remain.

Still held: exact schemas/status/error mapping, operation/history retention,
grants/owners/queue and decline/reassignment policy, availability/revocation guards,
expiry/replay/resource bounds, legal consent/projection/data-class mappings,
physical transaction/outbox/fan-out proof, Microsoft/media account capability,
compatible stable dependencies and production designs. This proposal is not
runtime validation, legal review or integrated Phase 1 acceptance.

## Primary technical evidence

Checked 2026-10-05. Context7 `/websites/postgresql_18` queried for explicit locking,
Read Committed predicate rechecks and whole-transaction retry. The resolver also
returned a development PostgreSQL 19 entry; it was not selected. Direct primary
documentation uses explicit version 18. These mechanism observations choose no
runtime, patch, isolation level, schema, installation or production graph.

- [PostgreSQL 18 explicit locking](https://www.postgresql.org/docs/18/explicit-locking.html):
  selected-row locks end with the transaction; deadlocks require handling. The
  shared guard/uniqueness recommendation above is a project design inference.
- [PostgreSQL 18 transaction isolation](https://www.postgresql.org/docs/18/transaction-iso.html):
  Read Committed can recheck an updated row's predicate; snapshot reads do not
  automatically enforce a multi-row invariant. Serialization failures require
  whole-transaction retry under the chosen isolation contract.
- [RFC 6455 §§10.1–10.5](https://www.rfc-editor.org/rfc/rfc6455.html#section-10):
  browser Origin checking, authentication and frame/reassembled-message limits
  are separate concerns. The project adds current object/purpose/replay guards;
  the transport standard alone does not specify the business lifecycle.

## Staff console text direction proposal — 2026-10-06

Status: DOING; independent review and integrated/founder acceptance pending.
The preceding lifecycle and its reviewed predecessor remain unchanged. This
refines only text on existing IF-STAFF-15, after separately authorized channel
initialization. It is not acceptance, assignment, ending, a new route or a role
grant. The [closed staff text schema](staff-chat-text.schema.json) registers
`client` and `server` explicitly; its module root rejects messages. Visitor
IF-CHAT-03 schemas are not accepted on the staff route, or vice versa. Shared
representation helpers do not merge the participants' credentials or streams.

### Current participant, ticket and immutable intent

Before upgrade and initialization, validate the current Hengshi staff session,
exact approved Origin, selected conversation, current granted text action,
accepted handoff and ownership generation, permitted purposes and projection.
Use the staff sign-in/security contract; visitor process proof cannot substitute
for staff authority. No private output, replay or text admission before successful
staff-specific initialization. Its CSRF/session binding, closed readiness/control
shapes and finite physical profile remain prerequisites; this schema does not
freeze a staff CSRF mechanism or make a missing initialization path usable.

An eligible initialized channel may receive unsequenced `staff_text_admission`:
current channel/stream, server-bound handoff and ownership generation, current
consent revision or explicit null, release identity, random UUIDv4 operation ID
and positive command revision. No raw principal, role, JWT or provider token.
The ticket is scoped internally to this conversation, principal and ownership
generation, with one current ticket across that participant's allowed channels.
Reconnecting or opening another tab cannot allocate an independent send slot.
Null describes an actually absent purpose map only; it supplies no consent to
share with staff. Missing required consent makes the ticket ineligible.

`staff_submit_text` carries that exact ticket, current channel/stream, expected
ownership and consent revisions, and a payload containing only plain `text`.
It cannot choose a sender, visitor, department, handoff, provider, release, role,
approval or event sequence. Resolve recipient and actual sender from current
authority. Revision equality is necessary but never sufficient. Atomically
recheck current identity, grant, conversation, assignment, permitted purpose and
ticket, reserve bounded work, then consume the ticket once. Reject whitespace-only
text, invalid scalar/UTF-8 input and excessive encoded bytes at actual ingress;
do not trim, truncate or rewrite admitted intent. Render permitted text as text.

Bind an admitted operation to original principal, conversation/handoff, ownership
generation, exact text and original purpose/release context. Current transport
fields are admission metadata, not immutable historical intent. Matching retries
reconcile that same operation without redispatch. Changed text/context conflicts;
an older unknown or forged pair cannot become a new send. Lost ticket/outcome
state fails unavailable; never rebuild it from logs or revive an old assignment.
Retain only bounded current/pending and latest terminal evidence under its mapped
data policy. No new durable history or consent follows from this proposal.

`staff_reconcile_text` carries only transport metadata, original ticket and
expected ownership generation. Recheck current disclosure authority; an old owner
does not gain historical private outcome access merely by knowing the operation.
Issue the next ticket only after guarded terminal settlement. Ending/reassignment,
staff-session revocation, consent changes and unknown authority fence dependent
tickets, queued output and late work without manufacturing a terminal outcome.

### Directional projections and truthful results

`staff_command_result` uses immutable event identity/sequence/release and a closed
payload with handoff, ownership generation and original ticket. `admitted` means
bounded work admitted; `pending` means unsettled and requires reconciliation.
`projected` means the authorized visitor-facing projection was admitted by the
coordinator, not received, rendered or read by the visitor. It does not promise
the still-queued bytes survive a later revocation. `refused` names only fixed
input/recipient categories and permits inspection of the conversation under
that read's own authorization; `unavailable` means outcome unknown and permits
reconciliation. No stronger success, deletion or booking claim follows.

Authorized visitor text reaches the staff channel as `visitor_text`, containing
only handoff/ownership, original visitor ticket and bounded plain text. The server
checks the current allowed shared projection; it cannot expose an unconsented
earlier transcript or unrelated private context. The visitor's existing `forwarded`
result refers to admission of this governed console projection, not human reading.
Authorized staff text reaches the visitor via the already defined `staff_text`.
Neither participant can submit these server-origin projections as a command.
Projection failure never routes private human text to AI, Teams or another owner.

Each participant's stream is separately bound to its authorized projection and
generation. Staff and visitor sequence numbers are not compared or copied across
streams. Eligible replay preserves exact immutable bytes and original ownership
generation; recheck current disclosure first. It cannot relabel an old owner's
event for a new owner, transfer history automatically, acknowledge unseen gaps or
resubmit text. Assignment changes do not reconstruct non-consented lost content.

### Finite profile, evidence and remaining boundaries

Reuse the visitor protocol's shared one-unsettled-text-operation-per-conversation
and eight-service-wide work pool; staff traffic does not create another pool or
double these ceilings. Scheduling fairness remains held. Proposed staff input is
1–4,000 Unicode scalar values and at most 8,192 encoded UTF-8 bytes for the whole
request; both bounds apply. Visitor projections retain the 2,000-scalar bound;
complete output events retain 16,384 bytes. Reuse aggregate queue/replay byte
ceilings and rate/scheduling ceilings from CHAT_EVENT_PROTOCOL for the combined
participants, not a new allowance per staff member/tab. These are unmeasured
proposals. Staff connection, initialization, decoded overhead, output/coordinator
cleanup and authority-revalidation limits need their own verified finite profile.

Required later actual-boundary cases: visitor credentials/variants at staff route;
wrong principal/assignment; two tabs consuming one ticket; changed-intent retry;
old-owner replay/reconciliation; consent or ending versus queued delivery; staff
logout/rotation versus late work; scalar/encoded-byte limits; finite shared pools;
and no provider dispatch or invented human-read/booking result. Schema fixtures
exercise representation/direction/closure only, not any of those runtime claims.
Handoff creation, accept/decline/end HTTP schemas, reason/routing/owner policy,
legal data-class mappings, staff initialization/control/close formats, measured
budgets, stable graph, production screens and independent/founder acceptance
remain required. The earlier review receipts do not cover this addition.

Primary evidence checked 2026-10-06: [RFC 6455 section 10](https://www.rfc-editor.org/rfc/rfc6455.html#section-10)
separates transport Origin/authentication concerns; participant/ticket guards above
are project design inferences. [JSON Schema object closure](https://json-schema.org/understanding-json-schema/reference/object#unevaluated-properties)
supports the composed closed event shape. Context7 `/python-jsonschema/jsonschema`
and its [validator documentation](https://python-jsonschema.readthedocs.io/en/stable/validate/)
support Draft 2020-12, offline registry use and explicit format assertion, not
current assignment, consent or delivery. No package installation, production
version selection, handler, account, Figma write or persistence is performed.

## Staff handoff HTTP request proposal — 2026-10-06

Status: DOING, unreviewed. This closes the proposed client request shapes for
existing IF-STAFF-12/13/14; it implements no route, grant, database operation or
staff action. The [directional request module](staff-handoff-request.schema.json)
rejects instances at its root. Callers must select the endpoint-specific
`accept_request`, `decline_request` or `end_request` definition. This addition is
outside earlier reviewed bytes and does not claim integrated acceptance.

### Bind a command to the existing authorized object

| Existing endpoint | Apply request | Independent admission obligation |
|---|---|---|
| IF-STAFF-12 acceptance | `phase: apply`, `intent: accept_text_handoff`, operation ID, expected binding and expected consent revision | Current authenticated permitted operator, assigned object, valid legal/purpose/consent and availability; eligible queued request; one accepted outcome. |
| IF-STAFF-13 decline | `phase: apply`, `intent: decline_text_handoff`, operation ID, expected binding and reason-catalogue reference | Current assigned operator with explicit decline permission, eligible request state and an approved applicable reason/recovery policy. No reassignment or transcript erasure. |
| IF-STAFF-14 ending | `phase: apply`, `intent: end_text_consultation`, operation ID and expected binding | Current explicit ending permission for the route's consultation, permitted lifecycle transition and authoritative ordering against in-flight text. No consent change, deletion, availability withdrawal or booking cancellation. |

The operation reference reuses the existing UUIDv4 representation. Expected
binding contains the handoff UUID, handoff revision and ownership generation,
using the shared positive exact-integer representation. The server first resolves
the protected route and current operator/object assignment; these client values
only express expectations against that binding. They cannot select an arbitrary
conversation, make a queue reader its owner, grant administrator override or
replace assignment authority. Intent is a route-matching discriminator, not a
permission. Never choose a privileged route from that client discriminator.

No client sender, operator ID, role, target assignment, transcript, token, clock,
provider result or declared success is accepted in these bodies. Authentication,
Origin/CSRF and private response controls remain governed by the security and
staff-session contracts. Shared raw JSON admission precedes schema validation;
field closure cannot recover duplicate keys or malformed bytes already discarded
by a parser. Whole-message/header/queue/work limits, HTTP status/error responses
and physical enforcement remain separate required contracts.

Acceptance's expected consent revision may be null only as an explicit report of
no effective map, never as a waiver or a consent decision. Actual admission must
still resolve the current legal/purpose and consent requirements; absent required
consent denies acceptance. New acceptance must atomically compare the expected
binding and consent revision with current authority before mutation. Decline/end
contain no consent edit or transfer authorization. Stopping an already-disallowed
transfer remains mandatory independently of whether an ending command is permitted
or committed; refusal of an ending request cannot revive the transfer.

### Decline reasons remain policy-bound references

`reason_reference` contains only `reason_key`, `catalogue_revision` and the exact
catalogue SHA-256 representation. It identifies the approved interpretation of the
reason, not free text. A matching string or hash cannot make that catalogue
approved or that reason applicable. No permitted taxonomy, default reason, owner,
escalation or visitor-facing reason copy is selected here. Unknown, retired or
unmapped references deny a new decline; its separately authorized recovery remains
honest. A staff-internal reason is not automatically a visitor disclosure.

The admitted meaning binds the authenticated actor, protected route/action,
original expected handoff/ownership, exact reason reference where applicable and
original permitted purpose. Reusing an operation ID with changed meaning conflicts.
Credential rotation changes transport authority, not that original meaning.
Accept cannot assign an operator or make a text socket ready. Decline/end cannot
reset retention or manufacture a deletion, booking or external-alert outcome.

### Recover uncertainty without a replacement effect

Each existing POST endpoint also proposes a closed `phase: reconcile` branch,
carrying only its fixed intent, original operation ID and original expected
binding. This adds no new route or grant. Reconciliation accepts no fresh reason,
consent revision, text or assignment. It must never dispatch the requested action,
including when operation evidence is missing. Unknown evidence is unavailable,
not an absent-operation finding or authority to create a replacement.

A known matching outcome is disclosed only after current identity and explicit
outcome-read/object/purpose authority checks. Reconciliation after a successful
transition need not falsely require the object's old pre-transition revision;
the operation's original expectations remain immutable, while current disclosure
and ownership are rechecked separately. Knowing the operation UUID or having been
the former owner grants no historical access. An ended text session does not itself
grant or erase permission to inspect its recorded outcome; that permission remains
an explicit, presently valid read policy. Policy expiry or restore must not forget
an admitted effect and reopen the same command for application.

An uncertain acceptance, decline or ending remains unsettled until authoritative
evidence resolves it. Another operation ID, client timeout, socket close or UI reset
must not bypass that uncertainty. Concurrent accept/decline/end/reassignment need
one ordered durable aggregate decision with current assignment/consent guards.
An ending result cannot assert completed suppression until relevant older work,
queued projections and replay are fenced or ordered under its accepted protocol.
Transport cleanup is a separate fact. This proposal creates no response format or
claim that any physical worker, socket or store has implemented those safeguards.

### Validation and remaining evidence

The request validator checks endpoint/phase separation, required fields, composed
and nested closure, operation/reference representations, revision boundaries and
the absence of mutable reconciliation payloads. Well-shaped null consent or a
synthetic reason remains shape-valid; neither is a valid grant or approved reason.
Required actual-boundary cases include wrong route/object/operator, stale bindings,
revoked consent during acceptance, concurrent transitions, changed-intent replay,
old-owner outcome inspection, timeout after commit, loss/restore of operation
evidence and ending versus late text/replay. No database, API or browser enforcement
is exercised by schema fixtures.

Visitor handoff creation/projection review, staff initialization/control formats,
response/HTTP and measured work profiles, exact authority/assignment and reason
policies, legal data-class mapping, stable graph, production screens and independent
and founder acceptance remain required. Earlier review receipts do not cover this
addition. No new retention, account, provider, Figma or application operation is
authorized by it.

Primary sources checked 2026-10-06: [HTTP retry semantics](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2)
do not make POST intrinsically repeatable; the guarded operation/reconciliation
design above is a project proposal. [JSON Schema composed closure](https://json-schema.org/understanding-json-schema/reference/object#unevaluated-properties)
supports `unevaluatedProperties: false` at each composed command. Context7
`/python-jsonschema/jsonschema` and [validator guidance](https://python-jsonschema.readthedocs.io/en/stable/validate/)
support the reused offline registry and explicit format checks. No dependency
installation, version selection, live permission or persistence follows.

## Staff handoff HTTP response proposal — 2026-10-06

Status: DOING, unreviewed. This scoped addition completes the proposed response
shapes for IF-STAFF-12/13/14, alongside the request proposal above. It does not
implement a route, grant, session, transition or transport. Earlier review
receipts cover their exact predecessor inputs only, not this addition.

[staff-handoff-response.schema.json](staff-handoff-response.schema.json) is a
closed Draft 2020-12 module whose root rejects instances. Consumers must select
`accept_response`, `decline_response` or `end_response` for the protected route.
A response has either a fixed error envelope or a matching operation ID, intent
and result. Errors cannot also contain an outcome. Unknown properties, unrelated
endpoint outcomes and client request bodies are rejected. Error bodies contain
only a fixed code and recovery label, without raw inputs, identity, credentials,
private existence, current ownership or exception detail.

| Endpoint outcome | Meaning and limits |
| --- | --- |
| `accepted` | The separately authorized human acceptance is known to have taken effect. This does not establish an active text connection, staff presence, human reply or media consent. |
| `declined` | The governed decline is known, with its originally approved reason reference. This private staff reference is not visitor-facing reason copy, reassignment authority or a deletion instruction. |
| `ended` | Text ending is known to be committed and the required ordered suppression/fencing outcome is established. It does not mean deletion, booking cancellation, staff availability off, media teardown or physical socket cleanup. |
| `pending` | This bounded operation is known to have been admitted but remains unsettled. The only recovery is reconciliation of the same operation; no applied binding or terminal result is included. |

### Correlation and historical outcomes

A terminal `applied_binding` records the immutable handoff/ownership snapshot at
that operation's effect. It uses the request binding's field representation,
with different meaning: it is not a fresh ownership grant or a statement of
current availability. The consuming boundary must correlate route, intent,
operation and original handoff/generation with the command it actually awaits.
A shape-valid UUID or revision alone proves none of these facts.

Current identity, object, assignment and purpose/disclosure guards still govern
whether any outcome may be read. Reauthentication or replay of a known outcome
does not renew consent, retention, text admission, ownership or a terminated
consultation. Preserve a known historical outcome as history; do not promote an
old acceptance to current staff access after reassignment. A delayed reply from
an earlier identity, handoff or generation cannot replace the current UI state.
The schema cannot enforce these contextual comparisons.

The original decline reason interpretation is retained with an admitted
operation. A later catalogue retirement must not silently relabel or rewrite
that history. `reason_unavailable` applies only to a decline, after applicable
current authorization, when a new application cannot use that reason. It is not
an accept/end error or evidence that an earlier decline failed. Any inspection
of IF-STAFF-10/11 remains a separately authorized read; an error or a historical
binding cannot confer that read grant.

### Ending, suppression and uncertainty

An `ended` result requires the actual coordinator's durable ending and the
relevant ordered fence against older admission, queued output and replay. The
HTTP/socket consumer must also reject obsolete frames or replies crossing that
fence; an HTTP response by itself cannot order a separate transport or renderer.
Bytes already disclosed cannot be recalled. Socket closing, physical cleanup,
data deletion and independent meeting/booking lifecycles retain their own
outcomes. Without the required ending/fence evidence, return an unsettled or
unresolved outcome rather than fabricate completion.

Use `pending` only when admission is positively known. Loss of evidence, a lost
reply, a restart or an unavailable operation store does not prove admission,
absence or failure: use a bounded `outcome_unresolved` or
`service_unavailable` response as applicable. Preserve the same operation for
reconciliation; do not dispatch again or create a new ID to escape uncertainty.
Even `correct_request` describes this request's shape, not permission to repeat
a possibly committed prior operation. Any eventual new intent follows the
existing reconciliation/conflict rules and fresh current authorization.

### Proposed HTTP association

This table associates response categories with transport status; actual raw
HTTP enforcement, exact staff authentication challenge/CSRF/session mechanisms
and measured lifetime/work profiles remain held. These statuses do not establish
business outcomes or the fate of an earlier request. In particular, a response
must not pretend that a generic transport error proves no prior effect.

| Status | Response category |
| --- | --- |
| 200 | Authorized known terminal outcome for the matched operation. |
| 202 | Positively known admitted, unsettled `pending` outcome. |
| 400 | `invalid_request`. |
| 403 | `request_denied`, without a private-object existence oracle. |
| 409 | `binding_outdated`, `operation_conflict`, or decline-only `reason_unavailable`. |
| 413 / 415 | `request_too_large` / `unsupported_media`. |
| 429 | `request_limited`; wait, then reconcile the same possibly admitted operation. |
| 503 | `outcome_unresolved` or `service_unavailable`; no redispatch follows. |
| 500 | Fixed `internal_error`; no private exception detail or inference of absence. |

The existing private browser JSON/no-store and complete-message admission
obligations continue to apply. No new byte cap, deadline, work reservation,
identity challenge, origin allow-list, reason taxonomy or ownership policy is
selected by this response addition. The fixed `request_denied` category does
not select a bearer fallback or replace the pending staff authentication profile.

### Validation and remaining work

The focused response fixtures exercise the real schema validator at its public
boundary: endpoint/direction separation, nested closure, fixed errors, pending
recovery, required bindings and exact-integer limits. They explicitly demonstrate
that a well-shaped wrong operation or synthetic reason can still pass: runtime
correlation, approval and effect are separate obligations. They are not API,
authorization, concurrency, consent, accessibility or delivery tests.

Actual-boundary verification must cover lost replies after commit, restart while
pending, wrong route/operation, obsolete ownership replies, revoked identity,
retired reason catalogues, duplicate-effect prevention, and end racing with
queued messages/replay. It must distinguish text ending from physical closure,
media, deletion and booking outcomes. Visitor handoff creation, staff
initialization/control, full raw HTTP/auth/work profiles, legal and owner
mappings, measured limits and independent/founder acceptance remain outstanding.

Primary sources checked 2026-10-06: [HTTP 202](https://www.rfc-editor.org/rfc/rfc9110.html#section-15.3.3)
means accepted for processing rather than completed; [HTTP 409](https://www.rfc-editor.org/rfc/rfc9110.html#section-15.5.10)
describes conflict with current resource state. Those transport definitions do
not select the business mappings above. The project operation design retains
[non-idempotent retry precautions](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2).
No dependency, runtime or production acceptance follows from this proposal.

## Visitor handoff creation proposal — 2026-10-06

Status: DOING, unreviewed. This refines the existing IF-CHAT-04 POST
`/api/v1/chat/sessions/{session_id}/handoffs`. It introduces no route, visitor
account, proof family, assignment permission or working consultation. The
[closed directional schema](visitor-handoff.schema.json) requires explicit
`request` or `response` selection; the module root rejects instances. The prior
reviewed lifecycle remains controlling, with its exact bytes preserved. Earlier
review receipts do not cover this addition.

### Visitor intent and exact sharing

The visitor explicitly chooses human help for a department. The interface
restates the sharing choice and applicable notice/purpose before submission.
IF-CHAT-02 owns consent decisions; this creation request does not supply new
consent, retroactively grant storage or grant media permission. A current positive
consent revision is required in the shape. Actual required purposes and decisions
must independently pass at the admission boundary, including durable request,
operation/alert metadata and any context transfer. Legal mappings remain held.

An `apply` request contains only phase, `request_text_handoff` intent, operation
ID, immutable publication context with a required canonical department wing,
expected consent revision and the explicit sharing variant. Session ownership
comes from the protected route and current chat-process proof, with its separate
CSRF request proof; it cannot come from JSON fields or a guessed ID. The server
resolves the department against eligible approved content and the permitted chat
context. A public availability response is advice, not a reservation or proof
that this private request is eligible now.

| Sharing variant | Allowed meaning |
| --- | --- |
| `no_prior_context` | Request a human without transferring prior conversation content. The minimal approved department/request metadata still follows its own consent and data-class rules. No hidden summary or transcript accompanies it. |
| `reviewed_projection` | Reference the exact context preview explicitly chosen by this visitor for the applicable purpose, using projection ID, revision and checksum. It does not include an arbitrary transcript, URL, staff identity or client-supplied storage permission. |

The preview is a separate prerequisite, not something this request schema creates
or approves. Its preparation/read/event shape, expiry, permitted field/class map
and exact display/confirmation evidence remain held under IF-CHAT-03 and the
existing purpose boundary; no new preview endpoint is selected here. Bind it to
the current selected session/proof context, original eligible source, sharing
purpose and consent revision, exact displayed content and permitted lifetime.
Its ID/checksum is neither a bearer credential nor a consent record. A client
assertion or shape-valid reference cannot establish that a preview ever existed,
that it was shown, or that the visitor approved those bytes.

Preview preparation cannot create an unauthorized durable copy of ephemeral
conversation content, trace or linkable metadata. Where earlier non-consented
content is still legitimately available, a separate explicit sharing operation
may select it under the approved purpose; it cannot claim prior storage was
consented. Lost or expired ephemeral content cannot be reconstructed from a
hidden transcript or sent to an AI/provider to manufacture context. If the exact
preview is unavailable, refuse that sharing intent truthfully and preserve
no-prior-context help, browsing and Book/Contact under their own authority.
Changing the sharing choice requires a fresh explicit visitor intent after any
uncertain prior request is reconciled; it is not an automatic fallback dispatch.

### Admission, uniqueness and uncertainty

Use the lifecycle's shared authoritative handoff binding for this permitted
conversation/purpose. Different operation IDs racing across tabs/workers cannot
create two simultaneously routable requests. A client cannot select an owner,
assert availability, change a queue, submit a staff decline/end action or choose
a target/provider through this body. Assignment and human acceptance retain
their independent staff grants and guarded transitions.

The admitted operation binds selected chat context, action, original release/
department, consent revision and immutable sharing meaning. A same-ID changed
meaning conflicts. Rotating proof/CSRF is not a new business intent. Historical
request truth does not renew consent, retention, routing or current authority.
Recheck current private disclosure permission before returning a known result;
later source withdrawal does not erase a valid historical request or permit new
use/transfer of the withdrawn source.

`phase: reconcile` contains only fixed intent and the same operation ID. It
cannot supply a new preview, grant consent, change department, route another
request or replay the create effect. Resolve it only within the currently
authorized selected session and original operation scope. Absence from one
worker/store is not proof that no effect occurred: consult authoritative binding
and operation evidence, or return unresolved/unavailable. Do not create a new ID
or replace the request to escape uncertain admission or a missing reply.

### Minimal response and recovery

A `requested` result contains the operation/intent, immutable creation-time
handoff ID/revision and original sharing variant/reference. It establishes only
the known permitted durable request. It does not assert queue placement, an
owner, staff availability, an alert, human acceptance, a first reply, text/media
connection or a response-time promise. The receiving boundary must correlate it
to the awaited process/operation and exact sharing intent. A late historical
creation result cannot replace a separately known current accepted/ended state.

`pending` is only for positively known admitted but unsettled work, with
reconciliation of the same operation. Unknown admission uses a fixed unresolved
or unavailable error rather than invented pending or definite failure. Errors
are closed fixed code/recovery pairs without private staff details, preview text,
raw request/proof values or process-existence disclosures. The reused common
error representation supplies no staff authority; decline-only reason errors
are excluded. This request's error says nothing by itself about an earlier
possibly committed operation.

Proposed HTTP associations: 200 for an authorized known `requested` outcome;
202 for positively admitted `pending`; 409 for a current binding/intent conflict,
source/consent/sharing change or known `staff_unavailable`; 503 for unresolved
admission or service unavailability. Existing fixed 400/403/413/415/429/500
categories retain their request/error meanings. The shared private raw JSON,
Origin/proof/CSRF and no-store obligations still apply. These are proposed
associations, not HTTP handler evidence or proof of any earlier operation's fate.
Exact full lifetime/header/body/work profiles and private auth mechanisms remain
held; this addition selects no new capacity, timeout or production dependency.

Unknown availability cannot produce a positive offer or routing claim. Known
`staff_unavailable` offers Contact/Book without promising a callback or starting
another handoff. Alert failure remains beside durable request truth and cannot
undo or duplicate that request. Separate status/events must later project actual
queue/acceptance/text states under current process/consent/assignment authority;
this creation result cannot synthesize them.

### Verification and remaining definition

Focused fixtures exercise the actual request/response schema-validator boundary:
phase/direction separation, required department/consent/sharing, closure against
authority and private payload injection, exact preview-reference syntax, and
pending/error/result separation. Synthetic valid references and a mismatched
operation intentionally remain shape-valid, demonstrating that real preview,
consent, correlation and durable effect need actual implementation boundaries.

Required runtime cases include cross-process proof, wrong/unshown/stale preview,
consent withdrawal versus creation, expired/lost ephemeral context, source
withdrawal, simultaneous different operation IDs, lost reply/restart/late commit,
changed sharing on the same ID, stale public availability, alert failure without
lost request, and reordered historical replies after acceptance/ending. Browser
checks must preserve separate consent, honest waiting and equivalent Quick Access
and Book/Contact. No mocked availability or schema result can prove these facts.

Still outstanding: preview preparation/display/confirmation and visitor handoff
status-event directions, staff initialization/control, complete raw HTTP/auth/
work profiles, data-class retention and reason/owner/legal mappings, physical
concurrency and revocation enforcement, measured limits, production screens and
independent/founder acceptance. No actual request, transfer or grant is implemented.

Primary guidance checked 2026-10-06: [HTTP retry semantics](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2)
do not make POST safely repeatable on their own. The guarded reconciliation above
is a project proposal. [JSON Schema closure](https://json-schema.org/understanding-json-schema/reference/object#unevaluated-properties)
and Context7 `/python-jsonschema/jsonschema` support the offline reference/real
validator checks; neither establishes current business authority or wire freeze.

## Staff channel initialization and control proposal — 2026-10-06

Status: DOING, unreviewed. This completes proposed control shapes around the
staff text variants above at existing IF-STAFF-15 WebSocket
`/api/v1/staff/conversations/{session_id}/events`. No route, account, grant,
subscription or chat implementation is created. Select `client` or `server` in
[staff-chat-control.schema.json](staff-chat-control.schema.json); its module root
rejects instances. Visitor control/text variants are not accepted on this route.
Earlier bounded receipts cover their exact preserved inputs, not this addition.

### Upgrade, initialization and readiness

1. Before upgrade, apply the current staff security/session contract, approved
   same-origin WSS/Origin and raw header/Cookie profile, selected conversation,
   current explicit text action and accepted handoff/assignment, required consent
   and permitted projection. A visitor process cookie, an Entra identity alone,
   guessed selector or content role cannot substitute for these grants. Reject
   ambiguous credentials and query/subprotocol bearer tokens generically.
2. Atomically reserve the shared bounded connection capacity, including
   quarantine and draining work. A transport accepted into quarantine has no
   private output, replay, text ticket, provider work or business action yet.
3. Receive one `staff_initialize` text JSON message within the inherited
   five-second monotonic initialization deadline. It carries protocol version 1,
   the non-bearer staff CSRF value, expected handoff ID/revision/ownership
   generation, expected positive consent revision, and explicit null or a closed
   resume cursor. Resolve the actual staff principal/session and conversation
   from current protected authority; no client identity or role is accepted.
4. Reject malformed UTF-8/scalars, duplicate members, unknown fields, coercion,
   nonfinite numbers, binary input and excessive fragmented/reassembled or
   decoded allocation before admission. Recheck current session/CSRF, object,
   action, handoff/assignment and purpose/consent guards together. The expected
   values are comparison inputs, not permission. A stale snapshot cannot silently
   select another owner or consent map. Repeated initialize or text/receipt before
   readiness closes the attempt without a business effect.
5. Only successful guarded initialization may produce `staff_ready`, containing
   server-issued channel/participant-stream IDs, the admitted handoff binding,
   current positive consent revision, coordinated head/next sequence and
   `fresh | resumed`. This is a transport projection snapshot, not a new human
   acceptance, assignment, staff presence, transcript transfer, send ticket or
   reply. Text admission remains the separate staff ticket protocol above.

The CSRF field reuses the existing canonical unpadded 32-byte base64url
representation only. A syntactically valid visitor token cannot pass staff
purpose/session verification. Exact staff CSRF issuance/rotation and JWT cookie
names, signing/rotation and session-revocation mechanisms remain held under the
staff mediation proposal; this schema chooses none of them. The approved
Secure/HttpOnly/SameSite cookie, 30-minute idle/eight-hour absolute and server
logout requirements remain. Never place staff JWT/provider/visitor bearer values
in this body, URL, public HTML or script-readable storage. Socket activity does
not itself renew staff identity, consent or absolute session lifetime; the exact
qualified idle-activity rules still require the staff session profile.

The client binds readiness to its selected conversation, expected handoff and
currently active local socket attempt. Delayed callbacks from a discarded
attempt cannot update the current projection. Server state also binds the channel
and stream internally to the real principal/session, conversation, handoff,
ownership generation, allowed purposes and consent. UUIDs are linkable metadata,
not bearer grants. Revalidate actual current authority at each relevant inbound
admission, outbound delivery and replay; successful initialization is not a
continuing permission.

### Staff stream, receipt and resume

The staff stream is distinct from the visitor stream. Its ordering uses the
existing authoritative coordinator and immutable events, with a guarded replay/
live watermark and no sequence reset/wrap inside a stream. For fresh readiness,
`next_sequence = head_sequence + 1` and no old transcript is replayed. For resumed
readiness, the requested cursor must belong to this same participant/conversation/
generation projection, lie at or before the head and have a complete currently
permitted suffix; `next_sequence = after_sequence + 1`. JSON Schema constrains
the exact integer representation but cannot enforce these relational facts.

`staff_receipt` contains only protocol/kind, current channel/stream, handoff ID,
ownership generation and the contiguous through-sequence. It acknowledges events
accepted into the currently authorized staff projection, not human reading,
durable transcript storage, visitor delivery or a business outcome. Verify it
against what this channel actually delivered. Duplicate receipts cannot advance
over an unseen gap; older receipts cannot move the watermark backward.

Replay preserves original immutable event identity/bytes and participant/
ownership meaning. Check current session, action, consent, assignment, source and
each permitted projection before delivery. Reassignment cannot relabel the old
operator's stream for the new owner or automatically transfer old history.
Separate approved history-transfer authority and legal mappings are necessary;
a new stream or cursor cannot supply them. If required content/authority is lost,
withdrawn, expired or unprovable, do not skip a gap and claim a complete resume.
Do not reconstruct non-consented ephemeral data from logs or a durable fallback.

Ending, reassignment, consent withdrawal, staff logout/session expiry/revocation
and unknown authority fence dependent tickets, subscriptions, queued output,
replay and late work under their actual decision boundary. Closing a socket is
not proof of that suppression, and already disclosed bytes cannot be recalled.
The snapshot may remain historical evidence but cannot renew any current grant.

### Fixed recovery, close and shared finite profile

Before authority/initialization succeeds, use generic handshake denial or a
close without private JSON. After initialization, `staff_unavailable` may carry
only fixed safe code/recovery pairs when that minimal output remains permitted.
Replay/authority changes suggest separately authorized conversation inspection;
resource/service unavailability suggests reconciliation of staff operations.
These labels grant no read, new owner, replay or redispatch. If no safe disclosure
is possible, close without a body. No raw exception, token, staff identity,
transcript, accepted/ended claim or booking result is included.

Reuse the visitor close/recovery proposal's empty reasons, safe close-code
classification, five-second physical cleanup target and separate work-reservation
accounting. A normal close does not end the consultation; a cleanup timer does
not prove termination or settle admitted text work. Apply its bounded four-attempt/
60-second reconnect episode and clipped initialization deadlines to this staff
subscription, rechecking current staff authority each time. Do not reset the
budget on remount, tab visibility, readiness followed by failure or automatic
authentication retry. Deliberate retry can start another episode only under
current authority, without resubmitting an unresolved business command.

The following are unmeasured proposal ceilings, not capacity or legal retention
claims. They extend the existing shared pools to staff without doubling them:

| Resource | Combined participant treatment |
| --- | --- |
| Connections | 128 service-wide, at most 32 quarantined, and two total per selected conversation across visitor and staff, including quarantine/drain. Another tab consumes the same pool. |
| Initialization/control | Five seconds and 8,192 encoded bytes per initialization; control input retains 8,192 bytes, one admitted control per connection and 64 service-wide across participants. No hidden waiting queue. |
| Queued output/replay | Preserve per-event 16,384 bytes and existing per-connection bounds. Also reserve a shared conversation output allowance of 64 events/262,144 bytes and shared replay allowance of 64 events/262,144 bytes across participant streams; no new staff allowance. Replay age is at most 60 monotonic seconds from original admission, with earlier legal/consent/session/source expiry winning. |
| Aggregate buffers/work | Existing 33,554,432-byte service buffer pool includes staff output/reassembly/replay and physical copies. The single unsettled text operation per conversation/eight-service-wide work pool and text reconciliation/rate ceilings remain shared. Control admission cannot enlarge creation, consent, handoff or provider pools. |

Count each physical copy, while a demonstrably shared immutable buffer is counted
once. Reserve room for any minimal failure control within the same ceiling; if
impossible, close without it. Do not release capacity solely on observer timeout,
lost handle, lease expiry or client disconnect. Scheduling fairness, transport/
decoded-object overhead, authoritative capacity bookkeeping and physical cleanup
need measured, reviewed mechanisms; uncertain state denies new admission.

### Evidence and remaining boundaries

Focused fixtures exercise real control-validator direction/closure, required
fields, canonical CSRF representation, cursor/integer bounds and fixed recovery.
They deliberately demonstrate that wrong sequence relations, an unbound CSRF
value or a synthetic binding can remain well-shaped. Schema results cannot prove
authorization, upgrade, readiness, contiguous delivery, suppression or cleanup.

Required actual-boundary cases include visitor credentials/controls at the staff
route; wrong staff/action/conversation; stale consent/handoff; repeated or late
initialization; replay/live races, guessed/old-owner cursors and skipped gaps;
over-acknowledgement; logout/reassignment/ending versus queued output; concurrent
tabs/workers exhausting shared pools; fragmented/decoded limits, slow clients,
lost coordinator and stuck cleanup; and retry storms without duplicate text.
No browser mock or framework connection flag proves those invariants.

Exact staff cookie/CSRF/JWT/revocation mechanisms and grants, participant/history
legal mappings, complete raw transport/auth/work profiles, scheduling/physical
enforcement, measured bounds, production screens, independent review and founder
acceptance remain held. Visitor sharing-preview/status directions remain separate.
No account, role, real channel, history transfer or application behavior is built.

Primary sources checked 2026-10-06: [RFC 6455 security/limits](https://www.rfc-editor.org/rfc/rfc6455.html#section-10)
defines transport concerns, not staff business authorization. The participant,
fencing and pooled-limit choices above are project proposals. The reused
[JSON Schema closure guidance](https://json-schema.org/understanding-json-schema/reference/object#unevaluated-properties)
supports shape validation only. No runtime or dependency version is selected.

## Visitor preview and status event proposal — 2026-10-06

Status: DOING, unreviewed. This defines additional closed directions on existing
visitor IF-CHAT-03, not new routes, accounts, consent grants, handlers or real
staff. Select `client` or `server` in
[visitor-handoff-events.schema.json](visitor-handoff-events.schema.json). Its
module root rejects instances. Controls, text, consent, handoff creation and
staff directions retain their separate prerequisites and authorization. Earlier
receipts do not cover these new inputs; predecessor bytes remain preserved.

### Preparing exactly what will be shared

On a currently initialized authorized visitor channel, `prepare_handoff_preview`
contains only protocol/kind, current channel/stream, scoped operation ID, expected
positive consent revision, eligible publication/department context and selected
event references. Each reference supplies event ID, stream and sequence; these
are untrusted selectors, not authority or source text. No raw history, client
role, staff identity, provider, storage permission or new consent is submitted.

At actual admission, recheck current own-process/initialized-channel authority,
allowed action, source context and all required preview/transfer purposes. Resolve
each reference to an existing permitted event in this same process/projection.
Reject repeated event identity even when the sequence differs, mismatched event/
sequence bytes, an unauthorized stream, unpublished/withdrawn source use, and
unavailable or lost ephemeral content. JSON Schema uniqueness checks exact
objects only; these contextual checks must occur at the real boundary.

Visitor-authored selector acquisition is still an open source-registration
prerequisite. Existing visitor text submissions carry operation/ticket metadata,
not a selectable visitor-own-text event with server event ID and sequence. The
staff-only visitor-text projection cannot be relabeled into the visitor stream.
Define and independently review that registration/projection path before
admitting visitor-authored selection; client display history or invented IDs
cannot satisfy it. This proposal does not silently add a new text direction.

Assemble a deterministic plain-text preview from exactly those permitted selected
messages, in authoritative conversation order with explicit participant/source
labels. Do not silently include other messages, omit selected content, truncate,
normalize strings, infer a contact record, or generate an AI summary. User/model
text remains untrusted content rather than approved company evidence. If the
selection cannot be represented within the limits, refuse the preview and let
the visitor make another explicit selection. No provider call, staff routing,
alert, durable request or consent decision is caused by preparation.

A prepared `handoff_preview` event includes the scoped operation, exact closed
projection document and projection reference. The document binds server-issued
projection ID/revision, eligible context, consent revision, approved purpose and
notice reference, selected events and exact plain text. The reference's digest
is SHA-256 of that entire document's RFC 8785 canonical UTF-8 bytes, excluding the
outer transport/event and the reference itself. The document contains no digest,
so there is no self-hash cycle. Reject invalid scalar input, duplicate JSON keys
and nonfinite/unsafe numeric values before canonicalization; preserve strings
without Unicode normalization. No canonicalizer implementation/library is
selected or validated by this shape proposal.

The receiving boundary must match operation, projection ID/revision, source/
purpose/consent and selected references, verify canonical digest against the
actual document and safely render its text as text. Transport receipt cannot
claim that the visitor read or understood it. The production journey must show
the complete proposed sharing content and notice, permit selection changes or
no-prior-context help, and require explicit final visitor intent. That final
IF-CHAT-04 request references this exact still-permitted preview. A stale/change/
lost preview, mismatched digest or changed consent cannot silently apply a new
document or a different sharing choice. Real screen/keyboard/assistive-technology
checks remain required; no pixel display or affirmative action is proven here.

### Bounded preview lifetime and uncertain preparation

Keep only one currently permitted prepared snapshot and one unsettled preparation
per selected conversation; opening another channel/tab cannot obtain another
allowance. Proposed selection is 1–16 event references and at most 8,000 Unicode
scalar values of exact preview text. The inherited 8,192-byte whole client
message and 16,384-byte whole output event limits apply independently. Reserve
against the existing shared control/output/buffer pools before work; no new
unbounded history queue or provider/text work pool follows. Oversize encoded
documents must fail rather than silently lose selected content.

These are unmeasured proposal ceilings. Preparation/reconciliation, reference
validity and selected-source retention require an approved finite work/lifetime
profile. Reference checks revalidate current process, source, purpose/consent and
original expiry anchors; preparation, reads, copies or reconnect cannot reset
them. The transport's replay ceiling does not itself select preview retention or
give permission to keep a separate transcript. No durable snapshot, digest index,
trace, retry record or linkable metadata may precede its data-class legal gate.
Lost ephemeral state is unavailable, not recoverable through logs or an AI call.
Until exact lifetime/legal mappings are approved, actual preview admission stays
held. Accessible reading/timeout warning, adjustment or refreshed-review behaviour
must be specified with that profile; no forced timed confirmation is accepted.

Same-operation preparation retries bind the same principal/process, context,
consent revision and exact selected intent. Changed meaning conflicts. A closed
`reconcile_handoff_preview` supplies only current transport metadata and original
operation ID, never new selection, consent or preparation. Return the exact
still-permitted known outcome, known admitted `pending`, or fixed unavailable
category. In the closed schema, `outcome_unresolved` must use
`reconcile_same_operation`; terminal `sharing_unavailable`, `authority_changed`
or `resource_limit` uses `review_or_contact_book`. Contact/Book remains a
separately permitted alternative, never permission to restart the uncertain
preparation. An unresolved preparation is not permission to start another operation
or handoff. Reconcile uncertainty before an explicit revised selection or final
creation. Replayed preparation does not renew validity or certify a visitor read.

### Honest visitor lifecycle updates

`inspect_handoff` requests only an authorized child handoff's status on this
channel; ID knowledge does not grant a read. Known status may also be projected
as a guarded subscription event. A closed `handoff_status` exposes only handoff
ID/revision and one known current state: requested, queued, accepted, text_active,
declined, ended or expired. Each state requires the lifecycle's separate actual
evidence. It reveals no operator identity, private assignment/generation, internal
reason reference, transcript, alert result, presence, callback, media, deletion
or booking outcome. Approved public recovery copy remains a screen/legal task.

The coordinator binds private event identity/sequence to the authorized visitor
stream and original contextual metadata. The event's release identity is context
provenance, not proof that public source content is currently eligible. Recheck
allowed private disclosure without erasing valid process history when public
sources change. Do not replay withdrawn content merely to fill a status gap.

The consumer accepts updates only for the selected process/handoff/current socket
attempt and coordinated eligible stream. Preserve known state against stale
handoff revisions and obsolete HTTP creation replies. Same event/revision with
changed meaning is a conflict, not a replacement. No preview, receipt, socket
ready, presence response or alert may fabricate acceptance or text activity.
Unsettled ending or other mutations remain visibly unresolved beside the last
known lifecycle state; do not label ended until the required result is known.

If current status cannot be established but minimal output remains authorized,
send fixed `handoff_status_unavailable` without echoing the object identity or
existence. Preserve last known history and offer separately permitted Contact/
Book. It does not mean declined, expired, ended or no request. If disclosure is
not permitted, close generically without a private status body. No automatic
replacement handoff, new owner, hidden transcript or repeated business command.

### Required evidence and remaining definition

Focused schema fixtures cover closed client intents, selected-reference limits,
direction/closure, prepared versus pending/unavailable, minimal status and safe
private-field exclusion. They explicitly show that a fabricated digest/reference,
same event ID with changed sequence, or invented accepted-state representation
can pass shape validation. Actual digest/canonicalization, reference resolution,
consent/display/confirmation, lifecycle truth and ordering remain unproven.

Actual-boundary cases include cross-process/unshown selection, duplicate identity
with changed sequence, malformed scalar/canonical bytes, wrong digest/reference,
lost source, consent/source withdrawal during preparation/confirmation, byte
overflow without truncation, pending/restart/late completion, old status versus
current ending, inspection denial without an existence oracle, shared tab/worker
limits, and no provider dispatch or hidden durable copy. Browser checks must show
all selected context, accessible notice/actions and truthful waiting/recovery.

Exact preview work/lifetime/legal mappings, staff/private auth/transport profiles,
physical ordering/uniqueness/revocation, measured caps, compatibility graph,
production screens, independent review and founder acceptance remain held.
No preview, status service, storage/transfer permission or real specialist is built.

Primary sources checked 2026-10-06: [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785.html)
defines reproducible canonical JSON while preserving string content;
[RFC 6455 security/limits](https://www.rfc-editor.org/rfc/rfc6455.html#section-10)
does not supply business consent, preview confirmation or lifecycle authority.
The projection, selection and pooled-limit decisions above are project proposals.

## Visitor-owned message registration proposal — 2026-10-06

Status: DOING, unreviewed. This proposes the missing visitor-authored selector
path identified by the [corrected handoff packet review](reviews/handoff-packet-correction1-v1-2026-10-06.md).
It extends IF-CHAT-03 only, through [visitor-message.schema.json](visitor-message.schema.json).
The earlier packet remains a bounded PASS at its frozen inputs; it does not cover
this new direction or accept an implemented source registry. Actual admission
remains held pending review, legal/lifetime/mechanism definitions and approval.

### One own-text projection for an accepted input

The server can emit `visitor_text_registered` only for an actually admitted
visitor text intent. Its immutable visitor-stream header contains protocol,
kind, stream, event ID, sequence and original release identity. Its closed payload
contains only the original operation ID, command revision and exact accepted
plain text. There is no client-supplied role, channel/proof/consent metadata,
staff identity, handoff assignment, provider result or delivery/read promise.
This is a private own-text projection, never approved company evidence.

Before registering a new input, verify the current own-process/channel/action,
ticket and exact intent, applicable classification/purpose/consent and legal
handling. Reserve the original event identity, visitor-stream order, permitted
source representation and shared output capacity within the guarded command
admission, before any new dependent provider or staff dispatch. One original
process operation/revision has one own-text registration, even across tabs,
reconciliation, reconnect or late completion. Unknown admission/registration
does not permit another dispatch or a second registration.

The own-text sequence precedes dependent answer/forwarding projections in that
visitor stream. Preserve original text without trimming, normalization, summary
or truncation; raw invalid scalars, whitespace-only or disallowed input still
fail actual admission. Recheck current disclosure authority at delivery/replay.
If the guarded registration cannot be established, deny new dependent dispatch
and preserve uncertainty about any already admitted effect. Allocation, an event
shape, a local message bubble or a status of admitted proves no actual delivery.
This registration means neither AI dispatch nor staff acceptance/readiness/read.

This server variant belongs to the visitor projection only. The existing
staff-stream `visitor_text` remains independently guarded, with its distinct
assignment and participant-specific identity. Do not copy staff event IDs,
sequences or ownership into the visitor stream. No new client text command,
HTTP route, account, staff grant, consent grant or durable transcript is added.
Adapters must compose explicitly approved directions; neither the generic event
header nor a module root is an accepted catch-all message.

### Sources eligible for the sharing preview

Register the authoritative association between the original process, visitor
stream/event/sequence, kind, exact permitted bytes, origin operation and existing
classification/purpose/expiry anchors. The association is server-owned and must
refer to actually authorized projection/source state, not client display history,
an input copied from a command-result event, logs or inferred staff history.
No hidden history store, durable index or longer retention follows from this map.

The proposed selector allowlist is only `visitor_text_registered`, `ai_answer`
and permitted visitor-delivered `staff_text`. Controls, tickets, command results,
status, preview documents and other events cannot be selected as conversation
text. This prevents previews from selecting earlier previews or operational
metadata. A source must have been projected to this own conversation and remain
permitted for the requested preview purpose; knowing its identifier is not a
read or transfer grant. A transport receipt is not reading or sharing consent.

Resolve the supplied stream/event/sequence against that association; reject
wrong process/stream, conflicting identity or bytes, repeated original message,
missing/unavailable/expired content and disallowed source use. Order the exact
selected text by authoritative visitor-stream sequence, never client array order
or client time. Derive participant labels from the registered kind, without
accepting a claimed role or invented specialist identity. Keep AI identification
and nonbinding status in its presentation. The final digest-bound preview and
explicit IF-CHAT-04 confirmation remain separate obligations.

An event's original release header is provenance, not permission to publish the
visitor's question or use currently withdrawn public evidence. Preserve valid
private process history without relabeling it into a new release; fail affected
source-dependent preview use when its authority is unavailable. The target
department/context must satisfy the existing current-context guards separately.

### Reconciliation, finite ownership and required evidence

Existing `reconcile_text` retains the same operation/revision. A known own-text
projection can be replayed only with its original identity/bytes and all current
guards, within the existing contiguous replay protocol; do not emit a fresh
registration to fill a missing event. Lost state or a forbidden replay is
unavailable. Earlier unregistered input and local pending text cannot be turned
into selectable history by reading browser storage or reconstructing a transcript.
The visitor can use no-prior-context help, separately permitted Contact/Book,
or later make an explicit new text intent after uncertainty has settled.

The inherited 2,000-scalar visitor-text limit and 16,384-byte complete output-event
ceiling apply independently. Registration/source metadata and physical copies
must remain inside the existing shared finite output/replay/aggregate pools;
they do not create a second staff/visitor history allowance. Reserve before work,
account actual encoded and decoded allocations, and deny when capacity or cleanup
is unknown. Exact source/work/reference lifetimes, legal mappings and physical
storage/fencing remain held; the replay ceiling is not their retention policy.

Focused fixtures exercise this new server-only closed shape, required identity
and text, private-field exclusion and scalar limits. They explicitly demonstrate
that wrong intent correspondence, unsafe text and invalid raw scalars can pass
shape validation. Actual registration, ownership, delivery and selection tests
must include forged/cross-process references, two-tab admission, duplicate
registration, changed-text reconciliation, late ordering, lost/withdrawn sources,
consent changes, buffer limits, replay without dispatch, exact preview order and
accessible selection/confirmation. No such runtime or UI is implemented here.

Primary representation sources checked 2026-10-06: the [JSON Schema composition guide](https://json-schema.org/understanding-json-schema/reference/object#unevaluated-properties)
and Context7 `/python-jsonschema/jsonschema` describe closed composed objects and
explicit registry/format checking. [RFC 6455](https://www.rfc-editor.org/rfc/rfc6455.html#section-10)
does not define these business registrations or grants. The direction, selector
allowlist and admission/ordering obligations above are Hengshi proposals, not
claims that the transport standard or validator implements them.


## Preview resource and timing reconciliation proposal — 2026-10-06

Status: DOING. Definition only; no worker, store, permission, retention notice,
renewal endpoint or UI is implemented. Frozen predecessors remain preserved.
The 2026-10-07 amendment records D-076's resolved visitor-lifetime direction;
it does not amend the accepted accessibility criteria or approve the proposed
resource numbers/implementation. Fresh review of this amendment remains required.

### Finite preparation and selectable-source resources

Propose a five-second elapsed work deadline from guarded preparation admission,
including source resolution and serialization. This is a server work target,
not five seconds for the visitor to read or confirm. No AI/provider generation
is part of preparing an exact selected-message projection. Timeout may stop new
work, but cannot declare cancellation, known outcome or released reservations.
An unsettled worker keeps its original operation and physical reservations until
settlement is established; reconciliation never dispatches preparation again.
Existing shared control admission applies. No separate waiting queue is created.

Propose at most 64 selectable source records and 262,144 encoded bytes per
conversation, shared across all visitor tabs/channels. Count exact retained text,
event bindings, source metadata, prepared snapshots, serialized copies and pending
work against the inherited service buffer budget as actually allocated. The
source ceiling is a sublimit, not permission for an additional uncharged transcript
beside output/replay buffers. Decoded/runtime overhead requires its own measured
bound before implementation. Refuse admission before allocation when reservations
cannot be satisfied; neither a timer nor dropped connection releases them.

Keep one prepared projection and one unsettled preparation per conversation, with
the existing 1–16 selected references, 8,000-scalar text and whole-message byte
limits. Preserve source ordering and text exactly. No silent truncation, inferred
summary, provider call, log recovery, automatic pinning or storage escalation.
When a source cannot be retained under its approved purpose/class/expiry and shared
capacity, it is not selectable. Report that fact rather than substituting another
message. A client reference is never proof of ownership or retained source bytes.

A reference remains eligible only while its original source, process and purpose
are eligible. Removal, withdrawal, ending, source eviction or loss of authority
can invalidate it earlier. A prepared projection ends no later than its earliest
source/process/purpose boundary. Preparation, replay, viewing and copying do not
renew those original anchors. There is no additional arbitrary preview countdown;
its validity is subordinate to the current permitted conversation/source
profile. D-076 selects inactivity/explicit End, with no absolute conversation
age; it does not extend source retention. Continuing a valid conversation does
not permit unlimited transcript/buffer growth. Refuse new work at capacity rather
than silently deleting an active conversation to admit another. Numerical resource
targets are unmeasured and require independent acceptance plus actual allocation,
clock and load evidence.

### Timing conflict requiring a scoped decision

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

### Review presentation and implementation exit

Show the exact selected text and purpose before the final sharing action. Keep
selection, display, More time, consent and request creation distinct; no default
acceptance or automated submission on a timer. Warn accessibly with at least the
accepted response time, keyboard/touch operability and stable focus/read order.
At known invalidity, disable sharing, state the reason safely and offer permitted
Contact/Book. Do not replace a displayed projection silently; a changed prepared
projection requires fresh review. Unknown work first reconciles the same operation.
A fallback or new session cannot claim to preserve a lost anonymous transcript.

The founder duration choice is resolved; proof/clock/End controls, permitted-state
preservation, class-specific retention/deletion and warning screens remain DOING
for independent review and later implementation. Test at actual admission, storage,
clock, revocation and browser boundaries: an active conversation beyond the old
two-hour mark; warning/More time and retained permitted progress; repeated extension
and stale duplicate denial; exact idle-boundary/End-versus-message races; authorized
visitor and assigned-staff ending versus unassigned-staff denial; retained cookie
after expiry; deadline exhaustion without reservation release; source loss;
cross-tab limits; stale preview; near-expiry extension; late/lost continuation
responses; disabled/replayed sharing; and assistive-technology reading.
No documentation wording test, schema count or read-only review proves them.
