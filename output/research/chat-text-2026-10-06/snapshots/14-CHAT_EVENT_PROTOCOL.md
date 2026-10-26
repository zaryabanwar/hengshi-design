# Chat event connection and resume contract — v1

Status: DOING. Proposed 2026-10-06; bounded independent review PASS, acceptance pending.
This defines the control layer of existing IF-CHAT-03, not an implemented chat
service or permission to persist conversation data. No application code changes.

[Independent review](reviews/chat-event-control-v1-2026-10-06.md) covers the exact
frozen proposal/schema/test inputs, not this later reference/status update.
Creation HTTP and consent refinements remain outside that bounded verdict.

## Authority and scope

[Interface catalog](INTERFACE_CATALOG.md#chat-consent-and-resumable-events),
[private process proof](PRIVATE_PROCESS_PROOF.md),
[handoff lifecycle](HANDOFF_LIFECYCLE.md#text-reconnect-and-separate-media-consent)
and the security/privacy contract remain controlling. The existing route is
WebSocket `/api/v1/chat/sessions/{session_id}/events`; no new route or account.
IF-STAFF-15 remains separate and requires staff identity/current assignment.

The [directional control schema](chat-event-control.schema.json) distinguishes
visitor initialization/receipt from server readiness/unavailability. Explicitly
reference `#/$defs/client` or `#/$defs/server`; the module root rejects instances.
Conversation command/result, approved-source answer, handoff event and media
variants still need their own closed directional definitions before wire freeze.
They cannot use arbitrary payload objects or a generic sender field to bypass this
control layer. No text, provider operation or business mutation is admitted by
the control variants defined here.

## Upgrade and initialization

1. Production transport is WSS at the same reviewed application origin. Apply
   the existing strict route, allowed Origin and bounded header/Cookie profile.
   Reject duplicate/ambiguous selected cookies, query credentials, guessed process
   selectors, missing/null/hostile Origin, and unauthorized session/context before
   accepting the upgrade. Generic rejection must not reveal process existence.
2. Atomically reserve bounded connection capacity. Verify the currently valid
   promoted chat proof, selected session, generation, process state and source
   eligibility. An accepted transport is quarantined, with no private response,
   subscription, history replay, provider work or business command yet permitted.
3. Within the proposed five-second monotonic initialization deadline, receive
   exactly one UTF-8 JSON text message with `protocol_version: 1`,
   `kind: initialize`, current `proof_generation`, separate process-bound
   `csrf_token`, and explicit `resume: null` or the closed cursor. No cookie/bearer
   secret is in the frame. The CSRF field follows the existing 43-character
   representation; representation alone cannot prove randomness or binding.
4. Strict raw decoding rejects duplicate keys, invalid UTF-8, nonfinite numbers,
   binary messages, unknown fields and coercion before admission. Bound WebSocket
   fragmentation/reassembly and decoded allocation before parsing; checking only
   the final Python string does not constrain the transport buffer. Validate
   CSRF and current authority again before initialization succeeds. Failed or
   timed-out initialization closes generically without echoing credentials.
5. Repeated initialize, commands before ready, or unexpected message kinds close
   the channel without effects. Protocol version 1 is an actual wire identifier,
   not an invented product release. There is no downgrade or query-token fallback.

## Readiness, current authority and client fences

An authorized `ready` response contains a server-issued random UUIDv4
`channel_id`, current `proof_generation`, current `consent_revision` or explicit
null when no map exists, a session-bound UUIDv4 `stream_id`, `head_sequence`,
`next_sequence`, and `resume_outcome: fresh | resumed`. Sequence values are exact
binary64-safe integers; head may be zero, next is positive. The cookie generation
is at least two. These identifiers are linkable private metadata, not access
secrets or authority grants. No token, transcript, staff identity or public claim
is included. A consent revision is not permission; purpose-specific decisions are
resolved from authoritative state under IF-CHAT-02, not inferred from its presence.

The client accepts readiness only for its currently selected session and active
socket attempt. Each attempt has its own local identity; late callbacks from an
older socket cannot update another attempt. Subsequent controls require its exact
channel and stream. End, proof rotation, consent changes, reassignment and source
withdrawal fence dependent queued/in-flight deliveries under their controlling
contracts. Current disclosure authority is checked at actual outbound delivery,
not merely at subscription time. A timer cannot establish immediate revocation.

Consent changes invalidate the old channel's admission snapshot: stop dependent
output and close it before any applied acknowledgement is treated as usable.
Reconnection validates the current map; it does not renew the proof or reapply a
historical grant. Already delivered bytes cannot be recalled. Lost state denies
dependent output, not an assumed harmless reset. A source withdrawal need not end
unrelated valid private process truth, but prevents replay of withdrawn sources.

## Stream order, receipt and reconnect

One authoritative coordinator orders delivery events per session/stream with
strictly increasing positive `sequence` and server-assigned event identity. Never
derive sender, publication authority, staff assignment or operation success from
a client sequence. The logical plan must prevent independent workers issuing
conflicting sequences; a per-worker list is insufficient. No numeric wrap/reset
within the stream. If exhaustion occurs, stop safely; a new stream cannot erase
an unresolved outcome or reconstruct lost content.

`head_sequence` is a coordinated initialization watermark. Subscription admission
and the replay/live boundary must be fenced together, so an event cannot fall
between the snapshot and the live subscription. For a fresh initialization,
`next_sequence = head_sequence + 1`: no historical transcript is replayed. Fresh
means a new transport subscription, not a new session or completed business action.
For resumed initialization, `next_sequence = after_sequence + 1`, with
`after_sequence <= head_sequence`. Bind the requested stream to this exact session;
a cursor for another session, unknown stream, future sequence or unprovable gap
is unavailable, without returning the other stream's existence or contents.

A client `receipt` contains only protocol/kind, current channel/stream and
`through_sequence`. It acknowledges contiguous events accepted into the currently
eligible client projection, not human reading, durable persistence, staff
acceptance, AI correctness or booking confirmation. The server verifies the
receipt does not exceed what this channel actually delivered. Monotonic duplicate
receipts are harmless; older receipts do not move the watermark backward. The
client cannot acknowledge over a gap to make an unseen message count as received.

Resume is a request to replay authorized delivery, never to execute commands
again. Verify current proof, consent, source, assignment and per-event projection
before each replay delivery. A sequence/event identity remains the same on replay;
the UI deduplicates matching identities. Identity with changed bytes is a conflict,
not a replacement message. Exact business operation identity and outcomes belong
to the later command/result variants; transport replay offers no exactly-once
business execution or provider confirmation guarantee.

Only replay the complete currently permissible suffix after the cursor. If a
required event is lost, withdrawn, expired, beyond bounds or has unknown authority,
do not silently skip it and claim continuity. Send a minimal authorized unavailable
control, close, and preserve uncertain business truth. The client can reconcile
through already-authorized process controls where defined, or offer public
Contact/Book. It must not automatically resend a message, create a new handoff or
booking, or recover another session. Proof loss cannot reveal replay status.

## Proposed finite operating profile

The following are **unmeasured engineering ceilings**, not legal retention
permission, verified capacity, service promises or deployment selections:

| Resource | Proposed bound and enforcement |
|---|---|
| Connections | 128 service-wide including quarantine, initialized and draining; at most 32 quarantined and two per selected session. Reserve atomically across workers, before upgrade. |
| Initialization | Five monotonic seconds; one 8,192-byte reassembled message. Deadline does not reset after fragments or invalid input. |
| Control input | 8,192 encoded UTF-8 bytes per complete message; one admitted control operation per connection and 64 across the service. No hidden waiting queue. |
| Connection output | 64 complete events and 262,144 encoded bytes, including admitted pending deliveries. Per-event encoded ceiling 16,384 bytes. Stop before either queue ceiling. |
| Replay | At most 64 events and 262,144 bytes per session/stream, at most 60 monotonic seconds from original admission; earlier proof, consent, source, process or legal expiry wins. Reading/reconnecting cannot extend it. |
| Aggregate buffers | 33,554,432 encoded payload bytes service-wide across socket output/reassembly and replay buffers, with shared buffers counted once and physical copies separately. Transport/decoded-object overhead also needs measured ceilings before implementation. |

Private creation and consent pools remain separate; socket admission cannot enlarge
their ceilings. Provider/text work is not admitted by these control operations.
Idle sockets do not renew the separate chat proof's idle/absolute clocks. Reservation
release follows verified cleanup/drain, never only disconnect, timer or observer
timeout. Uncertain coordinator/capacity state denies new work. No visitor
fingerprinting or unbounded retry list is introduced.

No replay retention is permitted merely by this numerical ceiling. The exact data
class, purpose, ephemeral/durable mapping and deletion/backup/provider obligations
must be approved. Refused retention cannot lead to durable replay, traces or
fallback queues. Where approved transient state is lost, return unavailable;
do not rebuild it from logs or a database. A grant does not automatically authorize
all classes or providers. Revocation invalidates pending buffers and prevents
future dependent delivery; eviction is not proof of deletion from every store.

When a slow client hits a bound, stop business delivery and close safely. Reserve
the ability to emit one minimal control within those same ceilings; if impossible,
close without it. Do not discard older events and claim a continuous or read
conversation. Client `bufferedAmount` is a send-buffer observation, not end-to-end
delivery acknowledgement. No WebSocketStream or new wrapper is selected here.

## Minimal errors and required evidence

Before initialization authority succeeds, return only generic handshake denial
or a close, with no private JSON body. After initialization, a closed `unavailable`
control can name a fixed safe category and recovery (`reconcile` or
`contact_or_book`), never arbitrary exception text, credentials, transcript,
operation/provider result, hidden source or staff details. Close codes/reasons
must likewise contain no private values; the exact transport close profile is
still held. Transport loss itself supplies no cancellation, delivery or deletion
result. Accessibility/UI copy and no-WebGL equivalents need approved references.

Required actual-boundary evidence after applicable approval: disallowed Origin
before upgrade; wrong/fixed/duplicate cookie; fragmented/oversized/binary/invalid
JSON; no private output before CSRF; old generation and cross-session cursor;
slow initialization; late old-socket readiness; consent withdrawal/source removal
versus queued and replayed delivery; concurrent worker ordering/watermark gap;
future/forged/duplicate receipt; lost ephemeral replay; finite backpressure and
draining cleanup; reconnect without renewed expiry or repeated business effects.
Schema fixtures establish directional representations only. They cannot verify
those security, lifecycle, transport or concurrency outcomes. Independent review,
exact close/text/event schemas, physical enforcement, legal mappings, measured
budgets, the stable compatibility graph and integrated/founder acceptance remain.

## Dated primary/framework evidence

Checked 2026-10-06, with Context7 `/websites/fastapi_tiangolo` and primary sources:

- [FastAPI WebSockets](https://fastapi.tiangolo.com/advanced/websockets/) supports
  cookie/dependency checks, receiving after acceptance and disconnect handling.
  Its tutorial manager is process-local; query-token and credential-echo examples
  are not adopted. A dependency check and a socket do not implement this contract.
- [OWASP WebSocket security](https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html)
  supports Origin validation, message authorization, input limits and privacy-safe
  handling. The numerical profile above is a project proposal, not an OWASP mandate.
- [MDN WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
  identifies the standard API's lack of backpressure. Project queue/reassembly and
  slow-client rules are engineering inferences; no library capability is assumed.

## Text admission and delivery proposal — 2026-10-06

Status: DOING, unreviewed. The earlier control review does not cover this addition.
This refines the existing text fields in IF-CHAT-03 and the visitor projection of
IF-STAFF-15; it creates no endpoint, provider entitlement, consent or implementation.
The [text directions](chat-text.schema.json) are additional explicitly registered
variants alongside the control schema. Neither module root accepts instances.
An unknown kind or wrong direction denies; a generic payload/sender fallback is
not permitted. Staff-origin requests still require their separate directional
schema and current identity/assignment before these visitor projections can exist.

### One current server-issued text ticket

After initialized current authority succeeds, the server can send a closed,
unsequenced `text_admission` control bound to the current channel/stream and proof
generation. It contains the current purpose-map revision or null, eligible
release identity, positive `command_revision` and server-issued random UUIDv4
`operation_id`. This ticket is not a bearer, grant or staff/readiness claim.
The same session has one current ticket across its allowed connections, not a
new ticket per tab/reconnect. The client treats it as transport-bound admission
metadata; it must not display these implementation fields in the visitor flow.

`submit_text` includes current channel/stream, this exact ticket pair,
`expected_consent_revision` and a closed payload containing only `text`. There
is no caller role, provider, staff target, publication override, secret, upload,
HTML, tool command or client-issued server event sequence. A natural-language
string is untrusted data, never executable workflow authority. Reject invalid
UTF-8/unpaired surrogates, oversized input, extra fields and whitespace-only text;
do not trim/normalize/truncate the immutable accepted intent into another message.

For a new intent, atomically verify current proof/process/source, ticket pair,
current consent revision and allowed purpose/classification, reserve bounded work,
and consume the ticket exactly once. Null matches an actually absent purpose map,
not revoked permission or lost state. Client observations cannot grant storage or
provider transfer. Match a known admitted pair to its original exact text/context
and intent; changed text conflicts. The same intent reconciles current permissible
status, never redispatches or reapplies a grant. Current transport fields are not
part of historical intent and cannot recover an expired process.

The session keeps a monotonic command revision and bounded current/pending plus
latest terminal operation state. Issue the next revision/ticket only after the
previous work's guarded terminal settlement; never after an observer timeout,
disconnect or unproven provider cancellation. An older unknown pair denies safely
without claiming it never ran. A higher/forged pair is not a new intent. This
provides a bounded admission mechanism without an unbounded UUID history. The
operation identity is scoped to session, command revision and UUID together;
representation reuse does not change creation/booking identities. Never wrap or
reset revision, recreate the counter from the browser, or restore a lost ticket
store from logs. At the exact-integer ceiling or unknown store authority, deny.

`reconcile_text` carries only the channel/stream and original ticket pair. It
queries a current permissible outcome, creates no work and cannot widen access.
For missing older evidence, return minimal unavailable, not a no-effect finding.
The browser must not automatically obtain a new ticket and resubmit old text.
Sending another message is a new deliberate visitor action, not recovery.

### Server-owned routing and truthful outcomes

Current authoritative conversation state determines the destination. Eligible AI
guidance uses approved published knowledge only. An accepted human conversation
routes new text to its currently permitted Hengshi console assignment; it does
not silently send private human conversation to AI or Teams. Staff presence off
alone does not end an already accepted conversation. Unknown assignment/purpose
denies the affected delivery. Reassignment and ending follow the handoff contract;
no client field, event kind or administrator role supplies missing authority.
An automatic switch back to AI after human-path failure is not selected here.

Before AI dispatch, enforce the approved input/sensitive-data/injection and policy
router boundaries: permitted purpose, classification, data handling, residency,
provider entitlement and availability. Personal/confidential data retains the
approved Azure Europe restriction; NVIDIA remains gated for public or demonstrably
de-identified data. D-068 hosting deferral changes neither restriction. Unknown
classification or unavailable permitted routing denies transfer and offers the
allowed Human/Book/Contact path. Retention refusal still permits eligible ephemeral
guidance; it grants no durable transcript, broad provider consent or legal basis.
No secrets, controlled defense data or hidden knowledge are admitted to guidance.

Sequenced delivery events use server-issued UUIDv4 `event_id`, the existing
session/stream order, current channel/proof/consent projection and eligible
`release_identity`. These values cannot grant authority; the server checks actual
current admission and outbound disclosure. A `command_result` identifies the
ticket pair and exactly one of these closed outcomes:

| State | Meaning, never a stronger outcome |
|---|---|
| admitted | Bounded work was admitted; no provider/console delivery or human read promise. |
| pending | An admitted outcome is unsettled; reconcile this pair rather than reissue it. |
| forwarded | The current governed Hengshi console accepted the authorized projection; not a human-read or staff-presence guarantee. |
| refused | Guidance/delivery is refused under a fixed safe category; no raw input/exception echo or promise of deletion everywhere. |
| unavailable | Current permissible outcome cannot be established; not evidence that no effect occurred. |

An `ai_answer` is a terminal complete, safe, nonbinding answer to that ticket pair,
with one to eight eligible source references. Each reference contains only a
published document identifier, canonical semantic route key and document SHA-256.
Resolve and verify all references against the answer's exact currently eligible
release, not arbitrary model URLs or a claimed digest. No sources means a fixed
refusal/recovery outcome, not plausible filler. AI is visibly identified as AI
using approved references/copy; generated text never binds price, scope, time,
legal advice or delivery and cannot operate staff/publication/calendar tools.

Do not stream unvalidated token fragments to visitors. Validate the complete
answer and source set before one bounded delivery; oversized/unsafe results fail
to a safe outcome, not silent truncation or unsourced fragments. Token/chunk
streaming would need its own validated protocol and is not selected here.

`staff_text` is a permitted server projection, with handoff identifier, current
ownership generation and bounded plain text. The server derives its sender from
current staff identity, grant and assignment under IF-STAFF-15. Visitors cannot
produce it; no raw staff identity/directory or arbitrary avatar/display name is
included. Exact approved presentation and staff-input protocol remain held.
Already disclosed text cannot be recalled by closing a socket; later collection,
transfer and replay still require current authority and mapped retention.

Business state cannot regress after terminal settlement. Old pending/forwarding
work cannot publish a newer pending event after a final answer/refusal. Replaying
an immutable event is historical delivery, not renewed current authority or new
work; apply sequence/dedup and current source/consent/assignment fences. Historical
ticket controls do not enter transcript replay. A current admission control alone
can enable a new message, and the server still independently consumes its ticket.
Reconcile responses use current permissible state without mutating old event bytes.

### Finite text profile and remaining proof

Proposed, unmeasured ceilings, subordinate to the existing connection/aggregate
buffer limits and all earlier expiry/deletion/withdrawal rules:

- Visitor text: 1–2,000 Unicode scalar values; whole request at most 8,192 UTF-8
  encoded bytes including its envelope. Both limits apply independently.
- AI/staff text: 1–4,000 scalar values, one whole event at most 16,384 encoded
  bytes including sources/envelope. No raw provider/exception data in errors.
- One unsettled text operation per session; eight service-wide including pending
  and draining work, across workers. No hidden queue or speculative dispatch.
- Ten new text admissions per rolling 60 seconds per session and 64 service-wide;
  reconciliation has separate ceilings of 20 per session/128 service-wide per
  rolling 60 seconds, in addition to the control-work pool. Counters/clock unknown
  denies new admission. Do not infer another person/session from a rate response.
- Ten-second observation may report pending, not cancellation. Provider work has
  a proposed 60-second scheduling deadline; stop new dispatch after it and fence
  late output. Unknown external settlement keeps its reservation and cannot issue
  another ticket. Exact adapter cancellation/reconciliation remains held.

Keep only the bounded current ticket/pending and latest terminal projection. Their
private metadata/plaintext require their own approved ephemeral/durable class,
purpose, duration and deletion/restore map. Replay's 60-second ceiling is no legal
permission or automatic duration for these records. Lost store authority denies
dependent work; no reconstruction from private logs or an unconsented database.
Plain text is rendered as text with approved semantic links, not innerHTML/model
Markdown that can introduce executable markup, hidden tracking or arbitrary URLs.

Required actual-boundary cases after approval: two tabs consume one ticket;
changed-text retry; unknown older/future pair; consent changes between ready and
admission; raw byte/scalar boundaries; injection/sensitive input/provider-routing
denials; missing/withdrawn source before final output; reassignment/end versus
staff delivery; timeout versus terminal settlement; late pending after completion;
lost ephemeral state; bounded queues/rates; replay without redispatch. Schema
fixtures test direction/shape only. Legal mappings, staff-input/handoff/end/close
variants, physical atomic/routing/safety/retention enforcement, measured budgets,
compatible stable adapters, approved UI and independent/integrated/founder
acceptance remain required. No provider call, storage write or application exists
because this definition or a JSON fixture passes.

### Dated representation evidence — 2026-10-06

- Context7 `/python-jsonschema/jsonschema` documents the Draft 2020-12 validator
  and explicit format checking. Its main-source examples are guidance, not proof
  of the installed version or a selected production dependency.
- The [official JSON Schema object guide](https://json-schema.org/understanding-json-schema/reference/object#unevaluated-properties)
  explains closure across composed schemas. The text event branches use `allOf`
  with `unevaluatedProperties: false`; the header remains an incomplete helper.
  Installed diagnostic jsonschema 4.23.0 registers this keyword in
  `Draft202012Validator`; its inspected `_keywords.py` implementation checks
  evaluated properties. Focused fixtures exercise composed-event closure and
  explicit UUID format assertion using the existing offline registry fixture.
- [RFC 9562 section 5.4](https://www.rfc-editor.org/rfc/rfc9562.html#section-5.4)
  defines UUIDv4 representation and generation. Shape checks cannot establish
  randomness, issuer, ticket authority or uniqueness under concurrent admission.
- Producer validation: eight focused text-schema methods and one broader batch
  of 98 schema methods pass. No dependency installation/lock change, socket,
  provider, staff console or retention implementation was exercised. The schema
  deliberately cannot reject whitespace, lone surrogates or safe rendering errors
  by itself; those remain actual-ingress/output obligations.
