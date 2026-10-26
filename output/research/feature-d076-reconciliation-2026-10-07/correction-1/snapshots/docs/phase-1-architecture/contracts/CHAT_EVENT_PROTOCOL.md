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

D-076 now selects 30-minute visitor inactivity expiry or authorized explicit End,
with no absolute conversation duration. The [amended visitor access profile](PRIVATE_PROCESS_PROOF.md#access-lifetime-retention-and-pending-cleanup)
owns proposed genuine-activity, warning/More time, shared-clock and terminal-fence
rules; staff authentication, booking and finite resource clocks stay separate.
Initialization, receipt, replay, reconnection and provider output cannot renew
visitor access. Earlier bounded reviews remain at their frozen inputs; this later
clock reconciliation and concrete visitor End/More time directional mechanisms
need independent review before wire acceptance or implementation.

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
Idle sockets do not renew the visitor conversation's server-authoritative inactivity deadline. Reservation
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

Status: DOING, correction 1 awaiting independent re-review of CHAT-TEXT-01.
The earlier control review does not cover this addition. The initial text review
and its exact frozen inputs are preserved in the [review receipt](reviews/chat-text-v1-2026-10-06.md).
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

Sequenced delivery events contain immutable protocol/kind, session-bound stream,
server-issued UUIDv4 `event_id`, positive sequence, original `release_identity`
and kind-specific payload. They contain no `channel_id`, `proof_generation` or
`consent_revision`: those are current connection metadata on ready/admission/client
controls, not immutable event bytes. On every new or replayed delivery, the server
checks current proof, consent, source eligibility and assignment independently.
The receiver binds callbacks to its active socket attempt and readiness snapshot,
then checks stream, contiguous order and immutable event identity. Old-attempt
callbacks cannot update the new projection. A received event supplies no current
permission or proof generation; transport admission and disclosure guards do.

Preserve stream/event/sequence/kind/release/payload bytes on eligible replay; never
rewrite an old event's release or source to make it eligible. A source-dependent
delivery can become unavailable without inventing an end/cancellation outcome for
unrelated valid human-process truth. Exact event-context/source registrations remain
held; no release-substitution or recovery flow is selected here. A `command_result` identifies the
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

## Transport close and recovery proposal — 2026-10-06

Status: DOING; independent review and integrated/founder acceptance pending.
This addition fills the transport close-profile gap identified above. Earlier
control/text receipts cover their frozen bytes only. Text correction 1 has since
received the [bounded PASS](reviews/chat-text-v1-2026-10-06.md); its earlier
awaiting-review label remains dated history, not the current disposition.
No new endpoint, business state, provider, wire variant or application is created.

### Denial, close codes and private output

Before upgrade, reject without private body, session-existence detail, credential
echo or reason-specific header. The standard framework pre-accept close produces
HTTP 403, not a WebSocket close message. Do not accept merely to return an error.
Different denial responses require verified server-extension capability; none is
selected here. A browser may expose only generic connection failure, not that
HTTP status. It must not infer that a process expired, ended or never existed.

After upgrade, application-initiated closing uses an empty UTF-8 reason. Never
send a private selector, exception, provider result or policy detail in it. A
currently authorized minimal unavailable control, when appropriate, precedes
Close and stays within existing queue/byte ceilings. Authority failure sends no
private control. Failure to send that optional control still closes; it does not
retry privately, replace an immutable event or certify delivery.

| Server/transport code | Proposed use; no business-state assertion |
|---|---|
| 1000 | Normal termination of this transport subscription. A confirmed business end uses its separate guarded contract. |
| 1001 | Server going away/shutdown. No staff-unavailable, cancelled or deleted finding. |
| 1002 | WebSocket framing/protocol violation, enforced by the transport parser. Invalid application JSON alone is not a framing error. |
| 1003 | Unsupported binary data where the chat channel accepts text only. |
| 1007 | Invalid UTF-8 text payload detected at the transport boundary. |
| 1008 | Generic policy denial: invalid closed/raw JSON, wrong direction/state, invalid proof/CSRF, expired admission, initialization timeout or lost current authority. Also slow-client output exhaustion without a more specific received-message violation. |
| 1009 | Received message exceeds its finite admitted encoded/reassembled limit, before unrestricted parsing/allocation. |
| 1011 | Unexpected server failure preventing transport service. Not proof of business rollback or non-execution. |

The table is the project's emission profile, not an assertion that other valid
peer codes do not exist. Incoming Close reasons are untrusted; never display,
reflect or retain them in ordinary diagnostics. If this endpoint has not already
sent Close, acknowledge a protocol-valid peer Close with 1000 and an empty reason,
even when the peer code is outside this application profile. Simultaneous Close
does not require another Close frame. Invalid peer frames/codes fail under the transport standard.
Do not emit reserved 1004/1005/1006/1015. Observed 1005/1006/1015 are diagnostics,
not application commands or proof of cause. Browser application code closes with
`close(1000, "")`, not server-only codes such as 1008; the browser API restricts
explicit codes to 1000 or 3000–4999. No private application code is selected.

### Closing fence, drain and unsettled work

At closing admission, fence this socket's commands, subscriptions, replay and
queued output before further application delivery. No data frame follows Close.
Pending private payloads are discarded under their mapped policy, not sent merely
to drain a buffer. Any permitted final unavailable control is sent before Close
and only while disclosure remains authorized. Closing cannot recall old bytes.

Propose five monotonic seconds from close initiation for the closing handshake;
fragments, pings, receipts and peer traffic cannot extend it. On expiry, request
physical transport termination. This is an unmeasured engineering target, not
proof the socket, task or external work stopped. Await verified local task/buffer
cleanup before releasing their connection reservations; uncertain entries remain
counted and deny new capacity. A selected runtime must support bounded teardown
and prove cleanup under its isolation/termination mechanism before acceptance.

The socket reservation is separate from an admitted text/provider, consent or
handoff operation. Even verified TCP/task cleanup cannot release an unsettled
business-work reservation, issue another text ticket, revoke process proof,
erase retention duties or settle an unknown external outcome. Those require
their own authoritative terminal/fencing evidence. Ping/pong, Close handshake,
receipt and reconnect never renew private-process proof clocks or consent.

### Bounded transport recovery

Only the current socket-attempt controller may schedule recovery. Explicit
visitor leave/end, a received policy/protocol/input rejection, lost proof/current
consent or an authorized unavailable recovery stops automatic reconnect. Offer
the existing permitted reconciliation or public Contact/Book paths; no credential
recovery, transcript reconstruction, fresh text submission or new handoff/booking.

For an ambiguous loss or server-going-away/unexpected-failure observation, propose
at most four upgrade attempts in one 60-second monotonic recovery episode,
including failed/timed-out attempts. Use random delay before each attempt with
upper bounds 5, 10, 20 and 20 seconds. Start no attempt after episode expiry;
each attempt retains the earlier five-second initialization deadline. No parallel
retry, background-tab retry storm or hidden retry queue. Bound each attempt's
initialization deadline by the episode deadline as well; fence late readiness.
A successful ready stops
scheduled retries but cannot reset the episode's counter/deadline. Navigation,
remount and a brief ready/close cycle cannot reset them either. After exhaustion,
only a deliberate visitor retry may start another bounded episode. This profile
is unmeasured, not a claimed RFC mandate or guaranteed recovery time.

Every new transport repeats current upgrade/initialize authority. Resume uses
only the eligible unchanged cursor; inability to prove a permissible suffix is
unavailable, not fresh history. A close code, `wasClean`, disconnect callback or
elapsed timer never changes the business outcome. The browser cannot reliably
distinguish a denied handshake from every network failure; ambiguous failures
remain bounded and carry no reason-specific claim. Server-wide admission limits
remain independently enforced across clients/workers.

### Evidence and remaining acceptance

Checked 2026-10-06: [RFC 6455 sections 5.5 and 7](https://www.rfc-editor.org/rfc/rfc6455.html#section-5.5)
defines transport control/closing and status semantics; its recovery guidance
supports randomized increasing backoff, not the project's particular ceilings.
The [WHATWG close algorithm](https://websockets.spec.whatwg.org/#dom-websocket-close)
defines browser code/reason restrictions. [Starlette's WebSocket guidance](https://starlette.dev/websockets/)
and Context7 `/kludex/starlette` show pre-accept HTTP 403, close emission and the
optional denial-response extension. [ASGI's WebSocket specification](https://asgi.readthedocs.io/en/stable/specs/www.html#websocket)
separates close/send/disconnect messages. Framework application state is not
physical transport/task/provider cleanup evidence; no version/server is selected.

No prose or copied-code tests are added. Required later actual-boundary cases:
pre-upgrade denial with no private bytes; invalid frames versus invalid JSON;
binary/UTF-8/size failures; no reason echo; policy change while queuing/closing;
full/blocked output queue; simultaneous peer/server Close; stuck close/cleanup;
unsettled provider work surviving a disconnect; expired proof during backoff;
late old-socket callbacks; flapping/remount without counter reset; finite failed
handshake attempts; and no automatic business redispatch. Legal mappings,
staff/handoff/end directional definitions, measured budgets, exact runtime/graph,
physical enforcement, production UI and integrated/founder acceptance remain.

## Visitor continuation and End controls proposal — 2026-10-07

Status: DOING, unreviewed. D-076 settles the product timing decision; this is a
proposed additional direction at existing IF-CHAT-03, not a new endpoint,
implemented timer or accepted security/accessibility mechanism. Earlier exact-input
control/text/closing reviews remain preserved and do not cover this amendment.

Use [visitor-lifetime-control.schema.json](visitor-lifetime-control.schema.json)
with its explicit client/server definitions, alongside the existing modules.
The root rejects every instance. These controls contain no transcript, provider
result, source grant, staff identity, consent decision, cookie or bearer secret.
Schema shape cannot establish current tickets, genuine activity, ordering,
terminal revocation, clock correctness or complete-process accessibility.

### Current admission, two distinct intent lanes

After successful current ownership/Origin/proof/CSRF initialization, send an
unsequenced `lifetime_admission` bound to that current channel and stream. It
contains the current proof generation, positive `lifetime_revision`, server UTC
Unix milliseconds and idle-deadline milliseconds, plus separate server-issued
renewal and ending tickets. Each ticket uses the existing UUIDv4 operation
representation and positive exact command revision. Tickets are process- and
lane-bound metadata, never bearer permissions or evidence of staff availability.
A deadline is an observation of authority, not a client-selected clock.

One renewal ticket and one ending ticket are current across all tabs/channels of
that conversation, independent of the text/provider ticket. Keep only the current
and latest settled renewal intent, plus the single ending intent. No growing
history of UUIDs, renewed record-retention period or hard conversation-age limit.
Do not reset revisions at reconnect/rotation; exhaust or lose authoritative state
safely, without reconstructing private state from browser selectors or logs.

Genuine admitted activity advances the lifetime revision and deadline and replaces
the renewal ticket. It does not consume the ending ticket. A current ending
intent remains available during pending text/provider or renewal work. A new
channel rebinds current tickets to its initialized authority; a late old-channel
admission/result cannot update a different active attempt or selected process.
Ticket equality alone cannot admit any action.

Send a fresh currently permitted `lifetime_admission` after a genuine activity or
applied renewal replaces the ticket, and on authorized initialization/reconciliation
of the active connection. It uses the same unsequenced control direction, not a
replayed historical grant. If its delivery is lost, the browser shows renewal state
as unresolved until it obtains current admission; a success receipt alone does not
issue a next ticket. Reconcile only within current authority and finite control/output
limits; receiving admission is never activity and must not renew the deadline.

Source withdrawal and refusal of optional retention do not remove an otherwise
currently permitted own-process continuation/ending control. Apply source/purpose
eligibility to dependent content, replay, sharing and provider work separately.
This narrows the earlier upgrade paragraph's source check: a valid owner may
initialize a control-only connection when content is held. `ready` alone grants
no content authority. Missing ownership/proof/CSRF or unknown process state still
denies the connection; no history or unavailable source is disclosed by controls.

### More time, warning and concurrent activity

`extend_idle` carries current channel/stream, the renewal ticket and the lifetime
revision it observed. No requested duration, client timestamp, role, retention
choice or new context is accepted. Atomically recheck current ownership, proof,
process state, ticket, lifetime revision and shared server time. Admission before
the existing deadline resets it to admission plus exactly 30 minutes, advances the
revision and settles that immutable ticket. At or after the deadline, deny rather
than backdate or resurrect authority. Failed/denied input does not count as activity.

Serialize this with message admission, consent/business changes, expiry and End
using the same authoritative fence. An activity or End that wins first cannot be
undone by a queued extension. A stale ticket may produce `not_applied/stale_ticket`
with a currently permitted snapshot; it is not a renewal success. Known identical
retries return the original permitted result, not another extension. Unknown older
tickets have no inferred no-effect outcome. `reconcile_idle_extension` observes the
same immutable ticket and cannot renew, dispatch or issue a replacement intent.

`idle_extension_result` is `applied`, `not_applied` or `pending`. Only current
permitted applied/not-applied results include a lifetime snapshot; pending contains
no guessed deadline. An applied receipt separately identifies the original applied lifetime revision
and deadline; its lifetime snapshot is a fresh currently permitted observation,
including any later genuine activity. Reconciliation cannot rewrite the original
applied result. A lower lifetime revision never replaces a newer one; equal
revisions must agree on the deadline, while server observation time may advance. The client accepts
results only for its selected process, active attempt and pending ticket. Lost
receipts reconcile that ticket while authority permits; no automatic new renewal.

The readable notice and More time control must be available from the beginning of
the process, with the selected inactivity rule and acknowledged current deadline.
Do not depend solely on a late push or throttled background countdown to introduce
the warning. Retain the accepted usable warning interval of at least 20 seconds,
keyboard/touch action, permitted-progress preservation and repeated extension.
A countdown is not a clock authority or a live-region announcement every second.
An unknown deadline is shown as unknown, never as a fresh 30-minute grant.

Reconnection or a background-tab return does not manufacture activity. If too
little usable warning remains, the complete-process reference needs explicit
review/evidence; this proposal claims no automatic WCAG pass or timer exception.
At expiry, stop affected controls/output and offer the permitted new-session or
Contact/Book path; do not claim restoration of a lost anonymous transcript.
Extension never renews source entitlement, consent, staff authentication, booking
or retention. Polling, receipt, provider output and reconciliation do not renew.

### Explicit End and narrowly scoped final acknowledgement

`end_conversation` carries the separate ending ticket and current channel/stream;
it does not depend on a possibly stale lifetime revision or source/consent map.
Require the current visitor's own-process authority. This visitor direction cannot
claim staff identity or end another visitor's process. Currently assigned authorized
staff use their separate governed human-consultation ending path; general staff
and content roles gain no private-AI access or ending power from this module.

At End admission, fence new messages, provider dispatch, preview preparation/sharing,
renewal and ordinary replay/output before reporting completion. Revoke applicable
proof/CSRF server-side and apply the existing ordered suppression/ending contract.
No End waits for an AI answer or falsely treats provider cancellation, socket close,
booking cancellation, staff availability off or verified deletion as its own result.
Already delivered bytes cannot be recalled. Physical cleanup and unsettled external
work keep their original reservations and truthful uncertain outcomes.

Propose a command-scoped closing receipt for the initialized channel that admitted
this exact ending ticket. It permits only that own `end_result`, despite revocation
caused by the same End. It grants no history/read/replay/provider/renewal authority,
accepts no unrelated command and cannot initialize a new connection. Bind it to the
original admitted process, channel, stream, ticket and pre-End authority; guessed
IDs and another channel have no such permission. Earlier unrelated authorization
loss cannot be bypassed by claiming End. This explicit exception refines general
post-revocation output fencing and requires independent security review.

`end_result` is `ended` only after committed terminal authority and required ordered
suppression are known; otherwise it is `pending`. Neither state carries private
content or a deletion/booking claim. `reconcile_end` may observe the same intent
under still-valid authority or its original limited closing receipt, never repeat
ending effects or widen access. Permit at most one final ending result during the
existing five-second monotonic closing window, then close. That window starts at
End admission, cannot reset on requests/fragments, and does not retain conversation
access. A lost/late acknowledgement or unproven fence remains unconfirmed in the UI;
new credentials/session creation cannot prove the old operation completed.

WebSocket messages cannot clear an HttpOnly cookie after upgrade: the
[ASGI WebSocket contract](https://asgi.readthedocs.io/en/stable/specs/www.html#accept-send-event)
permits response headers during acceptance, while later sends carry text or bytes.
Server revocation is immediate authority; a subsequent permitted HTTP response may
expire only the applicable process cookie. Residual cookie bytes never authorize access. Do not
clear staff or booking credentials to imitate conversation End. No local transcript
is reconstructed to explain ending, and ending does not certify deletion of every
consented/vendor copy; actual ephemeral cleanup follows DATA-004 and reviewed
class-specific privacy controls.

### Finite admission and later qualification

Keep the existing 8,192-byte complete control-input, 16,384-byte event, 64-event
and 262,144-byte connection-output ceilings and aggregate payload accounting.
For this amendment, propose splitting the existing 64 concurrent control-operation
ceiling into at most 48 ordinary and 16 ending operations. Permit one ordinary
and one separate End admission per initialized connection, with the same per-process
tickets across tabs; do not make End wait behind long-lived ordinary/provider work.
There is no hidden queue or borrowed capacity. Exhaustion or uncertain coordinator
state cannot be displayed as extended or ended. This split supersedes the earlier
one-control-per-connection profile only if reviewed/accepted; it is unmeasured,
not capacity proof or a new service promise.

Continuation admission/reconciliation uses a five-second monotonic work deadline;
the original server activity deadline still wins. A work timeout reports uncertainty,
never releases unproven reservations or silently creates another extension. End's
closing receipt uses that same finite window. Release an admission reservation only
after actual guarded operation cleanup/settlement; conversation expiry itself is
independent of a full command pool. Reserve the minimal final result within the
existing output ceilings, or close without inventing successful delivery.

Checked 2026-10-07 using Context7 `/websites/fastapi_tiangolo` and primary sources:
[FastAPI WebSockets](https://fastapi.tiangolo.com/advanced/websockets/) supports cookie/
dependency checks and explicit receive/send/disconnect handling; its process-local
tutorial manager and credential-echo/query-token examples are not adopted.
[OWASP WebSocket guidance](https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html)
supports message-level authorization and current server-side session invalidation.
These mechanisms and numerical allocations are project inferences, not framework
features or OWASP-mandated numbers. [OWASP session expiry](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#session-expiration)
recommends absolute as well as idle limits; D-076's no-absolute visitor policy remains
a specific product choice requiring risk review. [W3C SC 2.2.1](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html)
distinguishes adjustable duration and repeated extension; the accepted project
extension factor is not rewritten as an extension count.

Required later actual-boundary cases: current-owner success/unassigned-staff denial;
long legitimate use without a hard age cap; exact idle-boundary admission; genuine
activity versus duplicate/poll/provider output; two-tab extension and End races;
stale/lost tickets and equal-revision conflict; independent End during provider or
renewal work; source withdrawal with own-control eligibility; old proof/channel;
reserved-pool exhaustion; terminal fence versus outgoing bytes; scoped final receipt
versus unauthorized post-End reads; stuck closing cleanup; retained cookie after
revocation; late acknowledgements to another selected process; usable warning,
focus/reading preservation and repeated extension with assistive technology.

The closed schema fixtures validate representations only. Independent review,
concrete shared-clock/storage/fencing and priority enforcement, measured bounds,
approved complete-process screens, full compatible graph, actual runtime evidence
and integrated/founder acceptance remain held. No application feature is implemented.
