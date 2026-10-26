# Published scene assembly contract — v1

Status: DOING. Proposed 2026-10-05 under D-064/D-065/D-066/D-071,
F3D-04–F3D-07/F3D-14 and the [campus build specification](CAMPUS_ASSET_BUILD_SPEC.md).
This is a production-definition proposal, not an approved wire schema, generated
asset, new endpoint or implementation permission. The separate
[independent review](reviews/scene-assembly-v1-2026-10-05.md) records bounded PASS
at the [preserved inspected proposal](../../output/research/scene-assembly-2026-10-05/00-SCENE_ASSEMBLY_CONTRACT.md).
This later review-reference update is outside those exact inspected bytes.
The accepted composition and protected assets remain unchanged. Full Phase 1
acceptance, encoding approval and implementation-boundary evidence remain separate.
The later [closed descriptor shape proposal](#closed-descriptor-shape-proposal)
is outside that logical review's exact inputs and has the separate scoped review
identified below.

## Cause and controlling boundaries

The [public publication envelope](../phase-1-architecture/contracts/publication-manifest.schema.json)
identifies immutable artifacts, routes, streams and dependencies, but does not
describe their spatial assembly. The [internal inventory](asset-manifest.json)
groups study meshes, not production areas or safe connections. The
[loading contract](CAMPUS_ASSET_BUILD_SPEC.md#loading-and-residency-contract)
requires exact area/variant/placement/collision inputs before admission. This
proposal supplies their logical relationship without copying that lifecycle.

The [publication contract](../phase-1-architecture/contracts/PUBLICATION_CONTRACT.md)
retains approval, immutable identity, eligible serving and withdrawal. The
[World definition](WORLD_EXPERIENCE.md) retains journeys, input, stream selection
and sound. The [wayfinding map](../phase-1-ux-architecture/wayfinding-release-map.csv)
retains formal wing/room/destination keys and opening order. Scene records cannot
open a room, invent a route, assert staff availability or confirm a booking.

## Recommended packaging and three distinct graphs

Recommend one compact scene descriptor per eligible release and applied 3D stream,
carried as a manifest-listed `shared_asset` with its existing key/hash/byte identity.
This use of an existing artifact kind is proposed, not a frozen extension of the
public envelope. Quick Access has no scene descriptor dependency. A descriptor
contains the release ID, never its containing manifest's digest: its bytes are
already included in that digest, so embedding it would create a hash cycle.

Descriptor references are validated against that same release's manifest; they
are selectors, not URLs or authorization. Do not fetch all references when parsing
the descriptor. Publish preparation verifies every candidate artifact; visitor
residency acquires only the requested area bundle and its required dependencies.

| Relationship | Meaning | Loading consequence |
|---|---|---|
| Descriptor index references | All eligible area definitions, variants, anchors and connections known to this descriptor | Validate identities and coverage; do not treat every indexed area as a prerequisite for the descriptor or initial visit. |
| Manifest resource dependencies | Bytes/interpretations actually required to prepare a referenced asset | Must form a resolved acyclic graph; acquire the selected bundle's complete required closure under bounded scheduling. No reciprocal reference from geometry to its containing descriptor. |
| Walking topology | Explicit permitted crossings between authored area endpoints | May contain loops; adjacency alone grants neither entry nor asset readiness. Each crossing still checks both ready contexts and current permitted thresholds. |

Optional decoration is a separately identified request, not a hidden required
dependency of essential ground. A required surface, silhouette or semantic anchor
cannot be classified optional merely to fit a budget. Audio remains in its own
visitor-enabled lifecycle and is not an essential movement-bundle dependency.

## Logical records for subsequent closed encoding

The following are proposed record obligations, not chosen JSON property names or
approved SQL tables. The later closed schema must preserve these meanings and
declare required/optional fields explicitly. Reuse the public envelope's exact
identifier, artifact, route and stream domains; introduce no parallel URL namespace.

| Record | Required information and validation |
|---|---|
| Descriptor | Supported definition-format identity, independent release ID, one applied 3D stream (`S-HIGH`, `S-MEDIUM` or `S-LOW`), campus frame declaration, unique area/connection records and logical destination bindings. Its artifact streams must include that stream. |
| Area | Release-local area ID, revision, traversable or non-traversable role, placement, conservative campus-space bounds, selected variant bundle and stable local anchor IDs. Multiple areas may serve one canonical room; one wing mesh is not automatically one area. |
| Essential variant bundle | Immutable visual, safe-ground/collision and required interaction references; supported interpretation identity; expected placement/collision revision; required dependency closure. Match this stream and release. Collider/navigation format is still unselected. |
| Optional detail reference | Manifest artifact identity, compatible stream and bounds; separate ownership/admission from essential readiness. It cannot introduce a service, change ground or alter permission. |
| Anchor | Unique ID within its area, explicit purpose (safe entry, crossing endpoint or semantic interaction), area-local pose and, where applicable, an existing canonical destination/route binding. Display names and glTF node names are not identities. |
| Connection | Unique ID, source and target area/endpoint identities, explicit direction and permitted-threshold binding. Two-way walking requires both directed crossings. Opening-state policy comes from canonical publication/wayfinding, not a baked boolean in geometry. |
| Destination binding | Existing formal destination key, canonical route ID and candidate safe-entry/interaction anchors in this geometry revision. No stale raw-position migration; a closed, absent or unsafe target exposes eligible semantic recovery. |

All artifact references must resolve in the same manifest with the required kind,
stream and exact bytes. Visual chunks use `scene_chunk`; ground/collision uses
`collision`; published panel content uses `scene_panels`. Required shared buffers,
textures or interpretation data use manifest-listed `shared_asset` dependencies.
The descriptor must not embed private process data, staff identifiers, approval
records, credentials, scripts, booking tokens or unreviewed claims. Panels bind
published content; authoring labels cannot substitute for that content.

Traversable areas require a complete essential bundle and safe-entry definition.
Non-traversable scenery has no walking endpoints or safe-entry bindings; its
appearance does not promise reachable terrain. No fabricated collision resource
is required merely to render a distant mountain. Optional visual variants cannot
change essential route coverage or opening rules between the three 3D streams.

## Coordinate, geometry and resource interpretation

Use the campus's documented right-handed, metre-based glTF frame with Y up. Apply
one explicit area placement outside the asset's authored node hierarchy; geometry,
collision and local anchors undergo that same placement exactly once. Preserve
the Blender-to-glTF conversion at export, rather than applying it again at runtime.
Choose one closed transform encoding later; never accept conflicting matrix/TRS
values. Require finite, invertible placement and compatible scale/orientation;
handedness, normals, winding and authored floor seams need actual reimport evidence.
No body dimensions, scale correction, movement speed or clearance is selected here.

Bounds must conservatively contain all admitted geometry, instances and required
collision for that bundle after placement; check componentwise ordered minima/
maxima and finite values. Bounds support scheduling/culling, not collision proof.
Crossing endpoints must match the actual connected ground and threshold geometry;
mere overlapping boxes or sampled centre points cannot certify swept-body passage.

glTF indices apply only to their exact asset digest; names need not be unique.
If an anchor references a node, bind the immutable artifact and validated node
index, plus its declared local frame. Resolve hierarchy transforms before applying
area placement. Reject missing indices and inconsistent selected scene roots.

A GLB can still reference external buffers or images. Export inspection must list
every supported resource-bearing field/extension and associate each external
resource with an exact same-release manifest artifact/dependency. Any unresolved,
private or arbitrary external resource blocks that bundle. Inline resources remain
within the verified parent bytes but still count toward decode/residency limits.
The supported URI subset and resource-remapping encoding remain closed-schema
inputs under the [browser-resource proposal](../phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md#browser-resource-and-serialized-content-proposal);
neither a base path nor a loader URL modifier proves eligible serving.

Validate supported glTF version/scene structure and all required extensions before
admission. Verify external dependency bytes before decode/upload, with bounded
work and late-completion fencing. Interpretation includes compatible loader/
decoder settings; no compression, extension or current package version is selected.
`extras`, names and imported metadata are passive data, never executable actions.

## Preparation, admission and rejection evidence

At publication preparation, validate descriptor shape plus cross-record integrity:
unique IDs, valid canonical bindings, resolved kinds/streams/dependencies, finite
placement/bounds, valid anchors and endpoint directions, truthful held-room state,
semantic parity and no forbidden/private fields. Required graph cycles fail before
activation. Empty references are not permission to skip an essential resource.
Scene preparation cannot grant founder approval or serving eligibility.

At visitor admission, resolve the descriptor through eligible public serving;
verify bytes and select the exact area bundle for the applied stream. Acquire only
its required closure and recheck the existing loading contract's release, visit,
renderer, owner and budget conditions at the controlled commit. Keep current safe
ground during preparation. Geometry, collision, thresholds and semantic anchors
must observe one admitted context. A successful parse does not allow movement.

Future tests must exercise the real compiler/publication and browser-loader/mover
boundaries: unknown/wrong-kind references, another release/stream, cyclic required
dependencies, descriptor indexing without eager whole-campus fetch, external GLB
resources, bad/duplicate node references, transform misapplication, under-sized
bounds, disconnected/reversed endpoints, missing collision, stale callbacks,
withdrawal and logical-destination migration. Derive expected outcomes from the
controlling requirements, not from a duplicated compiler or documentation text.
These are future behavior cases; no runtime or schema tests were executed here.

## Remaining decisions and measured inputs

Acceptance of the later descriptor shape, exact external-resource schemas and
descriptor registration/selection binding, URI subset, navigation/collider format, supported extensions,
numerical payload/queue/residency limits, authored dimensions/clearances and borders
remain to be proposed, reviewed and accepted. Keep them finite and supported by
named-device/export evidence; no library default is a production budget. Final
gestures/screens, asset rights, the full compatible stable graph and Phase 1
acceptance remain separate. This proposal changes no accepted study geometry and
does not consume another substantial composition revision.

Primary guidance checked 2026-10-05: Context7 `/websites/threejs` and official
[GLTFLoader](https://threejs.org/docs/pages/GLTFLoader.html) /
[LoadingManager](https://threejs.org/docs/pages/LoadingManager.html) document parsing,
resource remapping and optional decoder integration; they do not establish
publication authorization. The [Khronos glTF specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)
defines coordinate/transform conventions, indexed references, external resources
and required extensions. The proposed package records and graph separation above
are Hengshi engineering choices for review, not requirements claimed from those
vendors or selection of a production dependency version.

## Closed descriptor shape proposal

Proposed 2026-10-05. The separate
[independent review](reviews/scene-descriptor-shape-v1-2026-10-05.md) records bounded
PASS for the shape, encoding explanation and local tooling at the
[preserved inspected contract](../../output/research/scene-descriptor-shape-2026-10-05/00-SCENE_ASSEMBLY_CONTRACT.md)
and exact schema/test hashes listed in its receipt. These later receipt-reference
edits are outside those exact review inputs. The
[closed JSON Schema](scene-descriptor.schema.json) supplies a candidate encoding
of the logical records above; it is not an approved public API or production asset.
The earlier logical review does not cover this schema, encoding or tooling.

The top-level fields are `schema_version`, `release_id`, `stream`,
`coordinate_frame`, `areas`, `connections` and `destinations`. `schema_version: 1`
describes this first format proposal. Identifier and digest definitions resolve to
the existing publication schema through a fixed local registry; instance values
cannot direct schema retrieval. No containing manifest digest, asset URL,
publication permission, private process field or audio activation is accepted.

Area `placement` is glTF-order TRS: translation, XYZW rotation and scale. Anchor
`pose` is already in area-local space; its optional `node_binding` identifies the
source artifact/node for verification, never another transform to apply at runtime.
Export preparation resolves the source hierarchy and checks that declared pose
against it. Bundle `placement_revision` binds the declared placement and matching
collision context; `geometry_revision` and `variant_id` are independent selectors,
not claims that resources are ready. The `interpretation_artifact_id` resolves to
same-release public `shared_asset` bytes recording supported interpretation;
its own exact schema/settings and compatible runtime remain held.

Every traversable area has nonempty visual and collision artifact references and
at least one safe-entry anchor. Required interaction anchors carry both formal
destination and route references; where panels are required, semantic validation
must verify the matching `scene_panels` artifact and canonical interaction. Empty
panel references cannot suppress a required board. Scenery has no collision,
panel or anchor entries. Optional details are separately referenced and acquire
no ground or permission authority.

Connections are always directed (`source` to `target`); reverse walking needs a
separate reverse record. `threshold_destination_keys` lists every canonical
threshold governing that crossing. An empty list is valid only where authored
crossing evidence proves no threshold applies, not a way to bypass a held wing.
Destination `safe_entry: null` explicitly describes no spatial entry mapping;
its eligible semantic route remains independently usable. It cannot make a
retired/closed/unsafe destination traversable. Non-null entry and interaction
references must resolve to the correct anchor purposes and matching route/key.

All objects are closed and fields are explicit; null is permitted only for the
destination's absent spatial entry. The numeric scalar bound is IEEE-754 binary64
representation capacity, not an approved campus extent, movement/body scale or
device budget. Reject duplicate JSON keys, invalid Unicode and non-JSON numeric
constants before schema validation. Validate finite parsed/calculated values and
safe integer indices; overflow during composed transforms still fails even when
each input fits the schema. The quaternion must be unit length under a reviewed
export/validation tolerance. Actual ordered/enclosing bounds, invertible compatible
transforms, safe scale/winding, unique record IDs, reference existence/kinds/streams,
canonical thresholds, dependency closure and collision/route coverage require
semantic compiler checks. `uniqueItems` does not enforce distinct IDs among
differently populated objects. No tolerance or resource limit is selected here.

Definition tooling: `python scripts/validation/test_scene_descriptor_schema.py`.
Handwritten synthetic fixtures exercise these proposed shapes and rejection
boundaries; they are neither a scene compiler nor application/runtime tests.
The four focused shape methods and the fifteen-method broader local schema suite
passed; the reviewer independently reproduced both and probed the stated limits.
These are tooling results only, including the need for strict parsing before a
validator can be trusted with non-JSON constants; no ingress parser is implemented.
Use the existing local validator with only explicitly registered schema files;
do not retrieve untrusted or missing schema references from the network. Physical
geometry, eligibility, ownership, movement, cleanup and performance need their
previously defined actual-boundary tests after implementation authorization.

Primary shape/tool guidance checked 2026-10-05: Context7
`/python-jsonschema/jsonschema`, [JSON Schema validation](https://json-schema.org/draft/2020-12/json-schema-validation)
and [local schema referencing](https://python-jsonschema.readthedocs.io/en/stable/referencing/).
Installed evidence tooling is `jsonschema` 4.23.0 / `referencing` 0.37.0; no package
upgrade or production compatibility selection follows. The exact schema is a
reviewable v1 proposal; registration/selection, interpretation/resource formats,
finite measured operating limits, geometry, rights and full acceptance remain held.

## Visual resource interpretation proposal

Proposed 2026-10-05. The separate
[independent review](reviews/gltf-resource-map-v1-2026-10-05.md) records bounded
PASS at the [preserved inspected contract](../../output/research/gltf-resource-map-2026-10-05/00-SCENE_ASSEMBLY_CONTRACT.md)
and the schema/test identities in its receipt. This later receipt-reference update
is outside those exact inspected bytes. The [closed resource-map shape](gltf-resource-map.schema.json)
refines the visual part of `interpretation_artifact_id` as same-release public
`shared_asset` data. It changes no publication-envelope kind, endpoint, protected
model or accepted composition. It is not an accepted format, compatible build,
loader implementation or resource authorization. Collider/navigation interpretation
is still unselected and requires its own reviewed binding before bundle acceptance;
this visual map cannot satisfy that obligation by itself.

The root binds `schema_version: 1`, independent `release_id`, one applied 3D
`stream`, `client_build_sha256`, `profile_id` and nonempty `models`. The build digest
identifies an exact immutable compiled client/build descriptor whose definition,
registration and selection evidence are still held; it is not a source commit or
a production dependency selection. That build identity must be independent of
this map and its containing release manifest to avoid a hash cycle. The build's reviewed, compiled registry must
resolve `profile_id` to fixed permitted parsing/extension/decoder behavior. A public
profile cannot supply callbacks, imports, module paths, decoder options or code.
An absent registry entry, mismatched build or unsupported profile rejects preparation;
do not negotiate a different interpreter from content or silently change streams.

Each model binds its immutable `scene_chunk` artifact to `GLB` or `gltf_json`, glTF
`2.0`, one existing selected scene index, used/required extension names, complete
external-resource mapping and the exact decoder artifacts needed by that model.
The glTF identifier is the actual asset format, not a later product release.
Preparation must inspect the verified bytes: declarations must match their actual
extension use, required extensions must be a subset of used, and the compiled
profile must explicitly cover every used extension or an inspected safe-ignore
rule. A required extension cannot be ignored. Unknown resource-bearing extension
fields cannot bypass the inventory. Check `asset.minVersion`, container/chunk
structure, scene/node references, MIME and decoder compatibility independently;
the map's declaration does not validate the model.

Recommend a conservative production-export URI subset: nonempty ASCII segments
beginning with a letter, digit, underscore or hyphen, followed by those characters
or dots, separated by one slash. It excludes schemes, authorities, absolute paths,
dot segments, percent escapes, query/fragment, whitespace and backslashes. This
is a Hengshi packaging proposal, not the full glTF URI grammar. Production exporters
would emit this subset before checksums are fixed; a loader must not silently
rewrite a published source into compliance. Existing evidence assets are untouched.
GLB BIN/bufferView resources remain allowed within verified parent bytes. Recommend
excluding data-URI resources from these production exports; that is not a claim
that glTF forbids them. Embedded resources still count toward decoded residency.

An external entry maps one exact decoded glTF `uri` string, case sensitively, to a
same-release `shared_asset` artifact. Its nonempty `uses` lists each resource-bearing
location and purpose (`buffer`, `image`, or supported `extension`). `location` uses
an unescaped JSON-pointer subset of slash-delimited ASCII property/index tokens,
ending in `uri`; it must resolve to that exact string in the verified model JSON.
Core locations must be `/buffers/<index>/uri` or `/images/<index>/uri` with canonical
nonnegative array indices. Extension locations and their actual use are controlled
by the compiled profile. Unsupported property names or non-URI reference mechanisms
need a reviewed format amendment rather than an arbitrary pointer escape hatch.
One URI entry may list multiple uses; duplicate model artifact IDs, URI entries or
locations fail semantic validation, even when their surrounding objects differ.
Every external use must appear exactly once and map to appropriate verified bytes;
unused mappings, private/cross-release/wrong-kind artifacts and MIME/use mismatches
fail. The schema cannot establish those facts by inspecting the map alone.

Model, URI and decoder references in this map are indexes, not eager-fetch edges.
Each model's manifest dependency graph must declare every buffer/image/extension
resource and runtime decoder byte required for that model. Decoder artifact IDs
are an inventory checked against the trusted build/profile; they never select
executable code by themselves. Required wrapper/WASM/worker bytes, if any, use
release-associated `shared_asset` identities and reviewed build provenance. No
decoder implementation, worker permission or WASM capability is selected here.
Do not add reciprocal model/map dependencies or fetch all indexed models when
parsing the map. A selected bundle acquires its interpretation and required model
closures under the existing bounded loading contract; optional areas/details and
audio keep their separate lifecycles.

Before the actual parser can request any resource, verified mappings and compiled
profile behavior must control all core, plugin and decoder fetch paths. A base URL
or URL modifier alone is insufficient. Unknown requests must fail without network
fallback; redirects/origin/CORS/MIME/integrity follow the controlling browser and
publication contracts. Any approved temporary Blob URL has an explicit owner,
bounded lifetime and disposal, never a public payload-provided source. Checking
hashes after uncontrolled decoding or fetching is too late. Safe ground, late
completion fences, withdrawal and semantic recovery remain unchanged.

Definition tooling is `python scripts/validation/test_gltf_resource_map_schema.py`:
handwritten synthetic records check closed shape and URI rejection only. No strict
parser, glTF inspector, URI resolver, registry, compiler or loader is implemented.
The four focused shape methods and nineteen-method broader schema suite passed;
the reviewer independently reproduced both and the stated semantic limits. These
are definition-tooling results, not runtime enforcement or format acceptance.
Future actual-boundary tests must include missing/mismatched external GLB resources,
mixed-use paths, invalid scene/minVersion, unsupported/undeclared extensions, changed
build/profile/decoder bytes, unexpected plugin requests and data-URI exclusion,
plus required closure without eager whole-campus fetch and failure disposal.
Exact build/profile registration, selected extensions/decoder formats, collider
binding, measured finite limits, origins/permissions, provenance/rights, complete
stable compatibility and integrated/founder acceptance remain held.

Primary guidance checked 2026-10-05 through Context7 `/websites/threejs` and the
[Khronos glTF specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)
(URIs, extension declarations and external GLB resources),
[GLTFLoader](https://threejs.org/docs/pages/GLTFLoader.html) and
[LoadingManager](https://threejs.org/docs/pages/LoadingManager.html). Those sources
describe loader mechanics, not Hengshi's proposed subset, resource inventory or
publication authorization. No current package/version or compression is selected.
