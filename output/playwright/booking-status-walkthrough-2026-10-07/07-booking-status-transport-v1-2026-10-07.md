# Booking status transport and bounded refresh — independent review, 2026-10-07

Verdict: REVISE for BKT-01 below. Scope is only frozen `PRIVATE_PROCESS_PROOF.md:1244–1376`, the additive IF-BOOK-07 transport/refresh proposal. Earlier read/shape proposals and receipts are context, not broader re-review or acceptance.
Packet: `output/research/booking-status-transport-2026-10-07/completion/review-inputs.json`, SHA256 `17b36a97c7f0e88eef77f14040df4cf748727d48bddfc9e06b0ade79bb0c0527`; all 18 frozen byte lengths/hashes independently verified before and after receipt. This is the first review of the completed producer proposal; initial parent preparation is not a prior verdict/revision cycle.
Exact predecessor: 92,845 bytes SHA256 `15abf3fc95262e482de6ab912027e81fac90922274208981831c947ec1fca684`, retained as exact prefix of the 102,614-byte reviewed contract SHA256 `99b9102915238d81a8a5a3ed1bdfe883ad0e4fac8525b062f87a1a320ed3f72a`. Current contract equals this frozen copy; current response/common schemas equal their frozen prior identities.

Exact frozen identities (snapshot names within the completion packet directory; SHA256):

| Snapshot | Bytes | SHA256 |
|---|---:|---|
| 00-PRIVATE_PROCESS_PROOF.md | 102614 | `99b9102915238d81a8a5a3ed1bdfe883ad0e4fac8525b062f87a1a320ed3f72a` |
| 01-booking-status-response.schema.json | 4072 | `1e2dd46fbf572a095827edbef681344df6ed74aaeb6f4e0abd8eeab705ff65da` |
| 02-process-value.schema.json | 1494 | `b4fd9fc84f322ecb6743c00244f3731ccd612861de53056aaddb20a377a67a95` |
| 03-DATA_CONTRACT.md | 33922 | `a1f9f33a86b12b451f11e6ef5132b6e2ebeeefe21e5dbb96d3cc1e47e77b6d47` |
| 04-SECURITY_PRIVACY_CONTRACT.md | 51692 | `fafea73bdcedcf3057d504b98514f5796b331bf0184d30d10a165aae754e336f` |
| 05-INTERFACE_CATALOG.md | 38158 | `d7da364547c19344ccb1fca5a2554bb27410a7234f8209afade8664980f55c79` |
| 06-interface-catalog.csv | 9367 | `42018a3e5cc6c1edf488c392b0349688a92b2cab5a8f50e717f1bca84a70a49c` |
| 07-process-fields.csv | 71516 | `5737b8f4bd47b90a5020ae8943cb2c7786582c605e14d97212b4334ffb26522a` |
| 08-FLOWS.md | 29631 | `168015a15b51c03cdf1f1532572d7b45c397708651c579c3e1e2025d5ee27097` |
| 09-STATES_AND_RECOVERY.md | 24105 | `fa3322d864dc8c29d2f7853d6dc9a961126f7a8aea2b575505997d05c3297064` |
| 10-booking-status-read-v1-2026-10-07.md | 5685 | `7e6872f051e60a223d83c065d4ec629178b745df3a8dd9a2978d887fce93c08b` |
| 11-booking-status-shape-v1-2026-10-07.md | 8468 | `f28a6dcb71a9dd0a5431f5b67f23b6343a208c61e05caee54b128af7ecf2acff` |
| 12-AGENTS.md | 7686 | `55405cb02a96d05f7f6d68e56a588d743f83877fb2691a5a9f2c736126adbcc5` |
| 13-constitution.md | 16234 | `33ec0bb02b0d0d9a55d0971589bd19f7242f5d56da130f8f496bc1d31a8b5d23` |
| 14-DECISIONS.md | 80333 | `ac3075adbc4414d88e4b0f7f111a0476c0dd461596c08943d488d3b7d8949d20` |
| 15-TASKS.md | 4122 | `a43ee7d44f2b9b0a5b2fe24b1b0cac3a1928387ec8d882037c2975253038a3e5` |
| 16-PROJECT_STATE.yaml | 6250 | `d1a4eace1bea848cf5b3207e3d65a9f4202f98bd14ef9535ecbad21f18a9c7da` |
| 17-PRIVATE_PROCESS_PROOF.md.before | 92845 | `15abf3fc95262e482de6ab912027e81fac90922274208981831c947ec1fca684` |

Actionable finding (path:line refers to the frozen 00 snapshot):

- BKT-01 [P2] — `00-PRIVATE_PROCESS_PROOF.md:1295,1306–1307`: HEAD is refused without object lookup, but the generic bodyless rule permits Content-Length: 0. [RFC 9110 §8.6](https://www.rfc-editor.org/rfc/rfc9110.html#section-8.6) permits Content-Length on a HEAD response only when it equals the content size the same GET would send; an authorized GET here has a nonempty private snapshot (or JSON error). Zero content transmitted does not establish that metadata value. Explicitly omit Content-Length on every route-owned HEAD response/refusal; preserve zero content and no object lookup, and do not calculate a hypothetical private GET length. Later qualify middleware/ingress header behavior at the actual HTTP boundary.

Other bounded coverage:

- Route/admission: `00:1255–1275,1289–1309` preserves catalogue GET, selector-only UUID, strict empty request/framing, conditional/range refusal, current booking-cookie/Origin checks and fixed non-disclosing outcomes. Effective Accept uses RFC media specificity/quality; known unsupported methods get 405/Allow and unimplemented methods 501. `00:1285–1287` explicitly amends earlier all-JSON generality for bodyless transport refusals; unchanged schema only covers body-bearing representations.
- Disclosure/effects: `00:1277–1283,1301–1309,1353–1356` keeps complete bounded JSON serialization, output-authority recheck, no truncated success, no cookie/CSRF/generation issuance, no-store/nosniff and no CORS/redirect diagnostics. It adds no booking/provider/reconciliation/alert effect, read-based renewal, authority or retention permission; stale/unknown observation cannot settle a booking.
- Resource proposals: `00:1267–1271,1277–1279,1313–1335` states 16,384 decoded header bytes, 8,192 Cookie bytes, 64 fields, 256-byte target, five-second receive, 1,024 output bytes, service-wide 64 readers/one per authorized context, two-second authority/projection, five-second delivery, ten-second client observation, ten starts/rolling sixty seconds and 1,024 live limiter keys. Receiving/delivery/draining ownership stays reserved until settlement; rotation/tab/worker changes cannot reset accounting, no active eviction/hidden queue is allowed, and uncertainty denies admission. These are unmeasured definitions; cancellability, queries, clocks, capacity and cleanup mechanisms remain held.
- Refresh proposal: `00:1337–1356` limits deliberate bursts to five starts/180 seconds, using 10/20/40/60-second waits only after valid pending states. Errors/inconsistency/429/terminal state stop automation; hidden/offline/leaving/proof-loss/context/expiry fences waits and replies without resuming on restoration. Manual refresh spacing and advisory thirty-second 429 delay grant neither success nor reconciliation. Existing revision/access-loss rules remain, including no lower/conflicting revision or stale-context error overwrite.

Primary sources independently read: [RFC 9110 GET](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.3.1), [405/Allow](https://www.rfc-editor.org/rfc/rfc9110.html#section-15.5.6), [Accept](https://www.rfc-editor.org/rfc/rfc9110.html#section-12.5.1), and [RFC 6585 §4](https://www.rfc-editor.org/rfc/rfc6585.html#section-4). They support the general method/media/429 distinctions, not project capacities, identity accounting or wait choices; §8.6 exposes BKT-01. Prior no-store/authorization sources are context.
Remaining limits: actual ingress/framing, shared limiter/store/clock/cancellation/cleanup/output mechanisms, measured load/backpressure, privacy/legal mappings, accessible production references, stable graph and integrated/founder acceptance remain held (`00:1368–1376`). Numeric proposals do not establish capacity, timing SLA or runtime enforcement. No new endpoint, schema, session lifetime, provider selection or cancellation entitlement is accepted here.
Actual actions: frozen/current identity and preserved-prefix inspection, bounded contract review and official-source reads. No prose/schema/runtime/browser tests or broad suite; only this uncommitted receipt authored. Producer inputs, application, model/account/provider/Figma/Git and unrelated edits unchanged.

## Correction 1 disposition — 2026-10-07
BKT-01 CLOSED; PASS for this corrected bounded proposal. Exact single paragraph replacement verified against original 00 snapshot: every HEAD refusal omits Content-Length and does no hypothetical private GET length lookup; other bodyless refusals retain optional zero length. No other byte changed.
Corrected immutable copy/canonical at inspection: 102,756 bytes SHA256 `b178fbfa3ace77a9f8c0bf02e89da811dfcf53a6cbaa4420e6a5189823b6c7d3`; correction record SHA256 `e187e16a0f1d0002b55f8ae37a3427934d5dbc66b7f3feba32330451144f56c5` at `output/research/booking-status-transport-2026-10-07/correction-1/correction.json`.
Original 43-line/7,359-byte REVISE receipt prefix remains exact, SHA256 `36963a6b29b2a33404891ae9daa09d5180ea6256b6a91d601de98c9c2a77f103`; all original 18 frozen identities/manifest, preserved predecessor and current response/common schemas unchanged. Initial current-copy equality above predates the producer correction.
Only this receipt append authored; no tests rerun. Resource/mechanism/HTTP/browser qualification and integrated/founder acceptance remain held; this first bounded revision establishes neither runtime enforcement nor production approval.
