# Independent visitor lifetime control review — v1

Date: 2026-10-07. Status: DOING; uncommitted, commits remain deferred.
Independent reviewer: `/root/review_visitor_lifetime_controls_current`.
Verdict: **bounded PASS for the D-076 visitor continuation/End definition and closed representations**.
Material findings: none established in this bounded scope. No runtime or founder acceptance.

## Exact inspected inputs

The [26-input manifest](../../../../output/research/visitor-lifetime-control-2026-10-07/review-inputs.json) has SHA-256
`09993498ab6152a25407ffbba7bffee7045f0fb6807d6ac189578ae16c73bdae`.
All 26 frozen snapshot hashes and byte counts matched, including final verification.
Review evidence uses the manifest's snapshots, not moving current-source authority.
The packet preserves the earlier unavailable review attempt; this completed recovery review is separate.
Later receipt, reference, manifest or state edits are outside the inspected bytes.

## Returned disposition

- Frozen [CHAT_EVENT_PROTOCOL.md](../../../../output/research/visitor-lifetime-control-2026-10-07/review-inputs/docs/phase-1-architecture/contracts/CHAT_EVENT_PROTOCOL.md):542–579 preserves current ownership, Origin, proof and CSRF checks. Process/lane-bound tickets are non-bearer metadata. Content/source holds preserve eligible own-process continuation/End controls while dependent content, replay, sharing and provider work remain separately guarded.
- The same snapshot:583–607 requires atomic ticket/revision/shared-time admission. Admission at or after expiry denies; activity, expiry and End share a fence. Immutable applied receipts remain separate from fresh lifetime observations; unknown older tickets cannot establish non-execution or silently cause another extension.
- The same snapshot:627–659 restricts visitor End to own-process authority and requires terminal fencing before completion. Its own-End receipt exception permits only the admitted ticket's final result on the original initialized channel, bound to pre-End authority, within a non-resetting five-second window. Earlier unrelated authorization loss cannot be bypassed; no history, provider, renewal or new-connection permission follows.
- The same snapshot:673–690 proposes separate 48 ordinary/16 ending allocations and one ordinary plus one End admission per initialized connection. No hidden queue, borrowed capacity, fabricated success or timeout-only reservation release is permitted. These allocations remain unmeasured, not a service promise.
- The same snapshot:609–623 and frozen [HANDOFF_LIFECYCLE.md](../../../../output/research/visitor-lifetime-control-2026-10-07/review-inputs/docs/phase-1-architecture/contracts/HANDOFF_LIFECYCLE.md):1224–1250 preserve accessible warning, at least 20 seconds usable response time, repeated extension, focus and permitted progress. The accepted `extension_factor_min: 10` stays distinct from ten extension opportunities; complete-process mapping remains held. [W3C SC 2.2.1](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html) supports that distinction, not automatic conformance.
- The same protocol snapshot:661–669 separates immediate server revocation from later applicable cookie clearing, provider cancellation, booking cancellation and verified retained-copy deletion. Physical cleanup and uncertain work cannot be represented as completed deletion or ending delivery.

## Residual security risk

A stolen but still-valid visitor proof can potentially be kept active indefinitely through authorized-looking activity. Idle expiry, current ticket checks and finite work pools do not independently bound that exposure. Frozen [PRIVATE_PROCESS_PROOF.md](../../../../output/research/visitor-lifetime-control-2026-10-07/review-inputs/docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md):897–936 recognizes the founder's no-absolute-duration choice and holds concrete clock/store/fencing and credential mechanisms for later review. This remains an implementation risk; it does not establish that OWASP endorses indefinite anonymous credentials. [OWASP session guidance](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#session-expiration) explains why attacker activity can defeat idle expiry and recommends absolute expiry.

## Independent reproduction and held limits

Executed from the frozen snapshot root, using its schema/test files and offline registry:

```text
C:/Python314/python.exe -B -m unittest scripts.validation.test_chat_event_control_schema scripts.validation.test_chat_text_schema scripts.validation.test_staff_chat_control_schema scripts.validation.test_visitor_lifetime_control_schema
```

Result: **24 affected schema methods PASS**, exit 0; elapsed test time **6.730 seconds**.
These establish representation validation only, not authentication or runtime enforcement.
Frozen [test_visitor_lifetime_control_schema.py](../../../../output/research/visitor-lifetime-control-2026-10-07/review-inputs/scripts/validation/test_visitor_lifetime_control_schema.py):112–126 explicitly demonstrates that schema shape cannot prove temporal relationships or current authority.

Authentication, current ownership/human intent, shared-clock correctness, atomic persistence, runtime races, effective revocation, scoped End receipt delivery, measured capacity, provider cleanup, privacy/legal compliance and WCAG conformance remain unproven. Background return with insufficient usable warning, complete-process extension-factor mapping and assistive-technology progress preservation remain held. End-pool priority enforcement, raw transport/resource bounds, physical settlement, approved complete-process screens, the full compatible graph and integrated/founder acceptance also remain held.
This verdict covers only the exact frozen proposal/representations. It grants no application development, storage, endpoint, provider, Figma, publication, Git or deployment authority. The review changed no files or external systems; subsequent authorized preservation creates this one uncommitted receipt only.
