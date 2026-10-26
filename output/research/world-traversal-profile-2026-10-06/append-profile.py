"""Define candidate World controls/traversal; preserve current model and predecessors."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
WORLD = ROOT / 'docs/phase-1-3d/WORLD_EXPERIENCE.md'
BUILD = ROOT / 'docs/phase-1-3d/CAMPUS_ASSET_BUILD_SPEC.md'
for path in (WORLD, BUILD):
    with (OUT / (path.name + '.before')).open('xb') as file:
        file.write(path.read_bytes())
text = '''
## Mouse/touch traversal and camera profile proposal — 2026-10-06

Status: DOING. This refines the proposed mechanics under [Movement and access](#movement-and-access)
and the accepted D-064 scope; it does not approve production controls or modify
D-071's layout/model. Exact numerical values below are unmeasured engineering
starting targets, not browser, accessibility, building-code or device-fitness
standards. Apply the same essential movement/clearance rules in every 3D stream;
Quick Access remains equivalent without WebGL. This is a client-side traversal
profile, not private-content authority or a second scene/publication manifest.

### Proposed visitor controls

Desktop default: primary-button drag on empty scene space looks around. An explicit
DOM Move action starts continuous travel in the selected forward/back/left/right
direction; a persistent Stop action ends it. Movement direction is camera-yaw
relative on the ground plane, never derived from camera pitch. While moving,
dragging the empty scene can steer by changing yaw; looking upward does not fly.
Single-click a valid ground point to choose collision-safe directed travel; clicking
a board/department/control invokes its own action instead of setting a floor target.
A floor request cancels continuous mode, and choosing continuous movement cancels
the prior route. Only one current travel intent exists. Right-click/context menu,
pointer lock, hover, wheel and a drag-release click are not alternate start actions.

Touch default: an optional visible thumb movement pad supports continuous planar
movement while engaged, and a scene drag controls look. Release/cancel of that pad
stops its travel. A one-pointer alternative uses the same explicit Move/Stop,
direction buttons, Look left/right/up/down, Reset look and destination controls;
the visitor need not drag or use two fingers simultaneously to reach equivalent
positions, orientations, content or processes. The pad cannot be the only way
to move, and keyboard controls alone are not the alternative for touch users.
Exact pad shape, pointer-down/drag cancellation semantics and comfort require the
approved B01 reference and input/accessibility inspection before implementation;
this proposal does not claim its hold gesture already satisfies WCAG 2.5.2.

Move/direction/destination activation occurs on an uncancelled pointer-up or native
button activation, never a hover/down-only commitment. Stop is an abort control
and may stop earlier. Scene drag and pad gestures are explicitly owned by the
engaged pointer; cancel, lost capture or device interruption clears that intent.
Do not convert a drag into a synthetic floor/board click. Use temporary element
pointer capture only during the engaged gesture, releasing it on end/cancel;
no browser pointer lock or capture trap is required to read, use Stop or Exit.
Initial gesture separation target is eight CSS pixels for mouse and ten for touch;
these thresholds need physical-device/usability validation and cannot substitute
for native button, focus or assistive-technology activation.

Proposed camera sensitivity is 0.2 degrees per CSS pixel horizontally/vertically,
with Look buttons stepping yaw by 15 degrees or pitch by 10 degrees and Reset
look returning pitch to horizontal without moving the body. CSS pixels, not device
pixels, keep the gesture independent of rendering scale. Relative displacement
is consumed only from the current owned gesture, not from a stale pointer event.
Pitch is clamped and yaw wraps; there is no inertia after release. Drag sensitivity
and step sizes are comfort targets, not proven acceptable across devices.

Browser pinch zoom stays available; do not use user-scalable=no or disable zoom on
the whole document. Evaluate narrowly scoped touch-action for scene/pad gestures
without suppressing scrolling, pinch zoom, text selection or ordinary controls in
DOM panels. Browser takeover produces cancellation and stops travel. Do not assume
one CSS value has identical supported behavior on every required browser/device.
The inspection viewer's orbit and centre-target zoom stay inspection tools;
production walking uses the body/eye camera, not that orbit target.

All controls are actual named, focusable DOM actions with visible focus and current
moving/direction state. Stop, Exit, destinations, orientation and core actions
remain keyboard operable; no global WASD binding is selected. Opening any content/
help/booking panel stops travel and clears pad/continuous/route state. Leaving the
World interaction focus domain, document/application visibility loss, context loss,
release invalidation, input cancellation or Exit also stops movement. Returning,
closing a panel or restoring resources does not resume old travel automatically.
Focus transitions within the World controls are not mistaken for leaving it.
Reduced motion removes decorative camera drift/bob and animated destination travel;
an explicit stable destination change still requires current eligible readiness.
No wheel-driven movement, forced orbit, jumps, sprint, motion sensor or timed skill.

### Proposed human-scale and camera targets

| Parameter | Initial proposal | Interpretation |
|---|---:|---|
| Frame | Metres, right-handed, Y up | Same approved glTF/scene/collision frame; apply each transform once. |
| Body | Upright capsule, 0.30 m radius, 1.70 m total height | Cylinder half-height 0.55 m plus radius at both ends; height is not the half-height parameter. |
| Body-to-obstacle offset | 0.02 m | Additional conservative controller separation; not permission to penetrate or shrink at a doorway. |
| Eye height | 1.60 m above admitted supporting ground | Inside the upright body; no automatic roll, bob or orbit. |
| Ground-plane travel speed | At most 1.20 m/s | Normalize diagonal intent; no faster backwards/diagonal movement or pitch-based flight. |
| Walking support slope | At most 25 degrees from horizontal | Steeper ground is excluded; normal authored visitor routes target at most 5 degrees. |
| Automatic stair climbing | Disabled initially | Author smooth thresholds/ramps; never step over closed boundaries or use a visual stair as an admitted route. |
| Permitted support snap | At most 0.04 m | Only between continuous admitted supporting surfaces; never snap across a hole/river/unready border. |
| Minimum authored public passage | 1.20 m clear width, 2.10 m clear height | Measured after transforms with body/offset and turns accounted for; these are virtual authoring targets, not physical-code claims. |
| Perspective camera | 60-degree vertical field of view | Horizontal view derives from aspect ratio; resizing cannot hide required DOM controls. |
| Camera pitch / roll | -65..+65 degrees / zero | Full wrapped yaw; no inverted/underground viewpoint or pitch-induced travel. |
| Camera near / far planes | 0.05 m / 1,000 m | Initial depth range; author distant silhouettes inside the qualified far range, and inspect precision/clipping before acceptance. |
| Movement integration | Fixed 1/60-second ticks; at most four ticks per render opportunity | Maximum accepted catch-up is 1/15 second; discard excess elapsed travel intent rather than teleport after a stall. |

Clamp actual movement to speed × admitted simulation time, after collision and
support checks, not render FPS or an unconstrained wall-clock delta. Interpolation
may display only between already admitted poses; it cannot extrapolate through
an unready edge. Stop/cancellation clears the accumulator and unconsumed input.
A delayed/background frame therefore cannot advance the body through old travel.
All targets require bound numeric/finite input and current profile identity; NaN,
Infinity, unsupported geometry or incompatible unit/transform binding denies motion.

The camera range is a starting proposal, not proof that today's study is at this
scale or that terrain outside it disappears acceptably. Qualify all-around near,
middle and distant landscape from every permitted visitor position/yaw, including
reversals. Authored terrain transitions, distant silhouettes, sky and controlled
atmosphere must form a coherent horizon; no walking position may expose a raw
island edge, unfilled backdrop gap or repeating mountain wall. Decorative distance
does not become walkable territory or justify downloading the entire world.
The inspection overview may expose a study boundary; it does not replace this
eye-level production criterion or accept a new composition/model revision.

### Collision, readiness and intent safety

Evaluate the proposed existing Rapier kinematic character controller first under
the complete compatible stable graph. Its shape-based translated movement does
not itself choose camera rotation, a route, active publication, ready areas or safe
support. The capsule includes body/head clearance; use swept-body checks rather
than a single centreline floor ray or endpoint collision test. No selected package,
WASM profile, adapter API, dynamic-body push or custom physics engine is introduced.
Exact candidate query/filter/offset/slope behavior needs source and geometry tests.

One authoritative client mover consumes the current immutable intent generation.
Continuous and directed movement share that mover, support checks and current
collision interpretation; a navmesh/path is a proposal, not permission to traverse.
Exclude staged/ineligible colliders from movement queries. Every admitted swept
segment and required supporting footprint must be covered by current ready ground
and collision; a successful obstacle query or streamed visual alone proves neither.
Protect the supporting surface/resources under the existing lease/retirement rules.
An unready boundary stops at the last admitted safe pose and offers truthful
waiting/retry/semantic access. Direction reversal changes demand/priority under
the existing scheduler; it does not bypass readiness, queues or memory targets.

Reject negative/unknown support, walls, water/edges, narrow turns, overhead collision
or withdrawn/closed/unready crossings; no gravity-driven fall or automatic steep
slide. Keep body and camera upright at the last known safe pose. If that pose loses
eligibility or cannot be established, stop traversal and expose approved recovery;
do not invent supporting ground, relocate into another room or revive old travel.
Return to reception/destination recovery is explicit and must resolve its own
current eligible safe pose. Release refresh, context recreation and resource
cleanup keep the existing gates and [measurement profile](WORLD_MEASUREMENT_PROFILE.md).
Collision/support resources cannot be evicted to keep decorative frames smooth.

### Primary support and acceptance

Checked 2026-10-06: Context7 `/websites/rapier_rs_javascript3d` and the
[official controller guide](https://rapier.rs/docs/user_guides/javascript/character_controller/)
describe translated shape-based control, offset, Y-up/slope/step/snap configuration;
they do not authorize the table's values or make renderer/campus safety automatic.
The [pointer cancellation](https://www.w3.org/WAI/WCAG22/Understanding/pointer-cancellation.html)
and [dragging alternatives](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html)
guidance distinguish cancel-safe controls, single-pointer alternatives and keyboard
operability. [MDN pointercancel](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointercancel_event)
and [touch-action](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/touch-action)
describe browser gesture takeover, cancellation and scoped native-touch behavior.
No guide provides tested Hengshi input, accessibility, collision or device fitness.

Before implementation, independently review and obtain integrated/founder acceptance;
produce the approved control screens, bind the actual supported engine/profile and
authored clearance/ground/crossings, and inspect comfort/zoom/keyboard/pointer behavior
on required real phones/computers. After authorization, exercise actual doorway/
corner/headroom/ramp/river-edge/closed-room/reversal/stall/cancel/context-loss paths
and no-drag/keyboard/semantic equivalence. Numerical targets need measured review;
no prose test, model update, application controller or safety certification is performed.
'''
with WORLD.open('ab') as file:
    file.write(text.replace('\n', '\r\n').encode('utf-8'))
text = '''
## Human-scale traversal profile proposal — 2026-10-06

The [World traversal/camera profile](WORLD_EXPERIENCE.md#mouse-touch-traversal-and-camera-profile-proposal--2026-10-06)
now proposes concrete mouse/touch/no-drag controls, body/eye/camera and walking/
clearance targets, fixed-step stall handling and swept support/readiness checks.
Keep movement authority there rather than duplicating its numeric table in this
asset specification. Authored metre/Y-up transforms, doors/turns/ramps/headroom,
safe ground and all-around eye-level horizon must satisfy the eventually approved
profile and existing lease/collision/stream gates. Targets are unmeasured proposals,
not permission to change D-071's accepted study composition, shrink a body at a
doorway, select physics/WASM or certify construction/accessibility. Independent
review, approved controls/geometry/profiles, compatible graph, physical-device
comfort/clearance and integrated/founder acceptance remain; no model or runtime change.
Earlier reviewed specification bytes are preserved and do not cover this appendix.
'''
with BUILD.open('ab') as file:
    file.write(text.replace('\n', '\r\n').encode('utf-8'))
for path in (WORLD, BUILD):
    (OUT / (path.name + '.reviewed')).write_bytes(path.read_bytes())
print(json.dumps({'world_sha256': hashlib.sha256(WORLD.read_bytes()).hexdigest(),
                  'build_sha256': hashlib.sha256(BUILD.read_bytes()).hexdigest()}))
