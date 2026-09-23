# Delivery Stream Accessibility Obligations — **[PROPOSED SPECIFICATION]**

**Status: [PROPOSED SPECIFICATION]. Pending founder decision. Not accepted
authority. Not a contract, not a validator rule, not an amendment to any accepted
artifact.**

**Author:** independent accessibility specification author. Not the producer of
the CR-002 package. Written under **D-044**, which places the delivery-stream
evidence model with reviewers rather than with the producer after four
consecutive producer remediations failed independent review.

**Date:** 2026-09-06
**Basis:** blocking findings **B-01** … **B-05** of
`docs/phase-1-ui-reference-design/accessibility/accessibility-audit-iteration-4.md`,
converted from negative findings into positive, testable obligations.
**Conformance target these obligations serve:** WCAG 2.2 Level AA for every
applicable full page and every complete process, including represented
third-party steps, holding **independently within each of the four peer delivery
streams**.

> **No conformance is claimed here, present or future.** Nothing is built. Every
> obligation below is a requirement on a *specification and evidence package*,
> not an assertion that any success criterion is met. Success criteria are
> evaluated against an implementation, never against this document.

**Vocabulary discipline.** `S-HIGH`, `S-MEDIUM`, `S-LOW` and `S-SEMANTIC` are
four **peer** streams carrying equivalent core journeys. `S-SEMANTIC` is P0, is
never a fallback, never an error surface, and never a destination for
"unsupported" clients. `S-LOW` reduces fidelity only and retains every hotspot
and every destination. WebGL capability is a hard ceiling. No failure and no
measurement promotes or demotes a stream mid-session; the only mid-session change
is the visitor operating the delivery stream control (§8.2.2 step 5).

**Reading key.** Each obligation carries: **ID**, **SC at stake**, **human
consequence if unmet**, **record or artifact that must carry it**, **reviewer
test**. `[UNRESOLVED GATE]` marks a fact this author cannot establish and
declines to invent. Device-tier thresholds are **U-03**, deferred to
implementation-phase measurement, and are not set anywhere in this document.

**Frame economy.** Evidence frames cost metered external design calls from a
20-per-month allowance. Every obligation that requires a *distinct* frame states
why annotation, prose, a prototype note, or an existing frame will not discharge
it. Where cheaper evidence suffices, this document says so explicitly and
requires no frame.

---

## Part 0 — The question B-01 asks directly

### Can any stream-invariance concept survive without becoming an exemption?

**Yes, but only in a form that is currently selectable by no record in the
package, and only if it is inverted from a claim into a derived conclusion.**

`DS-STREAM-INVARIANT` as written fails for a structural reason, not a drafting
one: it is a **producer-asserted** property whose truth condition ("renders
identically in all four streams") is not checkable from the record, while its
effect (one frame set discharges four streams) is immediate and total. Any
profile with that shape is an exemption regardless of its wording, because the
cheapest true-looking assertion always wins and no reviewer can falsify it from
the ledger. This is the same shape as the iteration-4 standing lesson: *a rule
stated in prose, a proxy asserted in code, and the gap between them holding the
defect.*

Invariance survives only if it becomes a **machine-derived conclusion with no
producer discretion**, under **OBL-INV-01** below. On the package's current data
the derived condition is true for **zero of 34 routes** and **zero of 19 route
templates**, which is the correct answer and the one the audit already
demonstrated three ways.

### OBL-INV-01 — invariance is derived, never declared

**SC at stake:** 1.4.3, 1.4.11, 2.4.3, 2.4.7, 2.5.8, 1.3.1, 1.3.2 (each measured
per stream).

**Obligation.** A record may be treated as stream-invariant if and only if **all**
of the following are computable as true from the record's own accepted columns.
No column may be a free-text producer assertion.

1. `immersive_stream_representation` is **empty** on that record.
2. The record depends on **no primitive that declares per-stream variants** —
   i.e. no primitive in its `reference_templates_or_flows` / primitive
   dependency set whose `required_variants` contains any of `stream_high`,
   `stream_medium`, `stream_low`, `stream_semantic`. `PRIM-001` declares all
   four, so every record depending on the Public semantic shell is excluded.
3. The record's `mode_profile` does **not** require a distinct
   `MODE-SEMANTIC-SHELL` frame. `MP-PUBLIC` and `MP-INTERACTIVE` both do, so
   every record carrying either is excluded.
4. The record's `state_profile` required values contain **no** state whose
   meaning is stream-relative (`STATE-STREAM-CHANGED`,
   `STATE-PREFERENCE-WRITE-FAILED`, `STATE-PREFERENCE-READ-FAILED`,
   `STATE-STREAM-CEILING-REFUSED`).

Any record failing any of 1–4 **must** select all four `DS-S-*` profiles. There
is no third option and no "not applicable" for `S-SEMANTIC` anywhere, ever.

**Record that must carry it.** `responsive-state-mode-matrix.csv` —
`DS-STREAM-INVARIANT.exception_rule` restated as the four derived conditions;
`UI_REFERENCE_DESIGN_CONTRACT.md` §9 restated identically; and the validator
assertion `delivery-stream-assignment` rewritten to compute conditions 1–4
instead of proxying on a five-value `state_profile` list.

**Human consequence if unmet.** A visitor whose client returns no WebGL context —
an older Android handset, a locked-down enterprise browser, a GPU-blocklisted
machine — uses `S-SEMANTIC` for all 34 routes and for the entire booking lineage,
and not one route row, template row, or booking / contact / AI-concierge /
human-handoff / media-opt-in flow row requires a single frame drawn in the stream
they will actually use. Their contrast, focus order, target sizes, and ability to
complete a booking end to end are discharged by pictures of a stream they will
never see.

**Reviewer test.** Recompute conditions 1–4 over
`foundation-route-coverage.csv`, `reference-template-inventory.csv` and
`foundation-flow-coverage.csv`. Every record for which the conjunction is false
must carry all four `DS-S-*`. The count of records carrying
`DS-STREAM-INVARIANT` must equal the count for which the conjunction is true. If
the validator can be satisfied by a record that fails any of 1–4, the assertion
is still a proxy and the finding recurs.

**Frame cost.** Zero. This is a schema and validator obligation; it consumes no
external design call.

### OBL-INV-02 — `S-SEMANTIC` evidence must attach to routes, templates, and complete processes by name

**SC at stake:** the per-stream target as a whole; `NFR-A11Y-001`, `-002`, `-003`.

**Obligation.** `DS-S-SEMANTIC`'s obligations — per-stream contrast, per-stream
focus order, per-stream target size, forced-colors and print captures, and
**every core journey completed end to end using only this stream** — must attach
to named records, not to a stream axis in the abstract. Minimum attachment set:

- **all 34 rows** of `foundation-route-coverage.csv` (every one declares a
  distinct immersive representation and therefore fails OBL-INV-01 condition 1);
- **all 19 route templates** in `reference-template-inventory.csv` (all depend on
  `PRIM-001`, which declares four per-stream variants, failing condition 2);
- **every flow row covering a complete process**: booking, contact, AI concierge,
  human handoff, media opt-in. These are the "complete processes" the conformance
  target names, so an `S-SEMANTIC` end-to-end obligation that skips them does not
  address the target at all.

**End-to-end means end to end.** For each complete process, the `S-SEMANTIC`
obligation is discharged only by evidence covering **every step from entry to
confirmation, including represented third-party steps**, in `S-SEMANTIC`. A frame
of the first step does not discharge the process. Where a step is represented by
a third party, the record must name that step and state that the same target
applies to it. `[UNRESOLVED GATE]` — which third-party steps are in the booking
lineage, and under what contractual leverage their accessibility can be
evidenced, is not established in the package; this must be resolved before the
process obligation can be called satisfiable.

**Record that must carry it.** The three coverage CSVs above, via `stream_profile`
= all four `DS-S-*`; and `traceability.csv` rows per **OBL-TRACE-01**.

**Human consequence if unmet.** As OBL-INV-01. Additionally: a producer can
satisfy every ledger cell, pass a clean validator run, and produce zero
`S-SEMANTIC` evidence for any page or any process — which is exactly what the
current package permits.

**Reviewer test.** For each of booking, contact, AI concierge, human handoff and
media opt-in, name the record that requires `S-SEMANTIC` end-to-end evidence and
the evidence IDs that will discharge it. If the answer for any one of them is "no
record", the obligation is unmet.

**Frame cost.** Deferred to the route and flow batches (B02 onward), not B01.
This document does not budget them; it requires that they be budgeted before
those batches are authorized, because the allowance makes an unbudgeted per-route
`S-SEMANTIC` obligation undeliverable by arithmetic rather than by intent.

### OBL-INV-03 — aggregate evidence can never discharge a per-stream obligation

**SC at stake:** 1.4.3, 1.4.11, 2.5.8, 2.4.3, 2.4.7.

**Obligation.** No frame that does not name a stream may discharge a `DS-S-*`
obligation. The reason is physical, not procedural: contrast, focus-indicator
contrast, target geometry and focus order are properties of a **rendering**, and
the four streams render differently by construction. A translucent
`bg-gray-900/95 backdrop-blur` panel (§6.2) over a high-texture lit 3D scene has
a different measured contrast ratio from the same panel over a low-texture
unshadowed scene, and a different one again from the same content as a standalone
semantic document with no canvas behind it. `NFR-A11Y-005`'s focus indicator at
"≥3:1 against every adjacent scene colour" differs per stream **by construction**
— the adjacent scene colours are not the same colours.

An aggregate frame therefore does not under-evidence the other three streams; it
evidences **none** of them, because it depicts a rendering that no visitor
receives.

**Record that must carry it.** All four `DS-S-*.annotation_requirements` (already
present in words: "never inherited from another stream"), plus an
`EC-*` rule that makes it checkable per **OBL-GRAM-02**.

**Reviewer test.** Take any `DS-S-*` obligation and ask which evidence ID
discharges it. If the answer is an evidence ID whose stream token is absent or
whose stream token names a different stream, the obligation is undischarged.

**Frame cost.** Zero directly. This obligation is the reason the frame counts in
Part 6 cannot be reduced by sharing.

---

## Part 1 — What the accessibility evidence chain requires of the evidence-ID grammar (B-02)

A separate technical-architecture author is specifying the mechanism. The
following are the accessibility **requirements** on it, not a proposed
implementation.

### OBL-GRAM-01 — the evidence-ID grammar must carry a stream token

**SC at stake:** the per-stream target; `NFR-A11Y-002`.

**Obligation.** `EC-08`'s grammar
`HSD_UIR_<BATCH>_<TEMPLATE>_<INSTANCE>_<STATE>_<VIEWPORT>_<MODE>_V<NN>` must gain
a `<STREAM>` position. Accessibility requirements on it:

1. **Mandatory, not optional.** Every evidence ID carries a stream token. There
   is no "unspecified" value. A record that is genuinely invariant under
   OBL-INV-01 carries an explicit token denoting *all four* — it does not carry a
   blank, because a blank is indistinguishable from an omission.
2. **Four peer values plus the derived-invariant value, and no fifth.** No token
   may encode "fallback", "degraded", "non-WebGL", "unsupported", "optional", or
   "quality". A token vocabulary is a naming surface and inherits the D-039
   vocabulary prohibition.
3. **Distinguishing, not decorative.** Four frames of the same template,
   instance, state, viewport and mode in four different streams must produce four
   **distinct** IDs. The grammar fails this requirement if any two of those four
   collide.
4. **Positionally unambiguous with `<MODE>`.** `MODE-SEMANTIC-SHELL` and stream
   `S-SEMANTIC` are different axes with a confusable name. The grammar must make
   a parse of a filename unambiguous as to which axis a token belongs to.
   (Note the live instance of exactly this hazard:
   `..._MODE_NON_WEBGL_QUICK_ACCESS_V01`, still present in
   `reference-template-inventory.csv`, evades the D-043 hyphen-scoped guard
   because frame names use underscores.)

**Record that must carry it.** `docs/phase-1-ui-reference-production/evidence-capture-plan.csv`
(`EC-08`), and the manifest schema it validates.

**Human consequence if unmet.** The one piece of evidence R-036's mitigation
rests on — ACT-09 proven in four streams on an authorized batch — is produced
under a grammar that cannot record which stream it shows. A reviewer looking at
four frames cannot tell which is `S-SEMANTIC`, so a screen-reader user's stream
is evidenced only by the producer's say-so.

**Reviewer test.** Construct the four B01 current-value evidence IDs by hand from
the grammar. If they are not four distinct strings, the grammar fails.

### OBL-GRAM-02 — a validator rule must check the stream token against required values

**SC at stake:** the per-stream target; verifiability of `NFR-A11Y-002`.

**Obligation.** A `stream_id` field must exist in the manifest and an `EC-*` rule
must check it against the assigned profile's `required_values`, in exactly the
way `EC-10` checks `viewport_id` and `EC-11` checks `mode_id`. Additionally:

- The rule must fail a record that carries all four `DS-S-*` and produces frames
  in fewer than four streams for a `critical_distinct_frame_value`.
- The rule must fail a record that carries `DS-STREAM-INVARIANT` while OBL-INV-01
  conditions 1–4 do not hold.
- Where the stream axis is genuinely deferred for a batch, it must be marked
  deferred **explicitly**, in the way `EC-14` already marks
  `deferred_B07;deferred_B09`. Silence is not deferral.

**Record that must carry it.** `evidence-capture-plan.csv`;
`validate-ui-reference-production.ps1`.

**Human consequence if unmet.** The stream axis is asserted upstream and inert
downstream — the D-042 defect, one layer lower. Metered external calls are spent
on frames whose stream cannot be validated, and the absence of `S-SEMANTIC`
frames is invisible to a clean run.

**Reviewer test.** Delete the `S-SEMANTIC` frame from a record carrying all four
`DS-S-*` and rerun the validator. If it still passes, the rule does not exist.

### OBL-GRAM-03 — the stream axis must reach the design-system handoff artifact

**SC at stake:** 1.4.3, 1.4.11, 2.4.7 at implementation time.

**Obligation.** `DESIGN_SYSTEM_IMPLICATIONS.md` — hash-pinned, specialist-owned,
and the artifact implementation actually inherits — currently says "Contrast is
checked per rendered state" and never "per stream", defines no delivery-stream
control component, and defines no tokens for the four stream values or for the 3D
focus ring §4.1 now mandates. The accessibility chain requires that these three
gaps be closed **in whichever slice re-opens that document**.

`[UNRESOLVED GATE]` — that document is read-only inside the design package and
this author cannot establish which slice may amend it. The obligation stands; its
owner does not.

**Reviewer test.** Search the handoff artifact for a per-stream contrast rule, a
stream-control component, and focus-ring tokens. Three hits required.

---

## Part 2 — The delivery stream control (B-04)

### OBL-CTRL-01 — role and activation model, specified normatively

**SC at stake:** 3.2.2 On Input, 4.1.2 Name Role Value, 2.1.1 Keyboard.

This is the single decision that determines whether 3.2.2 can be met, and it has
been left open through four remediations. It is made here.

**Normative role.** The delivery stream control is a **grouped set of four native
radio inputs** (`input[type="radio"]`, one per stream, sharing a name), wrapped in
a **`fieldset` with a `legend`** — i.e. an implicit `radiogroup` with an
accessible name from the legend — **plus a separate, always-present submit
button** that applies the selection.

**Normative activation model: two-step, explicit confirmation.**

1. Moving among the radios — by arrow key, by `Tab` into the group, by pointer,
   or by touch — changes only which radio is *checked*. It **must not** apply a
   stream, must not reload, must not alter the accessibility tree beyond the
   checked state, and must not initiate any transition.
2. A stream is applied **only** by explicit activation of the submit button
   (`Enter` or `Space` on the button, or pointer/touch activation), or by `Enter`
   pressed within the group where that is the platform's native form-submission
   behaviour for the same button.
3. Until the button is activated, the control's reported **current stream** is the
   stream in force, not the stream tentatively checked. These are two distinct
   pieces of information and both must be programmatically available
   (**OBL-CTRL-02**).

**Prohibited, normatively.** A native `select` whose `change` event applies the
stream; any listbox, combobox, menu, or radio group that applies on selection,
on `blur`, on arrow-key movement, or after a timeout; any control that applies on
first interaction of any kind. In several browser and platform combinations,
arrowing through a `select`'s options changes its value — the textbook 3.2.2
failure — and `aria-describedby` on a `select` is not reliably announced by
several common screen reader / browser pairings, so a description-only advisement
does not rescue it.

**Why radios plus submit rather than listbox plus Apply.** Both are two-step. The
radio form is chosen because it is native: role, checked state, group name, group
membership, arrow-key semantics and forced-colors rendering are all supplied by
the platform rather than authored, which removes four independent opportunities
for a 4.1.2 defect and makes the forced-colors obligation (OBL-CTRL-06)
achievable without custom high-contrast handling.

**Record that must carry it.** `3D_Mega_Menu_Style_Guide_v2.md` §8.2.4 (as the
behavioural home); `component-primitives.csv` `PRIM-001` (anatomy: the control's
role and its submit affordance must appear as named anatomy, not as the single
token `delivery stream control`), and `PRIM-042`, `PRIM-043`, `PRIM-044`
identically; `Hengshi_Design_SRS_v3.md` `FR-3D-014` and `NFR-A11Y-004`.

**Human consequence if unmet.** A keyboard user arrows down the control to read
what the options are and the page reloads into `S-SEMANTIC` — or into `S-HIGH`,
launching a camera flight — without warning and without their having chosen
anything. A screen-reader user browsing the utility navigation loses their place
mid-session. A visitor with a motor impairment who overshoots by one arrow press
has changed the entire delivery of the site.

**Reviewer test.** Read the record. It must name a role and state, in words that
admit no second reading, that moving among options does not apply a stream and
that a separate explicit activation does. If the words "select", "on change", or
"applies the selected stream" appear without an explicit confirmation step, the
obligation is unmet.

**Frame cost.** Zero. Role and activation model are specification text; a picture
cannot establish them. This is stated so no producer spends a metered call trying.

### OBL-CTRL-02 — accessible name, current value, and pending value

**SC at stake:** 4.1.2 Name Role Value, 1.3.1 Info and Relationships.

**Obligation.**

- The **group** has an accessible name that identifies it as the delivery stream
  control and **reports the stream currently in force**, so the active stream is
  available without inspecting the scene (§8.2.4 already requires this; it is
  restated here as a name obligation on a named role).
- Each **radio** has an accessible name identifying its stream in the D-039 peer
  vocabulary. No option label may contain "fallback", "degraded", "low quality",
  "basic", "optional", "reduced", "unsupported", or "non-WebGL". `S-SEMANTIC`'s
  label must read as a peer choice a visitor might prefer, not as a lesser one.
- The **submit button** has an accessible name that states it applies the
  selection, distinct from the group name and from any radio name.
- **Current** and **pending** are distinguishable programmatically: the checked
  radio is the pending value; the group name carries the in-force value. A
  visitor must never have to infer which is which.
- Where a stream is above the WebGL ceiling and therefore unreachable, its radio
  is present and its unavailability is conveyed **in text**, not by colour or
  dimming alone (`state_redundancy`: "visible text plus shape icon border pattern
  or position; never color only").

**Record that must carry it.** `PRIM-001` (`transactional_or_content_states` must
gain the current/pending distinction), §8.2.4, `NFR-A11Y-004`.

**Human consequence if unmet.** A screen-reader user hears four options and no
indication of which one they are currently in, applies the one they are already
using, and triggers a full re-entry for nothing — or believes they switched when
they did not.

**Reviewer test.** From the record alone, state what a screen reader announces on
entering the group, on arrowing to the second option, and on reaching the submit
button. If any of the three cannot be answered, the obligation is unmet.

### OBL-CTRL-03 — discoverability and presence in every stream, especially `S-SEMANTIC`

**SC at stake:** 3.2.3 Consistent Navigation, 3.2.4 Consistent Identification,
2.4.1 Bypass Blocks, 1.3.1.

**Obligation.**

- The control is present on **every** route in **every** stream. In `S-SEMANTIC`
  it lives in `PRIM-001`'s utility navigation — not in the World HUD, which does
  not exist there — and is reachable **without a canvas**.
- It is reachable **without traversing main content**: within the navigation
  landmark structure, on the skip-link path, and in the same relative position on
  every route (3.2.3), under the same accessible name on every route (3.2.4).
- Where narrow viewports collapse utility navigation into a disclosure, the
  control's reachability must be evidenced at `VP-320` **in `S-SEMANTIC`**
  specifically: this is the stream where the control has no HUD home and the
  narrow-viewport disclosure is the only path to it.
- It is **not** canvas-only in any stream (`PRIM-043` already forbids canvas-only
  controls; this extends that to the stream control by name).

**Record that must carry it.** `PRIM-001.required_anatomy` and
`responsive_and_mode_obligations`; `B01.required_visual_evidence`.

**Human consequence if unmet.** A visitor on a 320 px viewport in `S-SEMANTIC` —
the exact profile of the older-Android, no-WebGL visitor this amendment exists
for — cannot find the control that would let them try a richer stream, and is
silently locked into the stream a probe chose for them, with no evidence anyone
ever checked.

**Reviewer test.** Name the evidence ID that shows the control reachable at
`VP-320` in `S-SEMANTIC`. If none exists, unmet.

**Frame cost: 1 distinct frame** (`VP-320`, `S-SEMANTIC`, control revealed
through the narrow-viewport disclosure). A desktop frame will not do, because the
disclosure path does not exist at desktop width; an annotation will not do,
because the obligation is about rendered reachability, not about intent.

### OBL-CTRL-04 — keyboard operability and focus behaviour

**SC at stake:** 2.1.1 Keyboard, 2.1.2 No Keyboard Trap, 2.4.3 Focus Order,
2.4.7 Focus Visible, 2.4.11 Focus Not Obscured (Minimum), 2.5.8 Target Size.

**Obligation.**

- Fully operable by keyboard in every stream, with native radio-group semantics
  (one tab stop into the group; arrows move among radios; the submit button is a
  separate tab stop).
- **2.4.11** — in the 3D streams the control sits in a persistent HUD over a
  canvas. When any part of the control has focus, no sticky or overlay element may
  entirely hide it. `PRIM-043` already requires the HUD not to obscure focus;
  this binds it to the stream control by name. `NFR-A11Y` currently carries no
  2.4.11 row and must gain one (**OBL-TRACE-02**).
- **2.4.7** — the focus indicator on each radio and on the submit button meets the
  focus-indicator obligation **in each stream's own rendering**. In the 3D streams
  the adjacent colours are scene colours and vary; see the sampling gate below.
- **2.5.8** — target size for each radio and its label, and for the submit
  button, measured in each stream's own rendering.
- `Escape` must not be bound to dismissing or cancelling the control in the World
  streams, because §7.2 already binds `Escape` to "Close panel / go back". A
  visitor pressing `Escape` to back out of the control must not navigate.

`[UNRESOLVED GATE]` — `NFR-A11Y-005` requires the focus indicator at "≥3:1
against every adjacent scene colour". Against a lit, textured, animated 3D scene
this has **no sampling method, no adjacency definition, and no measurement
procedure**, so as written it can be neither passed nor failed. A sampling method
must be specified before any 3D-stream focus obligation is testable. This author
does not invent one.

**Record that must carry it.** `PRIM-001`, `PRIM-043`;
`3D_Mega_Menu_Style_Guide_v2.md` §7.2 (the `Escape` conflict) and §4.1;
`NFR-A11Y-005` plus a new 2.4.11 row.

**Human consequence if unmet.** A keyboard user in the World tabs to the stream
control, the focus ring lands behind the HUD's own translucent panel, and they
cannot see where they are; they press `Escape` to get out and are navigated
backwards out of the room instead.

**Reviewer test.** For each stream, name the frame that shows the control focused
with a visible indicator and nothing obscuring it. For `Escape`, read §7.2 and
§8.2.4 together and state what happens; if the two documents do not agree, unmet.

### OBL-CTRL-05 — `S-SEMANTIC`-specific obligations on the control

**SC at stake:** 1.3.1, 1.4.10 Reflow, 2.5.8, 3.2.3, 4.1.2.

**Obligation.** In `S-SEMANTIC` the control must additionally:

- be present with **no canvas anywhere in the document**, so no obligation on it
  may be discharged by a frame that contains one;
- offer the three 3D streams as **live, selectable options** whenever the WebGL
  ceiling permits — `S-SEMANTIC` is a peer stream a visitor may be *in by choice*,
  and a control that only offers "stay here" reinstates the fallback framing;
- when the WebGL ceiling makes the 3D streams unreachable, state that in text as
  a **fact about the client**, never as a failure, an error, or a recovery
  ("this device cannot obtain a WebGL context"), with no failure heading, no error
  styling, and no language of escape, recovery, or fallback
  (`DS-S-SEMANTIC.exception_rule`);
- survive forced colors with its current value and its checked state still
  distinguishable (**OBL-CTRL-06**).

**Record that must carry it.** `PRIM-001` variants `stream_semantic`;
`DS-S-SEMANTIC.minimum_evidence`.

**Human consequence if unmet.** The no-WebGL visitor is told, in the one surface
built for them, that they are on an error page — which is the framing D-039
removed and the reason CR-002 exists.

**Reviewer test.** Read the `S-SEMANTIC` control copy. If any word in it would be
out of place on a page the visitor chose deliberately, unmet.

### OBL-CTRL-06 — forced colors

**SC at stake:** 1.4.1 Use of Color, 1.4.11 Non-text Contrast, 1.4.3.

**Obligation.** In `MODE-FORCED-COLORS`, the checked radio, the in-force stream,
the focus indicator, and any unavailable-option state must all remain
distinguishable without relying on authored colour. `DS-S-SEMANTIC` already
requires forced-colors captures; this binds one of them to the control.

**Human consequence if unmet.** A Windows High Contrast user cannot tell which
stream they are in or which option they have checked, and applies the wrong one.

**Reviewer test.** Name the forced-colors evidence ID for the control in
`S-SEMANTIC`.

**Frame cost: 1 distinct frame.** Forced colors is a rendering substitution, not
an annotation; a standard-mode frame with a note cannot show what the platform
substitutes. It must be `S-SEMANTIC` because that is the stream where the control
carries the full burden alone, without a HUD.

---

## Part 3 — Advance advisement (3.2.2) and change announcement (4.1.3) are two mechanisms (B-04)

These are routinely conflated. They have different timing, different audiences,
different surfaces, and different evidence, and one cannot substitute for the
other.

| | Advance advisement | Change announcement |
|---|---|---|
| SC | **3.2.2 On Input** | **4.1.3 Status Messages** |
| Timing | **Before** the control is operated | **After** the change has occurred |
| Audience | **Every user class**, including sighted non-AT keyboard and mouse users | Users who are not looking at the change; delivered without moving focus |
| Surface | Persistent **visible text**, programmatically associated | Status region, polite |
| Fails if | Only in the accessibility tree | Announced by moving focus, or region injected with its message |

### OBL-ADV-01 — the advisement must be visible text, not only an accessible description

**SC at stake:** 3.2.2 On Input.

**Obligation.** The advance advisement — that choosing a stream re-enters the
experience in that stream and keeps the current location — must be:

1. **Rendered as persistent visible text** within the control's group, positioned
   so that it precedes the submit button in reading order and in visual order;
2. **Programmatically associated** with both the radio group and the submit
   button, so it is conveyed to assistive technology as well;
3. **Not** delivered by tooltip, title attribute, hover-only, or focus-only
   disclosure. A hover- or focus-triggered advisement is additional content on
   hover/focus and drags in **1.4.13** (dismissible, hoverable, persistent) —
   whose dismissal key, `Escape`, is already bound by §7.2 to "Close panel / go
   back". Persistent visible text avoids the conflict entirely;
4. **Present in every stream**, in the same words.

An accessible description **alone** is insufficient and must not be the stated
requirement. It reaches only users running an AT that surfaces descriptions for
that role; a sighted keyboard user and a sighted mouse user receive nothing, and
3.2.2's advisement must reach the user who is about to operate the control.
`NFR-A11Y-004` ("advises before it acts") inherits this and must be amended to
say *how*.

**Record that must carry it.** `3D_Mega_Menu_Style_Guide_v2.md` §8.2.4 (replacing
"its accessible description says…"); `PRIM-001.required_anatomy`;
`NFR-A11Y-004`; `B01.required_visual_evidence`.

**Human consequence if unmet.** A sighted keyboard user, no AT running, tabs into
the group, arrows to read the options, hits the button expecting a menu, and the
entire site re-enters in a different stream — losing their place — with no
warning they could have received. This is the precise failure the withdrawn
"3.2.2 satisfied by construction" claim pretended was impossible.

**Reviewer test.** For each of four user classes — sighted mouse, sighted
keyboard without AT, screen-reader user, screen-magnifier user at 400% zoom —
state where the advisement comes from and whether it arrives before operation.
Four answers required, and none of them may be "the accessible description" alone.

**Frame cost: 1 distinct frame** — the control in `focus-visible` with the
advisement text rendered in place, at `VP-DESKTOP`, `S-SEMANTIC`. Distinct
because it must simultaneously show (a) the visible advisement, (b) its position
relative to the submit button, and (c) a visible focus indicator on the control
(2.4.7) with nothing obscuring it (2.4.11). No resting-state frame shows the
focus indicator, and no annotation shows rendered placement.

### OBL-ANN-01 — the change announcement, and the empty-region-first rule

**SC at stake:** 4.1.3 Status Messages.

**Obligation.**

1. The change is announced through a **polite** status region. It does not
   interrupt and it does not move focus **within the same shell**. (Across the
   semantic boundary, focus does move — see OBL-BND-01; the two rules are not in
   conflict and the SRS must be corrected to say so, per **OBL-TRACE-03**.)
2. **The status region that carries the announcement must be identified by
   name**, and must **already exist in the accessibility tree, empty**, before
   the message is written into it. A live region inserted into the DOM together
   with its message is routinely not announced. Across the semantic boundary this
   is the whole difficulty: §8.2.4 requires the outgoing shell to leave the tree
   before the incoming one enters, so the announcing region must be the
   **incoming** shell's region, present and empty first, with the message written
   afterwards as a separate step.
3. The announcement states the **new stream** and the **arrival location** — see
   OBL-BND-02. Announcing only that the stream changed leaves the visitor knowing
   what happened and not where they are.

**Record that must carry it.** §8.2.4; `PRIM-001` (`page status region` is
already named anatomy — it must be stated as the carrier and as
present-and-empty-first); `SP-NAVIGATION` per **OBL-STATE-01**.

**Human consequence if unmet.** A screen-reader user selects `S-SEMANTIC`, the
old shell is destroyed, the new one arrives with its live region and message
inserted together, nothing is announced, and the user is silently somewhere else.

**Reviewer test.** Name the region, and state the ordering of the three steps
(outgoing removed; incoming region present and empty; message written). If the
record does not order them, unmet.

---

## Part 4 — The `S-SEMANTIC` boundary crossing (B-03, S-01)

This is the hardest case in the amendment and the one the current package
requires no one to draw, annotate, or review.

### OBL-BND-01 — focus destination when the operated control's subtree is destroyed

**SC at stake:** 2.4.3 Focus Order, 2.4.7 Focus Visible, 3.2.3, 3.2.4.

**Obligation.**

- Focus moves to the **delivery stream control in the destination shell** — the
  same control by role and accessible name, reporting the new stream as in force.
  §8.2.4 already names this destination; this obligation adds what makes it
  testable.
- Focus must be **visibly indicated** on arrival. Programmatic focus that is not
  visibly indicated fails 2.4.7 for the sighted keyboard user; §4.1's focus rule
  covers hotspots only and does not reach the destination control.
- Focus is set **after** the incoming shell is in the accessibility tree and
  **after** its status region exists, never before.
- Focus is never dropped to the document body and never left on a destroyed node.
- The destination control is the same by role and name in both directions
  (3.2.4), and in the same relative position within its shell (3.2.3).

**Record that must carry it.** §8.2.4 (already partly); a new
`SP-NAVIGATION` state per OBL-STATE-01; `NFR-A11Y` must gain a boundary-crossing
row (OBL-TRACE-02); `FR-3D-013` must be corrected (OBL-TRACE-03).

**Human consequence if unmet.** A screen-reader user in the World who chooses
`S-SEMANTIC` — the person this whole amendment exists for — lands with focus on
a destroyed element or on the body, hears nothing, and must re-explore the entire
page from the top to find out where they are.

**Reviewer test.** Name the frame showing the destination control focused, with a
visible indicator, immediately after arrival, and the annotation stating the tree
ordering. Both required.

**Frame cost: 1 distinct frame** — the incoming semantic shell **immediately
after** crossing from a 3D stream: focus on the destination control with a
visible indicator, the status region carrying the arrival message, the mapped
location's `h1` visible. Distinct from the same-shell announcement frame because
it depicts a different DOM and a different tree state — a shell just entered,
focus moved programmatically rather than retained. This is the single frame whose
absence B-03 identifies, and it is the one frame this document most insists on.

### OBL-BND-02 — what is announced on arrival

**SC at stake:** 4.1.3, 2.4.3, 2.4.2 Page Titled.

**Obligation.** The arrival announcement must convey **all three** of: the new
stream in force; the arrival location by its name; and, where the arrival
location is not the canonical mapping of the departure location, that fact and
why. Focus lands on the stream control, which sits in utility navigation — so
without an explicit location statement the visitor is told the stream changed and
not where they are.

**Reviewer test.** Write out the sentence the visitor hears. If it does not name
a location, unmet.

### OBL-BND-03 — the mapping, in both directions, including the unmapped cases

**SC at stake:** 3.2.3 Consistent Navigation, 3.3.7 Redundant Entry, 2.4.3.

**Obligation.**

1. **World → semantic.** Every World location resolves to one canonical semantic
   route. Where a location has no mapping, entry is at the **nearest ancestor**
   that has one, and that substitution is **stated to the visitor** — with a named
   surface, a named politeness level, a stated relationship to focus, and a
   wording constraint. "And says so" is not a requirement; it is a gap with a
   sentence around it.
2. **Semantic → World.** §8.2.4 currently maps "every semantic route *that is
   reachable in the World*", which leaves routes that are not. The rule for
   **unmapped semantic routes** must be stated, not implied.
3. **Mid-process crossings must not restart a process.** `/book` is the live case:
   `ROUTE-BOOK` declares an immersive panel, and the booking lineage is a
   multi-step process with a verified email and a held slot. If a visitor at
   `STATE-SLOT-SELECTED` selects `S-HIGH` and the process restarts, that is
   **3.3.7 Redundant Entry** and a lost booking. The specification must state
   whether process state survives a stream change, and if it does not, the
   advisement (OBL-ADV-01) must say so **before** the control is operated —
   because a warning after the fact is not a remedy.

`[UNRESOLVED GATE]` — whether booking process state survives a stream change is a
product and architecture decision this author cannot make. It must be decided
before the boundary crossing is called specified. Note that the decision does not
change the *accessibility* obligation, only which of two obligations applies: if
state survives, evidence it; if it does not, advise it in advance and treat the
crossing as destructive.

**Record that must carry it.** §8.2.4; `foundation-flow-coverage.csv` booking
lineage rows; `STATES_AND_RECOVERY.md` ACT-09 alternates.

**Human consequence if unmet.** A visitor with a held slot and a verified email
switches stream — perhaps because the 3D booking panel is unreadable at their
zoom level — and loses the slot and re-enters every field.

**Reviewer test.** State what happens to a visitor at `STATE-SLOT-SELECTED` who
selects a different stream. If the package cannot answer, unmet.

**Frame cost: 1 distinct frame** — nearest-ancestor arrival, showing the
substitution statement in its actual surface, in `S-SEMANTIC`. Distinct because
no other frame contains that surface or that wording, and the audit's finding is
precisely that the surface is unnamed; a frame forces it to be named.

### OBL-BND-04 — accessibility-tree ordering during the swap

**SC at stake:** 4.1.3, 2.4.3, 1.3.1.

**Obligation.** The ordering must be stated as a sequence with no overlap, and
must be **annotated on the boundary frame** (OBL-BND-01) rather than left to
prose in one document:

1. Outgoing shell removed from the accessibility tree.
2. Incoming shell added, including its status region, present and **empty**.
3. Focus set on the destination stream control.
4. Announcement written into the status region.
5. In a 3D destination only: the canvas added **after** the incoming shell is
   announced, never before. The canvas is not present in `S-SEMANTIC` at all.

No visitor perceives two shells at once, and no announcement is written into a
region that was inserted with it.

**Reviewer test.** Read the annotation on the boundary frame. Five ordered steps
required. If the ordering exists only in §8.2.4 prose and not on the evidence,
the evidence does not prove it and a reviewer cannot check it against a picture.

**Frame cost.** Zero additional — this is an annotation on the OBL-BND-01 frame.
Stated explicitly so no producer budgets a second call for it.

---

## Part 5 — Stream-change and preference-failure states (B-03)

### OBL-STATE-01 — where the states must live

**SC at stake:** 4.1.3, 2.4.3, 3.2.3, 3.3.1 Error Identification.

**Obligation.** The following states must be **required values** of every state
profile assigned to a record that hosts the delivery stream control. Concretely,
`SP-NAVIGATION` must gain all four, because D-043 re-homed `ACT-09` to it and
`TPL-GLOBAL-NAVIGATION` — B01's primary template and the control's authorized
home — carries it:

| State | Must be a required value of | Currently lives in |
|---|---|---|
| `STATE-STREAM-CHANGED` | `SP-NAVIGATION`, `SP-WORLD`, `SP-FIRST-VISIT` | `SP-WORLD` only |
| `STATE-PREFERENCE-WRITE-FAILED` | `SP-NAVIGATION`, `SP-WORLD`, `SP-FIRST-VISIT` | `SP-FIRST-VISIT` only |
| `STATE-PREFERENCE-READ-FAILED` | `SP-NAVIGATION`, `SP-FIRST-VISIT`, `SP-RETURN-VISIT` | **does not exist** |
| `STATE-STREAM-CEILING-REFUSED` | `SP-NAVIGATION`, `SP-WORLD` | **does not exist** |

**Additionally, a precedence rule is required.** The state axis and the stream
axis currently issue conflicting obligations with no stated precedence: the four
`DS-S-*` profiles demand `STATE-RECEPTION` and `STATE-STREAM-CHANGED` as
intersecting values on every record that selects them, while `COV-ACT-09` carries
`SP-NAVIGATION`, which permits neither. The same unresolved intersection governs
`MP-WORLD`'s `MODE-PRINT` exclusion against `DS-S-SEMANTIC`'s print requirement.
§9 of the contract must state which axis governs when they disagree.

**Human consequence if unmet.** The producer must either omit the frame or emit
an unresolvable state token, and `EC-03`/`EC-08` will accept neither. B01 demands
frames its own state profile cannot express, so the frames that matter most are
the ones easiest to skip and hardest to notice missing.

**Reviewer test.** Attempt to construct a legal evidence ID for a
`STATE_STREAM_CHANGED` frame of `TPL-GLOBAL-NAVIGATION`. If the state token is
not a legal value of the template's profile, unmet.

**Frame cost.** Zero for the schema change itself; the frames it enables are
counted below.

### OBL-STATE-02 — `STATE-STREAM-CHANGED`, same shell

**SC at stake:** 4.1.3, 2.4.3.

**Obligation.** Evidence must show: the polite announcement in its region; focus
**retained** on the operated control; scroll position, any open panel, and the
current route preserved; and the control's accessible name now reporting the new
stream as in force.

**Reviewer test.** One frame plus annotation naming the region and the four
preserved properties.

**Frame cost: 1 distinct frame.** Distinct from the boundary frame because it
proves the *opposite* focus behaviour (retained, not moved) — the two cannot be
the same picture, and conflating them is exactly how the `FR-3D-013` / §8.2.4
contradiction arose.

### OBL-STATE-03 — `STATE-PREFERENCE-WRITE-FAILED`

**SC at stake:** 3.3.1 Error Identification, 4.1.3, 3.2.2 context.

**Obligation.** Following the `ACT-11` pattern: the failure is explained
**without blocking**, the visitor's choice **still applies for the current
session**, the explanation is text (not colour, not an icon alone), and it does
not present as an error the visitor caused. The explanation must state the
consequence in plain terms — that the choice will not be remembered next visit —
because "preference could not be saved" does not tell a visitor what they will
experience.

**Human consequence if unmet.** A visitor who deliberately chose `S-SEMANTIC`
because 3D navigation triggers vestibular symptoms is silently returned to a
computed stream on their next visit, with a camera flight, and no explanation.

**Frame cost: 1 distinct frame.**

### OBL-STATE-04 — `STATE-PREFERENCE-READ-FAILED`

**SC at stake:** 3.3.1, 4.1.3; and the `NFR-A11Y-003` peer commitment.

**Obligation.** §8.2.2 step 4 handles read failure for the **measurement**
("skipped silently — it is an optimisation, not an obligation"). The **step-5
preference** is not an optimisation and must not inherit that treatment. Where a
previously stored stream preference cannot be read, the visitor must be told, in
the destination shell, that their stored choice could not be applied and that
they can re-select — not returned silently to a computed stream.

Two related gaps must be closed in the same slice:

- **One mechanism, two erasures.** The measurement and the preference share one
  storage mechanism, so `ACT-40` "Clear preferences or session" and any routine
  browser storage clear discard the accessibility choice along with the
  performance optimisation. Either they must be separable, or `ACT-40` must warn
  that clearing discards the accessibility choice.
- **The storage notice has nowhere to live.** §8.2.2 points at "the storage notice
  on `/credits` and the privacy route". There is **no privacy route** in the
  34-route inventory, and `ROUTE-CREDITS` names attribution actions only.
  `[UNRESOLVED GATE]` — the notice's home is unresolved and this author does not
  invent a route. (The consent conclusion bundling a user-set preference with an
  unrequested optimisation under one strictly-necessary exemption is a legal
  matter outside WCAG and outside this author's scope; it is flagged, not decided.)

**Human consequence if unmet.** As OBL-STATE-03, but silent: the visitor is not
even told their choice was lost. `prefers-reduced-motion` mitigates motion only;
it does not restore the semantic shell.

**Frame cost: 1 distinct frame.**

### OBL-STATE-05 — `STATE-STREAM-CEILING-REFUSED`

**SC at stake:** 3.3.1, 4.1.2, 4.1.3.

**Obligation.** `ACT-09`'s alternate path already requires that a request above
the WebGL ceiling **remain on the prior stream and say why**, with the ceiling
**stated, not silently substituted**. Evidence must show: the request refused,
the reason in text as a fact about the client, the control's accessible name
still reporting the *prior* stream as in force, and no error styling.

**Human consequence if unmet.** A visitor selects `S-HIGH`, the control silently
substitutes something else, and its accessible name now reports a stream the
visitor did not choose. They have no way to learn that their device cannot do
what they asked, and no way to trust the control's reported value again.

**Frame cost: 1 distinct frame.** This is the only frame that proves the control
does not misreport its own value, which is a 4.1.2 property no other frame
touches.

---

## Part 6 — Traceability and test obligations (B-05)

### OBL-TRACE-01 — every accessibility requirement gets traceability rows

**SC at stake:** none directly; this is the verifiability of the entire set.

**Obligation.** `traceability.csv` currently carries 99 `requirement` rows
(`BR-*`, `FR-*`, `SEO-*`, `UX-*`, `NFR-001`…`008`, `DATA-*`) and **not one**
`NFR-A11Y-*`. `FR-3D-010`…`FR-3D-014` are likewise untraced, including
`FR-3D-014`, created under D-042 specifically as the requirement-level home for
the stream control. Required rows, minimum **12**:

| source_id | contract_records that must appear |
|---|---|
| `NFR-A11Y-001` | all 34 routes; all 19 route templates; all complete-process flows |
| `NFR-A11Y-002` | `DS-S-HIGH`; `DS-S-MEDIUM`; `DS-S-LOW`; `DS-S-SEMANTIC`; the amended `DS-STREAM-INVARIANT`; `EC-08`; the new stream `EC-*` rule |
| `NFR-A11Y-003` | `DS-S-SEMANTIC`; `PRIM-001` `stream_semantic`; every complete-process flow |
| `NFR-A11Y-004` | `PRIM-001`; `PRIM-042`; `PRIM-043`; `PRIM-044`; `COV-ACT-09`; `B01` |
| `NFR-A11Y-005` | `PRIM-043`; style guide §4.1; **plus the sampling-method gate** |
| `NFR-A11Y-006` | style guide §7.3; `MODE-REDUCED-MOTION` |
| `NFR-A11Y-007` | this document's own review lineage; `R-035` |
| `FR-3D-010` | `DS-S-SEMANTIC`; `PRIM-001` |
| `FR-3D-011` | all four `DS-S-*` |
| `FR-3D-012` | style guide §8.2.2; `U-03` gate |
| `FR-3D-013` | §8.2.4; `SP-NAVIGATION`; **corrected per OBL-TRACE-03** |
| `FR-3D-014` | `PRIM-001`; `PRIM-042`; `PRIM-043`; `PRIM-044`; `COV-ACT-09`; `B01` |

**Reviewer test.** `grep NFR-A11Y traceability.csv` must return at least seven
rows; `grep FR-3D-01 traceability.csv` at least five. Zero is the current state.

**Frame cost.** Zero.

### OBL-TRACE-02 — the requirement set must cover what the design package promises

**Obligation.** `NFR-A11Y-001`…`007` are correctly marked unimplemented with no
conformance claimed, and are a real improvement. Against the package's actual
promises they are missing requirement-level rows for:

- **the boundary crossing** — focus destination, bidirectional mapping,
  nearest-ancestor entry, tree ordering (OBL-BND-01…04). `FR-3D-013` covers only
  the same-shell case;
- **persistence and its failure modes** — cross-session persistence, write
  failure, read failure (OBL-STATE-03, -04);
- **2.4.11 Focus Not Obscured (Minimum)** — new at AA in WCAG 2.2 and directly at
  risk from a persistent HUD over a canvas. The contract requires it of sticky
  navigation and HUD controls; no requirement row carries it;
- **1.4.13 Content on Hover or Focus** — §4.1 requires the hotspot label to expand
  on hover and on focus, which is additional content triggered by hover and focus,
  so it must be dismissible without moving focus, hoverable, and persistent. None
  of the three is specified anywhere, and §7.2 has already bound `Escape` to
  "Close panel / go back", so the obvious dismissal key would navigate;
- **2.2.1 Timing Adjustable** — the `TL-*` machinery is elaborate in the design
  package and has no requirement-level home;
- **the role and activation model** (OBL-CTRL-01) and **the visible advisement**
  (OBL-ADV-01), both of which must be stated at requirement level and not only in
  a style guide section.

**Human consequence if unmet (1.4.13 specifically).** A low-vision visitor at
400% zoom hovers a hotspot; the expanded label covers the adjacent hotspot and
cannot be dismissed without leaving the location.

### OBL-TRACE-03 — resolve the `FR-3D-013` / §8.2.4 focus contradiction

**SC at stake:** 2.4.3.

**Obligation.** `FR-3D-013` says the mid-session change "is announced politely,
**does not move focus**, and preserves scroll, open panel, and route". §8.2.4's
boundary paragraph says that across the semantic boundary focus is **not**
preserved and moves to the destination control. Both are correct for their own
case and the SRS row was not updated when the boundary case was added.

The requirement must be split into two rows, or restated with an explicit
same-shell qualifier and a companion boundary row. An implementation that
correctly follows §8.2.4 currently fails `FR-3D-013` as written, and a tester
verifying `FR-3D-013` literally would file the correct behaviour as a defect.

**Reviewer test.** Read `FR-3D-013` and §8.2.4 together. If a single
implementation can satisfy both as written, resolved; otherwise unmet.

### OBL-TEST-01 — tests that actually exercise streams

**Obligation.** Across all 45 UX tests in `CONTENT_ANALYTICS_TESTS.md`, the word
"stream" does not appear once. `COV-ACT-09`'s `linked_tests` are `UXTEST-007`
(loader/WebGL/asset/network/device loss at every transition) and `UXTEST-025`
(reduced motion/low power/audio muted) — the two tests that fitted its
predecessor, "Toggle quality", under failure conditions. Neither touches stream
selection, keyboard operability, the accessible name, the announcement, the
advisement, or the boundary crossing. **`COV-ACT-09` must be re-linked**, and the
following tests must exist:

| Test | Must verify | Discharges |
|---|---|---|
| **T-STREAM-01** Control conformance | Role is a radio group with a separate submit; arrowing does **not** apply a stream; only explicit activation does; group name reports the in-force stream; each option named in peer vocabulary | OBL-CTRL-01, -02; 3.2.2, 4.1.2 |
| **T-STREAM-02** Keyboard and focus | Full keyboard operability in every stream; no trap; visible focus indicator on every part; nothing obscures the focused control; `Escape` does not navigate | OBL-CTRL-04; 2.1.1, 2.1.2, 2.4.7, 2.4.11 |
| **T-STREAM-03** Advisement reception | The advisement reaches sighted mouse, sighted keyboard **without AT**, screen-reader, and 400%-magnifier users **before** operation | OBL-ADV-01; 3.2.2 |
| **T-STREAM-04** Same-shell announcement | Polite region announces; focus retained; scroll, open panel and route preserved | OBL-STATE-02; 4.1.3 |
| **T-STREAM-05** **Boundary crossing** — `S-SEMANTIC` ⇄ 3D | Outgoing shell leaves the tree first; incoming status region present and empty before the message; focus lands on the destination control **with a visible indicator**; announcement names stream **and** location; canvas added last when entering a 3D stream; nearest-ancestor entry states the substitution | OBL-BND-01…04; 2.4.3, 3.2.3, 3.2.4, 4.1.3, 2.4.7 |
| **T-STREAM-06** Persistence failures | Write failure explained without blocking, choice applies for session; read failure explained, not silent; ceiling refusal states the ceiling and does not misreport the control's value | OBL-STATE-03, -04, -05; 3.3.1, 4.1.2 |
| **T-STREAM-07** `S-SEMANTIC` end to end | Each complete process — booking, contact, AI concierge, human handoff, media opt-in — completed start to finish using `S-SEMANTIC` only, keyboard only, and again with a screen reader; no step requires a canvas; mid-process stream change does not force redundant entry | OBL-INV-02, OBL-BND-03; the conformance target; 3.3.7 |

**T-STREAM-05 is the mandatory boundary test** the brief requires and the one the
package currently has no equivalent of at any level.

**Human consequence if unmet.** A P0 requirement that no record selects and no
test exercises is an inert axis at requirement level — the same defect three
layers up, and the reason four remediations passed a clean validator while the
substance was missing.

**Reviewer test.** `grep -i stream CONTENT_ANALYTICS_TESTS.md` must return
matches in at least seven distinct tests, and `COV-ACT-09.linked_tests` must name
at least T-STREAM-01, -03, -04 and -05.

---

## Part 7 — Frame budget implied for B01

Metered external design calls are capped at 20 per month. The obligations above
imply **13 distinct stream-attributable frames on B01**, of which **7 are already
required by `B01.required_visual_evidence`** and **6 are net new**.

| # | Frame | Obligation | New? | Why nothing cheaper discharges it |
|---|---|---|---|---|
| 1–4 | Control reporting each of the four streams as in force; `VP-DESKTOP`, `MODE-STANDARD`, `TPL-GLOBAL-NAVIGATION` | OBL-CTRL-02 | existing | Per-stream contrast, target size and focus order are properties of a rendering; one frame evidences one rendering (OBL-INV-03) |
| 5 | Control reachable at `VP-320` in `S-SEMANTIC`, through the narrow-viewport disclosure | OBL-CTRL-03 | **new** | The disclosure path does not exist at desktop width; reachability is rendered, not asserted |
| 6 | Control focused, advisement text rendered in place, visible focus indicator, nothing obscuring | OBL-ADV-01, OBL-CTRL-04 | existing (advisement) | Resting frames show no focus indicator; annotations show no rendered placement |
| 7 | `STATE-STREAM-CHANGED`, same shell: focus **retained**, region announcing, scroll/panel/route preserved | OBL-STATE-02 | existing | Proves the opposite focus behaviour from frame 8; cannot be the same picture |
| 8 | **Boundary arrival**: incoming semantic shell immediately after crossing from a 3D stream — focus **moved** to destination control with visible indicator, status region carrying the message, mapped `h1` visible; tree ordering annotated | OBL-BND-01, -02, -04 | **new** | The single frame B-03 identifies as missing everywhere; a different DOM and tree state from frame 7 |
| 9 | Nearest-ancestor entry, showing the substitution statement in its actual surface | OBL-BND-03 | **new** | The surface is currently unnamed; a frame forces it to exist |
| 10 | `STATE-PREFERENCE-WRITE-FAILED`, ACT-11 pattern, non-blocking | OBL-STATE-03 | existing | A failure state's copy, styling and non-blocking placement are rendered properties |
| 11 | `STATE-PREFERENCE-READ-FAILED` on return | OBL-STATE-04 | **new** | A distinct state with distinct copy; currently does not exist anywhere |
| 12 | `STATE-STREAM-CEILING-REFUSED` — request refused, ceiling stated, prior stream still reported | OBL-STATE-05 | **new** | Only frame proving the control does not misreport its own value |
| 13 | `MODE-FORCED-COLORS` on the control in `S-SEMANTIC` | OBL-CTRL-06 | **new** | Forced colors is a platform substitution; a note on a standard-mode frame cannot show it |

**Explicitly requiring no additional frame** (stated so the budget is not
over-spent): the accessibility-tree ordering (annotation on frame 8); the
screen-reader reading order of the control (annotation on frames 4 and 8); the
role and activation model (specification text — a picture cannot establish it);
`MODE-PRINT` for `S-SEMANTIC` (attaches to route and process records in later
batches, not to the control).

**Budget note.** 13 frames against a 20-per-month allowance leaves 7 for
everything else B01 owns, which is not enough for B01's non-stream obligations.
`[UNRESOLVED GATE]` — this is a scheduling decision for the founder, not an
accessibility one. The accessibility position is only this: **the six net-new
frames are not reducible**, because each is the sole evidence of a distinct
behaviour that the last four remediations each failed to specify. If the
allowance forces a choice, frame **8** (boundary arrival) is the one whose
absence the audit identified as leaving the amendment's primary beneficiary
entirely unevidenced.

---

## Standing note

Nothing above is a conformance claim. Every obligation is a requirement on a
specification and an evidence package, and every WCAG 2.2 success criterion named
is evaluated against an implementation that does not yet exist. `R-035` and
`R-036` remain open on the record; this document does not close them and does not
purport to. It states what any delivery-stream evidence model must satisfy so
that a future model can be reviewed against something other than its author's
assurance.

**[PROPOSED SPECIFICATION] — pending founder decision.**
