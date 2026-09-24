# Motion, sound and 3D

## Motion

Motion must answer at least one question: what changed, what connects, where did focus move, or what is the next state. If it answers none, remove it. Use ease-out for arrival and ease-in-out for short relationship transitions. Spring, bounce, elastic, parallax, cursor-chasing and perpetual ambient motion are not part of the identity.

| Family | Purpose | Standard timing | Reduced-motion equivalent |
|---|---|---:|---|
| Signal reveal | Show one connection or progression | 180 to 320 ms | The signal appears complete with no travel |
| State transition | Confirm a panel or status change | 120 to 200 ms | Instant state swap plus persistent text or status |
| Context shift | Preserve orientation between related surfaces | 240 to 400 ms | Direct cut with heading focus and breadcrumb update |
| Evidence sequence | Reveal ordered evidence steps after user action | 180 ms per step, no auto-cycle | The complete numbered list, visible at once |
| Immersive arrival | Optional authored entry | About eight seconds maximum, skippable | Stable reception or Quick Access immediately |

Reduced motion:

- Respect `prefers-reduced-motion` before any nonessential movement begins; remove camera travel, parallax, looping particles, signal tracing and spatial zoom.
- Preserve every label, status, relationship, action and booking route. Move focus only through predictable document behaviour; never animate focus across the viewport.
- No opacity-only fades that temporarily hide essential content. Any later motion over five seconds or repeating gets explicit pause and stop controls.
- Flashing and rapid luminance changes are prohibited everywhere.

## Sound

Sound is optional atmosphere or feedback, never navigation, evidence, identity, urgency or status on its own. Audio is off by default until an informed user choice; one persistent, keyboard-operable mute control follows the visitor. No startup sound, autoplay voice, simulated call, spatial whisper, alarm or notification precedes consent. Meaningful speech has synchronized captions and a transcript; every cue has a simultaneous non-audio equivalent. Haptics are optional and never the only feedback. The identity includes no audio file, voice or composition; commissioning sound needs a separate rights gate.

## 3D material language

The identity defines implications, not a scene or material library, and reuses no protected prototype texture, mesh, layout or exterior geometry.

- **Ink basalt:** a low-sheen dark structural plane; no crushed-black detail.
- **Warm limestone:** a light warm neutral for readable orientation fields; never a specific quarry or an extraction story.
- **Brushed graphite:** controlled edge and equipment detail; no mirror chrome.
- **Signal glass:** narrow emissive cyan or amber inlays only for state and path; never luminous walls or bloom.
- **Paper ceramic:** matte high-contrast panels for semantic content and evidence.

Lighting is a broad neutral key with warm material response and localized signal accents; readable contrast without bloom, fog, glare or HDR dependence. No text on moving light, reflections, transparent glass or shadowed geometry. A low-power lighting tier and a non-WebGL semantic equivalent always exist.

## Wayfinding and parity

Formal service titles stay visible in semantic text; a concise sign accompanies a formal title only after its one-to-one mapping is approved. Direction uses text, icon, consistent location and path geometry, not colour. Current location, destination, exit, Quick Access, booking, quality, audio and accessibility controls remain persistent and keyboard operable. Closed or unavailable spaces are labelled with an equivalent useful route.

The optional WebGL expression may change pacing, spatial grouping, material and sensory emphasis. It may not change or remove the entity name, category, promise, formal taxonomy, evidence state, limitations, source, trust context, booking route, contact route or recovery path. Every room or panel maps to a canonical semantic page, and Quick Access remains complete with WebGL, audio, motion and asset loading disabled.
