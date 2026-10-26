# Governed human consultation lifecycle — v1 proposal

Status: DOING. Prepared 2026-10-05. Definition only; no handler, grant, record,
account, adapter or production screen is created. Integrated Phase 1 acceptance
and the exact implementation contracts remain required.

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
