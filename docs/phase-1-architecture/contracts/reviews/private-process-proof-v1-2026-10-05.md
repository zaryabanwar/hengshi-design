# Anonymous private-process proof — independent review v1

Reviewed 2026-10-05. **REVISE: one medium wording contradiction, PPP-MED-001.** This first review covers the new logical security/transport proposal and the two declared catalogue changes only. It is not implementation, whole-catalogue acceptance or founder approval.

## Exact inputs

Packet: `output/research/private-process-proof-2026-10-05/review-inputs.json`, SHA256 `60d28c6e7a4c5cd46f9fabb84f82bb0189347c5b812817230ac34b1e9012f693`. Independently recomputed all 17 frozen sizes/hashes and verified byte correspondence to current sources, plus all 10 protected-input guard hashes.

| Producer | Bytes | SHA256 |
| --- | ---: | --- |
| `docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md` | 16,385 | `693adf340b2db83736a457742981f00e96de5d2e343343c681ab2cc5e886c55a` |
| `docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md` | 32,203 | `03bc48bf98eefcd51fa5682cdfe5579bf23ea3d9e149acb40195de0e79450abd` |

Removing the new reference paragraph and restoring the single `verified` → `signed` historical descriptor exactly reproduces the 31,646-byte before catalogue, SHA256 `a8db67351427e93f9f32568691fa0a9f96bd7778cb3fa3bcefe74ce900798301`. All proposal local files/heading anchors resolve. These are artifact-integrity checks, not runtime tests.

## Actionable finding

**PPP-MED-001 — narrow the browser-storage prohibition to preserve the specified cookie transport.** `PRIVATE_PROCESS_PROOF.md:48` prohibits the raw secret in “browser storage”, while lines 19–20 and 50–51 require the bearer in a browser cookie. Cookies are browser storage; the literal restriction therefore contradicts the proposed transport. Amend the restriction to expressly forbid script-readable storage such as localStorage/sessionStorage and other unapproved browser stores, with the approved protected HttpOnly cookie as the sole bearer browser transport. Keep the database/replica/job/evidence/telemetry exclusions and the no-JSON/query/subprotocol/clipboard/email rules. This is a narrow clarification, not permission for another credential channel.

## Inspected coherence and evidence

No other actionable contradiction was identified within this proposal:

- Opaque proofs remain per-process, generation- and purpose-bound; selectors do not authorize access, possession does not establish identity/email/consent, and privacy target verification precedes its separate minimal status proof. Staff JWT/bcrypt/Entra and emergency controls remain separate. Chat-to-booking transfer requires explicit action and purpose permission rather than proof/history cloning.
- Bootstrap at the existing chat/booking POST boundaries allocates only bounded ephemeral provisional state after explicit action and exact Origin checks. It admits no message, qualification, consented history or external effect. Promotion requires current provisional proof, separate CSRF proof and scoped immutable operation meaning. Lost allocation need not be exactly once; unknown promotion reconciles rather than dispatching another create. Exact envelopes/admission mechanisms remain held.
- Host-only Secure/HttpOnly/Lax cookies, distinct process/generation slots, duplicate rejection, current selected-generation checks and bounded cleanup recognize shared tab/port scope. Prefixes, SameSite, CORS and CSRF do not establish object authority or XSS safety. Host/proxy trust and measured header/cookie capacity remain unresolved inputs, not selected infrastructure.
- WebSocket Origin/cookie/session checks precede acceptance; a distinct initialization CSRF frame gates all private events, subscriptions and business commands. Current generation, consent, assignment and source authority continue at message/replay/outbound decisions. Revocation must fence queued/in-flight delivery; neither a timer nor disconnect certifies immediate cross-system suppression. Staff sockets retain separate identity/assignment.
- Proof validity, business/challenge clocks and record retention stay distinct. Non-consented chat/replay/proof metadata remain ephemeral; durable verifier metadata needs its own approved class/store mapping. Restore cannot resurrect revoked generations. Lost rotation replies/proof do not prove cancellation, deletion or confirmation, and recovery cannot infer ownership from email or silently dispatch another booking.

Independently consulted [OWASP session guidance](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html), [CSRF guidance](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) and [WebSocket guidance](https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html). They support scoped random secrets/server expiry, one-way verifiers for store-disclosure threats, synchronizer/origin defenses and continuing socket authorization; they do not accept this particular two-phase design or its 256-bit recommendation. [MDN Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie), [RFC 6265 §8.5](https://www.rfc-editor.org/rfc/rfc6265.html#section-8.5) and the [browser WebSocket constructor](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/WebSocket) corroborate cookie attributes/restore, lack of port isolation and the constructor's URL/protocol interface.

Official [FastAPI cookie](https://fastapi.tiangolo.com/advanced/response-cookies/) / [WebSocket](https://fastapi.tiangolo.com/advanced/websockets/) and [Starlette middleware](https://starlette.dev/middleware/) documentation support framework primitives and readable signed session payloads, not opaque server-state ownership or complete CSRF/revocation enforcement. Independently inspected the installed native prototype: FastAPI `0.138.0`, Starlette `1.3.1`; `Response.set_cookie` defaults Secure/HttpOnly to false. Installed `sessions.py` SHA256 and all 15 quoted source observations match the frozen notes, including signed base64-JSON handling. Optional session import independently fails with `ModuleNotFoundError: No module named 'itsdangerous'`; nothing was installed. These are local source/import observations, not selected stable-graph or application evidence. Producer Context7/source summaries alone were not treated as verification.

## Limits and remaining gates

Exact cookie/CSRF/envelope formats, issuer/verifier cryptography, expiry/rotation/recovery, measured finite capacities, target-origin/ingress trust, current authorization and promotion/revocation/restore fences, identity verification and privacy-class/legal retention mappings, production references, complete compatible stable graph, actual HTTP/browser/store/socket behavior and integrated/founder acceptance remain held. No new account, staff grant, endpoint, provider, persistence permission or production operating claim is accepted. No prose wording tests or application tests were added/run. Only this receipt was authored; producer/protected inputs were unchanged at final inspection.

## Correction-1 disposition — superseding bounded PASS

Reviewed 2026-10-05. **PASS for the corrected proposal; PPP-MED-001 closed. No remaining actionable findings within the original scope.** The original REVISE and its evidence above remain an exact receipt prefix, SHA256 `47d30608d428b3b574a4e00d248b23045b82dd433a3c7889cdf945fe2a42e20d`.

Correction packet: `output/research/private-process-proof-2026-10-05/correction-1/review-inputs.json`, SHA256 `c4e69c581cdc05f0bbc8bed897776d586c4d6dd37520de00ca1f8ca53003a95d`. Corrected `PRIVATE_PROCESS_PROOF.md`: **16,586 bytes**, SHA256 `891ebd8f5e051b335f833f32ccff4242d755a326dd827798fc87126df35ae036`. The catalogue remains **32,203 bytes**, SHA256 `03bc48bf98eefcd51fa5682cdfe5579bf23ea3d9e149acb40195de0e79450abd`.

Independently verified all 17 corrected snapshot/current-source identities, byte equality of the other 16 inputs across packets, preservation of the original manifest and all original snapshots, and all 10 protected-input hashes. The sole producer diff replaces the blanket browser-storage exclusion with an explicit protected HttpOnly cookie as the only browser bearer transport, and rejects script-readable localStorage/sessionStorage and any other unapproved browser store. Database/replica/job/evidence/telemetry exclusions and the existing no-body/query/subprotocol/email/clipboard restrictions remain unchanged.

The correction resolves the contradiction without broadening authority or adding a transport. No application or prose tests were required or run for this exact prose repair. All original held implementation, security/privacy, physical enforcement, compatible stable graph and integrated/founder gates continue unchanged; this PASS is only corrected definition coherence. Only this receipt was appended.
