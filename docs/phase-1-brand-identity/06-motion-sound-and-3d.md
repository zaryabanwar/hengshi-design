# Motion, Sound, and 3D Implications

## Motion principles

Motion must answer at least one question: what changed, what connects, where did
focus move, or what is the next state? If it answers none, remove it.

### Motion families

| Family | Purpose | Standard timing | Reduced-motion equivalent |
|---|---|---:|---|
| Signal reveal | Show one connection or progression | 180–320 ms | Signal appears complete with no travel |
| State transition | Confirm a panel/status change | 120–200 ms | Instant state swap plus persistent text/status |
| Context shift | Preserve orientation between related surfaces | 240–400 ms | Direct cut with heading focus and breadcrumb update |
| Evidence sequence | Reveal ordered evidence steps after user action | 180 ms per step; no auto-cycle | Complete numbered list visible at once |
| Immersive arrival | Later optional authored entry | Approximately eight seconds maximum target; skippable | Stable reception/Quick Access state immediately |

Use ease-out for arrival and ease-in-out for short relationship transitions.
Spring, bounce, elastic, parallax, cursor-chasing, and perpetual ambient motion are
not part of essential identity behavior.

### Reduced-motion requirements

- Respect `prefers-reduced-motion` before any nonessential movement begins.
- Remove camera travel, parallax, looping particles, signal tracing, and spatial
  zoom from the reduced-motion expression.
- Preserve every label, status, relationship, action, and booking route.
- Move focus only through predictable document behavior; never animate focus
  across the viewport.
- Do not use opacity-only fades that temporarily hide essential content.
- Provide explicit pause/stop controls for any later motion that lasts more than
  five seconds or repeats.

## Sound principles

Sound is optional atmosphere or feedback, never navigation, evidence, identity,
urgency, or status on its own.

- Audio is off by default until an informed user choice.
- One persistent, keyboard-operable mute/control state follows the visitor.
- No startup sound, autoplay voice, simulated call, spatial whisper, alarm, or
  notification sound precedes consent.
- Meaningful speech requires synchronized captions and a transcript.
- Every audio cue has a simultaneous non-audio visual/text equivalent.
- Haptics, where available later, are optional and never the only feedback.
- The identity includes no audio file, voice, composition, sample, or license.
  Commissioning or licensing sound requires a separate rights and paid-asset gate.

## 3D material language

The identity defines implications, not a scene or production material library.

### Materials

- **Ink basalt:** low-sheen dark structural plane; avoid crushed-black detail.
- **Warm limestone:** light warm neutral for readable orientation fields; do not
  mimic a specific quarried location or imply extraction provenance.
- **Brushed graphite:** controlled edge and equipment detail; no mirror chrome.
- **Signal glass:** narrow emissive cyan/amber inlays only for state and path;
  never large luminous walls or bloom-heavy spectacle.
- **Paper ceramic:** matte high-contrast panels for semantic content and evidence.

No protected prototype texture, mesh, layout, material, or exterior geometry is
reused. A later Blender master requires project ownership, versioning,
provenance, scale/origin, LOD, export, and separate approval.

### Lighting

- Use broad neutral key light, warm material response, and localized signal
  accents.
- Maintain readable contrast without bloom, fog, glare, or HDR dependence.
- Do not place text on moving light, reflections, transparent glass, or shadowed
  geometry.
- Provide a low-power lighting tier and a non-WebGL semantic equivalent.
- Flashing and rapid luminance changes are prohibited.

### Wayfinding

- Formal service titles remain visible in semantic/accessibility text.
- A concise sign may accompany a formal title only after a one-to-one mapping is
  approved; this identity selects no campus shorthand.
- Direction uses text, icon, consistent location, and path geometry, not color or
  “enter the blue room.”
- Current location, destination, exit, Quick Access, booking, quality, audio, and
  accessibility controls remain persistent and keyboard operable.
- Closed/unavailable spaces are labeled with an equivalent useful route; they do
  not become mysterious locked doors or marketing teasers.

## WebGL and semantic parity

The optional WebGL expression may change pacing, spatial grouping, material, and
sensory emphasis. It may not change or remove the entity name, category, promise,
formal taxonomy, evidence state, limitations, source, trust context, booking
route, contact route, or recovery path. Every room/panel maps to a canonical
semantic page. Quick Access remains complete with WebGL, audio, motion, and asset
loading disabled.
