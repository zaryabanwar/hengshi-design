# Staff session handoff profile v1 — independent review, 2026-10-06

Verdict: PASS for the bounded definition proposal. No actionable contradiction found in this scope. This receipt is uncommitted; no repository task is marked DONE.

Scope: only `Staff session activity and consultation fencing proposal — 2026-10-06`, frozen `snapshots/04-SECURITY_PRIVACY_CONTRACT.md:442–562`; the other twelve inputs supply authority/context. This is an additive proposal, not another revision or acceptance of the original staff sign-in mediation proposal.

Frozen packet: `output/research/staff-session-handoff-profile-2026-10-06/review-inputs.json`.
Manifest SHA256: `03f0eede86913ad851391b0409d6d2498daca87bff62bd4617f6b2d289d0424e`.
All thirteen snapshot byte counts and SHA256 values matched the manifest; reviewed the frozen inputs, without live-source substitution.
Security snapshot: 40,793 bytes; SHA256 `283cc68e4f8634ca3a8abf49eeb2051528e59e6dcd6470646ba698e137d370b9`.
Original security prefix: exactly 32,221 bytes, matching the supplied before-snapshot; SHA256 `50f3c00d5e6aed36bb4fa99e864ba337cc3dc3f76c0665ff30e0f765782ad00a`.

Evidence below uses paths relative to that packet's `snapshots/` directory.

- `04-SECURITY_PRIVACY_CONTRACT.md:459–474`: only first guarded admission of an explicitly permitted business command qualifies as proposed idle activity. Positive admission may be pending; it proves neither commitment nor delivery. Replay/reconciliation, denied attempts, reads, polling, heartbeats, reconnect and client activity signals do not renew it. Other action mappings remain held.
- `04-SECURITY_PRIVACY_CONTRACT.md:476–484`: accepted 30-minute idle/eight-hour absolute bounds remain intact, with initial sign-in and original-session anchors. Rotation and new channels cannot reset absolute expiry. Atomic shared ordering must reject activity at/after expiry or revocation and deny on uncertain authority; no clock/store mechanism is claimed implemented. Accepted bounds also appear in `10-spec.md:122`.
- `04-SECURITY_PRIVACY_CONTRACT.md:488–506`: every protected effect, replay and private-output admission requires current session and object/action/purpose/ownership/source/consent authority. Ordered session/work generations fence stale workers, tickets and queued output; closure does not settle uncertain external work or release its reservations. Server logout is distinct from provider redirect/cookie clearing.
- `04-SECURITY_PRIVACY_CONTRACT.md:508–514`: session loss fences access without inventing consultation, delivery, booking or public availability outcomes. Availability evidence can independently expire/be fenced; actual ending/reassignment/deletion remain separately guarded operations.
- `04-SECURITY_PRIVACY_CONTRACT.md:526–535`: fresh sign-in requires fresh current authority; same-person identity cannot recover obsolete ownership or purpose. Lost ephemeral material stays unavailable. Retained state requires its approved legal class; uncertain old operations require reconciliation before fresh text, without resending old intent.
- `04-SECURITY_PRIVACY_CONTRACT.md:518–524`: exact accessible continuation is explicitly held. The accepted TPL-STAFF-AUTH/TPL-STAFF-QUEUE TL-WARN-EXTEND records in `12-column-authority.json` still require warning, extension and preservation; a warning or new login is correctly not presented as satisfying them. This slice neither changes those records nor resolves their implementation.

Primary-source verification, 2026-10-06:

- [FastAPI WebSockets](https://fastapi.tiangolo.com/advanced/websockets/) documents dependency and disconnect hooks, and explicitly limits its in-memory connection-list example to one running process. Continuing authorization/shared fencing are project requirements, not automatic framework guarantees; the appendix accurately separates these.
- [OWASP WebSocket Security](https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html) calls for expiry/logout handling and authorization for each action. [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#session-expiration) distinguishes server-enforced idle, original-session absolute and renewal clocks. The consultation activity allowlist is explicitly a Hengshi proposal, not an OWASP-selected rule.

Remaining prerequisites: founder selection/acceptance of this proposal and exact accessible continuation; cookie/JWT/CSRF issuance/rotation/reuse and Entra freshness/outage policy; other-action activity mappings; authoritative shared clocks/store/generation propagation; legal/source retention; finite physical allocation/cleanup; actual API/socket/store and accessible-browser evidence for the cases at `04-SECURITY_PRIVACY_CONTRACT.md:549–561`.

No runtime, schema or ordinary prose tests were run: no implementation/schema changed. Integrity checks establish frozen identity only. No runtime/security/accessibility certification, integrated Phase 1 approval, founder acceptance or grant is implied.

Only this requested receipt was added. Producer sources, accepted timing records, prior review receipts, protected prototype/GLB and unrelated edits were untouched; no agents, settings changes, commits or external writes were made.
