# Campus asset engineering — independent v1 review

Date: 2026-10-05. Reviewer: `review_semantic_preparation_v1`, independent of
the producer. Verdict: **PASS for the bounded definition and inventory**.
Task status: DOING; commits remain deferred. This is a new completed review
attempt; the earlier credits failure produced no verdict and is not evidence
for this PASS.

## Frozen inputs and scope

| Producer input | Verified SHA-256 |
|---|---|
| [Campus asset build specification](../CAMPUS_ASSET_BUILD_SPEC.md) | `642ec1f18228c549e521decc5e62f8f36a02ac740fed0fcdf230b48981335caa` |
| [Internal asset inventory](../asset-manifest.json) | `86b4b73249ce180d3cf72682575812ad182aba205ff60fbea6d10ef02254aec7` |

Reviewed governance, D-064/D-065/D-066/D-067/D-071, foundation NFR-002/NFR-007,
the World feature F3D-01–15, canonical World/storyboard/wayfinding definitions,
movement architecture addendum and earlier final-third study receipt. Review
covers the new authoring/export/streaming recommendations and inventory
accounting, not a fresh review of every supporting document or the whole Phase 1.

Inspected source generator and viewer as text and parsed the unchanged exported
GLB directly, without executing Blender, loading the generator or regenerating
models/renders. No producer source, protected asset, application, dependency,
settings or account was changed. Only this receipt was added.

## Independent accounting checks

- All nine inventoried source files exist and match their recorded exact byte
  lengths and SHA-256 hashes, including the accepted master/generator/GLB,
  selected concept, observations, viewer, wayfinding, World and storyboard.
- Raw GLB header/version/container length agrees with its 20,860,132 bytes.
  JSON has 117 mesh-bearing nodes, 117 meshes, 16 named materials and zero
  images, textures, animations, skins or cameras. All 117 nodes are scene roots
  without children. Generator identity and both declared material extensions match.
- Fifteen families cover indices 0–116 exactly once. Every recorded node name,
  mesh index and material reference matches the export; each per-family primitive,
  triangle, POSITION-entry and distinct geometry-bufferView count was independently
  recalculated. Triangle mode/count divisibility and absence of sparse accessor
  exceptions were checked before using index/accessor counts.
- Global totals reproduce **117 primitives, 726,056 triangles, 569,809 exported
  POSITION entries and 20,777,088 distinct referenced geometry-bufferView bytes**.
  Vegetation reproduces 513,632 triangles/14,199,192 bytes; all five wings total
  111,960 triangles/3,749,112 bytes; landscape 40,386 triangles/796,236 bytes.
  These are export accounting, not welded vertices, draw calls or measured memory.
- All five wing keys/routes/paths/opening ordinals and all ten service-room
  keys/routes/paths match the canonical wayfinding CSV. Geometry membership
  creates no activation or traversal permission. All production keys, digests,
  variants, collision outputs and global production selections remain null.
- Source inspection confirms procedural geometry/material authoring and
  name/material aggregation, declared metric study scale and no imported
  Atlanta/library scenery. The viewer uses OrbitControls, camera/target presets,
  a flat background and fog; that observation supports the inspector-versus-walking
  distinction. Neither original procedural construction nor metadata proves rights.

## Findings and engineering assessment

No actionable material finding within this bounded scope.

The accepted composition remains the basis; all-around depth, horizon treatment
and eye-level controls refine unfinished experience detail rather than reopen
D-071 or authorize a fourth substantial study correction. The specification
separates permitted look-around from flying/infinite traversal and retains
mouse/touch, destinations, accessible semantic actions and unselected WASD.
Reception/wing hierarchy, room gating and the AI + Data first-wing sequence agree
with current authority; a Strategy fixture does not open that wing first.

Recommendations remain evaluation candidates. [Rapier's controller guidance](https://rapier.rs/docs/user_guides/javascript/character_controller/)
supports translation with obstacle-aware movement while explicitly excluding
rotation; camera and application safety remain separate. [Recast binding guidance](https://docs.recast-navigation-js.isaacmason.com/)
supports offline navigation data/path queries and identifies WASM cost; neither
route planning nor a navmesh certifies body clearance, loaded ground or eligibility.
[Fiber performance guidance](https://r3f.docs.pmnd.rs/advanced/scaling-performance)
supports reusable resources, instancing/LOD and explicit invalidation for demand
rendering. No documentation example budget, parameter or version becomes selected.

[Three.js instancing](https://threejs.org/docs/pages/InstancedMesh.html),
[loader/decoder guidance](https://threejs.org/docs/pages/GLTFLoader.html),
[glTF Transform](https://gltf-transform.dev/) and
[WebGL resource guidance](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/WebGL_best_practices)
support the candidate optimization/resource approaches. Correct spatial bounds,
decoder lifetime, shared ownership, transient peaks and explicit release remain
application obligations; culling does not free memory or make ground traversable.
Primary guidance was checked on 2026-10-05; no complete package graph was resolved.

Generation/identity/variant fencing, readiness before admission, controlled
attachment, retained reversal ground and refusal to evict a live floor address
the material safety/failure obligations at definition level. Separate visual,
collision, content eligibility and process authority prevent an asset/cache from
publishing claims, granting room access or confirming staff/booking state.
No new service, database, provider, public API or durable movement history is selected.

## Limits and remaining gates

PASS establishes proposal coherence and independently reproduced inventory
accounting only. It does not establish appearance fidelity, human scale, body
collision, continuous route safety, physical accessibility, structural safety,
device/frame-time/memory/thermal performance, rights clearance, full stable
compatibility, working controls/loading/audio or enterprise readiness.

The whole export remains above the accepted initial transfer ceilings. Exact
dimensions/gestures/references, chunk borders, lifecycle/error schemas, bounded
numerical budgets and resource profiles require completion/review; NFR-007 is
still unfinished. Actual representative journeys, failures, reversal, eviction,
context loss, release withdrawal and same-model all-around visual/device checks
remain future implementation evidence. No new Blender execution, screenshot,
runtime movement test or physical-device measurement occurred in this review.
Production source/asset approval, detailed founder appearance acceptance and
integrated Phase 1 acceptance remain separate; this PASS opens no implementation.
