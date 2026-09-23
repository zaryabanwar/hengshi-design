# 3D Mega Menu Style Guide v2.0

**Version:** 2.0 | **Date:** February 9, 2026 | **Status:** Active
**Supersedes:** 3D Mega Menu Style Guide v1.0 (Angular + Three.js direct)

---

## 1. Overview

This document provides style guidelines for the Hengshi Design Platform's 3D immersive navigation system. The system uses **React Three Fiber (R3F)** with **GSAP** animations and **Zustand** state management to create an interactive building experience where users navigate through 3D rooms corresponding to service categories.

### 1.1 Technology Changes from v1.0

| Aspect | v1.0 (Feb 2025) | v2.0 (Feb 2026) |
|--------|-----------------|-----------------|
| Framework | Angular + Three.js direct | React 18 + React Three Fiber |
| State | Angular Services | Zustand stores |
| Animation | Tween.js + Angular Animations | GSAP timelines |
| 3D Helpers | Manual Three.js setup | @react-three/drei |
| Styling | SCSS + Angular Material | TailwindCSS |
| Build | Angular CLI | Vite |

---

## 2. Design Principles

### 2.1 Core Principles
- **Immersive Experience:** Depth and dimension that extends the platform's 3D environment
- **Performance First:** Visual richness must never compromise performance. This governs fidelity only — texture resolution, shadows, model detail, effects. It is never a reason to remove a hotspot, a destination, or a control from any stream; `S-LOW` carries the same destination set as `S-HIGH`.
- **Intuitive Navigation:** 3D elements enhance, not confuse, the navigation experience
- **Brand Consistency:** All elements reflect the Hengshi design language
- **Peer Delivery Streams:** Four streams of equal standing, selected by client
  capability; none is a degradation of another (§8.2)

### 2.2 Animation Philosophy
- **Purpose-Driven:** Every animation communicates meaning and guides users
- **Smooth Transitions:** Natural easing functions via GSAP
- **Restrained Effects:** Subtle over overwhelming
- **Performance Balanced:** Simplified animation in lower-capability streams;
  meaning is never carried by animation alone

---

## 3. Visual Language

### 3.1 Color Palette

| Element | Color | Hex Code | Usage |
|---------|-------|----------|-------|
| Card Base | Dark Gray | `#2D3142` | Primary card surface |
| Card Highlight | Red/Orange | `#E72A00` | Card edges, highlights |
| Card Accents | Orange | `#F44A25` | Interactive elements |
| Text Primary | White | `#F4F5F7` | Card titles, primary text |
| Text Secondary | Light Gray | `rgba(255,255,255,0.7)` | Descriptions, secondary text |
| Hotspot Default | Cyan | `#00BFFF` | Inactive hotspot glow |
| Hotspot Hover | White | `#FFFFFF` | Active hotspot glow |

### 3.2 Typography

| Element | Font | Size | Weight |
|---------|------|------|--------|
| Card Titles | Playfair Display | 1.25rem (20px) | 500 |
| Card Descriptions | Inter | 0.875rem (14px) | 400 |
| Section Headers | Playfair Display | 2rem (32px) | 500 |
| Featured Content | Inter | 1rem (16px) | 400 |
| Panel Headings | Inter | 1.5rem (24px) | 600 |
| Panel Body | Inter | 1rem (16px) | 400 |

### 3.3 Spacing (TailwindCSS)
- Card Padding: `p-6` (1.5rem)
- Grid Gap: `gap-6` (1.5rem)
- Section Margins: `my-10` (2.5rem)
- Content Padding: `p-4` (1rem)

---

## 4. 3D Elements

### 4.1 Hotspot Design

Hotspots are rendered as interactive spheres using `@react-three/drei` components within the R3F canvas.

**Configuration (database-driven):**
- Position: `{x, y, z}` from WorldHotspot.position
- Radius: `WorldHotspot.radius` (default 0.5 units)
- Normal: Surface alignment vector

**States:**

| State | Scale | Color | Emission | Non-colour, non-motion cue (required) |
|-------|-------|-------|----------|----------------------------------------|
| Default | 1.0 | `#00BFFF` | 0.3 | Visible label; solid ring |
| Keyboard focus | 1.0 | `#FFFFFF` | 0.6 | **Persistent 3 px focus ring at ≥3:1 against every adjacent scene colour, plus the label in its expanded form.** Present whether or not the pointer is used, and unaffected by `prefers-reduced-motion` |
| Hover | 1.2 | `#FFFFFF` | 0.6 | Label expands to its full form; ring thickens |
| Active/Click | 0.9 → 1.1 | `#F44A25` | 0.8 | Label shows the pressed form; ring becomes filled |
| Disabled | 0.8 | `#666666` | 0.1 | Label carries the reason text; ring becomes dashed |

No hotspot state may be distinguishable by colour, emission, scale, or animation
alone. Every row above carries a static cue that survives both a colour-vision
deficiency and `prefers-reduced-motion`, matching the universal rule already
binding on every component primitive ("visible text plus shape icon border pattern
or position; never color only"). The focus row is normative, not planned: a stream
that cannot show it cannot ship.

### 4.2 GLB Model Standards

- **Format:** GLTF Binary (.glb)
- **Source:** Blender export with draco compression (planned)
- **Coordinate system:** Blender defaults (Z-up converted to Y-up by Three.js)
- **Scale factor:** 100x (Blender meters to Three.js units)
- **Materials:** PBR (Physically Based Rendering) via MeshStandardMaterial

### 4.3 Lighting

| Light | Type | Color | Intensity | Position |
|-------|------|-------|-----------|----------|
| Ambient | AmbientLight | `#ffffff` | 0.5 | — |
| Main | DirectionalLight | `#ffffff` | 1.0 | (5, 5, 5) |
| Accent Blue | PointLight | `#0066ff` | 1.0 | Scene-dependent |
| Accent Red | PointLight | `#ff0066` | 1.0 | Scene-dependent |

### 4.4 Camera Settings

| Parameter | Value | Notes |
|-----------|-------|-------|
| FOV | 50° (configurable per node) | WorldNode.camera_fov |
| Near Plane | 0.1 | |
| Far Plane | 1000 | |
| Position | Per-node from database | WorldNode.camera_position |
| Target | Per-node from database | WorldNode.camera_target |

---

## 5. Animations (GSAP)

### 5.1 Timing Guidelines

| Animation | Duration | Easing | GSAP Function |
|-----------|----------|--------|---------------|
| Drone entry (per keyframe) | 2–4s | power3.inOut | `gsap.timeline()` |
| Room transition | 1.5s | power2.inOut | `gsap.to()` |
| Hotspot hover | 300ms | power2.out | `gsap.to()` |
| Hotspot click | 100ms | power1.inOut | `gsap.to()` with yoyo |
| Panel open/close | 400ms | power2.out | CSS transition |
| Loading fade | 500ms | linear | CSS opacity |

### 5.2 Drone Entry Sequence

The entry animation uses a GSAP timeline with 5 keyframes:

```
Keyframe 1: Bird-eye view (high altitude, looking down)
    ↓ 3s power3.inOut
Keyframe 2: Orbit approach (circling building)
    ↓ 3s power3.inOut
Keyframe 3: Front approach (straight-on view)
    ↓ 2s power2.inOut
Keyframe 4: Door-level approach
    ↓ 2s power2.out
Keyframe 5: At door (stopped, CTA visible)
```

### 5.3 Room Transition Pattern

When `NAVIGATE_NODE` hotspot is clicked:
1. Current hotspots fade out (200ms)
2. Camera animates to new node's `camera_position`/`camera_target` (1.5s, power2.inOut)
3. New hotspots fade in (200ms staggered)

---

## 6. Panel Overlay System

Panels are HTML/CSS overlays rendered outside the R3F canvas, triggered by `OPEN_PANEL` hotspots.

### 6.1 Panel Types

| Panel | Trigger | Content |
|-------|---------|---------|
| Services | `{"panel": "services"}` | Service listings filtered by category |
| Projects | `{"panel": "projects"}` | Portfolio items with media |
| Contact | `{"panel": "contact"}` | Lead capture form |

### 6.2 Panel Styling (TailwindCSS)

```
Container: fixed right-0 top-0 h-full w-[480px] bg-gray-900/95 backdrop-blur
Header:    p-6 border-b border-gray-700
Content:   p-6 overflow-y-auto
Close:     absolute top-4 right-4 text-gray-400 hover:text-white
```

---

## 7. Interaction Guidelines

### 7.1 Cursor States

| State | Cursor | Context |
|-------|--------|---------|
| Default (3D canvas) | `default` | Exploring scene |
| Hotspot hover | `pointer` | Over interactive hotspot |
| Panel interaction | `default` | Over HTML panel overlay |
| Dragging (future) | `grab` / `grabbing` | Camera orbit control |

### 7.2 Keyboard Navigation (required; not yet implemented)

- **Tab:** Cycle through hotspots
- **Enter/Space:** Activate hotspot
- **Escape:** Close panel / go back
- **Arrow keys:** Camera orbit (future)

### 7.3 Accessibility

- `prefers-reduced-motion`: the stream is **not** changed (§8.2.2 step 6). What is
  suppressed is exhaustive and normative — anything not listed continues to run:
  - drone entry sequence and all camera flights become instant cuts
  - room and panel transitions become instant cuts
  - hotspot hover and click animation (§5.1) is replaced by its static cue (§4.1);
    the state change itself is never lost, only its animation
  - ambient and idle scene animation, particle systems, and lighting loops stop
  - loading fades become instant; loading state is still announced
  - `S-SEMANTIC` has no camera or scene motion, so this setting affects only its
    panel and loading transitions there
- ARIA labels on hotspot overlays
- Focus indicators for keyboard navigation
- Screen reader descriptions for 3D scene state
- Minimum contrast WCAG AA for all text

---

## 8. Responsive Behavior

### 8.1 Breakpoints

| Breakpoint | Panel Width | 3D Adjustments |
|------------|-------------|----------------|
| Desktop (>1024px) | 480px side panel | Layout only |
| Tablet (768–1024px) | 400px side panel | Layout only |
| Mobile (<768px) | Full-width bottom sheet | Layout only |

**Viewport does not select the stream.** Breakpoints govern panel geometry, hit
target sizing, and label density only. Presentation richness is selected by §8.2
from the WebGL probe and `hardwareConcurrency` — a capable phone receives a higher
stream than a weak laptop, and no hotspot or destination is removed at any
breakpoint.

### 8.2 Delivery Streams

**Amended 2026-09-06 under CR-002, decision D-039. Amended again 2026-09-06 under
decision D-045**, which accepted the two delivery-stream specifications as the sole
authority for this axis and added the control model (§8.2.4), the separation of
stream selection from World entry (§8.2.5), and the process-state guarantee
(§8.2.6). This section previously
described a degradation ladder ending in a "fallback". It does not any more.
These are four **peer** streams. They differ in presentation richness and never
in what a visitor can accomplish; the semantic stream is a first-class product
surface, not a downgrade. Any wording that reintroduces "fallback", "degraded",
or "optional" for `S-SEMANTIC` is a regression against D-039.

| Stream | Presentation | Core journey |
|--------|--------------|--------------|
| `S-HIGH` | Full lighting, shadows, high-resolution textures | Equivalent |
| `S-MEDIUM` | Reduced shadows, medium textures | Equivalent |
| `S-LOW` | No shadows, low-resolution textures, reduced model detail; **every hotspot and every destination retained** | Equivalent |
| `S-SEMANTIC` | No WebGL; semantic Quick Access navigation with static imagery | Equivalent |

Every route reachable in `S-HIGH` is reachable in `S-SEMANTIC` by an equivalent
named action. `/credits` appears in all four streams, because the CC BY 4.0
attribution obligation does not vary by presentation tier (**R-032**).

#### 8.2.1 Verified selection signals

Verified 2026-09-06 against MDN Baseline. Full evidence and the verbatim banners
are in `docs/requirements/CR-002-signal-portability-verification.md`.

| Signal | Baseline status | Usable |
|--------|-----------------|--------|
| `navigator.hardwareConcurrency` | Widely available since March 2022 | **Yes** |
| `prefers-reduced-motion` | Widely available since January 2020 | **Yes** |
| WebGL context probe | Runtime feature detection; no Baseline dependency | **Yes** |
| Measured runtime performance | Observed at runtime, not declared by the client | **Yes** |
| `navigator.connection.effectiveType` | Limited availability | **No** |
| `prefers-reduced-data` | Limited availability; Experimental; not supported by any user agent | **No** |
| `navigator.deviceMemory` | Limited availability; coarsened to power-of-two buckets | **No** |

**No portable API reports network quality.** Connection tiering therefore binds
to measured runtime performance, not to a declared network class. For Firefox and
Safari clients an absent device signal is the **normal case**, not an edge case,
so the unsignalled default is a deliberate product choice rather than an error
path.

#### 8.2.2 Selection precedence

**Founder decision 2026-09-06 (D-040), corrected 2026-09-06 (D-042) after
independent design and accessibility review.** The original ordering evaluated the
user override at position 3, before the stream it was supposed to modify had been
selected, and allowed a mid-session promotion that changed the accessibility tree
without governance. Both are corrected below.

**Nothing in this list changes the stream after the session has started.** The
stream is resolved once, before first paint, and holds for the whole session. The
only exception is the visitor's own deliberate act at step 5.

Evaluated strictly in order:

1. **WebGL capability probe — hard ceiling.** If a WebGL context cannot be
   obtained, the stream is `S-SEMANTIC` and **no later step may raise it**.
   Capability is a fact about the client, not a preference, so nothing overrides
   it. This is the only step that can lower the ceiling.
2. **Device tier from `navigator.hardwareConcurrency`.** Where reported, it
   selects between `S-HIGH`, `S-MEDIUM`, and `S-LOW`, subject to the step 1
   ceiling. Boundary values are **U-03** and are not set here (§8.2.3).
3. **Unsignalled default — `S-LOW`.** Where no usable device signal is reported,
   the selection is `S-LOW`. This is the expected path for Firefox and Safari
   clients, not an error path, and it guarantees that no visitor is ever served
   more than their client has demonstrated it can handle.
4. **Stored measurement from a previous visit.** Runtime performance is measured,
   but **the measurement is never applied to the session that produced it.** It is
   stored and consulted here, on the next visit, where it may raise the selection
   above what steps 2 and 3 chose — never above the step 1 ceiling. It may only
   raise; it never lowers. A visitor with a stored override (step 5) skips this
   step entirely.

   **Storage.** The measurement and the step-5 preference share one mechanism:
   client-side storage scoped to the origin, holding the selected stream and the
   last measurement, retained until the visitor clears it. It carries no personal
   data and no identifier, so it needs no consent gate; the storage notice on
   `/credits` and the privacy route names it. If the store is unavailable or
   unreadable, step 4 is skipped silently — it is an optimisation, not an
   obligation — and selection proceeds from steps 1 to 3. A write failure at
   step 5 is different, because the visitor asked for something: it is explained
   without blocking, following the `ACT-11` pattern, and the choice still applies
   for the current session.
5. **User override — evaluated last, bounded by step 1.** A visitor may select
   **any stream at or below the step 1 ceiling, in either direction**, at any time.
   The choice is reversible: a visitor who tries `S-LOW` may return to
   `S-MEDIUM` if the ceiling allows it. The choice **persists across sessions**
   (CR-002 T-04) and takes precedence over step 4, so a visitor who dropped to
   `S-LOW` because the higher stream stuttered is never raised back up by
   measurement. If the preference cannot be written, it applies for the current
   session and the persistence failure is explained without blocking, following
   the ACT-11 pattern already established for reduced motion. Because this is the
   only step that acts after first paint, it is the only place a stream change
   must be announced (see §8.2.4).
6. **`prefers-reduced-motion` — motion, not stream.** Orthogonal to steps 1-5 and
   never changes the selected stream: the setting asks for reduced motion, not
   reduced content, and a visitor who enables it still receives the visual
   building. What it suppresses is enumerated in §7.3.

Consequences that reference production must prove rather than assume: `S-LOW` is
the highest-traffic first-paint stream and is designed first, not last; the step 5
control **must be reachable in every stream, including `S-SEMANTIC`**, and
therefore exists in the semantic shell primitive and not only in the World HUD;
and no reference frame may depict an automatic mid-session stream change, because
none occurs.

#### 8.2.3 Thresholds

The numeric boundaries between `S-HIGH`, `S-MEDIUM`, and `S-LOW` are uncertainty
**U-03** and remain `[MUST VERIFY AT SPECIFICATION]`. They require measurement
against the real building model on real devices and **cannot be closed in
Phase 1**. No threshold value may be written here until that measurement exists,
and no schedule is offered.

#### 8.2.4 Stream change announcement

A stream change can only result from step 5 — a deliberate visitor action. When it
occurs:

- The change is announced through the page status region as a polite status
  message. It does not interrupt.
- **Focus is not moved.** The visitor's focus stays on the control they operated.
- Scroll position, any open panel, and the current route are preserved across the
  change.
- The group accessible name reports the in-force stream, independently of any
  pending radio selection, so the active stream is available without inspecting
  the scene.

**Control model — normative (D-045, `N-05`, `OBL-CTRL-01/02`).** Use four native radio inputs sharing one name inside a fieldset with a legend,
one radio per stream, plus a separate, always-present Apply submit button.
Arrow, Tab, pointer and touch selection change only the checked state; they must
not apply a stream, reload, initiate a transition or alter the accessibility tree
beyond that checked state. A stream applies only after explicit Apply activation
with Enter, Space, pointer or touch, or native Enter submission of the same form
to that button. The control never applies on focus, selection, blur, arrow movement or timeout.
A native select that applies on change, or a listbox, combobox, menu or radio group
that applies on selection, is prohibited.

The group accessible name identifies the delivery stream control and reports the in-force stream
through its legend. The checked radio reports the pending selection. These values
are programmatically distinct: changing the pending selection leaves the reported
in-force stream unchanged until explicit submission applies it. On group entry a
screen reader receives the control name and in-force stream; on arrowing to another
radio it receives that radio's peer stream name and checked state, not an assertion
that the stream has changed. On reaching Apply it receives a distinct button name
stating that the button applies the selection.

Radio names use the peer stream vocabulary; they must not label a choice as
fallback, degraded, low quality, basic, optional, reduced, unsupported or non-WebGL.
Options above the step 1 ceiling remain present and disabled with a stated textual
reason, not hidden or distinguished by colour or dimming alone.

**Advance advisement — visible, not only accessible (D-045, `N-06`, `OBL-ADV-01`).**
Provide persistent visible text inside the fieldset, before Apply in both DOM reading order and visual order,
programmatically associated with both the group and the Apply button. It is
not tooltip, title, hover-only, focus-only or accessible-description-only content.
Use the same wording in every stream: explain that applying the pending selection
re-enters the experience in that stream while preserving the current location.
Exact public copy remains gated. Sighted mouse and keyboard users without assistive
technology receive the visible text before operation; a screen reader receives
the associated text at the group and button; at 400% magnification the visible text
remains before Apply without being hidden or clipped. The advance advisement is
distinct from the polite status announcement after the stream changes.
Neither is a claim of conformance — nothing is built, and WCAG 2.2
**3.2.2 On Input**, **3.3.7 Redundant Entry**, and **4.1.3 Status Messages** are
evaluated against the implementation, not against this document.

**Crossing the semantic boundary.** A visitor may move between `S-SEMANTIC` and a
3D stream, and the two shells are different subtrees, so the control the visitor
operated does not survive the change. Focus is therefore **not** preserved on that
element, and it is not dropped to the document body either. Focus moves to the
delivery stream control in the destination shell, which is the same control by role
and name and reports the new stream. That destination is named, so it is testable.

Location maps in both directions through the canonical route: every World location
has one canonical semantic route, and every semantic route that is reachable in the
World has one location. The change resolves the current location to its canonical
route, applies the new stream, and enters at the mapped location. A location with no
mapping enters at the nearest ancestor that has one, and says so.

During the change the outgoing shell is removed from the accessibility tree before
the incoming shell is added, so no visitor ever perceives two shells at once. The
canvas is not present in `S-SEMANTIC` at all; entering a 3D stream adds it after the
incoming shell is announced, never before.

#### 8.2.5 Stream selection and World entry are separate questions

**Founder decision 2026-09-06 (D-045, gate G-1).** §8.2.2 selects **which stream is
in force**. It does not decide **whether the World canvas is entered**. These were
being conflated, and the conflation had a concrete consequence: it implied that a
capable client landing on `ROUTE-HOME` would be dropped into a 3D building it never
asked for, which contradicts `ACT-06` — entering the World is an explicit act.

Both statements hold at once, and neither weakens the other:

- Capability and measured conditions choose the stream (`S-HIGH`, `S-MEDIUM`,
  `S-LOW`, `S-SEMANTIC`) for the whole session, per §8.2.2.
- **The World canvas is entered only on an explicit visitor action.** No automatic
  entry, on any route, in any stream, at any capability.

Therefore **`ROUTE-HOME`'s first frame is a non-World shell in every stream**,
including `S-HIGH`, and that shell carries the delivery stream control. A visitor in
`S-HIGH` who never enters the World still has a stream, still sees the control, and
still receives the complete journey. The stream in force determines how the World
looks *if and when* the visitor enters it, and determines nothing about whether they
do.

This is why the stream control lives in the semantic host shell primitive rather
than in the World HUD (§8.2.2, consequence 2): a control that existed only inside the
canvas would be unreachable on the very first frame every visitor sees.

#### 8.2.6 Process state survives a stream change

**Founder decision 2026-09-06 (D-045, gate G-7).** A stream change **never discards
booking process state.** A held slot stays held, a verified email stays verified, and
entered field values stay entered — across every boundary, **including the semantic
one**, where the shells are different subtrees and the DOM does not survive.

The semantic boundary is where this would otherwise break, and it is stated
explicitly for that reason. That the outgoing shell is destroyed is an
implementation fact about the shells; it is not a licence to destroy the visitor's
work. Process state is held independently of the shell that displays it and is
rehydrated into the incoming shell before that shell is announced. A visitor who
reaches booking verification, decides the 3D stream is stuttering, drops to
`S-SEMANTIC`, and continues, does not re-enter anything and does not lose the slot
they were holding. WCAG 2.2 **3.3.7 Redundant Entry** is the criterion this
anticipates, and as everywhere else in this document it is a design obligation on the
future implementation, not a conformance claim.

If process state genuinely cannot be carried — which is a failure, not a design
option — the change is **refused and explained**, the visitor stays where they are
with their work intact, and the refusal follows the `ACT-11` pattern. Silently
resetting a booking is never the answer.

---

## 9. R3F Component Patterns

### 9.1 Scene Structure

```jsx
<Canvas camera={{ fov: 50, near: 0.1, far: 1000 }}>
  <CameraController />        {/* GSAP animation target */}
  <ambientLight intensity={0.5} />
  <directionalLight position={[5,5,5]} intensity={1} />
  
  {entryPhase !== 'inside' && <ExteriorScene />}
  {entryPhase === 'inside' && <InteriorScene nodeKey={currentNode} />}
  
  <HotspotRenderer hotspots={activeHotspots} />
</Canvas>
```

### 9.2 State Flow

```
User Click Hotspot
    → worldStore.handleHotspotAction(hotspot)
    → switch(hotspot.kind):
        OPEN_PANEL  → setActivePanel(hotspot.payload.panel)
        NAVIGATE_NODE → setCurrentNode(hotspot.payload.target_node)
                        → CameraController animates to new position
        OPEN_URL    → window.open(hotspot.payload.url)
```

---

## 10. Testing Checklist

- [ ] Performance: 60fps on target devices
- [ ] Animation smoothness across entry sequence
- [ ] Hotspot click accuracy (raycasting precision)
- [ ] Panel open/close transitions
- [ ] `S-SEMANTIC` stream renders and carries every core journey
- [ ] Keyboard navigation, including a visible focus indicator on every hotspot
- [ ] `prefers-reduced-motion` behavior
- [ ] Cross-browser: Chrome, Firefox, Safari, Edge
- [ ] Mobile touch: iOS Safari, Android Chrome
- [ ] Memory usage during extended navigation
- [ ] GLB model loading time (< 3s on 4G)
