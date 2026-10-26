# Logical records and transaction contract

Status: DOING. Proposed 2026-10-04 under DATA-001–DATA-010, PUB-001–PUB-007,
FR-004–FR-010/FR-019, SEC-001–SEC-010 and accepted architecture D-065.
This defines logical records, not physical tables, migrations or implemented APIs.
The [entity matrix](data-entities.csv) gives required field groups, relationships,
visibility and invariants. The publication schema and interface catalogue remain
their respective public-format and operation authorities.

## Review coverage

The [later independent review](reviews/current-definition-amendments-2026-10-04.md)
records bounded PASS for this logical contract and its entity/classification
matrices at the receipt's exact hashes. The reviewed
[contract bytes](../../../output/research/contract-review-reference-reconciliation-2026-10-04/DATA_CONTRACT.pre-status.md)
are preserved. This page's review references were reconciled afterward; record
responsibilities and invariants were not changed. Exact schemas, mechanisms,
retention/legal mapping, founder acceptance and runtime proof remain pending.

## Common record rules

PROPOSED: private records use opaque server-assigned UUID identifiers, positive
integer revisions for mutable records and server UTC instants for lifecycle events.
Public route/wing/service keys come from the canonical inventory, not UUIDs invented
by a visitor. An identifier, hash, cookie presence or declared revision alone grants
no object access. A UUID is not an anonymous-person identity or visitor account.

Typed fields and bounded text replace unrestricted payload dictionaries. JSONB may
hold only versioned closed typed documents where explicitly needed. Do not hide
unmapped personal data, authorization state or an extra retention clock in JSON.
Every linkable digest, identifier and intent payload keeps its source privacy class;
hashing does not establish de-identification. Field lengths, precise JSON schemas,
encryption/key details and retention mappings remain inputs before physical design.

PostgreSQL is the durable application authority. Foreign keys, unique constraints
and guarded revision/state changes enforce relationships at transaction boundaries;
an in-process mutex or preflight SELECT is insufficient across workers. The
exact SQL isolation/locking and retry strategy needs reviewed PostgreSQL evidence
and concurrent integration tests in the later feature plan. SQLite cannot certify
those behaviors or silently become a production fallback. The protected prototype
currently defaults to SQLite in `apps/api/app/db/session.py:15` and constructs a
synchronous SQLAlchemy Session at line 31; this is evidence, not target permission.

## Guarded PostgreSQL transition proposal — 2026-10-12

Status: DOING. Proposal within D-065's durable-authority boundary, with
[11-input bounded independent definition PASS](../../../output/research/private-record-transactions-2026-10-12/independent-review-v1.json).
Integrated founder acceptance remains held. This defines
the preferred transaction mechanism, not physical tables, SQL migrations or
working API behavior. Endpoint-specific authority and response contracts remain
controlling; ephemeral non-consented chat cannot become a PostgreSQL transcript.

Recommend short Read Committed transactions only for transitions whose entire
invariant is protected by identified shared aggregate guards and database
constraints. Acquire existing guard rows with `SELECT ... FOR UPDATE`, in one
canonical family/record order used by every competing writer, then read the
current authority and state. Approval, withdrawal, revocation, reassignment and
normal mutations must obey the same guard protocol. Locking the target alone
cannot freeze a separately changing permission, consent or release record.
A missing guard or an unbounded predicate/set invariant keeps the operation held.
For an invariant needing predicate protection, prepare a separately reviewed
Serializable binding covering every participating writer; do not silently rely
on Repeatable Read, an in-process mutex or a row lock on nonexistent records.

| Transaction boundary | Proposed mechanism and outcome |
|---|---|
| Admission | Bind the exact principal/process, scope, purpose, release/consent/assignment generations and expected revision from current authority. Re-evaluate them after acquiring every relevant guard; a prior request/ORM/cache snapshot is insufficient. Apply the governing deadline before committing authority. |
| Revision write | Use an explicit conditional mutation bound to object/family, current revision and permitted state, with a database-returned result establishing exactly the intended changed row. Zero matches is a stale/denied transition under the endpoint contract, not success or an instruction to silently adopt a newer revision. Increment within the existing integer ceiling; no wraparound. |
| Constraints | Enforce actual uniqueness, foreign-key and any required scheduling exclusion constraints in the same database transaction. Guards on selected rows do not protect absent inserts by themselves. A uniqueness conflict follows its scoped operation/allocation rules; an upsert cannot merge different principals, meanings or lineages. |
| Commit | Commit the state change, scoped immutable operation binding/outcome and any authorized durable dispatch intent together. All retain their permitted data classes and expiry. Dispatch payloads cannot copy non-consented ephemeral context into durable storage. Commit the local intent before an external effect, under its existing worker/admission contract. |
| Dispatch | No provider call, browser interaction, generated-model work or person response while holding a database transaction. Dispatch and outcome recording are separate guarded operations. PostgreSQL commit cannot make Redis, calendar, email, Entra or release storage atomic, and does not establish provider success. |
| Unknown outcome | A lost commit acknowledgement is unresolved. Reconcile the same admitted operation under current access and terminal-state evidence; do not assume rollback, mint another intent, repeat a provider effect or disclose another process. Use the endpoint's truthful pending/recovery mapping. |

Use SQLAlchemy's transaction context management with one Session per concurrent
thread, or one AsyncSession per task; do not share a mutable session between
concurrent operations. Explicitly roll back failed transactions and discard their
stale state before restarting. Mapper `version_id_col` can supplement supported
ORM flushes, but cannot replace the explicit guard contract: SQLAlchemy documents
that its counter does not cover multirow update/delete paths. Every writer,
including workers, maintenance and authorized admin changes, must preserve the
same invariants; no ORM shortcut grants a bypass.

Propose at most one automatic whole-transaction retry after the initial attempt,
only for a confirmed aborted `40001` serialization failure or `40P01` deadlock.
Recheck current authority, intent, state and expiry from the beginning, preserving
the original operation identity, expected revision and admitted work deadline.
The retry cannot increase any endpoint's time/work/concurrency budget. Do not
retry when the budget is insufficient, authority was lost or commit is uncertain.
Do not generally retry stale revisions, uniqueness/exclusion conflicts, invalid
input or permission denial. Exhaustion follows the existing endpoint recovery
contract; it cannot become a successful write. This finite retry recommendation
is not an adopted operating limit or a measured contention result.

Primary guidance checked 2026-10-12: [PostgreSQL Read Committed](https://www.postgresql.org/docs/18/transaction-iso.html#XACT-READ-COMMITTED)
describes command snapshots and updated-row predicate rechecks;
[explicit locking](https://www.postgresql.org/docs/18/explicit-locking.html)
covers row-lock scope, deadlocks and consistent lock order;
[failure handling](https://www.postgresql.org/docs/18/mvcc-serialization-failure-handling.html)
requires retrying the complete transaction. [SQLAlchemy version counters](https://docs.sqlalchemy.org/en/20/orm/versioning.html)
and [session concurrency](https://docs.sqlalchemy.org/en/20/orm/session_basics.html#is-the-session-thread-safe-is-asyncsession-safe-to-share-in-concurrent-tasks)
support the ORM limits above. Context7 `/websites/sqlalchemy_en_20` was queried
on the same date. The proposed guard composition and retry cap are Hengshi design
recommendations, not requirements prescribed by those vendors. No exact database,
SQLAlchemy release, sync/async topology, provider or stable graph is selected.

After separately authorized implementation, exercise real PostgreSQL connections
and the actual request/worker boundaries: two simultaneous accepts, edit versus
approval, consent/revocation versus admission, same-operation retries, changed
intent, allocation/constraint conflicts, deadlock/serialization failure, lost
commit acknowledgement and delayed external acknowledgement. Assert authorized
state and actual effect counts from approved requirements. Include delivery-time
fences; a correct commit cannot authorize later revoked disclosure. SQLite,
mocked transactions and documentation checks are insufficient. Exact schema,
guard inventory/order, lock/statement/transaction timeouts within each existing
work profile, physical retention/copy bindings and their independent review remain
implementation prerequisites. No concurrency or application tests were run here.
The receipt covers the frozen proposal and catalogue reference only; this later
review-link update is outside its inputs and does not adopt a mechanism or retry cap.

## Publication and staff records

Content revisions retain exact owner, provenance, rights, evidence and classification.
Only authorized current staff can edit a candidate; editing creates a new revision
and invalidates prior review/approval. Reviews and founder approval bind the exact
candidate snapshot/checksum and actual authorized principal, with self-review/
self-approval prohibited under the accepted separation rules. These private records
never enter the public manifest or a public staff directory.

Approved release bytes remain immutable. Serving eligibility and withdrawal are
separate controlled records; retained bytes do not grant a public-read right.
One activation generation links the exact eligible release and durable cutover
intent. PostgreSQL guards plus the publication contract's external fencing or proven
terminal serialization prevent delayed cutover from replacing a newer generation.
Audit/history must preserve the actual outcome and cannot manufacture approval.

The founder's editable company identity/registration/address/contact facts are
typed content revisions under this same workflow; see the
[entity/contact amendment](../../software-definition/06-entity-and-public-contact.md).
Preserve identifiers as strings and validity precision explicitly. A draft edit
cannot change the active footer, structured data, World or AI evidence separately;
administration is the editing surface, not permission to bypass approval.

D-076 defers public registration identifiers, validity claims and the supplied
registered address. Private prepared facts may retain them for authorized admin
revision/review. Public derivatives must consume the [allowlisted publication
projection](PUBLICATION_CONTRACT.md#d-076-company-facts-public-projection--2026-10-07),
not the whole private object. The [13-input public-projection review](reviews/company-public-projection-v1-2026-10-07.md)
gives bounded definition/schema-seam PASS for its frozen inputs; it does not extend
earlier data/company reviews. Current owner/contact verification, semantic
exclusion, actual authorization/projection and applicable notices remain gates.
Synthetic local content never grants production publication authority. This later
review-reference update is outside those inspected bytes.

Entra principal/role mapping, session revocation and dormant emergency-account
activation reference private identity records. No local visitor user table, visitor
password, upload record or general administrator publication bypass is introduced.
Exact identity proofs and audit/credential policies remain security/legal gates.

## Conversations, consent and handoff

Without retention consent, conversation and replay state exist only in the bounded
ephemeral path. A durable transcript, message index, job payload or diagnostic copy
would violate that boundary. Ephemeral loss expires that session; it is not rebuilt
from PostgreSQL. Provider retention/no-training policy must independently comply.

D-076 now settles visitor access expiry at 30 minutes of inactivity or authorized
End, with no absolute conversation age. The [current lifetime profile](PRIVATE_PROCESS_PROOF.md#access-lifetime-retention-and-pending-cleanup)
and [continuation/End controls](CHAT_EVENT_PROTOCOL.md#visitor-continuation-and-end-controls-proposal--2026-10-07)
have a [26-input bounded definition/representation review PASS](reviews/visitor-lifetime-controls-v1-2026-10-07.md)
at its frozen inputs. Actual clocks, current-authority fences, credential/store
mechanisms and cleanup need separate qualification; the valid-proof exposure and
complete-process accessibility limits in that receipt remain held. Access expiry
does not determine every stored record's retention or prove external/provider
deletion. This later reference update is outside the reviewed inputs.

The [EU retention proposal](SECURITY_PRIVACY_CONTRACT.md#eu-privacy-and-retention-policy-proposal--2026-10-07)
now provides candidate purpose/class anchors, periods, recoverable-copy rules and
rights/transfer duties for MA-002 review. Its new numerical periods and mechanisms
are not accepted policy. Read `unmapped` or `pending` classification rows as an
unresolved acceptance/mechanism gate, not absence of that proposal or a request
for the founder to choose arbitrary periods again. The accepted consented-record
90-day rule below remains distinct from booking, identity, audit, suppression,
ephemeral access and backup rules; no universal 90-day or renewed expiry follows.
Old bounded data/classification PASS receipts do not cover these D-076 references.


Durable conversation/message/brief/lead records require an acknowledged versioned
purpose-specific consent decision before persistence. Record the relevant immutable
notice version and event instant, not a generic boolean that retroactively authorizes
earlier storage or a new purpose. Consent withdrawal interrupts disallowed writes/
transfers and starts the approved deletion workflow; it does not falsely claim
that all provider and backup copies disappeared synchronously.

Consented chat, derived traces and brief/lead have the approved 90-day rule. An
immutable policy-resolved expiry anchor and policy reference must govern all derived
records; resuming, copying, editing or restoring cannot reset it. The exact anchor,
exception authority, consent-proof and other record retention remain MA-002 inputs.
No launch persistence is authorized by this logical definition.

Public availability reveals only the approved minimal current state. Its expiring
staff setting, suppressive Teams signal and private routing identity stay separate.
Handoff requires current eligibility, authorized assignment and consented context.
Request acceptance, alert delivery and staff response are distinct outcomes.

### Proposed availability intent and expiring projection

SOF-01A/B's durable staff declaration and the accepted architecture's ephemeral
Redis presence serve different responsibilities. The earlier DE-18 combined the
explicit setting with its derived presence. This proposal separates them without
making Redis a durable source or changing who may declare availability:

| Record | Responsibility and authority | Prohibited inference |
|---|---|---|
| DE-22 — staff availability intent | Private PostgreSQL record of the authorized explicit declaration/withdrawal for an approved staff/department scope, its server-controlled revision and validity window. | Stored intent alone is not current live presence, a public staff directory or permission to route an unconsented conversation. |
| DE-18 — availability projection | Expiring Redis projection referencing the current intent/revision, current eligibility and suppressive presence state. Public reads expose only approved minimal availability. | Redis/Teams cannot create, prolong or resurrect an explicit declaration; a missing or unknown projection is not available. |
| DE-21 — bounded audit evidence | Actual authorized action and safe outcome under its separately reviewed audit policy. | No unlimited presence history, transcript payload, staff behavior analytics or retention exception follows from an audit requirement. |

PROPOSED transition obligations for IF-STAFF-09 and the corresponding reads/routing:

1. A declaration requires current explicit availability authority and approved
   staff/department scope. The server determines valid expiry under the reviewed
   policy; the client cannot grant itself a role or extend validity. Record an
   authorized guarded intent change before reporting durable acceptance.
2. Publish an available projection only after confirming the current declaration,
   its revision, expiry, staff eligibility and required fresh suppression state.
   An accepted declaration with a failed/unknown projection remains unavailable
   publicly. Declaring on is not a promise that a human has accepted a handoff.
3. Withdrawal, expiry, scope/identity revocation and suppression invalidate the
   available projection. A delayed on-write or retry for an older revision cannot
   reopen it. The serving/routing contract must reject stale revisions; a preflight
   check alone is insufficient for a concurrent projection write.
4. A projection's effective lifetime cannot exceed the declaration's validity or
   the reviewed freshness bound. Reading, reconnecting or retrying the same intent
   cannot renew its expiry. A new authorized declaration has its own guarded intent;
   it is not a side effect of Teams becoming online.
5. Cache loss or unknown suppression/eligibility gives unavailable. Rebuilding
   requires current authoritative declaration and eligibility, unchanged revision
   and fresh required signals. Do not replay a previously available cache snapshot
   as proof, change the intent's expiry or declare staff online after restart.
6. Handoff creation/acceptance rechecks current eligibility, consent and assignment;
   a public available indicator is not a reservation or acceptance. Existing valid
   conversation/booking state follows its own transition contract if availability
   subsequently changes, rather than being silently confirmed or deleted.
7. Restore keeps presence unavailable until current validity, revocation/withdrawal
   and fresh suppression are verified. An older backup cannot revive a later
   withdrawn declaration or reset its expiry. Exact restore suppression and policy
   evidence must be specified before availability recovery can be accepted.

This resolves the proposal's record responsibilities, not implementation proof.
The [availability consistency protocol](AVAILABILITY_CONSISTENCY.md) refines these
obligations with current-authority guards, identity-and-revision bindings,
decision-time expiry and reconciliation of uncertain negative effects. Its
[independent review](reviews/availability-consistency-2026-10-04.md) records
bounded PASS for the proposed protocol and the exact inspected inputs. The
[data-contract bytes inspected there](../../../output/research/contract-review-reference-reconciliation-2026-10-04/DATA_CONTRACT.pre-availability-reference.md)
are preserved; this later reference addition changes no record invariant.
The exact atomic publication/revocation mechanism across PostgreSQL and Redis,
expiry/freshness intervals, delegate scope, time-limit advisement, authorized
response fields and concurrent/restore tests remain required contracts. Do not
claim immediate cross-store suppression from a successful PostgreSQL write alone.

The added intent is identifying private staff data. Its legal retention, minimal
audit/history, classification/deletion and backup treatment remain held; business
expiry is not a retention duration and the visitor chat's 90-day rule does not
automatically apply. The classification/interface records must carry this split
for integrated acceptance. No persistence, migration, availability service
or selected Redis/provider mechanism is implemented. This logical amendment has
the later bounded review identified above; prior receipts retain their own scopes.

## Booking and provider transactions

The [scheduling lifecycle](BOOKING_SCHEDULING.md) and its later directional/HTTP
profiles refine these existing logical records for IF-BOOK-05/06/08/09. Use that
controlling source for purpose-bound offers/reviews, guarded admissions, same-
operation reconciliation, provider uncertainty and reschedule/cancel lineage.
Its logical, representation and HTTP correction receipts each retain their exact
frozen scope; this later navigation reference changes no record or transaction
invariant and inherits no PASS. Exact operating policy and resource bindings,
account capability, physical schema, actual PostgreSQL/provider enforcement and
integrated/founder acceptance remain separate.

The single booking lineage holds email, organization, role, desired outcome,
matched wing, timing and consent; budget remains optional. No required name, phone,
AI conversation, visitor account or upload. A syntactically valid address is not
verified ownership. Revision-bound challenges are separate from stored email facts;
correcting the address invalidates old challenges, verified status and old slot
eligibility in the same guarded transition. Resend preserves lineage and limits.

Server verification of the current eligible challenge enables slot selection.
Selection references an eligible owner/backup and the exact UTC start/end instants,
visitor timezone and 30-minute discovery duration. Client-provided owner IDs, a
visible slot card or a timezone label cannot establish server eligibility.
Revalidate ownership, verification, qualification, consent and slot availability
before the booking intent is accepted; stale revisions conflict safely.

Commit the authorized state transition and its durable external intent together.
Dispatch after commit, without holding a database transaction across a provider call.
Scope operation identity to the authorized lineage/action; changed intent under the
same identity conflicts. Claimed work/lease expiry cannot establish provider failure.
Unknown outcomes remain BOOKING_PENDING or RECONCILIATION_ERROR as appropriate;
reconcile authoritative provider identity/state before a safe retry or confirmation.
Only matching local state plus the approved calendar/meeting record permits
CONFIRMED_QUALIFIED. A provider event ID alone does not prove the requested slot,
owner, attendee, duration or online-meeting details match.

Reschedule/cancel mechanisms remain held under the interface contract. Keep last
confirmed truth until their authorized provider result is reconciled. Independent
notification/alert failure cannot undo the booking or cause a second calendar write.
Outbox payloads are private mapped data, not a general visitor-content log.

## Deletion, access and conformance

Link data classes and approved copies to the minimal purpose/lineage references
needed for verified access and deletion. Do not create cross-visitor marketing or
movement profiles. A process proof authorizes only its reviewed object/purpose;
historical privacy requests need the approved identity-verification procedure,
not possession of a guessed UUID or unrestricted email lookup.

Deletion requests track approved class scope, external result, exception authority
and outcome separately. Unmapped retention, unknown external deletion or unresolved
restore suppression keeps the request pending. Cascade rules cannot blindly delete
legally retained booking/audit evidence or preserve a linkable tombstone indefinitely.
Quarantined restores enforce approved deletion/expiry before serving traffic.

Future negative tests must demonstrate concurrent edit/review, wrong-object access,
old email challenge after correction, same operation with changed intent, duplicate
calendar dispatch and late acknowledgements, consent refusal/withdrawal, forbidden
retention-clock reset, invalid source release and deleted-data resurrection.
Use synthetic records and real PostgreSQL transactions for concurrency evidence.
The matrix is deliberately a logical contract; full field schemas, approved policy
mapping, provider behavior and complete Phase 1 acceptance remain prerequisites.

## Common value representation proposal — 2026-10-06

PROPOSED: use [the common value module](process-value.schema.json) as the entry
for private record UUIDs, mutable-record revisions and SHA-256 text, reusing the
exact lexical forms already present in the private preparation/publication
schemas. Those source schemas remain unchanged. Representation reuse imports no
publication lifecycle, private admission permission or operational grant.

| Value | Proposed representation | Separate mandatory meaning checks |
|---|---|---|
| Record UUID | Exactly 36 lowercase hex/hyphen characters, with explicit UUID format assertion; reject rather than trim, case-fold or strip braces/URN prefixes. | Permitted issuer/allocation, object family, current proof/tenant/purpose and exact record binding. A shaped UUID, including Nil/Max, proves no allocated record or uniqueness; the common schema selects no generator; the issuance profile below is a proposed refinement. |
| Mutable-record revision | Positive integer through 9007199254740991, matching the existing private-message range. | Server authority, expected/current comparison, atomic transition and overflow handling. JSON Schema's mathematical integer type does not enforce a raw token spelling; raw parser and interoperability profiles remain required. |
| SHA-256 text | Exactly 64 lowercase hexadecimal characters, without normalization. | Independently calculate the digest over exact governed bytes and verify source eligibility and the intended binding. A caller hash is not an approval, credential or privacy exemption. |

This module is not an inbound/outbound envelope: its root rejects every instance;
consumers reference a named `$defs` member. Register all local referenced schemas
explicitly and deny unregistered/network retrieval. Require UUID format assertion
at the actual validator boundary: a `format` annotation alone is insufficient.
The [JSON Schema validation specification](https://json-schema.org/draft/2020-12/json-schema-validation)
distinguishes format annotation from assertion. [RFC 9562](https://www.rfc-editor.org/rfc/rfc9562.html#section-4)
defines UUID text; this proposal's lowercase-only form is a narrower project
representation, not an RFC requirement. [I-JSON](https://www.rfc-editor.org/rfc/rfc7493.html#section-2.2)
supports preserving numeric interoperability; the existing revision upper bound
is retained, not a new throughput or resource budget.

Do not replace public route/release/wing keys with UUIDs. This proposal does not
select client operation encodings, UUID generation versions, proof/CSRF secrets,
timestamps, consent purposes, legal retention, numeric operating profiles or
database types/constraints. Directional contracts must bind each field and
remaining policy before wire freeze. Existing process CSVs and message schemas
are not mechanically rewritten or accepted by this addition.

Validation exercises only the module/reference/format boundary with synthetic
values. No HTTP, browser, persistence, privacy, cryptography or concurrent
authorization enforcement follows. Independent review, integrated/founder
acceptance and the full compatible stable graph remain required.

Review reference added 2026-10-06: the [independent receipt](reviews/common-process-values-v1-2026-10-06.md)
records PASS for the proposed helper and validator boundary. The exact
[inspected contract](../../../output/research/common-process-values-2026-10-06/DATA_CONTRACT.md.reviewed)
is preserved; this reference is outside those reviewed bytes. Field adoption,
raw parsing, request enforcement and integrated/founder acceptance remain held.

## Private-record issuance profile proposal — 2026-10-12

Status: DOING. Proposal with [11-input bounded independent definition PASS](../../../output/research/private-record-transactions-2026-10-12/independent-review-v1.json);
integrated founder acceptance remains required. This refines the existing opaque server-assigned
private-record rule. It changes no schema, allocated record, public key, prototype,
API path, secret format or database, and inherits no earlier review PASS.
The new receipt covers its exact frozen proposals only; this later review-link
update does not establish physical allocation, ingress enforcement or adoption.

Recommend UUIDv4 with the RFC variant for newly allocated server-owned private
record identifiers. This includes private conversation/booking lineages,
provisional contexts, challenges and other private record families governed here.
Existing chat stream/event references and caller operation IDs keep their own
issuers and directional contracts. A caller operation ID cannot become a
server-allocated record, principal, proof or permission by matching its text.
Public route/release/wing/service keys and external provider identifiers retain
their existing formats and ownership.

| Boundary | Proposed required behavior |
|---|---|
| Issue | Prefer Python's standard-library `uuid.uuid4()` in the eventual qualified runtime. Generate independently for each new record. Do not derive IDs from email, host address, timestamps, parent IDs or caller operation IDs; do not substitute a simulation PRNG when secure generation fails. Failed issuance admits no new record or external effect. |
| Commit | Enforce uniqueness in the authoritative record namespace at the allocation transaction. A detected collision cannot overwrite another record, disclose it or merge intentions. The later physical plan must bind constraint scope and finite conflict handling; random shape alone does not prove uniqueness. |
| Retry | A permitted retry of one already admitted intent resolves its existing allocation under current authority; it cannot allocate a new lineage or repeat its effect. A genuinely new record receives a new ID. Preserve the existing revision, replay and retention rules. |
| Read | Check the original canonical lowercase text before a permissive UUID parser. Resolve the exact allocated family, scope and current access authority. A shaped Nil/Max, foreign-family or unknown UUID supplies no record access. UUID version validation alone proves neither issuance nor authorization. |
| Order | IDs carry no business-time or causality guarantee. Use the existing authoritative lifecycle fields, revisions and event sequences for those jobs. Do not infer creation time, permission or event order by sorting UUID text. |

The common schema remains a representation helper. It does not become a universal
UUIDv4-only admission schema: each consuming direction must bind its permitted
issuer/version and current allocation. Existing immutable receipts and historical
or external references are not rewritten, migrated or silently rejected by this
proposal. Secret proof/CSRF material remains under its separate generation,
encoding, transport, revocation and disposal contracts; an ID is never a bearer
credential. Linkable IDs retain their applicable privacy/retention classification.

Primary guidance checked 2026-10-12: [RFC 9562 §5.4](https://www.rfc-editor.org/rfc/rfc9562.html#section-5.4)
defines random UUIDv4; [§8](https://www.rfc-editor.org/rfc/rfc9562.html#section-8)
recommends it for security-related UUID uses and prohibits UUID possession as a
security capability. [Python's UUID documentation](https://docs.python.org/3/library/uuid.html#uuid.uuid4)
describes its cryptographically secure built-in generator. Context7
`/python/cpython` was queried for this exact primitive on the same date; its
source examples confirm that the UUID constructor also accepts noncanonical
forms, so construction alone cannot enforce Hengshi's lexical boundary.
These sources support the primitive, not Hengshi's complete lifecycle design.

UUIDv4 has weaker B-tree insertion locality than time-ordered UUIDs, as
[RFC 9562 §2.1](https://www.rfc-editor.org/rfc/rfc9562.html#section-2.1)
explains. The physical design must measure the relevant indexed workloads;
this profile promises no performance result and does not select an internal
storage/index strategy. Any different externally exposed issuance profile needs
reviewed evidence and its applicable approval, rather than silent substitution.
No Python version or coupled graph is selected by this recommendation.

After implementation is separately authorized, verify the actual allocation and
request boundaries: wrong family/scope, canonical-form rejection, unknown or
retired references, generator failure before side effects, forced uniqueness
conflict, and concurrent retries resolving one admitted intent without duplicate
records/effects. Inject allocation failure at the behavior seam; matching test
fixtures to a schema or sampling random IDs cannot prove entropy, uniqueness,
transactions or permission enforcement. No application tests were run for this
proposed definition. The later11-input independent receipt linked above supplies
bounded definition-consistency PASS for this issuance profile and the guarded
transaction proposal. Physical allocation, actual boundary enforcement and
integrated founder acceptance remain held; no runtime evidence follows.

## Raw JSON admission proposal — 2026-10-06

The common value module defines parsed values; it cannot detect information lost
before parsing. This shared proposal refines the existing strict JSON obligations
in [availability reads](AVAILABILITY_READ_HTTP.md) and
[writes](AVAILABILITY_WRITE_HTTP.md), and the closed-input requirement in
[private creation](PRIVATE_PROCESS_PROOF.md#directional-creation-and-admission-proposal).
It selects no endpoint, HTTP error variant, middleware or production dependency.
Each directional contract still binds its body, fields and admission authority.

Require one agreed decoding path at the actual request boundary before framework
body coercion, schema/model validation or dispatch. Apply the accepted media,
content-encoding and finite receive/work profile before collecting or decoding
untrusted bodies. A trusted Content-Length alone cannot bound streamed input.
Streaming bytes, decoded bytes, nesting, token lengths, member/item counts, time
and concurrency need finite approved limits and enforcement; no defaults are
invented here. A hook which rejects after full allocation cannot prove these
limits. Unknown transport/profile support denies the affected operation.

Within that profile, require UTF-8 with strict byte decoding and no BOM. Reject
malformed JSON, trailing non-whitespace data, duplicate decoded object member
names at every depth, invalid Unicode scalar sequences in names or values and
non-JSON number tokens such as NaN or Infinity. Escaped and literal spellings of
the same name conflict. Valid supplementary-character surrogate pairs remain
valid; isolated surrogates do not. Preserve legitimate Unicode text without
silent replacement, trimming or normalization. BOM rejection is a project choice;
RFC 8259 allows parsers to ignore a BOM and does not require duplicate rejection.

Validate root type, null allowance, required/extra members and closed variants
against the exact directional schema. Do not impose one global ban on nested
arrays or nullable fields, merge unknown fields into persistence or accept a
coerced alternative type. Body validity alone cannot authorize mutation or
external effects: origin, CSRF, proof/identity, object/purpose, current state and
atomic/reconciled outcome checks retain their separate authority.

Preserve numeric meaning until field validation: do not round or overflow an
incoming token into an accepted value. Integers shared with JavaScript require
the approved exact safe range or the field's specified decimal-string form.
The availability revision string stays a string; the common positive-revision
helper does not change it. A mathematically integral 1.0 must follow the field's
explicit lexical policy, not an inferred global rejection. Decimal precision,
exponent and lexical rules remain field-profile inputs. Standard JavaScript
JSON.parse or an ordinary Python dictionary cannot recover discarded duplicates;
raw validation must precede that loss. Python arbitrary-size integers alone do
not establish browser interoperability.

Response producers must enforce the matching shape and numeric/Unicode profile
before emitting UTF-8 JSON; allow_nan=False alone does not establish safe numeric
precision, scalar validity, closed shape or finite work. Consumers need the
applicable raw and directional checks before using a response as process or
publication truth. Private errors must use approved safe variants without raw
input, field contents, parser exception text or secret/proof disclosure. A parse
failure never becomes a completed business action. Public caching and private
no-store obligations remain controlled by their existing HTTP contracts.

[Native framework observations](../../../output/research/raw-json-admission-2026-10-06/observations.json)
exercise installed Starlette 1.3.1 Request.json at requests.py:262 under native
Python 3.14.5/FastAPI 0.138.0. The twenty synthetic cases show discarded duplicate
names, accepted non-JSON/nonfinite numbers, isolated surrogates, UTF-16/32 and
BOM; they also distinguish exponent rounding and Python-preserved large integers
from raw syntax rejection. Valid controls parse, while trailing data and malformed
UTF-8 are rejected. These are parser observations, not actual Hengshi route
admission tests, exploit evidence, a compliant alternative decoder or a selected
production graph. Existing dependencies and application code are unchanged.

Prefer framework integration and standard-library hooks where they satisfy the
complete profile; json.object_pairs_hook and parse_constant can preserve duplicate
and invalid-number detection, but neither supplies the whole resource/Unicode/
numeric/security boundary. The [Python JSON reference](https://docs.python.org/3.14/library/json.html),
[RFC 8259](https://www.rfc-editor.org/rfc/rfc8259.html) and
[RFC 7493](https://www.rfc-editor.org/rfc/rfc7493.html) support these observations
and interoperability concerns. Context7 /python/cpython is indexed main; its
future array_hook is not evidence for the observed 3.14 runtime.

Before implementation: accept each field/transport profile and denial mapping;
choose a proven compatible parser/framework integration; then exercise actual
raw HTTP and browser boundaries, nested/escape duplicates, numeric loss, valid
Unicode controls, bounded streaming and denial without dispatch. Schema fixtures
and these native observations cannot certify that enforcement. Independent
review, founder/integrated acceptance and all existing legal/runtime gates remain.

Review reference added 2026-10-06: the [raw JSON admission receipt](reviews/raw-json-admission-v1-2026-10-06.md)
records bounded PASS with reproduced native observations and valid-value controls.
The exact [inspected contract](../../../output/research/raw-json-admission-2026-10-06/DATA_CONTRACT.md.reviewed)
is preserved; this later reference is outside those bytes. The review does not
prove a compliant alternative decoder, HTTP enforcement, wire freeze or acceptance.

## Private browser JSON admission profile proposal — 2026-10-06

Status: DOING. This refines the existing raw-representation boundary, not its
schemas or any endpoint. Apply the proposed common decoder to anonymous visitor
JSON HTTP mutations in IF-CHAT-01/02 and IF-BOOK-01–09 where a JSON body is defined,
and IF-STAFF-09 availability commands. Existing route-specific stricter limits
win. This is not a global replacement for publication/compiler messages, content
authoring, public release reads, WebSocket frames or provider callbacks; those
need their own bound profiles. No new parser dependency or production selection.

### Finite starting limits

All new numbers are unmeasured engineering proposals requiring integrated
acceptance and actual ingress/resource qualification. They are not RFC limits.

| Item | Proposed ceiling / meaning |
|---|---|
| Raw JSON body | 16,384 received bytes across all chunks; use the smaller route cap, including IF-BOOK-01's 1,024 bytes. No accepted compression or alternate encoding bypass. |
| Decoded container nesting | 16 object/array levels; root container is level 1. Scalars do not add a container level. |
| Object / array breadth | 64 members per object; 256 elements per array. A member name and its value are distinct counted nodes. |
| Total decoded nodes | 4,096, including root, every container, member name and scalar; count each once. |
| Decoded string / member name | 8,192 / 96 Unicode scalar values, respectively; field schemas may be stricter. These do not replace the received-byte cap. |
| Numeric spelling | At most 128 ASCII characters including sign, decimal point and exponent; explicit exponent at most four digits excluding sign and absolute value at most 1,024. Field value/range/type rules still apply. |

A route must bind its method/media/origin/proof, receive deadline, admitted work
and response/error profile before implementation. Unbound routes stay unavailable;
the common body limit supplies neither an auth policy nor a queue/concurrency
budget. IF-BOOK-01 retains its existing five-second receive/finite-work proposal,
JSON media and response/status rules unchanged. This profile does not authorize
a larger route body or add a JSON body to a bodyless action.

### Standard-library-first decoding recommendation

1. Do the applicable cheap transport/origin and work-admission checks first.
   Count actual chunks through the framework's request stream before copying or
   concatenating an over-limit body; reject an oversized declared length early
   but never trust that length instead of actual bytes. Empty/disconnected or
   incomplete framing is not an empty successful command. Keep the work permit
   until known cleanup. Upstream ASGI/proxy buffering can already allocate an
   oversized chunk; received-byte counting alone does not bound that allocation.
2. Decode accepted bytes explicitly as strict UTF-8 with no BOM. Do not pass raw
   bytes to a decoder that auto-detects UTF-16/32, silently replace invalid bytes,
   trim a BOM or normalize Unicode. Accept exactly one complete RFC 8259 value
   plus its permitted whitespace, never a parsed prefix or concatenated values.
   The route's closed schema decides its allowed root type.
3. Prefer Python `json.loads` with `strict=True`, an `object_pairs_hook` that
   rejects repeated **decoded** member names at every depth before dict collapse,
   and a rejecting `parse_constant`. Escaped spelling cannot evade duplicate
   detection; compare decoded names exactly, without case folding or Unicode
   normalization. Case/normalization variants remain separate names subject to
   the closed field schema. `strict=True` alone is not this contract.
4. Bound numeric token length/exponent before numeric construction. Recommend
   bounded `parse_int` and `parse_float` hooks, with exact finite `Decimal` for
   decimal/exponent spellings rather than immediate binary floating conversion.
   This preserves values such as 1e400 and 1e-400 long enough for field admission;
   it does not authorize them as a particular field value. Reject NaN/Infinity
   extensions, unbounded tokens and conversion failures. Keep native integer and
   recursion protections; do not change process-global limits to accept input.
5. Before schema/model dispatch, walk the parsed tree with bounded work, enforcing
   container/breadth/node/string ceilings and Unicode scalar validity in keys
   and values. A valid escaped surrogate pair may decode to its scalar; reject
   isolated surrogates. Escaped control characters permitted by JSON still need
   each text field's rule; do not invent global trimming or silently repair them.
   Stop counting on first excess rather than building another full tree copy.
6. Bind exact field representations before model coercion. A mathematically
   integral decimal can become an integer only when that field permits JSON
   integer semantics and its exact admitted range; `true` is never integer 1.
   A contract requiring a string stays a string. Reject a required conversion
   that overflows, underflows or changes the admitted value; do not round it to
   another revision, identifier, amount or operation meaning. No arbitrary
   `default=str`, float round-trip or serializer normalization defines identity.

The tree ceilings are **accepted-document bounds**, not claims that the native
decoder allocates only that many nodes or descends only sixteen levels. Hooks
may run after sub-values have been built. Account bounded raw bytes, decoding,
temporary containers and rejection cleanup in the route's admission envelope;
native recursion failures deny input. Prove actual peak allocation/CPU/cleanup
under malformed near-cap bodies before acceptance. If this candidate cannot fit
the qualified envelope, do not approve it; assess a bounded supported parser
through the complete stable compatibility graph rather than removing safeguards.

### Framework integration, effects and errors

Use framework streaming and typed validation, with the raw gate before any
automatic body parser, Body-dependent dependency or handler capable of effects.
An explicit Request boundary followed by validation of the admitted representation
is a candidate integration pattern; exact route/dependency/model wiring remains
to be verified against installed source. Calling the normal handler first and
catching its validation error cannot restore duplicate keys or undo effects.
OpenAPI declarations likewise do not enforce this admission boundary.

Only an accepted representation reaches closed field, current proof/CSRF,
source/consent/revision and immutable-operation checks. Parsing is neither
authorization nor permission to persist, call AI/provider code or return private
existence. Raw bodies and derived parser/model exception input are not recorded
in logs, traces, queues or response detail. The body has its original privacy
class during ephemeral handling; safe counters never include submitted values.

Use the applicable route's fixed safe denial, not raw framework exceptions or
new guessed universal status codes. Malformed current input cannot undo or
definitively describe an earlier uncertain operation. Capacity/internal failures
remain distinct from confirmed input rejection. Never claim another session or
lineage does not exist, or say an earlier effect failed because parsing now fails.

For output, project only the route's closed permitted response, enforce its
finite size and use JSON serialization with nonfinite output disabled. Decimal
or another unsupported internal value must reach only an explicit validated
field representation, never a generic string fallback. Serialization failure
cannot turn an admitted operation into an asserted no-effect result. JWT, cookie,
CSRF, staff identity, consent, data retention and idempotency policies are unchanged.

### Primary support and remaining proof

Checked 2026-10-06: [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259.html)
defines JSON grammar, Unicode/interoperability and permitted parser limits.
[Python JSON](https://docs.python.org/3.14/library/json.html) documents duplicate
collapse, numeric extensions, hooks, encoding detection and untrusted-input risk;
[Decimal](https://docs.python.org/3.14/library/decimal.html) preserves numeric text
without immediate binary rounding. The current rolling 3.14 docs identify a later
minor than the existing 3.14.5 research runtime: they do not select an upgrade.
Context7 `/websites/fastapi_tiangolo`, [Request](https://fastapi.tiangolo.com/reference/request/)
and [error handling](https://fastapi.tiangolo.com/tutorial/handling-errors/)
support streaming/model integration and show access to raw invalid input; copying
that tutorial body/error echo would violate this private contract.

This proposal adds no compliant decoder or route. Prior installed-framework
observations remain narrow evidence of defaults, not enforcement. After approved
planning, actual HTTP-boundary tests must cover nested/escaped duplicate keys,
valid international text and surrogate pairs, isolated surrogates, BOM/UTF-16/32,
trailing values, numeric overflow/underflow/integral equivalence and boolean
denial, every cap boundary, slow/oversized chunks and permit cleanup, redacted
errors and no business dispatch on rejection. Qualified ingress limits, actual
model/number binding, compatibility, privacy and integrated/founder approval remain.

## Record-purpose retention binding proposal — 2026-10-08

This binds the existing DE-01–DE-22 logical records to the
[controlling retention schedule](SECURITY_PRIVACY_CONTRACT.md#proposed-retention-schedule-and-immutable-clocks).
It changes no period, lawful basis, consent requirement, role or storage authority.
The schedule's new periods remain recommendations; a proposed binding is not an
adopted policy. Earlier receipts do not cover this addition. Matrix cells marked
`pending`/`unmapped` remain acceptance gates, with this proposal supplying the
candidate mapping rather than silently editing their reviewed values.

The [22-input independent review](reviews/record-purpose-binding-v1-2026-10-08.md)
records bounded logical-consistency PASS at the preserved exact snapshots.
This later link does not expand those reviewed bytes or adopt the policy; exact
bases/schemas/notices/provider bindings and integrated acceptance remain held.

### Binding carried by each purpose-limited field group

Resolve, before collecting or retaining identifying data: exact entity/field group,
existing record class and subpurpose, approved immutable policy revision, approved
basis, immutable notice revision where notice is required, relevant consent proof
when consent is the basis, first-admission/terminal-event anchor, applicable expiry
or bounded necessity-review criterion, source lineage/earlier expiry, authorized
copy/recipient inventory and deletion/suppression obligation. These are logical
obligations, not new columns or an unbounded metadata dictionary. Policy/notice
identifiers and exact storage schemas remain for approved physical planning.

The server derives the binding; a caller cannot assign a longer class or deadline.
Missing, unapproved or incompatible mappings deny the affected collection, durable
write and transfer. Deletion verification stays pending for unknown copies;
uncertainty cannot reopen ordinary access. Do not retain extra personal fields
merely to populate this binding. Ephemeral processing needs its authorized purpose
and finite cleanup rule, but does not justify a durable policy/visitor history.

| Logical record | Proposed field-purpose binding; separate clocks retained |
|---|---|
| DE-01 content revision | Eligible public fields use `published_content`; identifying portraits/quotes require their own rights/purpose expiry. Private owner/reviewer links use `staff_identity_and_approval`; unpublished identifying content needs its own accepted purpose and cannot inherit public-history retention. |
| DE-02 specialist review; DE-03 founder approval | Minimal principal/current authority fields use `staff_identity_and_approval`. Safe action/result accountability uses the relevant `audit_and_operational_copies` subpurpose. Exact publication-accountability necessity/archival mapping remains open; no blanket 90-day or perpetual retention is selected for release evidence. |
| DE-04 publication release | Public bytes use `published_content`; personal embedded content keeps its source rights/expiry. Approval and principal references stay private under DE-02/03 policies. Immutable bytes do not grant serving eligibility or exempt personal derivatives from deletion/withdrawal. |
| DE-05 publication activation | Public release identity follows DE-04; identifying operator/result fields use the appropriate audit subpurpose. Unsettled cutover keeps only authorized necessary reconciliation state; it cannot retain unrelated content indefinitely. |
| DE-06 staff principal | Current role/eligibility fields use `staff_identity_and_approval`, including its proposed obsolete-profile cleanup criterion. Referenced release accountability is separated as DE-02/03; removing access does not delete the Microsoft account. |
| DE-07 staff session | Staff binding uses `staff_identity_and_approval`; credentials use `secret_or_credential` and current staff session/rotation/revocation rules. Session validity is not roster or audit retention. No raw token enters the ordinary record/copy inventory. |
| DE-08 process ownership | Scope/verifier fields inherit the admitted conversation, booking or privacy-request purpose and the separately approved proof facility. Proof validity, verifier cleanup and necessary unsettled reservations are distinct. A guessed credential-class mapping cannot authorize durable non-consented conversation ownership. Exact verifier-store retention remains open. |
| DE-09 conversation; DE-10 message | Without retention consent use `nonconsented_chat`, ephemeral only. With valid retention consent use `consented_chat_and_derived_traces`; per-message first durable admission and earliest personal-source expiry govern. Access End/idle expiry does not silently extend retention or impose an absolute conversation age. |
| DE-11 consent proof | Minimal purpose/notice/decision evidence uses `consent_proof`; retain only while its mapped dependent processing/records and authorized recoverable copies require it. Withdrawal stops consent-authorized processing; evidence retention cannot restore consent. |
| DE-12 lead/brief | `brief_and_lead`, first durable creation for that accepted purpose, with earlier copied-source expiry preserved. A booking-linked brief is not automatically calendar history; creating it requires its own authorized purpose/consent. |
| DE-13 booking lineage; DE-15 slot selection; DE-16 booking record | Necessary scheduling/reconciliation fields use `booking_and_calendar`. Final known completion/cancellation supplies the proposed terminal anchor; unresolved reservations keep minimum justified state and a necessity-review obligation, not an indefinite full payload. Marketing/brief copies and verification material are separately mapped. |
| DE-14 email challenge | Revision-bound proof fields follow the separately approved short challenge/security lifetime; necessary delivery/reconciliation fields inherit the booking purpose. Never retain raw challenges as calendar history. Exact post-expiry verifier/dispatch-store disposition remains open. |
| DE-17 external intent | Each allowed payload field keeps its source purpose/class and earliest applicable expiry. Redacted action/result evidence uses its explicit audit/operational subpurpose; reservations retain only approved reconciliation fields. Durable intents cannot smuggle ephemeral chat or generic payload snapshots into PostgreSQL. |
| DE-18 availability projection | `availability_and_handoff`, ephemeral current projection only; validity cannot exceed current intent/eligibility/suppression bounds. No presence trail or durable reconstruction of old projections. |
| DE-19 handoff | Routing/assignment state uses `availability_and_handoff`; consented context keeps the source chat/brief expiry and transfer consent. Alert/provider copies require their own permitted inventory and verified handling. Handoff does not create a longer transcript. |
| DE-20 deletion request | Minimum scope/suppression keys use `deletion_evidence_and_tombstones`. Minimal closed rights-case outcome uses the proposed rights-accountability subpurpose of `audit_and_operational_copies`, with no transcript/body copy or default identity-document collection. Different purposes have separate disposition; completion cannot erase suppression still needed for recoverable copies. |
| DE-21 audit event | Select ordinary operational, security/authorization, rights-case or specifically reviewed incident/legal preservation subpurpose. No generic longest-period choice. Actors/object references remain identifying where linkable; no proof/body/email/URL dump or copied chat retention. |
| DE-22 staff availability intent | `availability_and_handoff` governs the minimal explicit intent; necessary staff links retain identifying protection. The schedule's proposed settled-expired-intent cleanup applies only once settlement is known. Uncertain on/off reservations stay restricted and require reviewed necessity; current validity, staff profile cleanup and audit evidence are separate. |

### Copy, expiry and recovery resolution

A receiver, derived record, cached projection or external intent cannot choose a
new expiry merely because it has a new ID. Personal copied fields retain their
source boundary; independently necessary recipient-purpose metadata must have a
separate accepted binding. Mixed-purpose records require field-group segregation
or deletion/redaction at the earliest applicable boundary, never the longest one.
The approved backup window is residual protected-copy handling, not ordinary-use
retention. The proposed 30-day window remains unadopted and cannot describe an
unknown provider. Recovery must suppress deleted/expired fields before serving;
immutable audit identifiers/checksums remain personal when still linkable.

Finite necessity reviews for unknown provider work cannot renew expired content,
credential validity or consent. A legal hold follows the security contract's exact
scope/basis/approver/next-review requirements; no automatic hold is inferred from
an error, foreign key, audit requirement or business state.

[EDPB purpose/minimisation/storage guidance](https://www.edpb.europa.eu/sme/learn-the-basics/data-protection-basics_en)
and [Commission principles guidance](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en),
checked 2026-10-08, support purpose-based limitation. This field-group mapping is a
Hengshi engineering proposal; neither source prescribes its particular periods.
Exact bases, release-accountability retention, proof-store cleanup, notices,
provider/copy windows and physical mechanisms still need their applicable review
and integrated acceptance. No live collection, persistence or migration is enabled.

### Proposed proof and challenge disposition — 2026-10-09

Status: DOING; independently reviewed proposal. This supplies the previously open DE-08 and
DE-14 disposition rules. It changes no access lifetime, retention period, consent
basis, operational grant or recovery method. The earlier record-purpose review
does not cover this addition. The separate [13-input independent review](../../../output/research/proof-disposition-2026-10-09/independent-review-proof-disposition-v1.json)
has bounded consistency PASS with no consequential findings at manifest SHA256
`7ba14c16d4200890c5a46a12d3ccc09246161ac3b4f1cfe1649a3e59ef966899`.
This receipt reference follows the frozen proposal bytes; actual store/copy/finite
cleanup bindings and integrated founder acceptance remain required before
implementation. No operational deletion, legal clearance or new grant follows.

Separate the current verifier from business outcome and replay reservations.
A verifier can establish only the currently admitted process/generation; retaining
an operation's unresolved outcome never requires keeping its old credential usable.
The existing visitor, booking, challenge and staff clocks remain distinct.

| Field group / event | Proposed disposition |
|---|---|
| DE-08 current visitor proof verifier | Retain only while its exact process/generation can authorize the admitted purpose. Use the existing sensitive one-way verifier representation; never persist its raw bearer. A non-consented chat's verifier, CSRF and replay state remain on the bounded ephemeral path with no snapshots or durable copies. Consent to transcript retention does not itself permit durable credential storage. |
| Proof rotation, revocation, authoritative End or expiry | Fence the old generation before any later admission or disclosure. Retire its verifier from the active lookup in that same guarded authority transition; late requests cannot revive it. Remove obsolete verifier/CSRF material as part of retirement. If physical removal is uncertain, record cleanup as pending under restricted handling while the authority remains fenced; never report complete deletion or extend access. |
| DE-14 email challenge consumption, expiry or replacement | Invalidate and remove the retired challenge's verifier through the guarded single-use transition. A newer email revision or replacement cannot reuse it. Preserve only separately necessary, purpose-bound delivery/action/result and reservation evidence; the retired secret or its verifier is not scheduling history. Existing challenge extension/admission rules control whether the challenge is still live. |
| Pending issuance, delivery, promotion or provider operation | Retain the minimum already-permitted operation identity, generation, reservation and reconciliation outcome until known settlement and mapped disposition. Do not retain a raw credential or payload as reconciliation evidence. If a dispatch genuinely requires a secret, use only its separately reviewed protected dispatch facility/lifetime; this proposal grants no general queue, email-provider or backup copy. |
| Settled replay/retirement record | Keep only what its approved purpose and finite replay/disposition window require. Removing a verifier cannot erase single-promotion, single-use or uncertain-effect evidence while it is still needed. Conversely, that evidence cannot become a longer transcript, durable non-consented visitor history or a new access grant. Unknown necessity or copy handling keeps the affected write/transfer denied. |

The guarded transition must resolve verification racing expiry, replacement,
consumption or End across workers. Check current generation, deadline and purpose
at admission, and enforce the existing delivery fence for already-admitted work.
Deleting a hash asynchronously without that authority check is insufficient.
An incomplete cleanup worker, restored record or delayed response cannot recreate
an active lookup for the retired generation. Missing proof state remains denial,
not permission to regenerate it from a selector, email or retained transcript.

Any permitted durable verifier copy is sensitive and linkable, and needs its own
approved storage/copy binding; no durable facility is selected here. At retirement,
ordinary authentication use ends immediately. Residual permitted copies follow the
accepted suppression and recoverable-copy policy before restored traffic; they
cannot be restored as active credentials. Unknown external copies remain unknown,
and the proposed backup window is not a credential-validity extension. Ephemeral
classes cannot enter that backup path at all. Release retained worker references
and exclude secrets from diagnostics; do not claim guaranteed memory zeroisation
from garbage collection or a successful database deletion.

This is a Hengshi disposition design, informed by the Commission's
[purpose, minimisation and storage-limitation guidance](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en)
and OWASP's [server-side session invalidation guidance](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#session-expiration),
checked 2026-10-09. Neither prescribes these field groups or proves their execution.
Exact physical stores, transactional retirement, copy inventory and bounded
cleanup/reconciliation profiles still need reviewed planning from the accepted
definition; disposal cannot rely on an unbounded best-effort worker.

After application authorization, exercise the actual issuer/store/request and
delivery boundaries: consumption racing another verification; rotation with a
lost response; End/expiry during pending work; delayed retired-generation replies;
cleanup/store failure; and quarantined restore with retired verifiers. Verify both
denied old authority and preserved truthful business outcomes, including no
non-consented durable copies or secret-bearing diagnostics. No runtime or prose
tests, new schema, table, migration or operational deletion are performed here.


## Public text projection profile proposal — 2026-10-08

Status: DOING. The [25-input independent review](../../../output/research/knowledge-extraction-profile-2026-10-08/independent-review-knowledge-extraction-profile-v1.json)
gives bounded logical-consistency PASS for this projection and the paired
extraction proposal at frozen inputs. Closed encodings, adapters, calibration,
actual-boundary enforcement and integrated/founder acceptance remain pending.
This later receipt-reference update is outside those inspected bytes. This refines DE-01's typed content and the
existing publication preparation input. It introduces no public endpoint,
artifact kind, database table, editor package or permission. Existing reviewed
bytes and their exact review scopes remain preserved.

The [closed projection encoding](public-text-projection.schema.json) and paired
[private extraction-map encoding](knowledge-extraction-map.schema.json) now have a
[separate 34-input bounded representation review PASS](../../../output/research/knowledge-extraction-shapes-2026-10-08/independent-review-knowledge-extraction-shapes-v1.json).
This covers their shape and validator boundary, not aggregate/encoded-byte limits,
source exclusion, actual compilation or safe AI. Registration, adapters, calibrated
profiles and integrated/founder acceptance remain held. This later reference
paragraph is outside both logical and encoding review inputs.

### One explicitly public input for text consumers

Recommendation: preparation constructs one closed `public_text_projection`
version 1 for each concrete approved source document, after company-facts
projection and all source/evidence/rights/classification gates. This is an
internal preparation representation, not a new downloadable/public artifact.
Its approved profile is registered with the preparation's configuration identity.
The renderer's complete document and its associated metadata/media may have
other reviewed typed profiles; this text profile neither replaces those nor
permits arbitrary fields to enter a public derivative.

| Field | Closed logical representation | Use |
|---|---|---|
| `schema_version` | Integer `1` | Profile format, not a new product release. |
| `title` | Public plain text, 1–160 Unicode scalar values | Same approved document title for semantic presentation and source label. |
| `sections` | Nonempty ordered array of closed section objects | Approved text order, not a dictionary traversed by reflection. |
| `sections[].section_key` | Unique document-local registered identifier using the existing restricted-ASCII/96-character profile | Stable identity within this immutable projection; no access grant. |
| `sections[].heading` | Public plain text, 1–160 scalar values | Visible section heading; guidance must retain it when needed to qualify a claim. |
| `sections[].units` | Nonempty ordered array of closed text-unit objects | Units remain in the document's reviewed order. |
| `sections[].units[].unit_key` | Unique document-local registered identifier under the same profile | Resolves approved extraction/context references only. |
| `sections[].units[].text` | Public plain text, 1–4,096 scalar values | Whole reviewed paragraph, list item, evidence/status note or limitation. |

All objects are closed. A unit contains only `unit_key` and `text`; a section only
`section_key`, `heading` and `units`; the root only the three listed root fields.
These scalar ceilings reuse the knowledge representation's proposed limits;
encoded-byte/parser/work ceilings and named-workload calibration remain separately
required. Valid nonblank Unicode, unique keys and complete meaningful coverage
are semantic checks, not consequences of shape alone. Oversized text cannot be
silently shortened: author a meaning-preserving revised representation and obtain
its required review, or hold preparation. Ordinary website text is not silently
cut to fit a guidance limit.

The source document's existing revision/content digest is resolved through the
same admitted preparation/manifest binding. The text projection does not claim
that hashing this subset reproduces the complete source document digest, and
cannot redefine `content_sha256`, mint a source revision or alter approval.
Record the exact projection/configuration association in the private preparation
plan; a copied label or client-supplied digest cannot establish it.

### Content categories and private separation

The approved route/content inventory, not a new type name in this projection,
determines each document's category. The private extraction plan must preserve
these category-specific obligations:

| Existing category | Required contextual information when the category is used as guidance |
|---|---|
| Home, service index, wing, service and industry information | Formal approved offer/scope, exclusions, delivery/evidence status and limitations; a reserved room or category never becomes delivered work. |
| Verified Work | Actual reviewed result, relevant context and limitations; its evidence/rights record remains private and must be current. |
| Hengshi-owned Demo | Explicit demonstration classification and limitations; no inferred client result or production assurance. |
| Expert/profile or specialist editorial/Insight | Only eligible public statements and approved attribution; qualifications, primary support, dates/cadence and scope follow the content contract. A private staff principal/review record is not a public profile. |
| Trust | Distinguish requirement/target, implemented evidence and its limits; no inferred certification, legal compliance or guarantee. |
| Company, Contact, Book and policy/utility pages | Only eligible static public information after applicable notice/contact review. Live staff, slot, booking, consent, account, retention or request state is never fabricated from static prose. |

Every concrete release route is either intentionally excluded from guidance with
private review evidence or covered by its registered public text/extraction
profile. A category listed here grants neither indexability nor source permission.
Missing category mapping, rights, mandatory context or required source content
holds that preparation; demo records remain usable only in their authorized local
context and cannot fill production evidence gaps.

Private owner/reviewer/approval references, evidence uploads, private contacts,
company registrations/address/validity excluded under D-076, chat/booking records,
credentials, draft/withdrawn data and controlled defense are absent. Semantic
review must also prevent those facts being disguised inside allowed public strings.
No paragraph, heading, caption or publication derivative bypasses source privacy
and disclosure duties merely because its field is allowlisted.

The source-field extraction plan and contextual passage obligations are defined
in the [publication extraction profile](PUBLICATION_CONTRACT.md#knowledge-source-extraction-profile-proposal--2026-10-08).
Exact closed-schema/editor/renderer adapters and per-document compiled projections
need later representation and real-boundary evidence. This proposal creates no
UI, physical storage, public content, provider transfer or working AI pipeline.
