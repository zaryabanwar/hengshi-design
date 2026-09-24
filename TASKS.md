# Hengshi Design Delivery Tasks

**State:** Phase 0 accepted; Phase 1 in progress
**Last reconciled:** 2026-09-03
**Status vocabulary:** `not_started`, `in_progress`, `blocked`,
`awaiting_human`, `in_review`, `accepted`

Tasks authorize only the named phase. Later-phase entries are sequencing markers,
not permission to implement them.

## Phase 0 — Recovery and Workflow Adoption

| ID | Status | Task | Evidence |
|---|---|---|---|
| P0-001 | accepted | Preserve and record the pre-existing dirty working tree without staging, reverting, moving, or overwriting it. | `PROJECT_STATE.yaml` working-tree baseline |
| P0-002 | accepted | Create the durable charter, state, task, decision, risk, manual-action, and changelog records. | Phase 0 artifact list in `PROJECT_STATE.yaml` |
| P0-003 | accepted | Amend the constitution, agent/project rules, software-definition workflow, Copilot guidance, and Spec Kit templates to implement the approved authority, latest-compatible-stable, Azure, SEO, AI/data, evidence, and review policy. | Constitution 2.0.0 and Phase 0 artifact list in `PROJECT_STATE.yaml` |
| P0-004 | accepted | Record evidence-based local, UAT, and launch readiness without reusing historical percentage estimates as current proof. | `PROJECT.md`, `PROJECT_STATE.yaml` |
| P0-005 | accepted | Validate YAML, referenced paths, documentation-only diff, whitespace, and absence of secret values. | Phase 0 validation report passed |
| P0-006 | accepted | Obtain independent documentation review and resolve findings within two revisions. | Iteration 2 passed with no remaining actionable finding |
| P0-007 | accepted | Obtain founder acceptance of the reconciled Phase 0 records. | Explicit founder approval on 2026-07-19; `MANUAL_ACTIONS.md` MA-001 |

Phase 0 became `accepted` when the founder explicitly closed P0-007 on 2026-07-19.
This approval opens Phase 1 definition work only; it does not authorize application
implementation, external writes, spending, or deployment.

## Exact Next Action — Phase 1 Contract

**Title:** Definition, SEO, design, architecture, and compatibility package
**Status:** `in_progress` after Phase 0 founder acceptance on 2026-07-19
**Coordinating role:** Hengshi project manager
**Producer/reviewer separation:** required

### Bounded Slice Status — 2026-09-03

| Slice | Status | Evidence / next gate |
|---|---|---|
| Requirements, claims, SEO, routes, and conversion foundation | `accepted` | D-025 records founder acceptance after both independent iteration-2 passes and final validation 49/49; `/industries` is retained. |
| Compatibility inventory and candidate graph | `awaiting_human` | Independent iteration 2 passed after all four findings closed. MA-013 covers inventory acceptance only; exact production locks and dependency changes remain deferred. |
| Brand strategy | `accepted` | D-026 records founder approval of Direction A — Evidence in Motion after producer validation 43/43 and a clean independent iteration-2 review. |
| Brand identity | `accepted` | D-035 records the founder's explicit `approved.` response at MA-015 for the exact frozen Signal Ledger system + Framework Relay logo hybrid. D-034 validation remains 63/63 with clean nine-state browser/a11y evidence and independent design/accessibility PASS. Marks remain unregistered/trademark-not-cleared; no implementation or publication authority is inferred. |
| UX architecture and accessible journeys | `accepted` | D-036 records the founder's explicit approval of the exact final package under `docs/phase-1-ux-architecture/`: 113/113, 33 routes, nine exclusions, 15 wayfinding entries, 53 action contracts, 45 UX tests, 123 trace rows, and final design/accessibility PASS. No UI/design production or implementation is inferred. |
| UI reference-design contract and foundation-surface coverage | `accepted` | D-037 records founder acceptance of the producer iteration 3/3 freeze at SHA-256 `97E79201CC36F01718A027AD800E63BDD5AAFC47E41137D65253BAABA6B2120F` after validation 183/183 and clean final independent design/accessibility reviews. External visual production now awaits MA-025; no application implementation is authorized. |
| External UI reference-production contract | `accepted` | **MA-025 approved 2026-09-06 (D-038).** Nine files frozen at SHA-256 `E3786F14C9F12CBF8127A18E7959881B91A9ECC5DC11BBE3E466BCEC6C7EC08D`. Batches B01–B06 and B08 authorized; B07/B09 and `docs/ui/UI_SPEC.md` remain deferred to MA-026. §3.5 capability enablement completed by Path A and recorded in `validation/capability-evidence.md`; Figma is capability-tested via a rate-limit-exempt `whoami`. No external write has been performed. |
| Figma call rationing under the verified allowance | `awaiting_human` | **`SC-05` fired and was resolved, not waived.** The verified allowance is **20 MCP tool calls per calendar month** (Full seat, `starter` tier) against a 21-call structural floor across seven batches, so the programme spans multiple months. Founder directed staying free and rationing precisely. `mcp-call-budget.csv` (`CB-01`–`CB-15`) and `mcp-call-ledger.csv` govern and count every call; write-tool exemption is **NOT ASSERTED**. **`CB-06` decided 2026-09-06:** all 20 calls spendable, zero reserve, **every call requires explicit founder approval immediately before it is made**. `CB-07` binds the producer to never call unprompted and to state tool, purpose, and running count each time. Tracked as R-033. |
| B01 pilot and metering experiment | `authorized_not_started` | Unblocked by the `CB-06` decision; each call now needs founder approval at the moment it is made. B01 keeps its MA-025 gated-pilot status and additionally measures true per-batch call cost. Its exit must report total calls, calls by tool, any rate-limit response, and a measured projection for B02–B06 and B08. **No schedule may be stated until that projection exists (`CB-09`).** |

| HQ exterior 3D asset provenance and rights | `accepted` | **MA-004 closed 2026-09-06.** `HSD-ASSET-001` records the verified Sketchfab source, author `99.Miles`, and **CC BY 4.0** licence — commercial use and modification permitted, attribution required. Identity corroborated at 37,302 triangles against the stated 37.3k without downloading the source. Founder adopted the narrow NoAI reading; geometry reuse authorized subject to AR-01–AR-04. Attribution decided as a footer "Asset Credits" link to `/credits`. Two obligations remain open and tracked: ATTR-03 (absent GLB `asset.copyright`, deferred to authorized 3D production) and the 34th-route reconciliation (R-032, assigned to the CR-002 revision window). No download, import, or Blender session performed. |
| CR-002 four supported 3D delivery streams | `accepted` | **MA-027 approved as Option A 2026-09-06 (D-039).** Four peer streams (high, medium, low, no-WebGL/semantic) selected by device capability and connection, with equivalent core journeys, a selection rule, user override, and accessibility-preference precedence. B07 reclassified from optional to core but **still deferred to MA-026**, since the 3D storyboard workstream is `not_started`. `U-01`–`U-03` remain `[MUST VERIFY AT SPECIFICATION]`; no schedule offered. |
| CR-002 signal-portability verification (U-01, U-02, U-03) | `accepted` | Verified 2026-09-06 against MDN Baseline banners; record at `docs/requirements/CR-002-signal-portability-verification.md`. **U-01 resolved unfavourably** — no portable declared network class exists. **U-02 split** — `deviceMemory` is outside Baseline, but `hardwareConcurrency` (Baseline since March 2022) and `prefers-reduced-motion` (since January 2020) are firm. **U-03 stays open** and is reclassified as implementation-phase measurement that cannot close in Phase 1. The four streams survive; the selection rule must bind to capability probes plus measured performance. R-030 stop **not** triggered. Per-browser versions and vendor standards positions were not obtained and are not asserted. |
| CR-002 revision window | `complete` | **Executed 2026-09-06 (D-040).** Style guide §8.2 rewritten as four peer delivery streams with the founder-decided selection precedence (WebGL ceiling; reduced-motion suppresses motion not stream; override may only simplify; `hardwareConcurrency` tiering; `S-LOW` unsignalled default; one promotion then locked). SRS `FR-3D-010` restated as the `S-SEMANTIC` peer at **P0** with `FR-3D-011`/`FR-3D-012` added. B07 reclassified to core with stream-selection evidence. 15 degradation framings removed across seven artifacts; `optional_immersive_representation` renamed `immersive_stream_representation`. `/credits` reconciled as the 34th route across foundation, UX, and design packages. Closes **R-032** and **R-034**. Two latent validator defects repaired: `git-write-scope` is now lifecycle-aware (the R-024 error again) and the foundation validator no longer aborts on git's CRLF warning. New standing assertion `semantic-stream-peer-framing` prevents regression. All four validators pass. |
| CR-002 amended package re-acceptance | `accepted` | **MA-028 approved by the founder 2026-09-06 (D-041).** The amended D-025/D-036/D-037 artifacts carry accepted authority; design aggregate `F16093D0...4AD6` and production aggregate `3DF0DBB6...8528` are the accepted freeze values. The production contract no longer falls back to the D-037-accepted package. **The independent design and accessibility reviews this gate also required did not run** — unreviewed quality risk is knowingly accepted and **R-035 stays open as `accepted_by_founder`**, not closed. Its exit evidence is still a clean independent design review and a clean independent accessibility review. |
| Reviewer-authored delivery-stream evidence model and accessibility obligations | `complete` | **Accepted at D-045 and implemented 2026-09-06.** Both specifications were accepted with seven founder resolutions (G-1 separation of stream from World entry; invariance category deleted with the test surviving; radio-group-plus-Apply normative; full merged frame set with per-call approval; G-4 B01 held in both plan files; G-7 process state survives a stream change; G-6 design-system gap recorded not authored). The producer implemented and only implemented: obligations **declared** at the primitive, **computed** at the template by a union fold, **inherited unstored** at route and flow. Design validator 201/0, production 165/0. Seven results are recorded as observations rather than repaired — see R-037, R-038, R-040, R-041 — because repairing them would be the producer authoring the model again. **This completes the implementation task and discharges nothing else.** |
| Reviewer-authored delivery-stream evidence model and accessibility obligations (commissioning record) | `complete` | **D-044.** Two [PROPOSED] specifications commissioned from the independent reviewers: `DELIVERY_STREAM_EVIDENCE_MODEL.md` (stream-dependence rule, evidence locus, schema, `EC-08` stream token, assertion designs, B01 frame-count impact) and `accessibility/DELIVERY_STREAM_ACCESSIBILITY_OBLIGATIONS.md` (per-stream conformance, the stream control's role and activation model, 3.2.2 advance advisement versus 4.1.3 announcement, the `S-SEMANTIC` boundary crossing, traceability and tests). Neither carries accepted authority until a founder decision. The producer implements to them and does **not** author the model. |
| R-039 design-system amendment (bounded specialist contract) | `in_progress` | **Commissioned at D-046 and accepted at D-047, 2026-09-24.** Amendment revision 2 (`cf455db`) accepted after independent review 1 (FAIL on DSA-01, resolved) and independent review 2 (PASS on both parts; DSB-01 and DSB-02 carried to application). Application slice in progress under D-047: the fourteen insertions applied mechanically to `DESIGN_SYSTEM_IMPLICATIONS.md`, freeze hash and aggregate re-pinned, four validators run, application independently verified. No Figma call, no external write, B01 still held. Exit evidence: the verified application commit plus a clean verification record; then R-039 closes. |
| Independent re-review of the D-043 remediated package | `failed` | The D-042 re-reviews ran 2026-09-06 and **both returned FAIL again**, converging on five defects — chiefly that the delivery stream axis D-042 added was **inert**, asserted by row count and selected by no record. Remediated under **D-043** (full schema fix: `stream_profile` required and populated across routes, flows, and templates; `DS-STREAM-INVARIANT`; `ACT-09` moved into authorized `B01`; WCAG 3.2.2 claim withdrawn; SRS §5.6 added). Three FAIL rounds have now followed validator runs of 183, 184, and 185 passing assertions. Gate **MA-029**; risk **R-035** stays open — the producer does not approve its own output. Exit evidence: a clean independent design review and a clean independent accessibility review against aggregate `DB92B4D0...4649`. **Round 3 ran 2026-09-06 and both reviews returned FAIL.** `stream_profile` was a derived function of `state_profile`, so the axis was inert one level up; all 34 routes took `DS-STREAM-INVARIANT` while every route template depends on `PRIM-001`, which that profile's own `exception_rule` forbids; and the production package has no stream axis, so per-stream frames cannot be named. **MA-029 not discharged; R-035 stays open.** Approach changed at **D-044**. |
| B01 reference-frame production | `blocked_by_founder_decision` | **Held by explicit founder decision until MA-029 returns clean, and set to `future_not_authorized` in *both* plan files under gate G-4** so one batch does not carry two authorization states. Frames drawn against a package with an inert stream axis would need redrawing, and redraws spend metered Figma calls from the 20-call monthly allowance. Zero allowance consumed; no external write. Release requires a founder decision plus the CB-06/CB-07 per-call approval exchange. **R-039 must also resolve first:** the design system declares no stream-control component and no stream tokens, so the control B01 would draw has nothing to draw it from. |

Passing this or any other bounded Phase 1 slice does not accept the complete
Phase 1 package and does not authorize application, dependency, migration,
infrastructure, external design, publication, Git-history, or deployment work.

### Active PM Contract — External UI Reference-Production Authorization

- **Objective:** define the bounded contract under which a later authorized
  producer may perform external design-provider writes to create the reference
  screens contracted by D-037, covering provider choice, batch scope and sequence,
  write scope, deliverables, evidence capture, review sequence, cost boundary,
  stop conditions, rollback, credential handling, and acceptance criteria.
- **Exclusions:** no Figma or Stitch operation of any kind, no visual production,
  no `docs/ui/UI_SPEC.md`, no application/3D code, no exact public or legal copy,
  no paid or licensed assets, no dependency, migration, or infrastructure change,
  no publication, no Git operation, no deployment, and no D-038 decision entry
  before the founder decides.
- **Deliverables:** nine files under `docs/phase-1-ui-reference-production/` —
  README, the normative contract, five CSVs (provider evaluation, batch plan,
  external write scope, evidence capture plan, stop conditions, traceability), a
  PowerShell validator, a validation report, and producer inspection. Frozen at
  SHA-256 `E3786F14C9F12CBF8127A18E7959881B91A9ECC5DC11BBE3E466BCEC6C7EC08D`.
- **Validation and review:** deterministic validation passes **147/147** with zero
  failures, including 37 cross-artifact assertions that carry every batch's
  prerequisites, time-limit branch, and browser profile verbatim from the accepted
  `design-batch-plan.csv`. Independent design and accessibility review are
  **not started**; the producer has not approved this package.
- **Two material findings:** (1) only seven of nine batches are authorizable —
  B07 is blocked by MA-004 and the `not_started` 3D storyboard workstream, and B09
  hard-requires B07, so the D-037 §15 handoff cannot complete under MA-025;
  (2) no Figma or Stitch MCP is configured or exposed on this host and the
  canonical inventory named by `AGENTS.md` does not exist, so MA-025 approval
  alone does not start production.
- **Revision limit:** three producer revisions per batch under the UI limit,
  budgeted per batch and non-transferable. Exhaustion escalates as a change
  request rather than a fourth revision.
- **Human gates:** MA-025 authorizes bounded external production for B01–B06 and
  B08 only. A founder B01 pilot acceptance releases B02–B08. MA-026 remains the
  later gate for B07, B09, `docs/ui/UI_SPEC.md`, and the final visual direction.
  MA-013 compatibility acceptance is separate and unaffected.

### Completed PM Contract — UI Reference-Design Definition

- **Objective:** define every required future reference template, route/flow
  instance, state, viewport, mode, evidence unit, and production batch without
  creating a screen or changing accepted product behavior.
- **Exclusions:** no Figma/Stitch or other external write, visual production,
  application/3D code, exact public or legal copy, assets, dependency changes,
  publication, Git operation, deployment, or complete Phase 1 acceptance.
- **Deliverables:** 13 frozen producer files under
  `docs/phase-1-ui-reference-design/`, plus preserved independent review history.
  The contract covers 33 routes, nine exclusions, 15 wayfinding records, 53
  actions, 45 UX tests, 40 templates, 32 profiles, 62 primitives, and nine future
  design batches.
- **Validation and review:** final deterministic validation passes 183/183;
  independent design iteration 3 and accessibility iteration 2 both PASS with
  zero CRITICAL, HIGH, MEDIUM, or LOW findings.
- **Revision limit:** all three normal UI-contract producer revisions are used.
  A material change requested at MA-024 requires a separately authorized change
  request rather than an unbounded fourth revision.
- **Human gates:** D-037 closes MA-024 and accepts this documentation contract
  only. MA-025 is the separate explicit approval required before any external
  Figma/Stitch production or write, and final visual direction remains a later
  founder gate.

### Completed PM Contract — UX Architecture and Accessible Journeys

- **Objective:** coordinate a founder-reviewable UX architecture and UI-definition
  package for the semantic Quick Access journey and optional 3D journey, with
  equivalent content, actions, recovery, and accessibility.
- **Exclusions:** no application/UI code, dependencies, 3D production assets,
  exact public copy/publication, external Stitch/Figma write without its explicit
  approval, paid assets, Git operation, deployment, or identity alteration.
- **Required inputs:** governing project documents; accepted Phase 1 foundation;
  D-026 strategy; D-035 frozen identity; CR-001 closure; software-definition and
  relevant legacy artifacts as non-authoritative evidence.
- **Allowed tools/write scope:** read-only repository/browser/official evidence;
  future project-scoped UX/UI definition artifacts only under bounded specialist
  contracts; durable root state records. No product source writes.
- **Deliverables:** information architecture, responsive journeys, semantic
  Quick Access/non-WebGL parity, optional 3D mapping, keyboard/reduced-motion/error
  and recovery states, reference-screen plan, traceability, and acceptance tests.
- **Validation evidence:** deterministic path/traceability checks plus separate
  UX, UI/design, and accessibility review; live visual/browser evidence only after
  an approved reference artifact exists.
- **Acceptance criteria:** all required states and parity are specified, claims and
  copy remain within approved authority, no unresolved CRITICAL/HIGH/MEDIUM
  finding remains, and the founder accepts the definition before implementation.
- **Maximum revisions:** three for UI/design production; two for other artifacts.
- **Human gates:** material journey/app-structure choice, exact public copy,
  identity change, external design write, paid activation, or complete Phase 1
  acceptance. MA-013 remains a separate compatibility decision.

### Objective

Produce a complete, decision-ready definition package for the approved Hengshi
Design product before application development. Apply the Phase 0-amended
latest-compatible-stable and Azure governance while superseding or reconciling
the older v3 product documents, backlog, diagrams, active technical references,
and draft feature specs.

### Exclusions

- No application feature implementation or UI production code.
- No dependency, lockfile, runtime, database, or container-image upgrade.
- No database migration or data mutation.
- No Azure, Microsoft 365, NVIDIA, DNS, Search Console, Bing, or other external
  account write or provisioning.
- No paid activation, credential change, commit, push, PR, or deployment.
- No final Blender production scene; Phase 1 defines its approved specification.

### Required Inputs

- `AGENTS.md`, `.specify/memory/constitution.md`, `PROJECT.md`,
  `PROJECT_STATE.yaml`, `TASKS.md`, `DECISIONS.md`, `RISKS.md`, and
  `MANUAL_ACTIONS.md`.
- `docs/software-definition/`, `docs/decisions-log.md`, the v3 consolidation,
  SRS/SAD/mapping/API/security/style references, and current-state diagrams.
- Relevant `specs/` artifacts, explicitly treated as drafts where recorded.
- Verified repository, browser, package, model, and live-tool evidence.
- Context7 and official primary documentation for every version-sensitive choice.
- The approved competitor/reference synthesis and only verifiable Hengshi business
  facts supplied or approved by the founder.

### Allowed Tools and Write Scope

- Read-only repository, browser, package-registry, Context7, official-documentation,
  and safe capability checks.
- Project-scoped writes only to Phase 1 definition/specification artifacts named in
  the approved specialist contracts.
- Approved Stitch or Figma references for production UI; use both only where the
  approved design contract requires both. Any external write that exceeds an
  already approved reversible design operation requires its gate.
- No source, dependency, infrastructure, migration, Git, or production writes.

### Deliverables

1. Product/business requirements with audiences, outcomes, service and sector
   scope, conversion definition, exclusions, and evidence rules.
2. Claim, case-study, demo, expert, content-owner, and missing-evidence inventory.
3. SEO entity strategy, keyword/intention map, canonical route inventory,
   structured-data policy, redirects, crawler policy, editorial standards,
   launch content briefs, and organic measurement plan.
4. Brand strategy, identity direction, voice, design tokens, and accessibility
   implications.
5. Information architecture, responsive and 3D journeys, error/recovery states,
   reduced-motion and non-WebGL parity, and UX acceptance evidence.
6. Approved Stitch or Figma references for all foundation production surfaces,
   with both formats only where the approved design contract requires both.
7. 3D storyboard, asset manifest, provenance rules, performance budgets, Blender
   rebuild specification, and old/new visual review method.
8. Technical architecture and ADR set for frontend, backend, publication,
   prerendering, Azure, AI routing, Redis, PostgreSQL, identity, Graph, monitoring,
   CI/CD, backup, rollback, and SEO delivery.
9. API, WebSocket, publication-manifest, data-model, consent, booking, audit,
   retention, and deletion contracts.
10. Security, privacy, AI-governance, defense-content, legal-review, and human
    handoff controls.
11. QA strategy covering unit, contract, integration, migration, browser,
    accessibility, security, performance, load, recovery, and release evidence.
12. Dated compatibility matrix for all runtime, framework, 3D, backend, database,
    Azure/Graph/AI, QA, Blender, CI, container, and Bicep/API components, with
    current version, target version, peer/runtime constraints, breakages, security
    status, source, rollback, and exception/recheck date.
13. Costed Azure/NVIDIA operating envelope and phase-specific approval gates,
    without activating paid services.
14. Reconciled legacy product definitions and feature specs, including explicit
    replacement of the obsolete AWS launch placeholder and fixed-version prototype
    targets under the already-amended Phase 0 governance.

### Validation Evidence

- Trace every approved decision and requirement to one or more deliverables and
  acceptance checks.
- Parse every machine-readable artifact and validate every local reference.
- Cite Context7 query dates and official primary sources for version-sensitive
  conclusions; run safe capability tests before calling an integration operational.
- Validate route uniqueness, content ownership/proof status, data classification,
  security/privacy threat coverage, and no unsupported public claim.
- Independently review requirements, brand/design, UX, architecture, security,
  accessibility, SEO/content evidence, and deployment/recovery.
- Resolve reviewer findings within two iterations; brand, UI, motion, and 3D allow
  three.
- Inspect the documentation-only diff and run a secret scan before the approval
  gate.

### Acceptance Criteria

- The package is decision-complete and contains no unresolved implementation choice.
- All documents agree on authority, product scope, routes, interfaces, data flows,
  versions, security/privacy rules, performance budgets, rollout, and rollback.
- Every public claim is verified, explicitly labeled as a capability demo, or held
  from publication.
- Every production UI surface has an approved Stitch or Figma reference and any
  additional design format required by its approved design contract.
- The compatibility graph has no unresolved peer/runtime/cloud conflict. Any
  exception is a dated ADR with rollback and quarterly recheck.
- Independent findings are resolved or explicitly accepted by the founder.
- The founder approves scope/claims, brand/design, architecture/security, and the
  proposed cost envelope before Phase 2.

### Human and External Gates

Phase 1 must stop only for a material business decision, unsupported claim,
identity/design approval, legal or defense decision, cost envelope, paid service,
credential/account action, or external write not already authorized. Exact known
gates are recorded in `MANUAL_ACTIONS.md`.

## Later Phases — Sequencing Only

| Phase | Status | Entry condition |
|---|---|---|
| 2 — Stability, security, and modernization | blocked | Phase 1 accepted |
| 3 — Publication, SEO, and admin foundation | blocked | Phase 2 accepted |
| 4 — Brand and responsive search experience | blocked | Phase 3 accepted plus approved Stitch/Figma surfaces |
| 5 — Exterior, reception, and atrium | blocked | Phase 4 accepted plus GLB/license and 3D design gates |
| 6 — Concierge, handoff, and booking | blocked | Phase 5 accepted plus provider/account approvals |
| 7 — Foundation hardening and launch | blocked | Phase 6 accepted plus legal, infrastructure, DNS, and paid gates |
| 8 — Shared spaces and wings | blocked | Foundation launch evidence accepted; each wing separately gated |
| 9 — Organic growth and lifecycle maintenance | blocked | Launch accepted and measurement baseline established |

- **Blocked on MA-030 — founder decision on the two [PROPOSED] delivery-stream
  specifications.** Both delivered 2026-09-06 under D-044. The producer may not
  implement, and may not accept, until the founder decides G-1, the invariance
  treatment, the control's activation model, and the frame budget. G-5
  (`time_limit_branch` derived from `state_profile`) is recorded and unfixed.
