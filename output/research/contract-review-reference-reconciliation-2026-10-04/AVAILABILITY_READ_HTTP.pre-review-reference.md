# Public department availability read — v1 proposal

Status: DOING. Proposed 2026-10-04 for existing IF-PRESENCE-01, FR-009 and
AF-02. No handler, staff declaration, account, permission or publication is
implemented. This proposal requires independent review and integrated acceptance;
it does not itself approve public freshness disclosure or select timing limits.

The cause is explicit in [process-fields.csv](process-fields.csv): the public
state codes, department-key mapping, freshness disclosure and stale handling are
unresolved. This refines those wire choices while retaining the current
[availability guard](AVAILABILITY_CONSISTENCY.md), [data records](DATA_CONTRACT.md)
and [security/privacy boundary](SECURITY_PRIVACY_CONTRACT.md). Actual timing,
clock, physical consistency and operational-policy evidence remain prerequisites.

## Request and public scope

`GET /api/v1/departments/{department_id}/availability` has no query parameters
or request body. Unexpected query parameters/nonempty body produce 400 before
lookup. No visitor account, chat session, consent or private-process proof is
needed. Credentials cannot broaden the public projection or grant a staff action.
The read creates no session, sets no authentication cookie and changes no intent.

Proposed mapping reuses the five existing canonical wing route IDs directly;
these are public inventory selectors, not staff IDs or new department records:

| department_id | Existing canonical wing path |
|---|---|
| ROUTE-WING-STRATEGY | /services/strategy-transformation |
| ROUTE-WING-DIGITAL | /services/digital-products-growth |
| ROUTE-WING-AI-DATA | /services/ai-data-automation |
| ROUTE-WING-IMMERSIVE | /services/immersive-creative |
| ROUTE-WING-CLOUD-TRUST | /services/cloud-reliability-trust |

Validate one URI-decoded selector without trimming, case folding, aliases or a
second decoding pass. Reject decoded separators, percent/dot/control sequences;
never use the selector as a filesystem path, storage URL or SQL expression.
A well-formed selector outside the current allowed public inventory, or a held,
retired or unavailable-to-public department, gets the same 404 without private
existence/reason details. Edge rejection may give generic 400/404 without a success
body. An authority outage is not proof that a known department is retired.

The [canonical inventory](../../phase-1-foundation/06-canonical-route-inventory.json)
controls the mapping and actual serving eligibility. A listed key, drawn room,
published service page or valid schema alone cannot establish live assistance.
Renaming/publication changes require reviewed mapping and compatibility handling;
the proposed table does not activate all wings or override held content.

## Response and meaning

Application responses use UTF-8 JSON, `Content-Type: application/json` and
`Cache-Control: no-store`. A 200 body contains exactly `department_id` and
`availability`; the echoed key must match the requested permitted department.
Producers must emit unique member names and valid Unicode/UTF-8; serialization
cannot produce duplicate members, invalid scalar sequences or non-JSON values.
Before schema validation, consumers must reject malformed UTF-8/JSON, duplicate
object member names at any depth (including equal names expressed with escapes),
and invalid Unicode scalar sequences such as unpaired surrogates. Do not silently
replace invalid bytes or collapse duplicate members with a last-value-wins parser.
Apply approved raw-response/resource bounds before decoding. A decoding failure
clears the live offer and retains Book/Contact recovery; no partially decoded
value, previous positive response or apparently schema-valid normalized object
can establish fresh availability. The actual strict-decoding mechanism and bounds
remain implementation prerequisites, not behavior implemented by this schema.
The [closed body schema](availability-read.schema.json) describes the following:

| availability variant | Exact fields | Meaning |
|---|---|---|
| available | state = available; expires_at = UTC instant | A guarded live offer was verified for this department at the server decision point. |
| unavailable | state = unavailable | No verified live offer is currently presented; this does not assert that every employee is offline. |

`available` requires every current-authority, exact-intent binding, expiry and fresh
suppression condition in AVAILABILITY_CONSISTENCY.md. `unavailable` collapses normal
off, absent/expired/stale/suppressed/uncertain live evidence after public department
eligibility is established. It carries no reason, count, employee identity,
setting/revision, Teams status, queue, calendar or private declaration timestamps.
If public eligibility itself cannot be established, return the safe 503 error,
not a guessed 200/404. A known negative declaration is not inferred from an outage.

The proposed `expires_at` is the effective public offer-freshness bound, not a
disclosure of the private declaration's original expiry. It cannot exceed any
applicable current-authority, intent, projection, signal or eligibility bound.
Its calculation, disclosure review and approved maximum lifetime remain held;
there is no default number of seconds. No positive result is permitted until those
inputs and the required guard/clock/stale-handling proofs are accepted.

The proposed timestamp profile uses calendar-valid RFC 3339 UTC with uppercase
T/Z, seconds and optional fractional seconds. No local offset, month label or
invented timezone is accepted. Normal seconds 00–59 are used; leap-second handling
would need a reviewed extension. A timestamp-shaped regex is insufficient:
assert real date-time format and calendar validation before accepting it. A
well-formed timestamp does not prove future validity or actual server authority.

A live offer is not a reserved specialist, acknowledged handoff, appointment,
response promise or staff directory. Handoff still independently rechecks current
eligibility, approved assignment, consent and operation authority. Going unavailable
does not cancel/end/delete an existing conversation, handoff or booking.

## Freshness, caching and conditional requests

Clients request unconditional GETs and accept only a verified 200 matching the
current department and current read attempt. Superseded/out-of-order responses
cannot restore a positive indicator after a newer negative result, navigation or
release-policy change. Transport errors, malformed/mismatched bodies or unsupported
versions clear the live offer and retain the approved Book/Contact alternatives.

The positive presentation stops by the effective expiry and earlier on known loss
of validity. Wall-clock comparison alone is not sufficient: reviewed clock
uncertainty, response transit/age, background/history behavior and detection bounds
must govern presentation. If these cannot establish remaining validity, do not
present a live offer. Reconnect, repaint, reread or replay never resets the anchor.
The exact timing/clock method and measured bounds remain definition inputs; this
proposal does not claim instantaneous revocation of an already delivered response.

Controlled serving/service-worker layers do not reuse stored positive or negative
responses for a new read. No ETag, Last-Modified, positive cache TTL or stale-if-error
policy is selected. `no-store` does not erase a screen or guarantee privacy against
a nonconforming intermediary; server guards and client stale handling remain needed.

Apply RFC 9110 precondition syntax/precedence against current public representation
eligibility at the guarded read boundary. Without emitted validators, specific
If-Match tags do not match and give 412; If-Match * only matches an existing permitted
representation. If-None-Match * on that representation gives bodyless 304, including
when the current availability is unavailable; no tag proves a staff state. Ignore
If-Modified-Since/If-Unmodified-Since when no usable modification date is available.
An application consumer cannot treat 304 as fresh live evidence or extend an older
expiry; obtain an unconditional 200 before offering live assistance again. Error
precedence and invalid conditional syntax require actual HTTP integration tests.

This covers GET application representations only. HEAD/OPTIONS/CORS, routing,
rate limits, transport/resource limits and gateway error bodies require shared
edge/security integration. They cannot mutate availability, disclose private
diagnostics or make a non-200 response into a live-offer proof.

## Closed application errors

An error body contains only `error`, with exactly the correlated strings below.
No department/private identity, raw parameter, exception, provider message,
request proof or free-form diagnostic is returned.

| HTTP | code | explanation | retryability |
|---|---|---|---|
| 400 | AVAILABILITY_REQUEST_INVALID | The availability request is invalid. | correct_request |
| 404 | AVAILABILITY_DEPARTMENT_UNAVAILABLE | This public department is unavailable. | refresh_context |
| 412 | AVAILABILITY_PRECONDITION_FAILED | The availability request precondition failed. | correct_request |
| 503 | AVAILABILITY_READ_UNAVAILABLE | Public availability information is temporarily unavailable. | retry_read |
| 500 | AVAILABILITY_READ_FAILED | Public availability information could not be verified. | stop |

These labels describe permitted recovery, not automatic retry or handoff. Recheck
the current permitted context before a later read; no retry interval or response
SLA is invented. A normal 200 unavailable result is distinct from service failure.
Error details remain nonpublic under their applicable audit/classification policy.

## Evidence required before acceptance/implementation

The fixture script checks this proposed body's state/expiry correlation, calendar
format, closed projections and error variants only. It does not execute a handler,
HTTP headers/status/preconditions, permission guard, clock, PostgreSQL, Redis or
Teams. Do not equate this artifact result with truthful runtime availability.

Later actual-boundary tests must cover every current-authority guard interleaving,
expiry during waits/transit, wrong department/out-of-order response, clock uncertainty,
warm/service-worker/history caches, conditional 304/412, unauthorized private-field
disclosure, taxonomy withdrawal, signal outage, admission uncertainty and retained
handoff/booking truth from the consistency protocol. No screenshot of an available
label or mocked response can establish these guarantees.
Raw HTTP/client cases must also inject duplicate top-level and nested members,
escape-equivalent member names, malformed UTF-8 and unpaired surrogate escapes;
observe rejection before schema use and live-offer clearing with recovery retained.
The present shape fixtures cannot prove these raw-decoding outcomes.

Held inputs are the public timestamp/disclosure and key/profile acceptance,
effective lifetime/clock/detection and request/resource bounds, aggregation/grants,
admission/fencing/restore mechanism, exact account/API capability, legal retention,
actual HTTP/edge enforcement and integrated Phase 1 approval. Alias ownership stays
undecided; B01, QA revision exception, provider/spend, commits and deployment gates
are unaffected. No application implementation is authorized by this proposal.

## Primary evidence checked 2026-10-04

Context7 `/python-jsonschema/jsonschema` and official [validator guidance](https://python-jsonschema.readthedocs.io/en/stable/validate/)
confirm format checking is opt-in and missing optional checkers can otherwise pass.
The fixture requires the existing date-time checker; no installation/version
selection is made. [RFC 3339 §5.6](https://www.rfc-editor.org/rfc/rfc3339.html#section-5.6)
supplies timestamp grammar, [RFC 9110 §13](https://www.rfc-editor.org/rfc/rfc9110.html#section-13)
supplies preconditions, and [RFC 9111 §5.2.2.5](https://www.rfc-editor.org/rfc/rfc9111.html#section-5.2.2.5)
supplies no-store semantics. Minimal states/mapping/freshness/error projection are
Hengshi proposals, not rules asserted by those standards.
[RFC 8259 §§4/8](https://www.rfc-editor.org/rfc/rfc8259.html) documents duplicate-name
interoperability and Unicode risks; the stricter rejection profile above is a
Hengshi requirement, not a claim that JSON Schema can inspect discarded raw members.
