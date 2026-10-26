# Logical collider binding — independent v1 review

Date: 2026-10-05. Independent reviewer: `/root/review_world_audio_v1`.
Verdict: **PASS**, bounded logical proposal coherence and source-claim accuracy.
Findings: 0 Critical, 0 High, 0 Medium, 0 Low. Task status: DOING; uncommitted.

## Exact scope and preservation

Reviewed only `SCENE_ASSEMBLY_CONTRACT.md:435–566`, headed “Static collision
interpretation proposal”, and `PUBLICATION_CONTRACT.md:798–833`, headed “Collision
map registration proposal”. Earlier sections and the listed schemas/contracts are
controlling context; this is not their repeated whole-document acceptance or a
review of later changes. This new logical binding slice does not consume a model,
appearance or composition revision. D-071's accepted layout and used revision
allowance remain untouched; geometry, supported format and implementation remain
held. AGENTS.md, constitution, current project/task authority, D-064–D-071 and
F3D-04–07/14 govern the scope. The current checkpoint was read as context; it is
not a newly accepted implementation artifact or an additional frozen input.

Frozen packet:
`output/research/collider-binding-2026-10-05/review-inputs.json`.
SHA-256 `456a25f640e2d3ea1f8261e2cd66e2d9282d877727f2ec26b32da3f825d67423`;
5,561 manifest bytes, 22 inputs totaling 489,420 frozen bytes.
All 22 snapshot sizes/SHA-256 values were independently recomputed, and every
canonical source was byte-compared to its frozen copy. All match, including the
final pre-receipt recheck. Exact identities are listed below.

Scene before bytes (31,918) are an exact prefix of the 40,979-byte current file;
only 9,061 bytes are appended. Publication before bytes (57,324) are an exact
prefix of the 59,908-byte current file; only 2,584 bytes are appended. This is
whole-byte prefix verification, not a keyword/line-count substitute. Neither
prior body or closed schema was revised. Both new relative local links and their
actual heading anchors resolve. The three proposed reserved collision keys fit
the unchanged public asset-key grammar; `shared_asset` and `collision` already
exist in the envelope. This establishes artifact consistency, not safe paths,
compiler enforcement, eligibility or runtime behavior.

## Inspected logical obligations

| Subject and exact producer location | Assessment |
|---|---|
| Separate interpretation, Scene 437–454 and Publication 816–829 | The visual resource map does not establish collider interpretation. The proposal explicitly recommends a distinct static collision export/consumer while keeping capsule/controller/engine evaluation separate. No Rapier, WASM graph or package is selected. Actual publisher-verified code/profile/unit association is required; equal public profile strings cannot prove it. Physics WASM cannot be relabelled a visual glTF decoder to fit the existing catalogue. The unchanged visual-profile schema is correctly described as insufficient to encode the new consumer. |
| Exact inventory and instance domains, Scene 456–473 | The map binds independent release ID, applied stream, immutable client build, compiled profile and exact model/scene inventory. References are limited to exact verified model bytes, with every reachable mesh-node/primitive instance covered once and an authored ground/barrier purpose. Different nodes sharing a mesh remain distinct placements. Wrong/missing kinds, indices, scene, release/stream/build, duplicate or incomplete inventory and unsupported profile block preparation. Names, extras and visual labels cannot provide identity or permission. Every traversable bundle's collision IDs need coverage; the existing visual interpretation reference remains visual. Scenery has no invented collider obligation. |
| Actual-byte export subset, Scene 475–493 | Indexed triangle lists, finite float32 positions and 16/32-bit scalar indices are a proposed Hengshi subset, not the full glTF definition. Geometry/count/index/range/stride/alignment/container checks and measured degeneracy tolerances are required beyond declarative shape. The initial subset excludes sparse/normalized accessors, skins, morph targets, animations, instancing extensions and external/data resource acquisition; all buffer bytes must be in verified BIN data. Images/materials/textures/cameras/lights/extension resources are rejected for this collision export. No general visual-loader fetching or presumed Draco/Meshopt/quantization decoder is authorized. Export stripping/baking, validator/reimport and production exporter remain unselected and cannot alter protected or published bytes. |
| Hierarchy and transform-once rule, Scene 495–509 | Verified scene hierarchy/node transforms compose through parents, then area placement once. Finite/invertible affine baking and explicit reflection/nonuniform-scale evidence prevent handing arbitrary scale to a future physics API or repeating Blender conversion. This agrees with the existing metre/Y-up frame and area-local anchor/pose interpretation. Collision, visual and anchor coordinates must match after placement. Repeated source geometry is not a repeated physics instance: raw bytes may share leases, while baked placement/world/generation and engine instances require distinct owners. Same digest alone cannot authorize old-release/disposed-world/other-area reuse. |
| Reserved selection and publication authority, Publication 805–823 | Compiler-owned fixed lookup has exactly the three applied 3D stream values and maps to an existing manifest-listed shared asset. Only the requested traversable bundle triggers the selected stream's collision lookup; Quick Access and scenery do not acquire it. Public data cannot provide arbitrary keys, suffix selection, imports, callbacks, parameters or permissions. Private preparation checks map/model associations before activation; eligible exact-release serving, verified bytes and admitted release/stream/build context remain necessary. The existing GET contract/envelope is preserved with no new endpoint or artifact kind. |
| Independent build and DAG, Scene 513–518 and Publication 830–833 | Independent client build precedes release-specific maps. No map self-digest or containing-manifest hash is introduced. Map inventory references are indexing selectors rather than whole-campus fetch prerequisites; requested bundles still acquire their required collision closure. Reciprocal descriptor/map/model dependency edges remain forbidden. This preserves the separation among acyclic required-resource graphs, lazy indexes and possibly cyclic walking topology. Optional visual detail/audio gates are not folded into essential collision loading. |
| Staged admission, Scene 520–526 | Collider construction must be isolated/query-excluded and cannot affect the active mover before guarded admission. Query set, rendered area, threshold/safe-entry context and generation must switch coherently. The proposal explicitly holds entry when the eventual engine cannot prove isolation. GLB validity, parsing and engine object creation are separate from usable ground/body clearance. This extends the existing loading preparation barrier without claiming engine filtering/staging is implemented or vendor-guaranteed. |
| Free/destination movement and forbidden space, Scene 528–535 | Both travel modes use the same admitted collision/query/threshold context. A route plan, ray, bounds or navmesh does not establish swept-body support/clearance. Ground labels and sensors cannot open a room. Static surfaces do not imply a solid interior, so closed-room/water/scenery boundaries retain authored barriers and decision-time guards. Camera look remains separate from body translation. No dimensions, offset, slope, speed or controller default is selected. Essential signs/destinations and semantic recovery remain required across streams under F3D-14. |
| Query/retirement and handle reuse, Scene 537–544 | Current safe ground persists only through coherent replacement or canonical recovery under the existing eligibility controls. Live mover support, queued queries and crossings prevent premature retirement; detachment/exclusion precedes release. Late work is fenced by release, stream, build/profile, placement, world/visit generation and owner attempt. A reused numeric handle cannot validate a stale completion. Existing loading contracts still require settlement/draining accounting and valid owners; CPU mesh/BVH/engine costs, staging overlap and any future runtime/worker/WASM overhead join bounded residency. No engine default or numerical envelope is invented. |
| Existing control authority and held acceptance, Scene 546–566 and Publication 824–833 | Malformed bytes, omissions, placement mismatch, stacked floors, walls/water, reflections, delayed imports, staging leaks, withdrawal and retirement during queries are named future actual-boundary cases. Loading/World/publication/security retain same-release eligibility, immediate withdrawal/unknown recovery, no automatic tier change, no optional audio enablement or eager fetch, semantic alternatives and private-process authority. Exact map/profile/engine-unit encoding, actual compiler/build association and integrated/founder acceptance remain expressly held. This is an engineering recommendation, not a public wire-schema amendment or implementation permission. |

No actionable contradiction or material unapproved selection is found in these
exact additions. The proposed representation is explicitly unapproved engineering
definition, with later encoding and actual enforcement held; this PASS neither
turns it into an accepted asset format nor supplies missing production inputs.

## Independent primary-source verification

The producer `source-notes.json` is a research summary, not archived full vendor
pages, and its Context7 query is not independent verification. The reviewer
independently opened the following primary pages on 2026-10-05. Their current
technical documentation identities and examples are observations, not selected
production package versions or source-to-binary proof.

- Khronos defines indexed references, metre/Y-up coordinates, strict-tree node
  hierarchies, TRS composition and parent/local transforms; accessors and buffer
  views describe binary ranges. A GLB can contain external resources as well as its
  BIN chunk, so self-contained collision files are correctly a Hengshi restriction.
  BIN padding rules still belong to actual validation; “lengths agree” is not a
  claim that padding must be absent. These facts support inspection/transform
  obligations, not collision or clearance proof. [glTF 2.0 specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)
- Three's loader documentation describes load/parse APIs, extension/plugin hooks
  and decoder dependencies. It does not establish collision admission or authorize
  uncontrolled external resources. The independent collision consumer and held
  actual code/build association therefore remain necessary project obligations.
  No example decoder URL or callback is selected. [GLTFLoader](https://threejs.org/docs/pages/GLTFLoader.html)
- Rapier describes triangle meshes as useful for fixed environments and as surfaces
  without an interior; it warns about long/thin triangles. Its collider identifiers
  are unique among live objects but may be reused after removal. These support
  geometry caution and generation/ownership fencing. Vendor examples explicitly
  use arbitrary values, which this proposal does not adopt. They do not prove
  current Hengshi physics isolation or clearance. [Collider guide](https://rapier.rs/docs/user_guides/javascript/colliders/)
- Rapier's character-controller section computes corrected translation from shape
  queries and requires the application to apply it. It explicitly excludes
  rotational movement and says application needs can require customization. This
  supports separating camera look and translation while holding thresholds,
  support, policy and numerical configuration; it does not certify a chosen
  capsule/profile/controller. [Controller guide](https://rapier.rs/docs/user_guides/javascript/character_controller/)

## Remaining inputs and operation limits

Closed collision-map/profile encoding must bind every index/instance/placement
and reject unsupported required interpretations/resources under the existing
compiler/loading rules. The actual collider consumer registry and engine-unit
catalogue roles/gates still need their own reviewed encoding and real build/code
association; no visual profile, copied digest or public selector can substitute.
Production must independently establish actual compatible stable exporter/parser/
renderer/physics/wrapper/worker/WASM/browser graph, resource integrity/serving and
applicable security permissions. No format, tool or permission is accepted here.

Still held: authored connected collision geometry, closed-room/water barriers,
body/slope/step/support/clearance profiles and tolerances, placement revisions,
measured finite transfer/CPU/GPU/engine residency and overlap limits, engine query
isolation/admission/retirement behavior, malformed-byte/late-work boundary tests,
real supported-browser/device journeys, semantic accessibility/recovery, asset
rights and source/build provenance, full independent/integrated/founder acceptance.
Mandatory Entra/private AI privacy rules and deferred hosting/provider scope remain
unchanged. Neither this review nor the cited guides authorizes production modeling,
implementation or another substantial composition revision.

Only this receipt was written. No application/source/schema/dependency/lock/asset,
runtime, credential, provider, external-design or Git-history operation occurred.
No package installation, vendor/example/experimental execution or new prose/schema
application test was run. Prefix/hash/key/link inspection is artifact validation;
primary-page inspection is source verification. Neither is collider, geometry,
loader/controller/security/accessibility/performance or production runtime proof.
Prior reviews retain their original exact scopes; no whole-contract, full World,
complete Phase 1, physical-phone, legal or founder acceptance is claimed.

## Exact frozen input identities

Snapshot filenames are relative to the packet folder; source paths are
repository-relative. Later amendments lie outside these identities.

| Index | Source | Frozen snapshot | Bytes | SHA-256 |
|---|---|---|---:|---|
| 00 | `docs/phase-1-3d/SCENE_ASSEMBLY_CONTRACT.md` | `00-SCENE_ASSEMBLY_CONTRACT.md` | 40979 | `c1cd0532c0dfa0dcd9c8fbb81f6458ec6b87949e1f84daa21b11004cf8f97a43` |
| 01 | `docs/phase-1-architecture/contracts/PUBLICATION_CONTRACT.md` | `01-PUBLICATION_CONTRACT.md` | 59908 | `f022b50504fc75e35d0bbbbfc131b63df67ab511252977ac7eba7eb7db8badd4` |
| 02 | `output/research/collider-binding-2026-10-05/scene.before.md` | `02-scene.before.md` | 31918 | `cb51f5a98c2f1453fcaaa5176eb8cda47288d8ee5dc1d0f2db66dba499ccd062` |
| 03 | `output/research/collider-binding-2026-10-05/publication.before.md` | `03-publication.before.md` | 57324 | `79db4c69345222a0cac60951b92f239e1f5e06a29c5e9e85622ea5b914f60ea5` |
| 04 | `output/research/collider-binding-2026-10-05/source-notes.json` | `04-source-notes.json` | 1262 | `be68dda447ab0fc320696acd9fb18fdaa835f6a453aa3175e6d4dcbee952f12e` |
| 05 | `AGENTS.md` | `05-AGENTS.md` | 7686 | `55405cb02a96d05f7f6d68e56a588d743f83877fb2691a5a9f2c736126adbcc5` |
| 06 | `.specify/memory/constitution.md` | `06-constitution.md` | 16234 | `33ec0bb02b0d0d9a55d0971589bd19f7242f5d56da130f8f496bc1d31a8b5d23` |
| 07 | `PROJECT.md` | `07-PROJECT.md` | 10942 | `a483bd2713fe420322772ab7fb07c848aaf103088697c05ab91f35d2e5ea1461` |
| 08 | `DECISIONS.md` | `08-DECISIONS.md` | 72891 | `1d53a14ac3347ebeefeeb728e03862b09de111b748cef4e48d5f4ca19141b6d8` |
| 09 | `TASKS.md` | `09-TASKS.md` | 3811 | `158e06c0d8cd67859c8b459b96dce3449cb4d16788d3c520e99d8823f72edcd3` |
| 10 | `docs/software-definition/README.md` | `10-README.md` | 15180 | `c454e744daeaff518e28b4095b47dd86fd3fb10e3298265c7cd159f142fa919c` |
| 11 | `docs/phase-1-3d/CAMPUS_ASSET_BUILD_SPEC.md` | `11-CAMPUS_ASSET_BUILD_SPEC.md` | 41840 | `42b0d89074b968704fa44d7ae40803ab4f5fab3f39c64a671ee75b2da66ba9e3` |
| 12 | `docs/phase-1-3d/WORLD_EXPERIENCE.md` | `12-WORLD_EXPERIENCE.md` | 31970 | `fab7bf1ec7d29621947763b45ecb9eb5e24abcad66f0a169cc4ce06a2b6adb33` |
| 13 | `docs/phase-1-3d/scene-descriptor.schema.json` | `13-scene-descriptor.schema.json` | 6971 | `ab452a793a6f0fea19455aa2e82878646fada677515de37b4173dee844813867` |
| 14 | `docs/phase-1-3d/gltf-resource-map.schema.json` | `14-gltf-resource-map.schema.json` | 3015 | `8d5cece4c921823c96e02c8f35707d991f391f560d261dcf2d9ff07e8c9fd939` |
| 15 | `docs/phase-1-architecture/contracts/client-build-catalogue.schema.json` | `15-client-build-catalogue.schema.json` | 3920 | `d41b989a4d5ab29178a7c498b200c82093ce9f09c34e3b8a2a42b68c56f5e0bf` |
| 16 | `docs/phase-1-architecture/contracts/publication-manifest.schema.json` | `16-publication-manifest.schema.json` | 4297 | `d3620c8326246bc34040188de610c5823f1013936572d3ffb63a5eb350bc3852` |
| 17 | `docs/phase-1-architecture/contracts/PUBLICATION_READ_HTTP.md` | `17-PUBLICATION_READ_HTTP.md` | 14860 | `a383350b1ed9301eae322b617e95055fc2731db0c877e2f67c8f60fcfb50d3a0` |
| 18 | `docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md` | `18-SECURITY_PRIVACY_CONTRACT.md` | 24722 | `74ab420b5bec9f0aad72f59178f4ea7c626bd14edfa9d4ba02f3aa1dd0a1a254` |
| 19 | `docs/phase-1-ux-architecture/wayfinding-release-map.csv` | `19-wayfinding-release-map.csv` | 10356 | `298876f35468e7501028a77de63d1b449fd75b52183619a500700c46c2999c63` |
| 20 | `specs/003-3d-experience-completion/spec.md` | `20-spec.md` | 25605 | `2aceefa18e51bd11a450d79b2c75d0a2f3a0783baac785de12e56956fa03d4f9` |
| 21 | `specs/003-3d-experience-completion/README.md` | `21-README.md` | 3729 | `f21f5be8eaf5916177bf5db66cee566b646948a43f0a7896b1c0357387955b70` |
