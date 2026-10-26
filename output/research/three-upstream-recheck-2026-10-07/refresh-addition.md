
## Published renderer blocker and exception proposal — 2026-10-07

The [fresh official registry packet](../../output/research/three-upstream-recheck-2026-10-07/observations.json)
retains Three 0.186.1/types 0.186.0, three-stdlib 2.36.1, Drei 10.7.9 and Fiber 9.8.1
as their current latest tags. No new stable helper release resolves the prior gate.
[PR 433](https://github.com/pmndrs/three-stdlib/pull/433) merged a declaration fix,
but its merge is later than the current published three-stdlib package.
The [archive/source comparison](../../output/research/three-upstream-recheck-2026-10-07/source-comparison.json)
verifies published archive SRI and exact equality of both loader declarations with
the earlier failing installation; their merged source differs. SRI proves archive
integrity, not signatures, provenance, licence clearance or runtime compatibility.
Context7's current development-source examples explain loader return semantics;
they do not prove an npm release or exact-version conformance.

The [bounded Three exception proposal](THREE_STABLE_EXCEPTION_PROPOSAL.md) recommends
the previously evaluated stable 184 pair under explicit approval, dated recheck
and rollback gates. It selects no graph and authorizes no application upgrade.
No compiler/build/browser rerun was justified by these unchanged published inputs;
the earlier exact-input receipts remain the executable evidence. The new upstream
and exception interpretation awaits its own independent review and founder decision.
