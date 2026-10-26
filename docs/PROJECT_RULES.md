# Project Rules — Hengshi Design

These rules apply to all agent hosts. D-097 (2026-10-25) is current delivery
authority: brand/shared foundations -> complete 2D platform -> full 3D -> launch.
All agreed requirements remain; the former whole-Phase-1 build gate is superseded.

## Rule 1 — Apply the Durable Authority Order

Use the authority hierarchy in `.specify/memory/constitution.md`:

1. current explicit founder approval recorded durably;
2. the constitution and project safety/governance rules;
3. approved decisions and compatibility-exception ADRs;
4. approved requirements and feature specifications;
5. approved software-definition and design artifacts;
6. current code, tests, generated artifacts, and live observations as evidence;
7. unreconciled active documents, consolidation files, research, drafts, and chat
   as supporting evidence only.

Approved decisions outrank approved requirements. A newer date alone does not make
a document authoritative.

## Rule 2 — Record Assumptions and Stop for Material Choices

Do not invent technical, business, branding, naming, scope, evidence, legal, or
architectural decisions. A missing detail may be derived only when the result is
unambiguous, reversible, within approved scope, and recorded in the active plan or
state. Stop and request a founder decision when the choice materially changes
scope, risk, cost, public claims, data handling, architecture, or approval rights.

## Rule 3 — Conflicts Are Scoped Stop Events

A material conflict stops the affected work. Record the sources and impact in
`RISKS.md` or `MANUAL_ACTIONS.md`, obtain a founder decision, and log the outcome.
Unrelated safe work may continue. Never silently resolve a conflict by relying on
document age, implementation convenience, or an industry default.

## Rule 4 — Decisions and State Are Durable

- `DECISIONS.md` is the operational index of approved and pending decisions.
- `docs/decisions-log.md` holds detailed decision records and ADR evidence.
- `PROJECT_STATE.yaml` is the phase-state source of truth.
- `TASKS.md` is the global task index and links feature-level tasks without
  duplicating them.
- `RISKS.md`, `MANUAL_ACTIONS.md`, and `CHANGELOG.md` keep execution resumable.

## Rule 5 — Definition Before Build

Before implementation, read the assigned increment's approved scope, relevant
Spec Kit artifacts, visual references, contracts and coupled compatibility.
Unfinished future 3D definitions and deferred launch work do not block unrelated
2D delivery. Reuse accepted baselines; no full definition restart.

## Rule 6 — Latest Mutually Compatible Stable Technology

Use the newest mutually compatible stable releases across the approved technology
families. Evaluate coupled packages, runtimes, browsers, cloud services, and
deployment targets as a graph. Use Context7 first, confirm with official primary
documentation and registries, record the query date and rollback, then lock exact
versions reproducibly.

Preview, beta, RC, nightly, or experimental dependencies cannot be production
requirements. When the newest stable major is blocked, use the newest proven
compatible stable release only under an approved ADR with exact evidence and a
quarterly recheck.

D-069 applies this rule to every coupled tool/library/framework/runtime and
exporter, not just the main technology families. Individually newest releases
are observations; peer ranges alone are not proof. Resolve, test, independently
review and reproducibly lock the complete stable set. This first product and
current production definition are v1; retain factual technical/schema versions
and historical evidence identifiers rather than renaming them as product releases.

D-068 defers deployment, provider, region and cost planning. Azure and AWS remain
candidates, with lowest feasible cost/free services preferred when planning
resumes. Neither is selected by an older document. Outlook/Teams remain intended
without a Microsoft 365 prerequisite; verify each required account/API capability
separately. Approved staff identity and AI privacy restrictions remain in force.
D-070 establishes Europe as the first market, not a European office or cloud region.

## Rule 7 — Design, SEO, and Accessibility Before UI

Production UI or material UI/UX changes require an approved Stitch or Figma
reference. Every indexable route must provide complete semantic HTML before
JavaScript. Quick Access must provide an equivalent WCAG 2.2 AA journey without
WebGL. Design output is a reference; production code remains in the approved React
and Tailwind families unless a separate decision changes them.

## Rule 8 — Phase Loop and Independent Review

Deliver one assigned outcome, validate/inspect it, correct defects, report and
stop. Independently review coherent material designs, money/security/external-
system changes, or when requested; do not review every routine edit separately.
No hard two/three-cycle cap: continue safe in-scope corrections with evidence of
progress, change diagnosis on repeated failure and escalate actual material
choices or missing inputs. Preserve action approvals and provider retry limits.
The founder supplies the next work-chat prompt from the discussion session.

## Rule 9 — Verification Is Proportionate and Repeatable

Frontend changes require focused tests, builds, Playwright validation, and
accessibility/visual checks for affected surfaces. Backend changes require import,
typing, contract, integration, and negative-authorization evidence as applicable.
Database, 3D, and deployment changes require migration, rollback, failure-mode,
and recovery evidence appropriate to their risks.

Tests exercise actual behavior against approved requirements and verified
external contracts, using focused unit, integration and browser layers. Include
failure and boundary cases proportionate to risk; do not copy implementation
logic into expected results. Documentation phrase/count/hash checks are artifact
integrity only; do not add brittle prose tests for ordinary edits or report them
as product correctness. An isolated schema check or OpenAPI declaration cannot
prove the application enforces it. Keep artifact and runtime evidence separate.

## Rule 10 — Approval-Bound Actions Stay Gated

Do not create branches, commits, remotes, migrations, paid activations, credential
changes, external design writes, production promotions, deployments, or other
irreversible actions without their explicit applicable approval. Reversible,
project-scoped documentation and implementation work may proceed only inside an
approved task contract.

## Rule 11 — MCP Status Must Be Truthful

The canonical inventory is `%APPDATA%\Code\User\mcp.json`. Installed, configured,
authenticated, protocol-tested, and capability-tested are different states. If a
configured server is not exposed in the active host, use a documented safe direct
fallback when permitted and report the exposure gap. Never expose secrets.
