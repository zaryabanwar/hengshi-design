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

D-076 defers public registration identifiers, validity claims and the supplied
registered address. Private prepared facts may retain them for authorized admin
revision/review. Public derivatives must consume the [allowlisted publication
projection](PUBLICATION_CONTRACT.md#d-076-company-facts-public-projection--2026-10-07),
not the whole private object. The added `public_projection` schema definition is
unreviewed; earlier exact-input data/company reviews do not cover it. Current
owner/contact verification, actual authorization/projection and applicable notices
remain gates. Synthetic local content never grants production publication authority.

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
are unreviewed amendments; clocks, current-authority fences and cleanup still need
review and later runtime evidence. Access expiry does not determine every stored
record's retention or prove completion of an external/provider deletion.

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
| Record UUID | Exactly 36 lowercase hex/hyphen characters, with explicit UUID format assertion; reject rather than trim, case-fold or strip braces/URN prefixes. | Permitted issuer/allocation, object family, current proof/tenant/purpose and exact record binding. A shaped UUID, including Nil/Max, proves no allocated record or uniqueness; generation version remains unselected. |
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
