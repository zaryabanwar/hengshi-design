# Accessibility Audit — Delivery-Stream Evidence Model as implemented under D-045 (iteration 5)

**Review date:** 2026-09-06
**Packages under review:** `docs/phase-1-ui-reference-design` at design freeze
aggregate
`0AA83FD298ABB12A96782205996EB3783BF8E80E11AD1B2BE44473F2E87EB536`
(recomputed by this reviewer from a fresh validator run; it matches the value
recorded at D-045), and `docs/phase-1-ui-reference-production`
(`RESULT=PASS PASS_COUNT=165 FAIL_COUNT=0`, recomputed; it matches).
**Reviewer:** independent accessibility review agent. I did not author any
material under review, I am not the producer, and I have not communicated with
the design reviewer running concurrently. Constitution 2.0.0 principle VII.
**Authority I audit against, and may not overrule:**
`accessibility/DELIVERY_STREAM_ACCESSIBILITY_OBLIGATIONS.md` [PROPOSED, accepted
at D-045]; `DELIVERY_STREAM_EVIDENCE_MODEL.md` [PROPOSED, accepted at D-045];
`DECISIONS.md` D-045 and its seven founder resolutions.

**Verdict: FAIL.**

**Conformance target reviewed against:** WCAG 2.2 Level AA for every applicable
full page and every complete process, including represented third-party steps,
holding independently within each of the four peer delivery streams. No current
conformance is claimed by either package and none is claimed here. Nothing is
built. This reviews whether the specification is complete, testable, and free of
unsupported conformance claims. I found no conformance claim that has crept in;
see "On overclaiming".

> Both validators reproduce exactly: design `PASS_COUNT=201 FAIL_COUNT=0` with
> the D-045 aggregate, production `PASS_COUNT=165 FAIL_COUNT=0`. Per the brief
> and per the producer's own recorded lesson, this is a determinism check and not
> evidence of correctness. It is now the **fifth** consecutive round in which
> every finding below was invisible to a clean run (183, 184, 185, 189, now 201).
> The producer's `producer-inspection.md` withdraws the "no unresolved producer
> finding" sentence and records six results as observations rather than repairs.
> That disclosure is real and is credited below. It is also not sufficient,
> because the disclosures name the *enumeration* facts and not the *consequences*,
> and the consequences are where the defect lives.

---

## Direct answer to the question this round asks

**The D-045 model is materially better than D-043 and the seven founder
resolutions are not implemented faithfully.** Three of them — resolution 2 (the
retained derivation conditions), resolution 3 (the control model), and resolution
4 (the merged frame set) — are implemented in the records that a validator reads
and not in the records that carry the obligation to a human or to a frame.

The defect class the brief names is present and has moved one column to the left.
It is no longer "a value derived from a value that already exists". It is now
**an amendment made in a column that no evidence rule consumes**. `A-08` demanded
two states in `state_profile.required_values`; fourteen profiles now carry them;
`N-04(b)` — the accepted normative frame multiplier — reads
`critical_distinct_frame_values`, and **eleven of those fourteen carry zero
stream states there**. The obligation exists, is machine-checked, passes, and
requires nothing to be drawn. That is the same shape as `DS-STREAM-INVARIANT`,
scored against a different column.

The single sentence that summarises this round: **the package now says the right
things in the places a validator looks, and the visitor this amendment exists for
still has no frame drawn in the stream they will actually use, for any process
they will actually complete.**

---

## Blocking findings

### B-01 — the `A-08` amendment was made in the column that generates no evidence; eleven state profiles carry a stream obligation that requires zero frames

`A-08` (`stream-state-availability`, validator lines 525–541) reads
`state_profile.required_values` and nothing else. The eleven profiles the
producer amended "as a derivation, not as a design choice" received
`STATE-STREAM-CHANGED` and `STATE-PREFERENCE-WRITE-FAILED` **only there**.

Recomputed over `responsive-state-mode-matrix.csv`, counting the four stream
states in each column:

| State profile | in `required_values` | in `critical_distinct_frame_values` |
|---|---|---|
| `SP-NAVIGATION` | 4 | **4** |
| `SP-WORLD` | 3 | 1 |
| `SP-FIRST-VISIT` | 3 | 1 |
| `SP-RETURN-VISIT` | 3 | **0** |
| `SP-BOOKING` | 2 | **0** |
| `SP-CONTACT` | 2 | **0** |
| `SP-AI` | 2 | **0** |
| `SP-HANDOFF-MEDIA` | 2 | **0** |
| `SP-SYSTEM-RECOVERY` | 2 | **0** |
| `SP-PUBLIC-DOCUMENT` / `-COLLECTION` / `-DETAIL` | 2 each | **0** each |
| `SP-EVIDENCE-COLLECTION` / `-DETAIL` | 2 each | **0** each |

`N-04(b)` computes a record's per-stream frame set as the baseline per stream
plus `criticalStates(T.state_profile) ∩ ⋃criticalStates(DS-S-*)`, and
`criticalStates` is `critical_distinct_frame_values`. Therefore:

- A visitor who changes stream **mid-booking** hits `SP-BOOKING`'s
  `STATE-STREAM-CHANGED`. Required frames in any stream: **zero**.
- The same for `/contact`, the AI concierge, human handoff and media opt-in, and
  system recovery. These are exactly the five complete processes `OBL-INV-02` and
  `T-STREAM-07` name, and exactly the surfaces `NFR-A11Y-001`'s "every complete
  process" reaches.
- **Founder resolution 6 (`G-7`, process state survives a stream change) therefore
  evidences nothing.** `FR-3D-016` is P0, traces to `SP-BOOKING`,
  `TPL-BOOKING-VERIFICATION` and `TPL-BOOKING-AVAILABILITY`, and generates no
  required frame in any stream because `SP-BOOKING` carries the state in the
  wrong column.

This is not a producer slip that a reviewer should quietly fix. It is the
producer's disclosed finding 3 ("`A-08` implicates eleven state profiles the
migration table did not enumerate") with its consequence unstated. The
enumeration was disclosed. The fact that the enumeration buys nothing was not.

**Why it is blocking.** Per-stream contrast, focus order, target size and reading
order are properties of a rendering (`OBL-INV-03`). An obligation that names no
rendering discharges nothing, and `A-08` passing tells a future reviewer that it
has been handled.

**What would close it.** Either the stream states become critical values of every
profile that requires them, or the specification states — in the accepted model,
not in a validator comment — which of the two columns carries the per-stream
obligation and why eleven profiles are exempt from drawing it. The second is a
design decision and is not the producer's to take.

### B-02 — `STATE-PREFERENCE-READ-FAILED` and `STATE-STREAM-CEILING-REFUSED` were created and orphaned in the same slice

Both states are required by `OBL-STATE-04` and `OBL-STATE-05`. Both now exist.
Searched across `docs/` (excluding this review directory, the two accepted
specifications, and prior reviews), each appears in **exactly one file**:

```
STATE-PREFERENCE-READ-FAILED   → responsive-state-mode-matrix.csv   (only)
STATE-STREAM-CEILING-REFUSED   → responsive-state-mode-matrix.csv   (only)
```

By contrast `STATE-STREAM-CHANGED` appears in eight files and
`STATE-PREFERENCE-WRITE-FAILED` in five.

So the two new states are:

- required by **no** validator assertion (`A-08`'s `$requiredStreamStates` is the
  two older states only);
- named in **no** batch's `required_visual_evidence`;
- referenced by **no** traceability row;
- carried by **no** requirement in the SRS (there is no read-failure or
  ceiling-refusal requirement row at all);
- exercised by **no** test.

They are inert on the day they were created. `OBL-STATE-04`'s human consequence —
a visitor whose stored preference cannot be read is silently put in a stream they
did not choose — and `OBL-STATE-05`'s — the control misreports its own value
after refusing a request above the ceiling, a 4.1.2 failure — are both
unaddressed by anything a reviewer or a producer will ever be asked to look at.

**Why it is blocking.** This is `R-037`'s inert-column defect at the level of a
state token, produced while implementing the remedy for it. The producer's
`INERT-REPORT` machinery detects inert *columns* and cannot see an inert *value*.

### B-03 — `B01.required_visual_evidence` omits five of the six net-new frames the accepted specification declared irreducible, including the one it named as most important

Founder resolution 4: "the union of both authors' required frames **is** the
evidence obligation." Part 7 of the accepted obligations enumerates 13 frames, 7
existing and 6 net new. Checked line by line against `design-batch-plan.csv`
`B01.required_visual_evidence`:

| # | Frame | Net new? | In `B01`? |
|---|---|---|---|
| 1–4 | Control reporting each stream as in force | existing | **Yes** |
| 5 | Control reachable at `VP-320` in `S-SEMANTIC` through the narrow disclosure | **new** | **No** — `B01` says only "Complete VP-320 and VP-DESKTOP shell frames; narrow disclosure", which is the pre-existing generic shell requirement and is not stream-bound |
| 6 | Control focused, advisement rendered in place, visible indicator, nothing obscuring | existing | **Partial** — the advisement and activation model are required; the focus indicator and the 2.4.11 "nothing obscuring" condition are not |
| 7 | `STATE-STREAM-CHANGED`, same shell, four streams | existing | **Yes** |
| 8 | **Boundary arrival** — incoming semantic shell immediately after crossing from a 3D stream | **new** | **No** |
| 9 | Nearest-ancestor entry showing the substitution statement | **new** | **No** |
| 10 | `STATE-PREFERENCE-WRITE-FAILED`, four streams | existing | **Yes** |
| 11 | `STATE-PREFERENCE-READ-FAILED` | **new** | **No** |
| 12 | `STATE-STREAM-CEILING-REFUSED` | **new** | **No** |
| 13 | `MODE-FORCED-COLORS` on the control in `S-SEMANTIC` | **new** | **No** — `B01` requires generic "forced-colors grayscale unavailable font/image" evidence, not bound to the control or to `S-SEMANTIC` |

Frame **8** is the one the accepted specification says it "most insists on" and
identifies as the single frame whose absence leaves the amendment's primary
beneficiary — the screen-reader user in the World who chooses `S-SEMANTIC` —
entirely unevidenced. It is not required by `B01`, by any other batch, or by any
assertion. Iteration 4's **B-03** was precisely this. It is not closed.

I record the mitigating fact plainly: `B01.status = future_not_authorized` and
`ma_025_disposition` agrees across both plan files, so nothing is being captured
against this list today. That is why this is a specification finding and not an
execution one. It is still blocking, because the list is what a future producer
will execute and the reviewer who accepts the batch will read it as the union
D-045 accepted.

### B-04 — founder resolution 3 is recorded in prose and not in the records `OBL-CTRL-01` and `-02` name; the advisement is weakened in all four loci

Three separate defects, all in the control model.

**(a) `required_anatomy` still carries the single token.** `OBL-CTRL-01`'s record
clause is explicit: `PRIM-001` anatomy must carry "the control's role and its
submit affordance … as named anatomy, **not as the single token
`delivery stream control`**", and "`PRIM-042`, `PRIM-043`, `PRIM-044`
identically". Current state:

```
PRIM-001.required_anatomy  … ;page status region;…;delivery stream control
PRIM-042.required_anatomy  … ;delivery stream control;…
PRIM-043.required_anatomy  … ;delivery stream control;…
PRIM-044.required_anatomy  … ;delivery stream control;…
```

Four for four, the exact token the obligation names as the thing that must
change. `A-07` and `A-08` both key on the regex `delivery stream control`, so the
token is load-bearing for the validator and would have to be retained alongside
the decomposition — but nothing prevented adding `stream radio group` and
`stream apply control` beside it, and nothing did.

**(b) The in-force / pending distinction exists nowhere in any record.**
Resolution 3 and `OBL-CTRL-02` require that the group name report the **in-force**
stream while the checked radio is the **pending** value, and that the two be
programmatically distinguishable. Searched across the style guide, the SRS, the
UX package and every design-package CSV: no record distinguishes them. Every
locus uses the single old formulation:

- §8.2.4 — "The control reports its **current** stream as part of its accessible
  name."
- `NFR-A11Y-004` — "reports its **current value** in its accessible name."
- `STATES_AND_RECOVERY.md` `ACT-09` — "applied and reported in the control's
  accessible name."
- `COV-ACT-09` — "the control reports the new current stream in its accessible
  name."
- `PRIM-001.transactional_or_content_states` — `…;current;stream-selected;…`.
  `OBL-CTRL-02` names this column specifically ("must gain the current/pending
  distinction"). `stream-selected` is not a pending value; read plainly it is the
  applied one, and a reader cannot tell which of `current` and `stream-selected`
  is which.

Apply `OBL-CTRL-02`'s reviewer test — *from the record alone, state what a screen
reader announces on entering the group, on arrowing to the second option, and on
reaching the submit button.* Question 2 has no answer in any record. Unmet.

**(c) The advisement is weakened from three requirements to one, identically, in
four places.** `OBL-ADV-01` and resolution 3 require persistent visible text
(i) **inside the group**, (ii) **preceding the submit in reading order and in
visual order**, and (iii) **programmatically associated with both the group and
the button**. Every implementing record says instead:

- §8.2.4 — "visible text **adjacent to** the control";
- `NFR-A11Y-004` — "visible text **adjacent to** the control";
- `UXTEST-046` — "visible text **adjacent to** the control";
- `TR-REQ-103` — "the advisement as visible text adjacent to t[he control]".

"Adjacent" establishes neither containment, nor order, nor association. All three
are the parts that make the obligation testable; "visible" alone was never the
contested part. `B01` is the one record that does better ("The visible advance
advisement and the radio-group-plus-Apply activation model, both proven **before**
the control is operated"), and `B01` is held.

**Why it is blocking.** 3.2.2 and 4.1.2 are the two criteria the entire control
model exists to satisfy, and this is the fifth round in which the record that a
future implementer reads does not say what it must do. The failure mode is the
one `OBL-ADV-01` describes: an advisement placed after the submit button, or
associated with neither, satisfies "adjacent" and reaches the sighted keyboard
user after they have already operated the control.

### B-05 — `OBL-TEST-01` is unmet by an order of magnitude; seven required tests were collapsed into one and the end-to-end test does not exist

The reviewer test is mechanical and I ran it:

```
$ grep -i stream docs/phase-1-ux-architecture/CONTENT_ANALYTICS_TESTS.md | wc -l
2                       # required: matches in at least SEVEN DISTINCT TESTS
```

The two lines are `CN-012` (a content row, not a test) and `UXTEST-046`. **One
test.** `COV-ACT-09.linked_tests` = `UXTEST-007;UXTEST-025;UXTEST-046`; the
obligation requires it to name at least four stream tests, and `UXTEST-007` and
`UXTEST-025` are the two the accepted specification already ruled inadequate
("neither touches stream selection, keyboard operability, the accessible name,
the announcement, the advisement, or the boundary crossing").

`UXTEST-046` is a genuinely good row and covers a real fraction of T-STREAM-01,
-03, -04 and -05. What it does not contain, checked clause by clause against the
seven required tests:

- **T-STREAM-02** — no keyboard trap (2.1.2); visible focus indicator on every
  part of the control (2.4.7); nothing obscures the focused control (2.4.11);
  `Escape` does not navigate. **None of the four appears.**
- **T-STREAM-05** — the incoming status region **present and empty before the
  message**; the announcement naming **stream and location**; the canvas added
  **last**; nearest-ancestor entry stating the substitution. **None of the four
  appears.** `UXTEST-046` covers only tree ordering of the two shells and the
  focus destination.
- **T-STREAM-06** — read failure and ceiling refusal. **Absent** (consistent with
  B-02).
- **T-STREAM-07** — each complete process (booking, contact, AI concierge, human
  handoff, media opt-in) completed start to finish in `S-SEMANTIC` only, keyboard
  only, and again with a screen reader. **Absent entirely, at any level.**

T-STREAM-07 is the test that would discharge `NFR-A11Y-001`'s "every complete
process" against `NFR-A11Y-003`'s peer-stream claim. It is `R-036`'s discharge.
Its absence is why `R-036` cannot close, and `R-036` is correctly recorded as
still open.

**Why it is blocking.** Seven distinct verifications folded into one prose cell
cannot fail independently. A tester reporting "UXTEST-046: pass" has reported one
bit about eleven behaviours. This is the standing lesson of iteration 4 —
*an assertion that classifies records by a proxy enforces the proxy, not the
rule* — restated at test level.

### B-06 — founder resolution 2's stated safeguard does not exist in the validator source, and `A-06` cannot fail

Resolution 2 reads: the `OBL-INV-01` derivation conditions "are retained as the
reasoning that justifies the deletion and **are recorded in the validator source
beside the assertion**, so a future record that would qualify is recognisable
without the category existing to absorb it."

The comment beside `A-06` (lines 480–486) records the deletion rationale and
restates the obligation triple. **It does not record conditions 1–4.** Grepping
the whole validator for the conditions' distinctive content —
`immersive_stream_representation` empty, no dependency declaring `stream_*`
variants, `mode_profile` not requiring `MODE-SEMANTIC-SHELL`, `state_profile`
carrying no stream-relative state — returns nothing. The stated purpose of the
retention therefore fails: a future record that would qualify as invariant is
**not** recognisable from the source, and the reasoning a later maintainer would
need in order to know why the category was deleted is not there.

Separately, `A-06` as written cannot fail:

```powershell
foreach ($s in $templatePresence[$t.template_id]) {
    $key = "{0}|{1}|{2}" -f $t.template_id, $c, $s
    if (@($key -split '\|')[2] -cnotin $legalStreams) { $a06.Add(…) }   # unreachable
    if (-not $obligations.Add($key)) { $a06.Add(…) }                     # dup-token only
}
```

The stream is taken from `templatePresence`, which `A-02` has already constrained
to the legal vocabulary, so the `not-single-stream` branch is unreachable by
construction. The `collapsed` branch fires only if a state profile lists the same
token twice in `required_values`, which `Split-List` plus the CSV schema make a
typo class, not a modelling class. `A-06` is an enumeration property of a
`HashSet`, not a test of the data.

And it reads `required_values` where `N-04` reads
`critical_distinct_frame_values`. **The package therefore carries two divergent
obligation sets and machine-checks the vacuous one** — which is the direct cause
of B-01 going unnoticed.

**Why it is blocking.** D-045 deleted a category on the express undertaking that
the test survives as an assertion. The assertion that survives cannot fail, and
the reasoning that was to survive beside it did not.

### B-07 — the two `OBL-BND-03` gaps are retained verbatim, the `OBL-BND-04` ordering is not stated, `OBL-ANN-01`'s empty-region-first rule is absent, and the `Escape` conflict is unresolved

Four unmet obligations in one section, all in §8.2.4 and its records.

**(a) `OBL-BND-03(1)`.** The obligation says, of the nearest-ancestor case:
*"'And says so' is not a requirement; it is a gap with a sentence around it"*, and
requires a named surface, a named politeness level, a stated relationship to
focus, and a wording constraint. §8.2.4 currently reads: "A location with no
mapping enters at the nearest ancestor that has one, **and says so**." The exact
phrase the obligation quotes as insufficient is retained, unchanged.

**(b) `OBL-BND-03(2)`.** The obligation says the semantic→World map "currently
maps 'every semantic route *that is reachable in the World*', which leaves routes
that are not", and that the rule for unmapped semantic routes "must be stated,
not implied". §8.2.4 currently reads: "every semantic route **that is reachable
in the World** has one location." Unchanged.

**(c) `OBL-BND-04` and `OBL-ANN-01(2)`.** The five-step tree ordering must be
stated as a sequence and annotated on the boundary frame. §8.2.4 states two of
the five (outgoing removed before incoming added; canvas added after the incoming
shell is announced). The three that carry the accessibility weight are absent:
the incoming status region **present and empty** before the message is written;
focus set **after** the region exists; the announcement written as a **separate
step**. `OBL-ANN-01`'s reviewer test — *name the region and state the ordering of
the three steps* — cannot be answered from any record. `PRIM-001` names the
`page status region` as anatomy but nothing states it as the carrier or as
present-and-empty-first. Since B-03 shows there is no boundary frame, there is
also nothing to annotate.

**(d) `OBL-CTRL-04`, the `Escape` conflict.** §7.2 still reads
"**Escape:** Close panel / go back", unchanged, and §8.2.4 does not mention
`Escape` at all. The obligation names §7.2 as a record that must carry the
resolution, and its reviewer test is *read §7.2 and §8.2.4 together and state
what happens*. The answer today is that a keyboard user backing out of the stream
control in a World stream navigates out of the room. Unmet.

### B-08 — no requirement anywhere names 2.4.11, 1.4.13, or 2.2.1

`OBL-TRACE-02` requires requirement-level rows for the boundary crossing,
persistence failure modes, **2.4.11 Focus Not Obscured (Minimum)**, **1.4.13
Content on Hover or Focus**, **2.2.1 Timing Adjustable**, the role/activation
model, and the visible advisement. Searching `Hengshi_Design_SRS_v3.md` for
`2.4.11`, `1.4.13`, `2.2.1`, `Focus Not Obscured`, `Content on Hover` and
`Timing Adjustable` returns **zero matches**.

- **2.4.11** is new at AA in WCAG 2.2 and is the criterion most directly at risk
  from a persistent HUD over a canvas — the exact geometry of the stream control
  in the three 3D streams. `OBL-CTRL-04` says so in terms: "`NFR-A11Y` currently
  carries no 2.4.11 row and must gain one."
- **1.4.13** is engaged by §4.1's hotspot labels expanding on hover *and* on
  focus. Dismissible, hoverable and persistent are unspecified, and the obvious
  dismissal key is bound by §7.2 to navigation — the same conflict as B-07(d).
- **2.2.1** has an elaborate `TL-*` apparatus in the design package (four
  profiles, `time_limit_branch` on three record files, `EC-12` annotation) and no
  requirement-level home at all. Gate `G-5` records that `time_limit_branch` is a
  total function of `state_profile` and was deliberately not fixed, so the branch
  selection — which *is* the SC 2.2.1 judgement — has never been made by a person
  for any of 40 templates, 34 routes, or 89 flow rows.

`OBL-TRACE-01`'s two count thresholds are met (7 `NFR-A11Y` rows, 7 `FR-3D-01`
rows, both above the minima). `OBL-TRACE-02`'s substance is not. The counts
passing while the coverage does not is, again, the proxy lesson; see S-09.

---

## Significant findings

### S-01 — `R-039` / gate `G-6`: a conforming stream control cannot be specified from the design system as it stands

`DESIGN_SYSTEM_IMPLICATIONS.md` was deliberately left untouched with its freeze
hash intact (`0E9FC68C…B763`, verified unchanged in this run), and `R-039` records
the gap. Assessing the accessibility consequence honestly, as asked:

The word "stream" occurs twice in the file. One occurrence is the amendment note;
the other is "World stream" in an unrelated coverage sentence. There is no stream
axis, no stream-control component, no four stream tokens, and no 3D focus-ring
token.

**Can a conforming stream control be specified without them?** Partly, and the
part that fails is the part that matters:

- *Specifiable without the design system:* role, activation model, group and
  option names, the advisement's text and position, the announcement, the tree
  ordering. All of these are structure and behaviour, and `OBL-CTRL-01` is right
  that a picture cannot establish them.
- *Not specifiable without it:* **1.4.3**, **1.4.11** and **2.4.7** for the
  control *in each stream's own rendering*. Contrast and focus-indicator
  conformance are token-level facts. With no per-stream tokens, "the focus
  indicator meets the obligation in each stream's own rendering" resolves to
  nothing a producer can draw or a reviewer can measure, and the producer would
  have to invent four token sets at capture time — which is the producer
  authoring the model D-045 barred it from authoring.
- **The 3D focus-ring case is worse than a gap.** `NFR-A11Y-005` requires
  "≥3:1 against every adjacent scene colour", and `OBL-CTRL-04` already records
  that this has no sampling method, no adjacency definition, and no measurement
  procedure, so it can be neither passed nor failed. With no 3D focus-ring token
  either, there is nothing to sample *and* no method to sample it with. This is
  the correct place to say plainly: **the 3D-stream focus obligation is currently
  unfalsifiable**, and `R-039` resolving "before the first metered Figma call" is
  the right sequencing only if the resolution includes the sampling method, not
  just the tokens.

I agree with the founder resolution that the file should not have been edited by
the producer, and with the reversion of the one edit made during the slice.

### S-02 — `A-14` drops the state coordinate from the obliged set and is currently vacuous on two independent grounds

The accepted model's obliged set is the `(template, stream-critical coordinate,
stream)` triple. `A-14` builds `(batch | template | stream)`:

```powershell
foreach ($t in (Get-BatchTemplateIds …)) {
    foreach ($s in $presenceByTemplate[$t]) { $obligedList.Add("{0}|{1}|{2}" -f $row.batch_id, $t, $s) }
}
```

One frame per template per stream discharges it. That is the aggregate-evidence
shape `OBL-INV-03` forbids: a single `STATE-REST` frame per stream would satisfy
`A-14` while `STATE-STREAM-CHANGED`, `STATE-PREFERENCE-WRITE-FAILED` and the
boundary states go unevidenced.

Its pass condition is `($unmet.Count -eq 0 -or $executable.Count -eq 0)` where
`$executable` is the batches carrying `ma_025_disposition = authorized_pilot`.
Under founder resolution 5 no batch carries it, so the second disjunct is true
unconditionally and the assertion passes whatever the data says. Answering the
brief's question directly: **this is a legitimate lifecycle condition today and a
structurally unsatisfiable one tomorrow.** It is legitimate because nothing may
be captured while B01 is held. It becomes a defect the moment authorization
arrives, because at that instant the assertion switches from "always true" to
"discharged by one frame per template per stream", and it never passes through a
state in which it demands the per-state coordinate the model specifies. `R-041`
correctly records the observation; it does not record that the escape survives
authorization.

### S-03 — `stream_disposition` is constant across all nine batch rows; the deferral mechanism is unexercised on live data

`INERT-REPORT batch-production-plan.csv:stream_disposition distinct-values=1
rows=9`. `EC-33`'s `deferred_<BATCH>` form — the mechanism by which B07's World
deferral was to be expressed, and the only way the production package can say
"this stream's evidence lives in another batch" — is used nowhere. A column with
one value across every row is a column no one has judged. Recorded honestly by
the producer; the accessibility consequence is that the B01/B07 split of `ACT-09`
evidence (iteration-4 **M-04**) is still not expressed anywhere it can be checked.

### S-04 — `COV-ACT-09` is profiled as a World surface, which contradicts gate `G-1`

`COV-ACT-09` selects `viewport_profile = VP-WORLD` and `mode_profile = MP-WORLD`.
Under founder resolution 1 the stream control's first and primary home is
`ROUTE-HOME`'s **non-World** shell, in every stream including `S-HIGH`, and
§8.2.5 says so explicitly. Profiling the action as World-shaped means its
viewport and mode obligations are the World's; `MP-WORLD` is also the profile
that excludes `MODE-PRINT` and required the `A-09` precedence sentence. The
control's own `S-SEMANTIC` obligations — where there is no HUD and no canvas —
are inherited from a profile written for a surface that does not exist in that
stream. This is the residue of the pre-G-1 conflation surviving in the coverage
row after the prose was corrected.

### S-05 — twenty-two inert judgement columns; only one can fail, and the ones that decide accessibility captures are among the inert

`A-11` writes all findings as `INERT-REPORT` lines, then hard-fails on exactly
one:

```powershell
$streamInert = @($inertFound | Where-Object { $_ -match 'stream_presence' })
Assert-True ($streamInert.Count -eq 0) 'inert-column-detection' …
```

Twenty-one others are reported and pass. Accessibility-relevant members of that
set: `mode_profile <- state_profile`, `mode_profile <- route_family`, and
`viewport_profile <- route_family / state_profile / mode_profile`. Those are the
axes that decide whether `MODE-FORCED-COLORS`, `MODE-PRINT`, `MODE-SCREEN-READER`
and `VP-ZOOM-400` captures are required for a given record — and they are
derived, so no person chose them for any record. Plus `time_limit_branch` in all
three record files, per `G-5` and B-08 above. The producer discloses the count
and discloses that `A-11`'s determiner set is its own reading of an
underspecified instruction (`R-037`, disclosed finding 2). Both disclosures are
correct and neither closes the exposure.

### S-06 — `stream_presence` is weakly load-bearing; the specific check the model demanded passes, and the column is close to a function of two existing ones

62 primitives: 50 declare all four streams, 9 are `STREAM-SCOPE-EXCLUDED`
(`PRIM-046/047/048/049/051/052/053/054/055`), 3 declare three streams
(`PRIM-042/043/044`).

The reviewer check the accepted model demanded — that `PRIM-042`, `PRIM-043` and
`PRIM-044`, the World overlay primitives, must **not** claim `S-SEMANTIC` —
**passes**, correctly and non-trivially. That is a real human judgement recorded
in a column, and it is the strongest single piece of evidence that the D-045
locus change was worth making.

Against that: the 62 values track §4.1's rule plus `primitive_category` almost
exactly, and `A-11` clears the column only because two categories split
(`PRIM-050` and `PRIM-056` are all-four inside otherwise-excluded categories).
Answering the brief's question directly — **the inert defect has not returned
wearing a new column name, but the column is one categorisation away from being
derivable, and nothing in the model prevents that drift.** Nine of the 62
decisions are real; 53 follow from the category.

### S-07 — the exclusion is not closed under union, so staff, publication and audit templates carry four-stream obligations

`presence(T)` is a union fold over `primitive_dependencies`, so one non-excluded
dependency pulls a staff template to all four public streams:
`TPL-STAFF-AUTH` via `PRIM-006`, `TPL-PUBLICATION-EDITOR` via `PRIM-003`, and
others. `A-07` separately *skips* those templates from the host-shell rule via
`$isExcludedSurface` (any dependency with an empty presence set). So the same
template is simultaneously "excluded, skip the host-shell check" and "present in
four streams, obliged under `A-14`". The producer discloses this as finding 4
("§4.2's fold has no exclusion for them"). The accessibility consequence is
modest — these are authenticated staff surfaces outside the public conformance
target — but the inconsistency means `A-14`'s obliged set is inflated by
templates whose stream obligations nobody intends, which makes the set's size
uninformative.

### S-08 — `OBL-INV-02` is satisfied by computation and cannot be answered by pointing at a record

Under D-045 stream facts are computed at the template and inherited **unstored**
at route and flow. That is the accepted model and I do not reopen it. Its
consequence for `OBL-INV-02` — "`S-SEMANTIC` evidence must attach to routes,
templates and complete processes **by name**" — is that no route row and no flow
row names `S-SEMANTIC`, and `A-01` now actively forbids a stream column on those
files. `OBL-INV-02`'s named mechanism (`stream_profile` on the three coverage
CSVs) was superseded, legitimately. What was not supplied in its place is a way
for a reviewer to *answer* the obligation without re-running the validator: the
per-flow `S-SEMANTIC` obligation exists only as the output of a fold. Combined
with B-01, the fold's output for every complete-process flow is a presence set
with no required stream-state frame behind it.

### S-09 — the traceability thresholds pass while the per-row record sets specified in the same table do not

`OBL-TRACE-01` gives two count thresholds and a twelve-row table of
`contract_records` that each row must carry. The thresholds pass (7 and 7). The
table does not:

| Row | Required records | Present |
|---|---|---|
| `NFR-A11Y-004` (`TR-REQ-103`) | `PRIM-001; PRIM-042; PRIM-043; PRIM-044; COV-ACT-09; B01` | `COV-ACT-09; PRIM-001; TPL-GLOBAL-NAVIGATION; TPL-WORLD-HUD; TPL-QUICK-ACCESS-RECOVERY` — **missing `PRIM-042/043/044`, `B01`** |
| `FR-3D-014` (`TR-REQ-111`) | `PRIM-001; PRIM-042; PRIM-043; PRIM-044; COV-ACT-09; B01` | `PRIM-001; COV-ACT-09; STATE-PREFERENCE-WRITE-FAILED` — **missing `PRIM-042/043/044`, `B01`** |

The reviewer test given in the obligation is a `grep` count, and the `grep` count
is what was satisfied. This is the iteration-4 standing lesson recurring at the
traceability layer, and it is the mildest instance in this report precisely
because it is visible.

### S-10 — `R-034` survives immediately outside `A-16`'s scan roots, this time inside a frozen, validated package

`A-16` is a genuine improvement (see credits) and its three-package union closes
iteration-4 **M-02** inside the design, production and UX packages: `ACT-06` now
reads "Enter the World (visitor-elected)" and `UX_ARCHITECTURE.md` carries no
`optional`/`elective`/`fallback`/`degrad*` framing. Outside those roots, in the
**accepted** `docs/phase-1-brand-identity` package that implementation inherits:

```
07-accessibility-seo-and-applications.md:121  "optional immersive choice → booking action"
traceability.csv:9                            "equivalent to optional immersive expression"
validation/audit-identity-board.mjs:175,206   'Review optional immersive principles'   (expected-string literal)
validation/browser-audit-report.json          the same string, three times
```

The last two are the hard case and are worth stating precisely: the abolished
phrasing is baked into a validator's expected-string literal and into its frozen
report, so correcting the prose would fail that package's own audit. `R-034`
cannot be closed by widening `A-16` again; it needs a decision about the brand
package. This is the fourth consecutive round in which `R-034` has been reported
closed or nearly closed and a surviving instance has been found one scope
boundary away. `R-034` is correctly recorded as not closed.

---

## Minor findings

- **M-01** — §8.2's opening retains present-indicative equivalence about an
  unbuilt system ("Every route reachable in `S-HIGH` **is** reachable in
  `S-SEMANTIC` by an equivalent named action") in a document headed
  `Status: Active`. Iteration-4 **M-06**, unchanged. Read as a requirement it is
  fine; read as a status statement it is the `F-09` shape.
- **M-02** — `A-09` consults only `MP-WORLD.exception_rule` for the precedence
  sentence, regardless of which mode profile issued the exclusion. If
  `MP-PUBLIC` or `MP-INTERACTIVE` ever excludes a mode a stream requires,
  `MP-WORLD`'s sentence would resolve it. Correct today because only `MP-WORLD`
  and `MP-STAFF` carry exclusions that intersect; fragile by construction.
- **M-03** — `DESIGN_SYSTEM_IMPLICATIONS.md`'s amendment note reads "the delivery
  stream axis, the ACT-09 stream control, and the peer-framing renames were added
  after it". On the intended reading this explains why the frozen file predates
  them; on a fast reading it says the file contains them, which it does not.
  Given `R-039`, the sentence should name the gap rather than describe the
  timeline.
- **M-04** — `PRIM-042`, `PRIM-043` and `PRIM-044` declare no `stream_*` values
  in `required_variants` while `PRIM-001` declares all four. The three World
  primitives are precisely where per-stream rendering differs most, and the
  variant axis that would require it is absent from them.
- **M-05** — `A-15`'s stream-token guard matches only the `EC-08` segment
  position (`_(STREAM[_-][A-Z0-9]+)[_-]V\d{2}`). The scope note explaining why
  broader matching was rejected is sound, and I record the residual: an abolished
  stream spelling outside that position is not caught by `A-15` and is caught by
  `A-16` only if it matches one of nine framing alternatives.
- **M-06** — `A-01`'s token scan deliberately excludes `producer-inspection.md`,
  `validation-report.md` and the script itself. The exclusions are reasoned and I
  do not object; I note that the exempt class in `A-16` additionally covers any
  file in a `reviews`/`accessibility` directory, which is correct for this
  document and means the two accepted specifications and every audit are outside
  every framing guard. Nothing currently hides there.

---

## Obligation-by-obligation result

| Obligation | Result | Where |
|---|---|---|
| `OBL-INV-01` | **Superseded and partly unmet** — category deleted per resolution 2; conditions not recorded in source | B-06 |
| `OBL-INV-02` | **Met in form, unanswerable in practice** | S-08, B-01 |
| `OBL-INV-03` | **At risk** — `A-14` permits aggregate discharge | S-02 |
| `OBL-GRAM-01` | **Met** — `EC-08` carries a mandatory `STREAM_*` segment | — |
| `OBL-GRAM-02` | **Met** — `A-12` resolves the token against `stream_id`, four negative fixtures | credits |
| `OBL-GRAM-03` | **Unmet** — design-system handoff carries no stream axis | S-01 |
| `OBL-CTRL-01` | **Unmet** in the named records; met in §8.2.4 and `FR-3D-014` | B-04(a) |
| `OBL-CTRL-02` | **Unmet** — no record distinguishes in-force from pending | B-04(b) |
| `OBL-CTRL-03` | **Partly met** — presence and reachability stated; the `VP-320`/`S-SEMANTIC` frame is unnamed | B-03 frame 5 |
| `OBL-CTRL-04` | **Unmet** — no 2.4.11 row, `Escape` conflict live | B-07(d), B-08 |
| `OBL-CTRL-05` | **Met** — `DS-S-SEMANTIC.exception_rule` retained verbatim and unweakened | credits |
| `OBL-CTRL-06` | **Unmet** — no forced-colors evidence bound to the control in `S-SEMANTIC` | B-03 frame 13 |
| `OBL-ADV-01` | **Unmet** — "adjacent" in all four loci; `PRIM-001` does not carry it | B-04(c) |
| `OBL-ANN-01` | **Partly unmet** — polite region named; empty-first and three-step ordering absent | B-07(c) |
| `OBL-BND-01` | **Partly unmet** — destination named; visible indication and ordering absent; no frame | B-03, B-07 |
| `OBL-BND-02` | **Unmet** — no record states that the arrival announcement names a location | B-07(c) |
| `OBL-BND-03` | **Unmet** — both quoted gaps retained verbatim; (3) met by `G-7` prose only | B-07(a)(b), B-01 |
| `OBL-BND-04` | **Unmet** — two of five steps stated, none annotated | B-07(c) |
| `OBL-STATE-01` | **Met for `SP-NAVIGATION`; defeated elsewhere** by the column choice | B-01 |
| `OBL-STATE-02` | **Met** — `STATE-STREAM-CHANGED` on `TPL-GLOBAL-NAVIGATION`, four streams, in `B01` | credits |
| `OBL-STATE-03` | **Met** — `STATE-PREFERENCE-WRITE-FAILED` likewise | credits |
| `OBL-STATE-04` | **Unmet** — state exists in one file and nowhere else | B-02 |
| `OBL-STATE-05` | **Unmet** — likewise | B-02 |
| `OBL-TRACE-01` | **Thresholds met, table unmet** | S-09 |
| `OBL-TRACE-02` | **Unmet** — 2.4.11, 1.4.13, 2.2.1 have no requirement | B-08 |
| `OBL-TRACE-03` | **Met** — `FR-3D-013` now carries the boundary case explicitly; one implementation can satisfy both readings | credits |
| `OBL-TEST-01` | **Unmet** — one stream test where seven are required | B-05 |
| Part 7 frame budget | **Unmet** — 5 of 6 net-new frames unnamed | B-03 |

---

## What genuinely improved, and must be credited

This is the first round in which the producer's own inspection record withdraws
its previous clean claim and names six unrepaired results. That is the correct
behaviour under principle VII and it is why several findings above could be
written quickly rather than excavated.

1. **`DS-STREAM-INVARIANT` is gone, and `A-01` guards its return** — including
   the underscore spelling, in data and in normative prose. Iteration-4 **B-01**,
   the round's headline finding, is closed at the category level. The reasoning
   recorded at validator line 292 — "a zero-member guarded category is where an
   unexamined record hides" — is the right lesson correctly stated.
2. **`R-038` was fixed in the open.** The PowerShell comma-vs-`+` precedence
   collapse that left the framing guard silently inert across 56 files is
   documented in full in the validator source and in the validation report rather
   than quietly corrected. `A-16` now asserts **its own alternative count**, which
   is the correct structural remedy: a guard that checks it is still a guard.
3. **`A-10` replaced a vocabulary regex with a token resolution**, forcing
   regeneration of every `baseline_frame_name` and killing the surviving
   `MODE_NON_WEBGL_QUICK_ACCESS`. Iteration-4 **S-03** is closed, and closed by
   changing the *kind* of check rather than by widening the old one.
4. **`MP-WORLD.exception_rule` now states stream-axis precedence explicitly** and
   `A-09` resolves against it. Iteration-4 **S-05** closed.
5. **`DS-S-*.minimum_evidence` is now stream-generic under `N-03`**, with World
   content relocated to `TPL-WORLD-SHELL` and `TPL-WORLD-HUD`. This is what makes
   B01 satisfiable at all, and it is the change D-045 correctly identified as the
   reason the slice is cheaper than releasing B01 as it stood.
6. **`SP-NAVIGATION` carries all four stream states in both columns.** It is the
   one profile done correctly, which is how B-01 was detectable.
7. **§8.2.5 and §8.2.6 are well written.** `G-1`'s separation of stream selection
   from World entry is stated cleanly, with the concrete consequence named
   (`ROUTE-HOME`'s first frame is a non-World shell in every stream including
   `S-HIGH`), and `G-7`'s process-state guarantee names the semantic boundary as
   the case that would otherwise break and refuses the silent-reset option. Both
   sections end by disclaiming conformance. The defect in both is downstream —
   neither generates a frame (B-01, B-03) and neither is tested independently
   (B-05) — not in the prose.
8. **`A-12`'s negative fixtures.** Four abolished forms, including
   `STREAM_FALLBACK` and `STREAM_ALL`, exercised against the grammar with the
   literals assembled at run time so the guard can scan its own source. This is
   the one assertion in either package that is unambiguously load-bearing today
   rather than once evidence exists.
9. **`DS-S-SEMANTIC.exception_rule` retained verbatim and unweakened**, and no
   peer-framing regression anywhere in the three scanned packages.

---

## On overclaiming

I found **no** current-conformance claim in either package. §8.2.4 states
explicitly that 3.2.2, 3.3.7 and 4.1.3 "are evaluated against the implementation,
not against this document"; §8.2.6 repeats it for 3.3.7; all seven `NFR-A11Y-*`
rows are marked `❌ Not implemented`; `B01.validation_and_review` ends "evidence
does not claim current conformance"; `PRIM-001` carries "definition and reference
designs do not establish conformance"; and the accepted obligations document ends
with a standing note that closes nothing. The withdrawn "3.2.2 satisfied by
construction" claim has not returned in any spelling.

The nearest thing to an overclaim is **M-01** (present-indicative equivalence in
§8.2) and **M-03** (the design-system amendment note), and neither is a
conformance claim.

---

## On `R-036`

`R-036` — the `S-SEMANTIC` P0 obligation not discharged — **cannot close on this
package**, and correctly remains open. The specific reason is now narrower than
in iteration 4 and can be stated as a single missing artefact: `T-STREAM-07`.
Until some record requires each of booking, contact, AI concierge, human handoff
and media opt-in to be completed start to finish in `S-SEMANTIC` only, keyboard
only, and again with a screen reader, `NFR-A11Y-003`'s "peer delivery stream
carrying the equivalent core journey" is an assertion about a stream nothing
exercises end to end. B-01 compounds it: even the per-state frames that would
partially stand in for it are not required.

## On `R-035`

`R-035` — unreviewed package — is discharged for the accessibility half by this
document, with a FAIL verdict. It does not close.

---

## Regression check on iteration 4

| ID | Status now |
|---|---|
| **B-01** `DS-STREAM-INVARIANT` is a loophole every route takes | **Closed at the category level.** The profile is deleted, `A-01` guards its return, presence is computed from `stream_presence`. The *shape* recurs one column over — see B-01 above — but the specific finding is closed and closed correctly. |
| **B-02** production package has no stream axis | **Closed.** `EC-08` carries a mandatory `STREAM_*` segment, `stream_id` is a manifest column, `A-12`–`A-15` exist, `A-13` resolves against the accepted design package rather than against the production package's self-description. |
| **B-03** stream-change state does not exist outside the World; boundary crossing has no required frame | **Not closed.** The state now exists in fourteen profiles (progress) and generates a required frame in one (B-01). The boundary frame is still required nowhere (B-03). This is the finding with the longest life in this series. |
| **B-04** advisement placed where most users cannot receive it; activation model never fixed | **Half closed.** The activation model is now normative and correct in §8.2.4 and `FR-3D-014` — a real fix. The advisement is weakened to "adjacent" in all four implementing records and the in-force/pending distinction is absent everywhere (B-04). |
| **B-05** new requirements have no downstream reference | **Closed.** 7 `NFR-A11Y-*` and 7 `FR-3D-01*` traceability rows now exist, `UXTEST-046` exists, `COV-ACT-09` is re-linked. The per-row record sets are incomplete (S-09) and the test count is one where seven are required (B-05), but the requirements are no longer orphaned. |
| **S-01** boundary crossing not testable as written | **Not closed.** B-07. |
| **S-02** step-4 storage: preference can vanish silently | **Partly closed.** `STATE-PREFERENCE-READ-FAILED` now exists — and is orphaned (B-02). §8.2.2's storage paragraph is unchanged and still asserts the consent conclusion; the `/credits` notice still has no named surface. |
| **S-03** `R-034` closed prematurely a second time | **Closed inside the three scanned packages; open outside them.** S-10. Third occurrence of the same pattern. |
| **S-04** `BP-NFR-006` reinstates unsupported-client framing | **Not addressed.** `PRIM-001.responsive_and_mode_obligations` still reads "semantic Quick Access for below-floor or **otherwise unsupported** clients" alongside §8.2.2 step 1, which says a no-WebGL client receives `S-SEMANTIC` as a peer stream, not as an unsupported-client recovery. `A-16`'s nine alternatives do not include "unsupported". |
| **S-05** mode and stream axes conflict with no precedence | **Closed.** `MP-WORLD.exception_rule` states the precedence and `A-09` resolves against it. |
| **S-06** 1.4.13 unaddressed | **Not closed.** B-08. |
| **S-07** `FR-3D-013` / §8.2.4 focus contradiction | **Closed.** `FR-3D-013` now carries the boundary case in the row itself; a single implementation satisfies both. `OBL-TRACE-03` met. |
| **S-08** SRS §5.6 does not cover what the package promises | **Partly closed.** `FR-3D-015`, `FR-3D-016` added and `FR-3D-013`/`-014` narrowed. 2.4.11, 1.4.13 and 2.2.1 still have no home (B-08). |
| **S-09** design-system artifact has no stream axis | **Not closed, and now a founder-tracked risk.** `R-039`, resolution 7. S-01 assesses the consequence. |
| **M-01** Reception surfaces forced onto the invariant profile | **Closed** with B-01. |
| **M-02** degradation vocabulary outside the guard's scope | **Closed in the UX package** (`ACT-06` renamed "Enter the World (visitor-elected)"); **open in the brand-identity package** (S-10). |
| **M-03** README overclaims the `stream_profile` mechanism | **Closed** — the mechanism it described no longer exists. |
| **M-04** `ACT-09` evidence split across authorized and deferred batches without saying so | **Not closed.** `COV-ACT-09` still lists `TPL-GLOBAL-NAVIGATION` (B01) with `TPL-WORLD-HUD` and `TPL-QUICK-ACCESS-RECOVERY` (B07), and `stream_disposition` — the column that exists to express exactly this — is constant (S-03). |
| **M-05** `COV-ACT-09` `TL-NOT-APPLICABLE` vs `B01` `TL-WARN-EXTEND` | **Not closed.** `B01.time_limit_branch_ids = TL-WARN-EXTEND` and `EC-12` still requires evidence annotated with the batch branch. Subsumed by the `G-5` derived-column exposure (B-08, S-05). |
| **M-06** present-indicative equivalence in §8.2 | **Not closed.** M-01 above. |
| **A11Y-UIR-I1-001/002/003** | **No regression found.** |

---

## Standing requirement

The lesson iteration 4 recorded was: *an assertion that classifies records by a
proxy enforces the proxy, not the rule.* It was applied. `A-08` no longer
classifies by a proxy; it requires a specific token in a specific column of every
implicated profile, and it is right to.

The lesson this round adds is the next one along:

> **An assertion that requires a value in a column no evidence rule consumes
> enforces the column, not the obligation.**

Both `A-08` and `A-14` are instances. `A-08` requires the state in
`required_values` while `N-04` counts frames from
`critical_distinct_frame_values`. `A-14` requires a triple without the coordinate
that makes it a per-state obligation. In both cases a producer can satisfy the
assertion completely and draw nothing, and in both cases the passing assertion is
what a future reviewer will read as proof that the matter was handled.

Three structural recommendations follow, all for the founder or an author
independent of the producer, none of them for the producer to take alone:

1. **Every assertion should name the evidence rule it feeds.** If `A-08` had been
   written as "the state profile of every stream-control host must *generate a
   frame* for these states", the column question would have been forced into the
   open on the day it was written. An assertion that cannot name a frame it
   causes to exist should be suspected of being an enumeration property.
2. **A new state token should be inadmissible until some record requires it.**
   B-02's two orphans would have been impossible under a rule that a value added
   to `responsive-state-mode-matrix.csv` must appear in at least one batch's
   `required_visual_evidence`, one traceability row, and one test before the
   package validates. This is the `R-037` inert-column rule extended from columns
   to values, and it is mechanically checkable.
3. **The frame budget in Part 7 should be a checked list, not a prose table.**
   Founder resolution 4 accepted a union of thirteen frames. Five of the six
   net-new ones are missing from the only record that will ever be executed, and
   no assertion in either package compares `B01.required_visual_evidence` against
   the accepted budget. That comparison is the single highest-value assertion
   neither package has.

Two closing observations offered without a finding attached, because they are
governance and not accessibility:

- The producer's decision to record six results rather than repair them is
  correct under D-045 and should not be read as evasion. Four of the six are
  specification gaps the producer was barred from filling. The gap in the
  disclosure is that it enumerates without stating consequence, and consequence
  is what a founder needs to decide whether to authorize.
- `B01` is held, `ma_025_disposition` agrees across both plan files, zero Figma
  allowance is consumed, and nothing is staged or committed. Every finding above
  is therefore correctable before a single metered call is spent, which is the
  best position this package has been in across five rounds.

**This package is not clean. B01 should not be released on it, and `R-039` should
be resolved with a sampling method as well as tokens before the first metered
call.**
