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
This canonical translation needs its own bounded comparison review. Prior PASS
does not certify changed bytes, exact wire mechanisms or integrated acceptance.

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
denied, scope inventory or hidden-row references are returned. Exact JSON
modules, temporal comparisons, raw parsing and byte/HTTP bindings remain held.

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
Exact encoding/decoder and temporal module still require wire review.

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
Exact error JSON/status/media/raw/header precedence remains wire work.

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

The exact closed directional modules and cursor parser, source/classification/
dictionary and physical mappings, queue/grant policy, purpose/copy bindings,
key custody/distributed fences, workload measurements, screen/accessibility
references, required reviews and integrated founder acceptance remain held.
No role, storage/index, retention adoption, provider or stable dependency graph
is selected. Application development and commits/pushes remain separately gated.

Primary support checked 2026-10-17: [OWASP authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html#validate-the-permissions-on-every-request),
[PostgreSQL transaction isolation](https://www.postgresql.org/docs/18/transaction-iso.html)
and [LIMIT ordering](https://www.postgresql.org/docs/18/queries-limit.html),
[HMAC](https://www.rfc-editor.org/rfc/rfc2104.html) and
[Python hmac](https://docs.python.org/3/library/hmac.html). Context7 documentation
ID `/websites/postgresql_18` is a research input, not version selection. HMAC is
integrity, not encryption; historical RFC hash examples are not selected. None
of these sources prescribes Hengshi's grants, cursor lifetime or capacities.
