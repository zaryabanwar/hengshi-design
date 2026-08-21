# {{ Feature Name }} — Tasks

## Status and Authority

| Field | Value |
|---|---|
| Status | Draft |
| Plan | `specs/{{ number }}-{{ slug }}/plan.md` |
| Current phase | |
| Author/producer | |
| Independent reviewers | |
| Founder approver | |
| Created | {{ date }} |
| Last updated | {{ date }} |
| Maximum revision cycles | 2; use 3 only for brand, UI, motion, or 3D |

## Bounded Contract

- **Objective**: _Concrete outcome._
- **Exclusions**: _Explicit non-goals and protected files/systems._
- **Required inputs**: _Approved specs, designs, decisions, and evidence._
- **Allowed tools/write scope**: _Project-scoped paths and safe external access._
- **Human gates**: _Founder, Git, migration, external write, paid activation, or
  deployment approvals required._

## Prerequisites

- [ ] Durable authority and current phase read
- [ ] Spec, research, data model, contracts, and plan approved
- [ ] Dated compatibility matrix approved for version-sensitive work
- [ ] Stitch/Figma/Blender reference approved for production design work
- [ ] Conflicts, risks, assumptions, and manual inputs recorded
- [ ] Baseline evidence exists before modernization

## Dependency-Ordered Work

Use `[P]` only for tasks with disjoint files and no unmet data/state dependency.
Keep baseline fixes, structural moves, upgrade waves, feature work, and release
actions separate.

### Task T001 — {{ Description }}

- **Status**: Not started
- **Priority**: Must
- **Objective/exclusions**: _Bounded result and non-goals._
- **Dependencies**: None
- **Owner/write scope**:
  - Create: `path/to/file`
  - Modify: `path/to/file`
  - Protected: `path/or/system`
- **Implementation notes**: _Reference approved plan/contract; no invented choice._
- **Acceptance criteria**:
  - [ ] _Observable criterion._
- **Validation and evidence**:
  ```powershell
  # Exact commands
  ```
- **Failure/rollback**: _How to restore the previous trusted state._
- **Independent reviewer**: _Role/agent separate from producer._
- **Human approval condition**: _State the exact gate._

## Required Verification Tasks

Add only applicable tasks, but do not omit an applicable gate:

- [ ] Backend import, typing, contract, integration, and negative-authorization tests
- [ ] Frontend unit/build, Playwright desktop/mobile/keyboard/reduced-motion and
  WebGL/asset-failure tests
- [ ] axe/WCAG 2.2 AA and Lighthouse/performance-budget evidence
- [ ] SEO prerender, canonical, metadata, status, sitemap, robots, schema, link,
  draft-isolation, and release-checksum evidence
- [ ] AI grounding/source/refusal/injection/residency/timeout/failover evidence
- [ ] Data retention/deletion/backup-tombstone and privacy evidence
- [ ] 3D loading, visual, color, interaction, memory, FPS, LOD, and fallback evidence
- [ ] Database migration/downgrade/backup/restore/Alembic/data-preservation evidence
- [ ] Immutable build, SBOM, license, candidate, rollback, and deployment evidence

## Review and Revision Log

| Cycle | Reviewer | Findings | Revision tasks | Revalidation | Outcome |
|---|---|---|---|---|---|
| 1 | | | | | |

## Completion Criteria

- [ ] All tasks and acceptance criteria complete
- [ ] No out-of-scope application or user-owned file changed
- [ ] Compatibility graph and deterministic locks verified where applicable
- [ ] All applicable validation and failure/rollback evidence passed
- [ ] Independent review has no unresolved critical finding
- [ ] Decisions, state, risks, manual actions, and changelog synchronized
- [ ] Founder click-based phase approval recorded
- [ ] Separate explicit approval obtained before any Git, migration, external-write,
  paid-service, credential, production-promotion, or deployment action
