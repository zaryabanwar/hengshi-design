# Published scene assembly v1 — independent bounded review

Date: 2026-10-05. Verdict: **PASS for the logical proposal and additive reference**.
No actionable REVISE finding was identified; no finding severity or corrective
action is assigned. PASS is coherence review, not approval of the recommended
descriptor packaging, an accepted wire schema or runtime enforcement.

## Scope and method

Reviewed `SCENE_ASSEMBLY_CONTRACT.md` and only the added reference paragraph under
`Loading, resource lifetime and failure` in `CAMPUS_ASSET_BUILD_SPEC.md`.
Independently checked the thirteen frozen inputs and corresponding canonical
copies, the exact campus delta and all new local references. Inspected relevant
decision, feature, World/loading, public-envelope, publication, internal-inventory,
wayfinding and security sources. Independently consulted official Khronos glTF
and Three documentation for the scoped source observations below.

Applied repository governance and the constitution/project authority previously
read in this continuing review session. This is the first bounded review of a
new logical assembly proposal. It does not reaccept the existing campus/loading,
architecture or feature packages, reopen D-071's composition, or consume another
substantial model revision. No schema/prose test or application, asset, renderer,
browser, device, provider, Figma or deployment execution was performed.

## Exact input identities

Manifest: `output/research/scene-assembly-2026-10-05/review-inputs.json`.
Independently observed SHA-256:
`55138a524899f05c58e50ec110d7b951a669a960d98b4f0590b18fd1abf31c16`.

Snapshot filenames below are relative to
`output/research/scene-assembly-2026-10-05/`. All thirteen frozen hashes match the
manifest. The twelve corresponding canonical files equal their frozen bytes.
The before file has no current canonical source. Each table entry records the
observed snapshot byte length and exact reviewed SHA-256.

| Canonical source or before identity | Snapshot | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| `docs/phase-1-3d/SCENE_ASSEMBLY_CONTRACT.md` | `00-SCENE_ASSEMBLY_CONTRACT.md` | 12467 | `bdea1a7fa3dccb20311c6b9083d6bf392f076cd6a18f45ba473ccb4326b4d725` |
| `docs/phase-1-3d/CAMPUS_ASSET_BUILD_SPEC.md` | `01-CAMPUS_ASSET_BUILD_SPEC.md` | 41582 | `208cb4c93bfabd05555f8f1a2148aee2c9aa0cd26bf2dcee3154257cf0f88e88` |
| `docs/phase-1-3d/WORLD_EXPERIENCE.md` | `02-WORLD_EXPERIENCE.md` | 31970 | `fab7bf1ec7d29621947763b45ecb9eb5e24abcad66f0a169cc4ce06a2b6adb33` |
| `docs/phase-1-3d/asset-manifest.json` | `03-asset-manifest.json` | 41651 | `86b4b73249ce180d3cf72682575812ad182aba205ff60fbea6d10ef02254aec7` |
| `docs/phase-1-architecture/contracts/publication-manifest.schema.json` | `04-publication-manifest.schema.json` | 4297 | `d3620c8326246bc34040188de610c5823f1013936572d3ffb63a5eb350bc3852` |
| `docs/phase-1-architecture/contracts/PUBLICATION_CONTRACT.md` | `05-PUBLICATION_CONTRACT.md` | 32501 | `2386bec046387527a50dd8e6b4847ac11133932e2267afb96cb20ac4996f111c` |
| `docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md` | `06-SECURITY_PRIVACY_CONTRACT.md` | 24722 | `74ab420b5bec9f0aad72f59178f4ea7c626bd14edfa9d4ba02f3aa1dd0a1a254` |
| `docs/phase-1-architecture/MOVEMENT_STREAMING_ADDENDUM.md` | `07-MOVEMENT_STREAMING_ADDENDUM.md` | 4802 | `0e6bbf4a51a9d44c8e47fb84fe222e1bdbbca4c93b3b70c827671e8eef48e71a` |
| `docs/phase-1-ux-architecture/wayfinding-release-map.csv` | `08-wayfinding-release-map.csv` | 10356 | `298876f35468e7501028a77de63d1b449fd75b52183619a500700c46c2999c63` |
| `specs/003-3d-experience-completion/spec.md` | `09-spec.md` | 25605 | `2aceefa18e51bd11a450d79b2c75d0a2f3a0783baac785de12e56956fa03d4f9` |
| `DECISIONS.md` | `10-DECISIONS.md` | 72891 | `1d53a14ac3347ebeefeeb728e03862b09de111b748cef4e48d5f4ca19141b6d8` |
| `AGENTS.md` | `11-AGENTS.md` | 7686 | `55405cb02a96d05f7f6d68e56a588d743f83877fb2691a5a9f2c736126adbcc5` |
| Campus before additive reference | `CAMPUS_ASSET_BUILD_SPEC.before.md` | 41027 | `6bd0c2e95df6d227a34c0611e4c957501b1c368cd4f6d460f42b530559d0b228` |

## Independent delta and link checks

The campus addition at lines 154–160 is exactly one 555-byte reference paragraph
plus its following blank line. Removing it in memory restores bytes exactly equal
to the complete before file, with SHA-256
`6bd0c2e95df6d227a34c0611e4c957501b1c368cd4f6d460f42b530559d0b228`.
No existing loading, geometry, selection or acceptance text changed.

All nine new local link occurrences resolve: eight in the assembly proposal and
one in the campus addition. The loading fragment matches `Loading and residency
contract`; the security fragment matches `Browser resource and serialized content
proposal`. Other links resolve to the existing campus, World, internal inventory,
public envelope, publication contract, wayfinding map and new assembly proposal.
These are static file/heading checks, not HTTP or product-runtime proof.

## Bounded findings and authority reconciliation

1. **Recommendations remain proposals.** The descriptor-per-release/applied-3D-stream
   recommendation and logical record tables are expressly proposed. The existing
   envelope already admits `shared_asset`, `scene_chunk`, `collision`, `scene_panels`
   and the four stream identifiers; recommending a descriptor use does not modify
   that envelope or accept a closed registration/selection schema. Quick Access
   acquires no scene descriptor dependency. D-065's retained architecture and
   publication authority are respected: no new deployable, endpoint, provider or
   approval privilege is selected. D-064/66/71 scope and accepted composition remain
   intact; there is no geometry or appearance change.

2. **The three graphs and manifest identity are separated correctly.** Descriptor
   index references describe available definitions and must resolve, but are not
   all prerequisites for descriptor loading. Required resource dependencies form
   an acyclic resolved graph under PUBLICATION_CONTRACT and the loading contract.
   Walking topology may have loops; both endpoints must be ready and currently
   permitted for each crossing. There is no reciprocal geometry-to-descriptor
   resource dependency. Embedding the independent release ID rather than the
   containing manifest digest avoids the artifact-hash/manifest-hash cycle.
   Logical selectors are neither URLs nor authorization.

3. **Preparation coverage does not imply eager visitor fetching.** Publication
   preparation verifies the candidate's artifacts. Visitor residency acquires
   only the requested selected bundle and its required closure under existing
   scheduling/budget rules; parsing the index cannot fetch the whole campus.
   Optional detail has separate admission/ownership, and required ground,
   silhouette or interaction resources cannot be relabelled optional to evade
   budgets. Audio remains outside essential movement dependencies and subject to
   its own visitor-enabled lifecycle. No eager whole-campus or optional sound
   acquisition is introduced.

4. **Release/stream readiness and canonical authority agree.** Essential visual,
   ground/collision and interaction references bind the same manifest, applied
   compatible stream, bytes and placement/collision revision. Preparation is not
   movement admission. The controlled admission retains current release, visit,
   renderer, owner and budget checks and one matching context across render,
   collision, thresholds and anchors. Supporting ground remains safe during
   preparation. This coheres with F3D-04–07/14 and the existing loading lifecycle,
   including withdrawal and logical destination migration. No automatic stream
   change, new readiness shortcut or hidden semantic dependency is selected.

5. **Wayfinding and permission are not baked into geometry.** Formal destination,
   route, room and opening sequence remain controlled by the existing wayfinding
   and publication records. Area-local stable anchors and explicit directed
   crossings do not invent routes or open services. Non-traversable scenery
   carries no walking/safe-entry bindings, and scenery adjacency/bounds cannot
   prove reachable terrain. Closed, absent or unsafe destinations retain eligible
   semantic recovery. Scene records cannot assert staff availability, human
   acceptance, booking confirmation or private-process outcomes.

6. **Transforms and asset interpretation are bounded.** The documented campus
   glTF frame, one explicit area placement, retained hierarchy and common
   geometry/collision/anchor transformation avoid implicit double conversion.
   Node references bind exact asset identity and validated index rather than
   potentially duplicate names. Finite conservative bounds, scene-root checks
   and real seam/swept-body verification are required. Bounds/culling are not
   collision proof. Exact encoding, collider/navigation formats, body dimensions,
   speed, clearance and authored borders remain held; no numeric profile or
   compatible loader/decoder is selected.

7. **External resources and passive metadata respect security scope.** The proposal
   correctly recognizes that GLB may contain external resources. Supported
   resource-bearing fields/extensions must map to verified same-release manifest
   dependencies; private/arbitrary/unresolved resources block the bundle. Inline
   bytes still count toward bounded work/residency. Exact URI subset and remapping
   are later closed-schema inputs, and a base path/URL modifier cannot establish
   eligible serving. Imported names/extras are passive data, not executable actions.
   Private process data, staff identities, credentials, approval records and
   unreviewed claims cannot enter descriptors. No new worker/WASM/origin permission,
   telemetry, rights or data-retention policy follows.

8. **The campus notice accurately bounds review coverage.** It distinguishes new
   material from earlier engineering/loading receipts, preserves the existing
   body and holds exact wire encoding, profiles and runtime evidence. It does
   not retroactively extend prior receipt hashes or approve the accepted model
   beyond D-071's composition basis. The new recommendations can proceed to
   remaining governance gates; this PASS does not select them for production.

## Independent primary-source observations

Checked 2026-10-05 against official documentation. The producer's Context7 report
is provenance, not an independently replayed query or exact selected-package check.

- Khronos specifies metre-based right-handed coordinates with Y up, indexed
  references and names that need not be unique. Hierarchy transforms compose
  parent and local transforms; matrix versus TRS and scene-root rules matter.
  GLB can reference external resources, and required extensions must be declared.
  These support the proposal's scoped format observations. Conservative bounds,
  invertible area placement, publication eligibility and graph/ownership choices
  remain project requirements rather than glTF safety guarantees.
  [glTF 2.0 specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)
- GLTFLoader documents parsing raw data with a base path and optional decoder
  integrations. Parse/load completion does not establish this project's release
  eligibility, safe collision or atomic admission.
  [Three GLTFLoader](https://threejs.org/docs/pages/GLTFLoader.html)
- LoadingManager can transform resource URLs before requests. This is a remapping
  mechanism, not proof of resource authorization or a supported production URI
  policy. No URL modifier or package version is selected by this review.
  [Three LoadingManager](https://threejs.org/docs/pages/LoadingManager.html)

## Held inputs and limits of PASS

Exact closed descriptor/resource schemas and registration/selection binding,
transform/URI encoding, supported extensions, navigation/collision interpretation,
finite payload/queue/residency profiles, dimensions/clearance, authored topology,
resource ownership/cleanup, stable compatible locks, rights and production design
references remain required before implementation/acceptance. Shape validation
must later be supplemented with cross-record and graph validation; a passing
schema cannot prove same-release eligibility, geometry or safe movement.

After implementation is authorized, actual compiler/publication and
loader/mover tests must exercise wrong/unknown kind or stream/release, required
cycles, index parsing without eager fetch, external resources, duplicate/bad node
references, transforms/bounds, endpoints and missing collision, stale completion,
withdrawal and logical-destination migration. Named-device/export/reimport and
browser journeys must establish resource budgets, semantic parity and real safety.
No routine schema/prose test was executed for this definition review.

No runtime, wire-schema, safe traversal, dimensions, appearance, rights, performance,
device, security, accessibility, provider or whole Phase 1 certification follows.
Hash/link checks establish artifact identity and navigation only. Earlier reviews
retain their recorded input hashes and limits. The reviewer authored only this
receipt and preserved all inputs; no producer document, application, public
envelope, protected asset, dependency, account, configuration, Figma, commit, push
or deployment was changed by this review.
