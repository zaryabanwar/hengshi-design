# Architecture and supply-chain review — iteration 2

**Review date:** 2026-07-19
**Reviewer:** Independent architecture/software-supply-chain reviewer; no producer role
**Decision:** **PASS**
**Scope:** Final independent verification of producer revision 1 against
`ASC-HIGH-001`, `ASC-HIGH-002`, `ASC-HIGH-003`, and `ASC-MED-004`. I inspected
the revised producer prose and machine artifacts directly. I made no producer,
source, manifest, dependency, lock, migration, container, CI/cloud, governance,
Git, or external-system change and did not select or approve a target, exception,
gate, checkpoint, vendor, region, cost, or implementation action.

## Validator evidence

Executed from the repository root:

```powershell
& 'docs/phase-1-compatibility/validate.ps1'
```

Exact result:

```text
PASS: JSON syntax: baseline, graph, controls, and reference index parsed.
PASS: Decision boundary: all top-level lock selection remains deferred.
PASS: Reference resolution: checked 1108 uses across 134 unique ids; zero unknown, duplicate, ambiguous, or unresolved references.
PASS: Coverage: every baseline item has exactly one graph component.
PASS: Graph structure: components, edges, and required absent families include evidence, constraints, rollback, tests, ownership, and deferred-lock state.
PASS: Candidate channels: no pre-stable production target appears in targetCandidate data.
PASS: Wave/checkpoint model: 14 unaccepted checkpoints, all 27 edges assigned once, atomic React/R3F/Drei transition enforced, and Router/Three/Zustand/GSAP remain reversible.
PASS: Human gates: 15 explicit gates remain unsatisfied; all human-gated components, 44 candidate paths, and deferred families are covered with zero orphans.
PASS: Supply chain: 7 blocking obligations cover all 44 candidate paths and all 9 deferred families; timed-out or missing scans remain blocking and no exception ADR is approved.
PASS: Integration truthfulness: version, protocol, scoped capability, timeout, authentication, and operational states remain distinct.
PASS: Text hygiene: no placeholders, tabs, trailing whitespace, or missing final newlines.
PASS: Markdown links: every local target resolves.
PASS: Secret-shaped scan: zero findings; matched values would be withheld.
PASS: Source reconciliation: all recorded source hashes match the working tree.
PASS: Observed state: runtimes, installed Python distributions, pip check, npm locks, declared plugin absence, and Compose tag reconcile.
VALIDATION PASSED: baselineItems=50; capabilities=6; components=50; edges=27; deferredFamilies=9; referenceIndexEntries=149; referenceUses=1108; unresolvedRefs=0; waves=14; checkpoints=14; edgeAssignments=27; humanGates=15; humanGateOrphans=0; supplyChainObligations=7; deferredFamilyCoverage=9; candidateComponents=42; deferredComponents=8; candidatePaths=44.
```

## Finding closure

| Stable ID | Result | Independent verification |
|---|---|---|
| `ASC-HIGH-001` | **Closed** | `reference-index.json` contains 149 unique canonical entries and explicit namespace/resolution rules. The resolver traverses nested reference fields and checked 1,108 uses across 134 used IDs with zero unresolved result. `DOC-010` and the former `DOC-*`, `CTX-*`, `PY-*`, and `PYPI-*` aliases are absent from producer reference uses. Validator predicates fail unknown, duplicate, namespace-ambiguous, missing-target, missing-record, or duplicate-use defects. |
| `ASC-HIGH-002` | **Closed** | `compatibility-controls.json` has 14 ordered, `not_authorized` waves and 14 `unaccepted` checkpoints; every graph edge has exactly one of 27 assignments. `WAVE-04` atomically contains React, React DOM, both React type packages, R3F, and Drei. `CP-04` forbids React 19 with R3F 8 or Drei 9. Retained Three 0.160.1 and Router 6.30.3 require same-spike peer/behavior proof or must join the atomic transition; Router, Three, Zustand, and GSAP retain conditional reversible checkpoints. |
| `ASC-HIGH-003` | **Closed** | All 15 explicit human gates are `unsatisfied` and contain approver, evidence requirements, prohibited actions, durable references, and no founder-approval evidence. They cover exact locks/exceptions, npm, TypeScript, Azure/PostgreSQL, Python locking, CI/container, providers/data/residency/DPA/security/cost, paid/external/credential actions, Git, migrations, deployment, and residual risk. Direct coverage contains 27 human-gated components and nine deferred families; all 44 candidate paths also have applicable gate references; orphan count is zero. |
| `ASC-MED-004` | **Closed** | Seven normalized obligations cover advisory triage, licenses, SBOM, provenance/signature or immutable references, deterministic locks, exception ADRs, and quarterly rechecks. Every one of 44 candidate paths and all nine deferred families references all seven obligations. Advisory timeout and missing scans remain blocking. The two exception paths remain unapproved; all ADR, reason, expiry, and recheck approval fields are null, and every supply-chain exception record remains unapproved. |

## Regression and machine-model assessment

- Counts reconcile directly: 50 baseline items, 50 graph components, 27 edges,
  nine deferred families, six capabilities, 42 candidate components, and 44
  candidate paths. The two multi-path components are npm and TypeScript.
- All locks remain deferred. No preview, beta, RC, nightly, or experimental
  candidate is a production target.
- Validator failure logic covers the four former defects: unresolved or ambiguous
  references; missing/duplicate edge assignments and an incomplete React atomic
  set; satisfied/incomplete/orphaned gates; and missing/non-blocking obligations,
  path/family coverage, or fabricated exception approval.
- Prose, reference index, controls, graph, and validation report agree. Capability
  truthfulness is preserved: timeouts and missing scans are unresolved/blocking,
  not passes, and no external integration is called broadly operational.
- No new blocker, HIGH, or MEDIUM finding was found. No misleading LOW finding
  remains that could affect later target selection.

## Retained gates and limitations

This PASS closes only the independent revision review. All 15 human gates remain
unsatisfied, including exact locks and exceptions; npm and TypeScript choices;
Azure/PostgreSQL region, SKU, features, cost, security, and recovery; Python lock
and CI/container architecture; provider entitlements, data, residency, DPA,
security, compliance, and cost; paid/external/credential/Git/migration/deployment
actions; and residual material risk.

No compatibility spike, install, real browser matrix, Docker/Compose capability,
advisory pass, SBOM/license report, Azure regional proof, migration/restore,
deployment, or rollback drill was performed or approved by this review. Exact
targets must still be refreshed, proven, locked, and independently gated at the
applicable future wave.

## Decision

**PASS.** All four iteration-1 findings are closed, the validator exits `0` with
the expected counts, and no regression or new blocker/HIGH/MEDIUM finding remains.
The bounded compatibility inventory is **ready for founder review only**. This is
not founder approval of the slice, exact locks, an exception/ADR, the whole Phase
1 package, implementation, migration, external action, spending, or deployment.
