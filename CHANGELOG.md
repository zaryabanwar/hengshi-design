# Changelog

All notable project changes are recorded here. This log distinguishes durable
workflow/documentation changes from application implementation and external
operations.

## [Unreleased]

### 2026-09-24 — R-042 line-ending freeze fragility treated (D-048)

- **`.gitattributes` added** at the root: `text eol=lf` for the design package's
  `*.md`, `*.csv`, `*.ps1` and `*.json` and for `scripts/validation/**/*.ps1`; no
  repository-wide rule. Five package CSVs normalized to their LF blobs with no
  content change; `component-primitives-freeze-hash` re-pinned from
  `EF0DE11B…9C78` (CRLF working copy) to `575D1478…034A` (canonical bytes) with
  provenance; the frozen report's `PASS_COUNT` and two file counts refreshed.
  New design aggregate `631324D0…3EBF`.
- **Validators before the commit:** UX 113/0, foundation PASS, stream tests 987
  checks; design and production each failed only their `git-write-scope` guard
  on the uncommitted root file, which clears at the commit. R-042 `in_progress`
  pending independent verification.

### 2026-09-24 — R-039 amendment applied to the frozen baseline and verified; R-039 closed

- **Applied at `c07e455`:** the fourteen insertions of the accepted amendment
  entered `DESIGN_SYSTEM_IMPLICATIONS.md` verbatim (+178/−7), `INS-01` pins the
  accepted revision (`cf455db`) per review-2 DSB-02, and
  `design-system-freeze-hash` moved from `0E9FC68C…B763` to `1893D026…8B81`
  with provenance comments in the validator. The amendment carries a Revision 3
  row for the DSB-01 heading fix.
- **Independently verified** (`reviews/design-system-amendment-r-039-application-verification.md`):
  PASS, no finding. Validators: design 208/0, production 167/0, UX architecture
  113/0, foundation PASS, stream-mapping tests 987 checks. R-039 `closed`; the
  task row `complete`.
- **Observations recorded, not fixed:** the frozen `validation-report.md` states
  `PASS_COUNT=201` while the validator has returned 208 since before this work
  (only the `COUNTS` line is asserted); and five package CSVs are CRLF or mixed in
  the working tree against LF blobs with `core.autocrlf=true` and no
  `.gitattributes`, so the pinned `component-primitives-freeze-hash` is of
  non-canonical bytes and a fresh checkout would fail it. Logged as **R-042**.
- **Design-system export synced** (`packages/design-system/` and the Design
  System artifact): sixteen `hd-stream-*` tokens (id, profile, evidence token,
  canvas per stream), the scene focus-ring width, the `DeliveryStreamControl`
  component with a static preview, and focus token usages marked [PROPOSED] as
  the amended file records them. Stream labels, the scene ring colour and offset
  stay gated and absent.

### 2026-09-24 — R-039 amendment authored, reviewed twice and accepted (D-047)

- **Amendment authored** under the D-046 contract by an agent independent of the
  D-045 producer (`DESIGN_SYSTEM_AMENDMENT_R-039.md`, `2c469b6`), revised once
  (`cf455db`) after independent review 1 (`740864b`: one MEDIUM, eight LOW
  findings, all resolved), and passed by independent review 2 (`0b7d0a2`: both
  parts PASS, two LOW findings carried to application).
- **Founder decision D-047** accepts revision 2 and authorizes its mechanical
  application to the hash-pinned `DESIGN_SYSTEM_IMPLICATIONS.md`, with the freeze
  hash and aggregate re-pinned and the four validators rerun. Application and its
  independent verification follow in the same session.
- **Nothing else moves.** B01 stays held under G-4; MA-029 undischarged; no Figma
  call; the twelve unresolved gates in the amendment stay open founder decisions.

### 2026-09-24 — R-039 design-system amendment commissioned (D-046)

- **Founder decision D-046** recorded: the design-system gap logged at D-045 gate
  G-6 (no stream axis, no stream-control component, no four `DS-S-*` stream
  tokens, no 3D focus-ring token) is commissioned as its own bounded specialist
  contract, executed in the Claude Code session. R-039 moves to `in_progress` in
  `RISKS.md`; a task row is added in `TASKS.md`.
- **Nothing else moves.** `DESIGN_SYSTEM_IMPLICATIONS.md` and its freeze hash are
  untouched until a separate acceptance decision; B01 stays held under G-4;
  no Figma call was made (a `whoami` capability test was offered and declined).

### 2026-09-24 — Design system export committed (derived, non-authoritative)

- **`packages/design-system/` added:** tokens, brand book, guideline sections,
  CSS component layer with static previews, and byte-identical copies of the
  Framework Relay logo and specimen SVGs, extracted at `989af66` from the Phase 1
  identity package and mirrored from the Design System artifact
  (`PACKAGE.md` records provenance and status).
- **No frozen file changed.** `DESIGN_SYSTEM_IMPLICATIONS.md` and
  `semantic-tokens.json` are untouched; the export uses their reserved `--hd-*`
  code names. The semantic aliases in `tokens.json` are **[PROPOSED]** and carry
  no accepted authority.
- **R-039 stays open.** The export does not add the stream axis, stream-control
  component, `DS-S-*` stream tokens, or 3D focus-ring token; it is input to that
  contract, not the amendment. B01 hold, MA-029, and the CB-06/CB-07 per-call
  Figma rule are unaffected. Local commit only; nothing pushed.

### 2026-09-06 — Fourth FAIL round; who defines the model changes (D-044)

- **Both independent re-reviews of the D-043 remediation returned FAIL.** Four FAIL
  rounds have now followed deterministic validator runs of 183, 184, 185, and 189
  passing assertions. Records: `reviews/design-review-iteration-5.md`,
  `accessibility/accessibility-audit-iteration-4.md`.
- **The central defect, found by both:** `stream_profile` was populated as a **total
  function of `state_profile`**. The column was derivable, encoded no independent
  judgement, and no human decided any of its 163 values. All 34 routes took
  `DS-STREAM-INVARIANT` and structurally could not do otherwise. The validator
  enforced the wrong answer — a producer correctly assigning all four `DS-S-*` to
  `ROUTE-BOOK` would have **failed** `delivery-stream-assignment`.
- **The decisive proof:** all 19 route templates depend on `PRIM-001`, which the
  package itself calls "the shell that hosts the delivery stream control" and which
  carries four `stream_*` variants. `DS-STREAM-INVARIANT`'s own `exception_rule`
  forbids that dependency. The rule prohibited the assignment the producer made, on
  every route.
- **Also blocking, found by both:** the **production package has no stream axis at
  all**. `EC-08`'s evidence-ID grammar has no stream token, so two frames of one
  template in `S-HIGH` and `S-SEMANTIC` cannot be given distinct IDs and `EC-30`
  would read the second as an illegal overwrite. Per-stream evidence obligations in
  the design package are meaningless while the production package cannot name a
  per-stream frame.
- **`delivery-stream-record-coverage` asserted `Count -eq 44`** — a row count, inside
  the assertion written to fix the row-count defect. D-042 counted profile rows;
  D-043 counted records pointing at those rows. Same pattern, one level up.
- **R-034 reopened — closed prematurely for the second time on the identical defect
  class.** The string it was recorded closed against survives in the production
  package's `batch-production-plan.csv` B07, and `MODE_NON_WEBGL_QUICK_ACCESS`
  survives in a `baseline_frame_name` where underscores evade a guard written for
  hyphens. Both the producer's sweep and the widened guard were scoped to the design
  package. A third closure requires independent verification, not a producer sweep.
- **Founder decision D-044 — the approach changed, not just the artifacts.** The root
  cause accepted: the producer invented the model, encoded it, wrote the assertion
  that checked it, and certified the result. A validator the producer writes cannot
  catch a model the producer got wrong. The two independent reviewers now author the
  model as **[PROPOSED]** specifications; the producer implements to them; the
  reviewers verify. The production stream axis is fixed in the **same slice**.
- **Not closed:** **MA-029 is not discharged.** **R-035** open, **R-034** reopened,
  **R-036** open. **B01 remains held.** Zero Figma allowance consumed; nothing
  staged, nothing committed, no external write.
- Confirmed genuinely closed by both reviewers: `S-MEDIUM` now has real
  representation, and no current conformance is claimed anywhere in the package.

### 2026-09-06 — Third FAIL round; the stream axis made load-bearing (D-043)

- **Both independent re-reviews of the D-042 remediation returned FAIL**, and they
  converged on five identical defects. That is three FAIL rounds against validator
  runs of 183, 184, and 185 passing assertions. Recorded as the standing lesson:
  **a passing validator is a determinism check, not a review.**
- **The stream axis was inert.** D-042 added four `DS-S-*` profiles to the matrix,
  and the validator asserted they existed — by counting rows. No route, flow, or
  template selected one, so a producer could satisfy every cell and produce no
  per-stream evidence. Named by the design reviewer as *assertions that pass by
  counting rows rather than resolving references*.
- **Full schema fix (founder decision).** `stream_profile` added to
  `foundation-route-coverage.csv`, `foundation-flow-coverage.csv`, and
  `reference-template-inventory.csv`, non-empty on every row. 36 flows and 8
  templates select all four `DS-S-*`. New profile `DS-STREAM-INVARIANT` is a
  positive claim that a record renders identically in all four streams — **not** an
  exemption; `S-SEMANTIC` is discharged there, never waived.
- **The axis was made load-bearing, not just present.** `ACT-09` moved from
  deferred `B07` into authorized `B01`, so the delivery stream control is evidenced
  on a batch that will actually run rather than on one held at MA-026.
- **`COV-ACT-08` and `COV-ACT-09` fixed** in the design package and mirrored into
  `STATES_AND_RECOVERY.md`: "quality downgrade" removed (no failure promotes or
  demotes a stream mid-session), and "Toggle quality" re-homed as "Select delivery
  stream" under `SP-NAVIGATION`, out of the World HUD it could not live in.
- **The frozen validation report described a different package** than the validator
  asserted (routes=33 profiles=32 vs 34 and 36). Rewritten, and a new assertion
  `validation-report-counts-agreement` now requires literal agreement with the
  counts computed in the same run, so it cannot drift silently again.
- **WCAG 2.2 3.2.2 claim withdrawn** from the style guide; replaced with an advance
  advisement requirement. §8.2.4 gains the specification neither reviewer had a
  home for: crossing the `S-SEMANTIC` boundary — where focus lands when the operated
  control's subtree is destroyed, bidirectional location↔route mapping, and
  accessibility-tree ordering during the swap. Step 4 storage specified; the
  undefined "never below what the visitor has already been shown" clause deleted.
- **SRS §5.6 Accessibility Requirements added** (`NFR-A11Y-001`…`007`). The SRS
  previously held zero accessibility entries, so the WCAG 2.2 AA target had no
  requirement-level home.
- **Production contract §0.1 corrected.** "Where this contract and the D-037 package
  differ, the D-037 package governs" would have directed a producer to resolve
  conflicts back to a superseded freeze and drop `/credits`. The **current
  aggregate** now governs; superseded hashes are provenance, not authority.
- **R-034 correction.** The D-042 note claimed the `FALLBACK` identifier rename
  "cascades into the foundation and UX packages". It does not — all 47 occurrences
  were in the design package plus history documents. The rename is done.
- **Not closed:** **R-035 stays open** — this remediation is the producer's own and
  Constitution §VII forbids self-approval; a third independent re-review is
  required (**MA-029**). **R-036** open. `U-03` deferred to implementation-phase
  measurement.
- All four validators pass: foundation PASS, UX PASS (113), design PASS (189),
  production PASS (153). Design freeze
  `DB92B4D0B889948D6C272F0DC7397327055B0108E7EEB953924F34E735BD4649`.
- **B01 is held** by explicit founder decision until a clean re-review. Zero Figma
  allowance consumed; nothing staged, nothing committed, no external write.

### 2026-09-06 — Independent reviews ran and both failed; blocking findings corrected (D-042)

- **Both reviews returned FAIL.** The independent design review and accessibility
  audit MA-028 required were run after acceptance, not before. Records:
  `reviews/design-review-iteration-4.md`,
  `accessibility/accessibility-audit-iteration-3.md`.
- **Same root cause, found independently:** the amendment changed the prose and not
  the data. The four stream IDs appeared exactly once in the whole design package,
  and `S-MEDIUM` had no representation anywhere.
- **Four blocking findings addressed; two of the four were not actually closed.**
  *(Corrected 2026-09-06 under D-043 — see the D-043 entry above. "All corrected"
  was an overstatement. The `DS-S-*` profiles were added to the matrix but no
  record selected them, so the stream axis was inert; and the 3.2.2 claim below is
  withdrawn. The original wording is kept so the overstatement is visible.)*
  The stream control now exists in
  `PRIM-001` so it is reachable in `S-SEMANTIC`; `S-LOW` retains every hotspot and
  destination; four `DS-S-*` profiles make the stream a real evidence dimension with
  per-stream contrast, focus order, and target size; §8.2.2 is reordered so the
  override is evaluated last, is reversible, persists, and outranks stored
  measurement.
- **The mid-session promotion is removed.** Measurement is stored and applied from
  the next visit. The stream resolves once before first paint and changes only when
  the visitor asks. ~~WCAG 3.2.2 satisfied by construction.~~ **Withdrawn
  2026-09-06 under D-043:** 3.2.2 governs changing the setting of a UI component,
  and the stream control *is* such a component, so removing automatic promotion does
  not satisfy it. A polite announcement after the fact is 4.1.3 treatment. §8.2.4
  now requires **advance advisement** instead, and claims no conformance at all.
  New §8.2.4 governs that one transition: polite status message, focus not moved,
  scroll/panel/route preserved.
- **Accessibility corrections beyond the blocking set:** hotspot states gain a
  normative keyboard-focus row and a non-colour, non-motion cue; §7.3 enumerates
  motion suppression exhaustively; `/credits` gains list semantics, per-entry
  `lang`, in-context link purpose, and a return path.
- **Production contract §0.1 corrected for D-041.** Authorized batches may now rely
  on the amendment. B07 stays deferred to MA-026 by founder choice.
- **Not closed:** R-035 stays open (remediation unreviewed, **MA-029** opened);
  **R-034 reopened** (ladder identifiers survive upstream); **R-036 opened**
  (`S-SEMANTIC` P0 written but not discharged while B07 is deferred).
- New freezes: design `4B9EB9AF...289B`, production `9B4CDE04...CA11`. All four
  validators pass. `U-03` remains open. No schedule offered.


### 2026-09-06 — MA-028 accepted (D-041); amended package carries authority, review gap stated

- **MA-028 approved by the founder.** The amended D-025/D-036/D-037 artifacts now
  carry accepted authority. Accepted freeze values: design
  `F16093D0...4AD6`, production `3DF0DBB6...8528`. The production contract no
  longer falls back to the D-037-accepted package.
- **Stated, not glossed:** the fresh independent design and accessibility reviews
  this gate also required **did not run**. Four passing validators are determinism
  checks, not reviews. **R-035 stays open as `accepted_by_founder`** with its
  original exit evidence intact — a clean independent design review and a clean
  independent accessibility review of the amended package.
- Superseded hashes retained as provenance; the amendment remains reversible.
  `U-03` remains open. No schedule offered.


### 2026-09-06 — CR-002 revision window executed; four peer streams are now the written model

- **Stream-selection precedence decided by the founder (D-040).** Evaluated in
  order, each step only narrowing what follows: the WebGL probe is a hard ceiling;
  `prefers-reduced-motion` suppresses motion without changing the stream; a user
  override may only select a *simpler* stream and never exceed the ceiling;
  `navigator.hardwareConcurrency` tiers the device; an unsignalled client defaults
  to `S-LOW`; measured performance may promote **once**, then the stream is locked
  for the session. The rule never promises more than the client has demonstrated,
  and never takes back something already shown.
- **`3D_Mega_Menu_Style_Guide_v2.md` §8.2** is no longer "Performance Adaptations"
  ending in a fallback. It is "Delivery Streams" — four peers carrying equivalent
  core journeys, plus the verified-signal table and the precedence above.
- **SRS `FR-3D-010`** restated as the `S-SEMANTIC` peer stream and raised **P2 to
  P0**; `FR-3D-011` (four peer streams) and `FR-3D-012` (selection precedence)
  added. The unusable network signals are explicitly banned from any implementation.
- **`design-batch-plan.csv` B07** reclassified from "Optional World HUD and Quick
  Access parity" to "Core delivery-stream World HUD and semantic peer parity", with
  required evidence for all four streams and every step of the precedence rule.
- **15 residual degradation framings removed** across seven design-package
  artifacts, and the column `optional_immersive_representation` renamed
  `immersive_stream_representation` in both CSVs and both validators.
- **`/credits` reconciled as the 34th route (R-032 closed).** `ROUTE-CREDITS` added
  to the D-025 canonical inventory, the D-036 UX parity CSV, and the D-037 coverage
  CSV; `TR-ROUTE-034` added; B02 takes primary ownership; `PRIM-001` now requires a
  footer attribution link. Route counts moved 33 to 34 in three validators.
- **R-034 closed** on exactly its stated exit evidence. D-039 and the accepted
  artifacts no longer contradict each other.

### 2026-09-06 — Two latent validator defects surfaced and repaired

- **`git-write-scope` was the R-024 error a second time.** It asserted that nothing
  outside the design package had changed — true only during that package's authoring
  window, and necessarily false once an approved change request reaches across
  packages. It now derives an explicit `PACKAGE_AUTHORING` / `CR002_REVISION_WINDOW`
  state from whether D-039 is approved, with an enumerated allowlist rather than a
  blanket exemption, so it still fails on genuinely unrelated writes.
- **The foundation validator aborted before printing any result.** It merged git's
  stderr with `2>&1`; because this repository stores CRLF blobs under
  `core.autocrlf=true`, git's benign "LF will be replaced by CRLF" warning surfaced
  as a terminating `NativeCommandError` on any modified file. It now discards git's
  stderr and reads the exit code.
- **New standing assertion `semantic-stream-peer-framing`** fails the design
  validator if optional or fallback framing for the semantic stream returns.

### 2026-09-06 — The amended package is NOT accepted (MA-028, R-035)

- Four passing validators are determinism checks, **not reviews**. Constitution
  principle VII forbids the producer approving its own material output, and no
  independent design or accessibility review has run against the amended artifacts.
- The D-037 aggregate moved `97E79201...120F` to `F16093D0...4AD6`, and the
  production aggregate `E3786F14...C08D` to `3DF0DBB6...8528`. Every superseded value
  is **retained** in `producer-inspection.md`, the production contract, and the
  design validator rather than overwritten, so the amendment is reversible.
- Dated artifacts under `reviews/` and `accessibility/` were deliberately not
  rewritten; they are evidence of what was inspected, not claims about the package now.
- Until MA-028 is accepted, the production contract keeps deriving authority from the
  D-037-accepted package and no production batch may rely on an amendment-only change.
- **Thresholds remain `U-03`**, unresolvable in Phase 1. **No schedule is offered.**
  Application and 3D implementation remain blocked. Zero Figma allowance consumed.

### 2026-09-06 — CR-002 signal portability verified; the selection rule must change

- **U-01 resolved unfavourably.** The Network Information API
  (`navigator.connection`, `effectiveType`, `saveData`) is MDN Baseline **Limited
  availability**, on a WICG incubation draft. Its CSS alternative
  `prefers-reduced-data` is Limited availability, Experimental, and warned as *"not
  supported by any user agent"*. **No portable declared network class exists.**
- **U-02 resolved with a split.** `navigator.deviceMemory` is likewise outside
  Baseline and coarsened to power-of-two buckets. But `hardwareConcurrency` is
  **Baseline widely available since March 2022** (WHATWG HTML) and
  `prefers-reduced-motion` since **January 2020**. Capability tiering and
  accessibility precedence stand on firm ground; memory-based tiering does not.
- **U-03 stays open** and is reclassified as implementation-phase measurement
  rather than a documentation gap. Thresholds need the real asset on real hardware
  and **cannot close in Phase 1**. No schedule may be offered.
- **The four peer streams survive; the selection rule as written does not.** Device
  tiering binds to `hardwareConcurrency` plus a WebGL capability probe; connection
  tiering binds to measured runtime performance.
- **The R-030 stop was not triggered.** It halts only if portable selection is
  *unachievable*; it is achievable once one input changes mechanism, and CR-002 §7
  named that exact replacement in advance as its fallback design — so this is
  inside the approved change, not an invented mechanism.
- **The fallback principle now binds harder.** With connection class unavailable in
  Firefox and Safari, the missing-signal path is the default for a large share of
  visitors, not an edge case.
- **Recorded as not obtained, not verified:** per-browser minimum versions (MDN's
  compat tables did not render), Mozilla and WebKit formal standards positions
  (retrieval returned 404), and any evidence that measured-performance selection is
  itself workable.
- R-030 marked realized and treated. New record at
  `docs/requirements/CR-002-signal-portability-verification.md`.

### 2026-09-06 — MA-025 and MA-027 accepted; Figma capability-tested; SC-05 fired and resolved

- **MA-025 approved (D-038).** Batches B01–B06 and B08 are authorized for external
  Figma reference production at freeze SHA-256
  `E3786F14C9F12CBF8127A18E7959881B91A9ECC5DC11BBE3E466BCEC6C7EC08D`. B07, B09,
  `docs/ui/UI_SPEC.md`, and the final visual direction remain deferred to MA-026.
- **MA-027 approved as Option A (D-039).** Four **peer** delivery streams — high,
  medium, low, and no-WebGL/semantic — with equivalent core journeys, a
  stream-selection rule, user override, and accessibility-preference precedence.
  3D is no longer an optional enhancement and the semantic stream is no longer a
  fallback. B07 is reclassified from optional to **core** but stays deferred,
  because the 3D storyboard workstream is still `not_started`.
- **Figma reached Capability-tested.** Registered at user scope, authenticated by
  the founder, bound into a restarted session, and verified with `whoami` — a Full
  seat on the `starter` tier. The tool is read-only and documented as exempt from
  rate limits, so the test consumed no allowance. No credential was seen,
  requested, or recorded. Canvas writing is **not** capability-tested.
- **One of the five §7.2 limits verified, and it blocks: 20 MCP tool calls per
  calendar month.** The Starter column spans both seat rows, so a Full seat does
  not receive the 200/day allowance. The contracted floor — `EC-25` inventory plus
  `EC-28`/`EC-29` archives, three calls per batch across seven batches — is **21
  calls**, exceeding a month before any visual evidence; realistic demand is in the
  hundreds. **`SC-05` fired at programme scope.** The producer halted, reported the
  exact shortfall, and made no purchase. The other four limits remain unverified
  and unasserted.
- **`SC-05` resolved, not waived.** Shown the verified limit, the founder directed
  staying on the free tier and rationing precisely. The accepted consequence is
  recorded plainly: the programme spans multiple calendar months and **no schedule
  may be stated** until B01 measures real consumption.
- **Rationing became an instrument.** Added
  `validation/mcp-call-budget.csv` (`CB-01`–`CB-15`) and
  `validation/mcp-call-ledger.csv`. `CB-02` records that write-tool exemption is
  **NOT ASSERTED**, because the provider's general claim does not agree in scope
  with its list of only three exempt tools. `CB-11`/`CB-12` forbid restoring
  allowance by purchase, second account, second seat, or trial.
- **`CB-06` decided by the founder:** all 20 monthly calls are spendable with
  **zero reserve**, and **every individual call requires explicit approval
  immediately before it is made**. `CB-07` binds the producer never to call
  unprompted and to state tool, purpose, and running count each time. Per-call
  approval makes a standing reserve redundant. B01 is unblocked.
- **Tension recorded, not resolved.** The founder also stated the project does not
  have a month and is developing fast. No allocation rule makes 20 calls per month
  deliver seven batches quickly. The paths that would remove the constraint — a
  paid envelope under MA-010, or producing references outside the Figma MCP — are
  unchosen, and the producer may start neither.
- **B01 gains a second purpose at no extra cost:** it is now the metering
  experiment as well as the gated pilot.
- **Validator boundary assertions superseded, not deleted.** It now derives an
  explicit `PRE_APPROVAL`/`POST_APPROVAL` state from the gate's ledger status —
  the R-024 lesson — and post-approval requires the capability evidence, budget,
  and ledger it previously forbade.
- **Risks:** R-025 closed; R-026 marked partly realized and treated, with the
  control judged to have worked because the limit surfaced *before* the first
  write; R-033 added for multi-month duration and mid-batch exhaustion; **R-034
  added** for the live contradiction between D-039 and the still-unedited
  D-036/D-037 artifacts.
- **No external write, no evidence directory, no commit, no purchase.**

### 2026-09-06 — Figma authenticated at host level; pricing check retired

- **The founder authenticated the Figma MCP server.** `claude mcp get figma` now
  reports `✔ Connected`. No token, session URL, or account identity was seen,
  requested, or recorded by the producer, and none appears in any repository file.
- **Session exposure is not yet established.** MCP tools bind to a session at
  start-up, and this session predates the server, so no Figma tool is callable from
  it — a tool search for Figma design tools returns no match. The server is
  authenticated at host level and not yet exposed at session level. Claude Code
  must be restarted and the tools **observed**, not assumed, before connectivity is
  claimed or `capability-evidence.md` is written.
- **R-031 re-scoped and the recurring pricing check retired**, on founder direction
  that the account is on a free plan and no such check should be performed. This is
  accepted: a free plan with no payment method cannot be charged silently, so the
  zero-spend boundary is protected by the account rather than by a check. The
  residual exposure is **loss of capability, not unexpected spend** — if canvas
  writing moves behind a paywall, batches stop working — and it needs no scheduled
  check because it announces itself when a write fails or prompts to upgrade.
  Treatment is now reactive: SC-04 halts on any paid prompt, a blocked write halts
  the batch and routes to MA-010, and no purchase may be made to unblock it.

### 2026-09-06 — MA-004 closed; Figma MCP registered pending authentication

- **MA-004 closed as accepted.** The founder adopted the **narrow NoAI reading** —
  the asset is never submitted to a model as training, fine-tuning, or generative
  input; permitted work is deterministic Blender operations under founder
  direction. Geometry reuse is authorized subject to four binding operating rules
  recorded as AR-01 through AR-04, with AR-04 requiring a stop and return to the
  founder rather than reinterpretation.
- **Attribution surface decided.** A footer "Asset Credits" link to a durable
  credits page, no prominent homepage placement required. **`/credits` selected**
  over `/legal/asset-credits` because the accepted inventory has no `/legal/*`
  family and the alternative would introduce an empty parent segment for a single
  leaf. The exact CC BY 4.0 attribution text is recorded in `HSD-ASSET-001` §6a.
- **Two obligations recorded as open rather than treated as done.** ATTR-03, the
  absent GLB `asset.copyright` field, is an asset modification deferred to
  authorized 3D production. `/credits` is a **34th route** against D-025's accepted
  33; its reconciliation into the route inventory, UX wayfinding, route-coverage
  CSV, and footer primitive is assigned to the CR-002 revision window rather than a
  third concurrent change request. Tracked as **R-032**.
- **Figma MCP registered** at `https://mcp.figma.com/mcp`, endpoint verified against
  Figma's official Dev Mode MCP guide. Registered at **user scope** so no endpoint
  or credential configuration enters the repository; `.mcp.json` remains absent.
  `claude mcp get figma` reports `Needs authentication`. **Authentication was not
  attempted** — it is a credential action and a founder gate.
- **Plan gate cleared, pricing caveat opened.** The remote server is documented as
  "available on all seats and plans", so a free seat suffices. However canvas
  writing — the exact capability every MA-025 batch depends on — is free only
  during beta and is documented to become "a usage-based paid feature". The MA-025
  zero-spend boundary is therefore **time-limited, not permanent**; pricing must be
  re-checked before each batch rather than once at the gate. Tracked as **R-031**.
- Recorded outside the frozen package so the approved freeze hash `E3786F14…C08D`
  stays valid and citable.

### 2026-09-06 — 3D asset provenance verified and four-stream change request opened

- Verified the HQ exterior model's provenance from the founder-supplied Sketchfab
  source page, read-only, and recorded it as `HSD-ASSET-001` in
  `docs/phase-1-3d/asset-provenance/`. Author `99.Miles`; licence **CC BY 4.0**,
  confirmed against the canonical Creative Commons deed: commercial use and
  modification **permitted**, attribution **required**.
- Corroborated asset identity **without downloading the source**: the repository
  file reports 37,302 triangles against the page's stated 37.3k. The vertex
  divergence is the expected glTF seam-splitting artefact, not a mismatch. Recorded
  SHA-256 `4767CAB4…6AAFE`, identical across the `public/` and `dist/` copies.
- Established that the file is **already a derivative** — generator string
  `Khronos glTF Blender I/O v5.0.21` — so CC BY's "indicate if changes were made"
  obligation attaches today, before any surroundings work.
- Narrowed **MA-004** from `blocked` to `awaiting_human`. The provenance, rights,
  attribution, modification, and security evidence it required is supplied; one
  founder decision remains on the source page's **NoAI notice**, which is material
  because the planned surroundings method is Blender driven by an AI agent.
- Opened **R-028** (NoAI conflict), **R-029** (CC BY attribution has no home in the
  33 accepted routes), and **R-030** (browser support for stream-selection signals
  is unverified).
- Opened **CR-002** at `docs/requirements/CHANGE_REQUEST_CR-002.md` after the
  founder stated that 3D is not optional. It proposes four peer delivery streams —
  high, medium, low, and no-WebGL/semantic — selected by device capability and
  connection, carrying equivalent core journeys across all 33 routes, plus a
  net-new selection rule, user override, and accessibility-preference precedence.
  B07 would be reclassified from optional enhancement to core.
- Opened **MA-027** as the founder gate for CR-002. **No accepted artifact was
  edited**: D-036 and D-037 remain the operative baseline until CR-002 is decided.
- Corrected a scope defect in the MA-025 validator. Its worktree check assumed it
  was the only authorized slice in flight and failed once CR-002 and the provenance
  record appeared — the same defect class previously diagnosed in the D-037
  validator, one level up. The allowed set is now the documentation tree plus the
  durable root records, and the load-bearing application/dependency/migration
  assertion is evaluated over every changed path rather than only rejected ones.
  **The 9-file freeze hash is unchanged** at `E3786F14…C08D`, because the validator
  and its report sit outside the freeze set by design.
- No download, Blender session, mesh edit, external Figma or Stitch operation,
  commit, push, or deployment was performed.

### 2026-09-06 — External UI reference-production contract prepared

- Produced a documentation-only external reference-production contract under
  `docs/phase-1-ui-reference-production/`: a README, the normative contract, five
  CSVs, a deterministic PowerShell validator, a validation report, and a producer
  inspection. The nine freeze files hash to SHA-256
  `E3786F14C9F12CBF8127A18E7959881B91A9ECC5DC11BBE3E466BCEC6C7EC08D`.
- Deterministic validation passes **147/147** with zero failures, including 37
  cross-artifact assertions that carry each batch's prerequisites, time-limit
  branch, and browser profile verbatim from the accepted `design-batch-plan.csv`.
- Selected **Figma** as the single provider and placed Stitch out of scope, with
  the rationale recorded per requirement in `provider-evaluation.csv`.
- Recorded that only **seven of nine batches are authorizable**. B07 requires an
  approved 3D storyboard and asset specification, whose workstream is
  `not_started` and whose MA-004 gate is blocked; B09 hard-requires B07. The
  D-037 §15 handoff and `docs/ui/UI_SPEC.md` are therefore deferred to a later
  MA-026 rather than promised under MA-025.
- Recorded a verified **host access gap**: no Figma or Stitch MCP, plugin, or API
  path is configured or exposed on this host, and the canonical MCP inventory
  named by `AGENTS.md` does not exist. Corrected the two superseded rows in
  `docs/software-definition/02-ai-dev-tooling-and-mcp.md` and made one of two
  enablement paths a precondition of the first external write.
- Held a **zero-spend boundary** and recorded five Figma free-tier limits as
  unverified rather than asserting them, because the pricing page rendered its
  comparison grid without attributable plan columns on 2026-09-06.
- Opened risks R-025, R-026, and R-027; moved the UI reference-design slice in
  `PROJECT_STATE.yaml` from `awaiting_human` to `accepted` to match D-037.
- **No external Figma or Stitch operation of any kind was performed or
  attempted**, no independent review has run, the producer has not approved its
  own package, and no D-038 decision entry has been created because the founder
  has not yet decided MA-025.

### 2026-09-05 — UI reference-design contract accepted

- Recorded the founder's explicit approval as D-037 and closed MA-024 for the
  exact 13-file producer freeze at SHA-256
  `97E79201CC36F01718A027AD800E63BDD5AAFC47E41137D65253BAABA6B2120F`.
- Opened MA-025 as the separate founder gate for a bounded external Figma/Stitch
  reference-production contract. External writes and implementation remain
  unauthorized.

### 2026-09-05 — Repository-state ambiguity reconciled

- Corrected the Phase 0 commit fact in `PROJECT_STATE.yaml` and recorded commit
  `d96ce616350c02667a020bde99edd8ec3e7159d0` as evidence that repository history
  exists.
- Clarified that the 2026-07-18 working-tree counts are a preserved historical
  pre-Phase-0 snapshot, not an assertion about the current working tree.
- Kept MA-024 at `awaiting_human`; this factual reconciliation does not accept the
  UI reference-design contract or authorize visual production or implementation.

### 2026-09-03 — UI reference-design contract ready for founder acceptance

- Produced the documentation-only UI reference-design contract under
  `docs/phase-1-ui-reference-design/` without creating a visual screen, changing
  application code, or making an external Figma/Stitch write.
- Covered 33 routes, nine exclusions, 15 wayfinding records, 53 actions, 45 UX
  tests, 40 reusable templates, 32 responsive/state/accessibility profiles, 62
  primitives, and nine dependency-ordered future design batches.
- Closed six design-contract findings and three accessibility-contract findings
  across the allowed three producer revisions. Final validation passes 183/183;
  final independent design and accessibility reviews both PASS with zero findings.
- Froze the 13 producer files at SHA-256
  `97E79201CC36F01718A027AD800E63BDD5AAFC47E41137D65253BAABA6B2120F`
  and opened MA-024 for definition-only founder acceptance or bounded change
  request. No D-037 decision has been created because approval is still pending.
- Reconciled stale mutable brand-identity state to its existing D-035 acceptance.
  MA-013, external visual-production authority, final visual direction, complete
  Phase 1 acceptance, implementation, publication, Git operations, deployment,
  and launch remain separate gates.

### 2026-07-20 — UX architecture accepted

- Recorded the founder's explicit `approved whats next? provide list of all phases
  with complete and remaining` response at MA-023 as D-036.
- Closed MA-023 and accepted the exact UX architecture package at SHA-256
  `35E0EA46C1099BA271521EF55AFF3E3F83B76FF2E13C7E94387D76757FFC89D3`
  without changing its artifacts or review evidence.
- Kept the combined UX/UI workstream in progress because UI reference designs do
  not exist. Identified UI reference-design contract and foundation-surface
  coverage planning as the next recommended bounded Phase 1 slice, but did not
  open UI production or authorize an external Figma/Stitch write.
- Compatibility MA-013, complete Phase 1 acceptance, implementation, publication,
  paid actions, Git operations, deployment, and launch remain separate gates.

### 2026-07-20 — UX architecture ready for founder acceptance

- Completed the bounded Phase 1 UX architecture under
  `docs/phase-1-ux-architecture/` after three producer iterations.
- Final deterministic validation passes 113/113 across 33 routes, nine exclusions,
  15 wayfinding entries, 53 action contracts, 45 UX tests, and 123 traceability
  rows; final producer package SHA-256 is
  `35E0EA46C1099BA271521EF55AFF3E3F83B76FF2E13C7E94387D76757FFC89D3`.
- Final independent design and accessibility iteration-3 reports both PASS with
  CRITICAL 0 / HIGH 0 / MEDIUM 0 / LOW 0. Earlier review findings remain preserved
  in their iteration reports.
- Opened MA-023 for 👍 accept or 🔁 revise of the exact UX definition. This does
  not authorize UI/design production, external Figma/Stitch writes, application or
  3D implementation, publication, Git actions, deployment, complete Phase 1
  acceptance, or launch. Compatibility MA-013 remains separate.

### 2026-07-20 — Frozen brand identity accepted

- Recorded the founder's explicit `approved.` response at MA-015 as D-035,
  accepting the exact frozen Signal Ledger system + Framework Relay logo hybrid.
- Closed MA-015 and CR-001 as accepted; set both the Phase 1 brand/identity
  workstream and bounded identity slice to accepted without changing identity
  artifacts.
- Opened UX/UI accessible-journey definition as the next Phase 1 workstream.
  Compatibility MA-013 remains separately awaiting human review; the marks remain
  unregistered/trademark-not-cleared, and no implementation, publication,
  external, Git, paid-asset, deployment, complete Phase 1, or launch authority was
  granted.

### 2026-07-20 — Brand identity verified and MA-015 reopened

- Completed D-034 with final deterministic validation 63/63 and a clean nine-state
  browser/a11y report: zero violations, incomplete results, external requests,
  console errors, page errors, or temporary residue.
- Refreshed only five directly invalidated captures, rebuilt the 29-record
  manifest/report/inspection, and preserved protected 6/31/24 plus logo/geometry
  integrity with zero mismatch.
- Independent design and accessibility verification both PASS with CRITICAL 0,
  HIGH 0, MEDIUM 0, and LOW 0 after one report-format-only correction each.
- Reopened MA-015 for the exact Signal Ledger system + Framework Relay logo hybrid:
  👍 approve or 🔁 revise. No production, trademark, publication, application,
  external, Git, or deployment authority is inferred.

### 2026-07-20 — Identity completion authority recorded

- Recorded the founder's 🧩 choice and “just complete this now all” directive as
  D-034, closing MA-022 without approving the identity.
- Superseded prior one-run/no-retry limits only for non-material internal validator,
  harness, and evidence reconciliation inside the existing D-033 contrast scope.
  Structured pre/post-state corrections and reruns may proceed as needed.
- Authorized only minimum remaining dependency-key/print contrast corrections,
  clean evidence rebuild/freeze, and separate independent design/accessibility
  verification. Identity redesign, application/UI code, external/production/Git
  actions, and final identity approval remain excluded.

### 2026-07-20 — D-033 stopped on validator-state drift

- Created and verified the pre-edit D-033 checkpoint at SHA-256
  `58A1823E3261440CE4B51969F0C95FA7A63A6EC9D8EA6D1503951A89520BE0D0`,
  preserving six reviews, 31 archive files, 24 forbidden authority files, current
  logo/geometry anchors, report `FC34146…128B`, and zero temporary residue.
- Applied the one authorized CSS-only source change set (`595B798…7CE2`) for the
  dependency-key background and print eyebrow specificity. The sole validator
  exited 1 with 56 PASS / 3 FAIL; browser invocation count remained zero.
- Classified all three failures as validator-state reconciliation defects, not an
  identity contrast verdict: unexpected authorized report state, exact old CSS
  literal, and superseded failed-report hash/signature. No edit/retry, evidence
  refresh/freeze, or independent review followed.
- Opened MA-022 for one consolidated three-assertion reconciliation against the
  D-033 checkpoint/CSS/report state or stop unresolved. MA-015 remains blocked.

### 2026-07-20 — Final contrast-only correction authorized

- Recorded the founder's 🎨 choice as D-033 and closed MA-021. This authorizes
  only `.dependency-key` contrast in four narrow/failure states and the print
  contrast violation across three nodes; it is not identity approval.
- Required a pre-edit checkpoint of the surviving browser report, all protected
  reports/archive/authority files, manifest/checkpoint/current-logo/geometry
  hashes, and exact mutable paths.
- Reopened one source change set, one deterministic validator, one browser/a11y
  pass, directly invalidated evidence freeze, and separate independent design and
  accessibility verification. Either test failure stops without edit/retry;
  application code, Git, external writes, and MA-015 remain blocked.

### 2026-07-20 — D-032 exhausted on contrast-only browser evidence

- Reconciled the interrupted D-032 run from surviving evidence: its sole
  deterministic validator completed with 59 PASS / 0 FAIL, then the authorized
  browser/a11y pass completed once and stopped without retry.
- The browser report (`FC34146CB3C457AA70270B7A2B71BCBDE120292A4A4236FF3CC136C03502128B`)
  records one serious print color-contrast violation across three nodes and four
  serious `.dependency-key` color-contrast incomplete results in the 390, 320,
  text-spacing, and asset-failure states. External requests, console errors, and
  page errors were zero; the temporary profile was removed.
- Confirmed all four original D-029 failure classes closed and protected integrity
  remained exact across six reports, 31 archive files, and 24 forbidden authority
  files. No evidence refresh/freeze or independent verification followed the
  non-pass.
- Opened MA-021 for a founder choice between one final contrast-only evidence
  correction and stopping unresolved. MA-015 remains blocked; this is not identity
  approval or implementation authority.

### 2026-07-20 — Two assertion-literal corrections authorized

- Recorded the founder's 🧰 choice as D-032 and closed MA-020. The decision
  authorizes only the approved authority phrase and pinned manifest-version
  expectations; it does not approve the identity.
- Froze the manifest/hash/inventory, authority documents, normalized selectors,
  all D-029 sources/checkpoint, reports, archives, and forbidden authority files.
- Reopened one validator and, only after a pass, the still-unconsumed browser/
  evidence/freeze/reviewer sequence. Any failure stops without edit or retry;
  MA-015 and all implementation/external gates remain blocked.

### 2026-07-20 — D-031 stopped on two stale assertion literals

- Normalized the final two audited selectors and confirmed zero malformed hits.
  The sole validator then returned 57 PASS / 2 FAIL on stale authority-phrase and
  manifest-version expectations, not on product or identity behavior.
- Read-only evidence confirmed D-029/MA-017 authority, the pinned manifest hash,
  exact 26/26 inventory, actual manifest version, and zero protected mismatch.
  No browser pass, evidence refresh, reviewer report, or freeze followed.
- Opened MA-020 for correction of exactly the two expected literals plus the
  unconsumed sequence, or stop unresolved. MA-015 and all implementation/external
  gates remain blocked.

### 2026-07-20 — Exhaustive remaining-selector normalization authorized

- Recorded the founder's 🛠️ choice as D-031 and closed MA-019. The decision
  authorizes normalization of exactly the forced-colors and color-contrast
  selector syntaxes identified by the exhaustive read-only audit.
- Requires zero malformed `Where-Object id -eq` hits before one deterministic
  validator and the still-unconsumed browser/a11y/evidence/freeze/reviewer sequence.
  Any failure stops without edit or retry.
- Preserves every product/identity source outside those two syntax forms, all D-029
  frozen hashes, six reports, 31 archive files, and 24 forbidden authority files.
  The choice is not identity approval and MA-015 remains blocked.

### 2026-07-20 — D-030 stopped on neighboring harness selector

- Repaired only the authorized text-spacing selector, then stopped the sole
  validator before assertions when PowerShell reached the neighboring malformed
  forced-colors selector. This remains a harness failure, not an identity verdict.
- A read-only `rg` audit found exactly two malformed selector occurrences remaining:
  forced-colors on line 171 and color-contrast on line 172. No product source,
  browser pass, evidence refresh, reviewer report, or freeze followed.
- Preserved the checkpoint, six reports, 31 archive files, 24 forbidden authority
  files, and five non-validator D-029 sources with zero mismatch. Opened MA-019 for
  one exhaustive two-selector syntax repair plus the unconsumed sequence, or stop.

### 2026-07-20 — Syntax-only D-029 validator recovery authorized

- Recorded the founder's 🛠️ choice as D-030 and closed MA-018. The decision
  authorizes exactly one syntax-only repair to the malformed PowerShell selector
  at validator line 171; it does not approve the identity.
- Froze all six D-029 source changes and protected the pre-stabilization checkpoint,
  six review reports, archive files, and forbidden identity-authority files. No
  product/identity/HTML/CSS/design/semantic/geometry change is authorized.
- Reopened one deterministic validator and, only after a pass, the still-unconsumed
  browser/a11y/evidence/freeze/reviewer sequence. Any failure stops without edit or
  retry; MA-015 and all implementation/external gates remain blocked.

### 2026-07-19 — D-029 stopped on validator-harness syntax

- Applied the six-file evidence-only patch, then stopped the sole deterministic
  validator before assertions when PowerShell rejected the line-171 `Where-Object`
  expression. This is a harness failure, not an identity/browser verdict.
- No browser pass or capture/report/manifest/inspection/reviewer refresh occurred.
  All six prior reports, 31 archive files, and 24 forbidden identity-authority
  files remained byte-identical; the two reserved reviewer reports remain absent.
- Blocked MA-015 and opened MA-018 for one recommended syntax-only harness repair
  plus the unconsumed bounded evidence/verification sequence, or stop unresolved.
  No edit, rerun, identity approval, or implementation authority is inferred.

### 2026-07-19 — Evidence-only identity stabilization authorized

- Recorded the founder's 🔁 choice as D-029 and closed MA-017. The decision
  authorizes exactly one evidence-only stabilization for the four recorded D-028
  browser failures; it does not approve the identity.
- Reopened only the smallest board semantics, CSS, audit harness, and directly
  invalidated evidence surfaces. All six prior review reports and existing
  archive/baseline evidence remain byte-for-byte immutable.
- Authorized one deterministic validator and one bounded browser/a11y pass with
  no retry. A clean freeze must still receive fresh independent design and
  accessibility verification before MA-015 can reopen; all implementation,
  external, production, publication, Git, deployment, and launch gates remain.

### 2026-07-19 — One-time hybrid identity correction stopped on browser evidence

- D-028's producer corrected the six recorded source classes and preserved a
  19-source pre-exception baseline plus all six immutable review reports.
- The single browser/accessibility pass failed with text-spacing width 321/320,
  one forced-colors contrast violation, and 12 incomplete checks. No captures,
  manifest rebuild, final validator, package freeze, or independent verification
  followed; browser/profile residue was zero.
- Marked the correction and its one stabilization exhausted, blocked MA-015,
  opened MA-017 for the founder to authorize exactly one evidence-only stabilization
  for the four recorded browser failures or stop unresolved, and kept identity, UI/application work,
  publication, production, trademark, Git, deployment, and launch unapproved.

### 2026-07-19 — One-time hybrid identity correction authorized

- Recorded the founder's 🔁 choice as D-028 and closed MA-016. The decision
  authorizes one correction-only exception for the recorded iteration-3 findings;
  it does not approve the identity.
- Reopened CR-001 and the identity slice only for stale Framework Relay semantics,
  application checkpoint/status grammar, traceability paths, responsive chart
  labels/series authority, text-spacing reflow, and directly affected evidence.
- MA-015 remains pending until deterministic validation and fresh independent
  design/accessibility verification pass. No redesign, second exception, external
  action, production use, implementation, publication, Git, or deployment work is
  authorized.

### 2026-07-19 — Hybrid identity revision escalated at the revision limit

- Producer iteration 3 delivered the Signal Ledger system + Framework Relay logo
  hybrid, archived the rejected Signal Ledger logo, and passed deterministic
  validation 41/41. The configured local axe evidence reported zero violations or
  incomplete checks, but automated validation was not treated as approval.
- Independent design review returned REVISE with four MEDIUM findings; independent
  accessibility review returned REVISE with two MEDIUM and one LOW. The core logo
  family was judged coherent, while stale semantics, one application-geometry
  error, evidence grammar, traceability paths, narrow labels, and text-spacing
  reflow still require correction.
- The approved three producer revisions are exhausted. Blocked MA-015, opened
  MA-016 for a narrow revision-limit exception or stop decision, and kept identity,
  UI/application work, publication, production, trademark, Git, deployment, and
  launch unapproved.

### 2026-07-19 — Hybrid identity change request opened

- Recorded D-027 and `docs/requirements/CHANGE_REQUEST_CR-001.md` from the
  founder/team response: retain the Signal Ledger identity system, reject its logo,
  and reconcile a Quiet Framework-derived logo family.
- Invalidated the prior MA-015 candidate without changing approved D-026 Evidence
  in Motion. Opened producer iteration 3 of the maximum 3 followed by fresh
  independent design and accessibility reviews; no final identity approval is
  inferred.
- Moved R-020 into active correction and added R-021 for final-iteration hybrid
  coherence/review risk. Application/UI work, external design writes, paid assets,
  trademark clearance, publication, production use, Git actions, deployment, and
  complete Phase 1 acceptance remain blocked.

### 2026-07-19 — Phase 1 brand identity ready for founder choice

- Produced and froze brand identity iteration 2 under
  `docs/phase-1-brand-identity/`, recommending **A — Signal Ledger** as the identity
  expression of approved **Evidence in Motion**. Deterministic validation passed
  35/35 with a 25-record local asset manifest and zero browser-profile residue.
- Independent design and accessibility iteration-2 reviews closed all eight prior
  findings. Design passed with one non-blocking LOW chart direct-labelling follow-up
  (`BID-DR-I2-001`) tracked as R-020 before production reuse; accessibility passed
  with no new or unresolved finding.
- Opened MA-015 for the founder's identity-direction choice. No approval is inferred;
  trademark/legal clearance, print proof, paid assets, external design writes,
  UI/application implementation, publication, production use, deployment, complete
  Phase 1 acceptance, and launch remain blocked.

### 2026-07-19 — Evidence in Motion approved; identity definition opened

- Recorded D-026 from the founder's thumbs-up after review of the complete
  Direction A strategy and its B/C comparison.
- Approved **Evidence in Motion**, the category “evidence-led innovation delivery
  partner,” and the promise “From complex ambition to accountable delivery.”
- Closed MA-014 and opened bounded brand-identity definition. No identity asset,
  UI, application code, public copy, external system, or deployment was approved.

### 2026-07-19 — Phase 1 brand strategy ready for founder choice

- Produced the bounded brand strategy under `docs/phase-1-brand-strategy/` with
  **Evidence in Motion** as the recommended direction, an evidence-led innovation
  delivery partner category, and the promise “From complex ambition to accountable
  delivery.” Identity assets and implementation remain excluded.
- Independent review iteration 1 returned one HIGH, one MEDIUM, and one LOW
  finding. Producer iteration 2 corrected the A-versus-B/C approval boundary,
  aligned qualified-booking and visitor-CTA language, and corrected/validated the
  weighted direction matrix.
- Independent review iteration 2 closed all three findings with no new finding;
  deterministic validation passed 43/43. Opened MA-014 for the founder choice.
  Direction B or C remains a preference requiring reconciliation, revalidation,
  and another independent review before strategy approval or identity work.

### 2026-07-19 — Phase 1 foundation accepted; brand strategy opened

- Recorded D-025 from the founder's “continue” response to the recommended gate,
  accepting the bounded foundation and retaining `/industries`.
- Closed MA-012 and opened the brand-strategy definition slice without authorizing
  identity production or application implementation.
- Recorded the compatibility inventory's independent iteration-2 pass after all
  four findings closed, and opened MA-013 for founder acceptance of its evidence
  and scope boundaries. Exact locks and dependency changes remain deferred.

### 2026-07-19 — Phase 1 foundation ready for founder review

- Produced the bounded requirements, claims, market/competitor, SEO/entity,
  canonical-route, editorial, conversion, and traceability foundation under
  `docs/phase-1-foundation/` without changing application code or dependencies.
- Resolved four independent requirements findings and two independent SEO findings
  in one bounded revision. Requirements iteration 2 and SEO iteration 2 passed
  with no new actionable finding in scope; final validation passed 49/49.
- Separated planned routes, approved content, active releases, indexability, and
  active-sitemap membership. No route is represented as active in the planning
  snapshot; `/industries` remains an explicit founder decision.
- Corrected the D-018 durable transcription to restore the founder-approved random
  24+ character break-glass credential requirement from the master plan; no new
  security decision was introduced.
- Added the dated compatibility inventory and coupled candidate graph under
  `docs/phase-1-compatibility/`. Producer validation passed for 50 baseline items,
  50 components, 27 edges, and nine explicitly deferred architecture families;
  exact production locks remain deferred and independent review is in progress.
- Opened manual gate MA-012 for the bounded foundation slice. Complete Phase 1,
  application implementation, publication, external actions, and launch remain
  unapproved.

### 2026-07-19 — Phase 0 accepted; Phase 1 opened

- Recorded the founder's explicit Phase 0 acceptance after the independent
  iteration 2 pass.
- Closed manual gate MA-001 and moved the durable project state to Phase 1
  `in_progress`.
- Preserved the definition-only boundary: no application source, dependency,
  migration, infrastructure, external-system, Git-history, paid-service, or
  deployment action was authorized by this gate.
- Repaired and updated LibreOffice to 26.2.4.2. A generated control DOCX and the
  24-page historical consolidation converted to PDF successfully; all target pages
  rendered for visual inspection. Independent QA passed the evidence and R-019
  closed with a fresh-conversion residual control. The historical source document's
  blank table of contents and sparse continuation pages remain classified as
  source-layout limitations rather than converter failures or approved design.

### 2026-07-18 — Phase 0 recovery and workflow adoption (awaiting founder acceptance)

#### Added

- Added the non-destructive project charter and explicit authority bridge.
- Added machine-readable phase/readiness state with the restricted workflow status
  vocabulary.
- Added dependency-ordered tasks and a decision-complete Phase 1 definition
  contract.
- Added the root operational decision index plus risk and manual-action registers.
- Added the detailed `docs/decisions-log.md` required by project rules.
- Amended the constitution to 2.0.0 and synchronized `AGENTS.md`, project rules,
  software-definition workflow documents, Copilot guidance, and Spec Kit templates
  with the approved authority, phase-state, latest-compatible-stable, Azure, SEO,
  AI/data, evidence, and independent-review policy.

#### Reconciled

- Classified the February 2026 v3 consolidation, SRS/SAD, AWS placeholder, and
  draft feature artifacts as supporting evidence when they conflict with the
  founder-approved direction.
- Recorded the future target as latest-compatible-stable technology within the
  retained stack families, with Context7 and official-primary-source evidence and dated
  exceptions.
- Recorded Azure managed services as the target direction and resolved the prior
  fixed-version/AWS governance conflict. Legacy v3 product documents, active
  technical references, backlog, diagrams, and draft specs remain Phase 1
  reconciliation work.
- Separated local (`in_progress`), UAT (`not_started`), and launch (`blocked`)
  readiness.

#### Independent review — iteration 1

- The independent reviewer returned `revise` with four high and one medium
  documentation findings.
- Removed the documentation index's conflicting “single source of truth” claim.
- Restored Context7 **and** official-primary-source evidence, including the safe
  direct MCP fallback for active-host exposure gaps.
- Removed the ungated Alembic mutation from generic local startup guidance.
- Demoted legacy numeric FPS thresholds to a Phase 1 proposal requiring founder
  approval, while retaining the already approved Core Web Vitals and asset budgets.
- Corrected the constitution Sync Impact Report artifact list and deferred spec
  path.

#### Independent review — iteration 2

- The independent reviewer returned `pass` with no remaining critical, high,
  medium, or actionable low finding.
- YAML/status, all 22 artifacts, 23 decisions, 11 manual actions, local links,
  deferred spec path, secrets, stale governance, Git diff, staging, and branch
  divergence checks passed.
- Phase 0 moved to `awaiting_human`; Phase 1 remains blocked until explicit founder
  acceptance.

#### Post-review evidence correction

- Confirmed LibreOffice 25.8.7.3 is installed; the earlier missing-installation
  inference was incorrect.
- The packaged renderer, isolated clean profiles, normalized DOCX copy,
  one-paragraph control DOCX, disabled graphics/OpenCL paths, and LibreOffice safe
  mode did not produce a PDF. Windows recorded BEX64 exception `0xc0000409` for
  `soffice.bin`.
- Structural review of the historical consolidation remains valid. Its visual
  layout remains unverified because the installed headless converter crashes, not
  because LibreOffice is absent. This is a non-blocking historical-evidence
  limitation and is now tracked as R-019.

#### Not changed

- No application source code, dependency, lockfile, runtime, migration, database,
  container, credential, MCP configuration, external service, branch, commit,
  remote, or deployment was changed by Phase 0.
- The 16 pre-existing tracked modifications and 63 pre-existing untracked files
  observed before Phase 0 were preserved rather than reverted or discarded;
  approved governance changes were layered onto the applicable files.

#### Gate

- Phase 0 is `awaiting_human` after independent review passed. Phase 1 is the only
  prepared next action and remains blocked until founder acceptance closes the
  gate.

### 2026-09-06 — D-044 specification commissioning complete (no implementation)

Added two `[PROPOSED SPECIFICATION]` documents, authored independently of the
producer under D-044:

- `docs/phase-1-ui-reference-design/DELIVERY_STREAM_EVIDENCE_MODEL.md`
- `docs/phase-1-ui-reference-design/accessibility/DELIVERY_STREAM_ACCESSIBILITY_OBLIGATIONS.md`

Nothing was implemented from either. No package artifact, validator, or ledger
row encodes their model. Neither document is accepted; the founder decision is
tracked at **MA-030**. Recorded rather than acted on: gate **G-1** (`S-LOW`
unsignalled default contradicts explicit World entry at `UX_ARCHITECTURE.md:173`)
and gate **G-5** (`time_limit_branch` is a total function of `state_profile`, the
same derived-column defect that condemned `stream_profile`). B01 remains held;
zero Figma allowance consumed; nothing staged or committed.

### 2026-09-06 — D-045 delivery-stream model accepted (specification only)

The founder accepted both `[PROPOSED]` specifications and resolved four contested
points: G-1 separates capability-derived **stream selection** from explicit
**World entry**, so neither the style guide nor `UX_ARCHITECTURE.md:173` is
overruled; `DS-STREAM-INVARIANT` is **deleted**, with the test surviving as an
assertion and `OBL-INV-01`'s derivation conditions retained in validator source as
the recorded reasoning; the radio-group-plus-explicit-submit control and the
persistent-visible-text advisement are normative; and the full merged evidence set
is the obligation, with Figma calls batched per CB-13 and approved individually per
CB-06. **No call projection was offered.** MA-030 discharged.

Accepting a specification is not accepting an implementation. R-035 remains open,
MA-029 remains undischarged, B01 remains held, and gate G-5 (`time_limit_branch`
derived from `state_profile`) is recorded and deliberately unfixed.

### 2026-09-06 — D-045 delivery-stream evidence model implemented (documentation only)

The producer implemented the two accepted specifications in one bounded slice across
the design and production packages, and **only** implemented them. Where literal
implementation produced a result the producer believes is wrong, the result is
recorded as an observation for the reviewers rather than corrected — authoring a fix
would repeat the exact D-044 pattern D-045 was decided to end.

**The model.** Stream obligations are **declared** at the primitive
(`component-primitives.csv.stream_presence`), **computed** at the template by a union
fold over `primitive_dependencies`, and **inherited unstored** at route and flow. No
route, flow, or template row carries a stream column, and `A-01` fails if one returns.

**Design package.** Eleven assertions `A-01`–`A-11` added; `EC-08` amended to carry a
mandatory single-valued `STREAM_<HIGH|MEDIUM|LOW|SEMANTIC>` segment with no aggregate
form, `EC-09` lineage widened to a 7-tuple, `EC-30` identity extended; all 74
`baseline_frame_name` values regenerated in one pass; `UXTEST-046` added; 14
requirement rows traced (`NFR-A11Y-001`–`007`, `FR-3D-010`–`016`) in both the UX and
design matrices. Validator `RESULT=PASS PASS_COUNT=201 FAIL_COUNT=0`.

**Production package.** Five assertions `A-12`–`A-16` added; `stream_id` defined in
contract §5.2; `stream_disposition` added to `batch-production-plan.csv`. Validator
`RESULT=PASS PASS_COUNT=165 FAIL_COUNT=0`. The package freeze hash moved from
`E3786F14…C08D` to `4464F6C44C11E7A00C4F007C3112840C6087CB3C1321B86ED5842B9100CC50CE`,
because the contract is inside the nine-file freeze set. The design package freeze
aggregate settled at `0AA83FD298ABB12A96782205996EB3783BF8E80E11AD1B2BE44473F2E87EB536`. The prior value is historical,
not wrong.

**Founder gates applied.** G-1 separates stream selection from World entry
(`FR-3D-015`, style guide §8.2.5); G-4 sets B01 to `future_not_authorized` in **both**
plan files; G-7 makes booking process state survive a stream change across any boundary
including the semantic one (`FR-3D-016`, §8.2.6); G-6 leaves
`DESIGN_SYSTEM_IMPLICATIONS.md` **untouched with its freeze hash intact** and records
the missing stream axis as risk **R-039** for a later bounded contract; the invariance
profile is deleted with its test surviving as `A-06`.

**Two defects found that no prior run could.** `A-10` resolves frame-name tokens
instead of pattern-matching them, and caught `MODE_NON_WEBGL_QUICK_ACCESS` on
`TPL-QUICK-ACCESS-RECOVERY` — the surviving R-034 instance, which evaded the old guard
because it was spelled with underscores — and `STATE_UNAVAILABLE` on `ROUTE-CONTACT`,
which **no reviewer had reported**.

**A third defect was the producer's own, and is recorded rather than quietly fixed.**
The new cross-package framing guard was **silently inert** on its first run: PowerShell's
comma operator binds tighter than `+`, so its nine-alternative array literal collapsed
into one `$OFS`-joined string and the guard reported zero hits across 56 files that
contained known matches. That is the D-045 defect shape — an assertion that cannot fail
— reintroduced while implementing the remedy for it. Both validators now assert the
alternative count. Logged as **R-038**.

**What the working guard then found.** Six live UX-architecture files still described
the World as optional and the stream axis as a quality ladder, three days after D-039
abolished that framing, because no previous guard looked outside the design package's
own thirteen freeze files. All six were swept. **R-034 does not close** — its exit
evidence names an independent reviewer, and this was again a producer sweep.

**Recorded, not repaired.** Twenty-two inert judgement columns including
`time_limit_branch` (**R-037**); the constant `stream_disposition`; `A-11`'s determiner
set as a producer reading of an underspecified instruction; eleven state profiles `A-08`
implicates that the specification's migration table did not enumerate; the staff,
publication, and audit templates folding to all four streams; the all-or-nothing frame
regeneration (**R-040**); `A-14`'s wholly unmet obligation set (**R-041**).

All four validators pass: foundation, UX architecture (113/0), design (201/0), production
(165/0). **Nothing staged or committed. No external write. Zero Figma allowance consumed.
B01 held. MA-029 undischarged. R-035 and R-036 open.**

