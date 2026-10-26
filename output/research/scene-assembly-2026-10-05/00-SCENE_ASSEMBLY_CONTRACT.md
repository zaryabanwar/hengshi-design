# Published scene assembly contract — v1

Status: DOING. Proposed 2026-10-05 under D-064/D-065/D-066/D-071,
F3D-04–F3D-07/F3D-14 and the [campus build specification](CAMPUS_ASSET_BUILD_SPEC.md).
This is a production-definition proposal, not an approved wire schema, generated
asset, new endpoint or implementation permission. Independent review is pending.
The accepted composition and protected assets remain unchanged. Full Phase 1
acceptance, exact encoding and implementation-boundary evidence remain separate.

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

The exact closed scene/resource schemas, descriptor registration/selection binding,
transform encoding, URI subset, navigation/collider format, supported extensions,
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
