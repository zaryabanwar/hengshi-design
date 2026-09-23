# Accessibility Audit — CR-002 Amended Package (iteration 4)

**Review date:** 2026-09-06
**Package under review:** CR-002 amended package as remediated under **D-043**,
design freeze aggregate
`DB92B4D0B889948D6C272F0DC7397327055B0108E7EEB953924F34E735BD4649`
(recomputed by this reviewer from a fresh validator run; it matches).
**Reviewer:** independent accessibility review agent. I did not author any
material under review and I am not the producer. Constitution 2.0.0 principle VII.
**Discharges:** MA-029 (accessibility half).

**Verdict: FAIL.**

**Conformance target reviewed against:** WCAG 2.2 Level AA for every applicable
full page and complete process, including represented third-party steps, holding
independently within each of the four peer delivery streams. No current
conformance is claimed by the package and none is claimed here. Nothing is built;
this is a review of whether the specification is complete, testable, and free of
unsupported conformance claims.

> The validator returns `RESULT=PASS PASS_COUNT=189 FAIL_COUNT=0`. This is the
> fourth consecutive round in which every finding below was invisible to a clean
> deterministic run (183, 184, 185, now 189). The producer has recorded the right
> lesson — *a passing validator is a determinism check, not a review* — and then
> reproduced the defect it describes. **The central defect of D-042 has recurred
> in D-043, one level up.** D-042 added a stream axis that no record selected.
> D-043 made every record select one, and made the *escape value* the default for
> every record that matters.

---

## Direct answer to the question MA-029 asks

**`DS-STREAM-INVARIANT` is not a sound positive claim. It is a loophole**, and it
is a wider one than the inert `DS-S-*` profiles it replaced. See **B-01**.

---

## Blocking findings

### B-01 — `DS-STREAM-INVARIANT` is an exemption wearing an equivalence claim, and every route takes it

**SC at stake:** the §2.3 per-stream target as a whole; concretely 1.4.3, 1.4.11,
2.4.3, 2.5.8, 1.3.1, 1.3.2.

The profile is worded as a positive claim — "the record must state that it renders
identically in each" — and carries its own guard rail:

> *"This profile may never be selected by a record whose rendering depends on the
> World canvas or on the shell that hosts the delivery stream control; such
> records must select all four `DS-S-*` profiles."*

Contract §9 repeats it verbatim. Both are violated on a majority of the ledger.

| File | rows | `DS-STREAM-INVARIANT` | all four `DS-S-*` |
|---|---:|---:|---:|
| `foundation-route-coverage.csv` | 34 | **34** | 0 |
| `reference-template-inventory.csv` | 40 | 32 | 8 |
| `foundation-flow-coverage.csv` | 89 | 53 | 36 |

Three independent proofs that the claim is false on those rows, each drawn from
the package's own data:

1. **Every one of the 34 routes declares a distinct World rendering in its own
   row.** `immersive_stream_representation` is non-empty on 34 of 34:
   `ROUTE-HOME` → "Reception/atrium orientation panel"; `ROUTE-WING-STRATEGY` →
   "Sequenced Strategy threshold; closed/held/opening/open"; `ROUTE-BOOK` →
   "Booking panel that opens same semantic booking flow"; `ROUTE-CREDITS` →
   "Attribution panel that opens the same semantic notice". A record cannot both
   assert that it renders identically in all four streams and specify a separate
   immersive rendering in the adjacent column. A translucent panel over a
   high-texture 3D scene and a standalone semantic document do not have the same
   contrast, the same focus order, or the same target geometry.
2. **All 19 route templates depend on `PRIM-001`**, the Public semantic shell —
   which is exactly "the shell that hosts the delivery stream control": its
   `required_anatomy` ends `…;delivery stream control`, its `required_variants`
   are `public;no_script;offline;unsupported_browser;prior_release;stream_high;
   stream_medium;stream_low;stream_semantic`, and its states include
   `stream-selected` and `stream-preference-write-failed`. A primitive with four
   per-stream variants does not render identically in four streams.
3. **The mode axis contradicts the stream axis on the same row.** All 34 routes
   carry `MP-PUBLIC` or `MP-INTERACTIVE`, both of which require a distinct
   `MODE-SEMANTIC-SHELL` frame. A record that needs a separate semantic-shell
   frame is, by construction, not stream-invariant.

**The validator forces the wrong answer.** Lines 335–350 classify a record as
stream-dependent by a proxy — `state_profile` in `SP-WORLD`, `SP-FIRST-VISIT`,
`SP-RETURN-VISIT`, `SP-NAVIGATION`, `SP-SYSTEM-RECOVERY` — and then requires
every other record to be *exactly* `DS-STREAM-INVARIANT`. A producer who
correctly assigned all four `DS-S-*` to `ROUTE-BOOK` would fail
`delivery-stream-assignment`. The contract states one rule ("depends on the World
canvas or on the shell that hosts the stream control"); the validator enforces a
different one and cannot be satisfied by the first.

**Net effect, which is F-02 verbatim in a new location.** `DS-S-SEMANTIC`'s
obligations — "contrast target size and focus order are each measured against
this stream's own rendering and never inherited from another stream",
forced-colors and print captures, "every core journey completed end to end using
only this stream" — attach to **zero routes and zero route templates**, and to no
flow covering booking, contact, the AI concierge, human handoff, or media opt-in.
Those are the complete processes the conformance target names.

**Human consequence.** A visitor whose client returns no WebGL context — an
older Android device, a locked-down enterprise browser, a machine with GPU
blocklisting — uses `S-SEMANTIC` for all 34 routes and for the entire booking
lineage. Not one route row, template row, or booking/contact/AI flow row requires
a single frame drawn in that stream. Their contrast, their focus order, their
target sizes and their end-to-end ability to book a meeting are discharged by
frames drawn in a stream they will never see. A producer can satisfy every ledger
cell, pass 189/189, and produce no `S-SEMANTIC` evidence for any page or any
process.

### B-02 — the production package has no stream axis at all, so no per-stream frame can be captured, named, or validated

**SC at stake:** the per-stream target; `NFR-A11Y-002`.

`B01`'s `required_visual_evidence` is genuinely strong (see B-04's partial
credit): four current-stream frames, the `STATE-STREAM-CHANGED` announcement
frame, the write-failure frame, the advisement. It is also uncapturable.

- `evidence-capture-plan.csv` **EC-08** fixes the evidence-ID grammar as
  `HSD_UIR_<BATCH>_<TEMPLATE>_<INSTANCE>_<STATE>_<VIEWPORT>_<MODE>_V<NN>`.
  **There is no stream token.** The four frames B01 demands cannot be
  distinguished from one another in the manifest.
- **EC-10** checks `viewport_id` against profile required values; **EC-11**
  checks `mode_id`. **No rule checks a stream.** There is no `stream_id` field.
- `grep -i stream` over `validate-ui-reference-production.ps1` returns two
  incidental matches, neither about delivery streams.
- `EC-14` already knows how to mark an obligation deferred
  (`deferred_B07;deferred_B09`). Nothing does so for the stream axis, because the
  axis does not exist there.

The production contract's own front matter acknowledges the D-043 stream fix, and
the artifacts that turn a ledger obligation into files on disk were not amended
to carry it. **The one piece of evidence R-036's mitigation rests on — ACT-09
proven in four streams on an authorized batch — will be produced, if at all,
under a naming grammar that cannot record which stream it shows and a validator
that will not notice its absence.** This is the D-042 shape exactly: an axis
asserted upstream and inert downstream.

### B-03 — the stream-change state does not exist outside the World, so the semantic side of the boundary crossing has no required frame anywhere

**SC at stake:** 4.1.3 Status Messages, 2.4.3 Focus Order, 3.2.3 Consistent
Navigation.

`STATE-STREAM-CHANGED` is a required value of **`SP-WORLD` only**. But D-043
re-homed `ACT-09` to `SP-NAVIGATION`, whose required values are
`STATE-CLOSED;STATE-OPEN;STATE-LOADING;STATE-EMPTY-QUERY;STATE-NO-RESULTS;
STATE-RESULTS;STATE-STALE;STATE-DERIVED-INDEX-UNAVAILABLE;STATE-OFFLINE;
STATE-ERROR;STATE-FOCUS` — a disclosure-and-search vocabulary that contains no
state for a stream having changed and no state for a preference write having
failed (`STATE-PREFERENCE-WRITE-FAILED` lives only in `SP-FIRST-VISIT`). The
same applies to `TPL-GLOBAL-NAVIGATION`, B01's primary template and the control's
authorized home.

Three consequences:

1. **B01 demands frames its own profiles do not define.** `EC-03` verifies "state
   coverage per profile" and `EC-08` encodes `<STATE>` in the filename. A
   `STATE_STREAM_CHANGED` or `STREAM_PREFERENCE_WRITE_FAILED` frame for
   `TPL-GLOBAL-NAVIGATION` is not a legal value of `SP-NAVIGATION`. The producer
   must either omit the frame or emit an unresolvable state token.
2. **The four `DS-S-*` profiles demand `STATE-RECEPTION` and
   `STATE-STREAM-CHANGED` as intersecting values** on every record that selects
   them. `COV-ACT-09` selects all four and carries `SP-NAVIGATION`, which permits
   neither. The obligation is unsatisfiable as written and there is no stated
   precedence between the state axis and the stream axis.
3. **The incoming semantic shell is unevidenced.** §8.2.4's hardest case is a
   visitor leaving the World for `S-SEMANTIC`: the outgoing subtree is destroyed
   and the incoming one must announce itself. The outgoing side has a state
   (`SP-WORLD`/`STATE-STREAM-CHANGED`, in deferred `B07`). The incoming side is a
   route on `SP-PUBLIC-*` with `DS-STREAM-INVARIANT` and `STATE-REST`. **No
   record anywhere requires a frame of the semantic shell immediately after a
   stream change.**

**Human consequence.** A screen-reader user in the World who selects
`S-SEMANTIC` is the person this whole amendment exists for. The moment they land
is the moment nothing in the package requires anyone to draw, annotate, or review.

### B-04 — the 3.2.2 replacement puts the advance advisement where most users cannot receive it, and never fixes the control's activation model

**SC at stake:** 3.2.2 On Input, 4.1.2 Name Role Value.

Withdrawing "3.2.2 is satisfied by construction" was correct and the correction
block is honest. The replacement is not sufficient.

§8.2.4: *"the control states what it will do **before** it is used: its
**accessible description** says that choosing a stream reloads the experience in
that stream and keeps the current location."*

- An accessible description is exposed through the accessibility tree. A sighted
  mouse user and a sighted keyboard user who are not running assistive technology
  receive **nothing**. 3.2.2's advisement must be available to the user who is
  about to operate the control, not only to the subset using an AT that surfaces
  descriptions — and several common combinations do not announce
  `aria-describedby` on a `select` at all. The requirement as written cannot
  discharge the SC it was written to discharge, and `NFR-A11Y-004` ("advises
  before it acts") inherits the same weakness.
- **The control's role and activation model are still unspecified.** §8.2.4,
  `PRIM-001`, `FR-3D-014` and `NFR-A11Y-004` all describe behaviour and none
  names a role. Whether the control is a native `select` (where arrowing through
  options changes the value in several browsers — the textbook 3.2.2 failure),
  a listbox with an explicit Apply, or a group of radio buttons plus a submit, is
  the single decision that determines whether 3.2.2 is met. It is not made.

**Human consequence.** A keyboard user arrows down the stream control to read the
options, and the page reloads into `S-SEMANTIC` — or into `S-HIGH`, launching a
camera flight — without warning and without their having chosen anything. This
is the exact failure the withdrawn claim pretended was impossible.

### B-05 — the requirements added to give this package a home have no downstream reference: nothing traces to them and nothing tests them

**SC at stake:** none directly; this is the verifiability of the entire set.

- **`NFR-A11Y-001`…`007` appear nowhere outside SRS §5.6.** A repository-wide
  search for `NFR-A11Y` across all CSV, MD, JSON and PS1 files returns matches in
  the SRS and in review documents only. `traceability.csv` carries 99
  `requirement` rows — `BR-*`, `FR-*`, `SEO-*`, `UX-*`, `NFR-001`…`008`,
  `DATA-*` — and **not one** `NFR-A11Y-*`.
- **`FR-3D-010` … `FR-3D-014` are also untraced**, including `FR-3D-014`, created
  under D-042 specifically as the requirement-level home for the stream control.
- **`ACT-09` has no test that exercises it.** `COV-ACT-09`'s `linked_tests` are
  `UXTEST-007` (loader/WebGL/asset/network/device loss at every transition) and
  `UXTEST-025` (reduced motion/low power/audio muted). Neither touches stream
  selection, keyboard operability, the accessible name, the announcement, the
  advisement, or the boundary crossing. Across all 45 UX tests, the word
  "stream" does not appear once in `CONTENT_ANALYTICS_TESTS.md`. ACT-09 is
  still linked to the two tests that fitted its predecessor, "Toggle quality",
  under failure conditions.

The iteration-3 correction block says the SRS "had no requirement-level home and
nothing to trace to". Half of that is fixed: the requirements now exist. The
other half is not: there is still nothing that traces to them, and nothing that
verifies them. A P0 requirement that no record selects and no test exercises is
the inert axis again, at requirement level.

---

## Significant findings

### S-01 — the `S-SEMANTIC` boundary crossing is specified in the right places and is still not testable as written

**SC:** 2.4.3, 3.2.3, 3.2.4, 4.1.3, 3.3.7, 2.4.7.

§8.2.4 is a real improvement — it names a focus destination, gives the mapping a
direction and a nearest-ancestor rule, and orders the accessibility-tree swap.
What remains unspecified:

- **Which status region carries the announcement across the swap.** The bullets
  say the change is announced "through the page status region" and the boundary
  paragraph says the outgoing shell leaves the tree before the incoming one
  enters. A live region inserted into the DOM together with its message is
  routinely not announced. Nothing says the incoming shell's status region must
  exist and be empty before the message is written into it. 4.1.3 turns on
  precisely this.
- **What is announced on arrival.** Focus lands on the stream control, which sits
  in utility navigation. Nothing requires the new location, route, or `h1` to be
  conveyed. The visitor is told the stream changed and not where they are.
- **"and says so" is not a requirement.** The nearest-ancestor case — a World
  location with no canonical route — must "say so" with no stated surface,
  no politeness level, no relationship to focus, and no wording constraint.
- **The reverse direction has no rule for unmapped routes.** The mapping is
  stated as "every semantic route *that is reachable in the World*" — leaving
  routes that are not. `/book` is one: `ROUTE-BOOK` declares an immersive panel,
  but the booking lineage is a multi-step process with a verified email and a
  held slot. What happens to a visitor who selects `S-HIGH` at
  `STATE-SLOT-SELECTED` is unspecified. If the process restarts, that is 3.3.7
  Redundant Entry and a lost booking.
- **2.4.7 on arrival.** Programmatic focus on the incoming control is not
  required to be *visibly* indicated; §4.1's focus rule covers hotspots only.

### S-02 — step-4 storage: the accessibility-relevant preference can vanish silently, the consent conclusion is asserted, and the promised notice has no surface

**SC:** 3.2.2 context, plus a privacy gap that is not a WCAG matter.

§8.2.2 step 4 is careful about write failure and about not applying a measurement
to the session that produced it. It leaves four gaps:

1. **Read failure of the step-5 preference is unspecified.** The text handles
   read failure for the *measurement* ("skipped silently — it is an optimisation,
   not an obligation"). The preference is not an optimisation. A visitor who
   deliberately chose `S-SEMANTIC` — because 3D navigation is unusable for them,
   or triggers vestibular symptoms — and whose store is later unreadable is
   returned to a computed stream with no notice and no explanation.
   `prefers-reduced-motion` (step 6) mitigates motion only; it does not restore
   the semantic shell.
2. **One mechanism for two things means one erasure for two things.** The
   measurement and the preference "share one mechanism", so `ACT-40` "Clear
   preferences or session" — and any routine browser storage clear — discards the
   accessibility choice along with the performance optimisation. Nothing warns
   that this will happen or offers to keep the choice.
3. **The consent conclusion is asserted, not reasoned.** "It carries no personal
   data and no identifier, so it needs no consent gate." A user-set preference is
   a strong candidate for the strictly-necessary exemption. **The stored
   measurement is not** — the document itself calls it an optimisation the
   visitor did not request. Bundling the two under one exemption is the kind of
   legal conclusion this package elsewhere refuses to make without a gate.
   Retention is "until the visitor clears it", i.e. indefinite, with no stated
   limit.
4. **The notice has nowhere to live.** "The storage notice on `/credits` and the
   privacy route names it." There is **no privacy route** in the 34-route
   inventory — the accepted set ends `/about`, `/contact`, `/book`, `/credits` —
   and `ROUTE-CREDITS`'s row names attribution actions only, with no storage
   notice in `instance_evidence` or `primary_next_actions`. B02's `/credits`
   evidence likewise requires the attribution list and says nothing about
   storage. The sentence resolves to nothing in either place it points.

### S-03 — R-034 has now been closed prematurely a second time, on the identical defect class, by a guard widened just short of the one surviving instance

**SC:** 1.3.1 / 3.3.1 framing; the D-039 peer commitment.

`reference-template-inventory.csv`, `TPL-QUICK-ACCESS-RECOVERY`, `baseline_frame_name`:

```
HSD_UIR_B07_TPL_QUICK_ACCESS_RECOVERY_REF_STATE_ASSET_FAILURE_VP_320_MODE_NON_WEBGL_QUICK_ACCESS_V01
```

The D-043 guard was widened to catch `MODE-NON-WEBGL[A-Z-]*`. Frame names use
underscores, so `MODE_NON_WEBGL_QUICK_ACCESS` evades it. This is the only
surviving occurrence in the repository, it is inside the freeze, and it is in a
package file the producer edited in this same remediation. R-034's D-043 closure
note asserts the rename is complete and the guard is now adequate; it is neither.
The pattern of the last two rounds repeats: the guard is widened to the shape of
the instances already found, and the freeze still contains one it cannot see.

A no-WebGL visitor's recovery reference is still named after "non-WebGL Quick
Access" — the semantic peer as an unsupported-client mode.

### S-04 — `BP-NFR-006` reinstates the unsupported-client framing and contradicts §8.2.2 step 1 on which stream a real visitor receives

**SC:** the peer commitment; concretely, which stream a below-floor client gets.

README and contract: *"Clients below the floor or otherwise unsupported must
receive the equivalent semantic Quick Access journey without WebGL."*

Style guide §8.2.2 step 1: `S-SEMANTIC` is selected **if and only if a WebGL
context cannot be obtained**. Browser version is not a selection signal anywhere
in §8.2.

A Safari 16.3 client is below the floor and has WebGL. Two accepted authorities
now disagree about what it receives. Iteration 3 recorded this as an open
residual on R-034 ("silent on which stream a below-floor client receives"); it is
no longer silent, it is contradictory — and the wording that resolves it makes
`S-SEMANTIC` the destination for unsupported clients, which is the framing D-039
removed.

### S-05 — the mode axis and the stream axis issue conflicting obligations with no precedence rule

`MP-WORLD` excludes `MODE-PRINT` ("not applicable to the live World shell").
`DS-S-SEMANTIC` requires print captures and states that its print obligation "is
not covered by the MP-WORLD print exclusion". `COV-ACT-09`, `COV-ACT-06`,
`COV-ACT-08`, `COV-ACT-11`, `COV-ACT-12` and the World flows all carry `MP-WORLD`
**and** `DS-S-SEMANTIC`. A producer reading the mode axis omits the frame; a
producer reading the stream axis draws it. §9 of the contract establishes no
precedence. The same unresolved intersection governs `STATE-RECEPTION` /
`STATE-STREAM-CHANGED` under `SP-NAVIGATION` (B-03).

### S-06 — 1.4.13 Content on Hover or Focus is unaddressed, and the hotspot design is a 1.4.13 case

**SC:** 1.4.13 (Level AA).

§4.1 requires the hotspot label to expand on hover ("Label expands to its full
form") and on keyboard focus ("the label in its expanded form"). That is
additional content triggered by hover and focus, so 1.4.13 requires it to be
dismissible without moving focus, hoverable, and persistent. None of the three is
specified anywhere — not §4.1, not §7.2, not the contract's §10 annotation list,
not `NFR-A11Y-005`. Worse, §7.2 binds Escape to "Close panel / go back", so the
obvious dismissal key is already taken and dismissing the label would navigate.

**Human consequence.** A low-vision visitor at 400% zoom hovers a hotspot; the
expanded label covers the adjacent hotspot and cannot be dismissed without
leaving the location.

### S-07 — `FR-3D-013` and style guide §8.2.4 now contradict each other on focus

`FR-3D-013`: the mid-session change "is announced politely, **does not move
focus**, and preserves scroll, open panel, and route (§8.2.4)".

§8.2.4, boundary paragraph: across the semantic boundary "Focus is therefore
**not** preserved on that element … Focus moves to the delivery stream control in
the destination shell."

The SRS row was written for the pre-D-043 text and was not updated when the
boundary case was added. An implementation that correctly follows §8.2.4 fails
`FR-3D-013` as written, and a tester verifying `FR-3D-013` literally would file
the correct behaviour as a defect.

### S-08 — SRS §5.6 does not cover what the design package promises, and one row is not testable as stated

`NFR-A11Y-001`…`007` are a real improvement and are correctly marked
unimplemented with no conformance claimed. Against the package's actual promises
they are missing:

- **the boundary crossing** — focus destination, bidirectional mapping,
  nearest-ancestor entry, accessibility-tree ordering (§8.2.4). `FR-3D-013`
  covers only the same-shell case and does so wrongly (S-07);
- **persistence and its failure modes** — cross-session persistence, the
  write-failure branch, and the unspecified read-failure branch (S-02);
- **2.4.11 Focus Not Obscured (Minimum)**, new at AA in WCAG 2.2 and directly at
  risk from a persistent HUD over a canvas. Contract line 232 requires it of
  sticky navigation and HUD controls; no requirement row carries it;
- **1.4.13** (S-06);
- **2.2.1** — the `TL-*` machinery is elaborate in the design package and has no
  requirement-level home.

`NFR-A11Y-005` requires the focus indicator at "≥3:1 against **every adjacent
scene colour**". Against a lit, textured, animated 3D scene this has no sampling
method, no adjacency definition, and no measurement procedure, so it cannot be
passed or failed. It also differs per stream by construction, which is why B-01
matters: the requirement exists and the ledger does not require it to be measured
in more than one stream.

### S-09 — the design-system artifact that implementation inherits has no stream axis

`DESIGN_SYSTEM_IMPLICATIONS.md` is hash-pinned, specialist-owned, and mentions
"stream" twice, both in passing. §5 "Accessibility and behavior contract" says
"Contrast is checked per rendered state" and never per stream; §3 defines no
delivery-stream control component; §2 defines no tokens for its four values or
for the 3D focus ring §4.1 now mandates. The document that will hand this to
implementation contains none of the amendment's accessibility substance, and
because it is read-only inside this package it cannot be fixed here.

---

## Minor findings

- **M-01** — `COV-FLOW-AI`, `COV-FLOW-HUMAN-HANDOFF`, `COV-FLOW-MEDIA-OPT-IN` and
  `TPL-AI-CONCIERGE` ("**Reception** AI Concierge") are Reception surfaces forced
  onto `DS-STREAM-INVARIANT` by the validator proxy. A concierge panel over a 3D
  scene and a concierge page in the semantic shell are not the same rendering; a
  translucent `bg-gray-900/95 backdrop-blur` panel (§6.2) over a high-texture
  scene has different measured contrast from the same panel in `S-SEMANTIC`.
  Subsumed by B-01.
- **M-02** — degradation vocabulary survives immediately outside the guard's
  scope, which is the 13 design-package files only: `STATES_AND_RECOVERY.md`
  "ACT-06 Enter **optional World**" and `UX_ARCHITECTURE.md` "J-02 **Optional
  immersive discovery**" both match the guard's own `optional (world|immersive)`
  alternative and are never scanned. The same scoping means the
  `unsupported-conformance-claim-absence` guard could not have caught the D-042
  "satisfied by construction" claim either, since that sentence lived in the
  style guide. Note also that `COV-ACT-06` renames the action "Enter World
  stream" while the accepted upstream row still says "Enter optional World" — one
  action ID, two names.
- **M-03** — README overclaims: the stream profiles are "assigned through the
  `stream_profile` column on every route, flow, and template row, **so per-stream
  evidence is a resolvable obligation rather than a claim in prose**". Given
  B-01 and B-02 the second clause is not supported: on the route axis the
  obligation resolves to a single invariant frame set, and downstream it cannot
  be named or checked at all.
- **M-04** — `ACT-09`'s evidence is split across an authorized and a deferred
  batch without saying so. `COV-ACT-09` lists `TPL-GLOBAL-NAVIGATION`
  (B01), `TPL-WORLD-HUD` (B07, deferred) and `TPL-QUICK-ACCESS-RECOVERY` (B07,
  deferred). Only the first is reachable under MA-025.
- **M-05** — `COV-ACT-09` selects `TL-NOT-APPLICABLE` while `B01`, the batch that
  owns it, selects `TL-WARN-EXTEND`, and `EC-12` requires evidence to be
  annotated with the batch branch. The stream control will be annotated with a
  time-limit branch it does not have.
- **M-06** — §8.2 retains present-indicative equivalence about an unbuilt system
  ("Every route reachable in `S-HIGH` **is** reachable in `S-SEMANTIC`…") inside
  a document headed `Status: Active`. F-09's fix — a dated decision header — was
  applied to §8.2.2 and not to §8.2's opening. Read as a requirement it is fine;
  read as a status statement it is the F-09 shape.

---

## Regression check on the earlier findings

| ID | Status now |
|---|---|
| **F-01** mid-session promotion | **Holds.** No promotion construct survives. `ACT-08` states in both the flow row and `STATES_AND_RECOVERY.md` that the stream does not change on failure; §8.2.2 makes step 5 the only post-first-paint change; `STATE-STREAM-CHANGED` replaced `STATE-QUALITY-DOWNGRADED`. The withdrawal of "3.2.2 satisfied by construction" is correct and correctly reasoned. **The replacement is not sufficient — see B-04.** 4.1.3 is now handled separately and correctly in kind (polite status region, focus not moved), but has no required frame outside the World (B-03). |
| **F-02** no stream axis; `S-MEDIUM` unrepresented | **Not closed — recurs as B-01.** The `S-MEDIUM` half *is* genuinely fixed: 36 flows and 8 templates select `DS-S-MEDIUM`, and B01 requires a `stream_medium` frame of the control. The main claim is not: a producer can still satisfy every ledger cell, pass 189/189, and produce no `S-SEMANTIC` evidence for any of the 34 routes or any complete process. |
| **F-03** control has no home / no a11y spec | **Partly.** Home is real: `PRIM-001`, `PRIM-042`, `PRIM-043`, `PRIM-044`; `ACT-09` re-homed and named "Select delivery stream"; §8.2.4 covers announcement, name and boundary. Missing: role and activation model (B-04), any state to draw it in (B-03), any test (B-05), any trace (B-05). |
| **F-04** governance deadlock / B07 deferred | **Unchanged and honestly recorded.** §0.1 remains corrected, B07 remains deferred, R-036 remains open, and no document claims the four-stream obligation is met. See **F-09 below** on whether the producer overstates the reduction. |
| **F-05** motion and non-colour cues | **Holds.** §7.3's suppression list is exhaustive and normative with the correct catch-all; §4.1 carries a normative Keyboard focus row and a static cue on every state; §7.2 is "required; not yet implemented". New gap found in the same section: 1.4.13 (S-06). |
| **F-06** ladder vocabulary | **Mostly fixed, one instance survives.** `FLOW-WORLD-HUD-FALLBACK` → `FLOW-WORLD-HUD-STREAM`, `WORLD_HUD_FALLBACK` → `WORLD_HUD_STREAM`, `MODE-NON-WEBGL-QUICK-ACCESS` → `MODE-SEMANTIC-SHELL` are all done, and D-043 is right that there was no cascade. `MODE_NON_WEBGL_QUICK_ACCESS` survives in a frame name (S-03), and the guard is still scoped to 13 files (M-02). |
| **F-07** route-count contradiction | **Holds fixed.** 34 routes everywhere; validator `COUNTS routes=34`; `/credits` is not an orphan. |
| **F-08** `/credits` actions and language | **Holds fixed.** Both actions present in `primary_next_actions`; B02 requires marked-up list semantics, per-entry `lang`, and in-context link purpose. |
| **F-09** present-indicative equivalence | **Mostly holds**; see M-06. |
| **F-10** `PRIM-001` attribution family | **Holds fixed.** `attribution notice link to /credits` is in the anatomy and `attribution` is in the applicable list; `ROUTE-CREDITS` reuses `TPL-PUBLIC-ABOUT`. |
| **A11Y-UIR-I1-001** conformance target | **Not weakened.** The full wording and the no-current-conformance disclaimer survive in README, contract, `PRIM-001`, `PRIM-058` and all nine batch rows, and `NFR-A11Y-001` now carries it at requirement level. It remains **unenforceable per stream** for every route and every complete process (B-01), which is the same residual iteration 3 recorded against it — not closed. |
| **A11Y-UIR-I1-002** browser/platform baseline | **Weakened.** The formerly silent point is now answered in a way that contradicts §8.2.2 step 1 and reinstates unsupported-client framing (S-04). |
| **A11Y-UIR-I1-003** time-limit specificity | **Not weakened.** Every record still selects an allowed `TL-*`; no record selects `TL-EXCEPTION`; `ROUTE-CREDITS` and `ACT-09` are `TL-NOT-APPLICABLE`, correct for static text and for a preference control. One record/batch mismatch at M-05. Residual: no `NFR-A11Y` row carries 2.2.1 (S-08). |

**On overclaiming.** The correction block appended to iteration 3 is honest, and
the producer-inspection and R-035 notes state the three-FAIL history without
smoothing. Three claims in the current package are not supported by the evidence:
the README "resolvable obligation rather than a claim in prose" (M-03); R-034's
second closure, which asserts a completed rename and an adequate guard (S-03);
and MA-029 item 1's premise that `DS-STREAM-INVARIANT` "is used only as a
positive stream-identical claim, never as an exemption" (B-01).

**On R-036 specifically.** The producer does **not** overstate it in the risk
register — R-036 still says the P0 commitment is written and not discharged, and
"no document may state that the four-stream obligation is met". Moving `ACT-09`
into `B01` is a real reduction and B01's `required_visual_evidence` for it is
the strongest per-stream language in the package. But the reduction is smaller
than it appears, because the evidence it demands cannot be named or validated
downstream (B-02) and two of its four required frames name states that do not
exist for its templates (B-03). **R-036 must stay open, and B-02/B-03 must be
fixed before B01 can discharge any part of it.**

---

## Standing requirement

The D-043 remediation has now had an independent accessibility review, and it
**fails**. **R-035 remains open**; its exit evidence is unchanged and now
requires a clean review of a package that fixes B-01 through B-05.

For the next round, the standing lesson needs one addition. The producer has
correctly recorded that *a passing validator is a determinism check, not a
review*, and that *an assertion that counts rows on a new axis is a placeholder*.
The iteration-4 addition is: **an assertion that classifies records by a proxy
enforces the proxy, not the rule.** `delivery-stream-assignment` does not check
what the contract says — whether a record's rendering depends on the canvas or on
the shell hosting the stream control — it checks a five-value list of state
profiles, and then *forbids* the correct assignment everywhere else. Every
remaining escape in this package is of that shape: a rule stated in prose, a
proxy asserted in code, and the gap between them holding the defect.

Two structural recommendations, offered as findings rather than instructions:

1. **Make the invariance claim earn itself.** `DS-STREAM-INVARIANT` should be
   selectable only by a record that declares *no* immersive representation and
   depends on no primitive with per-stream variants — both are already machine
   checkable from `immersive_stream_representation` and
   `PRIM-001.required_variants`. On the current data that condition is true for
   zero routes.
2. **Give the stream axis a downstream existence** — a `stream_id` in the
   evidence manifest, a stream token in `EC-08`, an `EC-*` rule checking it
   against `required_values`, and a `STATE-STREAM-CHANGED` /
   `STATE-PREFERENCE-WRITE-FAILED` value in `SP-NAVIGATION` — before B01 is
   released and metered external calls are spent on frames that cannot be
   validated.

**This package is not clean. B01 should not be released on it.**
