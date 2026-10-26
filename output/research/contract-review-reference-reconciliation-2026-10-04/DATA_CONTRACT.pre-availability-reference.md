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

Entra principal/role mapping, session revocation and dormant emergency-account
activation reference private identity records. No local visitor user table, visitor
password, upload record or general administrator publication bypass is introduced.
Exact identity proofs and audit/credential policies remain security/legal gates.

## Conversations, consent and handoff

Without retention consent, conversation and replay state exist only in the bounded
ephemeral path. A durable transcript, message index, job payload or diagnostic copy
would violate that boundary. Ephemeral loss expires that session; it is not rebuilt
from PostgreSQL. Provider retention/no-training policy must independently comply.

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
