# Closed collision-map shape — independent v1 review

Date: 2026-10-05. Independent reviewer: `/root/review_world_audio_v1`.
Verdict: **PASS**, bounded proposed shape/encoding/tooling review.
Findings: 0 Critical, 0 High, 0 Medium, 0 Low. Task status: DOING; uncommitted.
This is the first review cycle for this new encoding, not a model/composition
revision, prior-proposal reacceptance or founder approval.

## Scope, interruption and exact preservation

Reviewed only the new `docs/phase-1-3d/collision-resource-map.schema.json`,
`scripts/validation/test_collision_resource_map_schema.py` and the additive
“Closed collision-map shape proposal” at `SCENE_ASSEMBLY_CONTRACT.md:575–637`.
Preceding collider/scene/visual interpretation, publication/bootstrap/catalogue,
read/security, World/loading and F3D-04–07/14 requirements are controlling context.
The earlier logical collider receipt retains its exact original inputs/scope;
current review-reference edits and prior schemas are not retrospectively approved
by this new verdict. D-064–D-071, current AGENTS/constitution/project/task authority
and the held feature-implementation gates remain controlling.

The preceding attempt was interrupted by a workspace-credit error without a
receipt or verdict. This authorized retry continued from the actual unchanged
bytes and preserved tool output. It reverified identities and reproduced the
focused tests before issuing this concrete receipt. The earlier interruption was
not a REVISE cycle and is not converted into a historical PASS. Navigation or
checkpoint changes recording that interruption are outside the frozen proposal
and this receipt does not accept them or infer a verdict from them.

Packet: `output/research/collision-map-shape-2026-10-05/review-inputs.json`.
Manifest SHA-256 `8d33a3cb789ae44a76ac06d2726d0b9a54d27d6129dd8c393f6b7c7a6fda09d8`;
7,616 bytes. All **29** frozen inputs, totaling **565,476 bytes**, were independently
hashed/size-checked and byte-compared with their canonical sources. All match on
retry and the final pre-receipt recheck. The exhaustive identities are below.

The packet's immediate scene-before body (41,435 bytes; SHA-256
`87cf9eb48faa4a9f7ec1b68a8685f210cd42a123fbe0f7607fc7c9c18776be1a`)
is an exact byte prefix of the 45,890-byte current scene contract. Only 4,455 bytes
are appended. This immediate before snapshot is distinct from the earlier
31,918-byte logical-study before snapshot also retained as context. No prior
scene body was edited for this shape. Both new relative links to the schema and
tooling resolve. The 13 preserved unchanged-input guards were independently
checked against current bytes, including existing schema/publication context,
application dependency inputs and the protected layout GLB; all match. Hashes
are integrity evidence, not GLB correctness, application behavior or provenance.

## Inspected schema and encoding

| Subject | Assessment at these exact bytes |
|---|---|
| Closed root and collision identity | All six root fields are required: `schema_version: 1`, release ID, one of the three applied 3D streams, immutable client-build digest, distinct `collision_profile_id` and nonempty models. Shared identifier/digest definitions reuse the public publication schema through static references. No semantic/Quick Access stream is accepted. Format version 1 is a technical encoding identifier, not a later product release. Public metadata identifies a candidate compiled collision consumer; it is not executable configuration or proof of actual registration. |
| Model and primitive records | Models require collision artifact selector, fixed GLB/glTF 2.0 declarations, selected scene index and nonempty primitive inventory. Each primitive requires node index, mesh-local primitive index and ground-candidate/barrier purpose. Root, model and primitive objects all reject unknown fields. Null/missing values cannot supply a record; nested private fields, URLs, callbacks, decoder IDs, arbitrary resources, transforms, vertices or physics options are outside the closed projection. |
| Node-to-mesh resolution, Scene 592–599 | The appendix correctly resolves selected scene → reachable node → that node's mesh → mesh-local primitive index. There is no invented global primitive array or name-based lookup. A shared mesh under two nodes describes two instances. Descriptor area placement remains external and applied once; the map does not carry a second transform or replace placement ownership. Actual selected-scene reachability, mesh references and corresponding baked placement require verified bytes and semantic inspection. |
| Static actual-byte subset, Scene 601–607 | The embedded uncompressed extension-free GLB proposal remains a conservative project profile, not all glTF or an accepted production format. The constant GLB declaration cannot establish embedded BIN-only resources, triangle topology, finite positions, valid accessors/indices/container ranges or absence of skins/morph/animation/extensions. Those checks inherit the preceding logical collision profile and must execute at the inspector/importer boundary. A ground purpose cannot prove support, slope, body clearance or room permission. Barriers do not waive current thresholds/eligibility. |
| Array equality versus key identity, Scene 609–615 | `uniqueItems` rejects equal whole model/primitive records. It deliberately does not enforce unique artifact IDs when another field differs, or unique node/primitive selector pairs when purpose differs. The appendix requires both semantic uniqueness rules, complete reachable primitive coverage, collision-kind/same-release/bundle coverage, compiled profile/build association and exact geometry/placement inspection. This accurately distinguishes structural validity from the map's required meaning. |
| Index representation | All scene/node/primitive selectors are integers from 0 through 9,007,199,254,740,991. The bound is the proposed safe-integer representation domain, not an admissible allocation, geometry count, transfer or physical-device budget. It does not establish a referenced array exists or is that large. Later measured finite bounds remain mandatory under the loading/asset contracts. No geometry dimensions, tolerances or engine defaults are introduced. |
| Parsing and canonical bytes, Scene 616–620 | Duplicate JSON members and non-JSON/nonfinite input must be rejected before shape validation; ordinary fixture `json.loads` is explicitly not that ingress boundary. Canonical encoding remains required separately. No self-digest, containing-manifest digest or reciprocal required edge is introduced. Object validation cannot reconstruct erased duplicate keys or prove canonical original bytes after parsing. |
| Lazy lookup and DAG authority | The root is inert manifest-listed shared metadata under the preceding fixed per-stream collision lookup. It adds no URL, endpoint, scene field or visual-map field. Indexing a map is not permission to acquire all collision assets; selected essential bundle closure and loading gates still control acquisition/admission. Descriptor/map/model selectors are not reciprocal graph edges or whole-campus eager fetch requirements. Quick Access, scenery rendering and optional audio retain their separate gates. |
| Held compiled consumer/catalogue | Existing closed client catalogue profiles encode visual interpretation; the appendix expressly keeps collision-profile/engine-unit amendment and actual publisher/HTML/build/code association held. A valid map cannot bypass that gap, reuse a visual profile merely by matching text, or smuggle physics WASM into a decoder role. No engine, wrapper/worker/WASM graph, numeric physics configuration, browser permission or package version is selected. |
| Prior guards and production scope | Same eligible release/stream/build, staged query exclusion/admission, shared raw bytes versus distinct placed instance ownership, late work/generation fencing, query/retirement safety, closed-room/water protection and equivalent semantic recovery remain obligations from the existing logical/loading/World authority. This shape does not prove them or enable movement, assistance, sound or publication. D-071's protected layout and used revision allowance are unchanged. |

No actionable contradiction is found in the proposed shape or its bounded claims.
The knowingly structural-only accepted witnesses below are accurate documented
limitations, rather than production validity or a semantic acceptance bypass.

## Independent reproduction and boundary probes

Read the test source before executing it. It creates handwritten synthetic
records, checks the actual Draft 2020-12 schema and uses a fixed local
`referencing.Registry` containing only the map and publication schemas. Instance
values cannot direct schema retrieval. The fixture supplies no actual GLB,
publication envelope, compiled registry or runtime. Its negative expectations
exercise field/type/enum/domain boundaries; its semantic witnesses intentionally
validate shape while keeping the inspector's separate rejection obligations.
There is no installation, fetching, publication, mover or application mutation.

Recorded inspection tool runtime: Python **3.14.5**, jsonschema **4.23.0**,
referencing **0.37.0**. These are existing local validator tools, not selected
production graph versions.

| Independent command | Result and scope |
|---|---|
| `python -B -m unittest discover -s scripts/validation -p test_collision_resource_map_schema.py -v` | Retry exit 0, **5 test methods pass**. Covers all three streams/primitive inventories, required/closed records, identifier/build/profile/format/purpose boundaries, selector bounds/equal duplicates and explicit semantic-limit witnesses. The same focused methods had also completed before the interruption; this receipt relies on the reproduced retry result. |
| `python -B -m unittest discover -s scripts/validation -p 'test_*schema.py'` | Independently executed once in the preceding attempt against these unchanged bytes: exit 0, **31 methods pass**. That completed output was retained across the interruption; the broad suite was not repeated on retry. This is existing/new schema tooling, not application HTTP/compiler/GLB/physics enforcement. The separate frozen producer stdout/stderr remains producer evidence, not the source of this independent result. |

Additional independent in-memory probes used a separately constructed minimal
record and the same actual validator, rather than treating the producer's
assertions as proof:

| Probe | Observed shape outcome / implication |
|---|---|
| Repeated artifact ID with a different selected scene | Accepts; whole records differ. Semantic unique artifact identity remains required. |
| Same node/primitive pair with changed ground/barrier purpose | Accepts; whole records differ. Semantic pair uniqueness cannot be inferred from array uniqueness. |
| Unknown profile or another syntactically valid release | Accepts; no compiled registry/admitted release exists in shape validation. Actual context association is still held. |
| A dangling scene selector at the exact safe-integer maximum | Accepts; representation bounds do not inspect actual GLB indices or allocate memory. |
| An exactly equal duplicate primitive record | Rejects, confirming equality-based array uniqueness at the real validator. |
| Boolean, NaN, infinity, negative, fractional or above-bound node selector | Rejects. This does not turn the fixture parser into a strict raw-JSON boundary. |
| Extra visual `profile_id` or nested callback field | Rejects under the closed public projection. |
| Invalid first duplicate release member followed by a valid duplicate, parsed using default `json.loads` | Parsed object validates: the parser erased the first member. Explicit duplicate-member rejection remains an actual ingress obligation. |
| Noncanonical leading/trailing whitespace parsed to the same object | Object validates; the schema does not attest canonical raw text. |
| Validator started with no registered local resources | Fails with `_WrappedReferencingError`; the actual tooling uses its fixed registered resources and has no retrieval callback. |

These tests/probes support the schema and the stated separation of structural and
semantic validation. They establish no collision safety, geometry validity,
eligible serving, parser/code integrity, ownership, browser behavior or production
acceptance. No brittle prose assertion or ordinary documentation test was added.

## Primary-source corroboration

Independently opened the exact primary pages during this review on 2026-10-05;
producer source-notes is only summary context and its Context7 query is not the
reviewer's source verification. The official validation vocabulary defines array
uniqueness and structural assertions; it cannot inspect an external GLB or a
compiled application context. [JSON Schema 2020-12 validation vocabulary](https://json-schema.org/draft/2020-12/json-schema-validation)

The glTF specification defines a node's mesh reference and each mesh's local
primitives array, supporting the explicit selector chain. glTF's broader asset
capabilities do not make the recommended extension-free collision export subset
mandatory for other glTF applications, or prove collider admission. No vendor
example, current documentation package identity or dependency is selected.
[glTF 2.0 specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)

## Remaining gates and operation limits

Remain held: closed collision-consumer/profile and engine-unit catalogue encoding;
actual verified emitted-code/publisher/HTML/build/registry association; strict and
canonical publication/parser boundary; same-release/kind/scene/index/coverage and
placement compiler inspection; conservative actual-GLB/accessor/transform profile;
measured geometry/device/memory/concurrency/clearance/slope/support tolerances;
actual engine/controller/staging/query/fencing/retirement and failure tests;
complete supported mutually compatible stable graph, packaging/security permissions,
rights/notices/build provenance, semantic accessibility and physical-device/browser
journeys; integrated definition and founder acceptance. Valid shape is insufficient
while any such required input remains missing. Existing eligibility/withdrawal,
permissions, privacy, audio and provider-deferral authority is not weakened.

Only this independent receipt was authored. Application, schemas, producer prose,
protected models/assets, dependency/lock/settings, accounts/services and prior
receipts were not edited. No engine/sample/package execution, installation,
external design/API write, commit or push occurred. Shape/schema tests are reported
separately from hash/prefix/link integrity checks and from unexecuted production
behavior. This PASS does not accept prior contracts anew, a production collider
format/engine, full Phase 1, legal clearance or founder approval, and grants no
implementation or additional substantial model revision.

## Exhaustive frozen input identities

Source paths are repository-relative; snapshots are relative to the packet folder.
The manifest identifies these exact bytes, including older before/context files.
Later producer/navigation amendments are outside this receipt's identities/scope.

| Index | Source | Frozen snapshot | Bytes | SHA-256 |
|---|---|---|---:|---|
| 00 | `docs/phase-1-3d/collision-resource-map.schema.json` | `00-collision-resource-map.schema.json` | 2098 | `8d1d955526c33391ecccf483c7904f16fda0aa91617017873a95a51a581b9cea` |
| 01 | `scripts/validation/test_collision_resource_map_schema.py` | `01-test_collision_resource_map_schema.py` | 6880 | `392c97fee606205f4b8ea9dead7f8e193d1c266f74b229d452b42c63d1d1590c` |
| 02 | `docs/phase-1-3d/SCENE_ASSEMBLY_CONTRACT.md` | `02-SCENE_ASSEMBLY_CONTRACT.md` | 45890 | `87b693dadf215740ee798b22afd78b4531f5aabae8962f4b1d5f6aa7aa756bab` |
| 03 | `docs/phase-1-architecture/contracts/PUBLICATION_CONTRACT.md` | `03-PUBLICATION_CONTRACT.md` | 60361 | `48f1218c3888bdbe48bd40d47d911ce5786f1399b23d9776b4a7f776c897ad96` |
| 04 | `output/research/collider-binding-2026-10-05/scene.before.md` | `04-scene.before.md` | 31918 | `cb51f5a98c2f1453fcaaa5176eb8cda47288d8ee5dc1d0f2db66dba499ccd062` |
| 05 | `output/research/collider-binding-2026-10-05/publication.before.md` | `05-publication.before.md` | 57324 | `79db4c69345222a0cac60951b92f239e1f5e06a29c5e9e85622ea5b914f60ea5` |
| 06 | `output/research/collider-binding-2026-10-05/source-notes.json` | `06-source-notes.json` | 1262 | `be68dda447ab0fc320696acd9fb18fdaa835f6a453aa3175e6d4dcbee952f12e` |
| 07 | `AGENTS.md` | `07-AGENTS.md` | 7686 | `55405cb02a96d05f7f6d68e56a588d743f83877fb2691a5a9f2c736126adbcc5` |
| 08 | `.specify/memory/constitution.md` | `08-constitution.md` | 16234 | `33ec0bb02b0d0d9a55d0971589bd19f7242f5d56da130f8f496bc1d31a8b5d23` |
| 09 | `PROJECT.md` | `09-PROJECT.md` | 10942 | `a483bd2713fe420322772ab7fb07c848aaf103088697c05ab91f35d2e5ea1461` |
| 10 | `DECISIONS.md` | `10-DECISIONS.md` | 72891 | `1d53a14ac3347ebeefeeb728e03862b09de111b748cef4e48d5f4ca19141b6d8` |
| 11 | `TASKS.md` | `11-TASKS.md` | 3811 | `158e06c0d8cd67859c8b459b96dce3449cb4d16788d3c520e99d8823f72edcd3` |
| 12 | `docs/software-definition/README.md` | `12-README.md` | 15180 | `c454e744daeaff518e28b4095b47dd86fd3fb10e3298265c7cd159f142fa919c` |
| 13 | `docs/phase-1-3d/CAMPUS_ASSET_BUILD_SPEC.md` | `13-CAMPUS_ASSET_BUILD_SPEC.md` | 41840 | `42b0d89074b968704fa44d7ae40803ab4f5fab3f39c64a671ee75b2da66ba9e3` |
| 14 | `docs/phase-1-3d/WORLD_EXPERIENCE.md` | `14-WORLD_EXPERIENCE.md` | 31970 | `fab7bf1ec7d29621947763b45ecb9eb5e24abcad66f0a169cc4ce06a2b6adb33` |
| 15 | `docs/phase-1-3d/scene-descriptor.schema.json` | `15-scene-descriptor.schema.json` | 6971 | `ab452a793a6f0fea19455aa2e82878646fada677515de37b4173dee844813867` |
| 16 | `docs/phase-1-3d/gltf-resource-map.schema.json` | `16-gltf-resource-map.schema.json` | 3015 | `8d5cece4c921823c96e02c8f35707d991f391f560d261dcf2d9ff07e8c9fd939` |
| 17 | `docs/phase-1-architecture/contracts/client-build-catalogue.schema.json` | `17-client-build-catalogue.schema.json` | 3920 | `d41b989a4d5ab29178a7c498b200c82093ce9f09c34e3b8a2a42b68c56f5e0bf` |
| 18 | `docs/phase-1-architecture/contracts/publication-manifest.schema.json` | `18-publication-manifest.schema.json` | 4297 | `d3620c8326246bc34040188de610c5823f1013936572d3ffb63a5eb350bc3852` |
| 19 | `docs/phase-1-architecture/contracts/PUBLICATION_READ_HTTP.md` | `19-PUBLICATION_READ_HTTP.md` | 14860 | `a383350b1ed9301eae322b617e95055fc2731db0c877e2f67c8f60fcfb50d3a0` |
| 20 | `docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md` | `20-SECURITY_PRIVACY_CONTRACT.md` | 24722 | `74ab420b5bec9f0aad72f59178f4ea7c626bd14edfa9d4ba02f3aa1dd0a1a254` |
| 21 | `docs/phase-1-ux-architecture/wayfinding-release-map.csv` | `21-wayfinding-release-map.csv` | 10356 | `298876f35468e7501028a77de63d1b449fd75b52183619a500700c46c2999c63` |
| 22 | `specs/003-3d-experience-completion/spec.md` | `22-spec.md` | 25605 | `2aceefa18e51bd11a450d79b2c75d0a2f3a0783baac785de12e56956fa03d4f9` |
| 23 | `specs/003-3d-experience-completion/README.md` | `23-README.md` | 3729 | `f21f5be8eaf5916177bf5db66cee566b646948a43f0a7896b1c0357387955b70` |
| 24 | `docs/phase-1-3d/reviews/collider-binding-v1-2026-10-05.md` | `24-collider-binding-v1-2026-10-05.md` | 18011 | `13de852c49c184cf87b848181189af6e7c800b3b86cd36ea4282c37ee9a66961` |
| 25 | `output/research/collision-map-shape-2026-10-05/scene.before.md` | `25-scene.before.md` | 41435 | `87cf9eb48faa4a9f7ec1b68a8685f210cd42a123fbe0f7607fc7c9c18776be1a` |
| 26 | `output/research/collision-map-shape-2026-10-05/unchanged-inputs.json` | `26-unchanged-inputs.json` | 2133 | `0dbb8d25dfdd208d46a96777b1733bcb88023047fc8b87a2d40c02599f92595a` |
| 27 | `output/research/collision-map-shape-2026-10-05/schema-suite.stdout.txt` | `27-schema-suite.stdout.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 28 | `output/research/collision-map-shape-2026-10-05/schema-suite.stderr.txt` | `28-schema-suite.stderr.txt` | 135 | `0909b28feb3670edbec0c033fe4098dd7671aa181c54376622a2294b22f5f3a2` |
