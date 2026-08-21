# 03 — Autonomous AI Development Workflow

## Purpose

This document defines the durable, phase-gated delivery workflow. Codex is the
orchestrator; the project MUST NOT add a separate workflow dashboard, database,
queue, runner, or control plane.

## Required Starting Point

For every repository-changing task:

1. Read `AGENTS.md` and `.specify/memory/constitution.md`.
2. Read `PROJECT.md`, `DECISIONS.md`, `PROJECT_STATE.yaml`, `TASKS.md`, and the
   relevant entries in `RISKS.md` and `MANUAL_ACTIONS.md`.
3. Read `docs/software-definition/README.md` and the relevant approved feature
   artifacts under `specs/`.
4. Confirm the bounded task contract: objective, exclusions, inputs, write scope,
   tools, deliverables, validation, evidence, acceptance criteria, revision limit,
   and human-approval conditions.
5. Confirm that the phase and prerequisite gates are open before changing files.

## Authority and Phase State

Use the complete authority order in the constitution. Approved decisions outrank
approved requirements; implementation evidence describes current behavior but
does not redefine approved intent.

`PROJECT_STATE.yaml` is the durable workflow state. Permitted phase states are:

- `not_started`
- `in_progress`
- `blocked`
- `awaiting_human`
- `in_review`
- `accepted`

Only founder approval moves a material phase to `accepted`. Status, evidence,
review findings, revision count, blockers, and next action MUST be synchronized to
the durable records before a handoff.

## Material Phase Loop

Every material phase follows:

`create -> validate -> inspect -> independent review -> revise -> validate again -> founder approval`

The producer cannot approve their own material output. Use independent specialists
for design, code, accessibility, security, QA, and deployment gates as applicable.
Maximum revisions are two cycles by default and three for brand, UI, motion, and
3D. When the limit is exhausted, record unresolved findings and request a founder
decision.

## Approval Gates

| Gate | When it applies | Required behavior |
|---|---|---|
| Start | Any repository-changing task | Read durable authority/state and define the bounded contract. |
| Conflict | Material sources disagree | Record the conflict, stop affected work, and request a founder decision; unrelated safe work may continue. |
| Definition | Product scope, architecture, workflow, API, auth, security, infrastructure, data, AI, publication, or production UI/3D | Complete and approve the relevant definition and Spec Kit artifacts before implementation. |
| Compatibility | Any version-sensitive stack, runtime, browser, cloud, CI, image, or API choice | Use Context7 plus official primary sources; prove the coupled compatibility graph and rollback before locking. |
| Design | Production UI, brand, motion, sound, or 3D | Create/reference approved Stitch/Figma/Blender design evidence before implementation. |
| Contract | Frontend/backend or external behavior depends on an interface | Approve and validate OpenAPI, WebSocket, event, data, or provider contracts first. |
| Implementation | Approved source work | Keep modernization waves separate from features and structural moves mechanical. |
| Verification | Any implementation or release work | Run scoped automated, live, failure-mode, visual, accessibility, security, performance, and recovery evidence. |
| Independent review | Every material output | Assign a reviewer independent of the producer and resolve findings within the revision limit. |
| Founder | End of every material phase | Present evidence in a click-based approval gate; continue only after approval. |
| Git/external | Branch, commit, push, PR, migration, paid activation, credential change, external design write, production promotion, or deployment | Obtain the explicit applicable approval immediately before the action. |

No application feature development begins before the complete Phase 1 definition,
SEO, identity, proof, content, UX/3D, technical, API/data, AI/security/privacy, QA,
deployment/cost, and dated compatibility package is accepted.

## Tool Order by Work Type

| Work type | Required order |
|---|---|
| Product/workflow definition | Durable authority -> research/evidence -> Spec Kit/software definition -> independent review -> founder approval |
| Version selection | Baseline graph -> Context7 identifier/docs -> official release/registry confirmation -> compatibility spike -> rollback -> lock |
| UI/brand/motion/3D | Approved Stitch/Figma/Blender reference -> implementation -> Playwright/visual/accessibility/performance review |
| API/data contract | Approved spec -> OpenAPI/event/data contract -> implementation -> contract/integration/negative tests |
| AI/provider work | Approved knowledge/data policy -> adversarial contract tests -> adapter -> residency/failover/refusal evidence |
| Database change | Backup -> migration rehearsal -> data/Alembic verification -> rollback/restore -> approved switch |
| Frontend behavior | Focused unit/build checks -> Playwright CLI -> live browser/MCP inspection when exposed -> axe/Lighthouse as applicable |
| Deployment | Prepared immutable candidate -> independent deployment review -> zero-traffic verification -> founder promotion -> rollback drill |
| GitHub publication | Local status/scope review -> required evidence -> explicit Git approval -> branch/commit/push/PR action |

## MCP Fallback Rule

Installed, configured, authenticated, protocol-tested, and capability-tested are
distinct states. Check the canonical VS Code MCP inventory before declaring a
server absent. When a configured MCP is not exposed by the current host, a safe
direct MCP/CLI fallback may be used only inside the task contract and without
reading or exposing secret values. Record the exposure gap and exact capability
tested.

## Technology Governance

- Production uses newest mutually compatible stable versions, not merely newest
  isolated packages.
- Preview, beta, RC, nightly, and experimental dependencies cannot be production
  requirements.
- A blocked newest major requires an approved ADR with exact evidence, rollback,
  and quarterly recheck.
- Weekly grouped dependency proposals and immediate security alerts require human
  review; major upgrades are never auto-merged.
- Every production release includes exact locks, SBOM, license inventory,
  immutable action/image pins, and no unresolved production-critical deprecation.

## Documentation and Handoff Rule

When workflow or product authority changes, synchronize the constitution,
`AGENTS.md`, root durable records, affected Spec Kit templates/artifacts, this
software definition, decisions, risks, manual actions, and changelog. A handoff
must distinguish local code health, UAT readiness, and launch readiness, cite the
evidence actually run, state limitations, and identify the next executable action.
