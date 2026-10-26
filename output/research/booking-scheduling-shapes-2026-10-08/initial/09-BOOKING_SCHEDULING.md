# Discovery scheduling lifecycle — v1

Status: DOING. Proposed 2026-10-08; independent review and integrated founder
acceptance remain required. This completes a logical lifecycle proposal for the
existing IF-BOOK-05/06/08/09 interfaces, not their final wire formats or handlers.

The [correction-2 independent receipt](../../../output/research/booking-scheduling-lifecycle-2026-10-08/final-independent-review.json)
records bounded logical-definition PASS at its frozen inputs, closing BS01/BS02.
This later reference is outside those inspected bytes. Exact wire/resource/policy
bindings, actual account capability, enforcement and integrated acceptance remain held.

## Authority and scope

[FR-004–FR-007/019](../../phase-1-foundation/01-product-requirements.md),
[BF-01C/D/E](../../phase-1-ux-architecture/FLOWS.md#bf-01c-availability-and-slot-selection),
[booking data rules](DATA_CONTRACT.md#booking-and-provider-transactions) and the
[interface catalogue](INTERFACE_CATALOG.md#booking-lineage-and-external-effect)
control meaning. The qualification/email refinements in that catalogue and the
[private proof/status profile](PRIVATE_PROCESS_PROOF.md) control current process
authority, revision, replay and minimal status. D-076 changes conversation timing,
not booking access or calendar rules. D-068 still defers Azure/AWS deployment.

Keep exactly six qualification fields plus the separate consent element, a
30-minute discovery occurrence, one lineage and explicit visitor confirmation.
No required name, telephone, account, upload, AI conversation, budget or cancellation
reason is introduced. No provider subscription, permission, new endpoint or
production implementation follows from this proposal. MA-006 retains actual
mailbox/calendar/meeting authority and capability verification.

## Scheduling authority and configuration

The scheduling service derives candidate slots from an approved private calendar
policy, eligible service owner/backup, complete fresh provider evidence, and all
local held/confirmed time reservations. Teams presence is not a calendar, ownership
assignment, working-hours policy or reservation. A free/busy result is observation,
not a guarantee that a subsequent write will find the interval free.

The private, revisioned policy must identify the wing and eligible owner/backup
mapping, actual organizer/calendar, organizer timezone, supported meeting route,
working periods/exceptions, booking horizon/minimum notice, buffers, and permitted
reschedule/cancel cutoffs. Every required value must be explicit and validated;
missing policy or unknown calendar coverage cannot become unrestricted availability.
This proposal selects no working days, 24-hour cutoff, lead time, owner, mailbox,
paid plan or backup priority. Those are approved operating configuration, not values
inferred from the visitor's desired timing or browser clock. Account activation and
real team values remain later MA-006/production preparation; unresolved product
policy choices must be presented before their adoption, not invented by fixtures.

An offer privately binds the exact policy revision, scheduling resource and owner
mapping used. Changed policy or owner eligibility invalidates dependent unadmitted
offers/reviews, without undoing confirmed truth or forgetting unsettled work.
New-booking eligibility and maintenance of an existing booking are separate scopes:
a withdrawn public service cannot create new slots, but cannot silently remove
currently authorized cancellation/status/reconciliation of its existing booking.

## IF-BOOK-05 — availability, not a hold

This remains an authorized, no-store private GET under the common proof/browser
read boundary. Its selected purpose is initial booking or rescheduling of the
same lineage; no caller owner, mailbox, calendar, attendee or provider endpoint is
accepted. A bounded time window and display timezone may constrain the requested
view only. Exact query encoding, bounds and closed response/error shapes belong
to its later wire profile. The query cannot admit a booking, change qualification,
verify email, advance a business revision or invoke a provider mutation.

For initial booking require current ownership, applicable verified email revision,
valid six-field qualification and current booking-purpose authority; permit the
VERIFIED/NO_AVAILABILITY/SLOT_SELECTED stage only with no unresolved calendar intent.
For rescheduling require current authority over the confirmed occurrence, an
approved reschedule capability/policy and no unresolved create/change/cancel.
The response records its purpose and source lineage revision; neither is permission
to execute a later write. Recheck those conditions at response admission as well
as query start; late work cannot restore withdrawn access or disclose old slots.

Return only 30-minute UTC intervals and non-bearer, own-lineage slot references,
with the authorized display context. References resolve an immutable private
binding to exact instants, owner/calendar, policy and qualification/email/purpose
revision. They do not expose those private identifiers or authorize another process.
Do not accept a time copied from a card, recompute the interval from a local label,
or silently substitute an owner/backup/instant when the old reference is invalid.

Distinguish a complete eligible search with no slots from an unavailable/incomplete
search. Missing pages, permission failure, provider errors, unknown reservations,
or incomplete owner evidence are not an empty calendar. Do not return a partial
slot list as complete; a bounded continuation must disclose that more periods/results
remain. No raw calendar titles, other attendees, free/busy records, staff directory,
provider reason or meeting URL enters this projection.

The existing NO_AVAILABILITY branch is a truthful visitor presentation for a
complete empty search; GET itself cannot commit that lineage transition. Existing
status labels remain supported where an authorized mutation has recorded them.
A visible choice likewise does not durably establish SLOT_SELECTED. Availability
reads may maintain bounded derived reference/cache bookkeeping, never create a
business hold or new authority. Reads cannot renew process access or retention.

There is no new offered-slot or selection countdown in this proposal. Slot references
remain subject to current process/policy/qualification and real calendar eligibility;
server bookkeeping loss or changed eligibility triggers fresh lookup/review with
permitted input preservation. That is not permission for an inaccessible hidden
system timeout. Any later reference/selection expiry must meet the accepted warning,
More time and progress-preservation requirements before adoption. Finite reference,
page, worker and byte limits still need an explicit resource profile, without
silent eviction of live or uncertain records or borrowed email-extension capacity.

## Visitor time and review

Store and compare UTC start/end; the end is exactly 1,800 elapsed seconds after
start. Derive the visitor's labels from an explicitly confirmed supported timezone,
including calendar date, zone name and UTC offset for each instant. Repeated autumn
local times need their distinguishing offsets; nonexistent spring local times
cannot be accepted as instants. Organizer working-hours rules use the separately
approved organizer zone and transition rules, not the visitor's zone.

The visitor can change the display zone without changing the selected UTC interval.
A changed interval, qualification, purpose, policy or relevant occurrence requires
a new authoritative review. The browser's guessed zone is a visible suggestion,
never identity, location, scheduling permission or server time. Support an explicit
UTC display when browser-zone detection fails; do not silently use server-local time.
Timezone identifier set, aliases, IANA/Windows mapping and compatible database/runtime
versions need dated wire/adapter evidence before selection; they are not inferred
from Microsoft accepting a mailbox-specific timezone name.

Prepare a server-authored review from the exact current qualification/consent,
wing, selected interval and confirmed display timezone. It restates date/time,
duration, organization/role/outcome, wing and the exact applicable consent purpose,
with permitted correction controls and no new qualification questions. Its private
binding includes the current verified email revision, policy, selected slot and
lineage revision. The client receives only the own-process permitted review and
an opaque selection/review reference. A client hash, checkbox or claimed human
reading cannot manufacture that binding or a calendar reservation.

## IF-BOOK-06 — prepare, then deliberately submit

Refine the existing submissions interface with separate logical prepare-selection,
submit-booking and reconcile commands, not a new endpoint or an automatic GET write.
Preparation takes a current slot reference, display zone, expected lineage revision
and operation identity under current proof/Origin/CSRF. It revalidates eligibility
and stores the immutable private selection/review binding; atomically advance the
lineage once to SLOT_SELECTED. The operative selection/review binding uses that
resulting committed revision, with its earlier preparation revision retained only
as historical input. Preparation sends no invitation, creates no external calendar
event and reserves no owner time. Revising the choice invalidates the old
selection/review; same-operation replay cannot create a second selection or revision.

Submission is a separate deliberate action on that exact prepared review reference,
expected revision and new operation identity. The UI offers correction/back and
explicit confirmation before calling it. A changed form cannot be silently submitted
with an old review; preserve permitted values and require fresh preparation.

After raw command/authority admission, resolve the same scoped operation before
fresh-write revision checks. Existing matching typed intent only reconciles; changed
intent conflicts. For a new submit, under one atomic local fence revalidate current
object/purpose authority, qualification, verified email revision, selection/review,
policy, owner/calendar eligibility and the exact interval. Confirm fresh complete
provider observation under the capability profile; its age bound cannot be guessed.
A prior read does not substitute for this check. Serialize competing local admissions
for the same scheduling resource and overlapping intervals across all wings/lineages.

Commit BOOKING_PENDING, the immutable operation result/binding, private external
intent, and the time reservation together. The reservation interval includes the
configured buffers, not only the public 30 minutes. Use half-open intervals so
adjacency without buffer does not itself overlap. Enforce physical uniqueness of
operation/lineage intent and resource-time conflict in the durable store; an in-memory
lock, client disable or per-worker permit is insufficient. PostgreSQL range/exclusion
constraints are a candidate for overlap enforcement, not a selected migration or
extension: compatibility/SQLAlchemy/Alembic and concurrent rollback behavior need
verification before mechanism adoption.

No database transaction spans a provider network call. The provider read and write
cannot be made globally atomic with this database reservation. App-origin races
must be fenced locally; other applications/manual calendar edits remain possible.
Reobserve before dispatch and reconcile any collision/mismatch afterwards; never
claim an absolute no-double-booking guarantee from a free/busy query. Refusal or
known no-effect conflict preserves inputs and offers fresh selection/Contact.
Capacity alone cannot partly admit an intent without its outcome/reconciliation
and reservation allowance. Existing reserved email-extension resources remain isolated.

## Dispatch, confirmation and uncertainty

One authorized worker admission dispatches the one immutable intent after commit.
Check the current dispatch permission, policy/owner validity and explicit capability
profile before external admission. If a dependency is invalid before dispatch,
settle as definitely not sent only when no earlier admitted provider work is possible.
After provider admission, process expiry/withdrawal cannot establish non-execution,
delete its reservation or authorize a compensating cancellation. Reconcile minimum
permitted evidence under the admitted operation's separate lawful scheduling purpose;
private browser disclosure still requires current process authority.

Record operation-specific not-dispatched, admitted/uncertain and reconciled outcomes.
A lease, connection, worker, observation or retry deadline expiring is not proof that
external work failed. Missing acknowledgement, 429/5xx after admission, truncated
responses and uncertain timeout retain the intent/reservation. Do not create a new
operation or organizer event to escape uncertainty. Retry only after the adapter's
verified evidence establishes that the same immutable effect is safe to repeat;
provider deduplication assists but does not prove indefinite exactly-once effects.
SDK/transport retries, automatic reauthentication and job redelivery cannot bypass
this guard: repeated external writes need the same verified safe-retry decision.

CONFIRMED_QUALIFIED requires one correlated approved organizer-calendar/meeting
occurrence plus matching local qualification/consent, exact verified attendee,
owner/calendar, start/end/duration and required online-meeting capability/data.
An event ID, HTTP success, matching subject, echoed transaction ID, invitation being
sent, join link alone or attendee acceptance alone is insufficient. Evidence of
multiple matches, changed organizer/attendee/time or missing required meeting data
remains reconciliation failure/uncertainty, never a guessed winner.

The exact created result may supply authoritative evidence only where the adopted
adapter profile proves all required fields and identity correlation; otherwise read
back the same known event. Persist the matched provider version/evidence and local
confirmation atomically under the current intent fence. No confirmation means a
local pending receipt stays pending. A subsequent status read uses IF-BOOK-07's
minimal last-reconciled projection; a confirmed join URL needs a separately approved
minimal disclosure profile, never a public URL, log or status-schema addition here.

Alert/notification work has its own intent and permissions. An alert failure never
undoes confirmation or repeats the calendar write. Meeting creation may itself send
provider invitations; that is an external effect to minimize and authorize, not
an extra notification the application can assume it suppresses.

## IF-BOOK-08 — reschedule the existing occurrence

Require current authority over the existing confirmed booking and an approved
cutoff/capability. After current proof/object/action/disclosure checks, reconcile a
matching admitted operation before fresh revision/cutoff/candidate guards; replay
cannot allocate another review or alter pending truth. For a new preparation,
require current lineage state CONFIRMED_QUALIFIED and no unresolved create/change/
cancel under the atomic admission fence. A last-confirmed occurrence alone cannot
prove that condition or authorize overwriting RESCHEDULE_PENDING/CANCEL_PENDING.
Fresh submit-reschedule likewise requires that state/no-unresolved-intent guard,
its expected committed revision and the exact current prepared review.
Prepare-reschedule stores an exact replacement slot/review under
the same lineage using current proof/Origin/CSRF, an expected revision and a
separate operation. Advance the lineage once while preserving CONFIRMED_QUALIFIED
and its last reconciled occurrence; bind the replacement review to the resulting
revision. Preparation claims no new confirmed time or resource-time hold. Submit-reschedule explicitly confirms
that review, its expected revision and the last reconciled occurrence binding.
Recheck current policy, interval, owner/calendar and provider version before admission.
No new qualification entry, implicit attendee change or email re-verification occurs
through this action. Lost authority uses status/Contact recovery, not an email-only
authentication bypass or imported verification from another process.

Recommend updating the same organizer calendar event in place for the same owner,
attendee and meeting provider. A different organizer/calendar/meeting provider is
not a transparent time change; refuse and use authorized operations until a separately
reviewed replacement workflow exists. Do not implement create-new/cancel-old as an
unreviewed fallback or promise that two independent external writes are atomic.

Atomically admit RESCHEDULE_PENDING with immutable external intent, retain the old
occurrence reservation and reserve the replacement interval (including buffers).
Overlap with that same occurrence's old reservation may be permitted only under
the same locked intent; it cannot waive conflicts with other bookings. No second
reschedule/cancel/create may dispatch while this operation is unresolved. Provider
version/precondition support must be actually verified; changeKey existence alone
cannot prove compare-and-set or justify blindly overwriting a manual change. If
the adapter cannot bind the write to that observed version or an explicitly approved
exclusive-write facility, automated reschedule admission stays unavailable. A local
lock/read-then-write sequence is not a substitute for external conflict control.

While pending, display the old time explicitly as last reconciled, with the proposed
replacement and uncertainty where permitted; do not promise the old event still
exists unchanged. Promote the replacement only after correlated authoritative
provider evidence and local state agree. Then settle the intent, replace the last
reconciled occurrence and release only the old reservation known no longer needed.
A definitely failed/no-effect update preserves the old occurrence and releases only
the unused replacement reservation. Ambiguity retains both; automatic rollback is
another external write and is not implied by failure or a client Back action.

## IF-BOOK-09 — explicit cancellation

Cancellation first displays the exact currently authorized last-reconciled occurrence
and consequences; the visitor deliberately confirms its binding and expected revision
with an operation identity. No reason or repeated brief is required. After current
proof/object/action/disclosure admission, matching-operation reconciliation precedes
fresh guards and cannot repeat dispatch. A new cancellation requires current
CONFIRMED_QUALIFIED, no unresolved create/change/cancel, the expected revision,
current cancellation policy/authority and the exact same reviewed occurrence.
Bind its organizer/calendar/event identity, attendee, time and observed external
version to that immutable intent; admit CANCEL_PENDING, its intent and reservation
atomically. No conflicting time change may
start while it is unresolved. A matching replay never sends another cancellation.

Before external cancellation admission require a verified version-bound provider
operation, or an explicitly approved exclusive-write facility preventing conflicting
external edits from admission through actual effect completion or positively
established no-effect settlement, including uncertain in-flight work. Request send,
acknowledgement, observation/lease timeout and lost connection cannot release that
protection. If it is lost after external admission, retain uncertainty and the
required minimal reconciliation/reservation state; loss is not proof of cancellation
or no effect and cannot authorize fresh conflicting work. If neither conflict-control
alternative is established, automated cancellation admission stays unavailable with
permitted status/Contact recovery. A local lock,
read-then-cancel, changeKey presence or generic Graph cancel documentation cannot
establish that protection. Current provider evidence must still match the reviewed
identity/attendee/time/version; a mismatch refuses before cancellation rather than
being discovered only after its effect. Recheck the conflict-control facility at
worker dispatch; losing it cannot authorize blind cancellation or a guessed failure.
The adapter then cancels the organizer's exact known occurrence under its approved
capability; it cannot cancel another calendar item, recurring series or attendee
copy. Preserve the last-reconciled time as historical pending truth until authoritative
cancellation evidence and local state reconcile. An accepted request, generic 404,
absence from one page, notification delivery or local deletion is insufficient.

Positive evidence must be bound to the same organizer/calendar/identity and admitted
cancel intent: a provider-defined cancelled state, or scope-qualified absence/move
following the correlated cancellation where the verified provider profile defines
that as a settled cancellation. Loss of authorization, unknown pagination, moved
identifiers or mismatched resource scope cannot be interpreted as that evidence.
If the adapter cannot establish it, remain pending for authorized reconciliation.

Only then commit CANCELLED with null active occurrence and release the relevant
reservation when all associated work is known settled. Necessary historical outcome
records follow their existing retention policy; cancellation is not deletion, proof
revocation, conversation End or successful notification delivery. For unresolved changes retain RESCHEDULE_PENDING or CANCEL_PENDING and the last
reconciled occurrence; do not switch to the initial-create RECONCILIATION_ERROR
projection that requires a null occurrence. A reschedule/cancel that is proved to
have had no effect settles back to CONFIRMED_QUALIFIED under the same intent fence,
with a new lineage revision and its failure receipt; it does not repeat dispatch.
A cancellation that definitely had no effect preserves the prior confirmed occurrence. Do not treat
an already independently changed/cancelled event as this operation's success without
authorized correlation and truthful reconciliation of its actual state.

## Recovery, privacy and qualification

Same-lineage operation records remain recoverable while permitted current authority
can reconcile them, even after the original expected revision becomes stale. Current
status and historical operation receipts are distinct. Business cutoff passing cannot
block observation of an already admitted operation; it may block a fresh change.
Unknown old work cannot be bypassed by a new tab, operation, visitor process, restart,
restored database or guessed absence. IF-STAFF-07 requires its own approved booking
operations authority and authoritative evidence; it cannot manually manufacture email
verification, a slot, confirmation or cancellation from a screenshot/customer claim.

No email-only/public-link recovery mechanism is selected here. Lost private proof
stops disclosures and fresh visitor actions; permitted support and staff reconciliation
remain distinct. Exact proof recovery, action/link lifetimes and business cutoffs must
be approved before those controls appear in production. The original process, access
clocks and accessible continuation rules stay controlling; this proposal adds no
absolute visitor conversation limit or silent booking credential extension.

Bind scheduling lineage/selection/intent/reservation/outcome fields to the existing
DE-13/15/16 and booking_and_calendar purpose; credentials, email verifiers, consent
and optional brief/alert copies retain their separate mappings. Only minimum required
calendar invitation data crosses the approved adapter; no full qualification brief,
AI transcript, security credential, unrelated client or marketing consent is copied
by default. Exact field/notice/provider-copy retention requires adoption. Keep enough
minimal justified state to resolve uncertain effects, not indefinite full payloads.
A restored store must reconcile known provider effects before fresh dispatch; restore
cannot reset consumed intents, known cancellations or reservation conflict controls.

After implementation is approved, exercise the actual API/store/adapter/browser
boundaries: two lineages racing for overlapping buffered time; policy/owner/email
change after offer/review; multi-page provider failure versus empty; DST repeated and
missing labels; duplicate/reordered submit; current authority loss before/after provider
admission; unknown create/update/cancel with worker death; external manual edit;
reschedule overlap and retention of both reservations; organizer-only cancellation;
positive versus ambiguous absence; late acknowledgement after restore; notification
failure independent of calendar truth. Synthetic providers must model uncertainty,
not replace real authorized account-capability verification or assert live delivery.
No prose/hash/shape test proves these behaviors.

## Primary evidence and remaining definition

Checked 2026-10-08 with Context7 and official Microsoft Graph v1.0 documentation:

- [getSchedule](https://learn.microsoft.com/en-us/graph/api/calendar-getschedule?view=graph-rest-1.0) reports free/busy and does not support delegated personal Microsoft accounts. [calendarView](https://learn.microsoft.com/en-us/graph/api/user-list-calendarview?view=graph-rest-1.0) documents personal delegated read support. Neither proves a given account can supply this complete scheduling policy.
- [Create event](https://learn.microsoft.com/en-us/graph/api/user-post-events?view=graph-rest-1.0) supports delegated personal/work-school calendar writes and sends invitations when attendees are supplied. [Event resource](https://learn.microsoft.com/en-us/graph/api/resources/event?view=graph-rest-1.0) documents transactionId retry deduplication, version changeKey and isCancelled; this proposal infers no universal conditional-update or indefinite deduplication guarantee.
- [Online meeting capability](https://learn.microsoft.com/en-us/graph/outlook-calendar-online-meetings) is discovered from the calendar's allowed providers; an enabled online meeting cannot simply switch provider or be disabled through those properties. [Update event](https://learn.microsoft.com/en-us/graph/api/event-update?view=graph-rest-1.0) warns that replacing the body must preserve online-meeting data. A reschedule adapter should update only its intended time fields.
- [Cancel event](https://learn.microsoft.com/en-us/graph/api/event-cancel?view=graph-rest-1.0) is organizer-only, moves the item to Deleted Items and returns bodyless 202. [Immutable identifiers](https://learn.microsoft.com/en-us/graph/outlook-immutable-id) document an opt-in identifier format; case-sensitive, mailbox-scoped identity and move behavior must be verified in the actual adapter before correlation is accepted.
- [PostgreSQL 18 range constraints](https://www.postgresql.org/docs/18/rangetypes.html#RANGETYPES-CONSTRAINT) document exclusion of overlapping ranges. They protect local records, not transactions spanning an external provider. [RFC 9110 safe methods](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.1) support the no-business-mutation GET boundary; private transport/disclosure rules remain separate.

These primary sources describe capabilities, not Hengshi policy or account entitlement.
No Microsoft 365 prerequisite, SDK installation or provider/cloud choice is selected.
Remaining work: directional query/command/review/response schemas and HTTP/error profiles;
closed policy and adapter-evidence bindings; finite byte/page/reference/job/reservation
and retry/reconciliation accounting; exact timezone mapping; accessible expiry/progress
handling; approved proof-recovery/action rules, lawful provider/notice/copy mapping,
complete compatible graph and integrated founder acceptance. Real ingress, concurrency,
provider actions and load/accessibility qualification belong to later authorized work.

## Directional representation proposal — 2026-10-08

Status: DOING. The [scheduling schema](booking-scheduling.schema.json) refines the
four existing interfaces below; it does not replace the preceding reviewed logical
controls. Select the named `$defs` direction; the module root rejects instances.
These are proposed decoded representations, not final HTTP profiles or handlers.

| Interface | Request definition | Response definition |
|---|---|---|
| IF-BOOK-05 private GET | availability_query | availability_response |
| IF-BOOK-06 submission | submission_request | submission_response |
| IF-BOOK-08 reschedule | reschedule_request | reschedule_response |
| IF-BOOK-09 cancellation | cancellation_request | cancellation_response |

Every command and projection is closed. Unknown properties, client-authored owner,
calendar, provider identity, confirmation, proof/CSRF values in bodies, and copied
qualification in scheduling commands are rejected. Current proof and browser
admission remain outside these payloads under PRIVATE_PROCESS_PROOF.md. UUIDv4
operation and server references use the existing lowercase representation; slot,
view, page and review references are non-bearer own-lineage bindings, never grants.
Safe positive revisions and exact UTC calendar-valid millisecond instants reuse the
common and booking status modules. Spelling validity proves no allocation or access.

### Availability query and complete observation

The window query contains kind=window, purpose=initial|reschedule,
expected_revision, visitor_timezone, from_utc and until_utc. They constrain a
half-open [from_utc, until_utc) view; both bounds, a positive ordered interval and
an approved bounded horizon are mandatory semantic checks. The window must fit
current private policy. It cannot select a staff member or calendar. The page
query contains only kind=page, expected_revision and page_ref; its private binding
retains the original window, purpose, zone, policy and source revision. Changed
bindings require fresh availability, not substituted filters or a new hold.

These are decoded GET query values, not JSON request bodies. The later strict
query parser must reject duplicate/unknown keys, malformed percent encoding,
noncanonical integer tokens and invalid UTF-8, decode each value once and preserve
literal timezone characters (including percent-encoded +). It must not coerce
booleans, floats or repeated parameters into expected_revision. Exact raw query,
header/cookie, window-span, work, response-byte and view-storage limits and status
mapping remain for the bounded HTTP/resource profile; the JSON schema cannot
validate the raw request target. No unbounded query is authorized while those
limits remain unselected, and this appendix does not borrow email operation slots.

A slots projection carries source lineage_id/lineage_revision, purpose, zone,
window, observed_at, view_ref, one through 96 closed UTC slot records, and a
nullable continuation_ref. The 96-item limit is a proposed unmeasured page bound,
not a daily calendar capacity or performance result. A non-null continuation means
more application offer pages in that same authorized view. Null means no more
pages; it does not mean a previously returned offer is still selectable. Revalidate
current authority and all bindings before delivery and subsequent selection.

Return empty with [] and null continuation only when the entire requested window
has complete authoritative coverage and zero eligible offers. Provider pagination,
errors, partial coverage or unknown freshness cannot produce empty. Before paging,
establish complete coverage for the bounded view; application pagination is not
provider coverage. Offer pages must each contain at least one offer; the final
nonempty page has null continuation. Do not turn an empty filtered provider page
or an exhausted/stale page reference into a whole-window empty result. An expired
or changed view requires VIEW_CHANGED/refresh_availability, subject to current
access denial precedence. Identical item duplicates are schema-rejected; different
references to the same interval still require semantic deduplication. No slot is
held and no business revision advances by observing a view.

### Prepare, deliberate action and operation reconciliation

The prepare_selection and prepare_reschedule commands carry operation_id,
expected_revision, slot_ref and visitor_timezone. The submit_booking and
submit_reschedule commands instead carry operation_id, expected_revision and
review_ref. Preserve the earlier immutable private binding, resulting committed
review revision, distinct operation identities, explicit visitor confirmation and
fresh admission controls. Selecting a card or receiving a prepared receipt cannot
submit an external calendar mutation.

prepare_cancellation carries operation_id, expected_revision and visitor_timezone;
cancel_booking carries operation_id, expected_revision and review_ref. This
realizes the already required current cancellation review inside IF-BOOK-09;
it introduces no new endpoint, reason field, account or provider action. Reconcile
an existing same-kind operation under current authority before fresh guards. Fresh
preparation requires exact CONFIRMED_QUALIFIED, no unresolved create/change/cancel,
current proof/Origin/CSRF, applicable cancellation policy and verified capability.
It records an immutable review against the currently reconciled occurrence,
advances the lineage revision once while retaining confirmed truth, and binds the
review to that resulting revision. It creates no reservation, calendar effect or
external exclusion guard. A prior review is superseded; later submissions must
recheck all current identity/version/conflict controls from the preceding lifecycle.
Changing display timezone requires a new prepared review, never changing instants.

reconcile_submission, reconcile_reschedule and reconcile_cancellation carry only
kind and operation_id. They inspect the already admitted same-kind owned operation;
no expected_revision, replacement review, qualification or new side effect is
accepted. Current access still applies, even to a historically applied operation.
Exact operation-kind/intent equality and safe unknown-effect handling are semantic
requirements; a valid UUID alone cannot manufacture an operation or safe retry.

### Review projections and truthful receipts

A prepared receipt contains state=applied, receipt_kind=prepared, operation_id,
applied_revision and a required current projection. Historical applied_revision
records this preparation's single committed revision; it cannot be overwritten
with today's status. Current is either exact {state: unavailable} or state=known
with revision and the same-purpose server-authored review. Known requires current
authority and the still-active review from this originating operation, bound to
its resulting revision; current.revision must equal applied_revision here. If
superseded, invalidated or inaccessible, expose no old review; current unavailable
is not a submit grant. Reordered replies cannot restore an older review or access.

Book and reschedule reviews reuse the current six-field qualification and separate
booking-purpose consent by reference to booking-qualification.schema.json. Book
shows the proposed occurrence; reschedule shows the current last-reconciled and
proposed occurrences. Cancellation shows only wing_key and current occurrence,
without copying the brief, email, consent or optional reason. All review references
bind their exact purpose and stored data, not arbitrary client payload hashes.

Each occurrence exposes UTC start/end and server-generated local_start/local_end
objects with real date, millisecond clock and utc_offset_seconds. The schema bounds
offset spelling to +/-86400 seconds; this is not an accepted offset for every zone.
Validate the exact 1800-second elapsed duration, order, containment, zone conversion,
offset and local date/clock agreement against approved pinned timezone data. Render
both endpoint dates/offsets when needed for midnight or daylight-saving transitions;
never interpret a repeated local label without its UTC instant and offset. Browser
zone suggestion or Intl output cannot become scheduling authority. The key's bounded
ASCII spelling is separate from actual supported IANA keys and approved aliases.
Unknown zones return TIMEZONE_UNSUPPORTED; UTC is an explicit visitor-selected
fallback, never a silent substitution. A zone change only changes display labels.

[Python ZoneInfo documentation](https://docs.python.org/3/library/zoneinfo.html)
describes system IANA data or first-party tzdata fallback, including Windows' usual
lack of a system IANA database. The exact supported key set, canonical aliases,
calendar-adapter IANA/Windows mapping and pinned runtime/data graph still need
qualification before production. No tzdata package, version or upgrade is selected
or installed here. Missing data fails unavailable; it cannot use server-local time.

An accepted receipt contains state=applied, receipt_kind=accepted, operation_id and
applied_revision only. It means local pending-intent admission, not confirmed,
rescheduled or cancelled at the calendar. Use IF-BOOK-07 for current authoritative
lineage state; old accepted receipts do not restore old state. A pending receipt
contains state=pending and operation_id only and means the local outcome is not yet
established. Neither shape supplies an actionable review, provider identity or
meeting URL. A preparation operation can return prepared or pending; a submit/cancel
operation can return accepted or pending; reconciliation returns the exact original
kind's receipt or pending. Errors cannot be treated as evidence that admitted work
had no effect. Purpose/operation-kind matching is a handler duty beyond schema unions.

Error code/recovery pairs are fixed and closed, without arbitrary diagnostics,
private evidence or echoes. Availability SERVICE_UNAVAILABLE leads to fresh
availability; mutation SERVICE_UNAVAILABLE leads to reconciliation of the same
operation. Capacity denial cannot authorize blind retry of an uncertain admitted
write. Authorization-denial precedence, exact HTTP statuses, delivery/observation
limits and user recovery escalation belong to the later HTTP/resource profile.

### Evidence boundary

[Schema validation](https://json-schema.org/draft/2020-12/json-schema-validation#section-7)
with explicit UUID/date/date-time assertions checks representation, not field equality,
calendar policy, current access, complete provider coverage, reservations or effect
settlement. The focused scheduling fixtures exercise the validator offline with
synthetic data and reused qualification/common fixtures. They deliberately show
that wrong duration, revision equality and zone arithmetic can remain shape-valid.
Application boundary tests must reject those cases after implementation approval.
No schema-method count establishes a working booking service, accessibility,
privacy compliance, account capability, wire freeze or integrated Phase 1 acceptance.
