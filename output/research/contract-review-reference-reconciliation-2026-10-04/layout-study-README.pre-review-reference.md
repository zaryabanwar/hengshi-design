# Nature campus layout study — v1

Status: DOING. Final third isolated model revision, 2026-10-04. No production
implementation, accepted architecture appearance or complete Phase 1 acceptance.

Direction comes from D-066/D-067, the original
[selected concept](../../docs/phase-1-3d/concepts/nature-campus-direction-2026-10-04.png),
[World definition](../../docs/phase-1-3d/WORLD_EXPERIENCE.md) and
[spatial contract](../../docs/phase-1-3d/SPATIAL_STORYBOARD.md).
The [independent accounting review](../../docs/phase-1-3d/reviews/model-revision-accounting-2026-10-04.md)
identified the earlier false exhaustion gate: initial creation, stopped
refinement counted as cycle 1, composition rebuild as cycle 2. This is cycle 3
within that existing limit, not a new phase or an extension.

Open [the browser viewer](http://127.0.0.1:8766/artifacts/nature-campus-layout-study/index.html).
Overview, Arrival and Department use one export. The concept and earlier model
remain available for direct comparison. This viewer requires the existing local
8766 server and installed prototype Three.js modules. It selects no production
dependency version. No-JavaScript visitors can inspect the three same-model renders.

The study adds varied two/three-lobed planted roofs, branching reception supports,
graded terrain, denser forest, deliberate wing-facing openings and two visible
river crossings with piers and rails. It retains reception plus five service wings
and a representative Strategy information/consultation fixture; that fixture
does not alter the accepted first-wing release order. There are no simulated staff.

Original procedural geometry/materials are in `build_layout.py`; editable source
is `nature-campus-layout.blend`; export is `nature-campus-layout.glb`.
No Atlanta mesh/textures, external library assets or downloaded scenery were used.
Concept resemblance does not certify third-party rights or production provenance.
All original application, Atlanta asset and earlier campus bytes remain intact.

## Observations and limits

`layout-observations.json` preserves proposed units, module parameters, source
identity, routes and cameras. Scale is proposed at one Blender unit per metre;
architectural dimensions, accessibility clearances and safety remain unaccepted.
Blender 5.0.1 ran successfully as an inspection/build tool, not a selected
production matrix. Context7 `/websites/blender_api_current` and its linked official
Mesh/glTF documentation were consulted 2026-10-04; the exact installed exporter
executed. No tools or dependencies were upgraded.

`inspect_layout.py` imports the exported render meshes read-only. Its
`geometry-inspection.json` reports 81 centreline points plus two lateral offsets
per wing, and segment rays at proposed floor + 1.4 units. All five sampled routes
have named floor coverage, no tested glazing/frame/desk/column segment hits, and
no sampled terrain above the floor. East-side water is observed under 44 Immersive
and 51 Cloud sample positions; crossing meshes are present. This is finite
render-geometry evidence, not swept-body collision, continuous ground, rail safety,
structural, slope or accessibility certification.

The 20,860,132-byte whole GLB contains 117 exported mesh nodes and solid PBR colours.
It exceeds the accepted initial production transfer ceilings. No chunk loading,
LOD pipeline, realistic timber/plant textures, movement, collision controller,
streaming, sound or booking is implemented. It remains a low-detail interpretation;
the concept's detailed foliage, mountain silhouettes, material realism and room
composition are not faithfully reproduced.

Playwright checked desktop camera controls, a 390 × 844 viewport without horizontal
overflow, keyboard camera activation, three no-script render alternatives and no
page/console errors. This is viewer behavior only, not physical-phone performance
or WCAG certification. Independent review and founder visual disposition follow;
any further substantial model correction needs a revision-limit decision.
