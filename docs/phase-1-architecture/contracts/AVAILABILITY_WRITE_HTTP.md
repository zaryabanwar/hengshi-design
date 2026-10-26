# Staff availability declaration — v1 HTTP proposal

Status: DOING. Proposed 2026-10-05 for existing IF-STAFF-09 and SOF-01A/B.
Definition only: no route, grant, storage, account, migration or application change.
Independent review and integrated founder acceptance remain required.

## Controlling scope and cause

[The field dictionary](process-fields.csv), rows for IF-STAFF-09, leaves the
on/off request, initial revision, safe outcome and uncertain-write reconciliation
undefined. This contract refines those fields under [the accepted staff journeys](../../phase-1-ux-architecture/FLOWS.md#sof-01--staff-operator-information-architecture-and-operations),
[availability consistency](AVAILABILITY_CONSISTENCY.md), [logical records](DATA_CONTRACT.md#proposed-availability-intent-and-expiring-projection)
and [current authorization](SECURITY_PRIVACY_CONTRACT.md#staff-identity-and-authorization).
It complements [the public read](AVAILABILITY_READ_HTTP.md); neither a committed
declaration nor its historical receipt is a current live offer. The catalogue's
route and the PostgreSQL/Redis authority split remain unchanged.

## Request, identity and resource

`PATCH /api/v1/staff/departments/{department_id}/availability` accepts one closed
UTF-8 JSON command, no query parameters and no batch. Reuse the five canonical
department selectors and one-pass decoding rules from the public read. A selector
is not authority. Require the approved staff cookie/session, current explicit
availability action grant, object/purpose scope and applicable Origin/CSRF checks
before admitting work or disclosing a binding/result. Visitor/process proof,
content roles, administrator status and Teams presence cannot substitute.

The server resolves the declaration subject from authenticated identity, the
approved action/scope binding and the department. Exactly one authorized subject
must result. A delegate needs the separately approved target/action scope; no
client principal, owner, role or staff ID is accepted. An absent, unmapped or
ambiguous binding denies admission. This proposal does not invent a department-wide
on/off power or a grant to every department member. A later requirement to select
among several delegate targets needs a separately reviewed private selector;
arbitrary target IDs are not accepted as a shortcut.

The PATCH resource is that subject's durable availability intent. Redis projection,
Teams suppression and public live presentation are derived consequences governed
by the separate consistency/read contracts. Apply the entire durable intent change
and its known operation outcome atomically; never expose a partly changed intent.
No claim of an atomic PostgreSQL/Redis transaction follows.

Require `Content-Type: application/json`; content encodings/media parameters and
finite raw-body, nesting, field, queue and work bounds need the complete transport
profile before implementation. Within those bounds, reject malformed UTF-8/JSON,
duplicate decoded member names at any depth, invalid Unicode scalars, trailing
data, nulls, extra members and coercion. Do not repair invalid data, trim IDs or
merge an arbitrary dictionary into an ORM record. The same strict decoding and
closed-shape rules apply to responses. Framework shape validation after an ordinary
last-value-wins JSON parse is insufficient.

### Closed command shape

All commands contain exactly `operation_id`, `expected` and `declaration`.

| Field / variant | Exact proposed representation | Authority |
|---|---|---|
| `operation_id` | 32 lowercase hexadecimal characters representing 128 random bits; freshly generated for each new user intent | Untrusted deduplication selector, never an access token. Collision/uniqueness is checked under the resolved operation scope. |
| `expected`, no existing binding | Exactly `{ "state": "none" }` | Compare against no current durable binding for the resolved subject/scope. It does not mean expired, hidden, off or missing Redis. |
| `expected`, existing binding | Exactly `{ "state": "current", "setting_id": "…", "revision": "…" }` | `setting_id` uses the same 32-lowercase-hex syntax, server issued. `revision` is a canonical decimal string from 1 through 18446744073709551615, with no sign, leading zero, fraction or exponent. It projects the private positive integer without JavaScript rounding. Both identity and revision must match. |
| `declaration`, on | Exactly `{ "state": "on" }` | Explicit user intent only. Server computes validity from the approved policy and decision time. |
| `declaration`, off | Exactly `{ "state": "off" }` | Withdraw only the authorized subject's current intent; no conversation ending, assignment change or booking cancellation. |

Example command, illustrative random identity only:

```json
{
  "operation_id": "92e50e5ed07a4e3f8181ff975e889be2",
  "expected": { "state": "none" },
  "declaration": { "state": "on" }
}
```

The client supplies no expiry, clock, suppression evidence or renewal flag.
There is no implicit toggle, empty-patch/default-on behavior or automatic renewal.
Changing on/off, expected binding, route or resolved subject is changed intent.
The protocol integer range is not a selected database type; exhaustion fails
without wrapping or reusing the same setting identity/revision pair. Any binding
replacement must preserve the consistency contract's identity guard.

## Mutation and replay boundary

1. Resolve and recheck current authenticated action/object authority at admission
   and the actual durable decision. Authorize any outcome projection separately.
   A revoked principal or wrong object cannot retrieve history by guessing an ID.
2. Bind the operation to authenticated actor, resolved subject/scope, method,
   department and exact validated command meaning. Record enough immutable intent
   to distinguish changed retries, under approved retention. JSON whitespace/key
   order alone does not change intent; discarded extra fields cannot be ignored.
3. For a new operation, atomically compare the expected binding with current
   authoritative state and apply the allowed transition. Unknown authority,
   unresolved competing effects or an unprovable compare prevents completion.
   Do not rely on a Redis value, stale replica, browser state or job preflight.
4. Initial on may create a new server-owned setting identity/revision. Initial
   off with a proven absent binding and no earlier unresolved on that can still
   take effect is a known no-change withdrawal result; it creates no fictitious
   on state or expiry. A pending on must first be terminal or durably ordered and
   fenced before such a no-change off result is complete. Existing on/off changes use the
   guarded binding. A new on intent, even when already on, requires explicit
   current-revision authorization and the separately approved renewal policy.
5. Atomically preserve the actual durable result with the transition, including
   a known no-change result. A later projection failure does not roll that result
   back or justify dispatching the same on intent again.
6. A matching known operation replays its immutable historical result after
   current authorization; it does not rerun the stale expected comparison or
   renew expiry. A changed command using its identity conflicts. Pending/uncertain
   work reconciles the same intent before another dispatch; timeouts, aborts and
   lease expiry never prove rollback or terminal failure.
7. Guards discover relevant admitted/unresolved negative effects durably as
   required by the consistency contract. Unauthorized/stale requests cannot
   create a suppression flag. Prevent unresolved old on work from committing
   after a newer off; HTTP ordering and a client abort are not fencing.

Finite retry, operation retention/deletion and restore suppression are still
required policy/physical inputs. Missing operation history must not silently
become a never-seen identity while the old effect could still complete. Lost or
expired history requires terminal/fenced evidence and the approved reconciliation
policy; otherwise the scope remains unavailable and the response unresolved.

## Closed application responses

Use UTF-8 `application/json` and `Cache-Control: no-store` for every application
outcome, including errors. No response creates authentication or process proof.
No provider diagnostic, Teams state, staff directory/contact, private expiry,
conversation, principal/group, raw input or database exception is returned.
Do not redirect a mutation to a login/provider route. Safe authentication challenge
headers and exact allowed origins remain the separate security/transport contract.

Successful/pending bodies contain exactly `department_id`, `operation_id` and
`result`. Echo only the validated authorized selectors and correlate them before
using the result. A result binding uses the closed `none`/`current` structure
defined above; it identifies the historical durable outcome, not today's state.

| HTTP / `result` | Exact result fields | Meaning and client action |
|---|---|---|
| 200 / declared | `{ "state": "declared", "binding": <current> }` | On intent committed with that binding. Show declaration accepted/checking presence; only a fresh permitted public read can establish live availability. No expiry is projected or renewed. |
| 200 / withdrawn | `{ "state": "withdrawn", "binding": <none-or-current> }` | Off intent or proven already-off/absent result known at its durable decision. Current binding is the resulting off intent; none is permitted only for proven absence. No global/delivery-time forever-off guarantee. |
| 202 / pending | `{ "state": "pending", "recovery": "reconcile_same_operation" }` | Admission for this exact authorized intent is known, but completion is unresolved. Keep unavailable; bounded recovery resends the identical command to this same PATCH boundary, which inspects/reconciles rather than dispatches a duplicate. No new status route is implied. |

202 is not evidence that the intent committed, that it will succeed, or that any
staff is live. Do not manufacture 202 when admission itself is unknown. The same
PATCH serves bounded duplicate reconciliation without changing the original intent.
It may return a known outcome, remain pending or fail safely under current grants;
authorization failure does not erase the operation or authorize a new identity.

Error bodies contain exactly `error`, whose required fields are `code` and
`recovery`. No dynamic explanation/body echo is included. The following closed
application variants refine the catalogue's proposed safe-error responsibilities:

| HTTP / code | Recovery | Effect / disclosure boundary |
|---|---|---|
| 400 / `invalid_request` | `correct_request` | Invalid path/query/raw JSON or closed shape; no admitted change. No submitted values. |
| 401 / `authentication_required` | `authenticate` | Session absent/invalid; no object or operation existence detail. |
| 403 / `request_denied` | `stop` | Origin/CSRF/action denial independent of object existence. No binding, other subject or operation detail. |
| 404 / `scope_unavailable` | `stop` | A well-formed selector/subject outside the permitted scope and a nonexistent/held scope share this projection. No private existence/reason detail. |
| 409 / `stale_binding` | `review_current_binding` | Authorized new operation's optimistic compare failed without applying it. Only this variant adds `current` containing its authorized present none/current binding. If current authority/binding cannot be proved, return unresolved 503 instead. No automatic overwrite/new-operation retry. |
| 409 / `operation_conflict` | `stop` | Known scoped identity has different intent. No cached payload or foreign-operation existence. |
| 413 / `request_too_large` | `correct_request` | Finite approved transport/body limit exceeded; do not admit work. |
| 415 / `unsupported_media` | `correct_request` | Unsupported media/encoding profile; no alternate form or dictionary path. |
| 429 / `request_limited` | `wait_same_operation` | Preserve any existing outcome and exact intent. No assertion that a prior request failed. Any Retry-After value must come from approved bounded policy, not client time. |
| 503 / `outcome_unresolved` | `reconcile_same_operation` | Admission/commit/recovery authority is uncertain. Preserve the same intent and keep unavailable. No rollback/no-effect claim and no new identity to evade uncertainty. |
| 503 / `service_unavailable` | `wait_same_operation` | Required authority/service unavailable. This does not certify a previous attempt's rollback. |
| 500 / `internal_error` | `reconcile_same_operation` | Safe unexpected failure; no exception/stack/body disclosure and no terminal-effect inference. |

Wrong methods receive 405 plus the applicable Allow header; no mutation is admitted.
Edge/transport failures can be generic and need not match the application envelope;
the client treats them as lacking authoritative completion. Conditional headers
cannot replace `expected` or authorize bypass. This proposal does not assign an
ETag/If-Match or Idempotency-Key draft protocol; any conditional-request support
needs its own defined precedence, rather than silently ignoring conflicting guards.

## Console and race behavior

On makes no optimistic live claim. Off immediately removes the initiating console's
live claim while its request is unresolved; a confirmed historical withdrawal still
does not erase an already delivered public response. Recheck the current permitted
read and its expiry/recovery contract before presenting live availability again.

Bind UI responses to the active session, department, resolved scope and operation
generation. A late earlier declared/withdrawn receipt cannot replace a newer pending
off/on intent or fresh current evidence. An old on receipt replayed after off is
history only. Keep one unresolved mutation per console scope; other devices/workers
still require the durable compare/fencing rules. A required later off must use
the reviewed authoritative ordering/suppression mechanism, not assume aborting
the earlier on stopped it. Do not disable the persistent off recovery merely
because a prior on is ambiguous; its exact admission ordering is a physical-plan
prerequisite. No browser-local-only toggle is a completed withdrawal.

Unavailability does not silently end existing governed text, reset consent,
cancel booking or alter notification truth. No stored content or visitor movement
is added to operation/audit evidence. Required actor/scope/actual outcome belongs
only to separately approved minimal private retention, never analytics payloads.

## Implementation evidence and remaining inputs

After Phase 1 and implementation approval, test the actual HTTP/auth/strict decode,
PostgreSQL decision/outcome and Redis/public read boundaries with synthetic data:
wrong role/object/delegate and CSRF; no extra/server-owned input; duplicate JSON
and precision boundaries; initial none versus existing expired/off binding; stale
and changed-identity intent; matching retry after off/expiry without renewal;
concurrent on/off and lost acknowledgements; late commit after abort/lease expiry;
identity revocation before mutation and before replay; lost operation history;
projection outage/rebuild; stale UI responses; restoration predating withdrawal;
and off during a valid conversation/booking. Derive expected results from this
contract and accepted journeys, not copies of handler logic. OpenAPI/examples,
schema fixtures and mocked available responses cannot prove these outcomes.

Before wire freeze: approve exact subject/delegate/group grants and allowed origins,
session/CSRF/challenge mechanism, validity/renewal/time-limit policy, finite
transport/work/rate/retry bounds, operation and staff-data retention/restore policy,
physical compare/admission/fencing constraints, strict parser/typed models,
compatible stable toolchain and actual concurrent/HTTP/browser evidence. No account,
operator, fixed numerical service policy, persistence or new external API is selected.

## Dated primary-source observations

Checked 2026-10-05; protocol choices above are Hengshi proposals constrained by
accepted requirements, not behavior automatically supplied by these sources.

- [RFC 5789](https://www.rfc-editor.org/rfc/rfc5789): PATCH is not inherently
  idempotent; conditional application and atomic patch semantics motivate explicit
  compare and scoped operation handling. The chosen patch changes durable intent;
  it does not atomically commit derived Redis presence.
- [RFC 9110, 202](https://www.rfc-editor.org/rfc/rfc9110.html#section-15.3.3):
  acceptance for processing does not establish completion. This proposal adds
  known admission and same-operation recovery requirements.
- [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259): duplicate member handling
  varies; strict rejection is the project's stronger contract. The revision string
  avoids interoperable binary64 integer precision loss; it is still validated.
- [RFC 9111, no-store](https://www.rfc-editor.org/rfc/rfc9111.html#section-5.2.2.5):
  cache restrictions are not an authorization, privacy or deletion guarantee.
- Context7 resolved `/websites/fastapi_tiangolo` and queried PATCH models,
  extra-field rejection, response filtering and validation-error leakage.
  Official [body updates](https://fastapi.tiangolo.com/tutorial/body-updates/),
  [response models](https://fastapi.tiangolo.com/tutorial/response-model/) and
  [error handling](https://fastapi.tiangolo.com/tutorial/handling-errors/) support
  framework-native typed boundaries and controlled error projection. Tutorial
  dictionary updates and examples returning/logging invalid bodies are not safe
  substitutes for the guarded record and redaction contract. Output filtering
  is not object authorization or raw duplicate-member detection. No exact package
  release, coupled graph or response mechanism is selected by these observations.

## Directional shape encoding proposal

The [v1 schema](availability-write.schema.json), proposed 2026-10-05, encodes the
closed command and application responses above. Its separate
[independent review](reviews/availability-write-shape-v1-2026-10-05.md#correction-1-disposition--superseding-bounded-pass)
records bounded PASS after correction 1 at the
[preserved inspected bytes](../../../output/research/availability-write-shape-2026-10-05/correction-1/02-AVAILABILITY_WRITE_HTTP.md).
This later reference update is outside those exact inputs; neither review freezes
the private wire contract or accepts implementation. The prior body is preserved except for
correcting its illustrative operation ID from 33 to 32 characters to match the
existing rule. The earlier review still identifies the preserved prior bytes.

The schema root accepts **commands only**. Use `#/$defs/response` separately for
responses and `#/$defs/departmentKey` for the once-decoded path selector. Never
validate ingress against a request/response union. The five department keys reuse
the public-read schema; they still grant no private scope. Responses cannot be
accepted as commands, and clients cannot supply server-owned expiry or identity.

Bindings encode none versus current exactly; declared requires current, withdrawn
permits either, and pending carries only same-operation recovery. `stale_binding`
alone discloses an authorized current binding. Other errors correlate the fixed
code/recovery pairs without private diagnostics. The schema does not check HTTP
status, headers, conditional precedence, admission or authorization before error
disclosure; the preceding tables remain controlling for those requirements.

Revisions remain ASCII decimal strings in the existing 1–18446744073709551615
range. Separate lexical alternatives cover one through nineteen digits and the
twenty-digit ceiling without binary64 coercion. This is the reviewed protocol
range, not a new database choice or resource limit. Identity shape checks neither
prove random generation nor establish scoped uniqueness, ownership or issuance.

The [focused validator fixtures](../../../scripts/validation/test_availability_write_schema.py)
exercise these definitions using the existing local JSON Schema tooling. Their
revision oracle uses integer arithmetic independently of the lexical encoding.
Ordinary parsed dictionaries cannot preserve duplicate raw JSON member names;
valid shapes can still carry stale or unauthorized bindings and historical
receipts. Shape validation proves no strict parser, current-grant check, mutation,
expiry, durable ordering, replay, live-presence projection or browser behavior.
Those boundaries retain the implementation evidence and held inputs above.

The encoding uses standard [string/pattern constraints](https://json-schema.org/understanding-json-schema/reference/string)
and [schema combinations](https://json-schema.org/understanding-json-schema/reference/combining).
Context7 `/python-jsonschema/jsonschema` and its official referencing documentation
were consulted on 2026-10-05 for local `Registry`/`Resource` resolution. Fixtures
load the two known schemas in memory without instance-directed or remote schema
retrieval. The shared department-key reference uses the public schema's declared
URN rather than a relative filename under a nonhierarchical URN. Fixtures check
both canonical schema identifiers and local file aliases; a file-only registry
must not mask a broken canonical reference. This selects no new library release,
production graph or parser.
