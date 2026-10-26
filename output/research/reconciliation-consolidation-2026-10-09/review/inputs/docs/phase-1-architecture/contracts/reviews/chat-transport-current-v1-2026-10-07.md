# Independent current chat transport review — v1

Reviewed 2026-10-07; receipt preserved 2026-10-08. Status: DOING; uncommitted.
Independent reviewer: `/root/review_visitor_lifetime_controls_current`.
Verdict: **bounded PASS** for the exact seventeen-input close/recovery proposal.
No consequential security or external-contract inconsistency found. No adoption.

## Exact inspected inputs

The [seventeen-input manifest](../../../../output/research/chat-transport-current-2026-10-07/review-inputs.json) has SHA-256 `0786a4843b54435fbb6d92909f2c6c83d2ed20b61c5c3f1bc5e0661efba15d5a`.
All frozen byte counts/hashes matched initially and finally, with final independent verification at `2026-10-07T08:52:03.0494422Z`. Snapshot paths are relative to that manifest directory. Later receipt/state/reference edits are outside the frozen inputs.

## Returned disposition

- Frozen `CHAT_EVENT_PROTOCOL.md:416–450` separates pre-upgrade HTTP denial from WebSocket Close, prohibits private reasons, distinguishes application JSON rejection from framing failure, excludes reserved emission codes, and acknowledges a valid peer Close even outside the project emission profile. RFC 6455 requires acknowledgement but describes status echo as typical rather than mandatory; empty-reason 1000 acknowledgement is permissible. [RFC 6455 §5.5.1](https://www.rfc-editor.org/rfc/rfc6455.html#section-5.5.1)
- The same snapshot:448–450,506–514 accurately separates browser explicit codes from server codes and holds denial-extension capability unselected. Official WHATWG source confirms 1000/3000–4999 restrictions, the 123-byte reason limit and limited failure disclosure. ASGI/Starlette confirm pre-accept HTTP 403 and extension-dependent alternative denial. The published WHATWG endpoint timed out; its official primary source was checked successfully. [WHATWG source](https://raw.githubusercontent.com/whatwg/websockets/main/index.bs), [ASGI](https://asgi.readthedocs.io/en/stable/specs/www.html#close-send-event), [Starlette](https://starlette.dev/websockets/#send-denial-response)
- The same snapshot:454–473 fences commands and pending application output, prohibits data after Close and retains uncertain cleanup reservations. Transport cleanup cannot settle/release unresolved business work. Five seconds is an unmeasured target. Browser `close()` cannot discard messages already submitted to the user agent; the proposal's inability to recall old bytes preserves that distinction. [WHATWG close algorithm](https://raw.githubusercontent.com/whatwg/websockets/main/index.bs)
- The same snapshot:477–502 permits at most four attempts in a sixty-second monotonic episode, bounds initialization by both deadlines, fences late readiness, prevents remount/flapping resets and prohibits automatic business redispatch. These are project proposals; RFC guidance supports randomized increasing backoff without prescribing these ceilings. [RFC 6455 §7.2.3](https://www.rfc-editor.org/rfc/rfc6455.html#section-7.2.3)
- The same snapshot:573–579 narrows the earlier source gate: current ownership/proof/CSRF may admit control-only continuation/End while dependent content remains held. Lines 478–479 stop automatic recovery on authority/consent loss; they do not revoke otherwise permitted own-process controls.
- Frozen `DECISIONS.md:1006–1018` and `CHAT_EVENT_PROTOCOL.md:473,496–502,551–571` separate transport/work deadlines from thirty-minute inactivity/authorized End. Reconnect, receipts and admission observations cannot manufacture activity or renew consent. No hidden absolute visitor lifetime follows.

## Held limits

Historical thirteen-input no-verdict evidence remains historical. Later visitor-control and encoding receipts retain their exact bounded authority. No prose/schema/runtime tests, installations or writes were performed during review.

Exact runtime selection, physical teardown, actual ingress/resource enforcement, concurrency, provider settlement, accessibility/UI, legal mappings, integrated acceptance and founder adoption remain held. This PASS establishes neither whole-package acceptance nor runtime security/readiness. The reviewer changed no files; preserving this receipt does not modify the inspected snapshots or authorize application, provider, Figma, Git or deployment operations.
