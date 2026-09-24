# Design-System Amendment R-039 — Delivery-Stream Axis, Stream Tokens, Stream Control, and Focus-Ring Tokens — **[PROPOSED SPECIFICATION]**

**Status: [PROPOSED SPECIFICATION]. Pending founder decision. Not accepted
authority. Nothing in this document is implemented, no frozen file has been
changed by it, and no conformance of any kind is claimed here or anywhere in the
package it amends.**

**Author:** independent specification author. I am not the D-045 producer, I did
not produce the CR-002 package or any of its remediations, I did not author the
two D-044 specifications, and I wrote no validator, including
`validation/validate-ui-reference-design.ps1`. Written under founder decision
**D-046** (2026-09-24), which executes the deferral recorded at **D-045 gate
G-6**: the design-system gap is recorded first and amended later as its own
bounded specialist contract, so that the producer never authors the design-system
content it will later be judged against.

**Date:** 2026-09-24; Revision 2, 2026-09-24 (revision cycle 1 of three, addressing review 1 findings DSA-01 to DSA-09; see Revision history)
**Commissioned by:** D-046, executing D-045 gate G-6 (risk R-039).
**Inputs:** `DESIGN_SYSTEM_IMPLICATIONS.md` (whole file, §1 to §8);
`accessibility/DELIVERY_STREAM_ACCESSIBILITY_OBLIGATIONS.md` (header and
vocabulary discipline, Part 0 `OBL-INV-01` to `OBL-INV-03`, Part 1 `OBL-GRAM-01`
to `OBL-GRAM-03`, Part 2 `OBL-CTRL-01` to `OBL-CTRL-06` including the
translucent-panel passage at lines 470 to 473, Part 3 `OBL-ADV-01` and
`OBL-ANN-01`, Part 4 `OBL-BND-01` to `OBL-BND-04`, Part 5 `OBL-STATE-01` to
`OBL-STATE-05`, Part 6 `OBL-TRACE-01` to `OBL-TRACE-03`, and the Part 7 heading);
`DELIVERY_STREAM_EVIDENCE_MODEL.md` (header, §0 row 5 on `EC-08`, §7.1 `N-03`,
§7.2 `N-04`, §7.3 `N-05` and `N-06`, §8.1, §10 gates G-1 to G-7);
`component-primitives.csv` (header row, `PRIM-001`, `PRIM-042`, `PRIM-043`,
`PRIM-044`); `responsive-state-mode-matrix.csv` (`SP-NAVIGATION`, `DS-S-HIGH`,
`DS-S-MEDIUM`, `DS-S-LOW`, `DS-S-SEMANTIC` in revision 1; in revision 2 all 36
rows read with `Import-Csv` for the state distribution in §3.10);
`foundation-flow-coverage.csv`
(`COV-ACT-09`); `design-batch-plan.csv` (`B01`); `traceability.csv`
(`TR-REQ-103`, `TR-REQ-111`, `TR-TEST-046`);
`validation/validate-ui-reference-design.ps1` (read only: required-file list,
`design-system-freeze-hash`, the conformance-claim scan, the peer-framing guard,
`git-write-scope`, the frame-name pattern, `local-markdown-references`);
`docs/phase-1-ui-reference-production/evidence-capture-plan.csv` (`EC-08`);
`docs/active/3D_Mega_Menu_Style_Guide_v2.md` (§3.1, §4.1, §6.2, §7.2, §7.3, §8.2,
§8.2.1 to §8.2.6); `docs/active/Hengshi_Design_SRS_v3.md` (`FR-3D-010` to
`FR-3D-016` with their amendment notes; `NFR-A11Y-001` to `NFR-A11Y-007`);
`docs/phase-1-ux-architecture/CONTENT_ANALYTICS_TESTS.md` (`UXTEST-046`);
`docs/phase-1-ux-architecture/STATES_AND_RECOVERY.md` (`ACT-09`, `ACT-11`);
`docs/phase-1-ux-architecture/UX_ARCHITECTURE.md` (the explicit World-entry
statement near line 173); `docs/phase-1-brand-identity/semantic-tokens.json`
(searched only, for any `focus` or `stream` definition: one declared contrast
pairing names focus use; no stream token exists); `DECISIONS.md` (`D-039`,
`D-043`, `D-044` index rows; `D-045` resolutions 1 to 7; `D-046`); `RISKS.md`
`R-039`; `TASKS.md` R-039 row; `CHANGELOG.md` 2026-09-24 entries;
`reviews/design-system-amendment-r-039-review-1.md` (independent review 1 at
commit `740864b`, findings DSA-01 to DSA-09; read for revision 2, not edited);
`packages/design-system/tokens.json` (whole) and
`packages/design-system/README.md` (Principles, Colour, Radius/borders/elevation,
Focus and interaction states, Required modes, Not synced) as **[PROPOSED]** input,
never as authority (D-046).

**Scope of change:** one file, this one. `DESIGN_SYSTEM_IMPLICATIONS.md` is
hash-pinned (the validator asserts `design-system-freeze-hash`, expected
`0E9FC68C98AC25C4F7DFBC62B10DBA1FCB197F5C82AD2FF39DCD0C16D9CFB763`) and is not
edited. `component-primitives.csv` is likewise hash-pinned and not edited: the
control's anatomy is already recorded on `PRIM-001`, `PRIM-042`, `PRIM-043` and
`PRIM-044`, so this amendment adds no primitive. The freeze file is re-opened
only by a later slice under the separate founder acceptance decision that D-046
names; §5 below is written so that slice can apply the amendment without
judgement.

**Not authorized by this document:** any edit to a hash-pinned file, any
validator change, application implementation, external writes, Figma or Stitch
MCP calls, publication, deployment, or the release of batch **B01**, which stays
`future_not_authorized` in both plan files under D-045 gate G-4.

**Vocabulary discipline.** `S-HIGH`, `S-MEDIUM`, `S-LOW` and `S-SEMANTIC` are
four **peer** streams carrying equivalent core journeys (D-039; `FR-3D-011`;
`NFR-A11Y-003`). This document attaches no rank, ladder, quality ordering or
contingency vocabulary to any of them, and no token, label, state or annotation
it defines may do so. Where a sentence below could be read as ranking a stream,
the peer reading is the intended one and the sentence should be corrected.

**No conformance is claimed.** WCAG 2.2 Level AA is the normative target for
every applicable full page and complete process, including third-party steps,
holding independently within each stream (`NFR-A11Y-001`, `NFR-A11Y-002`). Every
sentence below is an obligation on a later specification, reference package or
implementation, evaluated against the built system and never against this
document. Success-criterion numbers are cited as the criterion at stake, not as a
result.

---

## 0. Summary of what this amendment adds

| # | Gap named at D-045 gate G-6 and R-039 | Addition | Home in the freeze file after application (§5) | OBL-GRAM-03 reviewer-test hit |
|---|---|---|---|---|
| 1 | No delivery-stream axis | The axis as a design-system dimension: a verification context, a token family and a component property, with the **per-stream contrast rule** (§1.3) | §1.1, §2.4, §4, §5, §8 | **(a) per-stream contrast rule** |
| 2 | No tokens for the four stream values | `semantic.stream.{high,medium,low,semantic}` reserved as `--hd-stream-{high,medium,low,semantic}` with six properties each (§2) | §2.2 note, §2.3 row | — |
| 3 | No delivery-stream control component | `HD/Shell and navigation/Delivery stream control`, code `DeliveryStreamControl`, mapped to `PRIM-001` anatomy (§3) | §3.1 rows, §3.3, new §3.4 | **(b) stream-control component** |
| 4 | No 3D focus-ring token | `semantic.focus.{ring,ring-width,offset}` resolved as names, plus `semantic.focus.scene.{ring,ring-width,offset,layer,contrast-floor,motion}` for WebGL hotspots and HUD controls (§4) | §2.3 rows, §4, §5, §8 | **(c) focus-ring tokens** |

Nothing in this table changes an inherited identity value, a primitive ID, a
route, a flow, a state profile, or the evidence-ID grammar. Every addition
consumes what D-045 already accepted.

---

## 1. The delivery-stream axis as a design-system dimension

### 1.1 Four peer streams

| Stream | Evidence profile | EC-08 evidence-ID token | Presentation (style guide §8.2 table, verbatim) | Core journey | Canvas |
|---|---|---|---|---|---|
| `S-HIGH` | `DS-S-HIGH` | `STREAM_HIGH` | Full lighting, shadows, high-resolution textures | Equivalent | Present only after explicit World entry |
| `S-MEDIUM` | `DS-S-MEDIUM` | `STREAM_MEDIUM` | Reduced shadows, medium textures | Equivalent | Present only after explicit World entry |
| `S-LOW` | `DS-S-LOW` | `STREAM_LOW` | No shadows, low-resolution textures, reduced model detail; every hotspot and every destination retained | Equivalent | Present only after explicit World entry |
| `S-SEMANTIC` | `DS-S-SEMANTIC` | `STREAM_SEMANTIC` | No WebGL; semantic Quick Access navigation with static imagery | Equivalent | None anywhere in the document |

Sources: style guide §8.2 (stream table), `responsive-state-mode-matrix.csv`
rows `DS-S-HIGH` to `DS-S-SEMANTIC`, `evidence-capture-plan.csv` `EC-08`
(`<STREAM>` is mandatory on every public evidence ID, positioned between
`<MODE>` and `V<NN>`, with no omissible and no aggregate form; a public frame
shows one stream), style guide §8.2.4 and §8.2.5 and `OBL-CTRL-05` for the
canvas column.

The four streams differ in presentation richness and never in what a visitor
can accomplish. Every route reachable in `S-HIGH` is reachable in `S-SEMANTIC`
by an equivalent named action (style guide §8.2). `S-SEMANTIC` is P0
(`FR-3D-010`), is served from first paint to any client that cannot obtain a
WebGL context (§8.2.2 step 1), and may be chosen deliberately by any visitor
whose client can (§8.2.2 step 5; `OBL-CTRL-05`). The `Presentation` column is
descriptive text carried as data by the stream token (§2.2); it is never a
label, never a rank, and never a rendering parameter.

### 1.2 What the axis is, and is not, inside the design system

- **A verification context**, in the sense of the freeze file §2.4 last bullet:
  every token pairing, component state, overlay, adjacent-colour combination and
  rendering obligation is verified within each stream separately, exactly as it
  is verified separately for forced colors, grayscale, reduced motion, low power,
  print, unavailable font and unavailable asset.
- **A semantic token family** (§2): four stream tokens in the semantic alias
  layer, consumed by components and by the evidence ledger.
- **A component property** of the delivery stream control (§3), and the
  required-variant axis `PRIM-001` already declares
  (`stream_high;stream_medium;stream_low;stream_semantic`; in design and code
  those variant values are the kebab-case `stream-high`, `stream-medium`,
  `stream-low`, `stream-semantic` per freeze §2.4).
- **Not a theme, not a mode, not a surface pairing.** Dark and light remain
  controlled surface pairings that exist in all four streams. `MODE-*` values
  intersect the stream axis; they never substitute for it. `MODE-SEMANTIC-SHELL`
  is a mode and `S-SEMANTIC` is a stream: different axes with a confusable name
  (`OBL-GRAM-01` point 4), and the design system never uses one to mean the
  other.
- **Selected once, before first paint**, holding for the whole session, and
  changed only by the visitor's explicit act through the control (§8.2.2;
  `FR-3D-013`). No token, component, mode or reference frame may depict or
  trigger an automatic mid-session stream change (§8.2.2, consequence 3).
- **Independent of World entry.** The stream in force does not decide whether
  the World canvas is entered (D-045 resolution 1, gate G-1; §8.2.5;
  `FR-3D-015`). `ROUTE-HOME`'s first frame in every stream, including `S-HIGH`,
  is a non-World shell carrying the delivery stream control.

### 1.3 The per-stream contrast rule — reviewer-test hit (a)

> **Per-stream contrast rule.** Contrast is checked per rendered state **and per
> stream**. Every contrast measurement (normal text at least 4.5:1; large text
> only under its valid size/weight rule; focus indicators and meaningful
> non-text boundaries at least 3:1), every focus-order check, every target-size
> measurement (at least 24 by 24 CSS px, or the exact documented valid exception
> and measurement), and every other verification context named in §2.4 is taken
> within one named delivery stream — `S-HIGH`, `S-MEDIUM`, `S-LOW` or
> `S-SEMANTIC` — against that stream's own rendering. A measurement taken in one
> stream is never inherited by another stream. Aggregate evidence, and any
> evidence whose EC-08 identifier carries no `STREAM_*` token or another
> stream's token, discharges no per-stream obligation (`NFR-A11Y-002`;
> `OBL-INV-03`; `DS-S-*` `annotation_requirements`).

The rule cannot be weaker, for a physical reason stated at `OBL-INV-03`: the
same translucent panel (style guide §6.2, `bg-gray-900/95 backdrop-blur`) over a
lit high-texture scene, over an unshadowed low-texture scene, and as a standalone
semantic document with no canvas behind it are three different renderings with
three different measured ratios. Contrast, focus-indicator contrast, target
geometry and focus order are properties of a rendering, and the four streams
render differently by construction. An aggregate frame does not under-evidence
the other three streams; it evidences none of them.

Consequences for the token system:

1. Every pairing recorded in the mapping ledger (freeze §2.2, §2.3, §8 item 2)
   records the stream in which it was measured. A pairing measured in
   `S-SEMANTIC`, where no canvas exists, does not stand for the same pairing in
   `S-LOW`, `S-MEDIUM` or `S-HIGH`.
2. The identity source's declared contrast pairings remain test inputs in every
   stream and approvals in none (freeze §2.2 closing paragraph, extended to the
   stream axis).
3. Opacity, glow, blur, backdrop filtering or material appearance cannot repair
   insufficient contrast in any stream, and cannot be measured away by choosing
   a different stream.
4. Frame economy is unaffected by this rule's strictness: `N-04` (evidence model
   §7.2) already bounds the per-stream obligation to the baseline frame plus the
   stream-critical states of each stream-dependent template, and this amendment
   adds no state and no template.

---

## 2. Stream tokens

### 2.1 Naming under freeze §2.4

Design variables use `hd/{layer}/{role}/{variant}/{state}/{property}`; code
variables use the same segments in lowercase kebab case with the `--hd-`
prefix; the mapping ledger records both names and the source path. Segments
that do not apply are omitted, as the freeze file already does for
`semantic.focus.{ring,offset}` to `--hd-focus-*`.

- **Layer: `semantic`.** Stream tokens are not identity source values: the
  identity source `semantic-tokens.json` defines no stream, so they cannot enter
  the frozen identity mapping of §2.2 without altering the frozen layer, which
  §1 forbids. They are not component tokens either, because more than one
  component consumes them (the four hosts `PRIM-001`, `PRIM-042`, `PRIM-043`,
  `PRIM-044`; the page status region announcement; the evidence ledger).
- **Role: `stream`.**
- **Variant:** `high`, `medium`, `low`, `semantic`.
- **State:** omitted. A stream token is a value; in-force and pending are states
  of the control (§3.10), never of the stream.
- **Property:** one of `id`, `profile`, `evidence-token`, `label`,
  `presentation`, `canvas` (§2.2).

| Stream | Design token path | Design alias family | Code token stem | Source path recorded in the ledger |
|---|---|---|---|---|
| `S-HIGH` | `hd/semantic/stream/high/{property}` | `semantic.stream.high.*` | `--hd-stream-high-{property}` | style guide §8.2 table row `S-HIGH`; `responsive-state-mode-matrix.csv` `DS-S-HIGH`; `evidence-capture-plan.csv` `EC-08` |
| `S-MEDIUM` | `hd/semantic/stream/medium/{property}` | `semantic.stream.medium.*` | `--hd-stream-medium-{property}` | style guide §8.2 table row `S-MEDIUM`; `DS-S-MEDIUM`; `EC-08` |
| `S-LOW` | `hd/semantic/stream/low/{property}` | `semantic.stream.low.*` | `--hd-stream-low-{property}` | style guide §8.2 table row `S-LOW`; `DS-S-LOW`; `EC-08` |
| `S-SEMANTIC` | `hd/semantic/stream/semantic/{property}` | `semantic.stream.semantic.*` | `--hd-stream-semantic-{property}` | style guide §8.2 table row `S-SEMANTIC`; `DS-S-SEMANTIC`; `EC-08` |

The four stream token names are therefore `--hd-stream-high`,
`--hd-stream-medium`, `--hd-stream-low` and `--hd-stream-semantic`, each
expanded by property (for example `--hd-stream-semantic-label`).

### 2.2 What a stream token carries

Derived from the sources: a stream token carries the identifier the SRS and
style guide use, the evidence profile the matrix assigns, the token the
evidence-ID grammar requires, the visible label the control and the announcement
use, the fidelity description the style guide table gives, and the canvas fact
that distinguishes the semantic shell from the World streams. It carries
nothing else (§2.3).

| Property | `S-HIGH` | `S-MEDIUM` | `S-LOW` | `S-SEMANTIC` | Source |
|---|---|---|---|---|---|
| `id` | `S-HIGH` | `S-MEDIUM` | `S-LOW` | `S-SEMANTIC` | `FR-3D-011`; style guide §8.2 |
| `profile` | `DS-S-HIGH` | `DS-S-MEDIUM` | `DS-S-LOW` | `DS-S-SEMANTIC` | `responsive-state-mode-matrix.csv` |
| `evidence-token` | `STREAM_HIGH` | `STREAM_MEDIUM` | `STREAM_LOW` | `STREAM_SEMANTIC` | `EC-08`; evidence model §0 row 5 |
| `label` | `[GATED]` | `[GATED]` | `[GATED]` | `[GATED]` | Exact public copy remains gated (`NFR-A11Y-004`; style guide §8.2.4; freeze §7) |
| `presentation` | Full lighting, shadows, high-resolution textures | Reduced shadows, medium textures | No shadows, low-resolution textures, reduced model detail; every hotspot and every destination retained | No WebGL; semantic Quick Access navigation with static imagery | style guide §8.2 table, verbatim |
| `canvas` | `on-explicit-entry` | `on-explicit-entry` | `on-explicit-entry` | `none` | style guide §8.2.4, §8.2.5; `OBL-CTRL-05`; `FR-3D-015` |

**Label constraints (apply to all four streams identically).** The `label`
value is one visible string per stream, used identically in the radio label,
in the legend's in-force segment, and in the status announcement (3.2.4
Consistent Identification is the criterion at stake). It is written in the
D-039 peer vocabulary; it must read as a choice a visitor might prefer
(`OBL-CTRL-02`); it may contain none of the label words `NFR-A11Y-004`
prohibits; it is the same in every stream and on every route; it is contained in
the radio's accessible name (freeze §5); and it is never a stream identifier,
a technology name, or a description of the client. The gate holding its exact
copy is listed in §7 (`UG-3`).

### 2.3 What a stream token never carries

- No raw colour, size, duration, opacity, texture or lighting value. The
  `presentation` property is descriptive text, not a rendering parameter; the
  rendering parameters behind it (shadow, texture, model detail) are
  implementation values that this design system does not select.
- No device-tier boundary. The numeric boundaries between `S-HIGH`, `S-MEDIUM`
  and `S-LOW` are uncertainty **U-03** and `[GATED]` (style guide §8.2.3;
  `FR-3D-012`). Because `[GATED]` values cannot live in a token, a stream token
  carries no boundary at all.
- No ordering, rank, weight or quality vocabulary (`OBL-GRAM-01` point 2). The
  tokens are four unordered peers; a later export must not number them, sort
  them by richness, or derive one from another.
- No mode value. Required modes per stream (`MODE-REDUCED-MOTION` and
  `MODE-KEYBOARD` for `DS-S-HIGH`; `MODE-KEYBOARD` for `DS-S-MEDIUM`;
  `MODE-LOW-POWER` and `MODE-KEYBOARD` for `DS-S-LOW`; `MODE-FORCED-COLORS`,
  `MODE-PRINT` and `MODE-KEYBOARD` for `DS-S-SEMANTIC`) are evidence
  obligations recorded on the `DS-S-*` rows, not token properties.
- No availability. Whether a stream is above the WebGL ceiling is a fact about
  the client established at runtime (§8.2.2 step 1) and carried by the control's
  radio state (§3.8), never by the token.
- No timing. Exact session, challenge and provider durations remain `[GATED]`
  (freeze §2.1 runtime policy row); transition durations are the accepted
  ranges of freeze §2.2 (`motion.stateTransition` 120–200 ms;
  `motion.contextShift` 240–400 ms; `motion.signalReveal` 180–320 ms) with
  their reduced-motion branches. A stream token carries none of them.

### 2.4 Ledger rows

The exact mapping-ledger rows the applying slice adds are given in §5,
insertion `INS-04`. Each row records the design path, the code token, and the
source path from the table in §2.1, plus a `stream measured in` column value
for any pairing that a component token later resolves through a stream token
(§1.3 consequence 1).

---

## 3. The delivery stream control component — reviewer-test hit (b)

This is the **stream-control component** required by `OBL-GRAM-03`, D-045 gate
G-6 and R-039. It is specified against the anatomy `PRIM-001` already records.

### 3.1 Name, hosts, and what it is not

- **Design component set:** `HD/Shell and navigation/Delivery stream control`.
  **Code component:** `DeliveryStreamControl`. The category segment is the
  freeze §3.1 taxonomy category of its authorized home, `PRIM-001`
  (`shell_navigation`), and the final words are the same in PascalCase, per
  freeze §2.4. Variant and state values are lowercase kebab case.
- **Not a new primitive.** No `PRIM-###` is added or reassigned.
  `component-primitives.csv` already carries the anatomy on `PRIM-001` (all four
  streams), `PRIM-042`, `PRIM-043` and `PRIM-044` (`stream_presence`
  `S-HIGH;S-LOW;S-MEDIUM`). The component is one reviewed component instantiated
  by those four hosts, which is exactly the freeze §3 case of "one primitive
  composed from several implementation components" in reverse: one component
  serving several primitives.
- **Where it lives in each stream.** In `S-SEMANTIC` the control lives in
  `PRIM-001`'s utility navigation and nowhere else, because the World HUD does
  not exist there, and it is reachable without a canvas (`OBL-CTRL-03`,
  `OBL-CTRL-05`, `FR-3D-014`). In `S-HIGH`, `S-MEDIUM` and `S-LOW` it lives in
  `PRIM-001`'s utility navigation on every non-World shell, including
  `ROUTE-HOME`'s first frame with the canvas not entered (`FR-3D-015`; §8.2.5),
  and is re-hosted by `PRIM-042` (World onboarding and return choice),
  `PRIM-043` (World HUD) and `PRIM-044` (World escape and recovery) once the
  World has been entered.
- **Present everywhere, identically.** On every route in every stream, within
  the navigation landmark structure and on the skip-link path, reachable without
  traversing main content, in the same relative position and under the same
  accessible name on every route (`OBL-CTRL-03`; 3.2.3 and 3.2.4 are the
  criteria at stake). It is not canvas-only in any stream (`PRIM-043`).

### 3.2 Anatomy, in `PRIM-001` record order, and the order constraints

The anatomy is `PRIM-001`'s, quoted from `required_anatomy` in the order that
record lists it:

1. `stream fieldset`
2. `stream legend naming delivery stream control and in-force stream`
3. `four native stream radio inputs sharing one name`, one radio per stream
4. `separate always-present Apply submit button`
5. `persistent visible stream advisement inside fieldset before Apply in DOM
   reading and visual order`

plus the host's `page status region` (also `PRIM-001` anatomy), which sits
outside the fieldset, carries the change announcement, and exists in the
accessibility tree, empty, before any message is written into it
(`OBL-ANN-01`).

Source-fixed order constraints are exactly two: the advisement is inside the
fieldset, and it precedes Apply in both DOM reading order and visual order
(`OBL-ADV-01` point 1; `NFR-A11Y-004`; `PRIM-001`). The freeze §3.2 composite
order is kept by reading the advisement as context (it explains what applying
does before anything is operated): context/title (the legend, then the
advisement), state (in-force in the legend; pending on the checked radio),
primary content (the radios), evidence or limitation (any unavailability text,
any failure explanation), available actions (Apply), recovery (the explanations
of §3.10). That reading, and hence the advisement's position relative to the
radios, is not fixed by any source and is recorded as assumption **A-2** in §7;
the frozen text inserted by `INS-08` carries only the two source-fixed
constraints and cites A-2 for the rest. Visual asymmetry cannot change DOM or
reading order. The visible order of the four radios is likewise fixed by no
source: the only ordering in the sources is the style guide §8.2 table order
(`S-HIGH`, `S-MEDIUM`, `S-LOW`, `S-SEMANTIC`), inherited from that accepted table
and not derived from richness, and because §2.3 forbids sorting the tokens by
richness and the order is the most public peer-framing surface the control has,
radio order is decided together with the four labels under gate `UG-3` (§7);
assumption **A-1** names the provisional order until then. Whatever order is
decided is identical on every route and in every stream.

### 3.3 Role and activation model (normative)

Authority: D-045 resolution 3; `OBL-CTRL-01`; `FR-3D-014`; style guide §8.2.4;
evidence model `N-05`.

- **Role.** A grouped set of four native radio inputs (`input[type="radio"]`,
  one per stream, sharing one name) inside a `fieldset` whose `legend` supplies
  the group's accessible name, plus a separate, always-present submit button that
  applies the selection. Role, checked state, group membership, arrow-key
  semantics and forced-colors rendering come from the platform, not from
  authored ARIA (D-045 resolution 3 rationale).
- **Two-step explicit confirmation.** Moving among the radios by arrow key, by
  `Tab` into the group, by pointer or by touch changes only which radio is
  checked. It must not apply a stream, must not reload, must not initiate any
  transition, and must not alter the accessibility tree beyond the checked
  state.
- **Application.** A stream applies only on explicit activation of Apply by
  `Enter`, `Space`, pointer or touch, or by `Enter` pressed within the group
  where that is the platform's native form-submission behaviour for the same
  button. The control never applies on focus, on selection, on blur, on arrow
  movement, or after a timeout.
- **Prohibited.** A native `select` whose `change` event applies the stream;
  any listbox, combobox, menu or radio group that applies on selection, on
  blur, on arrow-key movement or after a timeout; any control that applies on
  first interaction of any kind.
- **Until Apply is activated**, the control's reported current stream is the
  stream in force, not the stream tentatively checked; both are programmatically
  available (§3.4).

### 3.4 Accessible names; current and pending values

Authority: `OBL-CTRL-02`; `NFR-A11Y-004`; style guide §8.2.4; `COV-ACT-09`.

- **Group.** The legend gives the group an accessible name that identifies it as
  the delivery stream control and reports the stream currently in force, using
  that stream's `label` (§2.2). The reported in-force value remains unchanged
  until explicit submission applies the selection.
- **Radio.** Each radio's accessible name contains its visible label, which is
  the stream's `label` in peer vocabulary. The checked radio is the pending
  value, independent of the in-force value.
- **Apply.** The submit button's accessible name states that it applies the
  selection, and differs from the group name and from every radio name.
- **Screen-reader script** (the `OBL-CTRL-02` reviewer test; exact strings are
  `[GATED]` copy, the structure is not): on entering the group, the group name
  (control identity plus in-force stream label) followed by the focused radio's
  label and checked state; on arrowing to another radio, that radio's peer label
  and checked state, never an assertion that the stream has changed; on reaching
  Apply, a button name stating that it applies the selection.
- **Redundancy.** In-force is visible text in the legend; pending is the native
  checked mark plus the radio's visible label; neither is conveyed by colour
  alone (`PRIM-001` `state_redundancy`).

### 3.5 Advance advisement (before operation)

Authority: `OBL-ADV-01`; evidence model `N-06`; `NFR-A11Y-004`; D-043 (which
withdrew the "satisfied by construction" claim and required advisement
instead); 3.2.2 On Input is the criterion at stake.

- Rendered as **persistent visible text inside the fieldset**, before Apply in
  DOM reading order and in visual order.
- **Programmatically associated with both** the fieldset and the Apply button,
  so assistive technology receives it at the group and at the button. An
  accessible description alone is insufficient and is never the stated
  requirement; it is retained in addition, not instead.
- **Never** delivered by tooltip, `title` attribute, hover-only disclosure,
  focus-only disclosure, or description-only means. A hover- or focus-triggered
  advisement would be additional content on hover or focus (1.4.13) whose
  dismissal key, `Escape`, style guide §7.2 already binds to close panel / go
  back; persistent visible text avoids the conflict.
- **Identical wording in every stream** and on every route, explaining that
  applying the pending selection re-enters the experience in the chosen stream
  while preserving the current location. Exact public copy is `[GATED]`.
- **Reaches every user class before operation**: sighted mouse users and sighted
  keyboard users running no assistive technology read the visible text; screen
  readers receive the association at the group and at the button; screen
  magnifier users at 400% zoom still find the text before Apply, neither hidden
  nor clipped.
- The advisement is distinct from the post-change announcement (§3.6); neither
  substitutes for the other.

### 3.6 Change announcement (after the change), same shell

Authority: `OBL-ANN-01`; `OBL-STATE-02`; `FR-3D-013` (same-shell clause);
style guide §8.2.4; 4.1.3 Status Messages is the criterion at stake.

- The change is announced through the page status region as a **polite** status
  message. It does not interrupt, and within the same shell it does not move
  focus: focus stays on the operated control.
- The status region is named in the host anatomy (`page status region`), exists
  in the accessibility tree **empty** before the message is written, and never
  has its message inserted together with it.
- The announcement states the new stream in force by its `label`. The group name
  now reports that stream. Scroll position, any open panel, and the current
  route are preserved.
- Where the change crosses the semantic boundary, §3.11 governs instead: focus
  moves, and the announcement also names the arrival location.

### 3.7 Keyboard model and focus

Authority: `OBL-CTRL-04`; style guide §7.2; `PRIM-043`; 2.1.1, 2.1.2, 2.4.3,
2.4.7, 2.4.11 and 2.5.8 are the criteria at stake.

- One tab stop into the group; arrow keys move among the radios; Apply is a
  separate tab stop. Native `Enter` submission within the group targets Apply
  where the platform supplies that behaviour (§3.3).
- **`Escape` is not bound by the control** to anything. Pressing `Escape` with
  focus inside the control dismisses nothing, cancels nothing, and must not
  navigate; style guide §7.2 binds `Escape` to close panel / go back at the host
  level, and a visitor backing out of the control must not be navigated out of
  a room. The remaining reconciliation of §7.2's table is gate `UG-8`.
- **Focus visible in each stream's own rendering.** The focus indicator on each
  radio and on Apply uses the focus-ring tokens of §4: `semantic.focus.*` on any
  semantic shell (all four streams) and `semantic.focus.scene.*` where the
  control is re-hosted in the HUD over a canvas (`S-HIGH`, `S-MEDIUM`, `S-LOW`),
  measured per stream under §1.3.
- **Not obscured.** In the World streams the control sits in a persistent HUD
  over a canvas. When any part of the control has focus, no sticky or overlay
  element, including the HUD's own translucent panel, may entirely hide it
  (`OBL-CTRL-04` on 2.4.11; `PRIM-043` "does not obscure focus or content"; the
  human consequence recorded at obligations lines 470 to 473, where the focus
  ring lands behind the HUD's translucent panel). §4's `semantic.focus.scene.layer`
  is the token that carries this rule.
- **Target size.** Each radio with its label, and the Apply button, measure at
  least 24 by 24 CSS px, or carry the exact documented valid exception and
  measurement, in each stream's own rendering (freeze §4; `OBL-CTRL-04`).

### 3.8 Options above the WebGL ceiling

Authority: `OBL-CTRL-02`; `OBL-CTRL-05`; `OBL-STATE-05`; `FR-3D-014`; style
guide §8.2.2 step 1 and §8.2.4; `ACT-09` alternate path.

- Where the client cannot obtain a WebGL context, the three World-stream radios
  remain **present and disabled with a textual reason**. They are never hidden,
  never removed, and never distinguished by colour or dimming alone.
- The reason is stated as a **fact about the client**, never as a failure, an
  error or a recovery: no failure heading, no error styling, and no language of
  escape or contingency (`DS-S-SEMANTIC` `exception_rule`). Its copy is
  `[GATED]`; the words must not be out of place on a page the visitor chose
  deliberately (`OBL-CTRL-05` reviewer test).
- The `S-SEMANTIC` radio is always a live, selectable option; where the ceiling
  permits, the three World-stream radios are live, selectable options in
  `S-SEMANTIC` too, because `S-SEMANTIC` is a peer stream a visitor may be in
  by choice.
- A request that cannot be honoured at Apply time (for example a context lost
  after render, `PRIM-044` `context_loss`) is refused under
  `STATE-STREAM-CEILING-REFUSED` (§3.10): the visitor remains on the prior
  stream, the ceiling is stated and never silently substituted, and the group
  name continues to report the prior stream as in force.

### 3.9 Pseudo-states

Freeze §3.3 requires the five pseudo-states independently on every interactive
child. The control documents them on each radio (with its label) and on Apply.

| Pseudo-state | Radio (with label) | Apply | Rule inherited from freeze §3.3 |
|---|---|---|---|
| `base` | Native unchecked or checked rendering; visible label | Visible label; always present | — |
| `hover` | Pairing `[GATED]` (freeze §2.3: all interactive state pairings still to be decided) | Pairing `[GATED]` | Hover never carries exclusive meaning |
| `focus-visible` | `semantic.focus.*` or `semantic.focus.scene.*` per host (§3.7, §4) | Same | At least as discernible as hover; survives adjacent surfaces and forced colors; not clipped; verified with keyboard order, per stream |
| `pressed` | Native pressed rendering | Pairing `[GATED]` | Distinct from selected (checked, pending) and from current (in force) |
| `disabled` | Above the WebGL ceiling: present, disabled, textual reason (§3.8) | Documented as required by §3.3; no source authorizes disabling Apply, which is always present (`UG-5`) | Remains readable; cannot hide a required route; never the sole explanation for unavailability |

### 3.10 Transactional states

Freeze §3.3 keeps transactional states on a separate axis with visible text and a
redundant non-colour cue. The control uses the following subset, mapped to the
state IDs that `responsive-state-mode-matrix.csv` already carries. The matrix is
the authority for where each frame state lives; the distribution below was read
from its `required_values` and `critical_distinct_frame_values` columns with
`Import-Csv` (36 rows, revision 2) and is restated exactly. `OBL-STATE-01`'s
minimum (`SP-NAVIGATION` all four; `SP-WORLD` for the changed, write-failed and
ceiling-refused states; `SP-FIRST-VISIT` and `SP-RETURN-VISIT` for the changed,
write-failed and read-failed states) is met, and the first two states also
extend to every other public state profile.

| Frame state | State profiles carrying it in both `required_values` and `critical_distinct_frame_values` | Of the four profiles `OBL-STATE-01` names | Stream profiles carrying it in `critical_distinct_frame_values` |
|---|---|---|---|
| `STATE-STREAM-CHANGED` | `SP-PUBLIC-DOCUMENT`, `SP-PUBLIC-COLLECTION`, `SP-PUBLIC-DETAIL`, `SP-EVIDENCE-COLLECTION`, `SP-EVIDENCE-DETAIL`, `SP-NAVIGATION`, `SP-FIRST-VISIT`, `SP-RETURN-VISIT`, `SP-WORLD`, `SP-AI`, `SP-HANDOFF-MEDIA`, `SP-BOOKING`, `SP-CONTACT`, `SP-SYSTEM-RECOVERY` | All four: `SP-NAVIGATION`, `SP-WORLD`, `SP-FIRST-VISIT`, `SP-RETURN-VISIT` | `DS-S-HIGH`, `DS-S-MEDIUM`, `DS-S-LOW`, `DS-S-SEMANTIC` |
| `STATE-PREFERENCE-WRITE-FAILED` | The same fourteen profiles as `STATE-STREAM-CHANGED` | All four | The same four |
| `STATE-PREFERENCE-READ-FAILED` | `SP-NAVIGATION`, `SP-FIRST-VISIT`, `SP-RETURN-VISIT` | `SP-NAVIGATION`, `SP-FIRST-VISIT`, `SP-RETURN-VISIT`; **not `SP-WORLD`** | The same four |
| `STATE-STREAM-CEILING-REFUSED` | `SP-NAVIGATION`, `SP-WORLD` | `SP-NAVIGATION`, `SP-WORLD`; **not `SP-FIRST-VISIT`, not `SP-RETURN-VISIT`** | The same four |

The five staff profiles (`SP-AUTH`, `SP-STAFF-QUEUE`, `SP-STAFF-WORK`,
`SP-PUBLICATION`, `SP-AUDIT`) carry none of the four, consistent with the
excluded-surface scope marker of `EC-08`. `stream-in-force` and `stream-pending`
are values reported by the control, not frame states, and have no matrix row.

| State (component) | Matrix ID | Meaning | Visible text and non-colour cue | Focus | Announcement | Authority |
|---|---|---|---|---|---|---|
| `stream-in-force` | (value reported by the group name; not a frame state) | The stream currently applied | Legend text carrying the in-force `label` | — | — | `PRIM-001` `transactional_or_content_states`; `OBL-CTRL-02` |
| `stream-pending` | (value reported by the checked radio; not a frame state) | A checked radio not yet applied | Native checked mark plus label; never rendered or announced as in force | Retained on the radio | None | `PRIM-001`; `OBL-CTRL-02`; pending never reads as applied |
| `STATE-STREAM-CHANGED` | `STATE-STREAM-CHANGED` (homes per the distribution table above) | Apply activated, same shell | Group name reports the new stream; polite message in the status region | Retained on the operated control; scroll, open panel and route preserved | Polite; names the new stream | `OBL-STATE-02`; `FR-3D-013`; §8.2.4 |
| `STATE-PREFERENCE-WRITE-FAILED` | `STATE-PREFERENCE-WRITE-FAILED` (`PRIM-001` spells it `stream-preference-write-failed`; homes per the distribution table above) | The choice applied for the session but could not be stored | Text explaining, in plain terms, that the choice will not be remembered on the next visit; not an error the visitor caused; never blocking | Retained | Polite | `OBL-STATE-03`; `ACT-11` pattern; §8.2.2 step 5 |
| `STATE-PREFERENCE-READ-FAILED` | `STATE-PREFERENCE-READ-FAILED` (home on return: `SP-RETURN-VISIT`; also `SP-NAVIGATION` and `SP-FIRST-VISIT`; not `SP-WORLD`) | A stored choice could not be read | Text in the destination shell stating the stored choice could not be applied and that the visitor can re-select; never a silent return to a computed stream | — | Polite | `OBL-STATE-04` |
| `STATE-STREAM-CEILING-REFUSED` | `STATE-STREAM-CEILING-REFUSED` (`SP-NAVIGATION` and `SP-WORLD`; not `SP-FIRST-VISIT`, not `SP-RETURN-VISIT`) | A request above the ceiling refused at Apply time | Reason in text as a fact about the client; no error styling; group name still reports the prior stream | Retained | Polite | `OBL-STATE-05`; `ACT-09` alternate path |

Pending never looks or reads as applied, exactly as pending never looks or reads
as success in freeze §3.3. The control never reports a stream the visitor did not
apply (`OBL-STATE-05`, 4.1.2 is the criterion at stake). Explanation copy for the
failure states is `[GATED]`; where the explanation is rendered relative to the
fieldset is recorded on the `OBL-STATE-03` and `OBL-STATE-04` frames rather than
decided here.

### 3.11 The semantic boundary crossing

Authority: `OBL-BND-01` to `OBL-BND-04`; `FR-3D-013` (boundary clause);
`FR-3D-016`; style guide §8.2.4 (crossing paragraph) and §8.2.6; D-045
resolutions 1 (gate G-1) and 6 (gate G-7); `OBL-TRACE-03`; `UXTEST-046`.

When the applied stream moves between `S-SEMANTIC` and a World stream, the two
shells are different subtrees and the operated control does not survive. The
component contract therefore states the crossing as an ordered sequence with no
overlap, which the boundary frame annotates (`OBL-BND-04`):

1. The outgoing shell is removed from the accessibility tree.
2. The incoming shell is added, including its page status region, present and
   **empty**.
3. Focus is set on the **delivery stream control in the destination shell** —
   the same component by role and accessible name, in the same relative
   position, reporting the new stream as in force — and is **visibly
   indicated** on arrival with the destination host's focus-ring token (§4).
   Focus is never dropped to the document body and never left on a destroyed
   node (`OBL-BND-01`).
4. The announcement is written into the status region, politely, naming the
   new stream in force, the arrival location by its name, and, where the
   arrival location is not the canonical mapping of the departure location
   (nearest-ancestor entry, `OBL-BND-03`), that fact and why (`OBL-BND-02`).
5. In a World destination only, the canvas is added **after** the incoming shell
   is announced, never before. The canvas is not present in `S-SEMANTIC` at all.

`FR-3D-013` carries both cases as accepted at D-045: within one shell focus does
not move (§3.6); across the semantic boundary focus moves to the destination
control (`OBL-TRACE-03`). The two rules are not in conflict, and the component
must implement both.

**Process state.** A stream change never discards booking process state. A held
slot, a verified email address and entered field values survive every crossing,
including the semantic one, and are rehydrated into the incoming shell before
that shell is announced (`FR-3D-016`; §8.2.6; D-045 resolution 6, gate G-7). If
process state genuinely cannot be carried, the change is **refused and
explained** under the `ACT-11` pattern and the visitor keeps their work; a
silent reset is never permitted. Because process state survives, the advisement
(§3.5) does not need to warn of loss; it explains re-entry and preserved
location only.

### 3.12 Responsive, input and mode obligations

Authority: `OBL-CTRL-03`, `OBL-CTRL-05`, `OBL-CTRL-06`; `NFR-A11Y-004`;
`PRIM-001` `responsive_and_mode_obligations`; freeze §4.

- **320 CSS px.** Content, labels, in-force and pending state, advisement,
  unavailability text and Apply remain present in logical order. Where narrow
  viewports collapse utility navigation into a labelled disclosure, the control
  is reachable through that disclosure with predictable focus entry and return;
  this is evidenced at `VP-320` in `S-SEMANTIC` specifically, the stream in
  which the disclosure is the only path to the control.
- **400% zoom.** The advisement remains before Apply, neither hidden nor
  clipped; the focus indicator is not clipped.
- **Text spacing and long content.** Labels, legend, advisement and
  unavailability text wrap without truncating the accessible name or obscuring
  adjacent controls; translated-length simulations are included.
- **Forced colors** (`MODE-FORCED-COLORS`). The checked radio, the in-force
  stream, the focus indicator and any unavailable-option state remain
  distinguishable without authored colour: native radio rendering, legend text,
  the fieldset boundary drawn with a border rather than a surface change alone,
  and text reasons carry the state. One forced-colors capture is bound to the
  control in `S-SEMANTIC` (`OBL-CTRL-06`).
- **Grayscale, unavailable font and unavailable image.** No state of the control
  depends on colour, a font, or an image.
- **Reduced motion.** Applying a stream produces the complete stable state
  before any nonessential motion; the advisement and announcement never wait
  for animation. Reduced motion never changes the stream (§8.2.2 step 6;
  `NFR-A11Y-006`).
- **Pointer and touch.** Selection and activation follow §3.3; activation
  occurs on release; there is no drag.
- **Low power, offline, asset failure.** The control is present and operable in
  `PRIM-044`'s recovery surface and in the offline and unavailable states of
  `PRIM-001`; its own failure states are §3.10.

### 3.13 Component tokens (reserved; alias references only)

Per freeze §2.1 and §2.3 last row, component tokens reference semantic aliases
only and embed no raw colour, type, spacing, radius, stroke or motion value.
They are created only after the semantic aliases and this anatomy are approved;
the names below are reserved so the ledger has a place for them. The code
pattern is the freeze §2.3 pattern
`--hd-{component}-{variant}-{state}-{property}` with `{component}` =
`delivery-stream-control`.

| Component token (design) | Code token | May reference only | Decision still required |
|---|---|---|---|
| `component.delivery-stream-control.fieldset.{base}.{border,background}` | `--hd-delivery-stream-control-fieldset-base-{border,background}` | `semantic.border.strong` or `semantic.border.interactive`; `semantic.surface.{canvas,raised}` per host | Which boundary alias; the boundary must reach at least 3:1 and survive forced colors as a border |
| `component.delivery-stream-control.legend.{base}.text` | `--hd-delivery-stream-control-legend-base-text` | `semantic.text.{primary,secondary}` | Which text alias |
| `component.delivery-stream-control.advisement.{base}.text` | `--hd-delivery-stream-control-advisement-base-text` | `semantic.text.{primary,secondary}` | Which text alias; the advisement is essential instruction, so its contrast is measured as normal text at least 4.5:1 per stream |
| `component.delivery-stream-control.radio-label.{base,hover,focus-visible,pressed,disabled}.text` | `--hd-delivery-stream-control-radio-label-{state}-text` | `semantic.text.*`; `semantic.field.{label,disabled}` | Hover and pressed pairings (`UG-6`) |
| `component.delivery-stream-control.radio.{focus-visible}.{ring,ring-width,offset}` | `--hd-delivery-stream-control-radio-focus-visible-{ring,ring-width,offset}` | `semantic.focus.*` on semantic shells; `semantic.focus.scene.*` in the HUD | Whether the native input itself may be styled at all without losing platform forced-colors rendering (`UG-7`) |
| `component.delivery-stream-control.apply.{base,hover,focus-visible,pressed,disabled}.{foreground,background,border}` | `--hd-delivery-stream-control-apply-{state}-{foreground,background,border}` | `semantic.action.{primary,secondary}.*`; `semantic.focus.*` or `semantic.focus.scene.*` for focus-visible | Primary versus secondary action alias (`UG-6`); amber must not be inferred as destructive (freeze §2.3) |
| `component.delivery-stream-control.unavailable.{base}.{text,marker}` | `--hd-delivery-stream-control-unavailable-base-{text,marker}` | `semantic.text.*`; `semantic.status.information` | Never `semantic.status.error` and never `semantic.status.attention` alone: the reason is a fact about the client, not a failure (`OBL-CTRL-05`) |
| `component.delivery-stream-control.explanation.{base}.{text,marker}` | `--hd-delivery-stream-control-explanation-base-{text,marker}` | `semantic.text.*`; `semantic.status.{information,attention}` | Which status alias for the write-failed and read-failed explanations; never blocking and never presented as an error the visitor caused (`OBL-STATE-03`) |

No component token above carries a value in this document.

---

## 4. Focus-ring tokens including the 3D focus ring — reviewer-test hit (c)

These are the **focus-ring tokens** required by `OBL-GRAM-03`, D-045 gate G-6
and R-039.

### 4.1 The mandate

- Style guide **§4.1**, hotspot state table, row `Keyboard focus`: "Persistent
  3 px focus ring at ≥3:1 against every adjacent scene colour, plus the label in
  its expanded form. Present whether or not the pointer is used, and unaffected
  by `prefers-reduced-motion`." §4.1 adds that the focus row is normative, not
  planned: a stream that cannot show it cannot ship.
- **`NFR-A11Y-005`**: every interactive 3D state carries a non-colour,
  non-motion cue and a persistent keyboard focus indicator at ≥3:1 against every
  adjacent scene colour.
- **`OBL-CTRL-04`**: the focus indicator on each radio and on Apply meets the
  focus-indicator obligation in each stream's own rendering; in the 3D streams
  the adjacent colours are scene colours and vary; no sticky or overlay element
  may entirely hide the focused control (2.4.11). Its human consequence (lines
  470 to 473): a keyboard user in the World tabs to the stream control, the
  focus ring lands behind the HUD's own translucent panel (§6.2), and they
  cannot see where they are.
- **`OBL-BND-01`**: §4.1's focus rule covers hotspots only and does not reach the
  destination control, so programmatic focus on arrival must be visibly
  indicated by a rule that does reach it. The tokens below reach every focusable
  element in every host.
- **`OBL-TRACE-03`**: the same-shell and boundary focus rules are both carried
  (§3.6, §3.11); the tokens do not change which rule applies, only how the
  indicator renders.
- Freeze **§2.3** reserves `semantic.focus.{ring,offset}` as `--hd-focus-*` with
  thickness, offset, clipping prevention and surface pairings still to be
  decided; freeze **§3.3** and **§5** require focus-visible to be at least as
  discernible as hover, to survive adjacent surfaces and forced colors, to be
  unclipped, and to reach at least 3:1.
- Freeze **§7**: the protected prototype and exterior 3D evidence are not sources
  for production styling. The hex values in style guide §3.1 and §4.1
  (`#00BFFF`, `#FFFFFF`, `#F44A25`, `#666666`) are prototype-era palette entries
  that do not exist in the identity source, so no focus token below adopts them.

### 4.2 Token definitions

| Design alias | Code token | Value or rule | Source and status |
|---|---|---|---|
| `semantic.focus.ring` | `--hd-focus-ring` | Colour of the focus indicator on every focusable element of a semantic shell in every stream. Must reach at least 3:1 against every adjacent surface it is drawn on, measured per stream; each surface pairing recorded in the ledger. Value `[GATED]` | Freeze §2.3 (decision still required); §1.3. The identity source declares `color.signal.cyan.onDark` on `color.ink` at 10.86:1 with use "text, focus, icons, graphics" — a test input, not an approval. Proposed value source: `packages/design-system/tokens.json` `hd-focus-ring` (`{hd-color-signal-cyan-on-light}` in the light theme, `{hd-color-signal-cyan-on-dark}` in the dark theme, with measured 5.68:1 on paper and 3.22:1 on ink in light, 10.86:1 on ink in dark) — **[PROPOSED]**, never authority |
| `semantic.focus.ring-width` | `--hd-focus-ring-width` | Thickness of the 2D ring. Value `[GATED]` | Freeze §2.3 "thickness"; proposed value source `tokens.json` `hd-focus-ring-width` 3px — **[PROPOSED]**. The only source-exact width in the package is §4.1's 3 px, which mandates the scene ring |
| `semantic.focus.offset` | `--hd-focus-offset` | Outline offset of the 2D ring; clipping prevention stands. Value `[GATED]` | Freeze §2.3 "offset, clipping prevention"; proposed value source `tokens.json` `hd-focus-offset` 4px, equal to `space.scale[0]` 4 px — **[PROPOSED]** |
| `semantic.focus.scene.ring` | `--hd-focus-scene-ring` | Colour of the focus ring drawn for WebGL hotspots and for HUD controls, including the re-hosted delivery stream control, in `S-HIGH`, `S-MEDIUM` and `S-LOW`. Obligation: at least 3:1 against every adjacent scene colour, in each stream's own rendering. Value `[GATED]` | Style guide §4.1; `NFR-A11Y-005`; `OBL-CTRL-04`. Measurement method is gate `UG-1`; not the prototype values of §3.1 or §4.1 |
| `semantic.focus.scene.ring-width` | `--hd-focus-scene-ring-width` | **3 px** | Style guide §4.1, exact |
| `semantic.focus.scene.offset` | `--hd-focus-scene-offset` | Offset of the scene ring from the focused hotspot or HUD control; clipping prevention stands. Value `[GATED]` | Freeze §2.3 by extension; no source states it |
| `semantic.focus.scene.layer` | `--hd-focus-scene-layer` | Rule: the scene ring is rendered in the DOM overlay layer above `semantic.elevation.panel` (the HUD's translucent panel, §6.2) and above every sticky HUD element, and is never rendered inside the canvas alone, so that no part of a focused control or hotspot indicator is obscured | `OBL-CTRL-04` on 2.4.11; `PRIM-043` "does not obscure focus or content" and "no canvas-only control"; obligations lines 470 to 473; freeze §2.3 `semantic.elevation.*` |
| `semantic.focus.scene.contrast-floor` | `--hd-focus-scene-contrast-floor` | **3:1**, the floor against every adjacent scene colour | Style guide §4.1; `NFR-A11Y-005`; freeze §5. A rule-valued row, like `radius.status` in freeze §2.2 |
| `semantic.focus.scene.motion` | `--hd-focus-scene-motion` | Rule: static and persistent; present whether or not the pointer is used; unaffected by `prefers-reduced-motion` | Style guide §4.1 (line 93) and §7.3. The further clause "never animated across the viewport" occurs only in `packages/design-system/tokens.json` and `README.md` — **[PROPOSED]**, never authority — and is not part of the rule |

Every ring drawn from these tokens is accompanied by the non-colour cue its host
already requires: the label in its expanded form on a hotspot (§4.1); visible
label text on the control's radios and on Apply (§3.4).

### 4.3 Per-stream resolution

| Stream | WebGL hotspots (in the canvas) | HUD controls, including the re-hosted stream control | Semantic shell controls, including the stream control in utility navigation |
|---|---|---|---|
| `S-HIGH` | `semantic.focus.scene.*` | `semantic.focus.scene.*` | `semantic.focus.*` |
| `S-MEDIUM` | `semantic.focus.scene.*` | `semantic.focus.scene.*` | `semantic.focus.*` |
| `S-LOW` | `semantic.focus.scene.*` | `semantic.focus.scene.*` | `semantic.focus.*` |
| `S-SEMANTIC` | No canvas exists; not rendered | No HUD exists; not rendered | `semantic.focus.*` |

In `S-SEMANTIC` the ordinary 2D ring is the equivalent of the 3D ring: the
mapping ledger records `semantic.focus.scene.*` as resolving to
`semantic.focus.*` in `S-SEMANTIC`, so no token is undefined in any stream and
no export can emit a scene ring into a document with no canvas. The sources
establish only that `S-SEMANTIC` has no canvas and no HUD (`OBL-CTRL-05`; style
guide §8.2.4); the resolution rule itself is recorded assumption **A-4** (§7),
safe and reversible, and is cited as such wherever it reaches the frozen file
(`INS-04`, `INS-09`). Under §1.3, the
2D ring on a semantic shell in `S-HIGH` is measured in `S-HIGH` and the same
ring in `S-SEMANTIC` is measured in `S-SEMANTIC`; the two measurements are
recorded separately even where the renderings coincide.

### 4.4 Evidence the tokens require

- One `focus-visible` frame per stream for the control (`OBL-CTRL-04` reviewer
  test), each showing a visible indicator with nothing obscuring it and each
  carrying its `STREAM_*` token; the `S-SEMANTIC` frame at `VP-DESKTOP` also
  carries the visible advisement (`OBL-ADV-01` frame).
- The boundary frame with focus visibly indicated on the destination control
  (`OBL-BND-01`).
- The hotspot focus frame and HUD annotation relocated by `N-03` to
  `TPL-WORLD-SHELL` and `TPL-WORLD-HUD` (batch B07), which draw the scene ring
  above the translucent panel.
- Contrast calculations for each ring against each adjacent surface or scene
  sample, per stream, per freeze §8 item 7 as amended in §5 (`INS-13`), with the
  scene sampling method itself gated (`UG-1`).

---

## 5. Mechanical application plan

The later slice that re-opens `DESIGN_SYSTEM_IMPLICATIONS.md` under the founder
acceptance decision (`UG-9`) applies the insertions below in order. Each names
the target section of the freeze file, the operation, the anchor (the exact
existing text the insertion follows or replaces), and the exact text, given in
the fenced blocks that follow the table. `[GATED]` placeholders inside the
texts are filled only by the acceptance decision and are otherwise left as
written. The freeze file wraps its prose at about 80 columns, so every anchor
below is matched on whitespace-normalized text (line breaks treated as single
spaces); each anchor occurs exactly once in the freeze file. The same slice must update `$expectedDesignSystemHash` in
`validation/validate-ui-reference-design.ps1` to the new file hash and record
the old hash as provenance beside the existing ones; this document does not do
so.

| ID | Target section | Operation | Anchor in the freeze file | Text | Reviewer-test hit |
|---|---|---|---|---|---|
| `INS-01` | Header | Insert a line after the `**Amended:**` line | `**Amended:** 2026-09-06 under D-042 and D-043 ...` | Block `INS-01` | — |
| `INS-02` | §1.1 | Append a bullet after the `**Bounded inventory:**` bullet | `...it must not hide the gap in a one-off screen component or invented product fact.` | Block `INS-02` | — |
| `INS-03` | §2.2 | Append a paragraph after the closing paragraph of §2.2 | `...Opacity, glow, blur, or material appearance cannot repair insufficient contrast.` | Block `INS-03` | — |
| `INS-04` | §2.3 | Replace the `semantic.focus.{ring,offset}` row; insert two rows before the `component.*` row | `\| \`semantic.focus.{ring,offset}\` \| \`--hd-focus-*\` \| Thickness, offset, clipping prevention, and surface pairings \|` and `\| \`component.*\` \| ...` | Block `INS-04` | (c) |
| `INS-05` | §2.4 | Append a bullet after the last bullet | The bullet beginning `- Dark and light are controlled surface pairings. Forced colors, grayscale,` | Block `INS-05` | — |
| `INS-06` | §3.1 | Replace the `Shell and navigation` row and the `Overlay and immersive` row | The two rows quoted verbatim in anchor block `INS-06` (each occurs exactly once in the freeze file, at lines 206 and 211) | Block `INS-06` | (b) |
| `INS-07` | §3.3 | Append a paragraph after the transactional-states paragraph | `...dialogs, error summaries, and deliberate navigation may move focus under their own contract.` | Block `INS-07` | — |
| `INS-08` | §3 | Insert a new subsection `### 3.4 Delivery stream control component` after §3.3 and before `## 4.` | `## 4. Responsive, input, and mode obligations` | Block `INS-08` | (b) |
| `INS-09` | §4 | Append four bullets after the last bullet | `...evidence status, error/success distinction, and data-series identity without depending on color or shadow.` | Block `INS-09` | — |
| `INS-10` | §5 | Replace the contrast bullet | `- Contrast is checked per rendered state: normal text at least 4.5:1; large text only under its valid size/weight rule; focus and meaningful non-text boundaries at least 3:1. The identity pairings do not waive component-level testing.` | Block `INS-10` | (a) |
| `INS-11` | §5 | Append three bullets after the last bullet | The bullet beginning `- No accessible label, role, state, route title, evidence class, or recovery` | Block `INS-11` | (b), (c) |
| `INS-12` | §8 item 4 | Replace `UXTEST-001 through UXTEST-045` with `UXTEST-001 through UXTEST-046` | `UXTEST-001 through UXTEST-045.` | Literal, in this row | — |
| `INS-13` | §8 item 7 | Append two sentences to the end of item 7, leaving its existing words unchanged | The item beginning `7. Contrast calculations for every rendered state and adjacent surface` | Block `INS-13` | (a) |
| `INS-14` | §8 | Append items 15, 16 and 17 after item 14 | The item beginning `14. Controlled-clock evidence for every user time limit` | Block `INS-14` | (b), (c) |

The three OBL-GRAM-03 reviewer-test hits after application are: **(a)** the
per-stream contrast rule at `INS-10` (search "per stream"); **(b)** the
stream-control component at `INS-06` and `INS-08` (search "Delivery stream
control"); **(c)** the focus-ring tokens at `INS-04` (search "focus-scene").

**Block `INS-01`**

```
**Amended (R-039):** [GATED: date of the acceptance decision] under D-046 and
[GATED: acceptance decision ID], applying `DESIGN_SYSTEM_AMENDMENT_R-039.md`:
adds the delivery-stream axis, the four stream tokens, the delivery stream
control component, and the focus-ring tokens including the 3D focus ring. No
inherited identity value, primitive ID, route, flow or state profile changed.
```

**Block `INS-02`**

```
- **Delivery-stream axis:** the four peer delivery streams `S-HIGH`,
  `S-MEDIUM`, `S-LOW` and `S-SEMANTIC` (D-039; `FR-3D-011`) are a design-system
  dimension: a required verification context (§2.4), a semantic token family
  (§2.3), and a component property of the delivery stream control (§3.4). The
  streams are peers carrying equivalent core journeys; `S-SEMANTIC` is a
  first-class product surface served from first paint to clients without a
  WebGL context and selectable by any visitor (`NFR-A11Y-003`). The stream in
  force never decides whether the World canvas is entered (D-045;
  `FR-3D-015`).
```

**Block `INS-03`**

```
The delivery-stream axis adds no identity source token and changes no value
above. The stream tokens and the focus-ring tokens are semantic aliases (§2.3)
that consume identity values only through the alias layer. The identity
source's declared pairing of `color.signal.cyan.onDark` on `color.ink`
(10.86:1; declared use: text, focus, icons, graphics) is a test input for focus
pairings in every stream and an approval in none. Every pairing in the mapping
ledger records the delivery stream in which it was measured (§5).
```

**Block `INS-04`** — the replaced focus row, then the two new rows (insert the
new rows immediately before the `component.*` row):

```
| `semantic.focus.{ring,ring-width,offset}` | `--hd-focus-*` | Colour, thickness, offset, clipping prevention, and surface pairings, measured per delivery stream; the 2D ring is the `S-SEMANTIC` equivalent of the scene ring |
| `semantic.stream.{high,medium,low,semantic}.{id,profile,evidence-token,label,presentation,canvas}` | `--hd-stream-*` | Exact visible label copy per stream in peer vocabulary (gated public copy); the token carries the stream identifier, the `DS-S-*` evidence profile, the `EC-08` `STREAM_*` token, the style guide §8.2 presentation text and the canvas fact, and never a raw rendering value, a U-03 tier boundary, an ordering, a mode value or an availability |
| `semantic.focus.scene.{ring,ring-width,offset,layer,contrast-floor,motion}` | `--hd-focus-scene-*` | The focus ring for WebGL hotspots and HUD controls in `S-HIGH`, `S-MEDIUM` and `S-LOW`: width 3 px and a 3:1 floor against every adjacent scene colour (style guide §4.1; `NFR-A11Y-005`), rendered above `semantic.elevation.panel` so no part is obscured; ring colour, offset and the adjacency sampling method remain gated; resolves to `semantic.focus.*` in `S-SEMANTIC` (recorded assumption A-4 of `DESIGN_SYSTEM_AMENDMENT_R-039.md`) |
```

**Block `INS-05`**

```
- The four delivery streams `S-HIGH`, `S-MEDIUM`, `S-LOW` and `S-SEMANTIC` are
  required verification contexts, each verified separately: a pairing, state or
  rendering verified in one stream is not verified in another. The stream axis
  uses the role `stream` with the variant values `high`, `medium`, `low` and
  `semantic` (`hd/semantic/stream/{variant}/{property}`;
  `--hd-stream-{variant}-{property}`), and the primitive variant values
  `stream-high`, `stream-medium`, `stream-low` and `stream-semantic`.
```

**Anchor block `INS-06`** — the two rows to replace, quoted verbatim from the
freeze file:

```
| Shell and navigation | Landmarks, skip paths, primary navigation, breadcrumbs, directory/search, canonical location, and safe exclusions |
| Overlay and immersive | Dialog, drawer, panel, onboarding, HUD, exit, Quick Access, and asset/device recovery |
```

**Block `INS-06`** — replacement rows:

```
| Shell and navigation | Landmarks, skip paths, primary navigation, breadcrumbs, directory/search, canonical location, safe exclusions, and the delivery stream control (`HD/Shell and navigation/Delivery stream control`; code `DeliveryStreamControl`; hosted by `PRIM-001` in every stream; §3.4) |
| Overlay and immersive | Dialog, drawer, panel, onboarding, HUD, exit, Quick Access, asset/device recovery, and the delivery stream control re-hosted by `PRIM-042`, `PRIM-043` and `PRIM-044` in the World streams (§3.4) |
```

**Block `INS-07`**

```
The delivery stream control (§3.4) adds the transactional states
`stream-in-force` and `stream-pending`, reported respectively by the group
accessible name and by the checked radio, and four frame states whose homes
are the state profiles of `responsive-state-mode-matrix.csv`, which governs
this list through its `required_values` and `critical_distinct_frame_values`
columns: `STATE-STREAM-CHANGED` and `STATE-PREFERENCE-WRITE-FAILED` on
`SP-PUBLIC-DOCUMENT`, `SP-PUBLIC-COLLECTION`, `SP-PUBLIC-DETAIL`,
`SP-EVIDENCE-COLLECTION`, `SP-EVIDENCE-DETAIL`, `SP-NAVIGATION`,
`SP-FIRST-VISIT`, `SP-RETURN-VISIT`, `SP-WORLD`, `SP-AI`, `SP-HANDOFF-MEDIA`,
`SP-BOOKING`, `SP-CONTACT` and `SP-SYSTEM-RECOVERY`;
`STATE-PREFERENCE-READ-FAILED` on `SP-NAVIGATION`, `SP-FIRST-VISIT` and
`SP-RETURN-VISIT` only; `STATE-STREAM-CEILING-REFUSED` on `SP-NAVIGATION` and
`SP-WORLD` only; and all four as `critical_distinct_frame_values` of
`DS-S-HIGH`, `DS-S-MEDIUM`, `DS-S-LOW` and `DS-S-SEMANTIC`. Pending never looks
or reads as applied, and the control never reports a stream the visitor did not
apply.
```

**Block `INS-08`**

```
### 3.4 Delivery stream control component

Design component set `HD/Shell and navigation/Delivery stream control`; code
component `DeliveryStreamControl`; anatomy owned by `PRIM-001` and re-hosted by
`PRIM-042`, `PRIM-043` and `PRIM-044`; no new primitive ID. Authority: D-045
resolutions 1, 3 and 6; `FR-3D-013` to `FR-3D-016`; `NFR-A11Y-004`; style guide
§8.2.4 to §8.2.6; `OBL-CTRL-01` to `OBL-CTRL-06`, `OBL-ADV-01`, `OBL-ANN-01`,
`OBL-BND-01` to `OBL-BND-04`, `OBL-STATE-01` to `OBL-STATE-05`; `UXTEST-046`.

- **Anatomy:** `fieldset`; `legend` naming the delivery stream control and the
  in-force stream; four native radio inputs sharing one name, one per stream;
  persistent visible advisement inside the fieldset, before Apply in DOM
  reading order and visual order (its placement relative to the radios is
  recorded assumption A-2 of `DESIGN_SYSTEM_AMENDMENT_R-039.md`, not a source
  constraint); separate, always-present Apply submit button. The host's page
  status region carries the announcement and exists, empty, before any message
  is written into it.
- **Activation:** moving among the radios by arrow, Tab, pointer or touch
  changes only the checked state. The stream applies only on explicit Apply
  activation by Enter, Space, pointer or touch, or native Enter submission of
  the same form to that button; never on focus, selection, blur, arrow movement
  or timeout. A select applying on change, and any listbox, combobox, menu or
  radio group applying on selection, are prohibited.
- **Names:** the group name identifies the control and reports the in-force
  stream until submit; the checked radio reports the pending selection
  independently; Apply's name states that it applies the selection and differs
  from the group and radio names; radio labels use the peer stream vocabulary
  carried by `--hd-stream-*-label`, with none of the label words `NFR-A11Y-004`
  prohibits. Exact public copy is gated.
- **Advisement:** visible text inside the fieldset before Apply in DOM and
  visual order, identical wording in every stream, programmatically associated
  with both the fieldset and Apply; never tooltip, title, hover-only,
  focus-only or description-only.
- **Announcement:** a polite message in the page status region without moving
  focus within a shell. Across the semantic boundary: the outgoing shell leaves
  the accessibility tree; the incoming shell and its empty status region are
  added; focus moves to the destination control, visibly indicated and
  reporting the new stream; the announcement names the new stream and the
  arrival location; in a World destination the canvas is added only after the
  incoming shell is announced. Booking process state survives every crossing or
  the change is refused and explained under the `ACT-11` pattern.
- **Presence:** on every route in every stream, in the same position under the
  same name, reachable without a canvas and without traversing main content; on
  `ROUTE-HOME`'s first frame in every stream with the canvas not entered; in
  `S-SEMANTIC` in the utility navigation, reachable through the narrow
  disclosure at 320 CSS px. Radios above the WebGL ceiling remain present and
  disabled with a textual reason stated as a fact about the client, never
  hidden and never distinguished by colour or dimming alone.
- **States:** the five pseudo-states of §3.3 on each radio and on Apply, with
  hover and pressed pairings still to be decided; the transactional states of
  §3.3 as amended, each with visible text and a non-colour cue.
- **Keyboard and focus:** one tab stop into the group, arrows among the radios,
  Apply a separate tab stop; the control binds nothing to Escape;
  focus-visible on each radio and on Apply uses `semantic.focus.*` on a
  semantic shell and `semantic.focus.scene.*` in the HUD, measured per stream
  and never obscured by the HUD panel; targets at least 24 by 24 CSS px per
  stream.
- **Modes:** 320 CSS px, 400% zoom (advisement still before Apply, unclipped),
  text spacing, forced colors (checked, in-force, focus and unavailable state
  distinguishable without authored colour), grayscale, reduced motion,
  unavailable font and image.
- **Tokens:** `component.delivery-stream-control.*`
  (`--hd-delivery-stream-control-{variant}-{state}-{property}`) reference
  semantic aliases only.
```

**Block `INS-09`**

```
- Every obligation in this section is verified within each delivery stream
  separately (`S-HIGH`, `S-MEDIUM`, `S-LOW`, `S-SEMANTIC`); evidence names its
  stream and is never inherited across streams.
- At 320 CSS px in `S-SEMANTIC`, the delivery stream control is reachable
  through the narrow navigation disclosure; that reachability is evidenced in
  `S-SEMANTIC` specifically.
- In forced colors, the delivery stream control's checked radio, in-force
  stream, focus indicator and unavailable-option state remain distinguishable
  without authored colour.
- In the World streams, the focus ring for hotspots and HUD controls
  (`semantic.focus.scene.*`) renders above the HUD's translucent panel and every
  sticky element, so no focused control is obscured; in `S-SEMANTIC` no canvas
  and no HUD exist and the ordinary ring applies (recorded assumption A-4 of
  `DESIGN_SYSTEM_AMENDMENT_R-039.md`).
```

**Block `INS-10`** — replacement bullet:

```
- Contrast is checked per rendered state and per stream: normal text
  at least 4.5:1; large text only under its valid size/weight rule; focus and
  meaningful non-text boundaries at least 3:1. Every contrast, focus-order and
  target-size measurement, and every other verification context in §2.4, is
  taken within one named stream (`S-HIGH`, `S-MEDIUM`, `S-LOW` or `S-SEMANTIC`)
  against that stream's own rendering and is never inherited by another stream;
  aggregate evidence that names no stream, or another stream, discharges no
  per-stream obligation (`NFR-A11Y-002`). The identity pairings do not waive
  component-level testing in any stream.
```

**Block `INS-11`**

```
- The delivery stream control (§3.4) is operable by keyboard in every stream
  with native radio-group semantics and a separate Apply tab stop; selection
  never applies a stream; it binds nothing to Escape; its visible advisement
  precedes Apply and reaches sighted mouse, sighted keyboard, screen-reader and
  400%-zoom users before operation.
- A stream change is announced politely in a status region that already exists
  empty; within a shell focus does not move; across the semantic boundary focus
  moves to the destination shell's delivery stream control, visibly indicated,
  and the announcement names the new stream and the arrival location.
- Focus indicators use `semantic.focus.*` on semantic shells and
  `semantic.focus.scene.*` for WebGL hotspots and HUD controls, at least 3:1
  against every adjacent surface or scene colour in each stream's own rendering.
```

**Block `INS-13`** — sentences appended to item 7:

```
   Every calculation is taken in each of the four delivery streams separately,
   against that stream's own rendering, and each evidence ID carries its
   `EC-08` `STREAM_*` token. A calculation from one stream is never inherited
   by another.
```

**Block `INS-14`**

```
15. Delivery stream control evidence per `B01.required_visual_evidence`: one
    frame per stream showing the control reporting that stream as in force in
    its accessible name, reachable without a canvas; the visible advisement in
    `focus-visible` at `VP-DESKTOP` in `S-SEMANTIC`; `VP-320` reachability
    through the narrow disclosure in `S-SEMANTIC`; the forced-colors capture in
    `S-SEMANTIC`; `STATE-STREAM-CHANGED` and `STATE-PREFERENCE-WRITE-FAILED` on
    `TPL-GLOBAL-NAVIGATION` in each stream; the boundary frame annotated with
    the five-step tree ordering; and `UXTEST-046` execution evidence for names,
    associations and activation, which screenshots alone cannot establish.
16. Focus-ring evidence per stream: a `focus-visible` frame of the delivery
    stream control in each stream with nothing obscuring the indicator; the
    hotspot focus frame and HUD annotation on `TPL-WORLD-SHELL` and
    `TPL-WORLD-HUD` showing `semantic.focus.scene.*` above the translucent
    panel; and the scene adjacency sampling method, once decided, applied to
    each World stream.
17. Mapping-ledger rows for `semantic.stream.*`, `semantic.focus.*`,
    `semantic.focus.scene.*` and `component.delivery-stream-control.*`, each
    recording the design path, the code token, the source path, and the stream
    in which every pairing was measured.
```

---

## 6. Traceability

| Source | ID or section | What it fixes in this amendment |
|---|---|---|
| Decision | D-039 | Four peer streams, Option A; peer vocabulary; the axis exists (§1) |
| Decision | D-043 | `ACT-09` re-homed to `SP-NAVIGATION` and B01; advance advisement replaces the withdrawn "satisfied by construction" claim (§3.5, §3.10) |
| Decision | D-044 | Reviewers define, producer implements; the [PROPOSED SPECIFICATION] format of this document |
| Decision | D-045 resolution 1 (gate G-1) | Stream and canvas are different things; first frame is a non-World shell carrying the control (§1.2, §3.1) |
| Decision | D-045 resolution 3 | Role and activation model normative (§3.3, §3.4, §3.5) |
| Decision | D-045 resolution 6 (gate G-7) | Process state survives every crossing; `FR-3D-016` (§3.11) |
| Decision | D-045 resolution 7 (gate G-6) | The gap this amendment closes; freeze file untouched until acceptance (§5, `UG-9`) |
| Decision | D-046 | Commission; independence of the author; review against `OBL-GRAM-03`; export is input, not authority (§4.2) |
| Requirement | `FR-3D-010` | `S-SEMANTIC` is a P0 peer surface (§1.1) |
| Requirement | `FR-3D-011` | Four peer streams; `id` property (§2.2) |
| Requirement | `FR-3D-012` | U-03 stays gated; no boundary in a token (§2.3) |
| Requirement | `FR-3D-013` | Same-shell and boundary focus rules (§3.6, §3.11) |
| Requirement | `FR-3D-014` | Anatomy, activation, above-ceiling radios (§3.2, §3.3, §3.8) |
| Requirement | `FR-3D-015` | Control on `ROUTE-HOME` first frame, canvas not entered (§3.1) |
| Requirement | `FR-3D-016` | Process state survival or refusal under `ACT-11` (§3.11) |
| Requirement | `NFR-A11Y-002` | Per-stream contrast rule (§1.3, `INS-10`) |
| Requirement | `NFR-A11Y-003` | `S-SEMANTIC` peer status in every label and state (§2.2, §3.8) |
| Requirement | `NFR-A11Y-004` | Names, advisement, 400% zoom, gated copy (§3.4, §3.5, §3.12) |
| Requirement | `NFR-A11Y-005` | 3:1 floor and persistence of the 3D ring (§4) |
| Requirement | `NFR-A11Y-006` | Reduced motion never changes the stream (§3.12) |
| Primitive | `PRIM-001` | Anatomy, variants, states, presence in all four streams (§3.2, §3.10) |
| Primitive | `PRIM-042`, `PRIM-043`, `PRIM-044` | Re-hosting in the World streams; HUD must not obscure focus; no canvas-only control (§3.1, §3.7) |
| Matrix | `DS-S-HIGH`, `DS-S-MEDIUM`, `DS-S-LOW`, `DS-S-SEMANTIC` | Evidence profiles; per-stream measurement; required modes; `exception_rule` (§1.1, §2.2, §2.3, §3.8) |
| Matrix | `SP-NAVIGATION`, `SP-WORLD`, `SP-FIRST-VISIT`, `SP-RETURN-VISIT` and the ten further public state profiles listed in §3.10 | Homes of the four stream frame states, per state, read from the matrix with `Import-Csv` (§3.10; `INS-07`) |
| Production | `EC-08` | `STREAM_*` evidence token (§1.1, §2.2) |
| Evidence model | `N-03`, `N-04`, `N-05`, `N-06`; §8.1 | Stream-generic minimum evidence; frame multiplier; control model; advisement surface; B01 evidence (§1.3, §3, §4.4, `INS-14`) |
| UX | `COV-ACT-09`, `ACT-09`, `ACT-11` | Action contract; alternate path; write-failure pattern (§3.8, §3.10) |
| UX test | `UXTEST-046` | Execution evidence for the control, the boundary crossing and process-state survival (§3, `INS-12`, `INS-14`) |
| Obligations | `OBL-INV-03`; `OBL-GRAM-01` to `OBL-GRAM-03`; `OBL-CTRL-01` to `OBL-CTRL-06`; `OBL-ADV-01`; `OBL-ANN-01`; `OBL-BND-01` to `OBL-BND-04`; `OBL-STATE-01` to `OBL-STATE-05`; `OBL-TRACE-02`, `OBL-TRACE-03` | As cited in §1 to §4 |
| Style guide | §4.1, §6.2, §7.2, §7.3, §8.2, §8.2.2, §8.2.3, §8.2.4, §8.2.5, §8.2.6 | Focus mandate; translucent panel; Escape binding; reduced-motion enumeration; stream table; precedence; thresholds; control model; separation of stream and canvas; process state |
| Freeze file | §1, §2.1 to §2.4, §3.1 to §3.3, §4, §5, §7, §8 | Layer rule, naming, taxonomy, states, obligations, prototype exclusion, handoff evidence (§5) |
| Proposed input | `packages/design-system/tokens.json`, `README.md` | Proposed 2D focus values and alias names; cited as proposed only (§4.2) |
| Risk and task | `R-039`; `TASKS.md` R-039 row | Exit evidence: this amendment plus a clean independent review record at a founder gate |

---

## 7. Unresolved gates and recorded assumptions

Marked rather than invented. A fact not establishable from the sources is a gate.

| ID | `[UNRESOLVED GATE]` | Owner | What waits on it |
|---|---|---|---|
| **UG-1** | The adjacency sampling method, adjacency definition and measurement procedure for the 3D focus ring against a lit, textured, animated scene (`OBL-CTRL-04` gate; `NFR-A11Y-005`). As written, "≥3:1 against every adjacent scene colour" can be neither passed nor failed. | Founder, on a proposal from the independent accessibility specification author under the D-044 pattern | Any measured claim for `semantic.focus.scene.ring`; the per-stream World focus frames of §4.4 |
| **UG-2** | Raw values for `semantic.focus.ring`, `semantic.focus.ring-width`, `semantic.focus.offset`, `semantic.focus.scene.ring` and `semantic.focus.scene.offset`. `tokens.json` offers proposed values; the identity source names cyan-on-ink for focus use; neither is authority. | Founder at the visual-direction gate (freeze §8 closing paragraph), after independent design and accessibility review | The value cells of the mapping ledger |
| **UG-3** | Exact public copy: the four stream `label` strings, the legend, Apply's name, the advisement, the above-ceiling reason, the write-failed and read-failed explanations, the same-shell announcement, the arrival announcement and the nearest-ancestor statement; and the visible order of the four radios, decided together with the labels because it is the most public peer-framing surface the control has. Provenance of the only order in the sources: the style guide §8.2 table (`S-HIGH`, `S-MEDIUM`, `S-LOW`, `S-SEMANTIC`), inherited from that accepted table and not derived from richness; assumption A-1 names it as provisional until decided. | Founder (public-copy gate; `NFR-A11Y-004`; freeze §7) | `--hd-stream-*-label` values; every announcement sentence; the radio order |
| **UG-4** | U-03 device-tier thresholds (§8.2.3). | Implementation-phase measurement; no schedule is offered | Nothing in this amendment; recorded because the `DS-S-*` descriptions reference tiers and a token must not carry one |
| **UG-5** | Whether Apply is ever `disabled` (for example when the pending selection equals the in-force stream) or always enabled with a no-op announcement. No source decides it; freeze §3.3 requires the state to be documented regardless. | Founder, on the independent accessibility reviewer's recommendation | Only the documented-but-unused pseudo-state |
| **UG-6** | Primary versus secondary action alias for Apply; hover and pressed pairings for radios and Apply (freeze §2.3: all interactive state pairings still to be decided). | Later visual-reference producer, then founder at the visual-direction gate | Component token values (§3.13) |
| **UG-7** | Whether the native radio input may be styled at all (accent, custom mark) without losing the platform-supplied forced-colors rendering that D-045 resolution 3 relies on. | Independent accessibility reviewer, then founder | Radio component token values |
| **UG-8** | Style guide §7.2 still binds `Escape` to "Close panel / go back" without excluding the control; `OBL-CTRL-04` forbids the control from binding `Escape`. The component rule is stated in §3.7; the §7.2 reconciliation is outside this file. | Style guide owner under the D-045 implementation record; founder | Nothing in this amendment |
| **UG-9** | The acceptance decision that re-opens `DESIGN_SYSTEM_IMPLICATIONS.md`, its revision label, and the new `design-system-freeze-hash` in the validator (D-046: a separate decision after independent review). | Founder | Application of §5 |
| **UG-10** | The storage notice's home and the `ACT-40` erasure of the accessibility choice (`OBL-STATE-04` gate). | Founder; UX architecture owner | Copy of `STATE-PREFERENCE-READ-FAILED`, not its token or state definition |
| **UG-11** | Freeze §1.1's platform-targets bullet still describes the WebGL layer and the Quick Access journey with pre-D-039 vocabulary, and freeze §2.4 and §4 keep a mode-axis context named in the same vocabulary beside the stream axis that `INS-05` and `INS-09` add. Rewording any of them is outside this commission (review 1, V-11). | Founder at acceptance | Nothing; noted so the applying slice does not treat it as covered |
| **UG-12** | Whether `NFR-A11Y` gains the 2.4.11 Focus Not Obscured row that `OBL-CTRL-04` and `OBL-TRACE-02` require, so that `semantic.focus.scene.layer` has a requirement-level home. | SRS owner under D-045; founder | Traceability only; the token rule stands on `OBL-CTRL-04` and `PRIM-043` |

Recorded assumptions (safe, reversible, unambiguous; each is a single line to
reverse):

- **A-1** Until the founder decides radio order under UG-3, reference work
  uses the style guide §8.2 table order (`S-HIGH`, `S-MEDIUM`, `S-LOW`,
  `S-SEMANTIC`) as the provisional order. Provenance: inherited from that
  accepted table, not derived from richness; the token export still must not
  sort by richness (§2.3). Reversal: adopt the order decided at UG-3.
- **A-2** The advisement is placed between the legend and the radios, read as
  context in the freeze §3.2 composite order, so that it precedes both the
  radios and Apply in reading and visual order; the sources fix only that it is
  inside the fieldset and precedes Apply (`OBL-ADV-01` point 1; `NFR-A11Y-004`;
  `PRIM-001`). The frozen text (`INS-08`) carries only the source-fixed
  constraints and cites A-2. Reversal: place it after the radios and before
  Apply.
- **A-3** The component's category segment is the freeze §3.1 taxonomy name of
  its authorized home (`Shell and navigation`), and the World hosts instantiate
  the same component rather than a second one.
- **A-4** In `S-SEMANTIC`, where no canvas and no HUD exist (`OBL-CTRL-05`;
  style guide §8.2.4), the mapping ledger resolves `semantic.focus.scene.*` to
  `semantic.focus.*`, so that no token is undefined in any stream and no export
  can emit a scene ring into a document without a canvas. No source states the
  resolution; it is the author's rule, safe and reversible, cited from §4.3,
  `INS-04` and `INS-09`. Reversal: record the scene tokens as not applicable in
  `S-SEMANTIC` and leave `semantic.focus.*` as the only ring there.

---

## Standing note

This document defines names, obligations and an application plan. It selects no
colour, size or duration value that a source does not state exactly; it claims
no conformance; it changes no hash-pinned file; and it authorizes no external
call. Its exit evidence, per `R-039` and D-046, is this amendment together with a
clean independent review record against `OBL-GRAM-03` — three hits: the
per-stream contrast rule, the stream-control component, and the focus-ring
tokens — presented at a founder gate before the freeze file changes.

---

## Revision history

Revision 2 (2026-09-24) addresses independent review 1
(`reviews/design-system-amendment-r-039-review-1.md`, commit `740864b`, subject
revision `2c469b6`): Part A PASS, Part B FAIL on DSA-01 (MEDIUM), DSA-02 to
DSA-09 LOW. One row per finding. Line numbers refer to this revision. No
finding was declined. The matrix facts under DSA-01 were read with
`Import-Csv` over all 36 rows of `responsive-state-mode-matrix.csv`, never
assumed. Only this file changed; the frozen files, the validator and the review
record were not touched.

| Finding | Disposition | Change made (line in this revision) or reason |
|---|---|---|
| **DSA-01** (MEDIUM) | Resolved | §3.10 preamble replaced: the matrix is named as the authority and the distribution is restated per state, exactly as its `required_values` and `critical_distinct_frame_values` columns record it, in a new table (lines 539 to 560): `STATE-STREAM-CHANGED` and `STATE-PREFERENCE-WRITE-FAILED` on fourteen public state profiles including all four that `OBL-STATE-01` names; `STATE-PREFERENCE-READ-FAILED` on `SP-NAVIGATION`, `SP-FIRST-VISIT` and `SP-RETURN-VISIT` only, not `SP-WORLD`; `STATE-STREAM-CEILING-REFUSED` on `SP-NAVIGATION` and `SP-WORLD` only, not `SP-FIRST-VISIT` and not `SP-RETURN-VISIT`; all four as `critical_distinct_frame_values` of the four `DS-S-*` rows; the five staff profiles carry none (557). The §3.10 state rows now carry their homes, with `SP-RETURN-VISIT` as the on-return home of `STATE-PREFERENCE-READ-FAILED` (568). Block `INS-07` rewritten with the same per-state distribution and the matrix cited as the authority, so the frozen text cannot contradict the frozen matrix (888). §6 matrix row corrected (1085); Inputs updated (31). |
| DSA-02 (LOW) | Resolved | "five properties each" corrected to "six" in §0 row 2 (94). |
| DSA-03 (LOW) | Resolved | The clause "never animated across the viewport" removed from the `semantic.focus.scene.motion` rule and moved to the source column, marked as occurring only in the [PROPOSED] `tokens.json` and `README.md` input, never authority (730). |
| DSA-04 (LOW) | Resolved | Assumption A-4 recorded in §7 with the resolution rule, its reasoning and a one-line reversal (1135); cited from §4.3 (750), from the `INS-04` scene row (853) and from the `INS-09` fourth bullet (988). |
| DSA-05 (LOW) | Resolved | `INS-08` anatomy bullet restated so the frozen text carries only the source-fixed constraints (inside the fieldset; before Apply in DOM reading order and visual order) and cites A-2 for the placement relative to the radios (920). §3.2 anatomy list restated in `PRIM-001`'s own order (339) and its composite-order paragraph corrected: the "advisement as context" reading is now stated as part of A-2 rather than as a source fact (354). A-2 rewritten with its sources and reversal (1125). |
| DSA-06 (LOW) | Resolved | `INS-06` row now points to an anchor block (796); the two rows are quoted verbatim in that block (868); each verified by literal grep to occur exactly once in the freeze file (`\| Shell and navigation \| ... \|` count 1; `\| Overlay and immersive \| ... \|` count 1). |
| DSA-07 (LOW) | Resolved | Both the reviewer's and the coordinator's forms applied: provenance stated (the only order in the sources is the style guide §8.2 table, inherited from that accepted table and not derived from richness) and radio order moved under UG-3, to be decided with the four labels (1106); A-1 kept as the provisional order with provenance and reversal (1120); §3.2 states that no source fixes the order (371). |
| DSA-08 (LOW) | Resolved | "transition" removed from the gated list; transition durations cited as the accepted freeze §2.2 ranges (`motion.stateTransition` 120–200 ms, `motion.contextShift` 240–400 ms, `motion.signalReveal` 180–320 ms) with their reduced-motion branches (287). |
| DSA-09 (LOW) | Resolved | `INS-10` now reads "per rendered state and per stream", so the hint `search "per stream"` matches the inserted text literally (995). |
| V-11 (reviewer note, not a finding) | Adopted | UG-11 extended to cover the freeze §2.4 and §4 mode-axis wording that `INS-05` and `INS-09` sit beside (1114). |
| Header | — | Date line bumped to "Revision 2, 2026-09-24" (17); the review record and the `Import-Csv` matrix read added to Inputs (31, 50). |
| **Revision 3 (application, 2026-09-24)** | Applied | Applying slice under UG-9 after acceptance at D-047 (2026-09-24) of revision 2 (commit cf455db9d0fc5fc285ea2153d3d924f1d7afa332; SHA-256 61b924951ff955faa16ae067ba9baf2e0a0f7987f91df5f907f42cda4fe0e9ea). DSB-01 (LOW): §3.2 heading retitled "Anatomy, in `PRIM-001` record order, and the order constraints" (337); the list and the constraint sentence are unchanged. DSB-02 (LOW): the first option of review 2 taken; the applied `INS-01` line in `DESIGN_SYSTEM_IMPLICATIONS.md` fills the two `[GATED]` placeholders (2026-09-24; D-047) and pins the accepted revision by commit and SHA-256, so the A-2 and A-4 citations applied by `INS-04`, `INS-08` and `INS-09` resolve to that pinned revision; `INS-02` to `INS-14` applied as written. The pin names revision 2 as committed; this revision changes only the §3.2 heading and this row. |
