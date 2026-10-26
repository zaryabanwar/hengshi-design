# Spatial storyboard and connected-campus contract — v1

Status: DOING. Proposed 2026-10-04 under D-064/D-065/D-066/D-067, the accepted
wayfinding release map and World experience definition. This artifact supplies
spatial/journey review, not production screen, geometry or implementation approval.
Use the [browser storyboard](spatial-storyboard.html) to inspect the same evidence.

An earlier review attempt ended on workspace credits without a verdict. The
[later amendment review](../phase-1-architecture/contracts/reviews/current-definition-amendments-2026-10-04.md)
records bounded PASS for this connected-campus definition at its listed hash.
Those [reviewed bytes](../../output/research/contract-review-reference-reconciliation-2026-10-04/SPATIAL_STORYBOARD.pre-status.md)
are preserved; this page's later reference update does not replace that identity.
The earlier failure remains history, not the current review state. Final connected
geometry, screen references, physical-device budgets, rights and appearance
acceptance remain held. A reviewed spatial proposal or inspected screenshot is
not a traversable production campus or integrated founder acceptance.

## Authority and scope

The [World definition](WORLD_EXPERIENCE.md) owns movement, content, audio and
loading intent; [wayfinding](../phase-1-ux-architecture/wayfinding-release-map.csv)
owns formal titles, canonical links, room keys and opening sequence. This
storyboard binds that intent to a reviewable layout and names the geometry gaps.
It does not create a competing service taxonomy or reopen accepted boundaries.

Foundation/reception, concierge, handoff and direct booking precede wing release.
The accepted wing order is AI + Data, Strategy, Immersive + Creative, Digital +
Growth, then Cloud + Reliability. The current prototype's Strategy interior is
a representative visual fixture, not authority to release that wing first.
All five volumes may be visible in a private layout study without being open to
public traversal. Production thresholds obey eligible publication and sequence.

## Current geometry evidence

Inspected the existing generator, raw GLB scene metadata and current browser views.
The generator uses Blender XY for the plan; glTF maps it to X/-Z with Y vertical.
Units are model units; a verified real-world scale or dimensional clearance is
not established. The browser plan uses equal X/Y projection, not geographic north.
Gold links show the representative sequence rather than a verified walking path.
The diagram scrolls horizontally on small screens and has a keyboard-focusable
region; the complete journey and geometry limitations are also available as text.

| Volume | Generator centre XY | Shape parameters rx / ry / height | Current role |
|---|---|---|---|
| Reception | -3 / 12 | 15 / 11 / 7.2 | Largest central volume and welcome desk. |
| Strategy & Transformation | -29 / -5 | 12 / 8 / 5.1 | Representative information board and consultation seating. |
| Digital Products & Growth | -32 / 27 | 14 / 9 / 5.5 | Future wing volume; no finished department interaction. |
| AI, Data & Automation | -6 / 49 | 13 / 9 / 6 | Future wing volume; first wing in production release order. |
| Immersive & Creative | 28 / 39 | 14 / 8 / 5.6 | Footprint intersects river; geometry needs reconciliation. |
| Cloud, Reliability & Trust | 36 / -3 | 13 / 9 / 5.3 | Connector crosses river; bridge/collision readiness unproven. |

These are contour inputs, not measured floor dimensions or approved clearance.
The river generator has centre x = 20 + 7 sin(0.035y) + 4 sin(0.09y), half-width
3.6 model units. At y=39 its centre is x≈25.412, within 3.6 of the Immersive wing
centre x=28. Thus the horizontal footprint overlap is observable; it does not
alone establish a 3D intersection, structural support, collision or safe crossing.
The right-hand connectors are paving strips, not authored bridge structures.

Raw GLB: 8,945,052 bytes, 45 meshes/nodes, 11 materials, zero animations;
KHR_materials_transmission and KHR_materials_ior declared. No objects are named
as authored collision/navmesh/walkable geometry; the viewer implements no walking
or collision. Absence of those names alone is not a general mesh-usability test.
No independent chunk manifest, service-room subdivision or loaded-neighbor
controller is implemented. Batched forests/terrain and a single GLB are inspection
choices, not the production streaming decomposition.

Material inspection finds zero texture/image records: all 11 materials use solid
PBR colour factors. Named materials include honey timber, warm paving, valley and
roof meadow, river, stone, tinted glazing, leaves, earth plaster, information
display and forest green. Glazing declares transmission/IOR; that does not prove
the final browser/device appearance. Material names and linear colour factors do
not establish a match to the concept or the accepted interface colour tokens.

This explains part of the blockout appearance: no authored timber grain, planted-
roof surface or interior surface texture is present. Adding textures alone cannot
repair repeated building proportions, floor/entrance gaps or river crossings. The
[World asset/material definition](WORLD_EXPERIENCE.md#scene-materials-and-reusable-asset-families)
names the proposed reusable families and the scoped D-067 brand reconciliation;
that expansion has the bounded amendment review identified above. Its preserved
inspected bytes, held production inputs and visual acceptance remain separate.

### Exported connector inspection

A later read-only Blender 5.0.1 probe imports the same GLB, excluding factory
startup objects. It inspects its 45 mesh objects in Blender world coordinates
with triangle BVH rays. The
[inspection script](../../output/research/campus-geometry-2026-10-04/inspect_export.py),
[raw observations](../../output/research/campus-geometry-2026-10-04/inspection.json)
and [diagnostic plan](../../output/research/campus-geometry-2026-10-04/plan.html)
preserve the method, object names, sampled points and intersection coordinates.
This inspection does not save, render, export or revise the campus scene.

All five 20-segment connector centrelines intersect exported Reception glazing
at diagnostic Z=1.4. Digital, AI and Immersive also intersect the welcome desk.
Four routes intersect their destination wing's glazing; AI reaches its wing's
front opening but still intersects Reception glazing and the desk. These are
render-mesh intersections, not results from an implemented walking controller.

| Proposed connector | Other observed centreline intersections | Sampled points above exported water, out of 201 |
|---|---|---:|
| Strategy | Strategy glazing | 0 |
| Digital | Welcome desk; Digital glazing | 0 |
| AI + Data | Welcome desk | 0 |
| Immersive + Creative | Welcome desk; timber column; Immersive glazing | 38 |
| Cloud + Reliability | Cloud glazing | 31 |

All 201 source-curve samples per connector and 541 arrival-line samples have
named paving/terrace beneath them. This narrows the earlier unproven connection:
sampled floor coverage exists, while routes still require deliberate exits,
entrances and obstacle clearance. A paving strip above water is not a supported
bridge or proof that the room footprint, banks and water exclusion are resolved.
The probe height, density and model units are diagnostic choices, not accepted
human dimensions, step tolerances or accessibility clearances. Centreline rays
cannot prove full-width or continuous safe navigation, slope, structural support
or the untested surrounding geometry.

The diagram projects selected exported triangles and observed hit points; it is
not a new architectural appearance or approved walking map. The initial probe's
factory-cube-inclusive inventory and a pre-plan intermediate remain separate
noncanonical diagnostic records; only the final imported-object observation is
used here. This additional evidence awaits its own bounded independent review.

Evidence identities at inspection:

- `artifacts/nature-campus-prototype/build_composition.py` SHA-256:
  `8a2a8e6814a3edba881b1b9807b2837638bc6b5b3c3e56aa25413c57f5198972`.
- `artifacts/nature-campus-prototype/nature-campus.glb` SHA-256:
  `7ad9ee472b2e0f51a7e5e2107a88060258e43d87a9ddedceb887b6ebba0b94d8`.
- Current three browser screenshots: `output/playwright/definition/storyboard-overview.png`,
  `storyboard-arrival.png`, `storyboard-department.png`; same loaded GLB and
  existing overview/arrival/department controls, captured 2026-10-04.
- `artifacts/nature-campus-prototype/03-department.png` remains a stale earlier
  Blender render and is excluded from current three-view evidence.

## Six storyboard beats

| Beat | Spatial/interaction requirement | Equivalent/recovery | Evidence required before acceptance |
|---|---|---|---|
| 1. Semantic site and deliberate entry | Read, contact or Book without World; apply supported graphics selection and explicitly enter. | Quick Access remains peer content and conversion; capability loss stays truthful. | Approved homepage/selector reference and no-JS semantic journey. |
| 2. Arrival | Dominant reception visible along an understandable path; optional travel can stop/skip. | Stable destination/reduced-motion alternative; Exit/Quick Access always usable. | Same-model arrival camera, authored ground, entrance clearance and control reference. |
| 3. Reception | Directory, Reception AI Concierge, sourced information and direct Book occupy distinct deliberate contact points. | Semantic directory/help/booking; decorative desk is not availability. | Coherent central space, accessible published panels and approved action mapping. |
| 4. Eligible department | Safe path to an open threshold; formal service names, evidence and canonical actions match active release. | Held/closed rooms refuse entry and offer truthful canonical/Book recovery. | Threshold state, room layout, collision readiness and release-sequence proof. |
| 5. Guidance or consultation | AI clearly identified; human contact needs explicit current availability and consented sharing. | Offline/unavailable returns Book/Contact; declining sharing preserves browsing. | AF-01/AF-02 process and service-backed state, not a model person or desk. |
| 6. Return, reverse and failure | Retarget/reverse with current/adjacent/recent safe ground; opening a panel stops travel. | Loading/corrupt chunk holds last safe position, Stop/retry/Quick Access; process data preserved. | Failure/reversal/cancellation tests on actual runtime and independently reviewed budgets. |

Exact gesture and presence presentation remain proposed until their approved UI
reference exists. This storyboard is an internal document; it does not replace
B01 production screen evidence or authorize a production HUD.

## Required spatial reconciliation

1. Establish one coherent model-unit scale, entrance and floor-height specification;
   author separate collision surfaces, threshold boundaries and water exclusion.
2. Resolve the river/wing relationship and both east-side crossings. A raised
   supported crossing or revised siting must be represented consistently in the
   overview, arrival, interior and traversal geometry; no invisible teleport over
   absent ground. Exact design remains an appearance/layout acceptance item.
3. Connect the promenade, reception floor and each eligible wing entrance through
   authored routes rather than treating visual overlap as path continuity.
4. Give wings genuinely distinct proportions and terraced landscape relationships
   while preserving the selected reception hierarchy and brand/material direction.
   Current repeated roof language/flat campus is still a loose concept match.
5. Subdivide each eligible wing into the canonical service-room/content destinations;
   include information/evidence and help points without inventing live staff.

No current campus or Atlanta geometry was changed by this inspection/storyboard.
Any further substantial model revision stays subject to the phase revision limit
and its applicable design gate. This document does not silently extend that limit.

## Proposed export topology and loading proof

Author separate arrival/exterior, reception, each wing/interior and connected
landscape chunks, with shared immutable material/vegetation assets and distant
scenery variants. Exact chunk borders follow the approved layout and measured
residency budget, not arbitrary equal-size tiles. Give every chunk stable logical
identity, release/checksum, variant, dependency and collision-readiness metadata.
Define ownership/reference counts so shared assets survive neighbor eviction and
are disposed on final release/exit. No movement telemetry or second content store.

Current, immediate connected neighbors and recently traversed safe ground must
remain available under the accepted World contract. Interior entrances and river
crossings require ready collision/ground before travel crosses the boundary.
Reversal reprioritizes loading without instantly evicting behind the visitor.
Stream detail can vary; core route/actions and accepted stream lock cannot.

Retain approved initial lazy 3D transfer ceilings 8 MB desktop / 4 MB mobile and
incremental room ceilings 5 MB / 2.5 MB. Define measurement units, cold/warm profiles,
compressed transfer versus resident geometry/textures, actual supported devices,
frame-time percentiles, memory, thermal and network conditions before acceptance.
The current whole GLB alone exceeds either desktop interpretation of 8 MB/MiB;
it is not a production transfer or loaded-room proof. No unmeasured FPS, byte-per-
tree estimate, radius, speed or memory cap is selected here.

The [World sound-zone definition](WORLD_EXPERIENCE.md#sound) specifies exterior
nature, sheltered reception and quieter department contexts. These are optional
atmosphere, not service/status signals or simulated staff. Enabled user intent and
active-release eligibility control playback; loading a neighboring area is not a
playback trigger. Asset loading or turns must not reset mute/volume or create
abrupt layered playback. Declining audio avoids optional sound downloads; hidden
tabs pause it, and a missing asset preserves a silent equivalent journey.
Audio assets/rights, loop limits and transition budgets still need their reviewed
specification. Decorative sounds never carry sole service/availability information.

## Exit criteria and remaining gates

Accept the same-model three-view composition, connected floor/river/entrance layout,
service-room and truthful contact-point mapping, approved movement controls,
chunk/export contract and measured device/loading/audio budgets together. The
current browser views prove only one loaded model with three functioning cameras.
Independent review and founder appearance acceptance remain separate; this
artifact cannot certify walking, streaming, performance or a finished 3D asset.
