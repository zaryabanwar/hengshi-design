"""Append a definition proposal, retaining its predecessor; no handler changes."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
PATH = ROOT / 'docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md'
if (OUT / 'PRIVATE_PROCESS_PROOF.md.before').exists():
    raise RuntimeError('Refusing overwrite')
(OUT / 'PRIVATE_PROCESS_PROOF.md.before').write_bytes(PATH.read_bytes())
text = '''
## Booking creation transport and response profile proposal — 2026-10-06

Status: DOING. This is a proposed finite profile at the existing IF-BOOK-01
`POST /api/v1/bookings/lineages`, not a new endpoint or implemented handler.
It refines the earlier directional creation and request-encoding proposals.
The unchanged [client schema](booking-creation-request.schema.json) and new
[closed server response schema](booking-creation-response.schema.json) describe
opposite directions; neither proves authorization or atomic business behavior.
This section supplies candidate transport, lifetime and work values left open
for this boundary above. Values require independent review and integrated/founder
acceptance; they are not standards-mandated defaults, measured capacity or SLAs.
Chat, privacy, qualification, email/slot/provider and staff protocols retain their
separate contracts. No local prototype attribute is relaxed or store selected.

### Same-origin request and bounded decoding

Use a browser-only, same-origin HTTPS JSON POST. Require exactly one syntactically
valid Origin whose canonical scheme/host/effective port exactly equals the trusted
public application origin configured out of band. Do not derive that trusted
origin from Host, Forwarded, X-Forwarded-* or caller input; actual trusted-proxy
binding is still an implementation/deployment input. No wildcard, suffix match,
missing/null Origin, Referer fallback or redirect to another host is admitted.
The proposed deployment keeps API and web under that credential origin; choosing
its provider/host remains D-068-deferred. Fetch uses credentials `same-origin`.

Accept `application/json` with no media parameters or only one `charset=utf-8`
parameter, case-insensitive for media/parameter syntax. Reject forms, alternate
charsets, duplicate/unknown parameters, and any Content-Encoding other than absent
or `identity`. Protocol framing must be resolved unambiguously before ASGI/body
validation; conflicting length/transfer framing cannot become ordinary JSON.
Use the shared strict UTF-8/raw JSON boundary before parsed-schema validation:
no BOM, duplicate members, trailing data, surrogate scalars, nonfinite/coerced
values or unknown properties. These particular requests contain one root object,
no arrays/nested objects and at most three members; references are canonical ASCII.

Proposed per-request maxima: 1,024 received body bytes, 16,384 aggregate decoded
header bytes including Cookie, 8,192 Cookie-value bytes across all Cookie fields,
and a five-second receive deadline. These bound streamed input as well as declared
lengths; do not trust Content-Length or join duplicate credentials away. At most
64 admitted receive/creation jobs and 1,024 allocated pre-consent contexts/operation
records exist across the service, including pending/draining work. Refuse further
admission at capacity; do not create a hidden queue or evict a live/uncertain
process to make room. Exact shared permit/store mechanisms and ingress binding
must enforce these service-wide values across workers, not multiply them per worker.
No client fingerprint, unreviewed IP retention or new per-person identity follows.
Admission/capacity checks precede allocation. Cancelling a connection cannot release
work/state before its known settlement and cleanup. These modest initial limits
must be exercised under the eventual approved graph and sized by later load tests.

Check inexpensive method/media/Origin/size gates before costly allocation; then
raw/closed shape and, for create, selected current cookie plus CSRF authority;
then allocated family/purpose, immutable operation meaning and single-promotion
authority. An already recorded matching operation is reconciled, not executed
again. A ten-second creation observation deadline may return an authorized pending
projection; it is not permission to abandon work or mark no effect. If authority
or outcome cannot be established, use a safe unavailable projection instead.

### Proof, CSRF and cookie transport

Generate bearer proof and synchronizer CSRF independently from 32 CSPRNG bytes
each. Encode each as 43 canonical unpadded base64url characters; the final character
has zero unused pad bits. Schema checks only the CSRF response representation,
not randomness or the HttpOnly cookie. The bearer verifier recommendation is
SHA-256 over the decoded random bytes with constant-time verifier comparison;
256-bit random input prevents treating this as a human-password hashing pattern.
Staff bcrypt/JWT rules are unchanged. Never emit/store/log raw bearer in JSON or
durable rows. The separate CSRF token may remain in the bounded authorized process
state for return to its current caller; exclude it from logs, caches, public HTML,
durable pre-consent storage and script-readable persistent browser storage.

Create submits the CSRF token only in a single `X-Hengshi-CSRF` request header,
with its exact canonical encoding and current process/generation binding. Require
it together with current selected cookie and exact Origin; it cannot authorize
another context, replace bearer proof or extend validity. Bootstrap does not yet
have that synchronizer token and relies on its strict Origin/media/work gates.
Do not silently accept query, body, cookie-as-CSRF or multi-valued header variants.
Keep browser CSRF state in volatile application memory scoped to the selected
process/UI generation. An explicit reload cannot recover authority from a public
page token; approved authorized recovery or Contact is required.

Proposed cookie name: `__Host-hengshi-bk-<selector32>-g<generation>`, where
selector32 is the server-issued provisional UUID rendered as its 32 lowercase
hex digits without hyphens, and generation is canonical decimal 1..9007199254740991
without leading zeros. Selectors remain nonsecret; syntactic UUIDs are not issued
authority. The server issues UUIDv4 selectors/lineages independently and guards
collisions; client UUID text alone cannot establish that generation or allocation.
Each cookie has Secure, HttpOnly, SameSite=Lax, Path=/, no Domain, and finite Max-Age
no larger than remaining server authority. An Expires value, if emitted, agrees
with that deadline; a negative/expired lifetime never authorizes success.

Parse original Cookie fields under the header limits. Reject duplicate recognized
Hengshi booking credential names and malformed booking namespace/name/value forms
before selecting proof; two same-name tokens never become last-value-wins.
An unselected cookie, staff token or another valid booking cannot grant this
provisional context. Admit issuance only while at most eight recognized booking
cookie slots and four current booking contexts would be present in that request's
host credential set. This is an observed-request issuance cap, not proof that an
anonymous browser with omitted cookies owns no other contexts; the service-wide
capacity bound remains necessary. Count stale booking slots until known cleanup;
refuse capacity rather than discard an active credential. Other trusted-host
cookies still count toward aggregate header limits. Exact browser coverage must
verify prefix/attribute/size behavior and graceful eviction; a prefix or nominal
browser quota cannot promise preservation. Credentials are not isolated by tab/port.

Bootstrap starts at generation 1. Atomic successful promotion rotates bearer and
CSRF to generation 2, binds current authority to the selected provisional context
and its single lineage, and invalidates generation 1 before disclosing success.
Issue the new cookie and expire the old exact slot. Late responses cannot replace
a newer generation's name; late generation-1 cookies remain invalid server-side.
Later approved rotation may advance the generation, never decrement/reuse it.
An authorized created-result replay reports the current permitted generation/CSRF,
does not issue a fresh bearer, renew a lifetime or recover a lost cookie from its
stored verifier. This section approves no later rotation or recovery endpoint.

### Server projections, status and uncertainty

| Response | HTTP | Closed projection and meaning |
|---|---:|---|
| Bootstrap ready | 200 | `phase=bootstrap`, `state=provisional`, selected `provisional_id`, `proof_generation=1`, separate `csrf_token`; protected bearer only in Set-Cookie. No lineage or booking success. |
| Created or currently authorized matching replay | 200 | `phase=create`, `state=created`, selected `provisional_id`, same `operation_id`, own `lineage_id`, current `proof_generation` at least 2 and separate current `csrf_token`. One empty BOOKING_STARTED lineage, never qualification/email/slot/provider confirmation. |
| Currently authorized unresolved operation | 202 | `phase=create`, `state=pending`, selected `provisional_id` and scoped `operation_id`; no lineage, generation, token or completed result claim. Reconcile the same intent through this existing boundary under current authority. |
| Invalid closed/raw request | 400 | `state=unavailable`, `code=INVALID_REQUEST`, `recovery=correct_request`. |
| Body/media/header rejection | 413 / 415 / 431 | Same unavailable projection with BODY_TOO_LARGE / UNSUPPORTED_MEDIA / HEADER_TOO_LARGE, each `recovery=correct_request`. Ingress may safely terminate before an application JSON body; absence of a body is no business result. |
| Missing/expired/revoked/unusable authority | 403 | ACCESS_UNAVAILABLE with `recovery=contact`; do not distinguish unknown private object from invalid current proof. |
| Currently authorized action/CSRF denial | 403 | ACTION_DENIED with `recovery=contact`; no raw value or private state echo. Without current object authority use ACCESS_UNAVAILABLE instead. |
| Authorized immutable-meaning conflict | 409 | OPERATION_CONFLICT with `recovery=reconcile`; no replacement intent/lineage or automatic retry. |
| Bounded admission exhausted | 503 | CAPACITY_LIMIT with `recovery=wait`; a previous matching operation may still exist, so this does not establish absence of earlier effects. |
| Store/worker/outcome unavailable | 503 | SERVICE_UNAVAILABLE with `recovery=reconcile`; uncertainty and no currently permitted disclosure remain authoritative. |

All projections use `Content-Type: application/json` and `Cache-Control: no-store`,
with no permissive cross-origin credential access. Produce strict UTF-8 JSON under
the response schema and matching numeric/scalar rules, not arbitrary framework
exception bodies. Error objects have only state/code/recovery: no input echo,
free-form detail, object/operation reference, private existence, staff, cookie or
CSRF. Localized explanation comes from an approved fixed code-to-copy map, not
server exception text. Bound emitted JSON to 1,024 bytes before headers; response
shape alone does not prove header/cookie or raw encoding conformity.

Unavailable describes the current safe projection, not proof that no earlier
promotion occurred. A client timeout, invalid/lost body, failed cookie acceptance
or 202 never means completion or definite noncompletion. Retain the selected intent
and reconcile only under current proof/CSRF. No unauthorized recovery by email,
selector, old generation or operation ID; no replacement that evades uncertainty.
A syntactically valid created body is used only when it matches the initiating
UI generation/context/operation and the currently authorized server result; it
does not prove the browser accepted its protected cookie. A lost rotated cookie
can leave a known created lineage inaccessible; expose truthful Contact recovery,
not a second promotion. No retry, status read or receipt refresh renews authority.

### Initial lifetimes and data-class separation

Propose an empty provisional context with a five-minute absolute server lifetime,
and initial lineage access with 30-minute idle and two-hour absolute lifetimes
measured from successful promotion. Only an explicitly admitted permitted user
business action can reset idle time, within the absolute limit; background polls,
CSRF reads, duplicate create/replay, failures and transport heartbeats cannot.
CSRF is valid only while its bound current proof generation is valid, not under a
longer independent deadline. Cookie Max-Age is a transport hint capped to that
server authority, not the authority itself. Cookie deletion or tab closure is
neither verified record deletion nor a cancellation of a booking/provider action.

Before purpose-specific consent/legal storage permission, provisional references,
empty lineage, proof/CSRF and operation evidence remain in the approved bounded
ephemeral path; no transcript, qualification, email, IP profile or hidden durable
idempotency record is added. A lost ephemeral store cannot reconstruct them from
backups/logs or accept the forgotten selector as fresh. Expiry never reopens a
previously promoted context. Pending/draining authority keeps its reservation and
single-promotion fence until settlement/cleanup is known; capacity pressure or a
five-minute timer does not erase an uncertain effect. Admission fails unavailable
when the necessary evidence is absent. Actual uniqueness/fencing, permitted store
class and restore behavior must enforce this, not rely on schema or cache TTL.

Access lifetime is separate from retention. Existing purpose-specific consent,
90-day chat/brief/lead policy and approved active-client/legal exceptions govern
their classes; this profile creates no new retention basis or deletion deadline.
Later qualification, verified-email recovery, provider retries, reschedule/cancel
and privacy identity remain their own contracts. Public alias ownership stays
undecided; Contact recovery describes a route, not monitored mailbox or response SLA.

### Primary support and acceptance boundary

Checked 2026-10-06: Context7 `/websites/fastapi_tiangolo` and official
[FastAPI cookies](https://fastapi.tiangolo.com/advanced/response-cookies/) explain
cookie/header emission alongside response filtering, and direct responses' filtering
responsibility. They provide primitives, not automatic CSRF, proof/replay or raw
JSON enforcement. Exact installed behavior needs the complete compatible graph.
[MDN Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie)
explains host-prefix/attribute requirements, forbidden script access and cookie
expiry. [RFC 6265 section 6.1](https://www.rfc-editor.org/rfc/rfc6265.html#section-6.1)
describes general user-agent capacity guidance and eviction, not guaranteed slots.
[OWASP CSRF](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
supports a bound synchronizer token, separate transport and trusted origin checks;
[OWASP sessions](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
supports server-side expiry and independent idle/absolute controls.
[RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html#section-15.3.3)
distinguishes accepted from completed work. These sources do not mandate this
proposal's names, exact numeric lifetimes/caps or two-phase promotion protocol.

Independent review and integrated/founder acceptance remain. Actual handler/raw
parser/ingress, cookie/Origin/CSRF, distributed work/fencing/store, lifetime/restore,
privacy-safe errors, same/different-operation races, lost acknowledgements/cookies,
browser and measured load tests must prove their respective obligations after
implementation authorization. Schema fixtures establish representation only.
No new account, grant, persisted data, production UI, cloud/provider choice,
dependency, application code, runtime security or complete Phase 1 approval follows.
'''
with PATH.open('ab') as file:
    file.write(text.replace('\n', '\r\n').encode())
(OUT / 'PRIVATE_PROCESS_PROOF.md.reviewed').write_bytes(PATH.read_bytes())
print(json.dumps({'proof_sha256': hashlib.sha256(PATH.read_bytes()).hexdigest(),
                  'append_bytes': len(text.replace('\n', '\r\n').encode())}))
