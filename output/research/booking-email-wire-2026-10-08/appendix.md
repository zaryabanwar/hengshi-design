
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
Known controls cannot grant a Verify/resend/extension against a newer local server
revision; refresh/reconcile before proposing fresh work. Unavailable controls
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

Recommend using the qualification profile's existing service-wide 48 receive/
fresh-mutation and 16 receive/reconciliation slots as one shared pool across
qualification and these two routes, not multiplying capacity per endpoint.
Count draining/uncertain work until known release. Its five-second receive and
ten-second observation deadlines apply; observation expiry cannot abandon admitted
work or decide its outcome. Delivery workers are separately bounded private jobs,
not uncounted work hidden behind a completed HTTP request. Shared per-lineage 16
and service-wide 4,096 unsettled/replay-protection record ceilings include these
email operations; reserve before effects, refuse fresh work at capacity, preserve
permitted reconciliation. No cleanup can forget uncertain effects or prematurely
retire still-permitted historical outcomes. The reviewed send/guess budgets and
challenge clocks remain additional controls, not replaced by body/work limits.

These bounds are unmeasured recommendations. Closed variants, identifiers and
UTC shapes need focused validator checks; those checks cannot prove authorization,
raw transport, clocks, counters, secret storage, delivery truth or actual current
projection. Later runtime qualification must cover loss/duplicate/stale/out-of-order
responses, old-code guesses after replacement, changed retry intent, wrong process,
withdrawal, cap/timeout/limiter outages and no secret leakage at the real boundaries.
No new dependency is required by this schema. Official JSON Schema 2020-12
validation/format semantics and the existing local modules control tooling shape;
the complete stable graph, exact mechanism implementation and integrated acceptance
remain separate. This append and module do not inherit the earlier control PASS.
