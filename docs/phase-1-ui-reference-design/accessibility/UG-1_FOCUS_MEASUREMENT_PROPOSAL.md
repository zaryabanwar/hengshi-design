# UG-1 — Focus adjacency and measurement proposal

**Direction: Alternative A approved under D-055; independent nonauthor review PASS.**
**Measurement protocol: proposed basis; candidate-specific verification remains gated.**
**Date:** 2026-10-03. Independent accessibility specification author, D-044 pattern.
This document approves no geometry, colour token, implementation, scene asset, conformance claim, Figma call, publication, commit or push. No measurements exist.

Founder approval on 2026-10-03 selects opaque backing and expressly authorizes
the requirement amendment. Alternatives below preserve the reviewed proposal as
provenance; references to pending choice are historical, superseded by D-055.
Geometry, tokens, scenes, implementation and measured conformance remain gated.

## Authority and scope

`NFR-A11Y-005` requires a persistent focus indicator at ≥3:1 against every adjacent scene colour, plus non-colour/non-motion cues. Style guide §4.1 carries a 3 px hotspot ring requirement, but its prototype colour/emission values are not approved production values. `OBL-CTRL-04` and amendment UG-1 require an adjacency definition and reproducible measurement procedure before that claim is testable.

WCAG 2.2 AA requires visible keyboard focus (2.4.7), applicable authored state indicators to contrast with adjacent colours (1.4.11), and focused components not to be entirely hidden by author-created content (2.4.11). Its 2.4.13 focus-area and focused-versus-unfocused contrast criterion is AAA, not an AA requirement. The project's persistent 3 px ring and every-adjacent-scene-colour rule are additional project obligations. Do not treat a focus screenshot as full WCAG proof. W3C Understanding documents explain the normative criteria; they are informative.

This proposal distinguishes authored hotspot/scene indicators from native HUD radio controls. D-054 preserves native radio checked marks and platform focus rendering. Neither alternative authorizes replacing, recolouring or restyling that native indicator. Native radios and Apply remain separately keyboard-tested in their actual HUD/shell surroundings. The UA-appearance exception in 1.4.11 does not erase the project's existing obligations; any conflict needs explicit review.

## Alternatives and recommendation

| Alternative | Proposed geometry and adjacency | Consequence |
|---|---|---|
| A — Opaque backing around authored indicator | A solid backing extends on both sides of the complete focus-ring path. The ring's immediate inner and outer neighbours are backing pixels; no scene, texture, transparency, blur or bloom may intrude into those neighbours. Backing thickness, ring geometry, colours and layering remain unchosen. | Stable local contrast is easier to prove, but measuring ring-to-backing alone does **not** satisfy the current literal every-adjacent-scene-colour obligation. Founder must approve an explicit requirement amendment making the backing the ring's adjacent surface, together with a visibility/occlusion safeguard and updated traceability. |
| B — Direct scene adjacency | The ring directly borders the rendered scene/control on each relevant edge. Adjacency includes every distinct visible colour immediately touching the inner or outer boundary, not a mean or a conveniently selected screenshot patch. | Retains the current scene-colour obligation. Every reachable lit, textured and animated background must be covered; a fixed colour may fail when luminance approaches that colour. No guarantee is assumed. |

**Recommend A**, subject to the explicit requirement amendment, because separating
the authored indicator from varying scene colours permits a controllable contrast boundary. The backing must not cover the target, label or another focused control; the focus cue remains geometrically distinguishable and persistent. Its outer scene boundary still needs qualitative visibility inspection; backing contrast alone does not prove the target remains recognisable. If the founder wants the existing scene-colour requirement unchanged, choose B and accept its proof burden. A is not a shortcut that silently reinterprets the requirement.

## Proposed measurement protocol

1. Freeze the approved candidate geometry, compositing order, tokens, scene revision, lighting/material settings, camera states, stream profile and test matrix. Record browser/OS versions, viewport, zoom, device-pixel ratio, colour space, motion mode and rendering settings. Unapproved prototype assets cannot prove production compliance. No threshold or geometry value is selected here.
2. Define the focus ring's geometric path and the adjacent regions from that candidate, before inspecting results. For A, both adjacent regions must lie wholly within the opaque backing. For B, they are the immediate scene/control regions along both ring boundaries. Evaluate the whole perimeter, including corners and label/HUD intersections, with no averaging or omitted failing region.
3. Use authored/UA-resolved colours for solid CSS surfaces. For composited WebGL surfaces, export final composited, colour-managed colour samples and geometry masks using a documented capture method; include lighting, texture, alpha and postprocessing. Reject ambiguous colour-space or HDR-to-SDR conversion evidence. Use the WCAG relative-luminance formula and contrast ratio; never round a value below 3:1 into a pass. Keep exact minima and their coordinates.
4. Spatial coverage: test every distinct adjacent solid colour. For variable surfaces, evaluate all pixels in the declared adjacent regions of the native resolution capture. Exclude antialias fringe from the authored base-colour calculation using the predeclared geometry mask, never by deleting low-contrast samples after seeing results. Inspect the actual rendered fringe separately; clipping, a disappearing core or visibly indistinct focus blocks acceptance.
5. Temporal coverage: keep focus on each reachable target through every bounded approved animation/camera/lighting sequence, recording every rendered frame from focus acquisition through completion and stable state. Repeat for allowed interactions that alter its backdrop while focus remains. Do not use periodic screenshots or only beginning/end frames. Include loading/interruption/overlay states in which that target remains operable. Record the worst frame.
6. An exhaustive finite capture proves only that frozen run. For random, procedural, unbounded or user-controlled continuous scenes, require a justified bound on all possible adjacent luminances and ring output, or a constrained approved rendering envelope. Without it, universal contrast coverage is **BLOCKED**, even if every sampled screenshot passes. A regression sample cannot be labelled proof against every future scene colour.

For A, verify backing opacity, complete perimeter coverage, invariant compositing and unobscured ring throughout the same scene envelope; then compute all actual ring/backing pairs. It is not sufficient to measure nominal token colours if lighting, blending or overlays alter the output. For B, compute all ring/adjacent scene pairs or prove their lower bound throughout the declared envelope.

## Evidence matrix and deterministic acceptance

- Independently test S-HIGH, S-MEDIUM and S-LOW using their own actual rendering; no inherited contrast result. S-SEMANTIC has no canvas: inspect its semantic control surfaces and native keyboard focus independently.
- Cover applicable VP-320, desktop, landscape, and 400% zoom/reflow conditions, plus device-pixel ratios that change the ring rasterisation. Use the then-current approved browser matrix (latest two stable Chrome, Edge, Firefox and Safari families; the existing Safari/iOS minimum-floor obligation remains separate). Exact combinations and reachable targets must be enumerated before testing.
- Repeat standard and reduced-motion paths; focus never relies on motion, and suppressed flights/transitions become their approved cuts. Check forced-colors on a real supported OS/browser, not only emulation; native marks/focus remain visible under D-054. Capture keyboard traversal and static non-colour cues. WebGL colours are not assumed to adapt automatically to OS forced colours.
- **PASS for the declared scope:** every applicable pair/bound is ≥3:1, with complete spatial/temporal coverage; persistent, unobscured focus and the approved non-colour/non-motion cue remain visible. Geometry must satisfy its separately approved dimensions. For A, the requirement amendment is a prerequisite.
- **FAIL:** any required contrast pair below 3:1 or any missing/clipped/obscured required cue within the declared test scope. Report exact target/frame/location.
- **BLOCKED:** absent approved geometry/assets, missing matrix cells, unresolved colour conversion, an unbounded scene without a proof envelope, or an unapproved requirement amendment. Missing evidence is never a pass.

Each evidence row records target, stream, browser/OS, viewport/zoom/DPR, motion and forced-colors mode, approved revisions, capture/mask procedure, temporal envelope, minimum ratio and location/time, visibility result, reviewer and limitations. Retain raw captures and calculations alongside the review. No full-page/process conformance claim follows from passing this focus-specific protocol.

## Inputs and founder decision

**Choose A with explicit amendment authority, or B retaining the existing
scene-colour requirement.** Approval would select a direction only. Subsequent geometry/token approval, independent method review and implementation gates remain.

Missing inputs: approved indicator/backing geometry and layering; colour/token values; authorized per-stream scene/lighting/material/camera references; bounded motion/interaction envelopes; and the dated browser/viewport/zoom/DPR matrix. Until supplied, this is a proposed method and cannot produce measured results.

## Primary references

- WCAG 2.2 normative Recommendation.
- W3C: Non-text Contrast.
- W3C: Focus Visible.
- W3C: Focus Not Obscured (Minimum).
- W3C: Focus Appearance (AAA).

Local authority: `docs/active/Hengshi_Design_SRS_v3.md` NFR-A11Y-005; `docs/active/3D_Mega_Menu_Style_Guide_v2.md` §§4.1, 7.3, 8.2.4; `DELIVERY_STREAM_ACCESSIBILITY_OBLIGATIONS.md` OBL-CTRL-04; `DESIGN_SYSTEM_AMENDMENT_R-039.md` UG-1; DECISIONS D-044/D-045/D-054.
