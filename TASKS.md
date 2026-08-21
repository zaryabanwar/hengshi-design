# Hengshi Design Delivery Tasks

**State:** Phase 0 accepted; Phase 1 in progress
**Last reconciled:** 2026-07-20
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

### Bounded Slice Status — 2026-07-20

| Slice | Status | Evidence / next gate |
|---|---|---|
| Requirements, claims, SEO, routes, and conversion foundation | `accepted` | D-025 records founder acceptance after both independent iteration-2 passes and final validation 49/49; `/industries` is retained. |
| Compatibility inventory and candidate graph | `awaiting_human` | Independent iteration 2 passed after all four findings closed. MA-013 covers inventory acceptance only; exact production locks and dependency changes remain deferred. |
| Brand strategy | `accepted` | D-026 records founder approval of Direction A — Evidence in Motion after producer validation 43/43 and a clean independent iteration-2 review. |
| Brand identity | `accepted` | D-035 records the founder's explicit `approved.` response at MA-015 for the exact frozen Signal Ledger system + Framework Relay logo hybrid. D-034 validation remains 63/63 with clean nine-state browser/a11y evidence and independent design/accessibility PASS. Marks remain unregistered/trademark-not-cleared; no implementation or publication authority is inferred. |
| UX architecture and accessible journeys | `accepted` | D-036 records the founder's explicit approval of the exact final package under `docs/phase-1-ux-architecture/`: 113/113, 33 routes, nine exclusions, 15 wayfinding entries, 53 action contracts, 45 UX tests, 123 trace rows, and final design/accessibility PASS. No UI/design production or implementation is inferred. |
| UI reference-design contract and foundation-surface coverage | `not_started` | Recommended next bounded Phase 1 slice. Prepare the contract and coverage plan from D-036/D-035/D-026 and accepted foundation. Do not create production UI or make an external Figma/Stitch write without explicit approval. |

Passing the foundation slice does not accept the complete Phase 1 package and
does not authorize application, dependency, migration, infrastructure, external
design, publication, Git-history, or deployment work.

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
