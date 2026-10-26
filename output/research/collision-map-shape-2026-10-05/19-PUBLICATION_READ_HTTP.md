# Public publication reads — v1 HTTP proposal

Status: DOING. Evidence checked 2026-10-04. Definition only; no handler, database,
dependency, hosting provider or production lock is changed or selected.

This proposed wire contract refines IF-PUB-01/IF-PUB-02 in the
[interface catalogue](interface-catalog.csv) under D-019/D-065, PUB-001–PUB-007
and FCT-08/FCT-13. It reuses the
[immutable envelope schema](publication-manifest.schema.json) and
[publication contract](PUBLICATION_CONTRACT.md). It does not accept the full
Phase 1 package. Detailed transport choices require independent review and
integrated founder acceptance before implementation.

The [independent wire review](reviews/publication-read-http-2026-10-04.md) records
PASS after revision 1. Its exact
[reviewed producer bytes](../../../output/research/contract-review-reference-reconciliation-2026-10-04/PUBLICATION_READ_HTTP.pre-schema-reference.md)
are preserved; subsequent reference additions do not replace that identity. The
[application-error body schema](publication-read-error.schema.json) has a separate
[independent schema/fixture review](reviews/publication-read-error-schema-2026-10-04.md).
Both receipts are definition evidence; HTTP, cache and eligibility enforcement
remain implementation obligations.

## Requests and scope

| Interface | Request | Meaning |
|---|---|---|
| IF-PUB-01 | `GET /api/v1/publication/current` | Resolve one currently routed, eligible public release. A database pointer alone cannot establish routed identity during an unresolved cutover. |
| IF-PUB-02 | `GET /api/v1/publication/releases/{release_id}` | Read exactly the requested eligible public release, including a still-eligible older pin. Never redirect or substitute the current release. |

Requests have no query parameters or body. Unexpected query parameters or a
nonempty body produce 400 before lookup. Clients request JSON and normally send
unconditional GETs; credentials, visitor accounts, consent records and private
process proofs are unnecessary. Neither Cookies nor Authorization may grant a
draft preview, change this public projection or extend release eligibility.
These reads neither create a session nor set an authentication cookie.

`release_id` reuses `$defs.identifier`: 1–96 ASCII characters, first alphanumeric,
remaining alphanumeric/underscore/hyphen, case-sensitive and no final newline.
Validate the route value after one URI-decoding step, without trimming, case
folding or a second decoding pass. A decoded slash, backslash, percent sign, dot
segment or control character cannot become an identifier. Never concatenate it
into an unchecked filesystem path, storage URL or SQL expression. Rejected paths
at the routing/intermediary boundary may return a generic 400/404, but cannot
return an envelope or redirect into a valid/private resource. Handler-level
invalid identifiers use the 400 mapping below.

This profile defines GET representations, not an additional HEAD/OPTIONS API,
cross-origin trust policy, rate budget or artifact download endpoint. Their exact
edge behavior remains part of later transport/security integration. Unsupported
methods cannot invoke a publication transition. No service credential or private
operation reference is part of either URL.

## Successful response and identity

200 uses `Content-Type: application/json` and UTF-8 JSON conforming to the existing
closed envelope schema. Required top-level properties remain `manifest` and
`manifest_sha256`; no new serving status, approval identity, private record or
provider field is added. Validate shape, asserted date-time format, semantic graph
and the RFC 8785 checksum before sending a successful envelope. This proposal
does not change canonicalization or confuse the nested-manifest digest with an
HTTP representation validator.

For IF-PUB-02, `manifest.release_id` must equal the validated requested identifier.
For IF-PUB-01, the selected release and digest must agree with the reconciled
public serving identity. Each response is internally consistent at its guarded
read decision; it cannot promise the pointer or eligibility will never change
afterward. A cutover may leave a prior release in service only while the existing
publication contract establishes that routed identity and eligibility. Unknown
routing effects cannot be guessed from a newer database pointer.

The public projection contains only previously approved publishable material.
Schema validity, an immutable object-store key, a known identifier or a matching
digest cannot establish continued serving eligibility. A read cannot approve,
activate, repair, roll back or re-publish a release.

## Eligibility, caching and conditional requests

Proposed conservative read profile: every success and application error carries
`Cache-Control: no-store`. No positive TTL, stale-if-error behavior, immutable
cache directive, ETag or Last-Modified is selected for these two responses.
This constrains envelope/eligibility reads only; it does not prohibit a separately
reviewed cache design for immutable asset bytes behind enforced eligibility.
Request frequency, withdrawal detection bounds, drain limits and delivery costs
remain held inputs, not values inferred from this header.

Controlled serving layers and service workers must not use a stored envelope or
error to satisfy a new read. A browser may retain its currently verified content
context for the approved interaction, but that is not permission to continue
through expiry, unknown eligibility or detected withdrawal. `no-store` does not
erase already received bytes, offline copies or screenshots and cannot prove
compliance by an intermediary. Warm-cache, history and service-worker behavior
need runtime evidence before deployment acceptance.

Perform normal request checks, authoritative eligibility and integrity checks
before evaluating HTTP preconditions. An ineligible release returns the mapped
404 even if a client presents a formerly valid digest; an unavailable authority
returns 503. Neither can become a successful cached response or 304.

For an otherwise successful read, follow RFC 9110 sections 13.1/13.2 with this
validator-free profile: `If-Match: *` succeeds; a non-wildcard If-Match fails with
412 because no entity tag is advertised. `If-None-Match: *` yields bodyless 304
only after the successful eligibility/integrity decision. Non-wildcard
If-None-Match does not match an unadvertised tag. Ignore date preconditions when
there is no Last-Modified, and ignore Range/If-Range because this profile serves
only whole envelopes. Combined preconditions follow the RFC precedence, not
header arrival order. 304 also carries `Cache-Control: no-store` and never grants
an eligibility lease. A wildcard proves representation existence, not which release
the current route selects. After any 304 in this validator-free profile, an
application consumer must obtain and verify an unconditional 200 before accepting
or refreshing its release context. Previously verifying an envelope is insufficient
to establish that it matches this read, including after an A-to-B current cutover.
304 is not the normal application read path and cannot extend an older pin.

The eligibility check must be coordinated with withdrawal at the read boundary;
do not check once and later send bytes from an unchecked cached lookup. Reads
decided after a committed withdrawal cannot return that envelope. Exact fencing,
in-flight delivery limits and propagation/detection bounds remain required design
and measured evidence; this proposal cannot guarantee revocation of a response
already authorized or delivered before withdrawal.

## Application errors

Errors use `Content-Type: application/json`, `Cache-Control: no-store` and a closed
object containing only `error`. That object contains exactly `code`,
`explanation` and `retryability`, all strings from the table below. No nulls,
submitted values, internal exception text, alternate release identity, staff or
provider details appear. `operation_ref` is omitted: these public reads neither
create nor disclose a private operation. This is a scoped refinement of the
[logical field dictionary](process-fields.csv), not the error format for staff,
booking, handoff, AI or privacy operations.

The linked schema constrains each complete error object to one of the five
correlated variants below. It validates the JSON body only: status selection,
headers, request rejection, parsing and recovery behavior require real boundary
tests after authorized implementation. JSON Schema does not detect duplicate
wire keys after a permissive parser has discarded them.

| HTTP | code | Fixed English explanation | retryability | Trigger |
|---|---|---|---|---|
| 400 | PUBLICATION_REQUEST_INVALID | The publication request is invalid. | correct_request | Invalid handler-level identifier, unexpected query or nonempty body. |
| 404 | PUBLICATION_RELEASE_UNAVAILABLE | This public release is unavailable. | refresh_release | Requested release is absent or known not publicly eligible, including draft, rejected, withdrawn or expired eligibility. These states have the same public response. |
| 412 | PUBLICATION_PRECONDITION_FAILED | The publication request precondition failed. | correct_request | Otherwise eligible read fails an HTTP precondition. |
| 503 | PUBLICATION_READ_UNAVAILABLE | Public publication information is temporarily unavailable. | retry_read | No eligible current release, unresolved serving identity, eligibility authority unavailable or transient read dependency failure. |
| 500 | PUBLICATION_READ_FAILED | Public publication information could not be verified. | stop | Stored envelope fails schema, identity, graph or checksum verification, or an unexpected internal failure prevents a verified response. |

Example, with no registration, contact or process information:

```json
{"error":{"code":"PUBLICATION_RELEASE_UNAVAILABLE","explanation":"This public release is unavailable.","retryability":"refresh_release"}}
```

Known ineligibility uses 404; inability to establish eligibility uses 503, never
a fabricated “not found” conclusion or stale success. The same release-specific
404 body conceals editorial state but does not claim constant-time resistance to
enumeration. IF-PUB-01 uses 503 when no eligible current release exists; it cannot
choose an arbitrary retained release. No automatic redirect or fallback body is
returned by either interface.

`correct_request` means change to a conforming request before repeating it.
`refresh_release` means resolve current through IF-PUB-01, then perform the
existing safe content-context refresh; it cannot silently replace a pin or restart
a booking/handoff. `retry_read` permits a bounded later read attempt, not continued
presentation on an unknown eligibility state, an unlimited loop or any write.
`stop` halts use of the unverifiable result and offers truthful recovery.
No numerical retry timing or recovery SLA is invented. Omit Retry-After unless
the server has a verified temporary recovery estimate in its later approved
operating policy. Transport failures, gateway HTML and malformed JSON are not
application errors; the client treats them as an unavailable/unverified read.

## Consumer and implementation acceptance cases

These are future tests at the actual HTTP/persistence/serving boundary, not new
tests asserting documentation wording or mock success. Existing schema fixtures
remain schema-tooling evidence only. Consumer parsing must reject duplicate JSON
keys, unsupported schema, invalid Unicode/format/graph or digest before accepting
the envelope, and bind asynchronous results to their original request/context.

| Case | Required observable outcome |
|---|---|
| Eligible current and eligible older pin | 200 exact verified envelope; requested pin never changes to the current release. |
| Draft/rejected/withdrawn/expired and nonexistent selectors | Same mapped 404 and no private fields or preview through staff credentials. |
| Authority outage or unresolved cutover | 503; no guessed pointer, cached eligibility, 304 or new automatic activation. |
| Checksum/graph/schema corruption | 500 without partial envelope or diagnostic disclosure; consumer rejects tampered 200 independently. |
| Invalid final newline, 97-character ID, encoded traversal/separator, double encoding, extra query/body | Handler or earlier routing rejection, no envelope, lookup escape or redirect into private content. |
| Withdrawal races a normal or conditional read | Guarded decision prevents a post-withdrawal successful read; prove the eventual implementation's allowed in-flight boundary. |
| Old digest/wildcard condition after withdrawal | 404, never 304/200. Eligible wildcard and combined-precondition cases follow RFC precedence. |
| Current changes A to B while a consumer holds A and sends If-None-Match:* | A bodyless 304 proves neither A nor B identity. Consumer obtains and verifies an unconditional 200 before accepting/refreshing context; it cannot reuse A as the current result. |
| Warm intermediary/service-worker cache; network failure | New eligibility read cannot be fulfilled by stored success/error; unavailable authority stops affected use. |
| Delayed prior response after a safe release refresh | Old result cannot populate the new scene, panel, collision, audio or AI context. |
| Content refresh during pending/confirmed booking or handoff | Preserve private operation identity and truth; public read/refresh creates no duplicate or invented confirmation. |

Exact resource limits, monitoring/redaction, CORS/method handling, rate control,
eligibility/drain implementation and provider propagation remain integration
inputs. This GET proposal does not close those gates or assert feature readiness.

## Primary evidence and framework mapping

Checked 2026-10-04: [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html)
sections 9.3.1, 13.1–13.2, 14 and 15 ground GET, conditional ordering, whole-response
and status semantics; [RFC 9111 section 5.2.2.5](https://www.rfc-editor.org/rfc/rfc9111.html#section-5.2.2.5)
grounds no-store and its limits. The fixed code/recovery mappings and conservative
cache profile are Hengshi proposals, not requirements imposed by those standards.

Context7 `/websites/fastapi_tiangolo` was queried for response headers/status and
request-validation overrides. Official [error handling](https://fastapi.tiangolo.com/tutorial/handling-errors/)
and [additional responses](https://fastapi.tiangolo.com/advanced/additional-responses/)
show the framework mechanisms available to implement this profile. Declaring an
OpenAPI response does not enforce it; direct responses and exception handlers must
be tested, including accidental default 422/error leakage. No exact FastAPI,
Pydantic or other package version is selected by this documentation lookup.
