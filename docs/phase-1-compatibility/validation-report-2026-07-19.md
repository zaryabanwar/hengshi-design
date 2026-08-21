# Compatibility inventory validation report — 2026-07-19

**Status:** Revision 1 independently reviewed and validated; ready for bounded founder review

## Scope

The deterministic validator checks all four machine artifacts, canonical
reference namespaces and local resolution, baseline-to-graph coverage, normalized
waves/checkpoints and all 27 edge assignments, human-gate coverage, candidate-path
and deferred-family supply-chain obligations, candidate release channels,
constraints, rollback and tests, integration-state truthfulness, Markdown links,
text hygiene, secret-shaped values, source hashes, local runtime versions, npm
locks, installed Python distributions, `pip check`, declared pytest-asyncio
absence, and the Compose PostgreSQL tag.

## Execution record

Command, from the repository root:

```powershell
& 'docs/phase-1-compatibility/validate.ps1'
```

Final exit code: `0`.

Passed check groups:

1. Baseline, graph, controls, and reference-index JSON parse.
2. Top-level and per-record lock selection remains deferred.
3. The reference index contains 149 unique entries. The resolver checked 1,108
   nested reference uses across 134 unique IDs and found zero unknown,
   duplicate, ambiguous, or unresolved references.
4. All 50 baseline items map one-to-one to 50 graph components.
5. All 27 edges and 9 required absent-family records retain evidence,
   constraints, rollback, tests, ownership, and deferred state.
6. Fourteen waves and fourteen unaccepted checkpoints parse; all 27 edges have
   exactly one assignment. React/DOM/types/R3F/Drei move atomically at CP-04,
   incompatible React 19 plus R3F 8/Drei 9 checkpoints are forbidden, retained
   Three peer satisfaction is explicit, and Router/Three/Zustand/GSAP retain
   smaller reversible waves.
7. All 15 human gates remain unsatisfied. All 27 human-gated components, all 9
   human-gated deferred families, and all 44 candidate paths have gate coverage;
   missing/duplicate/orphan coverage is zero. A satisfied gate without durable
   founder decision evidence would fail.
8. Seven blocking supply-chain obligations cover advisory triage, license,
   SBOM, provenance/signature or immutable reference, deterministic locks,
   exception ADRs, and quarterly rechecks for all 44 candidate paths and all nine
   deferred families. Timed-out/missing scans remain blocking and no exception
   ADR is approved.
9. No pre-stable production candidate appears in `targetCandidate` data.
10. Installed, configured, authenticated, protocol-tested, capability-tested,
    version-probed, timed-out, and operational states remain distinct.
11. Text has no unresolved markers, tabs, trailing whitespace, or missing final
    newlines.
12. Every local Markdown link resolves.
13. The secret-shaped scan returned zero findings; the validator would report
    only finding kind, path, and line, never the matched value.
14. All six recorded source-file SHA-256 hashes match the working tree.
15. Node/npm/Python runtimes, 24 npm lock entries, installed Python
    distributions, `pip check`, declared pytest-asyncio absence, and the
    floating Compose `postgres:16` tag reconcile with the baseline.

Final summary:

```text
VALIDATION PASSED: baselineItems=50; capabilities=6; components=50; edges=27; deferredFamilies=9; referenceIndexEntries=149; referenceUses=1108; unresolvedRefs=0; waves=14; checkpoints=14; edgeAssignments=27; humanGates=15; humanGateOrphans=0; supplyChainObligations=7; deferredFamilyCoverage=9; candidateComponents=42; deferredComponents=8; candidatePaths=44.
```

The machine-layer revision passed before this report was updated. The final
post-prose and post-report re-run also exited `0` and produced the exact summary
above.

## Boundaries

- Validation does not approve candidates, select exact production locks, prove
  application behavior, or replace independent review.
- No real browser flow ran; the Playwright result is only a version probe.
- Docker/Compose capability and both npm advisory runs timed out; none is a pass.
- Context7 protocol and the two documentation operations used by this slice were
  capability-tested anonymously; authentication and broad operational state are
  not claimed.
- Azure regional, resource, cost, security, compliance, PostgreSQL service, and
  NVIDIA entitlement evidence remains human-gated and untested.
- No package install, source change, migration, provisioning, paid activation,
  external write, commit, push, or deployment occurred.

## Independent review closure

Independent [iteration 1](reviews/architecture-supply-chain-review-iteration-1.md)
returned `REVISE` with three HIGH and one MEDIUM finding. Producer revision 1
added resolvable evidence references, compatible accepted checkpoints, explicit
human-gate coverage, and normalized supply-chain enforcement.

Independent [iteration 2](reviews/architecture-supply-chain-review-iteration-2.md)
returned `PASS`: all four findings are closed, the validator exits `0` with the
expected counts, and no new blocker, HIGH, or MEDIUM finding remains. The reviewer
made no producer edits and retained all 15 human gates as unsatisfied.

## Acceptance meaning

The compatibility inventory is ready for bounded founder review only. No exact
lock, exception, gate, checkpoint, implementation action, migration, external
action, spending, deployment, or complete Phase 1 acceptance is implied. Every
later wave must refresh current official and registry evidence, perform its
approved spike, and satisfy the applicable independent and founder gates.
