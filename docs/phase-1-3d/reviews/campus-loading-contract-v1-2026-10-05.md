# Campus loading and residency — independent v1 review

Date: 2026-10-05. Reviewer: `review_semantic_preparation_v1`, independent of
the producer. Verdict: **REVISE**, one bounded MEDIUM clarification below.
Task status: DOING; no commit, implementation or founder acceptance is implied.

## Frozen inputs and scope

| Input | Verified SHA-256 |
|---|---|
| [Campus asset build specification](../CAMPUS_ASSET_BUILD_SPEC.md) | `2b1481d8a86d31d2bf66f96f82b89f15fdf6112cb0eb89f30d02a03fd3239ecc` |
| [World definition](../WORLD_EXPERIENCE.md) | `77987ae5ee1c0f31f0252e30ea8ff38403d82ae2ed6ff21abe3a549413512d84` |

The corresponding copies in `output/research/campus-loading-contract-2026-10-05/`
were also hashed and match these identities. Scope is the new Loading and residency
contract, its earlier ownership references and World controlling-source link.
Read current governance, F3D-04–07/F3D-14 and related movement/audio requirements,
the movement architecture addendum, publication eligibility/refresh and established
immutable dependency obligations. Supporting sources supply authority/context;
their entire unrelated contents are not re-reviewed.

No application scheduler exists in this review scope. No simulated scheduler,
documentation phrase test, model generation, asset edit, runtime measurement or
dependency/settings change was performed. Only this receipt was written. This
definition review consumes no campus composition revision.

## Actionable finding

| ID | Severity | Evidence and consequence | Required correction |
|---|---|---|---|
| LOAD-01 | MEDIUM | `CAMPUS_ASSET_BUILD_SPEC.md:354–359` combines permitted area connections and required dependency closure, then rejects only “cycles that prevent deterministic admission.” `PUBLICATION_CONTRACT.md:41–43` requires rejection of unresolved/cyclic artifact dependency references without that qualification. A developer could treat a mutually dependent artifact group as acceptable if jointly loadable, or mistakenly reject a legitimate circular walking route. The two graph meanings and cycle policies are not explicit. | Distinguish area connectivity from immutable artifact dependency graphs. Allow legitimate topology loops subject to ready/permitted thresholds, while rejecting every cyclic or unresolved manifest dependency before preparation/admission under the publication contract. This is a clarification of existing authority, not a new algorithm or founder choice. |

## Other reviewed obligations

No additional actionable material finding was identified within this bounded scope.

- Release/variant/interpretation/placement and visit/renderer/attempt identities
  fence reuse and late completion; hashes/caches cannot confer eligibility.
  Prepared and Ready are distinct, and failure cannot resurrect a released area.
- Admission rechecks authority/readiness and commits the matching visual, collision
  and threshold context without a yielded partial mount. Swept-body/path checks
  retain the last safe pose on unready crossings. This is a local consistency
  requirement, not proof that a browser transaction makes server eligibility atomic.
  Canonical eligibility/freshness/withdrawal enforcement remains required.
- Required ground/interaction precedes travel, neighbors/reversal and decoration.
  Stage-specific concurrency, queue limits, transient reservations and draining work
  remain bounded. Abort requests do not free permits while uncancelled decode can
  still run; shared demand and retries cannot evade peak accounting.
- Explicit idempotent leases cover area/preparation/cache owners and in-flight
  users. Eviction preserves support/current interactions; shared final-owner cleanup
  and separate image-source lifetime avoid both premature disposal and hidden caches.
- Ordinary refresh requires complete old/new overlap and logical destination
  resolution; insufficient budget recovers semantically. Withdrawal/unknown
  eligibility stops affected public presentation without asserting offline rights
  or altering authoritative private booking/handoff lineage.
- Context loss invalidates GPU generation/readiness and stops travel/audio.
  Restoration revalidates/rebuilds before admission, requires deliberate renewed
  travel and preserves separate sound consent/mute/visibility policy. Optional
  decoration/audio cannot block essential access or manufacture staff availability.
- Exact profiles, borders, clearances, gesture references, resource adapters and
  compatibility remain held; no library version, provider or fixed default is selected.
  This adds no publication power, deployable, durable movement record or telemetry policy.

## Primary-source verification and limits

Checked [Fiber object/disposal guidance](https://r3f.docs.pmnd.rs/api/objects)
on 2026-10-05: one Object3D cannot occupy two scene locations; primitives require
explicit cleanup, while managed unmount disposal must be controlled for shared
resources. The proposed single cleanup owner and separate instances reflect those
constraints without claiming an implemented adapter.

[MDN abort guidance](https://developer.mozilla.org/en-US/docs/Web/API/AbortController/abort)
covers fetch/body/stream cancellation, not a guarantee that arbitrary decoder work
or GPU cleanup has terminated. [Context-loss](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/webglcontextlost_event)
and [restoration guidance](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/webglcontextrestored_event)
support renderer invalidation/rebuilding requirements. The producer's disclosed
Context7 Three disposal evidence and failed direct Three retrieval are not relabeled
as a successful second fetch. These sources constrain APIs; they do not prove
Hengshi's proposed lifecycle, lease implementation or numerical performance.

After LOAD-01 is revised, recheck the changed paragraph and graph-policy regression
within the same bounded review. Actual scheduler/mover/registry/browser evidence
must later cover collisions, cancellation/draining, shared release, eviction,
refresh overlap, withdrawal, context recovery and named-device resource peaks.
No full Phase 1, asset appearance, rights, physical-device, collision, accessibility,
complete compatible graph or enterprise-readiness acceptance follows from this review.

## Correction 1 verification — superseding bounded verdict

Date: 2026-10-05. Verdict: **PASS** for this loading/residency definition;
LOAD-01 is resolved. This supersedes the initial REVISE verdict at the corrected
identity below, without changing the initial finding or expanding review scope.
Task status remains DOING; no commit or founder acceptance is implied.

| Correction input | Verified SHA-256 |
|---|---|
| [Preserved corrected build specification](../../../output/research/campus-loading-contract-2026-10-05/CAMPUS_ASSET_BUILD_SPEC.correction-1.md), matching current specification | `6bd0c2e95df6d227a34c0611e4c957501b1c368cd4f6d460f42b530559d0b228` |
| World definition, unchanged | `77987ae5ee1c0f31f0252e30ea8ff38403d82ae2ed6ff21abe3a549413512d84` |

The [initial reviewed build bytes](../../../output/research/campus-loading-contract-2026-10-05/CAMPUS_ASSET_BUILD_SPEC.reviewed.md)
retain the initial `2b1481d8a86d31d2bf66f96f82b89f15fdf6112cb0eb89f30d02a03fd3239ecc`
identity. Initial inputs were verified before the producer correction; corrected
current/preserved bytes and the unchanged World were verified before and after
this correction review.

An exact comparison against the initial preserved build specification found only
the bounded topology/dependency paragraph change. Corrected lines 354–363
explicitly permit walking-connectivity loops only with ready ground and permitted
thresholds, separate that graph from immutable artifact dependencies, and reject
every unresolved or cyclic manifest dependency before preparation/admission,
including a jointly loadable cycle. This matches PUBLICATION_CONTRACT.md:41–43.
The paragraph retains body clearance, variant bounds, unsupported-extension and
transform rejection, non-traversable scenery and authored connections; the
surrounding identity, complete-bundle and readiness obligations remain unchanged.
No graph-policy regression or further actionable finding was identified.

Only this receipt was amended. No scheduler/runtime, physical collision, device
resource, appearance or implementation correctness was established. The primary
review's held inputs and runtime verification obligations remain in force; this
PASS neither approves Phase 1 nor consumes a composition revision.
