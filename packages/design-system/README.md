Hengshi Design is an evidence-led, premium, platform-oriented innovation delivery company. Its identity strategy is **Evidence in Motion**: a visible system for showing how a consequential ambition becomes a decision frame, connected capabilities, evidence, and a next accountable step. The expression is the retained **Signal Ledger** system (layout, colour, type, evidence grammar, motion) carrying the **Framework Relay** logo. Everything here is exploratory and unregistered: the mark is not trademark-cleared, and no asset is approved for public production until the founder and legal gates in the source package close. The identity must remain understandable when all animation, imagery, sound, WebGL and colour are removed.

## Principles

Apply these before any token.

1. **Evidence has form.** Evidence states use stable labels, line patterns, geometry and text, never glow or colour alone. A verified fact, a Hengshi-owned demonstration, a proposed method, a requirement, a limitation and an unavailable state never share an ambiguous badge.
2. **Motion reveals a relationship.** Motion shows connection, sequence, state change or orientation. It never decorates an idle page or delays meaning.
3. **Mineral calm, luminous precision.** Ink, graphite, slate, stone, mist and paper carry the surfaces. Cyan and amber are brief signals for action and attention; lime and violet are reserved data and evidence accents. No large luminous fields, rainbow gradients or ambient glow.
4. **Semantics lead.** The full name, category, formal service title, evidence label and next action appear as text. A mark, icon, image or spatial location is never the only explanation.
5. **Precision stays human.** Strong grids, exact labels and narrow signal lines are balanced by generous space, warm stone neutrals, sentence case and candid limitations. No cold institutional density, no luxury ornament.
6. **Craft earns attention.** Distinctiveness comes from proportion, negative space, evidence choreography and coherent application, never from implied awards, customers, offices, certifications or outcomes.
7. **Recovery is branded quality.** Reduced-motion, monochrome, print, low-power, non-WebGL, asset-failure, keyboard and screen-reader experiences are authored outcomes that keep identity, content, evidence state and conversion.

## Voice and content

- Write in sentence case everywhere: headings, labels, buttons and navigation ("Book a conversation"). The only uppercase text is the `hd-eyebrow` style.
- Use the full name "Hengshi Design" on first contact, in page and entity headings, metadata, accessible names, structured data and anywhere the mark alone would be ambiguous. Keep formal service names intact and unabbreviated; a concise sign may accompany a formal title only after its one-to-one mapping is approved.
- Real copy from the source: the category line "Evidence-led innovation delivery partner"; the promise "From complex ambition to accountable delivery."; the eyebrow "EVIDENCE IN MOTION".
- State limitations candidly beside claims. Never imply awards, customers, global offices, certifications, sector leadership or measured outcomes the evidence does not hold.
- Label evidence. "Verified" appears only when the evidence and publication gates are satisfied, and always with source and date. Demonstrations say "Hengshi-owned capability demonstration". Proposed targets say "Target". Missing values stay missing and labelled.
- Errors say what went wrong and the recovery action in plain language. Unavailable and held states name the next useful route; closed spaces are never mysterious doors or teasers.
- Agriculture and mining are treated without pastoral, extractive, rescue or machinery spectacle; defence metaphors and unsupported superiority are absent.
- Quick Access, the non-WebGL journey, is a complete expression of the brand, not a lower-quality mode.

## Colour

Mineral neutrals carry the surfaces; four luminous signals mark actions and states. Signal colour stays under roughly 10% of a composition and is always paired with text, shape, line pattern, icon or position.

- Build pages on `hd-surface-canvas` with `hd-text-primary`. Raise cards and panels on `hd-surface-raised`; use `hd-surface-recessed` for large structural fields; `hd-text-secondary` for supporting text and `hd-text-muted` only at 16px or larger on the canvas.
- Compose a dark section inside a light page (masthead, hero, recommended card) on `hd-surface-inverse` with `hd-text-inverse`, and put its signals in the `hd-signal-*-on-inverse` tokens so both themes keep the right surface pair. A notice sits on `hd-surface-inverse-raised`.
- Every signal has an on-dark and an on-light value. On ink and graphite use `hd-color-signal-*-on-dark`; on paper, mist and white use `hd-color-signal-*-on-light`. The semantic tokens (`hd-text-signal`, `hd-text-link`, `hd-status-*`, `hd-action-*`, `hd-border-interactive`, `hd-focus-ring`) already choose per theme; components consume them, never the raw `hd-color-*` values.
- Cyan means action, active connection and current path. Amber means attention and conditional state, never destructive. Lime and violet are reserved for the verified and demonstration evidence states and for data series.
- Text on a signal fill is `hd-text-on-signal` (ink) on the on-dark signals and `hd-action-primary-foreground` (paper) on the on-light cyan. White on a signal fill is prohibited.
- No gradients, glow, blur, transparency or ambient luminous fields, and no shadow: boundaries survive without depth, so this system defines no shadow tokens.
- Two source pairs carry limits: `hd-color-muted-slate` on paper (4.52:1) is for normal text at tested sizes only, and `hd-color-signal-lime-on-light` reads on paper (4.66:1) but not on mist (about 4.3:1). Every other declared pairing is 5.27:1 or better; each token's usage note names its grounds and ratios.

The identity layer (`hd-color-*`) is frozen from the source. The semantic aliases (`hd-surface-*`, `hd-text-*`, `hd-border-*`, `hd-focus-*`, `hd-action-*`, `hd-status-*`, `hd-data-series-*`) resolve the alias families the source lists as still to be specified; they follow the identity board's own renderings, and each carries the contrast it measures. Hover and pressed pairings remain undecided in the source, so no token claims them.

## Typography

Three roles, all from platform system fonts. No font file is included, licensed or redistributed; the system does not claim cross-platform metric identity.

| Role | Family | Styles | Rule |
|---|---|---|---|
| Display | `display` | `hd-display-1` 72px, `hd-display-2` 56px, `hd-display-3` 40px, `hd-promise` 48px | Weight 650 where the platform face has it, 700 fallback; tracking -0.025em; leading 0.95 to 1.05 |
| Text | `text` | `hd-heading` 24px, `hd-lede` 20px, `hd-body` 16px, `hd-body-strong` 16px, `hd-action` 16px | 400 to 500 for reading, 800 for actions; leading 1.5 to 1.7 |
| Evidence and meta | `evidence` | `hd-eyebrow` 0.8rem, `hd-evidence` 13px, `hd-meta` 14px, `hd-series-key` 16px | Monospace 500 to 700; 12 to 14px; supplemental only |

- Set running text in `hd-body` at 45 to 75 characters per line (`hd-measure-max` is 72ch). 16px is the body default; nothing meaningful sits below 12 CSS px.
- Headings, buttons, labels and navigation use sentence case. Only `hd-eyebrow` is uppercase, letter-spaced 0.14em, in `hd-text-signal`.
- Avoid ultra-light weights, condensed essential text, justified paragraphs, decorative ligatures and all-caps paragraphs. Use tabular numerals only where comparison benefits, with clear headers and units.
- Evidence and meta text is supplemental: a limitation or essential instruction also appears in body text.
- The display sizes are fixed points inside the source's fluid ranges; the identity board's masthead runs from 48 to 120px with -0.06em tracking. Test line breaks, zoom, reflow and language expansion on the approved browser matrix.

## Spacing and layout

- The unit is 4px. Use only the nine steps `hd-space-1` (4px) to `hd-space-9` (96px): 4, 8, 12, 16, 24, 32, 48, 64, 96.
- Card and notice padding is `hd-space-4`; grid gaps `hd-space-5`; margins under section headings and above action rows `hd-space-6`; section padding runs from `hd-space-6` at narrow widths to `hd-space-9` on wide screens.
- Columns are 12 wide, 6 medium, 4 narrow (`hd-grid-columns-*`). Collapse follows content need, never device prestige; visual asymmetry never changes semantic reading order. Content measures at most `hd-content-max-width` (1180px) with gutters of at least `hd-space-4`.
- Every layout works at `hd-viewport-min` (320 CSS px), 400% zoom and increased text spacing without horizontal loss or overlap. Interactive targets are at least `hd-target-min` (24 by 24 CSS px).
- Keep the retained Signal Ledger asymmetry: evidence rails and offset blocks, not symmetrical grids; generous negative space around dense evidence.

## Radius, borders and elevation

- Evidence frames, cards, notices, figures and logo fields are square (`hd-radius-none`); the accepted evidence-frame range tops at `hd-radius-evidence-frame` (4px).
- Controls use `hd-radius-control` (8px). `hd-radius-status` (pill) is only for short labels with visible text.
- Hairlines are `hd-stroke-hairline` (1px): `hd-border-subtle` for decoration, `hd-border-strong` wherever a boundary carries meaning at 3:1 or better, `hd-border-interactive` for the active or selected boundary. Accent rules are `hd-stroke-rule` (6px) in `hd-signal-cyan-on-inverse` on hero and evidence blocks and `hd-stroke-notice-rule` (4px) in `hd-signal-amber-on-inverse` on notices.
- No shadow, blur, transparency or depth defines a boundary. Panels, dialogs and drawers are bounded by border and surface change, so they survive forced colours and grayscale. Do not repeat the logo brackets as a card or UI frame.

## Focus and interaction states

- Keyboard focus on a semantic shell is `hd-focus-ring`: a solid `hd-focus-ring-width` (3px) outline with `hd-focus-offset` (4px) on every focusable element, never clipped. These three values are [PROPOSED]: the frozen file records `semantic.focus.{ring,ring-width,offset}` as gated and cites them as the proposed source. Every focus pairing is measured within each delivery stream separately. In the World streams, WebGL hotspots and HUD controls use the scene ring instead: `hd-focus-scene-ring-width` is 3px exact (style guide section 4.1); its colour and offset are gated names (`--hd-focus-scene-ring`, `--hd-focus-scene-offset`) with no value yet; it holds at least 3:1 against every adjacent scene colour, renders above the HUD panel and every sticky element, and is static, persistent and unaffected by reduced motion. In `S-SEMANTIC` there is no canvas and the ordinary ring applies. Focus order follows document meaning. The skip link is the first focusable element and becomes visible on focus.
- Every interactive primitive defines base, hover, focus-visible, pressed and disabled. The source leaves the exact hover and pressed pairings undecided: until they are approved, hover adds an underline with a 0.2em offset and pressed keeps the native state. Disabled content stays readable (`hd-text-secondary` on `hd-surface-raised` with `hd-border-strong`) and is never the only route to a required action.
- Transactional states (loading, empty, offline, error, held, stale, unavailable, current, pending) are separate from pseudo-states and always show text plus shape, border, pattern or position. Never colour alone.

## Delivery streams

Four peer delivery streams carry equivalent core journeys: `S-HIGH`, `S-MEDIUM`, `S-LOW` and `S-SEMANTIC` (D-039; FR-3D-011; the frozen handoff file as amended under D-047). `S-SEMANTIC` is a first-class surface served from first paint to clients without a WebGL context and selectable by any visitor; the stream in force never decides whether the World canvas is entered. Never describe a stream as a fallback, reduced, lesser or optional mode, and never number or rank the four.

- **Verify per stream.** Contrast, focus order, target size and every other mode check are measured within one named stream against its own rendering and are never inherited by another; aggregate evidence that names no stream discharges nothing (NFR-A11Y-002).
- **Stream tokens.** `hd-stream-{high,medium,low,semantic}-{id,profile,evidence-token,canvas}` carry the identifier, the `DS-S-*` evidence profile, the `EC-08` `STREAM_*` token and the canvas fact (`on-explicit-entry` for the three World streams, `none` for `S-SEMANTIC`). The visible label per stream (`--hd-stream-*-label`) is gated public copy, and the presentation text (`--hd-stream-*-presentation`) lives in each id token's usage note. A stream token never carries a rendering value, a device-tier boundary, an ordering, a mode value, an availability or a timing.
- **The control.** The delivery stream control (`DeliveryStreamControl`, hosted by PRIM-001 in every stream and re-hosted by the World primitives) is a fieldset with a legend naming the control and the in-force stream, four native radios sharing one name, a persistent visible advisement before Apply, and a separate always-present Apply button. Selection changes only the checked state; the stream applies only on explicit Apply; the change is announced politely in a pre-existing empty status region without moving focus within a shell. Radios above the WebGL ceiling stay present and disabled with a textual reason stated as a fact about the client. The component guideline carries the full contract.
- **Frame states.** `STATE-STREAM-CHANGED`, `STATE-PREFERENCE-WRITE-FAILED`, `STATE-PREFERENCE-READ-FAILED` and `STATE-STREAM-CEILING-REFUSED` are homed on the state profiles the responsive-state-mode matrix names; pending never looks or reads as applied, and the control never reports a stream the visitor did not apply.
- **Gated by the founder.** Exact label, legend, advisement, reason and announcement copy (UG-3); the scene focus-ring colour, offset and adjacency sampling method (UG-1, UG-2); the U-03 tier boundaries; whether Apply is ever disabled (UG-5); hover and pressed pairings (UG-6); whether native radios may be styled at all under forced colours (UG-7).

## Evidence states and data

Six evidence states and five illustrative data series are the brand's most distinctive grammar; the Evidence states and data series section holds the full mapping and markup. In short: `hd-status-verified` filled circle and solid rail; `hd-status-demo` open diamond and dash-dot rail; `hd-status-proposed` filled square and short-dash rail; `hd-status-attention` filled triangle and long-dash rail; `hd-status-held` filled bar and dotted rail; `hd-status-error` open octagon and two parallel solid rails. Every state carries a visible label. Charts direct-label every series at its endpoint and never reuse an evidence-state marker.

## Motion

Motion answers a question (what changed, what connects, where did focus move, what is next) or it is removed. Signal reveal 180 to 320ms, state transition 120 to 200ms, context shift 240 to 400ms, evidence sequence 180ms per step after user action with no auto-cycle, immersive arrival at most about eight seconds and skippable. Ease-out for arrival, ease-in-out for short relationship transitions; no spring, bounce, elastic, parallax, cursor-chasing or perpetual ambient motion. Under `prefers-reduced-motion` every state appears complete and stable with its text. The Motion, sound and 3D section carries the full rules; by design no motion token exists in this system.

## Iconography

- The source ships construction rules and a meaning table, not an icon set: a 24 by 24 unit grid (`hd-icon-grid`), a 2-unit base stroke (`hd-icon-stroke`), square terminals with slight optical softening, and no filled pictograms except the status shapes. Minimum 20 CSS px; 24 CSS px for controls.
- Icons inherit the current text colour and stay visible in forced-colours mode. A primary icon combines one structural rail with one action or state cue.
- Meanings are fixed: explore or connect is two nodes joined by an open path; evidence or source is a stacked record with a source point; Quick Access is an open doorway with a direct horizontal path; immersive view is a framed perspective field; booking is a calendar outline with a confirmed point; human help is a person-neutral speech form with an availability state; AI help is a labelled circuit node with a visible "AI" label; reduced motion is a shortened path with pause bars; audio is a speaker form with its state and transcript route.
- Never sparkles for AI, shields for unverified trust, leaves for agriculture, pickaxes or mountains for mining, or tactical symbols anywhere. Icons never carry wing or sector meaning alone, and an icon-only control needs an accessible name plus visible text wherever ambiguity remains.
- Flag: no icon files exist in the source, so nothing ships under `assets/Icons`. Draw new icons to these rules and add them there; the status shapes live in the EvidenceStateLabel component.

## Logo

Use the Framework Relay assets under `assets/Logos` exactly as shipped: `logo-framework-relay-primary.svg` on ink, `logo-framework-relay-light.svg` on paper or white, `logo-framework-relay-mono.svg` (one ink on white) and `logo-framework-relay-reverse.svg` (one white ink on black) for single-ink contexts, `mark-framework-relay.svg` at 32 CSS px and above, `mark-framework-relay-small.svg` at 24 to 31, `favicon-framework-relay.svg` at 16 to 23. Full name first: the mark alone never defines the entity, a service, a state or evidence status. Clearspace is two framework returns (20 master units) on every side; the horizontal lockup is never narrower than 168 CSS px. Never stretch, rotate, outline, round, enclose, recolour by service or state, animate continuously, or place it over texture, imagery, data or 3D reflections. Every asset is marked EXPLORATORY, UNREGISTERED, TRADEMARK NOT CLEARED; the Logo system section carries construction, sizes and modes.

## Imagery

Imagery clarifies context, material, system, evidence or human decision; it never manufactures proof. Prefer documented human-scale work with consent and provenance, close material and interface detail with real scale cues, restrained architectural light and warm neutrals. Prohibited: strangers posed as staff or clients; handshake, globe, server-room, robot or AI-brain stock; pastoral agriculture or extraction heroism; military or war-room imagery; fake dashboards, invented metrics and client-logo composites; the protected prototype exterior model. Illustration is sparse system diagrams built from rails, nodes, brackets, numbered steps and open fields, each with a title, reading order, labels and a non-visual equivalent. Generated media must be labelled and can never serve as evidence. Every substantive image or video carries its owner, creator, date, provenance, rights, evidence class, caption and alt decision, or it stays held.

## Required modes

Reduced motion, forced colours, grayscale, print, 320px reflow, 400% zoom, unavailable font, unavailable image, low power, non-WebGL, offline, keyboard-only and screen-reader use are authored outcomes, not fallbacks. Each preserves identity, content, evidence state and the booking route. Every indexable route renders complete semantic HTML before script, and Quick Access provides the equivalent non-WebGL journey. Target WCAG 2.2 Level AA across full pages and complete processes, including third-party steps; latest two stable evergreen browser releases with a Safari and iOS 16.4 floor.

## Not synced

- Fonts: the source uses platform system stacks only, so `type.fonts` is empty and no font is fetched.
- Components: the source defines 62 UI primitives (PRIM-001 to PRIM-062) as anatomy and state contracts with no code. Eight CSS components are hand-written here, seven from the identity board's stylesheet and the delivery stream control from the amended frozen file; the Component inventory section tracks the rest as not built. The application under `apps/web` still runs the Vite starter stylesheet with an empty Tailwind theme, so nothing was taken from it.
- Assets: the superseded and exploration marks (Signal Ledger, Quiet Framework, Resonant Field, the three direction boards) and the identity-board screenshots were not carried; they are review evidence, not brand assets.
- Motion durations and the sound policy live in prose, not tokens; hover and pressed colour pairings are not defined because the source has not approved them.
- Stream labels and presentation text are not tokens: the labels are gated public copy, and the presentation strings carry punctuation this token format cannot hold, so they sit in the id token usage notes. The scene focus-ring colour and offset are gated and have no token; only the 3px width is carried. The component tokens `--hd-delivery-stream-control-*` exist as names in the frozen file and carry no value yet.
