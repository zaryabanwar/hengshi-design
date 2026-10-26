# {{ Feature Name }} — Tasks

## Status and Authority

| Field | Value |
|---|---|
| Status | TODO |
| Product/definition | v1; D-069 |
| Plan | `specs/{{ number }}-{{ slug }}/plan.md` |
| Current phase | |
| Author/producer | |
| Independent reviewers | |
| Founder approver | |
| Created | {{ date }} |
| Last updated | {{ date }} |
| Correction policy | D-097: no numeric cap; diagnose repeated failures; escalate material decisions only |

D-097: tasks deliver one assigned increment, then stop. Unfinished future 3D and
launch evidence are not universal code prerequisites. Preserve all agreed scope
in its later increments; assess actual coupled dependencies of the current work.

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
Use only TODO/DOING/DONE/BLOCKED for task status; DONE requires relevant tests
and an applicable approved commit. Preserve accurate technical/history versions.
Follow D-069's latest mutually compatible stable full graph; newest observations
alone do not select versions. D-068 defers deployment/provider/region/cost tasks;
do not infer Azure/AWS selection or a Microsoft 365 setup prerequisite.

### Task T001 — {{ Description }}

- **Status**: TODO
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
- **Independent review**: _Required for material design, money/security/external-system work or when asked; otherwise not applicable._
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
- [ ] Required independent review has no unresolved material finding, or is not applicable with reason
- [ ] Owning product references and compact checkpoint updated; no routine review narrative
- [ ] Relevant tests pass and approved commit exists before DONE; launch gates listed separately
- [ ] Separate explicit approval obtained before any Git, migration, external-write,
  paid-service, credential, production-promotion, or deployment action
