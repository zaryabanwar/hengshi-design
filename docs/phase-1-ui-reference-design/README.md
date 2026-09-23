# Phase 1 UI Reference-Design Contract

**Project:** Hengshi Design  
**Package date:** 2026-09-03  
**Amended:** 2026-09-06 under D-042 and D-043 (CR-002 revision window). The 2026-09-03 producer freeze date above is retained as provenance and is not restated as current; the delivery stream axis, the ACT-09 stream control, and the peer-framing renames were added after it.  
**Status:** Producer iteration 3 of 3; final producer freeze awaiting fresh
independent design and independent accessibility review before founder decision
at MA-024  
**Visual-production status:** Not authorized; no Figma, Stitch, UI, 3D, application,
or external write was performed

## Purpose

This package defines the complete, tool-neutral screen, state, breakpoint, mode,
content, and evidence contract for later Hengshi Design reference-screen
production. It turns the accepted foundation, brand strategy, brand identity, and
UX architecture into a bounded set of reusable reference templates and explicit
route/flow instances. It does not create visual screens.

The contract is deliberately two-layered:

1. `reference-template-inventory.csv` defines reusable visual and interaction
   templates. A later design producer creates the minimum reference evidence for
   each template.
2. `foundation-route-coverage.csv` and `foundation-flow-coverage.csv` instantiate
   those templates across every accepted route, exclusion, wayfinding record,
   flow family, and action. A route-instance record is coverage evidence, not a
   separate public route, content approval, or mandatory duplicate full-page
   frame.

## Controlling authority

- **D-025** accepts the requirements, claims, SEO, route, and conversion
  foundation and retains `/industries`.
- **D-026** accepts **Evidence in Motion**, the category **evidence-led innovation
  delivery partner**, and the promise **From complex ambition to accountable
  delivery**.
- **D-035** accepts the frozen **Signal Ledger system + Framework Relay logo
  hybrid** as the Phase 1 identity definition. The marks remain unregistered and
  trademark-not-cleared.
- **D-036** accepts the exact Phase 1 UX architecture package.

Some frozen source files retain historical status labels such as draft, pending,
or `founder_decision_pending`. Those labels are preserved byte-for-byte and are
subordinate to D-025, D-035, and D-036. In particular, `/industries` is retained.
No route is content-approved, release-active, sitemap-active, implemented, or
published by this package.

## Inventory baseline

| Authority set | Contracted count | Coverage artifact |
|---|---:|---|
| Canonical route definitions | 34 | [Foundation route coverage](foundation-route-coverage.csv) |
| Exclusion classes | 9 | [Foundation flow coverage](foundation-flow-coverage.csv) |
| Wayfinding records | 15 | [Foundation flow coverage](foundation-flow-coverage.csv) |
| Action contracts | 53 | [Foundation flow coverage](foundation-flow-coverage.csv) |
| UX acceptance tests | 46 | [Traceability](traceability.csv) |

## Artifact map

| Artifact | Role |
|---|---|
| [UI reference-design contract](UI_REFERENCE_DESIGN_CONTRACT.md) | Normative scope, evidence levels, naming, responsive/state/mode rules, interaction notes, content/asset constraints, handoff, and gates |
| [Foundation route coverage](foundation-route-coverage.csv) | Exact 34-route ID/path inventory, route-instance/template assignment, state/view/mode profiles, and content gates |
| [Foundation flow coverage](foundation-flow-coverage.csv) | Non-route flow families, all 53 actions, nine exclusions, and 15 wayfinding records with assigned references and recovery evidence |
| [Reference-template inventory](reference-template-inventory.csv) | Reusable screen/surface contracts and unique tool-neutral representative frame names |
| [Responsive, state, and mode matrix](responsive-state-mode-matrix.csv) | Named profiles for mandatory viewports, states, accessibility modes, degraded modes, the NFR-006 browser floor, WCAG 2.2 SC 2.2.1 time-limit branches, and evidence rules |
| Delivery stream profiles | `DS-S-HIGH`, `DS-S-MEDIUM`, `DS-S-LOW`, and `DS-S-SEMANTIC` in the same matrix, stating what evidence each stream owes. Stream presence itself is **not** assigned on a record: it is declared at the primitive in `component-primitives.csv.stream_presence`, computed at the template as the union over `primitive_dependencies`, and inherited unstored by routes and flows. Per-stream evidence is therefore a resolvable obligation rather than a column a producer fills in |
| [Design batch plan](design-batch-plan.csv) | Dependency-ordered later visual-production batches with single primary template/source ownership, separate supporting evidence, hard prerequisites, review obligations, and stop conditions |
| [Design-system implications](DESIGN_SYSTEM_IMPLICATIONS.md) | Semantic token/component guidance owned by the design-system specialist |
| [Component primitives](component-primitives.csv) | Machine-readable `PRIM-*` primitive inventory owned by the design-system specialist |
| [Traceability](traceability.csv) | Direct mapping to D-025/D-026/D-035/D-036, requirements, routes, exclusions, actions, 46 UX tests, and manual gates |
| [Validator](validation/validate-ui-reference-design.ps1) | Deterministic parsing, exact-set, reference, scope, claim, and gate checks |
| [Validation report](validation/validation-report.md) | Executed command, timestamp, counts, outcome, and limitations |
| [Producer inspection](producer-inspection.md) | Producer scope, completeness, feasibility, and unresolved-gate inspection |

## Status vocabulary

- **[ACCEPTED INPUT]** means an accepted upstream definition constrains this
  package; it does not mean the product or UI exists.
- **[PROPOSED UI CONTRACT]** means a reversible design-production requirement in
  this package, pending independent review and MA-024.
- **[UNRESOLVED GATE]** means exact copy, facts, provider behavior, ownership,
  rights, legal policy, or another material decision must not be inferred.
- **[FUTURE EVIDENCE]** means proof required from a separately authorized Figma
  or Stitch production and its later review.

## Boundary and non-claims

This package contains Markdown, CSV, and one PowerShell validator only. It does
not:

- create or approve a visual direction, screen, prototype, component library,
  `docs/ui/UI_SPEC.md`, application code, 3D asset, or production identity asset;
- activate a route, publish copy, certify WCAG conformance, or claim that a
  provider, person, mailbox, office, control, client result, or integration exists;
- authorize use of paid/licensed assets, the protected exterior GLB, external
  accounts, dependencies, migrations, Git operations, deployment, or launch; or
- turn a requirement, target, proposed control, prototype seed, or identity review
  specimen into public proof.

The later approved visual-production task must create the contracted reference
evidence and `docs/ui/UI_SPEC.md`, then pass independent design and accessibility
review before implementation can be considered.

## Normative accessibility, browser, and timing target

The future visual and implemented product target is **WCAG 2.2 Level AA for every
applicable full page and complete process, including represented third-party
steps**. This is a normative production and review target, not a statement of
current visual, implemented, tested, or certified conformance. Design references
and annotations alone cannot establish conformance.

`BP-NFR-006` is mandatory for every public, interactive, World, Quick Access, and
staff reference and every B01-B09 production batch. It requires the latest two
stable release families of Chrome, Edge, Firefox, and Safari current at the later
dated QA run; Safari on iOS 16.4 is the minimum legacy floor. Exact then-current
version numbers are deliberately deferred to that dated QA record. Safari/iOS
16.4 evidence must cover mobile layout, touch/input, virtual-keyboard, and safe-area
behavior. Clients below the floor or otherwise unsupported must receive the
equivalent semantic Quick Access journey without WebGL.

Every route, flow, template, profile, and batch also selects an explicit WCAG 2.2
SC 2.2.1 time-limit branch: `TL-REMOVABLE-ADJUSTABLE` (off or adjustable before
start), `TL-WARN-EXTEND` (warning at least 20 seconds before expiry plus a simple
extension of at least 10 times the default), `TL-EXCEPTION` (a documented,
criterion-supported exception accepted through the standards-exception gate), or
`TL-NOT-APPLICABLE` (no user time limit). Permitted data and the last authoritative
state must survive expiry where allowed, and accessible reauthentication must
return the user to preserved context. Exact product durations remain gated. No
current record selects `TL-EXCEPTION`; provider latency and system-response
timeouts cannot silently be treated as user time limits.

## Review and approval gates

1. Run the deterministic validator and complete producer inspection.
2. Obtain independent design and independent accessibility review. The producer
   cannot approve this package.
3. Resolve review findings within the UI maximum of three producer revisions.
4. Present **MA-024 — Phase 1 UI reference-design contract and
   foundation-surface coverage acceptance** to the founder. MA-024 accepts the
   frozen documentation package or requests a bounded revision only.
5. If MA-024 is accepted, obtain a separate explicit future manual gate before
   any external Figma or Stitch production/write. External-write authorization is
   currently false.
6. After separately authorized visual production, require independent design and
   accessibility review plus founder approval of the final visual direction.

MA-024 does not authorize application implementation, exact public/legal copy,
licensed assets, publication, complete Phase 1 acceptance, Git work, deployment,
or launch.

At the 2026-09-03 producer freeze, MA-024 and the separate external-write gate are
package proposals and are not yet recorded in root durable manual-action records.
Their trace rows therefore cite only package files. Root durable records may be
integrated only after clean independent design and accessibility reviews by an
authorized coordinator; that later integration does not alter this time-bounded
freeze provenance. External Figma/Stitch production/write authorization remains
false until its separate future manual gate is explicitly accepted.
