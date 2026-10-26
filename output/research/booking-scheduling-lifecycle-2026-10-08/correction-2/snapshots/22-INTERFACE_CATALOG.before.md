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

The later [staff sign-in mediation proposal](SECURITY_PRIVACY_CONTRACT.md#staff-sign-in-mediation-proposal)
refines the existing identity boundary: backend code exchange, bound callback,
validated principal and separate Hengshi staff-session admission. It introduces
no logical route, visitor account, operational grant or provider permission.
Its [separate review](reviews/staff-signin-boundary-v1-2026-10-06.md#correction-2-disposition--superseding-bounded-pass)
records bounded proposal-consistency PASS after correction 2 at the preserved
[security contract](../../../output/research/staff-signin-boundary-2026-10-06/SECURITY_PRIVACY_CONTRACT.correction2.reviewed.md)
and [catalogue](../../../output/research/staff-signin-boundary-2026-10-06/INTERFACE_CATALOG.reviewed.md)
inputs. These later references are outside the inspected bytes; exact
session/wire/freshness/retention mechanisms and founder/integrated acceptance remain held.
The [catalogue before this reference](../../../output/research/staff-signin-boundary-2026-10-06/INTERFACE_CATALOG.before.md)
is preserved unchanged.

The later D-076 [visitor continuation and End proposal](CHAT_EVENT_PROTOCOL.md#visitor-continuation-and-end-controls-proposal--2026-10-07)
and [closed directional module](visitor-lifetime-control.schema.json) refine existing
IF-CHAT-03 without adding a route. Status: DOING. The separate
[26-input lifetime-control review](reviews/visitor-lifetime-controls-v1-2026-10-07.md)
records bounded definition/representation PASS for its preserved snapshots,
including control-only admission, final End acknowledgement and reserved capacity.
Earlier reviews do not acquire that scope. Founder timing policy is settled;
concrete mechanisms, actual enforcement, complete-process accessibility and
integrated acceptance remain held.

### Booking qualification and email review navigation — 2026-10-08

The following separate reviews cover the named frozen proposals, not this later
navigation update or the entire current catalogue. Their receipts retain exact
manifests and inspected snapshots; later source changes do not inherit a PASS.

| Definition | Controlling proposal | Review scope |
|---|---|---|
| Qualification admission | [IF-BOOK-02 control](#qualification-admission-and-correction-proposal--2026-10-08) | [Logical-control review](reviews/booking-qualification-admission-v1-2026-10-08.md), correction 1: admission, correction fences and replay coherence. |
| Qualification encoding | [IF-BOOK-02 wire](#qualification-wire-profile-proposal--2026-10-08) and [schema](booking-qualification.schema.json) | [Wire review](../../../output/research/booking-qualification-wire-2026-10-08/final-independent-review.json), correction 1: directional representations, HTTP/control profile and installed mailbox-validator observations. |
| Email ownership | [IF-BOOK-03/04 control](#email-ownership-control-proposal--2026-10-08) | [Control and explanatory-view review](../../../output/research/booking-email-ownership-2026-10-08/final-independent-review.json), correction 1: code, timing, delivery uncertainty and guarded verification; separate supplied source/pixels. |
| Email encoding and admission | [IF-BOOK-03/04 wire](#email-ownership-wire-proposal--2026-10-08) and [schema](booking-email.schema.json) | [Wire review](../../../output/research/booking-email-wire-2026-10-08/final-independent-review.json), correction 1: closed directions/current controls, HTTP classifications and bounded protected extension admission. |

These are definition and validator observations, not a working qualification or
email service, measured capacity, wire freeze, provider selection or integrated
acceptance. IF-BOOK-05/06 availability, slot review and calendar submission, and
IF-BOOK-08/09 rescheduling/cancellation still need their exact definitions. Actual
request/store/job/browser enforcement belongs to later approved implementation.

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
separate staff JWT/Entra controls. Its
[correction-1 independent review](reviews/private-process-proof-v1-2026-10-05.md#correction-1-disposition--superseding-bounded-pass)
records bounded PASS at preserved exact inputs. These later receipt references
are outside those bytes. Integrated acceptance, formats, numerical policies, legal mappings,
recovery, physical enforcement and the complete stable graph remain held.

The later [directional creation/admission refinement](PRIVATE_PROCESS_PROOF.md#directional-creation-and-admission-proposal)
separates payload-free bootstrap, context/consent-scoped chat promotion and empty
booking-lineage promotion from later message, qualification and provider actions.
It specifies logical closure, guarded one-promotion/replay and honest lost-proof/
unknown-result handling. Its [bounded independent review](reviews/private-creation-boundary-v1-2026-10-05.md)
records PASS with no actionable findings for the exact additive proposal and
catalogue reference. The inspected [proof bytes](../../../output/research/private-creation-boundary-2026-10-05/PRIVATE_PROCESS_PROOF.md.reviewed.md)
and [catalogue bytes](../../../output/research/private-creation-boundary-2026-10-05/INTERFACE_CATALOG.md.reviewed.md)
are preserved; this later navigation edit is outside them. Prior receipts retain
their exact inputs. This freezes no JSON/status/identifier or numeric profile and
proves no handler, parser, persistence or concurrent behavior; integrated/founder
acceptance remains separate.

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

### Shared raw JSON boundary proposal — 2026-10-06

The [data contract's raw admission profile](DATA_CONTRACT.md#raw-json-admission-proposal--2026-10-06)
refines lexical decoding before directional validation and dispatch. It preserves
existing interface IDs, methods, paths, field authority and error variants.
Availability revision strings are not replaced by the common numeric helper.
Its native parser observations are not request-handler enforcement; per-interface
media/resource/numeric profiles, safe denial mapping, a proven framework integration
and actual HTTP/browser tests remain required before implementation or wire freeze.

The later [IF-BOOK-01 request encoding proposal](PRIVATE_PROCESS_PROOF.md#booking-creation-request-encoding-proposal--2026-10-06)
and [closed client schema](booking-creation-request.schema.json) have their own
[bounded independent review PASS](reviews/booking-creation-request-v1-2026-10-06.md).
They refine phase-only bootstrap and empty-lineage creation references, excluding
personal, consent, qualification and credential JSON. Server responses, transport,
expiry/work policies and actual admission remain held. This later navigation is
outside the receipt; chat, qualification and full Phase 1 authority remain separate.

The subsequent [booking creation transport/response profile](PRIVATE_PROCESS_PROOF.md#booking-creation-transport-and-response-profile-proposal--2026-10-06)
and [closed server projections](booking-creation-response.schema.json) now have
[bounded independent review PASS](reviews/booking-creation-http-v1-2026-10-06.md).
They refine this existing boundary's same-origin/media/raw input, separate
generation-bound bearer/CSRF transport, bootstrap/created/pending/safe-error
projections and finite proposed capacity/lifetime rules. Twenty-three actual
validator-boundary methods pass, not HTTP or distributed enforcement tests.
This ordinary reference does not claim the prior catalogue body was reviewed
anew or alter its fields/routes. The profile receipt names
its exact inputs, including the existing catalogue. Measured capacity, legal
class mapping, stable graph, actual mechanisms and integrated/founder acceptance
remain. Chat/qualification/email/provider/status protocols stay separate.

### Shared private browser decoding profile proposal — 2026-10-06

The [private browser JSON profile](DATA_CONTRACT.md#private-browser-json-admission-profile-proposal--2026-10-06)
refines raw admission for the explicitly listed existing visitor HTTP mutations
and availability commands. It proposes finite accepted-document/body/token
ceilings, strict UTF-8, recursive decoded-name duplicate rejection, exact numeric
admission, a standard-library-first candidate and redacted errors before effects.
It preserves stricter route limits and does not apply to public/worker payloads,
authoring, WebSocket events or callback ingress. No route, field, proof, grant,
consent, retention or response variant changes; independent review, exact ingress/
model wiring and resource/actual HTTP evidence remain required before implementation.

## Qualification admission and correction proposal — 2026-10-08

Status: DOING. Definition-only refinement of existing IF-BOOK-02,
`PATCH /api/v1/bookings/lineages/{lineage_id}/qualification`, under accepted
[BF-01A/B](../../phase-1-ux-architecture/FLOWS.md#bf-01a-qualification), the
[booking data boundary](DATA_CONTRACT.md#booking-and-provider-transactions),
[private-process authority](PRIVATE_PROCESS_PROOF.md#scope-and-recommendation)
and [purpose bindings](DATA_CONTRACT.md#record-purpose-retention-binding-proposal--2026-10-08).
It changes no route, required visitor question, budget policy, provider or
application. This proposal needs its own independent review and integrated/founder
acceptance; earlier receipts do not cover these appended bytes.

### Direction and permitted effect

The visitor proposes exactly the existing six data fields: email, organization,
role/job title, desired outcome, one matched canonical wing, and desired timing.
One separate versioned booking-purpose consent record is the seventh element.
Operation identity and expected server revision are protocol metadata, not
additional questions or visitor identity. The path selects an already-created
lineage; neither it nor that metadata grants access. Do not admit caller-supplied
verification, challenge, selected slot, staff assignment, calendar/meeting identity,
server time, proof generation, retention period or completed booking state.
Optional budget stays absent until its representation and meaning are approved.

Recommend one closed qualification-set command carrying all six values and the
separate consent decision, rather than a generic property merge or sparse field
patch. It modifies only the qualification portion of the existing lineage. The
client displays already-permitted values for correction/confirmation under BF-01A;
it does not make the visitor retype unchanged fields. This recommendation does
not create a qualification-read endpoint or broaden IF-BOOK-07's minimal status
projection. Exact authorized review/read delivery still needs a directional
contract; status alone cannot supply fields that it intentionally omits.

Server admission requires current own-lineage proof and CSRF, a permitted action,
current expected revision/state, the raw/closed input boundary, six valid values,
an eligible published canonical wing and exact current applicable notice/purpose
evidence. A route suggestion is not confirmation, and a wing key is not permission
to assign any staff member. Email syntax does not establish ownership; desired
timing is not a meeting instant or delivery promise. No scoring, minimum budget,
marketing permission, AI use, name, phone, upload or visitor account is inferred.
Use the separate proof, raw JSON and current consent boundaries; this appendix
does not invent an email validator, normalization rule, legal basis or credential.

Declining before submission returns to browsing/ephemeral help without sending
the personal qualification payload. If refused, missing, stale or inapplicable
consent nevertheless arrives, it cannot authorize retention or challenge issuance.
Stopping new admission is not a deletion claim: disposing of earlier lawfully
admitted data follows its independently applicable purpose/withdrawal policy.

### Atomic changes and correction fence

Validate the whole command before applying any proposed personal value. Under
the authoritative transaction/fence, recheck object authority, operation meaning,
expected revision, qualification state, notice/purpose eligibility and conflicting
intent. Apply the accepted value set, minimal permitted consent evidence, revision
change and dependent invalidations together. No reader or worker can observe new
email with old email verification, new qualification with old slot eligibility,
or partially replaced fields. Authorization/withdrawal and booking-intent admission
must serialize with this fence; a prior HTTP check cannot win that race by itself.

An initially invalid submission creates no retained lead/brief, qualified value
set or email challenge. Do not persist its supplied values in request logs,
analytics, validation diagnostics, retry queues, audit payloads or operation
fingerprints. Any allowed control/error accounting is minimal, non-payload and
subject to its own finite store/retention profile. If an already-valid qualification
is corrected unsuccessfully, leave the earlier record unchanged only while its
original purpose remains permitted; failure cannot renew consent or retention.
Valid draft values can remain in the open form under its approved privacy boundary,
without silent browser PII persistence. The UX's VALIDATION_ERROR describes rejected
input; it must not erase a previously admitted qualification or provider truth.

Before external booking-intent admission, a valid correction may replace the
qualification under current revision/purpose guards. A changed email atomically
advances its server email revision, invalidates all earlier challenges and verified
email authority, and clears dependent slot selection/eligibility in this lineage.
Any older challenge result must fail its current revision/purpose guard. Queued
delivery work not yet admitted to provider dispatch must recheck its bound email
revision/purpose and reject stale dispatch admission. Correction cannot recall
email already dispatched or stop delivery already admitted/in flight; those known
or unknown effects remain under IF-BOOK-03's delivery reconciliation before safe
retry/resend. Address correction alone is not proof of delivery failure. The old
challenge remains invalid even if that email arrives. Issuing a new challenge
remains IF-BOOK-03, not an incidental PATCH effect. The corrected qualification can
be QUALIFICATION_COMPLETE, never VERIFIED merely because its syntax is valid.
Resend is not this correction action.

An unchanged email cannot be silently treated as a newly verified email. Existing
verification is usable only if its exact email revision and applicable purpose/
challenge bindings remain current; any required invalidation wins. Other accepted
qualification changes invalidate an old selection's qualification/review binding
even when the address is unchanged. Require fresh eligibility and visitor review
before a later booking intent; no renewed verification lifetime or automatic
replacement slot follows. The exact unchanged-email state mapping and current
challenge/verification lifetime remain inputs to the later closed state/schema
profile. Do not infer that retaining a verifier permits keeping SLOT_SELECTED.

Once a calendar/meeting booking intent is admitted or its outcome is unresolved,
refuse qualification replacement until that intent's current authority has
established that replacement is safe under its approved state policy. A timeout,
expired lease, RECONCILIATION_ERROR or missing calendar/meeting provider read cannot
unlock correction. This fence concerns booking mutations, not verification-email
delivery. Before booking-intent admission, an otherwise authorized address
correction remains possible even while earlier verification delivery is unknown;
the current challenge is invalidated, and delivery reconciliation/retry rules
remain separate. An old email delivery cannot become a permanent correction lock.
Neither confirmed bookings nor reschedule/cancel transitions are
rewritten by this endpoint. Their separately reviewed actions retain last confirmed
truth and the accepted lineage. No automatic cancellation, attendee change, second
meeting, new lineage or external retry is created by correcting this form.

### Replay, projection and visitor recovery

Scope operation identity to the authorized lineage and qualification action.
Bind it to the immutable admitted meaning, including the expected revision, all
six proposed values and applicable consent evidence. Changed meaning under the
same identity conflicts; a new identity cannot bypass the revision/intent fence.
The exact privacy-safe binding/store representation remains to be selected: a
plain hash of personal input is not automatically anonymous or retention-free.
Do not retain rejected personal input merely to implement duplicate detection.

For an already-admitted matching operation, reconcile the recorded outcome under
current object/disclosure authority before considering a fresh mutation. Its
original expected revision is not a fresh-write permission, and the revision
advanced by its own application is not a reason to apply it again. A receipt must
distinguish that earlier application from a current eligible qualification;
subsequent correction, withdrawal, expiry or booking progress can make its earlier
state inapplicable. Replay cannot restore earlier values, proof, consent, email
verification, slot eligibility or retention. If the binding/outcome is unavailable,
preserve uncertainty and deny a fresh mutation; do not claim no earlier effect.

The logical server result separates applied, rejected/conflicting, and unresolved
outcomes. An authorized applied receipt needs only the scoped operation reference
and applied revision; any current lineage state is a separately guarded snapshot,
not an assertion that the earlier revision remains current. No raw qualification,
email, consent text, bearer/CSRF, challenge, staff/provider detail or arbitrary
exception text is echoed. Safe validation feedback names only the allowlisted six
field keys or separate consent element and fixed reason categories, with no
submitted value. Object denial reveals no private existence or previous validity.
Exact JSON/status/error variants and finite response limits remain to be frozen;
do not borrow IF-BOOK-01/07's different projections as this route's complete schema.

A timeout, lost/malformed response or unresolved result means completion is unknown.
Keep the same initiating UI intent and reconcile it only under current authority.
IF-BOOK-07 can show permitted current lineage status; its state/revision alone cannot
prove which operation applied. Do not guess success from QUALIFICATION_COMPLETE,
repeat external work, overwrite a newer command, or allocate a replacement lineage.
The qualified intent itself sends no email and creates no calendar record. The
reviewed operation-result protocol must expose a safe same-intent reconciliation
mechanism at the existing boundary before implementation; this appendix adds no
new recovery endpoint. Until that contract exists, show honest uncertainty/Contact.

Preserve BF-01A's linked textual errors, associated labels and already-supplied
valid-value recovery. A permission/consent conflict is not an invitation to keep
retrying. Lost permitted form state needs truthful recovery rather than reconstructing
personal values from unauthorized logs or browser storage. Cross-stream changes
cannot bypass any admission or privacy gate.

### Primary support, validation scope and remaining wire definition

[RFC 5789 section 2](https://www.rfc-editor.org/rfc/rfc5789.html#section-2)
supports atomic application of PATCH changes and collision-aware admission; it
does not make PATCH inherently idempotent or select Hengshi's command format.
[RFC 9110 section 13.1.1](https://www.rfc-editor.org/rfc/rfc9110.html#section-13.1.1)
describes If-Match lost-update protection, but does not select it over an explicit
expected-revision command here. Do not claim that a numeric field implements HTTP
conditional semantics. These are primary references checked 2026-10-08, not a
new library/provider selection or implementation proof.

[JSON Schema 2020-12 validation](https://json-schema.org/draft/2020-12/json-schema-validation#section-7)
and the [jsonschema FAQ](https://python-jsonschema.readthedocs.io/en/stable/faq/#my-schema-specifies-format-validation-why-do-invalid-instances-seem-valid)
separate format assertion from annotation. Context7's `/python-jsonschema/jsonschema`
documentation was consulted: a declared email format alone supplies neither
asserted complete address validation nor mailbox ownership. No new dependency or
schema test is added for this prose/control definition.

Next wire-definition inputs are exact directional request/result/error schemas;
email internationalization/normalization and delivery capability; bounded Unicode
text and desired-timing representation; current notice/purpose mapping; unchanged-
email state transitions; operation admission/reconciliation/retention mechanisms;
and finite media, raw byte, receive/work, response, header and cleanup profiles.
The shared decoder's maxima are ceilings, not a complete route profile. Exact
review/read delivery, provider/challenge bindings, accessibility/load/runtime tests
and integrated/founder acceptance remain. Later tests must exercise actual request,
transaction, concurrent correction/verification/booking/withdrawal, denial and
recovery boundaries; documentation wording checks cannot prove those outcomes.

## Qualification wire profile proposal — 2026-10-08

Status: DOING. This refines the preceding IF-BOOK-02 control proposal with the
[closed directional module](booking-qualification.schema.json). It preserves
the earlier reviewed catalogue prefix; that receipt covers its thirteen frozen
inputs, not these new bytes. It
retains the existing PATCH path, six required fields and separate noticed consent.
All new bounds/form representations are reversible, unmeasured engineering
proposals requiring independent review and integrated/founder acceptance. No
application, dependency, provider, proof policy or production form is implemented.

### Closed submission, timing and mailbox representation

Reference the module's `request` definition, never its rejecting root. Two closed
commands share the existing own-lineage PATCH boundary:

| Command | Exact client body | Permitted effect |
|---|---|---|
| `set_qualification` | `kind`, CSPRNG UUIDv4 `operation_id`, positive `expected_revision`, closed `qualification` and separate `consent`. | One guarded complete qualification set, subject to all current admission/correction gates. |
| `reconcile_qualification` | `kind` and the same scoped `operation_id` only. | Read the earlier admitted operation's permitted outcome; no new value set, consent, mutation, challenge, calendar action or renewal. |

Qualification contains exactly email, organization, role, desired_outcome,
wing_key and timing. The proposed timing representation is one closed object
with `description`: bounded free text expressing desired project timing, including
uncertainty. It adds no date bands, required deadline, slot instant, duration,
timezone, price or delivery commitment. Protocol metadata is not another question.
Optional budget remains absent until separately approved.

| Field | Proposed decoded Unicode-scalar limit |
|---|---:|
| email | 1–320; shape only, with the additional mailbox validation below |
| organization / role | 1–200 each |
| desired_outcome | 1–2,000 |
| timing.description | 1–500 |

Non-email text requires at least one code point outside Unicode 17's White_Space
property. Preserve entered text; do not silently truncate, transliterate, trim,
apply compatibility normalization or turn it into executable HTML/markdown.
These are code-point limits, not UTF-8 bytes, UTF-16 units or visible graphemes;
the raw body limit still wins, including escaped input. The shared raw admission
profile rejects invalid scalar sequences before schema validation. Any later
rendering uses the independently approved safe text/accessibility boundary.
`wing_key` reuses the existing five canonical keys, with current published
eligibility checked separately. The separate consent object reuses the noticed
decision shape but admits only `grant`; its purpose must be the approved current
booking purpose, not an arbitrary syntactically valid or chat-specific key.
Refusal is a no-personal-payload UI exit, not a second qualification command.
Exact notice, lawful basis, copy and purpose bindings remain required.

Recommend validating a plain mailbox through the existing email-validator family,
not a handwritten regex or Pydantic `EmailStr` alone. The observed installed and
registry stable version is 2.3.0, already in the backend candidate inventory; it
is not a selected complete production graph. Candidate options are explicitly
`check_deliverability=False`, `allow_display_name=False`,
`allow_quoted_local=False`, `allow_domain_literal=False`,
`allow_empty_local=False`, `allow_smtputf8=True`, `strict=True`,
`test_environment=False`. Reject surrounding whitespace rather than quietly
stripping it. No request-time DNS/SMTP lookup or mail dispatch follows. The
normal form is compared only inside this authorized lineage. Preserve ordinary
local-part case and plus tags, with the candidate library's explicit exception:
its RFC 2142 reserved mailbox names are normalized to lowercase (for example,
`POSTMASTER@example.org` becomes `postmaster@example.org`). The installed
`CASE_INSENSITIVE_MAILBOX_NAMES` set and normalization branch define this
bounded exception; [RFC 2142 section 2](https://www.rfc-editor.org/rfc/rfc2142.html#section-2)
specifies case-independent recognition of these well-known names. Do not add
provider-specific mailbox alias rules, drop plus tags, lowercase every
customer local part or join people/histories by email. Do not retain an extra
raw spelling by default.
Binding an operation to its received typed values remains distinct from storing
the validated normalized mailbox.

Non-ASCII domains and local parts require separately verified delivery capability.
A syntax result's SMTPUTF8 indication is not an entitlement or deliverability
promise. Until the eventual adapter capability is verified, do not issue a
challenge that requires it, silently rewrite the mailbox, or invent an ASCII-only
customer policy. Capability refusal remains truthful Book/Contact recovery at
the email boundary. Exact adapter submission, supported forms and account/API
binding remain held; no mail provider is selected by this candidate profile.
The JSON Schema deliberately has no email-format assertion: a bounded non-address
can pass shape, so server mailbox validation is mandatory before application.

### Admission ordering, state mapping and same-intent recovery

After method/media/raw decoding, recognizable command-metadata and current
proof/CSRF/action gates, look for the
scoped admitted operation before treating an old expected revision as a fresh
write. For an existing operation, compare the complete received typed intent under
the permitted private binding: all six values, expected revision and consent
reference/decision. JSON property order/insignificant syntax whitespace does not
change typed meaning; changed scalar spellings do, even if mailbox normalization
would yield the same address. Matching replay reconciles only; changed meaning
conflicts without echoing or retaining rejected input. Current disclosure/purpose
denial can suppress a historical receipt. If its binding/outcome cannot be safely
established, return uncertainty, never apply a new command.

For a new set, check the current expected revision, valid normalized mailbox,
six-field validity, wing/notice/purpose eligibility and booking-intent fence.
Under the same atomic authority, apply the complete permitted set, minimal consent
evidence and dependent invalidations; advance lineage revision once for this new
guarded admission. Matching replay does not advance it. Exhaustion of the safe
integer revision range refuses before effects, never resets/reuses a revision.
This advance grants no new access, challenge validity or retention period.
Invalid input retains no lead/qualification payload or personal operation binding.

The proposed post-application mapping is evaluated from current authoritative
state under that fence, not from a browser's claimed state:

| Current conditions before a permitted new set | Resulting booking state |
|---|---|
| No still-applicable challenge/verified authority, including changed normalized email or invalidated purpose binding | QUALIFICATION_COMPLETE; all old challenge/verification and selection authority rejected. |
| Same normalized email and still-applicable challenge/purpose binding, no verified authority | Preserve the truthful current EMAIL_PENDING, EMAIL_EXPIRED or EMAIL_UNDELIVERABLE branch as applicable; no dispatch or freshness extension. |
| Same normalized email and still-valid current verified authority | VERIFIED; clear the old selection/review and stale no-availability result. Fresh availability/selection/review is required before booking. |
| Admitted or unresolved calendar/meeting mutation, confirmed occurrence or reschedule/cancel phase | Refuse replacement under the preceding booking-intent fence; preserve reconciled truth. |

Challenge/verification applicability includes exact email revision, purpose,
revocation and expiry. An expired challenge record can support an EMAIL_EXPIRED
display but never verification or slots. Unknown/inconsistent authority does not
fall through to a convenient successful branch: refuse and reconcile it. Exact
challenge/verification lifetimes and delivery mechanisms remain in IF-BOOK-03/04.
Previously dispatched email may still arrive; its old challenge remains invalid.
The field-set operation itself issues no challenge or calendar intent.

Reconciliation sends no qualification/consent again and allocates no operation.
An applied historical receipt says only which revision this operation applied;
IF-BOOK-07 separately reads current state. A newer revision, withdrawal or expiry
cannot be overwritten by replay. A missing row alone is not proof that an earlier
request never ran: a still-running/uncertain writer or lost binding may exist.
Without authoritative matching applied/pending knowledge, return safe unavailable
and retain uncertainty; do not reuse the operation ID for a fresh write or mint a
new lineage to evade it. Reconciliation/polling renews no idle/absolute access,
consent, challenge, retention or worker lease.

### Minimal results, errors and finite starting profile

Reference `response`; requests and responses are different closed shapes.
All application JSON is UTF-8, `application/json`, `Cache-Control: no-store`,
at most 1,024 emitted bytes, without credential CORS or input/exception echo.
Current own-object authority is checked before disclosing operation references,
applied revisions, field validation or conflicts. Unauthorized paths use one
ACCESS_UNAVAILABLE projection, without object-existence or earlier-validity detail.

| Outcome | HTTP | Closed meaning |
|---|---:|---|
| Applied or authorized matching replay | 200 | `state=applied`, own `operation_id`, historical `applied_revision`; no current-state or verification/booking assertion. |
| Known admitted operation whose application is unresolved | 202 | `state=pending`, own `operation_id`; no completed revision or absence-of-effect claim. |
| Authorized new set fails qualification/notice validation before application | 422 | `state=rejected`, INVALID_QUALIFICATION, `recovery=correct_request`, nonempty `errors` map containing only six field keys and/or consent, each with its closed fixed reason. No submitted value or operation echo. |
| Raw syntax, unknown command/properties or malformed protocol metadata | 400 | INVALID_REQUEST / correct_request. |
| Missing/expired/revoked/wrong-object proof | 404 | ACCESS_UNAVAILABLE / contact; do not distinguish existence. |
| Current object authority but action/CSRF denied | 403 | ACTION_DENIED / contact. |
| Current expected revision or booking state disallows new set | 409 | REVISION_CONFLICT or STATE_CONFLICT / refresh_status; no new mutation. |
| Existing operation has changed typed meaning | 409 | OPERATION_CONFLICT / reconcile. |
| Finite admission exhausted | 503 | CAPACITY_LIMIT / wait; does not deny earlier effects. |
| Outcome/store/binding unavailable or not provable | 503 | SERVICE_UNAVAILABLE / reconcile; preserve uncertainty. |
| Raw body/media/header refused | 413 / 415 / 431 | BODY_TOO_LARGE / UNSUPPORTED_MEDIA / HEADER_TOO_LARGE, each correct_request. |

Unavailable errors contain exactly `state=unavailable`, fixed code and recovery.
Rejected field feedback is available only for a fresh authorized set that has not
been admitted, not as a retrospective no-effect result for an uncertain operation.
For a recognizable new set, missing/invalid known qualification fields or consent
are mapped to the fixed 422 field feedback only after current object authority
and existing-operation checks. A schema failure by itself does not select 400;
unknown members/malformed protocol and known field-value failures have different
classifications. A changed existing intent conflicts instead of claiming that
its earlier application was rejected. Without current object authority, no field
feedback or private conflict detail is disclosed.
Reconcile returns only applied, pending or safe unavailable; never invented
validation feedback from discarded rejected payloads. HTTP correlations, this
command/result pairing and current authority are semantic checks beyond schema.
Localize fixed reasons in the approved UI, associating errors with fields/summary;
do not surface raw library messages. A transport termination/bodyless ingress
error is neither a successful JSON result nor proof that no earlier effect exists.

Use the existing same-origin HTTPS browser proof/CSRF and strict JSON admission
rules. Accept only application/json with absent or single UTF-8 charset and absent
or identity Content-Encoding; no form, alternate encoding, media defaults,
duplicate names, coercion, malformed Unicode or permissive credential origin.
Propose received-body caps of 16,384 bytes for set and 1,024 for reconcile, checked
across actual chunks, with the common lower nesting/string/node limits retained.
Before kind is known, the 16,384 maximum cannot be exceeded; after decoding the
stricter reconcile byte ceiling still applies. Headers/Cookie limits retain the
existing private profile's 16,384 aggregate / 8,192 Cookie-value bytes. Propose a
five-second receive deadline and ten-second observation deadline; observation
timeout never abandons admitted work or decides its outcome.

Propose service-wide limits of 48 admitted receive/set jobs and 16 receive/reconcile
jobs, counting draining/uncertain work until known cleanup, without a hidden queue.
Reserve no personal operation record before all admission/legal gates. At most
16 unsettled/replay-protection operation records per lineage and 4,096 across the
service may remain; at capacity refuse new set before effects, keeping permitted
reconciliation available. Retain the admitted outcome and necessary private
binding throughout the current purpose/expiry-permitted reconciliation window,
so an authorized visitor can recover a lost acknowledgement. An applied write
makes its expected revision stale immediately; that alone cannot retire its
receipt. Receipt retirement is separate from non-reexecution suppression:
retire only when the lawful reconciliation window ends, retaining the minimum
necessary suppression while an old intent could otherwise be admitted again.
Expired or revoked authority cannot retrieve or restore a receipt. Store
cleanup cannot forget unresolved ambiguity, reset revisions, renew access or
reexecute an old intent; it also cannot create indefinite personal history.
Each outcome/binding/copy inherits its approved purpose/expiry; hashes are not
automatically anonymous. Finite
mechanisms, ingress buffering, multiworker fencing, clock/cleanup integration and
actual load qualification remain required; these counts are not measured capacity.

### Primary evidence and limits

Checked 2026-10-08: Context7 `/pydantic/pydantic` and official
[Pydantic network types](https://pydantic.dev/docs/validation/latest/api/pydantic/networks/),
[email-validator documentation](https://github.com/JoshData/python-email-validator),
[PyPI metadata](https://pypi.org/pypi/email-validator/json),
[SMTPUTF8 RFC 6531](https://www.rfc-editor.org/rfc/rfc6531.html#section-3.2)
and [Unicode 17 White_Space data](https://www.unicode.org/Public/17.0.0/ucd/PropList.txt).
The [read-only native observations](../../../output/research/booking-qualification-wire-2026-10-08/email-observations.json)
preserve ten public-synthetic syntax/normalization cases with DNS delivery disabled,
installed source hashes, registry requirements and explicit options. This is neither
complete international address conformance nor actual API/provider enforcement.
No library install, runtime/lock change, outbound delivery or full graph selection.

Schema fixtures exercise only the module/validator boundary. They cannot prove
mailbox syntax, scalar-safe raw decoding, consent, atomicity, current state,
operation-result correlation, HTTP, provider or browser enforcement. Exact notice/
basis, adapter capability, allowed purpose/read projections, proven bindings/store/
fences/cleanup, wire freeze, load/accessibility/runtime and integrated/founder
acceptance remain. Earlier control/schema PASS scopes are not broadened by this
later profile; its own independent review and adoption are required.

## Email ownership control proposal — 2026-10-08

Status: DOING. This completes the logical control profile for existing
IF-BOOK-03 (`POST /api/v1/bookings/lineages/{lineage_id}/email-challenges`)
and IF-BOOK-04 (`POST /api/v1/bookings/lineages/{lineage_id}/email-verification`).
It refines [BF-01B](../../phase-1-ux-architecture/FLOWS.md#bf-01b-email-ownership),
[booking data](DATA_CONTRACT.md#booking-and-provider-transactions) and the
[private-process boundary](PRIVATE_PROCESS_PROOF.md#scope-and-recommendation).
These are concrete engineering recommendations for integrated/founder acceptance,
not implemented controls or a new mail/account/provider entitlement. Earlier
receipts apply only to their preserved inputs. Wire schemas/HTTP envelopes remain
a subsequent representation task; this profile fixes their required semantics.

### Method and accessible interaction

Recommend a single-use, uniformly random eight-ASCII-digit confirmation code
sent to the currently qualified normalized mailbox. Use `secrets.randbelow(10**8)`
and zero-pad to eight digits; leading zeroes are significant. The code confirms
access to that mailbox for this booking lineage only. It creates no visitor
account, staff login, general identity assurance, process cookie, calendar access
or permission to inspect another lineage. In particular, email confirmation is
not Entra authentication or staff MFA. NIST's email-address confirmation distinction
supports this separation; it does not certify this design or select its limits.

Use one labeled text input, `inputmode=numeric`, `autocomplete=one-time-code`,
and an explicit Verify action. Permit whole-code paste and user-agent filling;
do not use eight independent boxes, numeric coercion, disabled paste, puzzles,
automatic submission or unaided memorization/transcription requirements. Email
plain text and HTML present the same contiguous eight digits, purpose, expiry
and a warning not to share the code. The email contains no qualification brief,
staff/personal identity, process proof, CSRF secret, tracking pixel or verification
URL. Copying a code must work with keyboard and assistive technology. Opening,
previewing or scanning email cannot perform verification.

Return to the existing authorized booking form; a new browser/device with only
the email code cannot recover or transfer the process. Reading email on a second
device and copying the code into the original process is allowed. Loss of the
original process uses its approved recovery/Contact boundary; do not disclose
historical data or mint a process proof from mailbox possession. Display no
masked address by default; authorized qualification review supplies the existing
permitted field under its own forthcoming projection, not this response.

The code's representation is exactly eight ASCII digits; whitespace, signs,
separators, Unicode lookalike digits and integer JSON values are invalid. UI may
explain the expected form but does not silently rewrite submitted secrets. Invalid
syntax is not a cryptographic comparison, although its bounded request/abuse
accounting still applies. Invalid, stale, exhausted, superseded and foreign
challenge submissions receive the same non-verifying recovery category after
current object authority; no code value, mailbox membership or remaining guess
count is returned. Access denial precedes these object-specific outcomes.

### Challenge identity, verifier and clocks

The server allocates a UUIDv4 challenge reference with CSPRNG bits and binds it to
the booking process, lineage, current email revision, applicable notice/purpose,
issue operation and code verifier. The reference is not a bearer credential.
Mutable lineage revision and email revision are distinct: a permitted non-email
qualification correction does not make the current code valid for another email
or silently extend its life. No client supplies those server bindings.

Recommend a 600-second code window from the atomic challenge admission, never
from mail acknowledgement or browser receipt. No provider claim resets it.
For timing accessibility, warn with at least 60 seconds remaining and provide
explicit More time with at least 20 seconds to act. Recommend up to ten extensions
of 600 seconds for the same still-valid challenge, without new mail, new code,
reset guesses or automatic continuation. Each extension checks current own proof and CSRF/action authority, then reconciles
matching admitted operations before fresh-work guards. For a fresh extension,
require expected lineage revision to equal current revision, and recheck eligible
state, challenge/purpose/email bindings and extension count under the same fence.
A stale fresh command conflicts before counters, time changes or any effect.
Each committed extension advances the lineage revision once; concurrent duplicates
for the same operation extend once. No extension after
expiry, use, invalidation, withdrawal or loss of process authority; offer permitted
fresh issuance or Contact instead. This bounds the challenge to at most 6,600
seconds from original admission and supplies the ten-extension timing route;
it does not claim complete WCAG conformance. The exact More time representation
belongs to IF-BOOK-03, not a new endpoint or extra qualification question.

Successful verification is usable only in that same currently authorized
booking process, with its email revision and applicable purpose still current.
This profile adds no separate verification-freshness timer. The owning process's
reviewed expiry/accessible continuation governs access; verification, status reads
or email receipt do not renew that access or consent. A new or recovered process
cannot inherit this verification. Before booking-intent admission, losing current
process/email/purpose authority disables new slots and invalidates selection/review
eligibility. After calendar/meeting intent admission, loss of this authority cannot
erase confirmed truth, reexecute provider work or unlock qualification correction.
Reschedule/cancel retain their separate authorization rules. Retained historical
verification is purpose-permitted evidence only, never a grant to another process.
D-076's conversation inactivity and staff-session clocks remain separate.

Store a keyed HMAC-SHA-256 verifier rather than a plain/unkeyed short-code hash.
Recommend a separately managed 32-byte CSPRNG key, explicit key identifier, and
an unambiguous domain-separated length-prefixed message containing the action
family, process/lineage/challenge references, email revision and eight code bytes.
Compare equal-length digest bytes with `hmac.compare_digest`; ordinary equality
and fast offline enumeration of an unkeyed eight-digit hash are unsuitable.
The key stays outside the record store, source, snapshots, logs and public output.
Retain the appropriate key only through the governed active-verifier window;
an unavailable or revoked key denies verification, never bypasses it. Key creation,
storage, rotation/restore arrangements and credential changes require their later
applicable approvals. This recommendation does not change staff JWT/bcrypt.

Delivery needs the code transiently. Its encrypted, purpose-mapped outbox copy
uses separately managed encryption authority; HMAC is not reversible encryption.
Only the guarded delivery worker may decrypt for the approved adapter. No secret
is retained in diagnostics, analytics, operation fingerprints or browser storage.
Remove delivery secret material when its permitted need ends; retained delivery
evidence contains no code. Unknown delivery cannot justify indefinite plaintext
or an expired verifier; expiry and unresolved-effect evidence are separate clocks.
The provider's own copies and retention require MA-006/privacy assessment.

### Issuance, resend and uncertain delivery

IF-BOOK-03 has four closed logical commands: issue, explicitly resend, extend the
current challenge, and reconcile an already-admitted issue/resend/extension.
Mutating commands carry their own UUIDv4 operation identity and expected lineage
revision; reconciliation carries only the scoped earlier operation identity.
Resend/extend also identify the current server challenge. No client-supplied email,
code, delivery state, provider identity or verified flag is admitted here. The
mailbox comes from the current valid qualification. Issue applies only when this
current email revision has no earlier challenge; subsequent replacement uses
explicit resend of its most recent challenge, including one expired or exhausted.
A different operation cannot issue beside an existing challenge to bypass resend.
Reconciliation sends no code
or personal payload and creates no new operation, mail or renewal.

Current own-process proof, CSRF/action authority, valid complete qualification,
current applicable consent/purpose, supported mailbox delivery form and the atomic
revision/state guard are required before issuance. Refuse issue/resend once a
calendar/meeting intent is admitted; their uncertainty is not an email retry cue.
Current matching replay lookup precedes stale expected revision for fresh work:
the same immutable command returns its still-permitted historical outcome without
new code, mail, attempt counter or extension. Changed input under that operation
conflicts. Outcome/binding remains recoverable throughout its permitted window,
independent of the expected revision becoming stale after admission.

Issue is eligible in QUALIFICATION_COMPLETE with no earlier challenge for the
current email revision. Explicit resend may replace the most recent challenge in
QUALIFICATION_COMPLETE, EMAIL_PENDING, EMAIL_EXPIRED, EMAIL_UNDELIVERABLE, VERIFIED
or SLOT_SELECTED, only before any calendar/meeting intent and with all current
admission/revision/purpose guards. It is deliberate re-verification, not an
automatic side effect of refresh. No other state admits either mutation.
Atomically admit the new challenge, invalidate every earlier challenge/verifier,
revoke existing verified-email authority and clear all dependent availability,
selection, review and no-availability eligibility, reserve delivery/abuse budget,
record its operation result
and durable delivery intent, and advance the lineage once to EMAIL_PENDING. Refusal
or known pre-commit failure does none of these. Dispatch only after commit. The
worker rechecks current purpose/email/challenge/expiry and exclusive dispatch
authority immediately before external admission. Stale queued work is suppressed;
already-dispatched or in-flight email cannot be recalled by invalidation.

Track delivery separately as queued, submission_pending, submitted, definitely_not_sent
or delivery_unknown. An adapter acceptance proves submission, not inbox arrival,
reader access or email verification. Enter definitely_not_sent only from authoritative
evidence excluding external submission; local timeout, lease expiry or missing
provider record alone do not establish it. Worker crash/ambiguous adapter response
retains delivery_unknown, fences duplicate dispatch and requires authoritative
adapter reconciliation before safe retry. Retry, where demonstrably safe, preserves
the original intent/code/expiry and does not allocate a challenge or reset a clock.
If the chosen adapter cannot reconcile an uncertain submission, that retry remains
unavailable with honest recovery; no claim of exactly-once external mail follows.

Explicit resend allocates a distinct current challenge/code only after the previous
same-mailbox delivery intent is terminal and applicable budgets permit it; it never
reuses or reactivates the old verifier. A terminal submission may still arrive late;
the old code remains invalid. Unknown old delivery is not definite failure and
cannot be bypassed with a new operation, tab, proof rotation or new lineage for the
same intent. A separately permitted address correction can proceed under IF-BOOK-02
while old delivery is unknown; it invalidates the old challenge but cannot claim
to cancel that email. Issuance to the corrected address is a new current-email
intent, not a retry of the uncertain old one; keep its independent evidence and
purpose/capacity guards. Do not let unknown obsolete delivery lock correction forever.

EMAIL_PENDING describes a pending challenge, never verified or a mail delivery
promise. EMAIL_UNDELIVERABLE requires a current definitely-not-sent refusal supported
by the adapter; EMAIL_EXPIRED requires actual current challenge expiry. Superseded
late callbacks cannot change the current challenge/state. Unknown submission can
coexist with expiry/invalidation; retain the necessary uncertainty evidence without
asserting that expired email was not sent. The public result gives only current
permitted challenge reference, expiry/extension affordance and a fixed safe state;
provider IDs, raw errors, code, verifier and address are absent.

### Verification admission and concurrent effects

IF-BOOK-04 has verify and reconcile logical variants. Verify carries operation ID,
expected lineage revision, challenge reference and the exact eight-digit code;
reconcile sends only the earlier scoped operation ID. Bind retry semantics to the
received typed values without persisting the code: use separately keyed intent
binding with length framing, never a raw/unkeyed code fingerprint. Bindings inherit
the operation's purpose/expiry and cannot form a mailbox/history index.

First check current process/CSRF/action authority and reconcile matching admitted
operation intent/results. For fresh Verify, require expected lineage revision to
equal current revision and recheck eligible EMAIL_PENDING state, current
qualification/purpose/email binding, challenge validity and attempt budget.
Reject a stale fresh command before comparison, guess reservation or any effect.
Fresh verifies compare and consume under the same transaction/fence as correction,
withdrawal, resend, extensions and booking admission. A successful match consumes
the challenge once, records verification against the current email revision and
purpose/process, clears stale selection/review, records the immutable operation
result and advances lineage once to VERIFIED. It grants only current eligibility
for the separately guarded availability/selection stages, not a calendar booking.

Each fresh well-shaped comparison atomically reserves a guess; duplicates of the
same admitted operation do not compare or count again. Recommend at most five
comparisons per challenge, shared across tabs/workers. Five wrong comparisons
invalidate that challenge, clear dependent eligibility and return to
QUALIFICATION_COMPLETE with one lineage revision advance; do not mislabel guess
exhaustion as time expiry or definite mail failure. Earlier wrong comparisons record
only their bounded private counter/result and leave lineage state/revision unchanged.
The fifth correct comparison can succeed if its complete
authority remains current. A stale/wrong-reference request cannot decrement a
different challenge's counter. A competing success/replacement/end wins through
serialization; no second verification or stale-code promotion can be committed.

Lost acknowledgement is reconciled under current own authority. A matching old
success is a historical applied result, not assurance that verification is still
current; IF-BOOK-07 remains the current-status boundary. A wrong-code operation
has a recoverable fixed rejected outcome, without echoing code or remaining guesses.
If a current-authority reconciliation cannot prove the outcome, return pending or
unavailable and preserve ambiguity; never compare again from a missing receipt.
Read/reconcile/invalid code alone does not renew process access, purpose, verified
freshness or challenge expiry. Only separately eligible admitted activity may
affect the owning process's existing idle policy.

### Abuse, finite work and failure qualification

The eight-digit space has 100,000,000 possibilities (about 26.6 bits), so expiry
and per-challenge limits alone are insufficient. Propose a shared rolling budget
of five issue/resend admissions per process and normalized destination per hour,
and ten per destination per 24 hours, with at least 60 seconds between mail intents
for that destination. A new lineage/proof/email spelling cannot reset destination
budgets; reuse the reviewed mailbox normalization without provider alias guessing.
Track destination controls by a keyed, purpose-mapped digest, not public email
lookup or a permanent user profile. Their finite window/copy cleanup must be
approved under the abuse-purpose mapping before real data is stored.

Propose at most 25 fresh verification comparisons per process and normalized
destination per rolling hour, shared across replacement challenges/workers, plus
the five-comparison challenge cap. Reserve counters atomically before comparison/
send admission; rollback only a proven pre-effect cancellation, never ambiguous
work. More time and replay never reset these counters or create another mail intent.
Provider/limiter/key/clock/store uncertainty refuses new sensitive action; retain
permitted status/reconciliation and public Contact without guessing delivery or
verifying. Infrastructure-wide finite ingress/work limits from the existing private
profile also apply. Exact distributed store/key/expiry implementation is a later
engineering task, not a hidden in-memory counter or a selected Redis deployment.

These numerical budgets are unmeasured proposals, not a response SLA, defence
against all distributed abuse or NIST assurance-level claim. Network/service abuse
controls must complement them without storing browsing/movement histories or
permanently locking a customer mailbox. Capacity or retry guidance reveals no
membership, other-lineage state, provider internals or counter totals.

Later implementation qualification must exercise real transaction/worker boundaries:
simultaneous correct/wrong guesses; duplicate operations and changed code;
same-email qualification correction and changed-email invalidation; expiry at the
comparison/dispatch fence; More time versus expiry/use/End; 11th extension refusal;
new lineage/tab/worker limiter bypass; exactly one local consume and no duplicated
uncertain mail dispatch; known refusal versus ambiguous provider acknowledgement;
late obsolete email/callback; loss of verification authority before and after booking intent;
lost responses; withdrawal/deletion/restore; unavailable limiter/key/clock/store;
no secret leakage; full-code paste/autofill/leading-zero behavior, focus/errors,
timing warning/extension and screen-reader/mobile equivalence. Synthetic fixtures
are allowed locally; mocks or schema shape alone cannot prove these outcomes.

### Primary sources and acceptance boundary

Checked 2026-10-08: Context7 `/python/cpython`, official
[Python secrets](https://docs.python.org/3/library/secrets.html) and
[HMAC](https://docs.python.org/3/library/hmac.html) APIs; these support the standard
library primitives, not selection of a complete production Python graph.
[OWASP code/token guidance](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
informs randomness, secure storage, single use, expiry and abuse controls by analogy;
Hengshi's flow is email confirmation, not password recovery.
[NIST's email-confirmation distinction](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/)
separates this purpose from out-of-band authentication.
[W3C accessible authentication](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html)
and [timing adjustment](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html)
inform paste/filling and the explicit extension path; no unsupported essential-time
exception or blanket accessibility pass is asserted.

The eight-digit method, clocks, keyed verifiers, delivery state split and budgets
are this proposal's choices, not numerical prescriptions from those sources.
Independent control review and integrated/founder acceptance remain required.
Wire/HTTP representation, the authorized qualification-review projection, exact
purpose/notice/copy policy, MA-006 adapter/account capability, secret management,
distributed persistence and runtime/UI qualification remain tracked obligations.
No source/lock/provider/account/credential/deployment change is authorized here.

## Email ownership wire proposal — 2026-10-08

Status: DOING. The [directional module](booking-email.schema.json) supplies the
two existing email boundaries' proposed representations. The preceding control
profile and its [correction-1 review](../../../output/research/booking-email-ownership-2026-10-08/final-independent-review.json)
retain their preserved input scope; this appended wire proposal needs its own
review and integrated/founder acceptance. It changes no route, account, mail
provider, process proof, code method, counter or clock. No handler is implemented.

### Direction, correlation and current controls

The module root rejects all instances. Consumers register all local referenced
modules and reference the named directional definitions. Validate raw scalar/closed
JSON separately; schema does not establish authority, raw integer-token spelling,
single use, freshness or capacity. No network schema resolution is permitted.

| Boundary | Client command | Exact required body members |
|---|---|---|
| IF-BOOK-03 challenge_request | issue_challenge | kind, operation_id, expected_revision |
| IF-BOOK-03 challenge_request | resend_challenge / extend_challenge | kind, operation_id, expected_revision, challenge_ref |
| IF-BOOK-03 challenge_request | reconcile_challenge | kind, operation_id only |
| IF-BOOK-04 verification_request | verify_email | kind, operation_id, expected_revision, challenge_ref, code |
| IF-BOOK-04 verification_request | reconcile_verification | kind, operation_id only |

All operation and challenge references reuse the already proposed lowercase
CSPRNG UUIDv4 shape; revisions reuse the positive binary64-safe integer range.
Only the current server-issued challenge has authority after all guards. Codes
are strings of exactly eight ASCII digits, including leading zeroes; numbers,
lookalikes, whitespace and separators are rejected. Neither request accepts email,
qualification, consent, verified flag, expiry, extension amount, server counter,
proof/CSRF material or provider identity in JSON. Proof/CSRF remains in its approved
transport. The path selects the already-authorized lineage, not a transferable
credential. Reconciliation never sends the code or repeats a mutating command.

IF-BOOK-03's applied result contains state=applied, operation_id, historical
applied_revision and a separate current control projection. Pending contains
state=pending, operation_id and the same separate projection; it has no applied
revision. Neither receipt says submitted, delivered, verified or booked. Applied
means the local challenge/extension intent was committed; mail submission can
still be uncertain. Pending means operation application is uncertain, not that
an email or appointment was sent. No missing receipt can be inferred as no effect.

The projection is either exactly `{state:unavailable}`, with no facts/affordances,
or `{state:known, revision, challenge}` read under current own-process, purpose
and guarded lineage authority. Challenge is exactly one of:

- `{state:none}` when the current email revision has no allocated challenge;
- `{state:inactive, challenge_ref}` for its most recent allocated but currently
  ineligible/consumed/expired/exhausted/superseded authority, with no reason,
  expiry, extension control or remaining guesses;
- `{state:active, challenge_ref, expires_at, can_extend}` for the current valid
  unconsumed challenge, with its server expiry and a boolean guarded affordance.

Use the existing UTC instant helper: four-digit calendar-valid UTC date/time,
three fractional digits and seconds 00–59. Format assertion supplements the
lexical pattern; no trimming, offsets or invented time from browser receipt.
The server supplies expires_at from the reviewed issue/extension fence.
can_extend requires current permission, unconsumed/valid binding, remaining
extension budget and service eligibility; it is not a reserved extension or grant
to bypass a later guard. Reading controls does not renew access or code lifetime.
Active is code authority, never a delivery, verification or slot assertion.

A receipt and controls have different time meanings: a matching replay returns
its earlier permitted applied result but rereads current controls rather than
rebuilding them from that old challenge or expiry. A newer corrected email can
therefore show none/inactive while the older operation remains historically
applied. Never copy its applied_revision into the current snapshot. If the current
projection cannot be safely proven but the receipt remains permitted, use
current=unavailable; if receipt disclosure authority itself is lost, return
ACCESS_UNAVAILABLE and no receipt. A current-known snapshot may be omitted only
through the explicit unavailable variant, not an incomplete object.

IF-BOOK-04 reuses the minimal applied/pending receipt shapes from qualification.
An applied verification is historical single-use consumption, not current verified
eligibility. The client reads IF-BOOK-07 separately before acting on current status;
that read still cannot replace slot/booking admission guards. A verification
rejection is exactly state=rejected, VERIFICATION_UNAVAILABLE, refresh_status,
without operation/code/mailbox/counter/reason echo. It represents no successful
verification. Reconciliation may return the earlier fixed rejected outcome under
current authority; it must not compare again or renew anything.

The client correlates route/process UI generation, operation and server revisions.
Do not install a lower-revision snapshot or a late response for an abandoned proof/
process. Historical receipt revisions cannot restore old challenge controls.
A known projection must come from the current authoritative lineage fence, not
a stale replica or an old response cache. When paired with an applied receipt, its
revision cannot precede applied_revision; if that current read cannot be proven,
use unavailable. Active also requires the current EMAIL_PENDING code-admission
state. These cross-field/state relationships are semantic obligations; shape alone
does not enforce them. Known controls cannot grant a Verify/resend/extension
against a newer local server revision; refresh/reconcile before fresh work. Unavailable controls
disable secret/actions rather than manufacture none/inactive/verified. Existing
private status ordering, hidden/offline cancellation and authority-loss clearing
still apply; this projection contains no qualification read or new GET endpoint.

### Admission classes and HTTP meaning

Both routes use their current proof, CSRF, exact allowed Origin/media/method and
raw decoding boundary before object-specific responses. After recognizable
metadata/current authority, resolve matching earlier operations before applying
fresh expected-revision/state guards. An existing operation with changed typed
intent conflicts, including a changed code; JSON property order/insignificant
whitespace do not change intent. Never persist a raw code or unkeyed fingerprint.
The reviewed keyed bindings and finite operation outcome lifetime still apply.

| Outcome | HTTP | Closed result |
|---|---|---|
| Applied fresh/replay under current disclosure authority | 200 | Boundary's applied receipt; IF-BOOK-03 also has independent current controls. |
| Admitted operation outcome still uncertain | 202 | Boundary's pending result; IF-BOOK-03 controls unavailable unless independently proven current. |
| Authorized recognizable fresh verification has invalid code form or current code cannot verify | 422 | Fixed VERIFICATION_UNAVAILABLE rejection; no foreign/current/exhausted/used distinction. |
| Malformed raw input, unknown member or malformed protocol metadata | 400 | INVALID_REQUEST / correct_request. |
| Own authority unavailable | 404 | ACCESS_UNAVAILABLE / contact; no object result or conflict feedback. |
| Own action not permitted | 403 | ACTION_DENIED / contact. |
| Stale fresh expected revision | 409 | REVISION_CONFLICT / refresh_status, before counters/comparison/effect. |
| Changed admitted intent under same operation | 409 | OPERATION_CONFLICT / reconcile. |
| Other ineligible challenge mutation/state | 409 | STATE_CONFLICT / refresh_status. |
| Reviewed shared abuse budget exhausted | 429 | RATE_LIMIT / wait; no membership, quota or private deadline echo. |
| Finite work/record capacity or service uncertainty | 503 | CAPACITY_LIMIT / wait, or SERVICE_UNAVAILABLE / reconcile; never assumed no effect. |
| Actual streamed body, media or header boundary refused | 413 / 415 / 431 | BODY_TOO_LARGE / UNSUPPORTED_MEDIA / HEADER_TOO_LARGE, each correct_request. |

For an otherwise recognizable fresh Verify, missing/invalid known code is the
fixed 422 category after own authority and operation checks, not a code echo or
comparison. Missing/malformed challenge/operation/revision protocol metadata or
extra members remain 400. A well-shaped wrong/foreign/ineligible challenge used
for fresh Verify also gives the fixed 422 outcome, not a reason revealing it.
Stale expected lineage revision still conflicts before any comparison. A same
already-admitted operation with changed submitted values remains 409, never a new
422 operation that consumes another guess. Unauthorized callers receive none of
this validation/conflict detail. Schema rejection alone cannot choose these
runtime admission classes or prove HTTP behavior.

Reconcile_verification has no code, so it can expose only the permitted recorded
outcome, pending or safe unavailable error; it cannot create a rejected guess from
today's code state. A known failure remains fixed rather than becoming success
because another operation later verified. Reconcile_challenge similarly creates
no issue/extension and returns no verification rejection. Client/service timeout
never gives permission to allocate a new operation and duplicate mail/comparison.

### Transport, work bounds and qualification limits

Recommend at most 2,048 actual UTF-8 body bytes for each mutating command and 1,024
for payload-free reconciliation, enforcing a 2,048 pre-kind cap then the stricter
reconcile cap. Reuse the existing stricter raw duplicate-key/nesting/scalar/token
constraints, 16,384 aggregate header bytes and 8,192 Cookie-value bytes. Actual
chunked bytes count; Content-Length alone is insufficient. Emit at most 2,048
UTF-8 response bytes, no-store JSON, with no input/code/provider/exception/proof
echo, cache validator, HTML fallback or redirect. Apply the existing private
security/cache/header/method rules also to route-owned failures.

Recommend retaining one service-wide 48 receive/fresh-mutation slot budget across
qualification and these routes, partitioned into 16 general and 32 protected
challenge-extension slots; retain the separate 16 receive/reconciliation budget.
Before issue/resend, also reserve one protected receive/work slot for that active
challenge, in addition to its operation records below. Refuse new challenge
admission before effects if that complete work/record reservation is unavailable.
General issue/resend/qualification/verification traffic cannot consume a protected
slot, and one challenge cannot consume another challenge's allocation. One such
receive/extension job may be in flight per challenge; same-operation replay does
not create parallel extension work. Total active/reserved/draining protected slots
never exceeds 32, counted across workers, replacement challenges and processes.

Ingress must route a currently authorized own-process challenge-extension candidate
to its protected receive slot before general-pool pressure can reject it. Require
the allowed Origin/method/media and current proof/CSRF scope; guessed selectors or
public requests cannot allocate that reservation. Decode the bounded body within
the existing five-second receive deadline. A candidate that is not the closed
extend command cannot execute ordinary mutations in this lane: use general
admission or a safe refusal, without altering challenge clocks/counters. Exact
proxy/receiver routing and malicious/incomplete-body qualification remain later
implementation obligations; an ordinary pool gate placed ahead of this lane would
violate the proposed protection.

Release the reserved extension slot only when no further extension is eligible
(consumption, expiry, invalidation or the tenth extension), and its in-flight/
draining/uncertain work is known released. Replacement cannot forget or borrow an
older occupied slot. Its ten-second observation deadline is not work abandonment
or proof of failure; reconcile the same uncertain operation before fresh extension.
This protects admission from unrelated general traffic, not network, clock/store/
key outages or an already-uncertain own operation. No guarantee of actual latency
or complete timing accessibility follows before real-load/ingress qualification.
Delivery workers remain separately bounded private jobs, not work hidden behind a
completed HTTP response. For the combined qualification/email profile, propose a per-lineage ceiling of
32 operation-record slots, replacing the qualification-only 16 ceiling when email
controls are enabled; retain one service-wide 4,096 ceiling, including reservations.
Before issue/resend, reserve 16 slots for that challenge: its issuance result, ten
possible extension results and five comparison results. Other requests cannot
consume its unused reserved record slots. This protects the ten-extension route
from record-capacity exhaustion; the distinct protected work-admission profile
above addresses ordinary receive/mutation pool pressure. Each admitted action consumes its reserved
slot once. Invalidation, expiry or consumption releases only unused reservations;
still-permitted receipts and unresolved effects keep their occupied slots. An
issue/resend that cannot reserve this complete bounded allowance is refused before
effects, never partially admitted with an unusable timing route. Per-lineage and
global counters include all older retained records/reservations across workers.
This is an explicit unmeasured capacity refinement, not an accepted upgrade.
Reconciliation remains permitted at capacity and cannot allocate a new record. No cleanup can forget uncertain effects or prematurely
retire still-permitted historical outcomes. The reviewed send/guess budgets and
challenge clocks remain additional controls, not replaced by body/work limits.

These bounds are unmeasured recommendations. Closed variants, identifiers and
UTC shapes need focused validator checks; those checks cannot prove authorization,
raw transport, clocks, counters, secret storage, delivery truth or actual current
projection. Later runtime qualification must cover reserved-extension admission
while the general pool is saturated/draining, no cross-challenge slot borrowing,
incomplete/malicious-body bounds, atomic release/replacement and an uncertain own
extension, plus loss/duplicate/stale/out-of-order responses, old-code guesses after replacement, changed retry intent, wrong process,
withdrawal, cap/timeout/limiter outages and no secret leakage at the real boundaries.
No new dependency is required by this schema. Official JSON Schema 2020-12
[validation/format semantics](https://json-schema.org/draft/2020-12/json-schema-validation#section-7) and the existing local modules control tooling shape;
the complete stable graph, exact mechanism implementation and integrated acceptance
remain separate. This append and module do not inherit the earlier control PASS.
