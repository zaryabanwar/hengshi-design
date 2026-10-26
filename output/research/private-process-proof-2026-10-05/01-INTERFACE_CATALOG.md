# Versioned interface and process contract proposal

Status: DOING. Proposed 2026-10-04 under FR-015/FR-016, D-016/D-019/D-065.
The [interface catalogue](interface-catalog.csv) assigns logical v1 routes and
failure obligations to the required capabilities. No route is implemented or
activated here; existing public APIs remain protected until reviewed replacement,
consumer/deprecation and rollback contracts authorize migration.

## Review coverage

The [later independent review](reviews/current-definition-amendments-2026-10-04.md)
records bounded PASS for this catalogue, its operation CSV and all 143 logical
field rows at the receipt's exact hashes. The reviewed
[catalogue bytes](../../../output/research/contract-review-reference-reconciliation-2026-10-04/INTERFACE_CATALOG.pre-status.md)
are preserved. This page's review references were reconciled afterward; logical
requirements and field rows were not changed. PASS establishes proposal coherence,
not exact wire schemas, founder acceptance or runtime enforcement.

## Field dictionary and authority

The [process field dictionary](process-fields.csv) refines the catalogue into
logical request, response and private-record fields. It is a proposed v1 design,
not OpenAPI, a migration, a wire-format freeze or implemented enforcement. The
existing publication envelope/schema remains the format authority for public
release bytes; the dictionary references it rather than redefining its properties.
Accepted BF-01 and AF-01/AF-02 in
[the journey flows](../../phase-1-ux-architecture/FLOWS.md), the
[logical data contract](DATA_CONTRACT.md) and
[classification matrix](data-classification.csv) govern process meaning and data
handling. Proposed field names/types cannot override those requirements.

Each row records interface scope, direction, required condition, writer, source
authority, classification/storage, invariant and unresolved input. `client_to_server` means
untrusted input; `server_to_client` means an authorized minimal response;
`server_private` means a server-owned record field, never an accepted client input.
Any permitted response projection needs its separate `server_to_client` variant;
private storage alone does not authorize disclosure to a staff browser. Client input never grants
ownership, staff role, consent authority, email verification, slot eligibility or
confirmed provider state. A row's required condition applies to that operation or
state, not to every request. Private operational fields are not extra booking-form
requirements. The row status remains TODO until its detailed contract is reviewed;
the catalogue itself is DOING, with application implementation still held.

`path_input` is an untrusted route parameter, not an authorization grant.
`client_and_server` denotes separate allowed inbound/outbound variants, not
permission to send any server event from the client. Exact schemas must prohibit
server-owned fields in client messages and unauthorized response properties.

Logical types deliberately expose gaps: `bounded_text` has no approved numeric
limit yet, and a `closed_*` type still needs its exact alternatives/structure.
Do not implement those placeholders as unrestricted JSON, open strings or invented
defaults. Required fields are present and valid; an optional field may be omitted.
Null/empty handling, normalization, Unicode/email rules, transport/header placement,
HTTP status mapping and rejection semantics require the later exact schema. The
client clock is never authoritative. UTC instants must pass real calendar and
timezone validation; a regex, timestamp-shaped string or local label is insufficient.

The six BF-01 qualification fields remain email, organization, role, desired
outcome, matched wing and desired timing. One separate, versioned purpose-specific
consent record is the seventh required element. Its internal evidence fields do
not add visitor questions. Optional budget is omitted unless its representation
and meaning are approved; there is no inferred currency, minimum or fixed-price
branch. Wing keys resolve to the canonical five-wing inventory; a client cannot
select an unpublished department, provider, staff member or unrestricted destination.

Before a wire-format freeze, replace every unresolved input with approved evidence,
bind fields to request/response variants for all catalogue routes and event kinds,
and reconcile state transitions, role permissions, storage and retention. The
logical dictionary has the bounded independent review identified above; exact
schemas and integrated founder acceptance remain pending. The earlier review
capacity failure is historical and is not the current state of this proposal.

### Public publication GET refinement

The [public release-read HTTP proposal](PUBLICATION_READ_HTTP.md) refines existing
IF-PUB-01/02 with the unchanged envelope schema, identifier boundary, explicit
public error variants and eligibility-before-cache/precondition behavior. Its
[independent review](reviews/publication-read-http-2026-10-04.md) records PASS after
revision 1 at the exact producer hash. Request limits, eligibility/fencing/drain,
edge/CORS/method integration and integrated acceptance remain held; this is not a
whole-catalogue wire freeze. Other process error variants, proofs and private
operations retain their unresolved inputs. This later reference addition does not
replace the catalogue bytes covered by the earlier amendment receipt.

### Public department availability GET refinement

The [public availability-read HTTP proposal](AVAILABILITY_READ_HTTP.md) refines
IF-PRESENCE-01 with the existing canonical five-wing selectors, closed public
state/expiry and error variants, guarded freshness, strict raw JSON decoding and
conditional/client recovery obligations. Its
[independent review](reviews/availability-read-http-2026-10-04.md#correction-1-verification--superseding-bounded-pass)
records bounded PASS after correction 1 at the preserved exact inputs. Two
schema-tooling tests exercise body correlation/calendar checking only. The
logical field dictionary remains historical proposal input to this refinement;
its TODO rows are not an assertion that no later wire proposal exists. Public
expiry disclosure, exact timing/clock/resource rules, grants, mechanisms and
integrated acceptance remain held. No handler, decoder or truthful live staff
availability is implemented or proven by this reference.

### Staff availability PATCH refinement

The [staff declaration HTTP proposal](AVAILABILITY_WRITE_HTTP.md) refines existing
IF-STAFF-09 and SOF-01A/B with closed on/off commands, initial/current
identity-and-revision guards, authorized historical receipts, safe error variants
and same-operation uncertain-write reconciliation. Its [independent review](reviews/availability-write-http-v1-2026-10-05.md)
records bounded PASS for the [preserved proposal bytes](../../../output/research/availability-write-http-2026-10-05/AVAILABILITY_WRITE_HTTP.reviewed.md)
and listed source inputs, including the [exact pre-reference catalogue](../../../output/research/availability-write-http-2026-10-05/INTERFACE_CATALOG.before-write-reference.md).
Durable declaration, public live offer and human
acceptance remain separate outcomes; replay cannot renew validity or revive an
old on after off. The later [directional schema](availability-write.schema.json)
now encodes commands separately from responses, the existing revision-string
range, binding/result alternatives and fixed error/recovery pairs. Its
[bounded independent review PASS after correction 1](reviews/availability-write-shape-v1-2026-10-05.md#correction-1-disposition--superseding-bounded-pass)
covers the exact encoding, fixtures, additive explanation and illustrative-ID
repair. Canonical schema-ID resolution and file aliases were separately checked;
the earlier failing input retains REVISE. This later catalogue reference is
outside that review and proves no raw parser, HTTP or current-state enforcement.
The logical dictionary remains referenced input, not a competing
wire authority. Exact subject/delegate grants, validity/renewal, transport/work
bounds, retention/restore and physical compare/admission/fencing evidence remain
held. No handler, persistence, grant, runtime result or integrated acceptance is
implied. Earlier catalogue reviews keep their exact inspected identities; this
later refinement does not replace them.

### Governed consultation lifecycle refinement

The [consultation lifecycle proposal](HANDOFF_LIFECYCLE.md) refines existing
IF-CHAT-04, IF-STAFF-06/10–15 and AF-02/SOF-01. It separates current availability,
durable request, assignment, human acceptance, text connection and alert outcome.
Its [bounded independent review](reviews/handoff-lifecycle-v1-2026-10-05.md)
records PASS at the [preserved proposal](../../../output/research/handoff-lifecycle-2026-10-05/docs__phase-1-architecture__contracts__HANDOFF_LIFECYCLE.md)
and [exact pre-reference catalogue](../../../output/research/handoff-lifecycle-2026-10-05/docs__phase-1-architecture__contracts__INTERFACE_CATALOG.md)
identities. The proposed current-binding guards address duplicate creation,
concurrent acceptance/reassignment, unknown outcomes and late delivery without
granting roles or selecting physical constraints. Off, ending, alert failure and
public-source withdrawal do not manufacture another process's outcome.
Exact directional schemas, grants/owners, queue/reassignment/decline policy,
consent/projection and retention, resource/replay/revocation limits, physical
enforcement, provider capability, designs and actual runtime evidence remain
held. No new route, wire freeze, working consultation or integrated acceptance.
Earlier receipts retain their own exact inputs; this reference-only addition
does not extend their reviewed hashes to the current catalogue.

### Private preparation boundary

The later [semantic preparation engineering proposal](PUBLICATION_CONTRACT.md#semantic-preparation-engineering-proposal)
describes how the existing approved candidate becomes complete HTML and matching
derivatives. It is outside the earlier catalogue review's inputs; the separate
[semantic preparation review](reviews/semantic-preparation-v1-2026-10-05.md)
records bounded PASS at the [preserved inspected catalogue bytes](../../../output/research/semantic-delivery-2026-10-05/INTERFACE_CATALOG.reviewed.md).
No exact schema or runtime proof follows. It adds no public endpoint or staff grant. Preparation consumes an
immutable approved candidate and returns artifact identities/verification or a
failure to publication; neither result can approve or activate the candidate.

Input/output schemas must separately permit public content projection, private
job/approval references and artifact evidence. Public hydration/loader data is an
output disclosure boundary, not a copy of the private job input. The renderer's
code/toolchain/configuration identity, snapshot and route set must bind its result.
Changing any of them requires a new preparation identity; a stale result cannot
be attached to a newer candidate. The later
[private message proposal](PUBLICATION_CONTRACT.md#private-preparation-message-and-acceptance-proposal)
and [closed schema](publication-preparation.schema.json) now refine request,
prepared and failure shapes plus coordinator verification. They are outside the
preceding review's inputs; their separate
[independent message review](reviews/preparation-message-v1-2026-10-05.md) records
bounded PASS at the [preserved inspected catalogue bytes](../../../output/research/preparation-message-2026-10-05/INTERFACE_CATALOG.reviewed.md)
and listed schema/test hashes. Closed shape
does not prove cross-message identity, content, authority or activation checks.
Exact process isolation, bounded work, worker authorization, diagnostic retention
and physical fencing/transaction mechanisms remain implementation inputs.

### Staff and privacy field bindings

The later dictionary expansion binds logical fields to the added staff operations,
the existing assignment operation and privacy status. It also moves the explicit
availability setting to DE-22, retaining only the expiring derived reference in
DE-18. These are source-grounded logical records, not a completed wire schema.

| Operation family | Logical field groups and authority boundary |
|---|---|
| Staff/private object paths | `department_id`, `handoff_id`, `session_id`, `intent_id`, `lineage_id`, `exception_id`, `release_id` and privacy `request_id` are untrusted selectors. Each resolves under current object/purpose authority; none is a bearer permission. |
| Availability declaration/projection | A closed explicit declaration request is separate from the guarded intent result, server-owned revision/expiry and transient projection freshness. Durable acceptance cannot assert current available presence. |
| Queue and exception reads | Allowlisted filters and bounded pagination requests produce authorized minimal summaries and a distinct empty/unavailable outcome. No arbitrary query, unrestricted export, transcript copy or provider payload. |
| Handoff acceptance/decline/end | Purpose-permitted context, guarded transition results and an approved reason variant remain separate from server-owned assignment state. Concurrent acceptance cannot create two owners; ending cannot change consent, retention or booking truth. |
| Assignment/reassignment | A requested approved-assignee reference is untrusted input. The server binds the actual actor and checks assignment power, eligibility and current revision; no identity creation or implicit self-assignment. |
| Staff conversation events | Directional protocol/kind/payload, scoped delivery IDs, ordering and authorized resume are separate from the private authenticated sender and current assignment. Staff input cannot impersonate visitor/AI/server events or create a disallowed durable replay copy. |
| Alert recovery | A closed approved recovery variant applies only to an alert-class intent. Its result describes the attempt, never confirmation/cancellation of the parent booking or handoff. |
| Booking exceptions | A bounded evidence-based disposition and its truthful result do not replace authoritative provider reconciliation, erase exception evidence or manufacture booking confirmation. |
| Knowledge review | Exact bundle digest, independent review decision and verified evidence references bind the prepared grounding bundle; they grant no founder approval or activation. |
| Withdrawal and candidate editing | Closed withdrawal scope and guarded candidate edits exclude server-owned eligibility/approval fields. Suppression may remain pending; edits create new revisions rather than rewriting approved immutable release bytes. |
| Privacy status | The same authorized request has an opaque selector and minimal safe outcome. Request-specific verified proof is still required; accepted/pending cannot become verified deletion while copies or policy mappings remain unresolved. |

The common scoped mutation identity, expected revision, ownership/session proof
and minimal operation reference still apply where required. A group binding is
not an assertion that every listed field is required in every request. `closed_*`
and pagination types require exact reviewed alternatives/structures and limits;
do not implement them as arbitrary dictionaries or silently accept server-owned
properties in an input. Provider observations and workflow outcomes remain
server-authoritative even when an operator requests reconciliation.

Per-route directional schemas, event kinds/acknowledgements, resource and query
bounds, exact state variants, role/delegate mappings, legal retention and provider
proofs remain held. The later review identified above covers the logical expansion
at its listed hashes; prior receipts apply only to their own inputs. No request
handler, migration, authorization test or OpenAPI enforcement is implied by the
dictionary.

## Common boundaries

Publication reads are public technical data; conversation and booking objects are
private process data. An opaque identifier alone never authorizes object access.
Anonymous visitors need a reviewed process-scoped ownership/resume proof without
creating accounts. Staff actions require the server-enforced role/action matrix
and current object authorization; administrator status cannot approve content.
Exact token/cookie/link format, lifetimes and anti-abuse thresholds remain security
inputs. Proofs must not appear in URLs, general logs or public manifests.

The [anonymous private-process proposal](PRIVATE_PROCESS_PROOF.md) now recommends
per-process opaque server proof, protected cookie transport, two-phase creation
at the existing chat/booking POST boundaries, separate CSRF request proof and
current HTTP/WebSocket authorization. It preserves no visitor accounts and the
separate staff JWT/Entra controls. This new proposal requires its own independent
review and integrated acceptance; formats, numerical policies, legal mappings,
recovery, physical enforcement and the complete stable graph remain held.

The proposed [action/object authorization matrix](SECURITY_PRIVACY_CONTRACT.md#proposed-action-and-object-authorization)
binds IF-STAFF-01–IF-STAFF-08 to role or explicit operational authority plus exact
object/purpose and state conditions. The four staff roles are independent, not
an administrator inheritance ladder. Several roles on one principal do not permit
self-review/self-approval. Unmapped operational permissions remain denied until
their group/scope binding is approved; the catalogue does not assign them to an
administrator, founder or email alias owner by default.

For visitor routes, IF-PUB-01/02 and IF-PRESENCE-01 expose only eligible public
projections. IF-CHAT-01 and IF-BOOK-01 may establish the reviewed anonymous process;
other chat/booking/privacy operations require their own valid process proof and
current purpose/state eligibility. A staff session is not a substitute for that
visitor proof, and a visitor process proof grants no staff operation. Use dedicated
approved staff operations for authorized intervention. Email verification adds
booking-slot eligibility; it does not grant arbitrary process or staff access.

The catalogue now also assigns proposed interfaces to SOF-01 availability, queue
triage, request inspection, conversation accept/decline/end and governed staff
events, alert recovery, booking exceptions and knowledge review. Candidate edits,
controlled release withdrawal and an authorized privacy-request status read have
separate boundaries. These additions are traced below; they do not select exact
wire formats or grant operators. Do not overload assignment or reconciliation
endpoints with arbitrary action dictionaries. An allowlisted closed variant is
required wherever a proposed operation has several dispositions.

The field dictionary now binds their logical request/response/event groups;
complete exact directional schemas, bounded queries, state transitions and
security grants before calling the interface package complete. The security matrix covers IF-STAFF-01–08 explicitly; its
current-identity, action, object/purpose, state and deny-by-default rules also
apply to each new staff operation. Exact operational-role/group bindings remain
held. No new endpoint is an administrator fallback or implementation permission.

The initial availability record conflicted with SOF-01A/B by placing the durable
staff declaration and transient suppression together in Redis. The proposed
[availability split](DATA_CONTRACT.md#proposed-availability-intent-and-expiring-projection)
now distinguishes private PostgreSQL intent DE-22 from the ephemeral Redis
projection DE-18 in [the logical entity matrix](data-entities.csv). It preserves
the accepted architecture: PostgreSQL is durable truth and Redis presence is
derived. The [classification matrix](data-classification.csv) marks private intent
retention/deletion/backup treatment as unmapped; business expiry is not a legal
retention duration. The logical split has the bounded amendment review described
above. The later [availability consistency protocol](AVAILABILITY_CONSISTENCY.md)
and [independent review](reviews/availability-consistency-2026-10-04.md) refine
positive-read and handoff guards, identity-and-revision binding, decision-time
expiry and uncertain negative effects. The
[catalogue bytes inspected by that review](../../../output/research/contract-review-reference-reconciliation-2026-10-04/INTERFACE_CATALOG.pre-availability-reference.md)
are preserved. These receipts cover their exact inspected proposals; this later
reference update grants no persistence or availability implementation authority.

IF-STAFF-09 records an authorized guarded intent; successful durable acceptance
does not itself permit an available public projection. IF-PRESENCE-01 and handoff
routing require current unexpired intent/revision, current staff eligibility and
fresh required suppression state. Withdrawal, revocation, expiry, cache loss or
unknown projection/suppression state cannot remain available. A delayed old
projection cannot restore a withdrawn declaration, and retries cannot renew expiry.
Exact cross-store publication/invalidation proof, freshness intervals, delegate
scope and recovery/restore suppression remain held before the write contract
freezes. Teams still only suppresses an explicit setting and cannot create one.

Requests and responses use closed typed schemas with versioned action/state fields,
not arbitrary persisted dictionaries. Per-field schemas and numerical length,
message/resource and retry limits must be reviewed before implementation. Return
only public eligibility/availability and process-safe status; no provider secret,
private staff contact, queue internals, raw policy prompt or other visitor's data.
State-changing browser requests require the applicable origin/CSRF protection;
WebSocket upgrades verify the allowed Origin and object ownership independently.

Proposed error envelope: stable error code, safe explanation, retryability and
opaque operation reference where authorized. Do not echo submitted sensitive
values. Distinguish malformed input, unauthenticated process, denied operation,
stale revision/conflict, expired process, rate limiting, pending reconciliation
and service unavailability. HTTP success/acceptance is not provider confirmation.
An operation/status endpoint exposes only its authorized process's safe outcome.

Every applicable durable mutation carries a scoped operation identity and expected
revision. Reusing the same identity with changed intent conflicts; the same intent
returns its known result. An unresolved external write reconciles before retry.
Exact identity retention and external deduplication support require approved legal
and provider evidence, not an assumed universal idempotency header.

## Publication and presence

The current-envelope endpoint returns only an eligible approved release and its
schema/checksum. A release-specific read verifies eligibility and immutable
identity. Public route/department keys map to the candidate's canonical inventory;
arbitrary client keys never authorize draft, private or withdrawn content.
Knowledge and panels obey the publication contract, including urgent withdrawal.

Department availability reports explicit server-known availability or honest
unavailable/unknown state. It is not an attendance guarantee, staff identity
directory or raw Teams presence feed. Stale or suppressed availability cannot be
shown as live. The exact expiry and permitted response fields need reviewed rules.

## Chat, consent and resumable events

Session creation permits anonymous text guidance with an explicit consent choice.
Refused retention means ephemeral operation, not a hidden durable transcript.
Context references only the eligible publication and mapped wing; model output
does not grant staff, publication, calendar or tool authority. Answers include
approved accessible source references or a cannot-verify/refusal with help/Book.

PROPOSED event envelope: protocol version, session-scoped event ID/sequence,
event kind, active publication identity, safe typed payload and resumable cursor.
Acknowledgement means receipt/processing as defined by the event kind, never
booking completion or a human-read promise. Duplicate events are not redelivered
as new business actions; reconnect resumes only the same valid session/cursor and
eligible publication. Invalid/expired/revoked context explains failure and offers
a new ephemeral session without silently recovering old content.

Resume windows, replay bounds and ordering across workers require exact contracts.
If non-consented ephemeral state is lost, return unavailable/expired rather than
reconstructing it from a hidden durable copy. Consent change or deletion interrupts
disallowed persistence/transfer and follows verified privacy orchestration.
Handoff needs explicit visitor consent and current eligible staff assignment;
Teams is an alert destination, not the authoritative conversation store.

## Booking lineage and external effect

Qualification has six required data fields: syntactically valid email,
organization, role, desired outcome, matched wing and timing, plus one
purpose-specific consent record. Budget is optional. Do not add required name,
phone, visitor account, upload or prior AI/chat use. Accepted BF-01 lineage remains:

`BOOKING_STARTED → QUALIFICATION_COMPLETE → EMAIL_PENDING → VERIFIED →
SLOT_SELECTED → BOOKING_PENDING → CONFIRMED_QUALIFIED`.

Validation errors, expired/undeliverable challenges, no availability and
reconciliation errors use the accepted branch states. Correcting email invalidates
the previous challenge/verification; resends stay on the same lineage. Only the
successful current challenge enables availability/slot access. Client assertions
cannot verify email, choose an ineligible owner or confirm a calendar write.

Availability returns eligible 30-minute discovery slots with an unambiguous instant
and timezone for visitor-local display, including daylight-saving boundaries.
Review restates the slot, organization/role/outcome, wing and consent before submit.
Initial durable acceptance is BOOKING_PENDING. Exactly one reconciled approved
calendar/meeting record plus matching local state enables CONFIRMED_QUALIFIED.

Reschedule/cancel retain the lineage and last confirmed truth until the approved
provider result is reconciled. Do not expose either action until authorization,
cutoff/lifetime and provider rules are approved. An alert failure retries separately
and cannot undo a confirmed booking. Missing slots/owners provide an honest
Contact/Book recovery without a callback or response-time promise.

## Staff publication and operations

### Added operation traceability

| Proposed interface | Existing source and permitted purpose | Specific remaining contract |
|---|---|---|
| IF-STAFF-09 | SOF-01A/B, FR-009 and the proposed DE-22/DE-18 split: explicitly declare or withdraw staff availability. | Approved staff/delegate scope, exact expiry, idempotent on/off variants and proven guarded projection/invalidation. Private intent retention is held; unknown/stale/suppressed state never asserts availability. |
| IF-STAFF-10/11 | SOF-01C, FR-010 and DE-19: governed queue and request inspection. | Bounded filters/pagination and minimal context projection for the authorized object/purpose. Queue empty differs from unavailable; these reads cannot reconstruct a non-consented transcript. |
| IF-STAFF-12/13/14 | SOF-01D/E/F: accept, decline and end governed text. | Reviewed state/assignment transitions, concurrency, reason taxonomy and escalation. Acceptance requires current eligibility and only one owner; decline/end cannot erase evidence or change retention. |
| IF-STAFF-15 | FR-010/FR-016 and SOF-01D/F: actual governed text inside the Hengshi console. | Closed staff-origin event variants, server-bound sender, authorized assignment, Origin, replay/resume bounds and revocation. This is distinct from the visitor event route; no sender kind supplied by a client grants impersonation. |
| IF-STAFF-16/17 | SOF-01G and DATA-010: inspect and recover an alert attempt. | Bounded exception projections and approved retry/closure variants. An alert intent must belong to that operation class; its recovery endpoint cannot dispatch a calendar or publication intent. Missing acknowledgement requires reconciliation. |
| IF-STAFF-18/19 | SOF-01I/J and DATA-010: inspect and disposition booking exceptions. | Typed exception identity, evidence and held/escalated/resolved variants under approved policy. A disposition is not a substitute for IF-STAFF-07's authoritative reconciliation and cannot manufacture a booking state. |
| IF-STAFF-20 | SOF-01L, AI-001 and PUB-001: review the exact grounding bundle. | Approved knowledge-review scope, independent reviewer and exact bundle/source/checksum binding. Passing knowledge review neither approves new claims nor activates a release. |
| IF-STAFF-21 | Publication contract serving eligibility/urgent withdrawal and PUB-001/004/006. | Approved withdrawal authority, affected scope, concurrency and suppression acknowledgement. Preserve immutable bytes and private process truth; unknown suppression stays pending. No independent permission to delete retained source artifacts. |
| IF-STAFF-22 | PUB-002/003 and the data contract's revision-bound authoring rules. | Closed editable candidate fields, author/write scope and guarded revision creation. Server-owned approvals/eligibility are excluded; approved immutable release bytes cannot be edited in place. |
| IF-PRIVACY-02 | DATA-006 and DE-20: report the same authorized privacy request's safe outcome. | Request-specific ownership/identity proof and minimal projection. Knowing a request ID or email alone does not authorize a read. Accepted/pending is not verified deletion; unmapped copies remain pending. |

The additions are proposed 2026-10-04 and have the later bounded review identified
above; integrated acceptance remains pending. Their catalogue rows remain TODO.
Earlier interface review hashes cover only the earlier catalogue; the later
receipt identifies the amended routes and permission proposal it inspected.
No automatic prose test, generated OpenAPI, backend route or staff screen was
created. Required approved screen references and operational/retention policy
remain separate prerequisites.

Authoring, specialist review and founder approval refer to exact candidate content
and revision. Edits invalidate prior review; jobs cannot turn permission to prepare
artifacts into approval to publish. Activation uses the reviewed fenced publication
contract. Source withdrawal, deletion, booking reconciliation, assignment and audit
queries require their particular authorized role, not a blanket public admin API.

The catalogue includes staff release/SEO/knowledge, conversation/assignment,
booking reconciliation and audit responsibilities. Exact fine-grained operational
permissions, query filters/pagination and audit retention remain reviewed inputs.
All new paths are proposals; this catalogue must not silently remove prototype
routes or grant the current `require_admin` helper unverified role enforcement.

## Required conformance and remaining inputs

Contract tests must cover wrong-object access, self-approval, stale revision,
changed-idempotency intent, unknown acknowledgement, replay/expiry, corrected email,
duplicate submit, no owner/slot, withdrawn release and rejected provider route.
Cross-stream changes preserve valid process state or refuse with explanation.
Use synthetic fixtures and exact state labels; tests cannot mock away authoritative
confirmation or assert no-duplicate behavior from an adapter that cannot prove it.

Before implementation, finish per-field OpenAPI/JSON/WebSocket schemas, verified
ownership/CSRF and pagination/resource bounds, challenge/resume/availability expiry,
role matrix, Graph/alert/AI operations and data-class retention mappings. Their
absence remains explicit; this catalogue does not certify a complete API package.
