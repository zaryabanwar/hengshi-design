# Atlanta HQ asset assessment

Date: 2026-10-04. Status: DOING; retained inspection/comparison evidence,
not approval of a production asset or implementation. Original GLB unchanged.

Current authority: D-066 selects an original modular headquarters; D-067 selects
the nature-integrated direction and D-071 accepts the final-third study as the
layout basis. The replacement choice is settled. The recommendations below
describe the earlier asset assessment, not another open founder decision.
Continue through the [campus build specification](CAMPUS_ASSET_BUILD_SPEC.md);
retain this inspection and the Atlanta asset for provenance and comparison.

## Recommendation

Useful as a customizable exterior shell and prototype/reference asset. Not usable
as-is as a complete freely walkable headquarters. Build a purpose-designed
interior, circulation and collision model. Retaining the exterior is technically
possible; a new modular building is preferable if the approved experience needs
multiple service wings, seamless indoor/outdoor travel and controllable streaming
units. Building our own surroundings alone does not require replacing this shell.
Resolve the journey/space plan before choosing the production building.

## Inspection method and identity

Imported the repository GLB into Blender 5.0.1, rendered exterior/base and isolated
lobby geometry, inspected all imported mesh bounds and materials, sampled vertical
geometry intersections, checked temporary welded topology, and inspected current
WorldCanvas/ExteriorScene code. Temporary scripts/scenes are outside the repository.
SHA-256 matches the provenance record:
4767cab4d346207a2109ffc1584e256e82ae1cecc110780b99c4406a9586aafe.

## Findings

| Area | Evidence and implication |
|---|---|
| Packaging | 10,002,012 bytes; 13 GLB meshes, 28 nodes, 13 materials, 23 images. No animations, skins or cameras. Mesh/node grouping is predominantly material-based, not room/sector based. |
| Exterior | Tower geometry, windows/blinds/glass and billboard are separately addressable. Exterior rebranding and surroundings are feasible deterministic Blender work. Removing a billboard is not a substitute for designing the facade. |
| Interior | Lobby baked mesh has 5,910 imported vertices and 2,963 faces; trimsheet mesh has 108 vertices and 54 faces. Interior-related geometry exists, but sparse surfaces/core do not constitute the required service rooms and circulation. |
| Upper floors | Fifteen downward probes, at three interior positions across five heights from 35 to 200 Blender world units, all hit lobby roof surfaces around 25.96/28.15. No intermediate upper-floor surfaces were encountered at those sample positions. This supports an exterior tower interpretation, not a completed occupiable tower; it is sampling, not exhaustive proof of every cavity. |
| Lobby surfaces | Twenty sampled footprint positions intersect a broad surface around 8.13 and several surfaces around 13.85/16.47/25.96, with a central upper surface around 28.15. Surface hits alone do not prove traversable connectivity, appropriate normals or collision clearance. |
| Geometry integrity | After temporary coordinate welding, lobby still has 1,943 boundary edges; main structural mesh has 11,295 boundary edges and 11,306 non-manifold edges. Open architectural surfaces can be intentional. Raw glTF seam counts would overstate defects; neither metric proves the asset unusable for rendering. Do not use the visual mesh as a ready-made closed collision solid. |
| Scale/placement | Asset geometry sits above the origin (base about 8.13); tower top about 220.13, footprint roughly 61 by 97 world units. These are imported coordinates, not verified real-world metres. Normalize placement and validate human scale before a walk-through. |
| Textures | Embedded images range from 256-square to 1024-square, with some rectangular images. Approximately 79.5 MiB for one uncompressed RGBA8 copy plus full mip chains; actual GPU format, sharing and buffers change memory use. The 10 MB download is not the GPU-memory budget. |
| Rendering | Glass, repeated facade surfaces, baked interior and parallax-labelled mesh need close-range/backface and transparency checks. Triangle count alone cannot certify mobile performance; LODs, compressed textures and device measurements remain necessary. |
| Interaction | No supplied navigation/collision metadata or door animation. Required collision proxies, entrance clearance, floor connections, accessible routes and streaming partitions must be designed and tested. No end-to-end avatar traversal has been certified. |
| Current prototype | WorldCanvas.tsx defines a separate simple Room from planes/boxes; ExteriorScene.tsx loads this GLB and transitions to a lobby node. Existing indoor behavior is not evidence that the GLB interior works. |

## Rights and customization

The repository provenance record identifies the creator as 99.Miles and records
CC BY 4.0 plus founder-confirmed asset identity. A fresh source-page fetch was
blocked by HTTP 403; the source licence label was not reverified live in this
assessment. The Creative Commons deed was checked live: commercial adaptation
and redistribution are permitted with attribution, licence link and indication
of modifications. Copyright is retained; this is not public-domain material or a
software open-source licence. No endorsement may be implied. The deed does not
guarantee third-party rights, including depicted branding.

Sources: [asset source](https://sketchfab.com/3d-models/free-atlanta-corperate-office-building-d96380fb001345cca9a9be121f3e43d5),
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), and
[existing provenance record](asset-provenance/HSD-ASSET-001-hq-exterior.md).

Preserve existing credit requirements and modification notices. The recorded NoAI
operating restriction remains binding: deterministic Blender editing under founder
direction is permitted by the project decision; do not submit asset geometry or
textures to generative systems. The embedded copyright notice is still an open
production obligation. Existing roof advertising needs separate branding/right
review or removal in an authorized derivative.

## Choice comparison

| Approach | Best fit | Remaining work |
|---|---|---|
| Retain exterior, rebuild interior | Existing tower appearance is wanted; only selected interior zones are needed. | Scale/origin cleanup, facade/branding adaptation, new interior and entrance connections, collision, LOD/texture work, streaming partitions, attribution. |
| New modular building | Spatial layout and identity should follow service journeys rather than this tower. | New architectural concept, editable Blender master, UV/materials, interiors, collision, budgets and visual approval. More initial modelling; stronger control over spatial structure. |

No time/cost estimate or unconditional replacement claim is justified yet. A
production decision needs the approved spatial brief and measured performance.
