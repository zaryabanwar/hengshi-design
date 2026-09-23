# Design-System Implications for UI Reference Production

**Evidence date:** 2026-09-03
**Amended:** 2026-09-06 under D-042 and D-043 (CR-002 revision window). The 2026-09-03 producer freeze date above is retained as provenance and is not restated as current; the delivery stream axis, the ACT-09 stream control, and the peer-framing renames were added after it.  
**Status:** Definition contract; producer revision 3 of 3; accessibility correction only
**Authority:** D-025, D-026, D-035, and D-036
**Implementation status:** Blocked

## 1. Purpose, authority, and boundary

This document defines the reusable token and primitive obligations that a later,
separately approved Figma or Stitch reference package must satisfy. It is a
component contract, not a component library, visual screen, public-content set,
or implementation specification.

The controlling sources are the [decision index](../../DECISIONS.md), [project
brief](../../PROJECT.md), [project state](../../PROJECT_STATE.yaml), [phase
tasks](../../TASKS.md), accepted
[foundation](../phase-1-foundation/README.md), accepted [brand
strategy](../phase-1-brand-strategy/03-BRAND_STRATEGY.md), accepted [brand
identity](../phase-1-brand-identity/BRAND_IDENTITY.md), frozen [identity semantic
tokens](../phase-1-brand-identity/semantic-tokens.json), and accepted [UX
architecture](../phase-1-ux-architecture/UX_ARCHITECTURE.md). The complete route,
exclusion, wayfinding, flow, state, and test authorities are the [route parity
matrix](../phase-1-ux-architecture/route-room-parity.csv), [excluded-surface
matrix](../phase-1-ux-architecture/excluded-surfaces.csv), [wayfinding release
map](../phase-1-ux-architecture/wayfinding-release-map.csv), [flow
definitions](../phase-1-ux-architecture/FLOWS.md), [action and recovery
contracts](../phase-1-ux-architecture/STATES_AND_RECOVERY.md), and [UX acceptance
tests](../phase-1-ux-architecture/CONTENT_ANALYTICS_TESTS.md).

D-035 and D-036 take precedence over stale status labels inside the frozen
identity and UX packages. The exact Signal Ledger system plus Framework Relay
logo hybrid is an accepted Phase 1 identity definition, and the UX package is
accepted definition evidence. Neither decision authorizes production UI, public
use, implementation, or an external design write.

The following boundaries are absolute for this contract:

- No primitive in this document or the accompanying [primitive coverage
  matrix](component-primitives.csv) is production-approved.
- No inherited identity token, logo geometry, asset, evidence-state grammar,
  typography rule, spacing value, motion range, or sound rule may be altered here.
- No exact legal, privacy, consent, refusal, error, contact, provider, response,
  or service-delivery copy is selected here.
- No Figma, Stitch, shared-library, Code Connect, application, WebGL, asset,
  publication, or deployment write is authorized or performed.
- Code Connect may be considered only under a later explicit contract when it is
  supported and requested. It is not a substitute for a reviewed mapping ledger.
- The next founder gate is **MA-024 — Phase 1 UI reference-design contract and
  foundation-surface coverage acceptance**. It accepts or revises only this
  definition package and does not authorize external Figma, Stitch, or
  design-system production or writes.

### 1.1 Inherited delivery context and inventory boundary

- **Approved direction:** Signal Ledger supplies the evidence-led visual system;
  Framework Relay supplies the entity mark; D-036 supplies the responsive,
  accessible route and flow architecture. This contract adds no visual direction.
- **Platform targets:** responsive public and staff browser surfaces, complete
  semantic HTML for every indexable route before JavaScript, and an optional
  WebGL layer whose Quick Access route remains an equivalent non-WebGL journey.
- **Implementation family:** later implementation remains within the approved
  React, TypeScript, Vite, TailwindCSS, and React Three Fiber family on a
  separately approved stable compatibility matrix. This document selects no
  package version, framework primitive, or production API.
- **Bounded inventory:** the contract consists of the 62 stable records
  `PRIM-001` through `PRIM-062`. A reference template or flow that cannot be
  composed from those records must stop and propose a new, reviewed primitive;
  it must not hide the gap in a one-off screen component or invented product fact.

### 1.2 Normative accessibility and browser-support profiles

WCAG 2.2 Level AA is the normative target for all applicable full pages and
complete processes, including third-party steps. Neither this definition contract
nor a later Figma or Stitch reference design alone establishes WCAG conformance.
Conformance requires implementation evidence for the complete process and
independent accessibility review. Any proposed standards exception must name the
criterion, standards-supported rationale, affected route or flow, accessible
fallback, and independent-review acceptance. A standards exception or target
change remains a human gate.

The normative NFR-006 browser profile covers the current latest two stable
evergreen releases, with Safari/iOS 16.4 as the minimum legacy floor. Clients
below that floor or otherwise unsupported receive semantic Quick Access rather
than a broken or misleading experience. Exact current browser-version selection
is dated later QA evidence and is not invented here. Every affected public,
interactive, World, and staff reference must map to this profile; later evidence
must annotate Safari mobile layout, input, and safe-area behavior plus the
unsupported-client classification and semantic Quick Access recovery.

## 2. Token inheritance and design-to-code mapping

### 2.1 Layer model

| Layer | Status in this contract | Rule |
|---|---|---|
| Identity source tokens | Inherited and frozen | Preserve exact paths, values, ranges, and behavioral meaning from `semantic-tokens.json`; D-035 accepts the definition but does not make it production authority. |
| Semantic UI aliases | Required but unresolved | Later reference production must name aliases for surfaces, text, actions, focus, fields, status, overlays, loading, and data without changing the identity source layer. |
| Component tokens | Required but unresolved | Component recipes may reference semantic aliases only. They must not embed raw color, type, spacing, radius, stroke, or motion values. |
| Code tokens | Reserved mapping only | The names below reserve a one-to-one handoff. No code token exists or is implemented by this document. |
| Runtime policy | Accepted behavioral branches; exact values deferred | Sound default, the SC 2.2.1 timing branches, permissions, provider behavior, and retention are behavioral policies, not styling values. Exact session, challenge, and provider durations remain gated. |

### 2.2 Frozen identity token mapping

The mapping below preserves the approved identity vocabulary without selecting a
UI theme or changing a value. A later token export must keep both source and code
names in its mapping ledger.

| Design token path | Reserved code token or mapping stem | Exact inherited value or rule |
|---|---|---|
| `color.ink` | `--hd-color-ink` | `#0B0F14` |
| `color.graphite` | `--hd-color-graphite` | `#161D26` |
| `color.slate` | `--hd-color-slate` | `#2A3542` |
| `color.stone` | `--hd-color-stone` | `#D8D3C8` |
| `color.mist` | `--hd-color-mist` | `#F3F1EA` |
| `color.paper` | `--hd-color-paper` | `#FAF9F6` |
| `color.white` | `--hd-color-white` | `#FFFFFF` |
| `color.signal.cyan.onDark` | `--hd-color-signal-cyan-on-dark` | `#00D4FF` |
| `color.signal.cyan.onLight` | `--hd-color-signal-cyan-on-light` | `#006D82` |
| `color.signal.amber.onDark` | `--hd-color-signal-amber-on-dark` | `#FFB000` |
| `color.signal.amber.onLight` | `--hd-color-signal-amber-on-light` | `#8A5600` |
| `color.signal.lime.onDark` | `--hd-color-signal-lime-on-dark` | `#B6F36B` |
| `color.signal.lime.onLight` | `--hd-color-signal-lime-on-light` | `#4F7D18` |
| `color.signal.violet.onDark` | `--hd-color-signal-violet-on-dark` | `#A98CFF` |
| `color.signal.violet.onLight` | `--hd-color-signal-violet-on-light` | `#6D52B5` |
| `typography.display.{stack,weight,lineHeight,tracking}` | `--hd-font-display-family`; `--hd-font-display-weight`; `--hd-line-height-display`; `--hd-letter-spacing-display` | System sans stack; weight 650 with 700 fallback; 0.95–1.05; `-0.025em` |
| `typography.text.{stack,weight,lineHeight,minimumMeaningfulSize,defaultBodySize}` | `--hd-font-text-family`; `--hd-font-text-weight`; `--hd-line-height-text`; `--hd-font-size-minimum`; `--hd-font-size-body` | System sans stack; 400–500; 1.5–1.7; 12 px; 16 px |
| `typography.evidence.{stack,weight,lineHeight}` | `--hd-font-evidence-family`; `--hd-font-evidence-weight`; `--hd-line-height-evidence` | System monospace stack; 500–600; 1.4–1.6 |
| `space.scale[0..8]` | `--hd-space-1` through `--hd-space-9` | Ordered one-to-one values: 4; 8; 12; 16; 24; 32; 48; 64; 96 px |
| `layout.{wideColumns,mediumColumns,narrowColumns}` | `--hd-grid-columns-wide`; `--hd-grid-columns-medium`; `--hd-grid-columns-narrow` | 12; 6; 4 columns; collapse follows content need |
| `radius.evidenceFrame` | `--hd-radius-evidence-frame` | Accepted range 0–4 px; the later component recipe selects within the range |
| `radius.control` | `--hd-radius-control` | 8 px |
| `radius.status` | `--hd-radius-status` | Pill only for short visible-text labels |
| `stroke.{iconGrid,iconBase,signal,minimumDeviceStroke}` | `--hd-icon-grid`; `--hd-icon-stroke`; `--hd-signal-stroke`; `--hd-min-device-stroke` | 24 units; 2 units; 2–5 px by output size; 2 device pixels at small mark sizes |
| `motion.signalReveal` | `--hd-duration-signal-reveal` plus runtime reduced-motion branch | 180–320 ms; stable complete path when reduced |
| `motion.stateTransition` | `--hd-duration-state-transition` plus runtime reduced-motion branch | 120–200 ms; instant state with text when reduced |
| `motion.contextShift` | `--hd-duration-context-shift` plus runtime reduced-motion branch | 240–400 ms; direct cut with heading focus when reduced |
| `motion.immersiveArrival` | `--hd-duration-immersive-arrival-target` plus runtime skip branch | Approximately 8 s maximum target; immediate stable Reception or Quick Access when reduced |
| `sound.{default,activation,equivalence,meaningfulSpeech}` | `policy.sound.{default,activation,equivalence,meaningfulSpeech}` | Off; informed choice; non-audio equivalent; captions and transcript required |
| `evidenceState.verified.*` | `--hd-evidence-verified-*` | Lime surface pair; filled circle; solid line; visible label required |
| `evidenceState.demo.*` | `--hd-evidence-demo-*` | Violet surface pair; open diamond; dash-dot line; visible label required |
| `evidenceState.proposed.*` | `--hd-evidence-proposed-*` | Cyan surface pair; filled square; short-dash line; visible label required |
| `evidenceState.conditional.*` | `--hd-evidence-conditional-*` | Amber surface pair; filled triangle; long-dash line; visible label required |
| `evidenceState.unavailable.*` | `--hd-evidence-unavailable-*` | Neutral surface pair; filled bar; dotted line; visible label required |
| `evidenceState.error.*` | `--hd-evidence-error-*` | Amber/neutral treatment; open octagon; double-solid line; visible error and recovery required |
| `dataSeries.{contextBaseline,dependencyMap,decisionFrame,evidenceDepth,riskView}.*` | `--hd-data-series-{context-baseline,dependency-map,decision-frame,evidence-depth,risk-view}-*` | Preserve the five exact marker, line-pattern, and direct-label mappings; never reuse them as evidence status |

The existing declared contrast pairings are test inputs, not blanket approval for
all combinations. Every later semantic alias, component state, overlay, and
adjacent-color combination needs its own contrast evidence. Opacity, glow, blur,
or material appearance cannot repair insufficient contrast.

### 2.3 Semantic UI aliases still to be specified

The later visual-reference producer must resolve these token families and record
each design name, code name, inherited source alias, mode, and contrast result.
No value is selected by this document.

| Required design alias family | Reserved code pattern | Decision still required |
|---|---|---|
| `semantic.surface.{canvas,raised,recessed,inverse,overlay}` | `--hd-surface-*` | Exact dark/light surface pairing and overlay opacity |
| `semantic.text.{primary,secondary,inverse,muted,link}` | `--hd-text-*` | Role-specific contrast and unavailable-font behavior |
| `semantic.border.{subtle,strong,interactive}` | `--hd-border-*` | Adjacent-color contrast and forced-colors mapping |
| `semantic.focus.{ring,offset}` | `--hd-focus-*` | Thickness, offset, clipping prevention, and surface pairings |
| `semantic.action.{primary,secondary,quiet,destructive}.{foreground,background,border}.{base,hover,focus-visible,pressed,disabled}` | `--hd-action-*` | All interactive state pairings; amber must not be inferred as destructive |
| `semantic.field.{background,border,text,label,hint,error,success,disabled}` | `--hd-field-*` | Input and validation contrast, autofill, high-contrast, and read-only treatment |
| `semantic.status.{information,attention,verified,demo,proposed,held,error,pending}` | `--hd-status-*` | Alias to the frozen redundant evidence/status grammar without conflating states |
| `semantic.loading.{skeleton,progress,placeholder}` | `--hd-loading-*` | Reduced-motion behavior and preserved-content treatment |
| `semantic.elevation.{panel,dialog,drawer}` | `--hd-elevation-*` | Boundaries must survive without shadow, transparency, or depth |
| `semantic.data.{axis,grid,label,series,missing,target,interval}` | `--hd-data-*` | Exact series alias, direct labels, grayscale, table equivalent, and uncertainty treatment |
| `component.*` | `--hd-{component}-{variant}-{state}-{property}` | Created only after semantic aliases and component anatomy are approved |

### 2.4 Naming and lifecycle rules

- Design variables use `hd/{layer}/{role}/{variant}/{state}/{property}`. Code
  variables use the same segments in lowercase kebab case with the `--hd-`
  prefix. The mapping ledger records both names and the source identity path.
- Component sets use `HD/<Category>/<Component>`. Code component names use the
  same final component words in PascalCase. Variant and state values use
  lowercase kebab case.
- Stable primitive IDs are `PRIM-###`. An ID is never reassigned. A later
  replacement records `deprecated_by` instead of changing the meaning of an ID.
- Raw identity values may appear only in the identity source layer and generated
  token output. Components consume semantic or component aliases.
- Breaking token, component API, or cross-product governance changes require a
  human decision and migration record. Shared-library publication requires its
  own explicit approval.
- Dark and light are controlled surface pairings. Forced colors, grayscale,
  reduced motion, low power, non-WebGL, print, unavailable font, and unavailable
  asset are required verification contexts, not optional decorative themes.

## 3. Primitive and component contract

The machine-readable inventory is [component-primitives.csv](component-primitives.csv).
It covers public shell and route templates, AI/handoff/booking, World stream,
media, staff operations, publication, authentication, state/recovery, and data
presentation. The contract is deliberately technology-neutral; later Figma,
Stitch, and code components must preserve the same stable IDs even when one
primitive is composed from several implementation components.

### 3.1 Taxonomy

| Category | Responsibility |
|---|---|
| Shell and navigation | Landmarks, skip paths, primary navigation, breadcrumbs, directory/search, canonical location, and safe exclusions |
| Content and evidence | Collection/detail structure, services, industries, Work/Demos separation, evidence labels, sources, Trust, and entity identity |
| Actions and input | CTA/link/button behavior, fields, selection, consent, validation, error summary, and contact |
| AI and handoff | Transparent AI identity, transcript/composer, sources, refusal/cannot-verify, human availability, durable handoff, and media opt-in |
| Booking | Qualification, verification, availability, slot, review, pending, confirmation, reschedule/cancel, and reconciliation |
| Overlay and immersive | Dialog, drawer, panel, onboarding, HUD, exit, Quick Access, and asset/device recovery |
| Media and data | Player controls, captions/transcript/description inventory, charts, tables, and responsive lists |
| Staff and publication | Staff shell, availability, queues, work item, candidate/version/checksum, decisions, release state, and audit |
| System feedback and access | Authentication, session/permission, notification/live region, loading, empty, offline, error, and recovery |

### 3.2 Anatomy and composition

Every primitive record names its required anatomy. Composite components must keep
the following order unless a reviewed surface proves an equivalent accessible
order: context/title, state, primary content, evidence or limitation, available
actions, and recovery. Visual asymmetry cannot change DOM or reading order.

Child controls retain their own semantics and states inside a composite. For
example, a booking review is not one large clickable panel: it contains a heading,
editable summary, consent reference, authoritative status, primary submit,
secondary correction actions, and a live status destination. A queue row is not
the complete work item: it links to an independently versioned detail with its own
permission and stale-state handling.

### 3.3 Interaction states versus transactional states

Every interactive or composite-interactive primitive must show and document these
five pseudo-states independently:

1. `base`
2. `hover`
3. `focus-visible`
4. `pressed`
5. `disabled`

Hover never carries exclusive meaning. Focus-visible is at least as discernible
as hover, survives adjacent surfaces and forced colors, is not clipped, and is
verified with keyboard order. Pressed is distinct from selected or current.
Disabled remains readable and cannot hide a required route or serve as the sole
explanation for unavailability.

Transactional/content states are separate axes. Each primitive uses the relevant
subset of `loading`, `empty`, `error`, `pending`, `success`, `permission_denied`,
`offline`, `unavailable`, `stale`, `expired`, `held`, `current`, `selected`, and
`confirmed`. Pending never looks or reads as success. Every state has visible text
and a redundant non-color cue such as shape, line, icon, boundary, position, or
pattern. Status semantics must not steal focus; dialogs, error summaries, and
deliberate navigation may move focus under their own contract.

## 4. Responsive, input, and mode obligations

- Use the inherited 12/6/4-column model, but choose exact breakpoints only from
  content stress evidence. Device prestige or a familiar framework breakpoint is
  not sufficient justification.
- At 320 CSS px and 400% zoom, retain content, labels, state, recovery, and primary
  action in logical order. Two-dimensional scrolling is limited to genuinely
  two-dimensional data with an equivalent responsive list when needed.
- Narrow navigation becomes a labeled disclosure with predictable focus entry and
  return. Book remains reachable without opening media, AI, World, or a drawer.
- Long formal service names, evidence labels, source titles, time-zone labels,
  errors, and translated-length simulations wrap without truncating the accessible
  name or obscuring adjacent controls.
- Pointer actions activate on release or provide cancellation/undo. Every drag has
  a single-pointer non-drag and keyboard equivalent. Targets are at least 24 by 24
  CSS px or carry the exact documented valid exception and measurement.
- Reduced motion produces the complete stable state before nonessential travel,
  tracing, parallax, particle, loop, or camera movement. Essential content never
  waits for animation.
- Low-power, non-WebGL, unsupported-browser, offline, missing-image, missing-font,
  and 3D-asset failures preserve canonical content, location where safe, and the
  smallest valid recovery action.
- Forced colors and grayscale preserve focus, boundary, current/selected state,
  evidence status, error/success distinction, and data-series identity without
  depending on color or shadow.

## 5. Accessibility and behavior contract

- Use native landmarks, headings, lists, links, buttons, fields, tables, and
  dialogs first. Any composite pattern must document roles, names, states,
  properties, keyboard model, focus entry, focus return, and escape behavior.
- The visible label is contained in the accessible name. Icon-only use is limited
  to universally understood actions and still requires an accessible name;
  ambiguous actions retain visible text.
- Form labels, required/optional text, descriptions, validation, and error-summary
  links are programmatically associated. Unaffected values remain intact after an
  error when policy permits.
- Loading, queued, pending, reconciliation, confirmation, refusal, and recovery
  messages use appropriate polite or assertive announcements without repeating or
  interrupting uncontrolled updates.
- Booking verification and staff authentication allow paste, password managers,
  and assistive mechanisms or an equivalent accessible method.
- For every user time limit, each affected route, flow, and primitive must select
  and evidence one SC 2.2.1 Timing Adjustable branch: the time limit is removable
  or adjustable before it starts; or the user is warned with at least 20 seconds
  and can use a simple extension at least ten times; or a criterion-supported
  exception is documented. Expiry preserves permitted data and the last
  authoritative state, then offers accessible reauthentication. Exact session,
  challenge, and provider durations remain gated. A provider or system response
  timeout is not silently treated as the user's time limit.
- Prerecorded synchronized media requires captions and the separately applicable
  audio-description obligation at the WCAG 2.2 Level AA target. Audio-only content has a
  transcript; offered live synchronized media has live captions. Missing required
  alternatives hold media only, not semantic content or Book.
- Contrast is checked per rendered state: normal text at least 4.5:1; large text
  only under its valid size/weight rule; focus and meaningful non-text boundaries
  at least 3:1. The identity pairings do not waive component-level testing.
- No accessible label, role, state, route title, evidence class, or recovery
  instruction may exist only inside canvas, imagery, audio, motion, tooltip, or
  hover.

## 6. Required content stress cases

| Case | Reference requirement |
|---|---|
| Long formal taxonomy | Render every five-wing and ten-service title, including the longest service titles, at narrow width and 400% zoom without abbreviation. |
| Evidence language | Fit the full visible `Hengshi-owned capability demonstration` label, source/date/limitation, and held/error recovery without relying on a badge alone. |
| Empty and held collections | Work, Demos, Insights, Experts, Trust, About, and Contact preserve truthful reason, remaining utility, and next route without placeholder proof. |
| Booking qualification | Exactly six required data fields plus one separate consent record; optional budget; multiple linked errors; preserved values; long organization/outcome and time-zone text. |
| Booking ambiguity | Pending, provider-unknown, stale slot, reconciliation mismatch, reschedule/cancel conflict, and prior-confirmed truth remain visually and semantically distinct. |
| AI | Multi-turn transcript, long source titles, zero sources, cannot-verify, policy refusal, interrupted/resumed/expired session, and unavailable human path. |
| Staff operations | Empty queue versus unavailable queue; long candidate title; version/checksum mismatch; negative role; stale tab; no eligible assignee; read-only audit chain. |
| Media and assets | Unavailable imagery, font substitution, captions wrapping, transcript length, description status, media permission denial, and held rights. |
| Data | Missing values, uncertainty interval, directly labelled five-series specimen, long units/sources/limitations, grayscale, forced colors, and equivalent table/list. |
| Entity | Full `Hengshi Design` text at first contact and ambiguous contexts; missing logo asset never removes entity identity. |
| Localization readiness | Expanded plain-English strings, bidirectional-neutral structure, no concatenated essential phrases, and no direction-only instruction. Launch remains English-only. |

These fixtures are structural test content, not publication copy or evidence.

## 7. Asset, evidence, claim, and policy boundaries

- Later references may point only to current entries in the accepted identity
  manifest. They must not recreate, modify, recolor, crop, or reinterpret the
  Framework Relay family, and must never use the superseded mark as a fallback.
- Full-name-first, minimum-size, clearspace, flat-background, monochrome,
  reverse, and small optical-variant rules remain inherited. The mark is
  unregistered and trademark clearance remains open.
- Work and Hengshi-owned Demos stay separate. `Verified` is used only when the
  evidence and publication predicate passes. Requirements, targets, controls,
  test evidence, limitations, pending review, and unavailable states remain
  visibly distinct.
- No client, outcome, person, office, contact, sector-history, partner, award,
  assurance, operating-provider, staff-availability, or service-response fact may
  be added to make a component look complete.
- Exact legal/privacy/consent/refusal language, named owners and backups,
  provider behavior, response expectations, retention mappings, media rights,
  and public route content remain gated. Use structural field labels and explicit
  held placeholders in design evidence.
- Defense remains absent rather than represented by a hidden, disabled, or
  teaser component.
- The protected prototype and exterior 3D evidence are not sources for production
  styling, geometry, screenshots, or content.

## 8. Handoff evidence required before implementation

Reference production is not complete until all of the following exist and pass
independent design and accessibility review:

1. An approved reference-file inventory identifying every covered surface,
   component set, variant, mode, and immutable revision. External creation still
   requires a separate approval after MA-024.
2. A token export and mapping ledger that proves every design variable maps to the
   reserved code token, every component consumes semantic aliases, and all frozen
   identity values remain exact.
3. Component anatomy and property records for every `PRIM-###` row, including the
   five required pseudo-states for all interactive primitives and every relevant
   transactional/content state.
4. Coverage evidence for all 34 canonical routes, nine exclusion classes,
   15 wayfinding entries, AF-01/AF-02, BF-01A through BF-01E, DF-01, PF-01,
   SOF-01A through SOF-01M, CF-01, FV-01, RV-01, ACT-01 through ACT-53, and
   UXTEST-001 through UXTEST-045.
5. Responsive captures and annotations for narrow, medium, and wide layouts;
   320 CSS px; 400% zoom; text spacing; long-content fixtures; landscape mobile;
   and genuinely two-dimensional data behavior.
6. Keyboard/focus diagrams and inspected behavior for disclosure navigation,
   search, dialog/drawer/panel, consent, AI, booking, media, staff decisions,
   error summaries, escape, and focus restoration.
7. Contrast calculations for every rendered state and adjacent surface, plus
   forced-colors, grayscale, unavailable-font/image, reduced-motion, low-power,
   offline, and non-WebGL evidence.
8. Screen-reader semantics for landmarks, headings, lists, source citations,
   state labels, tables, form relationships, status announcements, and
   permission-denied behavior.
9. Content/evidence review showing no invented public fact, exact gated copy,
   leaked draft/defense content, or false success/availability/assurance state.
10. A route-to-template and primitive-to-screen trace proving each route/flow can
    be composed without a new unreviewed primitive or product fact.
11. Later implementation evidence must compare the approved reference revision,
    token export, component props/states, responsive rendering, and accessible
    behavior one-to-one. Any mismatch is a failed parity check, not a design
    interpretation.
12. When separately authorized, the durable production design-system document
    must be maintained at `docs/ui/DESIGN_SYSTEM.md`. This contract does not
    create that artifact or authorize its implementation.
13. A dated browser matrix must select the then-current latest two stable evergreen
    releases, retain Safari/iOS 16.4 as the minimum legacy floor, and prove
    semantic Quick Access for below-floor or otherwise unsupported clients,
    including Safari mobile layout, input, and safe-area annotations.
14. Controlled-clock evidence for every user time limit must identify its selected
    SC 2.2.1 branch and cover warning, simple extension, expiry, focus/status,
    permitted-data and authoritative-state preservation, and accessible
    reauthentication. An exception record must contain the criterion-supported
    rationale, affected flow, fallback, and independent-review acceptance.

After those records pass review, founder approval is still required for the exact
visual direction. Breaking token changes, material brand/product tradeoffs,
licensed assets, exact public/legal copy, shared-library publication, external
design writes, implementation, publication, and deployment remain separate human
gates.
