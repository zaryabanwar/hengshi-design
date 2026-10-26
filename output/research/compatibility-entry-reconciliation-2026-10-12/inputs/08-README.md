# Phase 1 compatibility inventory — v1

## Current authority and dated evidence

The complete production graph remains unselected. Read [governance](../../AGENTS.md),
[decisions](../../DECISIONS.md) and the [reconciliation map](../software-definition/04-reconciliation-map.md)
first. Select the latest mutually compatible stable set across all coupled tools,
frameworks, libraries, runtimes, renderers/exporters, browsers and databases.
Independently newest registry versions and satisfying peer ranges do not prove
compatibility. Resolve, qualify, independently review and reproducibly lock the
complete set before MA-013 acceptance and separately authorized application adoption.

## Accepted bounded exceptions

- [D-072](../../DECISIONS.md#d-072--bounded-gensync-development-and-ci-lint-exception)
  permits only `gensync 1.0.0-beta.2` in the isolated React development/CI lint
  evaluation, under its five reviewed conditions. It expires 2027-01-05. Actual
  conformance, integrity/provenance, licences/advisories, deterministic resolution
  and exclusion from every deployed execution/artifact path remain obligations.
  A devDependency label proves no exclusion. This permits no production runtime,
  general Babel/build use, other prerelease or peer/parity waiver.
- [D-077](../../DECISIONS.md#d-077--temporary-evaluated-three-renderer-exception)
  permits only root `three 0.184.0` with `@types/three 0.184.1` as the temporary
  evaluated pair for the eventual complete stable graph. The [exact conditions](THREE_STABLE_EXCEPTION_PROPOSAL.md)
  retain strict declarations, separate nested-renderer evidence, full graph,
  supply-chain, rollback and adoption gates. Recheck by 2027-01-07, before adoption
  and on a relevant stable fix; continued use then needs a fresh decision.

Neither exception accepts a production graph, changes application dependencies
or waives complete qualification. Do not reopen these already-settled choices.
D-068 defers hosting/provider/region/SKU/cost planning: Azure and AWS remain
candidates. Existing Entra/AI privacy constraints and Outlook/Teams intent remain,
without requiring Microsoft 365. Native local operation requires no Docker.

## Controlling evidence by subject

| Subject | Source and scope |
|---|---|
| Frontend, renderer and lint candidates | [Frontend/3D appendix](refresh-evidence-2026-10-04.md) owns the strict resolver failures, official lint/native alternatives, TypeScript bridge/React/LSP probes and coupled declaration/build/browser results. Each study retains its failures, warnings and exact bounded review; successful fixtures select no full graph. |
| Renderer exception basis | [Published blocker](refresh-evidence-2026-10-04.md#published-renderer-blocker-and-exception-proposal--2026-10-07) and the [D-077 proposal review](reviews/three-stable-exception-v1-2026-10-07.md) retain the evidence for the accepted temporary pair. They grant no application upgrade or broader renderer exception. |
| Frontend inventory, notices and provenance | [Supply-chain observations](refresh-evidence-2026-10-04.md#matched-candidate-supply-chain-observations--2026-10-06), [full installed notice reads](refresh-evidence-2026-10-04.md#full-installed-notice-reads-and-broader-root-inventory--2026-10-08) and [supplemented bundled inventory](refresh-evidence-2026-10-04.md#supplemented-virtual-bundled-inventory--2026-10-08) own the subsequent exact-artifact studies and reviews. The bounded supplement does not turn the original failed npm CLI SBOM into a success. Empty advisory/import lists establish no universal security or deployed-exclusion proof. |
| Backend candidate closure and native qualification | [Backend appendix](backend-evidence-2026-10-04.md) owns the current metadata closure, earlier isolated trial and [preferred-client result/wheel notices](backend-evidence-2026-10-04.md#preferred-client-native-result-and-wheel-notices--2026-10-09). Native library and bounded results reviews do not prove Hengshi API/OIDC/database behavior or select production clients. |
| Identity distribution and rights evidence | [Staff identity comparison](backend-evidence-2026-10-04.md#maintained-staff-identity-client-comparison--2026-10-08) and [distribution observations](backend-evidence-2026-10-04.md#staff-identity-distribution-licences-and-publishing-evidence--2026-10-09) retain source, licence and publishing evidence plus its scoped review. Package identity, archive integrity and available attestation metadata are distinct from verified build provenance and legal clearance. |
| Backend roles and advisory scope | [Role/metadata proposal](backend-evidence-2026-10-04.md#proposed-backend-dependency-roles--2026-10-09) and [dated advisory observation](backend-evidence-2026-10-04.md#separate-dated-advisory-observation) retain conditional identity/migration/test reachability and exact lookup scope. They select no production split and qualify no separately deployed environments. |
| Machine artifacts and reversible waves | The [artifact map below](#artifact-map) preserves the dated baseline, graph, controls, reference registry and original reviews. July provider mappings and candidate observations are historical inputs, subordinate to current decisions. |

The appendices own detailed commands, inputs, source associations, frozen review
receipts and remaining limitations. This index does not duplicate a live evidence
journal. Receipts apply to their exact snapshots; current entry-page edits do not
replace their hashes or expand PASS to new inputs.

## Remaining selection and acceptance work

Complete the coupled stable graph and all required platform/embedded/deployed
inventories; qualify applicable declarations, build/runtime/browser/database and
editor/CI boundaries; establish D-072 isolation, exact licence/notice obligations,
advisory disposition and provenance; produce reproducible locks plus reversible
wave/checkpoint/rollback criteria. Conditional and deferred families retain their
selection and approval gates. No runtime result, legal clearance or implementation
is inferred from a schema, metadata model, source association or synthetic fixture.

MA-013, full Phase 1 independent/founder acceptance and applicable adoption
permissions remain. Protect the application, its locks/environments and the Atlanta
asset. No installation, dependency upgrade, provider operation, paid activation,
commit, push or deployment is authorized by this entry.

The [complete preceding entry](../../output/research/compatibility-entry-consolidation-2026-10-09/README.before.md)
is preserved with original links interpreted from this directory. The inventory
and later dated observations below retain their historical identities and scope;
their old awaiting-approval/provider statements are not new founder requests.
No machine artifact, exception condition, evidence appendix or review receipt is
changed by this navigation consolidation.

## July inventory and review context

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
[constitution](../../.specify/memory/constitution.md), the
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

## Later React declaration diagnostic evidence — 2026-10-06

The [React-specific probe](refresh-evidence-2026-10-04.md#typescript-react-declaration-diagnostic-probe--2026-10-06)
extends the earlier plain-TypeScript evidence with eight finite TSX cases using
registry-pinned React/DOM declarations. Native7 and API6 compiler/in-process service
match their diagnostic and accept/reject oracles; invalid numeric CLI exits still
differ. This is not React runtime, compiler transform, native LSP/editor, bundler,
full stable graph or adoption proof. Exact observations and protection guards are
retained separately; independent review and integrated/founder acceptance remain.

The [independent React diagnostic review](reviews/typescript-react-diagnostics-v1-2026-10-06.md)
records bounded PASS for these exact observations. The inspected bytes are
preserved in the [React evidence directory](../../output/research/typescript-react-parity-2026-10-06/);
this later reference is outside the receipt. Broader parity and adoption remain held.

## Later native language-server evidence — 2026-10-06

The [native LSP probe](refresh-evidence-2026-10-04.md#native-typescript-language-server-probe--2026-10-06)
exercises the existing 7.0.2 executable through the public stdio protocol, using
the unchanged eight React fixtures. Its diagnostic codes match their earlier
CLI/API6/in-process-service observations; one in-memory prop correction clears
the error and restoring it reports it again. This is finite language-server
evidence, not editor UI, build, full protocol/graph or adoption proof. The first
client's unsupported configuration registration and the corrected session are
both preserved. Protected application/candidate locks and models are unchanged.
Independent review and integrated/founder acceptance remain required.

The [independent native LSP review](reviews/typescript-native-lsp-v1-2026-10-06.md)
records bounded PASS after reproducing all eight fixture diagnostics and both
in-memory transitions. The [exact reviewed bytes](../../output/research/typescript-native-lsp-2026-10-06/)
remain preserved; this later reference is outside them. The initial client failure,
exit EOF log and producer-reported Context7 limit remain visible. No editor/build,
complete graph, adoption or founder acceptance follows.

## Later coupled frontend candidate evidence — 2026-10-06

The [isolated candidate](refresh-evidence-2026-10-04.md#coupled-frontend-candidate-and-declaration-gate--2026-10-06)
resolves and installs with strict peer/engine checks, but does **not** pass its
strict declaration gate. API6 and native7 both report incompatible SVG/TGA loader
declarations in three-stdlib 2.36.1 against @types/three 0.186.0. A separate public
type-import control reproduces the same two codes. Successful installation is
not evidence of complete compatibility, and no runtime loader failure is claimed.

The candidate uses portable research-only Node 26.10.0/npm 12.2.0; installed
machine runtimes and application dependencies remain unchanged. Vite/build/browser
execution is held at the failed type gate. Initial fixture/control mistakes and
corrected observations are preserved, as are unequal invalid CLI exits and raw
diagnostic messages. D-072 remains lint-only, with execution/exclusion and full
conformance unproven here. Independent review, latest-compatible graph selection,
supply-chain clearance, MA-013 and integrated/founder acceptance remain required.

The [independent declaration-gate review](reviews/frontend-candidate-declaration-gate-v1-2026-10-06.md)
records bounded PASS for accuracy of this failed-candidate evidence after
reproducing all six CLI controls. The candidate remains rejected at the strict
type gate. All 382 frozen inputs and 78 protected inputs matched; the
[exact reviewed snapshots](../../output/research/frontend-build-evaluation-2026-10-06/)
remain preserved. This later reference lies outside the receipt and creates no
build/browser, complete graph, adoption or founder acceptance.

## Later matched Three candidate evidence — 2026-10-06

The [matching-runtime candidate](refresh-evidence-2026-10-04.md#matched-three-candidate-build-and-browser-evidence--2026-10-06)
uses Three 0.184.0 with @types/three 0.184.1 while retaining the other direct
frontend pins. Both strict checker paths accept the valid fixture and public
loader control, and reject the invalid prop. An actual default Vite build and
finite built-page interactions also pass. This is an evaluated fallback, not
selection of an older production renderer or acceptance of the complete graph.

A fresh npm12 lockfile-only attempt failed at optional bundled registry-tarball
extraction. Normal installation and a separate fresh frozen installation succeed
with npm's default policy intact; no broad remote, peer or script override is
used. Keep that distinction and the initial Chrome-channel failures visible.
The actual build's large-chunk warning, two runtime Clock deprecation warnings,
existing browser/tool version mismatch and all broader evidence limits remain.
Independent review and D-069's dated exception/rollback/recheck and founder
selection gates are still required; D-072 remains lint-only.

The [independent matched-candidate review](reviews/frontend-three-remedy-evaluation-v1-2026-10-06.md)
records bounded PASS without a correction: six checker controls, two native type
comparisons, the default Vite build and finite built-page browser interactions
reproduce. Reviewer build artifacts also match the producer bytes. The
[exact reviewed snapshots](../../output/research/frontend-three-remedy-evaluation-2026-10-06/)
remain preserved; this later navigation reference is outside that receipt.
Warnings, existing browser/tool mismatch, complete graph and D-069 selection/
exception/rollback/recheck gates remain. Separate later supply-chain observations
are outside this review; no application adoption or Phase 1 acceptance follows.

## Matched-candidate supply-chain follow-up — 2026-10-06

The [separate read-only follow-up](refresh-evidence-2026-10-04.md#matched-candidate-supply-chain-observations--2026-10-06)
records zero reported known advisories, an installed-tree SPDX inventory matching
233 package/version pairs plus the private fixture root, and npm12 signature/
available-attestation verification with no reported invalid or missing entries.
Only 78 attestation records are emitted; gensync has no emitted attestation record.
These observations do not clear all provenance, installed-file integrity or D-072.

The all-platform virtual SBOM fails on six missing dependencies beneath optional
oxide WASM; the successful installed-tree inventory does not replace that failure.
Licence declarations include non-MIT terms and one missing declaration; retained
top-level licence texts are evidence, not legal clearance or complete bundled
notice coverage. No dependency repair or production selection is made. Separate
independent review, complete graph and founder acceptance remain required; this
follow-up is outside the preceding compiler/build/browser receipt.

The [independent supply-chain review](reviews/frontend-supply-chain-v1-2026-10-06.md)
records bounded evidence-accuracy PASS without revision. Saved command outcomes,
package/SBOM identities, available attestation correlations and retained top-level
licence texts reproduce; the reviewer did not rerun remote CLI verification.
The [inspected snapshots](../../output/research/frontend-supply-chain-2026-10-06/)
remain preserved. This later reference is outside those reviewed bytes and grants
no full-platform inventory, recursive notice completeness, cryptographic/security/
legal clearance, D-072 conformance, production selection or Phase 1 acceptance.

The subsequent [optional WASM bundled-dependency inspection](refresh-evidence-2026-10-04.md#optional-wasm-bundled-dependency-inspection--2026-10-06)
is producer evidence outside that review. The cached oxide WASM archive matches
the exact candidate-lock integrity and contains all six packages reported missing
by the virtual SBOM, at versions satisfying their declared ranges. The retained
Arborist observation still reports missing virtual records. This identifies a
bundled-metadata inventory gap; it does not repair the failed SBOM or prove WASM
execution, complete platform inventory, recursive rights/provenance, stable graph
selection or independent acceptance. Earlier candidate inputs remain unchanged.

## Current backend candidate recheck — 2026-10-08

The [new coupled Windows study](backend-evidence-2026-10-04.md#current-registry-and-coupled-windows-study--2026-10-08)
resolves the newer direct FastAPI and SQLAlchemy candidates, including the coupled
Pydantic 2.14.0/core 2.50.0 pair, without installation. Saved registry and
marker/extras inspection support metadata closure only. The dated earlier graph
and initial registry receive-cap failure remain preserved. The [132-input bounded
independent review](../../output/research/backend-current-review-2026-10-08/independent-review-backend-current-v1.json)
passes for saved metadata closure, release/source observations and migration-claim
accuracy. These later navigation references are outside its frozen bytes. No wheel
authenticity, native/API/database proof, complete graph selection, application
upgrade, production lock or Phase 1 acceptance follows.
