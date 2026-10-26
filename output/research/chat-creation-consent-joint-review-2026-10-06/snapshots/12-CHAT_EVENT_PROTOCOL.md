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
