# Change Request CR-002 — Four Supported 3D Delivery Streams

**Status:** Proposed — awaiting founder approval. Nothing accepted has been altered.

**Requested:** 2026-09-06

**Requester and approval authority:** Founder

**Recorded by:** Hengshi project manager

**Earliest invalidated gate:** D-036 UX architecture, D-037 UI reference-design
contract, and the B07 batch classification in `design-batch-plan.csv`

**Classification:** Business confidential

## 1. Source and intent

On 2026-09-06 the founder stated that the 3D experience is **not optional**, and that
the product has different delivery streams selected by device capability and
connection conditions.

The accepted baseline says the opposite. D-036 and D-037 model an *optional* 3D
journey with a semantic Quick Access path as the guaranteed route, and
`design-batch-plan.csv` classifies batch B07 as "an optional enhancement."

This change request replaces the optional-enhancement model with **four supported
experience streams that carry equivalent core journeys**: high, medium, low, and
no-WebGL/semantic.

The intent is a reclassification, not a redesign. The accepted templates, route
inventory, action contracts, and accessibility requirements stay; what changes is
whether 3D is a guaranteed obligation and how a visitor is routed to a stream.

## 2. Current approved and reviewed baseline

### 2.1 Authority retained

- **D-025** — 33 canonical routes, claims and conversion foundation.
- **D-026 / D-035** — Evidence in Motion strategy and the frozen brand identity.
- **D-036** — UX architecture: 113/113, 33 routes, 53 action contracts, 45 UX tests.
  Its **content, action, recovery, and accessibility equivalence requirement is
  retained in full** and is strengthened, not weakened, by this change.
- **D-037** — the UI reference-design contract: 40 templates, 32
  responsive/state/mode profiles, 62 primitives, 271 traceability rows, nine batches.

### 2.2 Superseded framing

| Source | Current wording | Status under CR-002 |
|---|---|---|
| D-036 / D-037 | 3D journey is **optional**; semantic Quick Access is the guaranteed path | Superseded — both become supported streams |
| `design-batch-plan.csv` B07 | "as an optional enhancement" | Superseded — B07 becomes a core batch |
| `docs/active/3D_Mega_Menu_Style_Guide_v2.md` §8.2 | Four device tiers framed as **performance adaptations** and a "fallback to static image gallery" | Partially adopted — the tier shape is correct; the fallback framing is superseded |
| `docs/active/Hengshi_Design_SRS_v3.md` FR-3D-010 | "WebGL fallback for unsupported devices", `Not implemented`, priority **P2** | Superseded — becomes a core requirement, not P2 |

The two `docs/active/` documents are non-authoritative legacy drafts. They are cited
because they demonstrate the tier concept predates this request; they do not confer
authority and their "fallback" language is exactly what CR-002 corrects.

## 3. Authorized target and exclusions

### 3.1 Authorized target

**T-01 — Four peer streams.** Define high, medium, low, and no-WebGL/semantic as
supported experience streams. Each is a first-class delivery target with its own
acceptance evidence. No stream is a degraded consolation for another.

**T-02 — Equivalent core journeys.** Every stream delivers the same content,
actions, wayfinding, recovery, and conversion outcomes across all 33 accepted routes.
Streams differ in *presentation and fidelity*, never in what a visitor can learn,
reach, or do. This extends D-036's parity requirement from two paths to four.

**T-03 — A stream-selection rule.** Specify how a stream is chosen from device
capability and connection conditions, including the signals used, thresholds,
precedence, and the fallback when a signal is unavailable. **No such rule exists in
any accepted or draft document today** — this is net-new specification, and it is the
largest single piece of work in this change request.

**T-04 — User override.** A visitor may change stream at any time, and the choice
persists. Automatic selection is a default, never a cage.

**T-05 — Accessibility preference precedence.** An explicit user or platform
preference — `prefers-reduced-motion`, a data-saver signal, an explicit override —
outranks any capability measurement. A capable device whose user asked for less
motion gets less motion.

**T-06 — B07 reclassified.** B07 moves from optional enhancement to a core batch,
with its evidence obligations extended to all four streams.

**T-07 — Stream stability.** Selection resolves once per session and does not
oscillate mid-journey. A stream may only change on explicit user action or an
unrecoverable capability failure.

### 3.2 Exclusions

This change request does **not** authorize:

- any application, UI, or 3D implementation;
- any Blender session, mesh edit, or asset production;
- external Figma or Stitch writes — MA-025 remains the separate gate;
- new routes, new services, altered booking lineage, or altered conversion definition;
- altering the frozen brand identity;
- exact public copy or publication;
- paid or licensed assets;
- dependency, migration, or infrastructure change;
- Git operations or deployment;
- resolution of MA-004's open NoAI question;
- complete Phase 1 acceptance.

## 4. Affected authority, requirements, artifacts, tasks, and risks

| Artifact | Effect |
|---|---|
| `docs/phase-1-ux-architecture/` (D-036) | Journey model changes from optional-3D to four peer streams; parity obligations extend to four |
| `docs/phase-1-ui-reference-design/UI_REFERENCE_DESIGN_CONTRACT.md` (D-037) | §2 optionality wording; the 32 responsive/state/mode profiles gain a stream dimension |
| `design-batch-plan.csv` | B07 reclassified as core; B07 evidence scope widens |
| `responsive-state-mode-matrix.csv` | Stream becomes a new axis alongside viewport, state, and mode |
| `traceability.csv` | New trace rows for T-01…T-07 |
| `foundation-route-coverage.csv` | Each of 33 routes must show stream coverage |
| `HSD-ASSET-001` provenance record | Attribution obligation ATTR-01 must be carried into every stream that renders the model, including a still image in the no-WebGL stream |
| `MANUAL_ACTIONS.md` | New MA for CR-002 approval; MA-004 gains urgency because 3D is now required |
| `RISKS.md` | New risks, see §5 |

## 5. Impact matrix

| Dimension | Impact | Note |
|---|---|---|
| Scope | **Increase** | Three additional first-class streams to specify and evidence |
| Accessibility | **Improvement** | The semantic stream stops being a fallback and gains equal standing |
| Evidence volume | **Increase** | Stream multiplies the existing viewport/state/mode matrix |
| MA-025 / Figma batches | **None today** | B01–B06 and B08 are unaffected; only B07/B09 scope changes, and both are already deferred |
| MA-004 | **Raised severity** | 3D is now required, so an unresolved asset gate blocks a core stream rather than an optional one |
| Schedule | **Increase, unquantified** | See §7 |
| Cost | **None** | No paid service, asset, or licence is implicated |

## 6. Options and tradeoffs

| Option | Description | Assessment |
|---|---|---|
| **A — Approve as written** | Four peer streams with equivalent journeys | Matches founder direction; largest specification effort; strongest accessibility position |
| **B — Two streams** | 3D required, plus semantic; quality varies continuously inside the 3D stream | Less specification and less evidence; loses the explicit low-tier contract, which is where cheap devices actually fail |
| **C — Keep the accepted optional model** | No change | Contradicts explicit founder direction; not recommended |

**Recommendation: Option A**, with the §7 uncertainties resolved during
specification rather than assumed now.

## 7. Estimate, uncertainty, and dependencies

Deliberately unestimated. Three inputs are unverified, and each materially changes
the work. They must be resolved by Context7 and official primary documentation before
any schedule is offered.

**U-01 — Connection signals may not be portable.** The stream rule depends on reading
network conditions in the browser. The relevant API surface is understood to be
unevenly supported across browser engines, which would make connection-based
selection unavailable for a meaningful share of visitors and force a different
strategy — measured load performance rather than declared network class. This is
recorded as `[MUST VERIFY AT SPECIFICATION]` and is **not asserted here**.

**U-02 — Device-capability signals may be equally uneven.** Memory and processor-count
hints are believed to differ by engine. If unavailable, tier selection must fall back
to rendering-capability probes. `[MUST VERIFY AT SPECIFICATION]`

**U-03 — Threshold values are unknown.** What separates high from medium from low
cannot be set from documentation. It requires measurement against the real asset on
real hardware, which is implementation-phase evidence.

### Verification result — 2026-09-06

Verified against MDN Baseline availability banners on each feature's primary page.
Full record: `CR-002-signal-portability-verification.md`.

| ID | Result |
|---|---|
| **U-01** | **RESOLVED UNFAVOURABLY.** Network Information API is *Limited availability*, on a WICG incubation draft. `prefers-reduced-data` is *Limited availability*, Experimental, and warned as "not supported by any user agent". **No portable declared network class exists.** |
| **U-02** | **RESOLVED, SPLIT.** `deviceMemory` is *Limited availability* and coarsened to power-of-two buckets. But `hardwareConcurrency` is **Baseline Widely available since March 2022** (WHATWG HTML), and `prefers-reduced-motion` is **Baseline Widely available since January 2020**. Capability tiering is achievable; memory-based tiering is not. |
| **U-03** | **STILL OPEN**, and reclassified as implementation-phase evidence rather than a documentation gap. Thresholds require measurement of the real asset on real hardware and **cannot close in Phase 1.** |

**Consequence.** The four peer streams survive; the selection rule as written does
not. The substitution this section anticipated — "measured load performance rather
than declared network class" — is now required. Device tiering binds to
`hardwareConcurrency` plus a WebGL capability probe; connection tiering binds to
measured runtime performance; accessibility precedence is unchanged.

**This does not trigger the R-030 stop.** R-030 halts only if portable selection
proves *unachievable*. It is achievable — one input changes mechanism, and that
replacement was named here in advance as the fallback design, so adopting it is
inside the approved change. Target text implying a declared network class is
amended in the revision window.

**The fallback principle now binds harder.** With connection class unavailable in
Firefox and Safari, the missing-signal path is the default for a large share of real
visitors, not an edge case. The conservative choice must be the designed-for case.

**Not obtained, and not asserted:** per-browser minimum versions (BCD tables did not
render), Mozilla and WebKit formal standards positions (retrieval returned 404), and
any evidence that measured-performance selection is itself workable.

**Dependencies:** MA-004 §7 must resolve before any stream that renders the building
model can be produced. The 3D storyboard and asset-specification workstream, today
`not_started`, must run — CR-002 makes it a critical path rather than an optional one.

**Fallback design principle:** because U-01 and U-02 may both resolve unfavourably,
the rule must degrade safely — when a signal is missing, select the stream that is
most likely to succeed, not the most impressive one, and surface the override.

## 8. Validation, review, and acceptance

1. Deterministic validation that all four streams cover all 33 routes, 53 actions,
   and 45 UX tests with no gap.
2. A stream-selection specification with explicit signals, thresholds, precedence,
   missing-signal behaviour, and override.
3. Independent **UX** review of journey equivalence.
4. Independent **accessibility** review that the semantic stream is genuinely
   equivalent and that preference precedence holds.
5. Independent **design** review that the four streams remain one coherent brand.
6. Later Playwright browser evidence per stream — **implementation phase, explicitly
   not part of this change request.**
7. Founder approval.

Revision limit: three, under the UI/motion/3D allowance.

## 9. Rollback and stop conditions

**Rollback:** CR-002 is documentation-only and additive. Reverting means discarding
the CR artifacts; D-036 and D-037 remain the operative accepted baseline because this
request does not edit them.

**Stop conditions:**

- Any attempt to edit D-036 or D-037 artifacts before approval.
- Any implementation, Blender, or asset work.
- Any external Figma write.
- A verified finding that portable stream selection is not achievable — stop and
  return to the founder with Option B rather than inventing an unsupported mechanism.
- Any proposal that gives one stream content, actions, or conversion capability that
  another lacks.

## 10. Approval status and state transition

**Current status: APPROVED — Option A, by the founder on 2026-09-06 at MA-027.**
Recorded as decision **D-039** in `DECISIONS.md` and `docs/decisions-log.md`.

The four peer streams — high, medium, low, and no-WebGL/semantic — carrying
equivalent core journeys with a stream-selection rule, user override, and
accessibility-preference precedence, are now the authorized target state.
Targets `T-01`…`T-07` are authorized.

**REVISION WINDOW EXECUTED 2026-09-06 — decision D-040.** All five items below
are done; see `docs/decisions-log.md` D-040 for the full record. The selection
rule was set by founder decision: WebGL probe as a hard ceiling; reduced-motion
suppresses motion without changing the stream; user override may only simplify and
never exceed the ceiling; `hardwareConcurrency` device tiering; `S-LOW` for an
unsignalled client; one measured promotion, then locked for the session.
**R-032 and R-034 are closed.** The amended package is **not accepted** — founder
re-acceptance is required at **MA-028**, tracked as **R-035**.

The paragraph below records the position at approval and is retained as provenance.

**No accepted artifact has been modified yet.** Approval *opens* the revision
window; it does not perform it. Until that bounded slice completes, D-039 and the
older D-036/D-037 artifacts state contradictory positions on whether 3D is
optional. That divergence is recorded as **R-034** rather than left implicit, and
D-039 governs intent in the interim. Nothing may be implemented from either version
while application work remains blocked, which confines the divergence to
documentation.

The revision window covers, in one bounded slice:

1. D-036 and D-037 accepted artifacts
2. `design-batch-plan.csv` — B07 reclassified from optional to core
3. `docs/active/3D_Mega_Menu_Style_Guide_v2.md` §8.2 — replace degradation framing
   with peer-stream framing
4. `docs/active/Hengshi_Design_SRS_v3.md` `FR-3D-010` — replace "WebGL fallback"
   with the semantic stream as a peer
5. `/credits` reconciled as the 34th route against D-025's accepted 33, per
   **R-032**, appearing in **all four** streams because the CC BY 4.0 obligation
   does not vary by tier

**The uncertainties survive approval.** `U-01`, `U-02`, and `U-03` remain
`[MUST VERIFY AT SPECIFICATION]` against Context7 and official primary
documentation. **No schedule estimate is offered.** Per **R-030**, if portable
stream selection proves unachievable, work stops and Option B returns to the
founder rather than an unsupported mechanism being invented.

Downstream gates are unchanged by this approval. **MA-004** is closed. **MA-025**
is accepted and its `SC-10` still refuses B07 and B09. **MA-026** is still not
preparable, because the 3D storyboard workstream remains `not_started` —
reclassifying B07 as core raises its importance without unblocking it. Application
and 3D implementation remain blocked until complete Phase 1 approval.
