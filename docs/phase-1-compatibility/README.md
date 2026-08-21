# Phase 1 compatibility inventory

**Snapshot date:** 2026-07-19 (Asia/Karachi)
**Workflow state:** Revision 1 passed independent iteration-2 architecture and supply-chain review; ready for bounded founder review
**Approval state:** Not founder-approved; not a production target, compatibility exception, ADR, or implementation authorization

## Purpose

This bounded Phase 1 slice records the current runtime and dependency baseline and
creates a dated compatibility-graph skeleton across the frontend, 3D, backend,
database, QA, container, CI, and cloud-relevant boundaries. It distinguishes
registry-observed stable candidates from exact production locks. Every candidate
remains subject to a fresh graph recheck, an isolated compatibility wave,
independent review, and the applicable founder gate.

Revision 1 adds a canonical reference registry and deterministic resolver, a
normalized wave/checkpoint and gate model, and candidate-path supply-chain
obligations in response to the independent iteration-1 architecture and
supply-chain review. Independent iteration 2 verified that all four findings are
closed with no new blocker, HIGH, or MEDIUM finding. This makes the bounded slice
ready for founder review only; it does not approve a target, exception,
checkpoint, gate, implementation action, or the complete Phase 1 package.

The current application, package locks, Python environment, Compose file, tests,
and exterior GLB remain protected prototype evidence. They do not select future
production versions. No source, dependency, lock, migration, container, CI, cloud,
or external-system change is made by this slice.

## Authority and input state

Binding inputs are [D-004, D-014, D-020, and D-021](../../DECISIONS.md), the
[Constitution 2.0.0](../../.specify/memory/constitution.md), the
[project charter](../../PROJECT.md), and the approved
[system boundaries](../software-definition/01-system-boundaries.md). They require
newest mutually compatible stable technology, separately reversible upgrade
waves, PostgreSQL truth, Azure as the target platform, explicit performance and
recovery targets, and supply-chain governance.

The concurrent
[Phase 1 product requirements](../phase-1-foundation/01-product-requirements.md)
have passed their bounded independent reviews and remain under founder review;
they are not yet an approved requirements baseline.
Rows marked there as approved constraints are used only as a traceability view of
binding decisions. Proposed decomposition does not create new authority. No
approved production UX design exists yet; this inventory therefore records
browser, semantic fallback, and WebGL constraints without selecting UI behavior.

## Decision boundary

This slice may identify stable candidate generations when official evidence is
available. It does not:

- lock any exact production version or approve a compatibility exception;
- select an Azure subscription, tenant, region, SKU, capacity, API version, or
  cost envelope;
- prove PostgreSQL 18 availability in the founder-approved region;
- select a Python locking tool, GitHub Actions, container digest, or CI design;
- authorize application fixes, dependency installs, migrations, provisioning,
  paid activation, commits, pushes, or deployment;
- treat a configured tool, installed executable, or timed-out check as an
  operational capability.

## Artifact map

| Artifact | Purpose | Authority |
|---|---|---|
| [baseline-inventory.json](baseline-inventory.json) | Machine-readable observed runtimes, packages, locks, manifests, and capability states | Current evidence only |
| [compatibility-graph.json](compatibility-graph.json) | Machine-readable component and coupling-edge skeleton with candidates, constraints, tests, and rollback | Candidate analysis; lock selection deferred |
| [compatibility-controls.json](compatibility-controls.json) | Machine-readable waves, checkpoints, edge assignments, unsatisfied human gates, coverage, supply-chain obligations, and 44 candidate paths | Revision 1 control model; no gate or checkpoint is accepted |
| [reference-index.json](reference-index.json) | Canonical namespaces and deterministic local resolution for every nested reference in the machine artifacts | Evidence registry; unknown, duplicate, ambiguous, or unresolved references fail validation |
| [evidence-log-2026-07-19.md](evidence-log-2026-07-19.md) | Context7, official-documentation, registry, local-command, inference, and unresolved evidence | Dated evidence record |
| [blockers-and-obligations.md](blockers-and-obligations.md) | Human gates, compatibility blockers, failure modes, wave boundaries, rollback, and test obligations | Required handoff constraints |
| [validate.ps1](validate.ps1) | Deterministic structural, source-reconciliation, link, whitespace, candidate-channel, and secret-shaped-value validation | Validation tool |
| [validation-report-2026-07-19.md](validation-report-2026-07-19.md) | Executed validation evidence and limitations | Necessary but not sufficient for acceptance |
| [architecture and supply-chain review — iteration 1](reviews/architecture-supply-chain-review-iteration-1.md) | Independent review that identified three HIGH and one MEDIUM finding | Durable `REVISE` evidence retained unchanged |
| [architecture and supply-chain review — iteration 2](reviews/architecture-supply-chain-review-iteration-2.md) | Independent closure verification of revision 1 | `PASS`; all four findings closed and no new blocker/HIGH/MEDIUM finding |

## State vocabulary

- **Observed current:** resolved from a lock, installed environment, manifest, or
  harmless command on 2026-07-19.
- **Registry-observed candidate:** the authoritative registry reported a stable
  release; it is not yet proven against this repository.
- **Conditional candidate:** official evidence supports the generation, but a
  peer, regional, browser, security, cost, or human gate remains.
- **Configured:** a canonical inventory contains a definition.
- **Protocol-tested:** initialization and tool discovery succeeded.
- **Capability-tested:** the exact harmless operation needed for this slice
  succeeded.
- **Operational:** intentionally not claimed for any external integration here.
- **Deferred lock:** no exact target may enter a production manifest until the
  relevant wave reruns registry and official-doc evidence and passes its spike.

## Traceability

| Authority | Compatibility obligation | Evidence in this slice |
|---|---|---|
| D-004; OPS-004 through OPS-009; OPS-011 | Stable coupled graph, official evidence, no preview production target, deterministic locks, exceptions, defect-first sequencing, reversible waves | Baseline, graph, evidence log, blockers, validator |
| D-014; DATA-001; OPS-010 through OPS-012 | PostgreSQL truth, Azure target, immutable release references, no AWS target | PostgreSQL/Azure/container/CI nodes and regional gate |
| D-020; NFR-001 through NFR-007 | Core Web Vitals, 3D transfer, load, availability, RPO/RTO, browser floor, and later device-tier thresholds | Browser/QA edges and wave test obligations; no new numerical target invented |
| D-021; OPS-006, OPS-007, OPS-012, OPS-013 | SBOM/license evidence, human-reviewed majors, dated exception/recheck, immutable pins, lifecycle cadence | Deferred lock states, conditional TypeScript exception, CI/container blockers |
| R-003, R-004, R-005; OPS-008 | Stabilize hook-order, authorization, and database-configuration defects before modernization | Wave 0 prerequisite in the blockers document |

## Headline compatibility findings

1. The current React 18.3.1, R3F 8.18.0, and Drei 9.122.0 lock is internally
   aligned by published peer ranges. The registry-observed React 19.2.7, R3F
   9.6.1, Drei 10.7.7, and Three 0.185.1 candidates also align at the peer-range
   level, but repository behavior and visuals are untested.
2. React Router is a package-topology migration, not only a version bump. The
   current app uses `react-router-dom` 6.30.3; the latest `react-router` candidate
   is 8.2.0, while `react-router-dom` remains on the v7 compatibility line.
3. TypeScript 7.0.2 is stable and Microsoft documents an official side-by-side
   bridge: the TypeScript 7 compiler can coexist with the stable
   `@typescript/typescript6` API package that tools such as typescript-eslint can
   consume through an npm alias. The graph therefore keeps two unselected paths:
   a TypeScript 7 compiler plus TypeScript 6 API/tooling bridge spike, and a
   TypeScript 6-only compatibility exception. Both require diagnostic, editor,
   build, and lint parity; the exception also requires an ADR and quarterly
   recheck.
4. The Python requirements are unbounded and no standards-based lock exists.
   The installed environment is coherent under `pip check`, but it is not
   reproducible and `pytest-asyncio` is declared yet absent.
5. PostgreSQL 18.4 is current and Azure documents PostgreSQL 18 as GA generally.
   The approved region, feature/extension fit, capacity, cost, backup, restore,
   and major-upgrade evidence are still absent, so target selection remains gated.
6. Docker CLI and Compose executables are present, but the bounded capability
   check timed out. Container capability is unverified, not passing. No GitHub
   Actions or Azure/Bicep manifest exists in the observed repository.
7. Required future matrix families that are absent today are represented in the
   graph's `deferredFamilies` section: Redis, Azure AI/Search, Microsoft Graph,
   OpenTelemetry/Application Insights, NVIDIA, Blender/glTF tooling, CI actions,
   container images, and Bicep/API versions. These are explicit architecture
   gaps with owners, selection evidence, tests, rollback, and later Phase 1
   dependencies—not invented package or vendor selections.

## Revision 1 closure mapping

| Review finding | Producer remediation and validation evidence |
|---|---|
| ASC-HIGH-001 | `reference-index.json` defines 149 unique canonical entries and allowed namespaces. All legacy `DOC-*`, `CTX-*`, `PY-*`, and `PYPI-*` graph aliases were normalized to defined `OFF-*`, `CTX7-*`, `LOC-*`, and `REG-*` records. The validator checked 1,108 nested reference uses across 134 unique IDs with zero unknown, duplicate, ambiguous, or unresolved references. |
| ASC-HIGH-002 | `compatibility-controls.json` defines 14 unaccepted checkpoints and assigns all 27 graph edges exactly once. WAVE-04 moves React, React DOM, both React type packages, R3F, and Drei atomically; CP-04 forbids React 19 with R3F 8 or Drei 9. Retained Three 0.160.1 requires same-spike peer and behavior proof, and Router, Three, Zustand, and GSAP use smaller reversible waves. |
| ASC-HIGH-003 | Fifteen explicit human gates remain `unsatisfied` and cover exact locks, exceptions, npm, TypeScript, Azure/PostgreSQL, Python locking, container/CI, Azure AI/Search, Graph, NVIDIA, paid/external/credential writes, Git, migration, deployment, and residual risk. All 36 human-gated graph component/family records plus all 44 candidate paths have deterministic gate coverage; orphan count is zero. |
| ASC-MED-004 | Seven normalized blocking obligations cover advisory triage, licenses, SBOM, provenance/signature or immutable references, deterministic locks, exception ADRs, and quarterly rechecks. They map to all 44 candidate paths and all nine deferred families. Timed-out or missing scans remain blocking and every exception retains a null, unapproved ADR state. |

**Revision state:** independent iteration-2 `PASS`; all four findings closed; no
new blocker, HIGH, or MEDIUM finding; ready for bounded founder review only.

## Required continuation

Founder review must now accept, reject, or request revision of this bounded
compatibility inventory while leaving its 15 material human gates unsatisfied.
A later approved compatibility spike must still refresh official/registry
evidence and rerun the graph immediately before each isolated upgrade wave. No
exact lock, exception, gate, checkpoint, implementation action, or complete Phase
1 acceptance is created by the independent PASS.
