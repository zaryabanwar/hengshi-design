# Nature campus visual prototype — v1

Status: DOING. Founder requested an isolated low-detail prototype and browser
viewer on 2026-10-04. No production implementation or appearance acceptance.

Sources: PROJECT.md service architecture; D-064 movement direction; D-065
architecture; D-066 modular headquarters; D-067 nature-integrated art direction;
the [selected original concept board](../../docs/phase-1-3d/concepts/nature-campus-direction-2026-10-04.png).

Includes central reception, five named service wings, connecting paths, simplified
trees/mountains/water and a representative information board/consultation space.
The current exported GLB comes from `build_composition.py` and
`nature-campus-composition.blend`. This replaces the first study's generic pavilion
arrangement with a larger reception, varied wings and a continuous river valley.
`build_blockout.py` / `nature-campus-blockout.blend` preserve the first version;
`build_refined.py` is a stopped, superseded refinement attempt. The protected
Atlanta GLB and application remain untouched.

`01-campus-overview.png` and `02-arrival.png` are composition renders.
`03-department.png` is a stale first-version render and must not be presented as
the current model's department. Current same-model browser views and the
source-grounded layout comparison are now in the
[spatial storyboard](../../docs/phase-1-3d/spatial-storyboard.html) and its
[spatial contract](../../docs/phase-1-3d/SPATIAL_STORYBOARD.md). Appearance/layout
acceptance and a connected walkable model remain pending.

index.html is a local Three.js inspection viewer, reusing the existing installed
prototype dependency. It does not select a production dependency version.
The first version passed model-loading/control checks; early composition checks
timed out. Fresh Playwright inspection on 2026-10-04 loaded the current composition,
operated Arrival/Department controls and captured all three current browser views
in `output/playwright/definition/model-*.png`, with no console errors/warnings.
The department board is visible in that camera. This is a desktop viewer check,
not mobile performance, sustained frame-time, accessibility or geometry acceptance.
This remains a simplified composition study, not a faithful material match or
accepted spatial specification. The founder described the revised overview as
better; that is not acceptance of the complete production appearance.

The raw current GLB is 8,945,052 bytes. It is not a compressed production
transfer manifest and does not demonstrate the accepted desktop/mobile budgets.
Inspection on 2026-10-04 found 45 meshes/nodes, 11 materials and no authored named
collision geometry. The river footprint overlaps the Immersive wing, and the
right-hand connectors need supported crossing/collision proof. A plan overlap
alone does not prove structural intersection or a safe route. The storyboard
records these gaps without changing current geometry or extending revision gates.
The viewer's current product label is v1 under D-069; numerical query parameters
identify the existing study/cache artifact, not a later product release.

Not implemented: free walking/collision, streaming, sound, staff availability,
booking or production UI. Clear prototype/no-live-staff wording prevents implied
operational functionality. Scene scale, accessibility and full route parity remain
definition/verification work. No commits or pushes performed.

Local preview: http://127.0.0.1:8766/artifacts/nature-campus-prototype/index.html?composition=3
The local server must remain running. Three.js modules currently resolve from
apps/web/node_modules; this viewer is not a standalone distribution.
