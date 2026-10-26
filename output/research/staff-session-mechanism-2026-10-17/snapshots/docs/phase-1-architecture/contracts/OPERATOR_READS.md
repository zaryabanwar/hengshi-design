# Staff operator reads — v1

Status: DOING. Proposed 2026-10-17 for the three existing list interfaces below.
This document owns their common query, projection, paging, cursor and prospective
HTTP/resource profile. [Staff security](SECURITY_PRIVACY_CONTRACT.md) retains
identity, action, object and purpose authority; [data](DATA_CONTRACT.md) retains
source/copy/expiry meaning; [handoff lifecycle](HANDOFF_LIFECYCLE.md) retains
business transitions. The [catalogue](INTERFACE_CATALOG.md#staff-publication-and-operations)
retains route identities and related capabilities. No endpoint, grant, key,
database change or application implementation is created here.

The [initial logical review](../../../output/research/operator-reads-2026-10-17/independent-review-operator-read-logical-v1.json)
requires OPREAD01: output checks must cover pagination dependencies as well as
returned rows. The [correction-1 logical review](../../../output/research/operator-reads-2026-10-17/correction-1/independent-review-operator-read-logical-v1.json)
has bounded PASS for its 14 frozen inputs, resolving that finding without a new
grant, copy-retention purpose or multi-request snapshot claim.
The [canonical-binding review](../../../output/research/operator-reads-2026-10-17/canonical-binding/independent-review-canonical-binding-v1.json)
has separate bounded PASS at 12 frozen inputs for this owner and the catalogue
references. This later review-reference update is outside those preserved bytes.
The later [wire review](../../../output/research/operator-reads-2026-10-17/wire/independent-review-wire-v1.json)
records OPWIRE01 and representation-only observations; its
[eight-input correction review](../../../output/research/operator-reads-2026-10-17/wire/correction-1/independent-review-wire-correction-v1.json)
has bounded PASS after restoring global admission before receive/authentication.
The [12-input field-binding review](../../../output/research/operator-reads-2026-10-17/field-binding/independent-review-field-binding-v1.json)
separately passes six dictionary references and three existing operation labels.
These review-reference updates are outside the preserved inspected bytes.
No receipt certifies policy/physical adoption, runtime enforcement or integrated
acceptance. Actual cursor/identity/fence mechanisms remain to be implemented and tested.

## Current authority and minimal membership

Every request needs a current authenticated staff session, explicit route action
and query scope, and current per-object/purpose/consent/assignment permission.
The four content roles and administrator are not an operational inheritance
ladder. Missing grants deny; queue visibility and people/group bindings remain
held. No general right to inspect unassigned requests is invented.

| Interface and existing GET route | Eligible work | Optional first-page filter | Minimal item fields |
|---|---|---|---|
| IF-STAFF-10 `/api/v1/staff/handoffs` | Durably admitted `requested`/`queued` handoffs under the approved queue-visibility purpose. | `wing_key`: one canonical wing below. | `handoff_id`, `revision`, `recorded_at`, `wing_key`. |
| IF-STAFF-16 `/api/v1/staff/alerts` | Existing alert-class intents with unresolved external outcome or recorded unsuccessful delivery still needing approved recovery/disposition, under lawful parent/operational purpose. Resolved/closed work is excluded. | `origin`: `handoff` or `booking`. | `intent_id`, `revision`, `recorded_at`, `origin`, `issue_class`. |
| IF-STAFF-18 `/api/v1/staff/bookings/exceptions` | Already-recorded unresolved/held/escalated exceptions under current exception/lineage/query purpose. Resolved work is excluded. A no-slot observation or unknown provider read does not itself create a record through GET. | `issue_class`: one booking class below. | `exception_id`, `lineage_id`, `revision`, `recorded_at`, `issue_class`. |

Canonical wings are `ROUTE-WING-STRATEGY`, `ROUTE-WING-DIGITAL`,
`ROUTE-WING-AI-DATA`, `ROUTE-WING-IMMERSIVE` and `ROUTE-WING-CLOUD-TRUST`.
A handoff with no admitted wing has explicit null; a filtered query matches only
an actual equal nonnull wing. Alert classes are `OUTCOME_UNKNOWN` and
`ACTION_REQUIRED`. Booking classes are `DUPLICATE`, `MISSING`, `MISMATCH`,
`ALERT`, `NO_SLOTS` and `OUTCOME_UNKNOWN`. These are minimal read classifications,
not new stored workflow states, provider acknowledgement or business success.
Exact stored-evidence mappings remain required; unknown mapping is unavailable.

IDs are permitted source UUIDs. Revision is the current positive source revision;
for booking exceptions it belongs to the exception, not its parent lineage.
`recorded_at` is immutable server record-creation UTC metadata, not visitor time,
exact arrival/commit order, response time or SLA. Source fields, immutability,
classification and physical store/column/index bindings require explicit review.
Existing common value helpers can supply representation only.

No list delivers name/email/organization/brief, transcript/message, consent/role
history, staff directory/contact, provider/debug payload, bearer/CSRF secret,
meeting URL, recovery command or arbitrary JSON. IF-STAFF-11 detail,
IF-STAFF-17 recovery, IF-STAFF-19 disposition and IF-STAFF-07 reconciliation keep
their own guards. Reading neither assigns/accepts/declines/ends work nor dispatches
or reconciles an effect, verifies email or confirms/cancels a parent operation.
It does not mark seen or renew staff idle/absolute, consent or retention clocks.

## Closed query and live pages

First page accepts no query or optional `limit` and the route's single filter.
Default limit is 25; supplied limit is canonical ASCII decimal 1–25 with no sign,
leading zero, whitespace or coercion. Names/enums are exact case-sensitive ASCII.
Reject duplicate/unknown/aliased parameters, empty values, bracket/array forms,
percent/plus encodings and stray separators. No sort, offset, owner, tenant,
raw-ID, SQL or free-text selector exists. A continuation has exactly one `cursor`
parameter; it cannot override filter or limit.

Apply current route/query and row/purpose authority **before** membership,
ordering, LIMIT and lookahead. Denied rows cannot leak through counts,
`has_more`, cursor or timing categories. Unknown source/permission/purpose or
classification is unavailable, not an excluded row or a falsely empty success.

Order descending by the unique immutable pair `(recorded_at, item_id)`, using the
handoff/intent/exception ID. First page fixes its highest eligible key as ceiling;
later pages require `key < after` and `key <= ceiling`. No OFFSET, arbitrary sort
or database transaction held between browser requests. Sequence allocation does
not prove PostgreSQL commit order.

Each page is a live coherent database observation. It is not a frozen multi-page
snapshot or complete export. Late commits, insertion, membership/authorization
changes and deletion can affect later pages. Refresh the first page for the
current head. End of page traversal means no further eligible row under this
page boundary at its observation, not that no work exists anywhere or forever.

One complete scoped observation yields at most `limit + 1` eligible ordered rows.
Return at most limit. `has_more` is true only with eligible lookahead, a full
page and a next cursor. Otherwise next cursor is null; an empty page requires
false/null. The closed logical result has `kind`, `items`, and
`page: {limit, has_more, next_cursor, consistency: "live"}`. Route kinds are
`handoff_queue`, `alert_exceptions` and `booking_exceptions`. No total, matched,
denied, scope inventory or hidden-row references are returned. The directional
encoding proposal below supplies closed shapes; actual temporal comparisons,
raw parsing, authority and byte/HTTP enforcement remain held.

## Complete output-dependency fence

The admitted output decision covers all returned rows, every unreturned
lookahead used for `has_more`, current source objects of incoming ceiling/after
keys, and all source-derived ceiling/after keys in a new cursor. Deduplicate
repeated objects. At output admission immediately before first byte, recheck
current session/action/query authority and every dependency's current
object/purpose/consent/assignment and source-copy expiry fence.

An incoming anchor must still satisfy current minimal-row disclosure, route/filter
membership and copy-purpose/expiry. Historic permission, a valid MAC and a live
navigation window cannot authorize re-emitting a source key. Known source loss,
expiry, revocation, membership loss or a changed participating fence requires
generic `page_changed/restart_view`; current route/session/action denial remains
uniform `request_denied`. Unknown authoritative source/fence state is
`service_unavailable`. Do not silently remove a lookahead, shorten the page,
guess `has_more`, issue a replacement cursor or emit partial success. Previously
transmitted bytes cannot be recalled.

The ordered rows and at most two incoming anchor lookups are distinct bounded
logical observations: at most `limit + 3` unique source dependencies, 28 at limit
25. This is not a database scan-work bound or a selected query/index plan. All
dependencies belong to one coherent admitted page/output decision within the
common deadline. Do not persist metadata solely to keep pagination working.
This fence does not create an immutable multi-page snapshot or require finding
every concurrent insert.

## Cursor candidate and copy lifetime

Propose a bounded stateless, integrity-protected non-bearer bookmark. It avoids
an unbounded server cursor store or transaction across HTTP requests. It is
**not encrypted**. Payload contains only still-permitted source keys, public
filter enums, limit and timing; no principal/session ID, grant, contact/content,
provider payload or secret. It cannot serve as independent historical evidence.

Candidate format is exactly `q1.<payload>.<tag>`. Payload is canonical unpadded
base64url of at most 512 strict UTF-8 bytes. Tag is canonical unpadded base64url
of the full 32-byte HMAC-SHA256, 43 characters. Cursor is at most 768 ASCII
characters; padding, whitespace and noncanonical trailing bits are refused.
Closed logical payload: protocol 1, exact route filter or null, limit 1–25,
ceiling/after pairs `{recorded_at, item_id}`, `issued_at` and `expires_at`.
The directional proposal below refines encoding; decoder/temporal enforcement
and independently reviewed adoption remain held.

Authenticate a length-delimited, domain-separated message containing fixed
purpose `hsd-operator-page-q1`, trusted route ID, actual server staff session ID,
principal ID, current approved action/query-scope policy fence and exact decoded
payload bytes. Trusted bindings are not cursor inputs. Admit current session and
action before cursor interpretation; compare the full MAC in constant time.
Current per-object and output checks remain mandatory. JWT rotation within the
same eligible login session grants no new authority or life.

First-page issuance anchors a maximum 600-second chain window. Descendants
retain original issued/expiry times, ceiling, filter and limit. Trusted current
time must satisfy `issued <= now < expires` and `expires - issued <= 600 seconds`.
Unknown time/key/fence does not extend access. GET, token rotation, retry and
Next do not renew it. Navigation expiry is not a booking/task/retention timeout.

The 600 seconds is a maximum navigation window, **not a copy-retention grant**.
Bookmarks and in-memory pages remain bounded by the earliest applicable source
expiry and current purpose. Recheck incoming/outgoing key sources and lookahead
before minting descendants. No separate historical-key purpose is selected;
such a purpose would need its own reviewed accepted binding. Discard/redact
private copies on current loss and fence late replies. Do not persist bookmarks
to evade deletion or acquire longer audit/navigation retention.

After current route admission, malformed, tampered, expired, wrong-session,
wrong-route and changed-scope bookmarks share safe `page_changed/restart_view`,
without reason/payload echo. Cheap outer target/length/syntax refusals are object
independent. No unsigned fallback or reinterpretation as an ID. Unknown
authoritative source/fence state remains unavailable under the output rule.

Use a purpose-separated high-entropy protected server key; do not reuse
JWT/CSRF/proof keys. No key is generated/configured here. Custody, shared fences
and the actual cryptographic mechanism remain held. Rotation may invalidate
bookmarks instead of retaining an unbounded old-key set. Standard-library HMAC
and constant-time comparison are candidates, not a selected production runtime
or new signing dependency. Bookmarks remain linkable private query metadata:
scrub query values from gateway/access/audit/analytics/referrer diagnostics;
no local/session storage, public links, indexing or saved history state. Minimum
approved audit may record route/class/result, without cursor/item payload.

## Prospective HTTP and finite-resource profile

These are unmeasured initial targets, not an accepted workload, capacity or SLA.

| Boundary | Candidate limit or rule |
|---|---|
| Shared service work | One 32-reader pool across all three routes, receive through auth/query/encoding/output/drain; no hidden queue. One admitted reader per eligible staff session. Only currently authorized sessions allocate keyed limiter state. |
| Shared session starts | At most 60 starts per rolling 60 seconds across routes, tabs, JWT rotations and workers; at most 1024 live authorized limiter keys. No untrusted selector keys or active-state eviction/reset. Retire only after window and known settlement. |
| Manual client | At least one second between starts; after 429, wait 30 seconds before the next deliberate attempt. No automatic retry, crawl or export. |
| Intake | Request target at most 1024 bytes; decoded headers at most 16384 bytes including aggregate Cookie values at most 8192; at most 64 fields; receive/framing at most five seconds. No request body/content type/content encoding/transfer body. Actual ingress framing across HTTP versions remains held. |
| Execution and delivery | Authority/query/serialization at most two seconds after admitted headers; body delivery at most five seconds; client observation at most ten seconds. Abort/deadline does not release reservations until work/drain settlement is known. No second result after uncertain transport. |
| Output | Entire authorized JSON serialized before headers; success at most 32768 emitted UTF-8 bytes, fixed error body at most 1024. Identity/no Content-Encoding. Route-owned results use no-store and nosniff, no ETag/Last-Modified/304/Set-Cookie or CSRF issuance. |

Same-origin HTTPS staff-cookie fetch only. No conditional/range, cross-origin
CORS, JSONP, HTML/login/provider redirect or browser Bearer fallback. Present
Origin must exactly match trusted configuration; null/malformed/foreign denies.
Missing Origin grants no authority. Available Fetch Metadata must indicate
same-origin; absence removes no cookie/action/object checks. GET borrows no
business-mutation CSRF authority. Future separately approved authentication
transport rotation cannot turn list activity into session-clock renewal.

| HTTP outcome | Safe logical result |
|---|---|
| 200 | Authorized complete page, including truthfully empty. No action grant or all-system completeness. |
| 400 | `invalid_request/correct_request`, no query echo. |
| 403 | `request_denied/check_access` for unknown/invalid/expired staff session or missing current route/query/object disclosure authority; no existence or private reason. Auth challenge/reauthentication belongs to the separate staff boundary. |
| 409 | `page_changed/restart_view` for admitted bookmark/fence/page changes; no silent filter widening. |
| 429 | `request_limited/wait`, Retry-After 30; no private owner/existence/quota details. |
| 503 | `service_unavailable/refresh_view` for incomplete/unknown authoritative query, output or resource state; never falsely empty. |
| 500 | Fixed `internal_error/refresh_view`, no diagnostics. |

Object-independent 405 with Allow GET, 501, 406, 414 and 431 are bodyless.
Bodyless HEAD refusal omits hypothetical GET Content-Length. Intermediary
failures are observation failures, not queue or parent-operation outcomes.
The directional proposal below binds error JSON/status/media/raw/header rules;
actual ingress and handler enforcement remain unproved.

## Client behavior, qualification and remaining gates

Offer deliberate Open/Next/Refresh, with no polling. Each page replaces the
visible page. If still-permitted prior pages remain in memory, deduplicate IDs
and current revisions and label them last observed; detail/actions reauthorize.
Selection/filter/navigation/auth epochs reject late replies and errors. Current
authority loss clears private pages. Cursor expiry/change preserves only
still-permitted filters/work and offers a deliberate head refresh; it does not
end tasks, discard admitted operations or reset access/retention clocks.
Complete-process accessibility and timing design remain required.

After implementation, exercise actual protected query/output boundaries for
wrong roles and cross-scope counts/cursors; true empty versus unavailable;
lookahead/anchor-only revocation and expiry races; late commits and live paging;
MAC/encoding/context/expiry refusal; no mutation/renewal; cross-route/tab/rotation
limits and unsettled cancellation; independent detail/action authority; and
actual framing/byte/cache behavior. Schema fixtures will prove shape only.

The closed directional module below is a candidate, not an adopted wire freeze.
The actual cursor parser, source/classification and physical mappings,
queue/grant policy, purpose/copy bindings,
key custody/distributed fences, workload measurements, screen/accessibility
references, required reviews and integrated founder acceptance remain held.
No role, storage/index, retention adoption, provider or stable dependency graph
is selected. Application development and commits/pushes remain separately gated.
The [field dictionary](process-fields.csv) now references this proposal for its
six existing operator-read rows; their TODO status and unresolved source/policy/
physical/adoption obligations remain, rather than claiming working queries.

Primary support checked 2026-10-17: [OWASP authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html#validate-the-permissions-on-every-request),
[PostgreSQL transaction isolation](https://www.postgresql.org/docs/18/transaction-iso.html)
and [LIMIT ordering](https://www.postgresql.org/docs/18/queries-limit.html),
[HMAC](https://www.rfc-editor.org/rfc/rfc2104.html) and
[Python hmac](https://docs.python.org/3/library/hmac.html). Context7 documentation
ID `/websites/postgresql_18` is a research input, not version selection. HMAC is
integrity, not encryption; historical RFC hash examples are not selected. None
of these sources prescribes Hengshi's grants, cursor lifetime or capacities.

## Directional encoding and HTTP binding proposal — 2026-10-17

Status: DOING. [operator-read.schema.json](operator-read.schema.json) proposes
endpoint-specific query maps, response bodies and decoded private cursor shapes.
Its root rejects; explicitly select `handoff_query` / `handoff_response`,
`alert_query` / `alert_response` or `booking_exception_query` /
`booking_exception_response`. Query maps are representation fixtures for an
already-separated raw query, **not JSON request bodies**. No route accepts JSON
input. The three `*_cursor_payload` definitions describe decoded private
bookmark data; they are neither responses nor independently accepted input.

Reuse [common UUID/revision shapes](process-value.schema.json) and the existing
[canonical UTC-millisecond shape](booking-status-response.schema.json#/$defs/utc_instant),
with UUID and real calendar format assertion in addition to lexical validation.
Do not round source instants silently. Require a reviewed source mapping capable
of preserving this order/precision; representation alone supplies no stored field.
Whole page, item, metadata, query, key and payload objects are closed. Item
revision/limit/protocol are canonical unsigned decimal JSON integer tokens,
without exponent/fraction/coercion. JSON Schema integer validation alone also
accepts parsed `1.0`; raw token/serialization checks remain separate.

The module correlates item count with all allowed limits, full-page `has_more`
and cursor/null. It cannot establish unique IDs, tuple order, actual lookahead,
complete membership, authorized anchors or current expiry. Repeated IDs with
different revisions are not permitted merely because a schema accepts them.
All earlier query/output/source-purpose fences still govern.

### Raw query and transport binding

At the exact route, absence of a query starts page one. A present query is a
nonempty ASCII sequence of `name=value` pairs separated by one `&`, with no
leading/trailing separator, fragment, extra `=` or bare `?`. First-page pairs
may appear in either order; `limit` and the route filter may each appear once.
Continuation is only `cursor=<token>`. Refuse percent/plus encoding, duplicate
names, Unicode, aliases and unknown fields before a lossy query parser can join,
decode or choose a last value. Bad outer query grammar is fixed 400. Once this
grammar and current route authority pass, malformed/tampered cursor contents
use generic 409 under the cursor rule; no object-specific diagnostic.

Browser fetch sends `Accept: application/json`, credentials same-origin, cache
no-store and redirect error. Use the existing staff-cookie selection and current
server-session checks in [staff security](SECURITY_PRIVACY_CONTRACT.md#authenticated-staff-cookie-and-csrf-transport-proposal--2026-10-06),
never a visitor proof or browser Bearer fallback. Unknown/duplicate/ambiguous
staff credentials do not grant authority; use uniform 403 without cookie echo.
The staff authentication/challenge contract remains separate.

No body, Content-Type, Content-Encoding, Transfer-Encoding or trailers are
admitted. An optional Content-Length must be an unambiguous zero. Reject body
presence without collecting/decoding it. The trusted ingress rejects or closes
ambiguous/conflicting/incomplete framing before route admission, never hands
different interpretations to multiple parsers. Do not assume every ingress
rejection supplies route JSON. Conditional If-* and Range fields are unsupported
fixed 400 before object lookup; never 304/206 or an identity/existence probe.

Effective Accept follows RFC media-range specificity and quality; if it excludes
application/json, send bodyless 406. Missing Accept permits JSON. Known unsupported
methods, including HEAD/OPTIONS, return bodyless 405 with `Allow: GET`; unknown
unimplemented methods return bodyless 501. Size gates return bodyless 414/431.
These method/media/size gates are object independent and precede costly private
lookups. Earlier transport-close/intermediary outcomes are observation failures.
The shared service-wide 32-reader permit is reserved **before route-owned
receiving and authentication work**, and held through that work, projection,
output and known draining settlement. Safe ingress must enforce this finite
admission without a hidden receive/auth queue; header sizes/deadlines alone do
not replace the concurrency cap. After safe framing and current session/action
admission, attach only the authorized session's one-in-flight reservation and
shared start accounting to that already-held global permit, before cursor
interpretation or source/anchor lookups. Never allocate session-keyed state from
an untrusted selector or grant a second global slot after authentication. Refusal,
abort, auth failure and deadline cannot free the original permit until its work
and drain settle. This is the earlier receive-through-drain pool, not a new pool,
larger capacity or implemented ingress guarantee.

All complete route-owned responses, including bodyless refusals, use
`Cache-Control: no-store` and `X-Content-Type-Options: nosniff`. No validators,
304, redirect, CORS grant, Set-Cookie, CSRF issuance or session renewal. Bodyless
means zero content bytes and no Content-Type; omit Content-Length for HEAD and
otherwise emit zero or omit it. Do not compute a private hypothetical GET length.
Body-bearing responses use `Content-Type: application/json`, strict UTF-8 with
no BOM, identity/no Content-Encoding and complete serialization before headers.
Apply the existing emitted-byte ceilings; oversize/encoding/fence uncertainty
cannot produce partial or shortened success.

Success 200 has only its endpoint's page. Errors are exactly `{code, recovery}`
with the fixed pair in the HTTP outcome table above: 400 invalid_request,
403 request_denied, 409 page_changed, 429 request_limited,
503 service_unavailable and 500 internal_error. Error values are lowercase as
shown, not free text. 429 additionally sends `Retry-After: 30`. No state, request,
item, grant, count, reason or submitted query is appended. Bodyless outcomes
have no JSON-schema instance. Unknown session/action denies uniformly; a known
changed page dependency restarts; unknown authoritative dependency is unavailable.
Never collapse those into a successful empty page.

### Exact cursor candidate bytes

Interpret the q1 format using RFC4648 base64url, deliberately without padding,
line breaks or ignored nonalphabet characters. Require zero unused trailing bits
and a decode/re-encode identity check. Payload is 2–683 encoded characters and
at most 512 decoded bytes; tag is exactly 43 characters decoding to 32 bytes.
The lexical schema covers lengths/alphabet/pad-bit positions only. A public
zero tag or an encoded non-JSON string can pass it without being a valid cursor.

Within the received/query budget, admit current route/session/action, bound the
token, decode bytes and verify its full trusted-binding MAC before using payload
values for a source lookup. Never parse a cursor-supplied principal, route or
grant as a trusted binding. After MAC validation, require strict UTF-8 and the
route's closed payload shape. Reject duplicate names before dictionary loss,
BOM, invalid scalars, extra data and numeric aliases. Schema fixtures cannot
validate those raw-byte properties or the MAC.

Propose one deterministic ASCII JSON payload serialization: member order
`protocol`, `filter`, `limit`, `ceiling`, `after`, `issued_at`, `expires_at`;
each key pair orders `recorded_at` then `item_id`. Use protocol literal `1`,
canonical decimal limit, exact allowed filter string or null, canonical UUIDs
and UTC-millisecond strings. No whitespace, escapes or trailing bytes. All
permitted strings are ASCII; no generic Unicode/JSON canonicalization algorithm
is invented. Compare exact decoded bytes to this canonical serialization; a
different but valid JSON spelling is not this cursor protocol.

For the proposed HMAC message, concatenate six length-prefixed byte strings in
order: fixed purpose `hsd-operator-page-q1`; trusted exact interface ID
`IF-STAFF-10`, `IF-STAFF-16` or `IF-STAFF-18`; canonical trusted server staff
session identity; canonical trusted principal identity; canonical current approved
action/query-scope fence; exact decoded payload bytes. Each length prefix is a
four-byte unsigned big-endian octet count. The purpose/interface and payload have
the bounds above; each of the three trusted identity/fence encodings must be
nonempty and at most 256 UTF-8 bytes, without truncation or hashing away ambiguity.
Exact identity/fence source encodings remain a required security binding;
unknown/oversize/unrepresentable trusted state is unavailable, never an implicit
empty binding. No key ID, principal, route or policy value enters the payload.

Check issued/expiry ordering, the nonrenewing 600-second maximum, current trusted
time, tuple ordering (`after <= ceiling`), current filter/limit/chain bindings,
all anchor/lookahead sources and their output/copy fences. A next cursor uses
the last returned key as after; its ceiling/filter/limit/chain times stay fixed.
First-page ceiling is its highest eligible returned key. No cursor exists for
empty/final pages. This sets no source-copy retention grant and does not relax
OPREAD01. Missing current source bindings fail closed under the existing outcomes.

Key custody, actual HMAC/parser, shared identity/fence encoding, source query,
physical ingress, rate accounting, clock precision and workload enforcement need
their own reviewed implementation after Phase 1 acceptance. No signing key or
credential is generated. The module/fixtures and this prospective HTTP encoding
need independent review and integrated adoption; none establishes a working list.

Additional primary support checked 2026-10-17: [RFC4648](https://www.rfc-editor.org/rfc/rfc4648.html)
for alphabet/pad bits, [RFC8259](https://www.rfc-editor.org/rfc/rfc8259.html) for
JSON interoperability/UTF-8, and [RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html)
for media negotiation, method and bodyless-response semantics. The stricter
canonical payload, fixed responses, query grammar and budgets are Hengshi proposals.
