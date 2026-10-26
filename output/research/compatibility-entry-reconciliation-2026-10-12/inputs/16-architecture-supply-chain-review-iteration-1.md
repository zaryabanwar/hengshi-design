# Architecture and supply-chain review — iteration 1

**Review date:** 2026-07-19  
**Reviewer:** Independent architecture/software-supply-chain reviewer; no producer role  
**Decision:** **REVISE**  
**Scope:** Founder-review readiness of the completed producer inventory in
`docs/phase-1-compatibility/` only. This review made no producer, source,
manifest, dependency, lock, migration, container, CI, cloud, Git, or external
change and did not select an exact target or approve an exception.

## Evidence and validation

I read the governing records required by the review contract, every producer file
in this directory, and the machine-readable JSON records directly. I did not use
the stalled prior review as evidence and did not need optional external research;
the dated producer evidence is sufficient to judge this bounded handoff.

Executed from the repository root:

```powershell
& 'docs/phase-1-compatibility/validate.ps1'
```

Exact terminal result:

```text
PASS: JSON syntax: baseline and graph parsed.
PASS: Decision boundary: all top-level lock selection remains deferred.
PASS: Coverage: every baseline item has exactly one graph component.
PASS: Graph structure: components, edges, and required absent families include evidence, constraints, rollback, tests, ownership, and deferred-lock state.
PASS: Candidate channels: no pre-stable production target appears in targetCandidate data.
PASS: Integration truthfulness: version, protocol, scoped capability, timeout, authentication, and operational states remain distinct.
PASS: Text hygiene: no placeholders, tabs, trailing whitespace, or missing final newlines.
PASS: Markdown links: every local target resolves.
PASS: Secret-shaped scan: zero findings; matched values would be withheld.
PASS: Source reconciliation: all recorded source hashes match the working tree.
PASS: Observed state: runtimes, installed Python distributions, pip check, npm locks, declared plugin absence, and Compose tag reconcile.
VALIDATION PASSED: baselineItems=50; capabilities=6; components=50; edges=27; deferredFamilies=9; humanGates=4; candidateComponents=42; deferredComponents=8; candidatePaths=44.
```

The validator result is necessary but not sufficient. Its current structural
checks do not detect the unresolved evidence-reference, upgrade-wave, and
machine-readable gate/obligation defects below.

## Findings

### ASC-HIGH-001 — Evidence-reference IDs are not completely resolvable

**Evidence:** `compatibility-graph.json` record `HG-002` cites `DOC-010`, but no
`DOC-010` evidence record exists in the dated evidence log or another identified
producer evidence registry. The relevant defined evidence appears to be
`OFF-TS` and `OFF-TSESLINT`. The validator verifies that human-gate reference
arrays are non-empty, but it does not resolve their values. It likewise does not
cross-check every nested `evidence.refs`/`evidenceRefs` value against a declared
record, durable decision/manual-action ID, or resolvable local path and anchor.

**Impact:** A later lock-selection reviewer or implementer cannot deterministically
retrieve all evidence from the machine graph. This fails the explicit
resolvable-evidence acceptance condition and can conceal stale or mistyped support
for a material choice.

**Required remediation:** Replace `DOC-010` with the actual defined evidence ID(s)
or create a dated evidence record for it. Define the allowed reference namespaces
and add a machine-readable evidence index or deterministic cross-artifact resolver.
Extend validation over every reference-bearing field in the baseline, components,
edges, deferred families, and human gates, including nested references.

**Acceptance evidence:** The validator fails on an unknown, ambiguous, duplicate,
or unresolved evidence reference; a clean run proves zero unresolved references
and reports how many references were checked.

### ASC-HIGH-002 — The proposed React and 3D waves create an incompatible accepted checkpoint

**Evidence:** The inventory correctly records the coupled sets as React 18.3.1 +
R3F 8.18.0 + Drei 9.122.0 currently and React/DOM 19.2.7 + R3F 9.6.1 + Drei
10.7.7 for the candidate generation. `OFF-R3F` and the producer inference state
that R3F 8 is the React 18 line and R3F 9 is the React 19 line. Nevertheless,
`blockers-and-obligations.md` Wave 2 upgrades React, React DOM, types, and Router,
while Wave 3 upgrades R3F, Drei, Three, Zustand, and GSAP only after Wave 2 is
accepted. Wave 2 would therefore leave React 19 with the retained R3F 8/Drei 9
set, even though its rollback text requires a coherent React set and the graph
evidence says the 3D peers are React-major-coupled.

**Impact:** The staged plan is not independently reversible at a compatible
checkpoint. Builds or shallow route tests could pass while the protected 3D path
is peer-incompatible or behaviorally broken.

**Required remediation:** Redraw the waves so every accepted checkpoint closes the
React/R3F/Drei peer set. Either move React, React DOM, React types, R3F, and Drei
through one atomic compatibility wave, or document and prove a supported
transitional set before accepting an intermediate wave. Three.js may remain a
separate change only if the exact retained version satisfies every selected peer
and the same spike proves behavior. Keep Router topology and Zustand/GSAP in the
smallest reversible subwaves that do not violate a peer edge.

**Acceptance evidence:** The graph assigns each coupled edge to a wave/checkpoint;
each checkpoint has a fully satisfiable peer/runtime set, clean forward and reverse
install/build/browser/3D evidence, and no period in which React 19 is paired with
the current React-18-only R3F/Drei generation.

### ASC-HIGH-003 — Material human gates are not complete in the machine-readable graph

**Evidence:** The four `humanGates` records cover exact locks/exceptions,
TypeScript, Azure/PostgreSQL, and Python/container/CI. Material retained gates in
the approved review contract and producer blocker document are not represented as
explicit gate records: npm 12 versus a bundled-npm exception; Azure AI/Search,
Microsoft Graph, and NVIDIA provider entitlement/data/residency/DPA/security/cost
choices; paid activation and external/credential writes; Git, migration, and
deployment actions; and founder acceptance of residual material security,
privacy, compliance, cost, recovery, or irreversible risk. Deferred-family objects
set `humanApprovalRequired: true`, but do not reference a concrete gate record or
carry the gate state needed to prove that the decision remains closed.

**Impact:** Automation can count four apparently complete gates while omitting
decisions that governance requires humans to retain. Implementers could treat an
approved package choice as authority for vendor, data, cost, migration, or release
actions that were never approved.

**Required remediation:** Add explicit machine-readable gate records (or an
equally deterministic mapping to durable gate records) for every retained human
decision. Include scope, approver, state, evidence requirements, prohibited
actions before approval, and the durable decision/manual-action reference. Require
every `humanApprovalRequired` component/path/deferred family to reference at least
one applicable gate. Keep exact locks, exceptions, paid/external/Git/migration/
deployment actions, and residual-risk acceptance separate where their authority
differs.

**Acceptance evidence:** A validator cross-check shows complete coverage of every
human gate in the governing contract and blockers document, zero orphan
`humanApprovalRequired` records, and no gate marked satisfied without its durable
founder decision.

### ASC-MED-004 — Supply-chain obligations are not complete or enforceable as machine records

**Evidence:** The prose correctly retains advisory, SBOM, license, immutable-lock,
action-SHA/image-digest, provenance, and exception/recheck obligations, and it
truthfully records npm-audit timeout plus missing Python advisory/SBOM/license
evidence. The machine artifacts do not provide a complete normalized obligation
set linking all 42 candidate components/44 paths and nine deferred families to
advisory, license, SBOM, provenance/signature, exact-lock, exception-ADR, and
recheck requirements. The validator checks deferred lock state, record shape,
candidate channels, and selected capability truthfulness, but it does not fail
when one of these material supply-chain obligations or its status/evidence link is
absent.

**Impact:** Prose-only obligations can be lost during later target selection, and
a structurally valid graph can pass without complete supply-chain exit evidence.

**Required remediation:** Add normalized machine-readable supply-chain obligation
records with scope, owner, status, evidence references, required-before gate, and
failure/exception handling. Link every applicable candidate path and deferred
family to the required advisory, license, SBOM, provenance/immutable-reference,
and lock evidence. Model exceptions with ADR ID, approver, reason, expiry or
quarterly recheck date, and rollback. Extend the validator to enforce coverage and
truthful incomplete states without treating absent scans as passes.

**Acceptance evidence:** Validation reports complete obligation coverage for all
candidate paths and deferred families; timed-out/missing scans remain explicitly
blocking; every exception has a dated approved ADR and recheck; no exact lock is
selected before all applicable obligations pass.

## Bounded assessment by required area

| Area | Assessment |
|---|---|
| Inventory and graph counts | Structurally correct: 50 baseline items map one-to-one to 50 components; 27 edges, 9 deferred families, 6 capabilities, 4 current gate records, 42 candidate components, and 44 candidate paths parse and reconcile. Count correctness does not close ASC-HIGH-003 or ASC-MED-004. |
| Primary-source/stable-channel quality | Adequate for this dated candidate skeleton. Context7 capability is narrowly described; official project/vendor sources and authoritative registries are separated from inference. No preview, beta, RC, nightly, or experimental production candidate is present. Exact locks remain deferred. ASC-HIGH-001 prevents complete evidence traceability. |
| Node/npm/Vite/TypeScript/ESLint | Runtime and peer-floor reasoning is appropriately conditional. Node 24/npm 12, Vite/plugin, TypeScript bridge/exception, and ESLint/plugin migrations retain spikes and rollback. The TypeScript human choice is explicit; the separate npm choice needs machine-gate coverage under ASC-HIGH-003. |
| React/Router/R3F/Drei/Three | Candidate peer ranges are represented and Router is correctly treated as a package/import topology change. The implementation waves are not coherent because the React and R3F/Drei major transition is split across accepted checkpoints; ASC-HIGH-002 is blocking. |
| Python/FastAPI/Starlette/Pydantic/SQLAlchemy/Alembic/Psycopg | The installed state, declared/installed divergence, Python lock absence, Pydantic Core/Psycopg coupling, and database rehearsal needs are truthfully recorded. Candidate metadata is not overstated as application proof. Fresh locked-environment, contract, auth-negative, migration, advisory, SBOM/license, and rollback evidence correctly remains pending. |
| PostgreSQL/Azure | PostgreSQL 18.4 is correctly conditional on founder-approved Azure region, feature/extension, HA, quota, residency, cost, backup/restore, and migration evidence. General Azure GA is not misreported as regional proof. The machine gate must be expanded to cover all provider/data decisions under ASC-HIGH-003. |
| Capabilities and timeouts | PASS for truthfulness: configured, authenticated, protocol-tested, capability-tested, and operational are kept distinct. Docker/Compose and npm-audit timeouts are failures/unresolved evidence, not passes; Playwright version reporting is not promoted to browser-flow capability. |
| Supply chain | Exact locks are deferred; floating container/CI references, missing Python lock, advisory gaps, SBOM/license/provenance, immutable image/action references, and exception rechecks are acknowledged. Machine coverage/enforcement remains incomplete under ASC-MED-004. |
| Rollback and failure tests | Strong bounded prose coverage across runtime, React/Router, 3D, backend, database, QA, container/CI/cloud, and restore. Rollback is source/data-aware rather than lockfile-only. React/3D wave boundaries must be repaired under ASC-HIGH-002. |
| Retained human gates | The report does not approve exact locks, exceptions, TypeScript/npm selection, Azure/PostgreSQL region/SKU/features/cost/security/recovery, Python lock or CI/container architecture, provider/data/residency/entitlements, paid/external/Git/migration/deploy actions, or residual material risk. Machine representation is incomplete under ASC-HIGH-003. |

## Decision and next gate

**REVISE.** There are three unresolved HIGH findings and one unresolved MEDIUM
finding. The producer validator passes, but the inventory is not founder-review
ready under the supplied acceptance rule. The producer should revise only the
compatibility artifacts and validator, rerun validation, and return them for
independent review iteration 2. Exact target selection and every retained human
gate remain closed. This report does not approve the compatibility slice, the
complete Phase 1 package, implementation, or any external action.
