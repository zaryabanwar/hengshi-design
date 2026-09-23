# Design Review — CR-002 Amended Package as remediated under D-043 (iteration 5)

**Review date:** 2026-09-06
**Package under review:** CR-002 amended package as remediated under **D-043**,
design freeze aggregate
`DB92B4D0B889948D6C272F0DC7397327055B0108E7EEB953924F34E735BD4649`
**Reviewer:** independent review agent. I did not write any of the material under
review and I am not the producer. This review discharges **MA-029**.
**Verdict at review:** **FAIL**
**Deterministic validator state at review:** `RESULT=PASS PASS_COUNT=189
FAIL_COUNT=0`, freeze aggregate matching the value above. I ran it. It agrees
with itself.

> This is the fourth consecutive time this package has entered independent review
> immediately after a clean deterministic run (183 → FAIL, 184 → FAIL, 185 →
> FAIL, now 189 → FAIL). None of the findings below were detectable by any of the
> 189 assertions that passed. A passing validator is a determinism check, not a
> review, and the producer's own `validation-report.md` now says so in those
> words — correctly, and to its credit.
>
> **Direct answer to the question MA-029 asks:** the delivery stream axis does
> **not** resolve. It is present in identifier space and absent from evidence
> space. The D-042 defect — *assertions that pass by counting rows rather than
> resolving references* — has not been removed; it has been moved one level up,
> from "does the profile row exist" to "do the right number of records point at
> it". Findings B-01 through B-04 are that single defect seen from four sides.

## Blocking findings

### B-01 — `stream_profile` is a derived column, not a design decision

`validate-ui-reference-design.ps1` lines 335–352 compute the legal value of
`stream_profile` as a total function of `state_profile`:

```powershell
$streamDependentStates = @('SP-WORLD','SP-FIRST-VISIT','SP-RETURN-VISIT','SP-NAVIGATION','SP-SYSTEM-RECOVERY')
...
if ($row.state_profile -cin $streamDependentStates) { ...must be all four DS-S-*... }
elseif (-not ($selected.Count -eq 1 -and $selected[0] -ceq 'DS-STREAM-INVARIANT')) { ...error... }
```

Every route, flow and template row's `stream_profile` is fully predicted by its
`state_profile`. The column therefore carries **zero information** that the
package did not already contain, and no per-record design judgement was
exercised anywhere in the 163 records. The `DS-STREAM-INVARIANT` profile's own
`applies_to`, `annotation_requirements` and `exception_rule` describe a judgement
("records whose rendering does not vary by delivery stream", "if any stream would
render it differently the record must instead select the four `DS-S-*`
profiles"); the validator never evaluates that judgement, and there is no record
in the package where the judgement was actually made.

**Consequence.** The remediation the D-043 correction block claims — that the
axis is now load-bearing because records select it — is not true. A producer
reading `stream_profile` learns nothing they could not derive from
`state_profile`, and cannot get the column wrong even by trying: any value other
than the derived one is a validator failure, including a *correct* one. If a
record genuinely renders differently per stream but does not carry one of the
five hard-coded state profiles, the package makes it **illegal** to say so.

### B-02 — The route axis is structurally constant; no route-level per-stream evidence can ever exist

All **34 of 34** rows in `foundation-route-coverage.csv` carry
`stream_profile = DS-STREAM-INVARIANT`. No route uses any of the five
stream-dependent state profiles, so under B-01's derivation rule no route can
ever select `DS-S-*`. The route axis is a constant column.

This directly contradicts the same file's own `immersive_stream_representation`
column, which asserts a *different* World rendering per route —
`ROUTE-HOME` "Reception/atrium orientation panel"; `ROUTE-WING-STRATEGY`
"Sequenced Strategy threshold; closed/held/opening/open per accepted wayfinding
map"; `ROUTE-BOOK` "Booking panel"; `ROUTE-CONTACT` "Reception human-help panel".
A record cannot simultaneously render identically in `S-SEMANTIC` and `S-HIGH`
and have a distinct atrium representation in the World. `DS-STREAM-INVARIANT`'s
`minimum_evidence` requires the record to "state that it renders identically in
each" stream. Thirty-four route rows now assert that, and thirty-four route rows
also describe how they differ.

**Consequence.** `EC-06` obliges `ROUTE_INSTANCE_SHEET` evidence per route
instance, reconciled against this file. Because every route is stream-invariant,
a producer discharges every route instance in the entire programme with **one
frame set per route** and no per-stream frame at all. The end user affected is
the `S-SEMANTIC` visitor: no route sheet in any batch is ever obliged to show
what a canonical route looks like to them.

### B-03 — `DS-STREAM-INVARIANT`'s `exception_rule` binds nothing, and at least 13 flow rows violate it

The rule reads: "This profile may never be selected by a record whose rendering
depends on the World canvas or on the shell that hosts the delivery stream
control; such records must select all four `DS-S-*` profiles."

`reference-template-inventory.csv` declares `TPL-GLOBAL-NAVIGATION`,
`TPL-WORLD-SHELL`, `TPL-WORLD-HUD`, `TPL-QUICK-ACCESS-RECOVERY`,
`TPL-SYSTEM-RECOVERY`, `TPL-DIRECTORY-SEARCH`, `TPL-FIRST-VISIT` and
`TPL-RETURN-VISIT` to be stream-varying (all four `DS-S-*`). Resolving
`template_ids` across `foundation-flow-coverage.csv`, these `DS-STREAM-INVARIANT`
flow rows depend on templates the same package declares stream-varying:

`COV-ACT-02`, `COV-ACT-13`, `COV-ACT-17`, `COV-ACT-20`, `COV-FLOW-AI`,
`COV-FLOW-HUMAN-HANDOFF`, `COV-FLOW-CONTACT`,
`COV-FLOW-AUTH-SESSION-PERMISSION`, `COV-EXCL-ADMIN`,
`COV-EXCL-NONPUBLIC-PUBLICATION`, `COV-EXCL-CHAT-SESSIONS`,
`COV-EXCL-TRACKING-PARAMETERS`, `COV-EXCL-STAGING`.

The worst case is `COV-ACT-02` "Open canonical route", whose `template_ids` are
`TPL-GLOBAL-NAVIGATION;TPL-QUICK-ACCESS-RECOVERY` — *both* stream-varying, one of
them the shell that hosts the delivery stream control by `FR-3D-014` and style
guide §8.2.2. The most-travelled flow in the product is marked as rendering
identically in all four streams while being composed entirely of templates the
package says do not.

No assertion resolves `template_ids` against template `stream_profile`. The
`exception_rule` is prose.

**Consequence.** A producer executing any batch containing these flows produces a
single frame set and is validated clean, while having proven nothing about the
flow in `S-SEMANTIC`. This is exactly the failure mode finding 3 of iteration 4
was raised against, reproduced at flow granularity.

### B-04 — `delivery-stream-record-coverage` is a row count

```powershell
Assert-True ($streamSelectingRecords.Count -eq 44) 'delivery-stream-record-coverage' ...
```

The named pattern carried forward from iteration 4 is present verbatim in the
assertion added to fix it. The number 44 is not derived from any independent
statement of which records ought to vary; it is the count of rows that happen to
carry one of five state profiles, asserted against a literal that was read off
the current data. Any future record that should vary per stream but does not
carry one of those five states will make this assertion fail for the wrong
reason, and the cheapest repair will be to edit the literal.

**Consequence.** The assertion cannot detect the defect it was written for. It
detects only that nobody edited the state column.

### B-05 — B01's per-stream evidence obligation is unsatisfiable as written, and the production package contradicts it

`design-batch-plan.csv` B01 `required_visual_evidence` now demands the delivery
stream control "in every stream including `S-SEMANTIC`; one frame per
current-stream value". B01's primary templates are
`TPL-GLOBAL-NAVIGATION;TPL-DIRECTORY-SEARCH;TPL-SYSTEM-RECOVERY` — none of them
World surfaces. But the `minimum_evidence` of the `DS-S-*` profiles those
templates now select is written entirely in World terms: "Reception and one open
room at VP-320 and VP-DESKTOP", "keyboard focus frame on a hotspot",
"screen-reader annotation of the HUD". A producer capturing
`TPL-DIRECTORY-SEARCH` under `DS-S-HIGH` is instructed to photograph a room and a
hotspot that the template does not contain.

Simultaneously:

- `UI_REFERENCE_PRODUCTION_CONTRACT.md` §0.1 states "B07 remains deferred and not
  authorizable under MA-025 … **the four-stream reference evidence is therefore
  not produced under this contract and waits on MA-026**."
- `RISKS.md` R-036 states "Until then no document may state that the four-stream
  obligation is met."
- `design-batch-plan.csv` B01 now states the four-stream obligation is discharged
  on an authorized batch.

**Consequence.** B01 is the batch this review releases and the batch that spends
metered Figma calls. Its producer receives three mutually exclusive instructions
— capture per-stream frames, capture World content on non-World templates, and do
not produce four-stream evidence at all under this contract — with no rule for
resolving them. The likely outcome is metered allowance spent on frames that a
later review rejects.

### B-06 — The production package has no stream axis at all

`evidence-capture-plan.csv` enumerates the axes a capture must cover: `EC-10`
viewport, `EC-11` mode, `EC-03` state, `EC-12` time-limit branch. **There is no
`EC-*` rule for stream.** `batch-production-plan.csv`, `external-write-scope.csv`
and `mcp-call-budget.csv` contain no occurrence of `stream_profile`, `DS-S-`, or
`DS-STREAM-INVARIANT`. `EC-08`'s evidence-ID grammar is
`HSD_UIR_<BATCH>_<TEMPLATE>_<INSTANCE>_<STATE>_<VIEWPORT>_<MODE>_V<NN>` — it has
no stream slot, so two frames of the same template in `S-HIGH` and `S-SEMANTIC`
**cannot be given distinct evidence IDs**, and `EC-30`'s append-only rule would
read the second as an illegal overwrite of the first.

**Consequence.** Even if B01's prose obligation were coherent (it is not, per
B-05), the naming grammar that governs capture makes per-stream frames
unexpressible. The design package's new axis stops at the boundary of the
package that actually drives production.

## Significant findings

### S-01 — Degradation vocabulary survives outside the guard's reach, including the exact string R-034 was closed against

The `semantic-stream-peer-framing` regex is applied only to
`$producerFreezeText`, i.e. the design package's 13 frozen files. Outside it:

- `docs/phase-1-ui-reference-production/batch-production-plan.csv` B07
  `batch_name` = **"Optional World HUD and Quick Access parity"** — the verbatim
  string cited in `RISKS.md` as R-034's originating evidence, in a file whose
  `source_row_authority` is `design-batch-plan.csv`, where the same batch is now
  named "Core delivery-stream World HUD and semantic peer parity". **R-034 is
  recorded closed.**
- `docs/phase-1-ux-architecture/UX_ARCHITECTURE.md` — "optional World are
  utilities" (:118), "J-02 Optional immersive discovery" (:169), "Visitor
  explicitly selects optional World" (:173), "optional World" (:246).
- `docs/phase-1-ux-architecture/excluded-surfaces.csv` EXCL-WORLD — "Optional
  immersive shell; never required".
- `docs/phase-1-ux-architecture/README.md:12` — "optional immersive exploration".
- `docs/phase-1-ux-architecture/FLOWS.md:241` — "**Quality downgrade** never
  removes content".
- `docs/phase-1-ux-architecture/STATES_AND_RECOVERY.md` ACT-06 — "Enter optional
  World".

**Consequence.** R-034 is closed against a defect that is still in the
repository, so the risk ledger is wrong on a point it explicitly asserts. A
downstream reader of the UX package — which is accepted and normative — learns
the World is optional and the semantic route is the non-optional baseline, i.e.
the ladder model the whole of D-039/D-043 exists to remove. The guard's
deliberate narrowing to the design folder is recorded in `docs/decisions-log.md`
as a decision; the consequence of that decision is that the vocabulary defect
persists in the packages that were never in scope, and no ledger says so.

### S-02 — The unsignalled default contradicts the "optional World" model, and nothing resolves it

Style guide §8.2.2 makes `S-LOW` the unsignalled default and states "S-LOW is the
highest-traffic first-paint stream and is designed first, not last". `S-LOW` is a
World stream. Therefore a WebGL-capable visitor with no stored signal lands in
the World by default. The UX package states the World is entered only when the
"visitor explicitly selects" it (`UX_ARCHITECTURE.md:173`).

These cannot both be true, and which one is true determines B-02: if the default
lands in the World, then no route is stream-invariant and all 34 route rows are
mis-assigned; if entry is opt-in, then §8.2.2's precedence table is describing a
stream nobody is in at first paint.

**Consequence.** The producer cannot know what the first frame of `ROUTE-HOME`
shows. That is the single most-produced frame in B01.

### S-03 — `DS-STREAM-INVARIANT` is a positive equivalence claim that no record actually makes

The profile's `minimum_evidence` requires "the record must state that it renders
identically in each" stream. 34 routes, 53 flows and 32 templates carry the
profile. **None of them contains that statement.** The claim lives once, in the
profile row; the 119 records that inherit it are silent. This is the equivalence
claim being asserted by the container rather than by the records, which is the
same substitution as B-01.

**Consequence.** The "positive assertion, not an exemption" framing the D-043
record leans on is not instantiated. Operationally `DS-STREAM-INVARIANT` behaves
as an exemption: it is what a record carries when nobody looked.

### S-04 — `validation-report.md` restates the derived rule as if it were a finding

The report says the validator proves "the 36 flows and 8 templates **whose
rendering depends on the World canvas or the shell hosting the stream control**
select all four `DS-S-*` profiles". The validator proves no such thing. It proves
that the 44 records carrying five specific `state_profile` values carry four
specific `stream_profile` values. The dependency claim is the producer's
assertion about what those state profiles mean, asserted in a document that
elsewhere correctly warns against reading validator output as approval.

**Consequence.** This is the overclaiming class the report itself was rewritten
to remove. A founder reading §Coverage is told a semantic property was verified
when a syntactic one was.

## Minor findings

- **M-01** — `docs/phase-1-ux-architecture/README.md:43` still reads "**All 33
  route definitions** and their Quick Access / optional immersive
  representation" against a 34-row `route-room-parity.csv`. Same defect class as
  iteration-4 finding 9, in a location that fix did not reach. (The design
  package's remaining "33" references are correctly framed as provenance — "33
  accepted at D-025 plus `/credits` reconciled 2026-09-06 under R-032" — and are
  sound.)
- **M-02** — `RISKS.md` R-032 is closed, but its evidence cell still reads
  "`foundation-route-coverage.csv` enumerates 33 routes". The closure is right;
  the cited evidence is stale and now describes a state that does not exist.
- **M-03** — `UI_REFERENCE_PRODUCTION_CONTRACT.md` retains a paragraph asserting
  the D-042 remediation "has not been re-reviewed since", which was true when
  written and is superseded by the §0.1 supersession chain in the same file.
- **M-04** — `design-batch-plan.csv` carries `status = future_not_authorized` on
  **all nine** batches, including B01, while the production plan carries B01 as
  `authorized_pilot` at execution order 1. The two files disagree on whether the
  batch this review releases is authorized.

## What I found sound

- **The producer's own account of the D-042 failure.** `validation-report.md`
  §"What this report is not" and §"Why this report was rewritten" state the
  defect plainly, name the count that was wrong, and decline to claim approval.
  `docs/decisions-log.md` D-043 records the cascade claim "**was false**",
  records that it was the producer's claim and not the reviewer's, records the
  guard being widened and then deliberately narrowed, and ends "**R-035 does not
  close.**" `design-review-iteration-4.md` was corrected by appending a dated
  block rather than by rewriting the original dispositions. This is honest
  ledger practice and it is the reason this review could be conducted at all.
- **`validation-report-counts-agreement`.** A genuine structural guard: it
  resolves a reference (the report's `COUNTS` line against the run's computed
  counts) rather than counting rows. It is the one assertion added under D-043
  that could not be satisfied by a placeholder.
- **The substance of the founder's stream decisions.** WebGL as a hard ceiling;
  no failure and no measurement promoting or demoting mid-session; `S-LOW`
  retaining every hotspot and destination; motion decoupled from stream; the
  removal of the mid-session promotion window rather than an attempt to specify
  it. The defects in this review are in instantiation, not in intent.
- **The withdrawal of the WCAG 3.2.2 "satisfied by construction" claim** and
  §8.2.4's explicit statement that 3.2.2 and 4.1.3 "are evaluated against the
  implementation, not against this document". SRS §5.6's NFR-A11Y-001…007 are all
  marked "❌ Not implemented", and NFR-A11Y-002 states aggregate evidence does not
  satisfy per-stream conformance. **No current conformance is claimed anywhere in
  the package.** I looked for it specifically and did not find it.
- **`DS-S-SEMANTIC`'s `exception_rule`** — "may never be marked not applicable …
  never drawn as `STATE-WEBGL-UNSUPPORTED` … carries no failure heading no error
  styling and no language of escape recovery or fallback". This is correctly
  written and correctly framed. Its problem is that only 44 records reach it.
- **The `S-SEMANTIC` boundary-crossing focus-destination specification** in
  §8.2.4 and the step-4 storage specification in §8.2.2 are concrete and
  testable.

## Standing requirement

The producer does not approve its own material output. **MA-029 is not
discharged clean.** R-035 remains open and R-036 remains open. B01 should not be
released and no metered external design allowance should be spent until at
minimum B-01 through B-06 are addressed, because B-05 and B-06 mean the calls
would be spent producing evidence that cannot be named, cannot be validated
against a stream axis, and is contradicted by the contract that governs it.

**On what a future PASS would and would not cover.** This review examined
documents. Any PASS on this package covers internal consistency, resolvability of
identifiers, and absence of overclaiming in prose. It does **not** and cannot
cover: whether the four streams are actually equivalent in a running product,
whether WCAG 2.2 AA is met, whether `S-SEMANTIC` is usable, or whether the device
signals in §8.2.1 behave as described on real hardware. Those are implementation
and audit findings and no reference-design package can pre-empt them.

**Named pattern, carried forward again:** *assertions that pass by counting rows
rather than resolving references.* Under D-042 the count was of profile rows.
Under D-043 the count is of records pointing at them. The next remediation should
be tested by a different question: **is there any record in the package whose
`stream_profile` a human had to decide?** Today the answer is no. Until it is
yes, the axis is inert regardless of how many assertions pass.
