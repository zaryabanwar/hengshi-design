# Design Review — Delivery-stream evidence model as implemented under D-045 (iteration 6)

**Review date:** 2026-09-06
**Packages under review:** `docs/phase-1-ui-reference-design` (design freeze
aggregate `0AA83FD298ABB12A96782205996EB3783BF8E80E11AD1B2BE44473F2E87EB536`)
and `docs/phase-1-ui-reference-production` (freeze
`4464F6C44C11E7A00C4F007C3112840C6087CB3C1321B86ED5842B9100CC50CE`), as
remediated under **D-045**.
**Reviewer:** independent review agent. I did not write any of the material under
review and I am not the producer. This review is offered under Constitution 2.0.0
principle VII.
**Verdict at review:** **FAIL**
**Deterministic validator state at review:** design `RESULT=PASS PASS_COUNT=201
FAIL_COUNT=0`; production `RESULT=PASS PASS_COUNT=165 FAIL_COUNT=0`. Both freeze
aggregates reproduce the values recorded at D-045. I ran both. They agree with
themselves and with the ledger.

> This is the fifth consecutive independent review to open on a clean
> deterministic run (183 → FAIL, 184 → FAIL, 185 → FAIL, 189 → FAIL, now 201 + 165
> → FAIL). None of the blocking findings below was detectable by any of the 366
> assertions that passed.
>
> **Direct answer to the question D-045 asks.** The evidence model is correctly
> *specified*. `DELIVERY_STREAM_EVIDENCE_MODEL.md` is the best document in this
> programme and I do not dispute a line of it. What it *directed* has been
> implemented in shape and not in substance: the declared-at-primitive column
> exists, the fold exists, the assertions exist, the guards exist — and the fold is
> a **constant function**, so every one of the 40 templates, 34 routes and 89 flows
> carries the identical stream obligation, and the assertion set that reads it
> cannot distinguish the current package from one in which the column had never
> been authored.
>
> The specification anticipated exactly this. §9.4 warned that setting every value
> to all four streams makes the column inert and that `A-11` will not catch it, and
> §11 gave the reviewer three tests. I ran all three. **Test 1 fails** (below,
> B-01/B-02). **Test 2 fails** (B-05). **Test 3 fails** (B-06). The defect class
> D-045 was commissioned to end is present in the remedy for it, in its original
> form and in three new ones.

---

## Blocking findings

### B-01 — The union fold is a constant function; `presence` carries no information at any locus

§3.1 defines the model as *declared at the primitive, computed at the template by a
union fold over `primitive_dependencies`, inherited unstored at route and flow*.
That is what the code does. It is also, on this data, a constant map.

I recomputed the fold independently of the validator, from
`component-primitives.csv` and `reference-template-inventory.csv` directly. All
**40 of 40** templates fold to the identical set:

```
S-HIGH;S-LOW;S-MEDIUM;S-SEMANTIC
```

Without exception. `TPL-PUBLIC-HOME`, `TPL-BOOKING-VERIFICATION`,
`TPL-AUDIT-INSPECTION` and `TPL-WORLD-HUD` are indistinguishable in stream space.
Because route and flow presence are inherited via `template_id` / `template_ids`,
presence(R) is constant over all 34 routes and presence(F) is constant over all 89
flows. The cause is structural rather than accidental: 50 of the 62 primitives
declare all four streams, 9 declare `STREAM-SCOPE-EXCLUDED` (which the fold skips),
and the only three primitives that discriminate — `PRIM-042`, `PRIM-043`,
`PRIM-044`, each `S-HIGH;S-LOW;S-MEDIUM` — never appear in a template that does not
also depend on an all-four primitive. `PRIM-057` (status region) and `PRIM-058`
(loading/empty/offline container) are all-four and are dependencies of **every**
template, so the fold's result was determined before any World primitive was
consulted.

This is §11 test 1, and the specification pre-wrote the answer: *"There must be
exactly 62, in `component-primitives.csv`, each with a stated reason. If they are
all `S-HIGH;S-LOW;S-MEDIUM;S-SEMANTIC`, the column is inert and the answer is no."*
They are not literally all four — 12 are not — but the twelve exceptions are
absorbed by the fold before they reach any consumer, so the answer at every locus
that anything reads is the same as if they were.

The consequence is that `stream_presence` is a **declared** column whose only
downstream use is a **constant**. It is the D-042/D-043 defect with the arrow
reversed: rather than a column derived from another column, it is a column from
which nothing can be derived.

### B-02 — The three discriminating values have no consequence, and one of them is a false claim the specification told reviewers to look for

§9.4 is explicit: *"The reviewers must check `PRIM-042`, `PRIM-043` and `PRIM-044`
specifically: a World HUD present in `S-SEMANTIC` is a false claim, and it is the
cheapest available way to make this column mean nothing."*

I tested the column in both directions, by mutation, in an out-of-repository
sandbox seeded from a pristine copy (the sandbox reproduces the repository run
byte for byte: `PASS_COUNT=201`, aggregate `0AA83F…B536`).

- **M1b — make the false claim.** Set `PRIM-042`, `PRIM-043` and `PRIM-044` to
  `S-HIGH;S-LOW;S-MEDIUM;S-SEMANTIC`, i.e. assert that the World HUD renders in the
  semantic stream. Result: **`RESULT=PASS`**, 201/0. The only observable change is
  the freeze hash, which changes for a whitespace edit too.
- **M1c — correct a value in the other direction.** Narrow `PRIM-050` (staff
  version/checksum display) away from all four. Result: **`RESULT=PASS`**, 201/0.

The column is unfalsifiable in both directions. Nothing in either validator can
tell a true `stream_presence` value from a false one.

Separately, and independently of any mutation: because the fold is constant,
`presence(TPL-WORLD-HUD)` **already includes `S-SEMANTIC`** in the shipped package.
The package as frozen makes the exact claim §9.4 names as false — that the World
HUD is present in the semantic stream — and states it as a computed fact rather
than an authored one, which is worse, because no human wrote it and no human can
be held to it.

### B-03 — `A-11` skips constant columns, which is the single hole §9.4 named, and it is not on the known-limits list

`validate-ui-reference-design.ps1`:

```powershell
if (@($rows | ForEach-Object { [string]$_.$c } | Sort-Object -Unique).Count -le 1) { continue }
```

A column with one distinct value is skipped before any determiner is tested. It is
never reported and never failed. `A-11` is the assertion the specification
nominated as the defence against the inert-column defect, and it is blind to the
most extreme form of that defect — a column that is a total function of *nothing*.

`validation-report.md` states, in the known-limits section, that
"`stream_presence` is **not** among them — that is a hard failure and the run
passes it". The statement is true and immaterial: `stream_presence` has three
distinct values, so it is tested, and it is not a function of any determiner. The
property that matters — that its image under the fold is a singleton — is not
tested by `A-11` or by anything else. This exclusion is not disclosed in the
producer's known limits, in `producer-inspection.md`, or in `RISKS.md`.

### B-04 — `A-14` cannot fail. Its escape disjunct is pinned true by another assertion 500 lines earlier in the same file

`A-14` is the only rule in either package that would ever check per-stream frame
coverage — the whole point of `EC-31`. Its pass condition
(`validate-ui-reference-production.ps1` line ~750):

```powershell
$executable = @($batchRows | Where-Object { $_.ma_025_disposition -eq 'authorized_pilot' })
Assert-That -Name 'A-14:unmet-per-stream-obligations-are-explained-by-held-authorization' `
    -Condition ($unmet.Count -eq 0 -or $executable.Count -eq 0) ...
```

And at line 247 of the same file, in the same run:

```powershell
Assert-That -Name 'authorization:nothing-is-authorized-to-execute' `
    -Condition (@($batchRows | Where-Object { $_.ma_025_disposition -eq 'authorized_pilot' }).Count -eq 0) `
    -Detail 'no batch carries an unconditional execution authorization'
```

`$executable.Count -eq 0` is not a contingent property of the data that `A-14`
happens to observe; it is a property the file **asserts as a precondition of
passing at all**. While `authorization:nothing-is-authorized-to-execute` holds,
`A-14`'s second disjunct is true by construction and the first is never evaluated
for effect. The token `authorized_pilot` occurs in exactly three places in the
entire repository — those two assertions and one comment — and in **no data file**.

`RISKS.md` **R-041** describes this as *"passes only because every unmet obligation
is currently explained by held authorization. If the explanation is ever recorded
incorrectly, the assertion becomes permanently…"*. That framing is too generous by
one level. It is not a data state that could change; under G-4 it is a state the
validator requires. `A-14` is a named, passing, documented assertion that tests
nothing, which is the definition R-038 gives of the defect, and it is the fourth
consecutive remediation to ship one.

### B-05 — Five further assertions cannot fail, or can fail only for reasons unrelated to streams

§11 test 2 asks: *"Can a record be wrong?"* and names two fixtures. I ran them, and
then the rest of §6's fixture set.

1. **`A-05` is a NOT-NULL check.** The specification's own fixture (b) — *"Remove
   `PRIM-001` from `TPL-BOOKING-SHELL` and confirm `A-05` fails in the other
   direction"* — returns **`RESULT=PASS` 201/0**. The reason is B-01: the right-hand
   side of the comparison is `$computed`, filtered to the three immersive streams,
   which is non-empty for every template regardless of dependencies, because
   `PRIM-057`/`PRIM-058` supply all four. The assertion reduces to *"the
   `immersive_stream_representation` cell is not blank"*. The specification called
   this column *"independently authored"* and *"load-bearing under `A-05`"*. It
   bears a null check.
2. **`A-04`'s stream clause is unreachable.** `$owned` is constructed from a
   superset of the same source as `$fp`, so `foreach ($s in $fp) { if ($s -cnotin
   $owned) … }` has an empty failure set by construction, for any data.
3. **`A-06`'s only reachable failure is a duplicate token in a state profile's
   `required_values`** (confirmed by mutation M5). Its `not-single-stream` branch
   splits a key it formatted three lines earlier from a value already constrained
   to `$legalStreams`; it is a round trip through string formatting. A CSV hygiene
   defect can fail `A-06`; a stream defect cannot.
4. **`A-10` never resolves `<TEMPLATE>`.** The grammar regex captures group 2 and
   the group is never used. Renaming a `baseline_frame_name`'s template segment to
   `TPL_NO_SUCH_TEMPLATE_XYZ` returns **`RESULT=PASS` 201/0**. This directly
   contradicts §6.1's statement of `A-10`'s purpose — *"resolving each parsed token
   against the accepted value set the record itself selects"* — and the
   `validation-report.md` sentence that repeats it. I spot-checked the 74
   regenerated names against the amended `EC-08` grammar: the *shape* is right and
   the `<STREAM>` segment is present and legal on all of them; what is absent is any
   resolution of the tokens the grammar extracts.
5. **`A-13`'s live content is a key-presence check on a constant.** Every one of the
   nine `stream_disposition` cells is the identical string
   `S-HIGH=in_scope;S-LOW=in_scope;S-MEDIUM=in_scope;S-SEMANTIC=in_scope`. The
   `in_scope` branch is a bare `continue`; the `not_present` and `deferred_<BATCH>`
   branches have zero instances, so `EC-33`'s deferral mechanism is entirely
   unexercised. `B07` and `B09` carry `deferred_not_authorizable` and nonetheless
   declare all four streams `in_scope`, which is the one combination `EC-33` exists
   to express and it is expressed as its opposite.

### B-06 — Roughly twenty assertions still pass by counting rows. This is §11 test 3, run as directed

§11 test 3: *"Does any assertion pass by counting rows? Grep the validators for
`-eq <literal>` in an assertion's pass condition. The only legitimate form is the
comparison of two independently derived quantities."*

Design validator, literal row counts in pass conditions:
`source-experience-id-count` (`-eq 32`), `flow-coverage-row-count` (`-eq 89`),
`template-count` (`-eq 40`), `profile-count` (`-eq 36`), `route-template-ref-count`
(`-eq 19`), `flow-template-ref-count` (`-eq 29`), `exclusion-count` and
`wayfinding-count` (each also comparing two derived quantities, so partly
legitimate), `d025-industries-retained` (`-eq 1`), `freeze-file-count` (`-eq 13`).

Production validator: `csv-parse:batch-production-plan` (`-eq 9`),
`csv-parse:stop-conditions` (`-eq 12`), `csv-parse:evidence-capture-plan`
(`-eq 33`), `csv-parse:provider-evaluation` (`-eq 12`), `csv-parse:traceability`
(`-eq 40`), `authorization:six-batches-conditional` (`-eq 6`),
`authorization:two-batches-deferred` (`-eq 2`), `sequence:B01-runs-first` (`-eq 1`).

D-043's named defect was *"the replacement assertion asserted `Count -eq 44`"*.
That exact construction is present about twenty times across the two validators,
five of them added new in the D-045 production validator. I accept two of them —
`degradation-pattern-alternative-count -eq 9` and
`A-16:framing-pattern-is-nine-alternatives -eq 9` — as legitimate, because they
detect the R-038 array collapse and there is no second derivation available; the
producer's reasoning there is correct and well written. The rest are row counts
asserting against a literal transcribed from the row count.

### B-07 — R-034 survives a third widening, including the exact banned string, in both spellings

The mandate asked whether any artifact still frames the semantic stream as a
degradation, a fallback, or an optional extra, in any identifier spelling. It does.

I applied the shipped nine-alternative pattern to the packages myself:

- `docs/phase-1-ux-architecture/producer-inspection.md` contains **two literal
  matches for `optional World`** — the phrase R-034 is recorded closed against —
  at lines 27 and 93. The guard finds them. `A-16` passes anyway, because that file
  is exempt **by filename**. The exemption's stated justification is that *"a dated
  evidence record must be able to name the defect it records as removed"*. Neither
  use is a mention of a removed defect. Line 27 is a present-tense architectural
  assertion — *"Semantic Quick Access and optional World share content authority and
  direct Book"* — and line 93 is an open hypothesis about *"optional World value"*.
  The exempt class is closed and structural, which is a real improvement over a
  discretionary list, but it exempts by **file identity** where the justification is
  about **use versus mention**, and the abolished vocabulary is now sitting in the
  one place the guard has been instructed not to look.
- `docs/phase-1-ux-architecture/UX_ARCHITECTURE.md:9` — *"The **optional campus**
  may improve orientation and memorability…"*. Scanned, not exempt, **zero guard
  hits**. `campus` is the document's own synonym for the World; the alternation
  lists `world|enhancement|immersive`.
- `docs/phase-1-ux-architecture/UX_ARCHITECTURE.md:88` — the route diagram edge
  `H -. optional .-> X[/world - noindex]`. Scanned, not exempt, zero hits.
- `docs/phase-1-ux-architecture/FLOWS.md:231` — *"Immersive location is optional;
  canonical destination is primary."* Zero hits; the word order defeats
  `optional (immersive)`.
- `docs/phase-1-ux-architecture/CONTENT_ANALYTICS_TESTS.md:99` — `UXTEST-003`,
  *"Compare each **optional room/panel** to canonical route"*. Zero hits.
- `docs/phase-1-ui-reference-design/UI_REFERENCE_DESIGN_CONTRACT.md:317` —
  *"transition interruption, **low-power downgrade**, unsupported WebGL…"*, a
  required-variant name inside the design package's own normative contract, in the
  freeze, scanned, zero hits. The pattern bans `quality downgrade`, not `downgrade`.
- `docs/phase-1-ux-architecture/UX_ARCHITECTURE.md:187` — *"memory/thermal
  downgrade"*. Same shape, zero hits.

The pattern has been widened twice and both times it was fitted to the instances
last found rather than to the vocabulary. `quality downgrade` was banned because
`"Quality downgrade never removes content"` had been found; the two remaining
`downgrade` phrases describe a transition *between peer streams* as a descent, which
is the ladder framing D-039 abolished, and they survive because they are not the
string that was caught last time. R-034's status line reads `reopened`; on this
evidence it must stay open, and the remedy is not a tenth alternative.

### B-08 — Two changes the accepted specification directs were not made, and are not disclosed anywhere

§8.2 resolves the three-way `B-05` contradiction by **stated precedence**, and the
§9 migration tables direct two consequent edits. Neither was performed, and neither
appears in `producer-inspection.md`, `validation-report.md`, `DECISIONS.md` D-045,
or `RISKS.md`.

1. **`UI_REFERENCE_PRODUCTION_CONTRACT.md` §0.1 was not narrowed; it was emptied.**
   §8.2 directs that *"the four-stream reference evidence is therefore not produced
   under this contract"* be **narrowed** to *"four-stream **World** evidence is
   deferred to B07; four-stream **semantic-shell** evidence of the delivery stream
   control is produced in B01."* The offending sentence is gone from the contract;
   the narrowed replacement is nowhere in the repository. The contract is now silent
   on where four-stream evidence is produced, which is the state §8.2 exists to end.
   Deleting a contradiction is not resolving it; it removes the record that the
   question was ever decided.
2. **`RISKS.md` R-036 was not amended.** §8.2 and the §9.3 migration row both direct
   that R-036 stay open *"with its scope narrowed to the World half"*. R-036 is
   verbatim unchanged and is now false in two clauses: it asserts that B07 is *"the
   only batch carrying any four-stream obligation"* (B01's rewritten
   `required_visual_evidence` carries an explicit four-stream semantic-shell
   obligation, and `batch-production-plan.csv` marks all four streams `in_scope` on
   all nine batches), and it asserts that *"§0.1 authorizes B01-B06 and B08 only"*
   (under G-4 nothing is authorized to execute). R-036 is the standing authority
   for the sentence *"no document may state that the four-stream obligation is
   met"*, and it now states two things that are not true.

---

## Significant findings

### S-01 — Two checkable numbers in the producer's self-report are wrong, and nothing asserts either

- **"eleven state profiles"** — `validation-report.md` and `producer-inspection.md`
  both say *"Fourteen profiles are implicated; the table named one. The other eleven
  were amended as a mechanical derivation."* Fourteen minus one is thirteen. I
  enumerated them: the two states are now carried by `SP-PUBLIC-DOCUMENT`,
  `SP-PUBLIC-COLLECTION`, `SP-PUBLIC-DETAIL`, `SP-EVIDENCE-COLLECTION`,
  `SP-EVIDENCE-DETAIL`, `SP-NAVIGATION`, `SP-FIRST-VISIT`, `SP-RETURN-VISIT`,
  `SP-WORLD`, `SP-AI`, `SP-HANDOFF-MEDIA`, `SP-BOOKING`, `SP-CONTACT` and
  `SP-SYSTEM-RECOVERY` — fourteen. §5.3 named `SP-NAVIGATION`. At HEAD, exactly one
  of the twenty-eight cells existed. Thirteen profiles were amended without the
  migration table naming them, disclosed as eleven.
- **"Twenty-two judgement columns are inert"** — repeated in `validation-report.md`,
  `producer-inspection.md`, `RISKS.md` R-037 and `DECISIONS.md`. The run emits **23**
  `INERT-REPORT` lines covering **14** distinct file:column pairs. Twenty-two is
  neither. `validation-report-counts-agreement` pins the `COUNTS` line to the run
  and nothing pins this one.

The derivation itself I found **sound**: `A-08` gates on `$controlHosts` —
primitives whose `required_anatomy` names the delivery stream control — which is
`PRIM-001`, `PRIM-042`, `PRIM-043`, `PRIM-044`. Placing the control in the semantic
shell is founder resolution G-1, and once it is there, `N-01` puts it in almost
every template. That is a genuine mechanical consequence and "derivation, not design
choice" is the correct characterisation. The disclosure of its size is not correct.

### S-02 — The staff/publication/audit fold is described accurately and its consequence is under-reported

The producer's account — *"They depend on primitives that are legitimately present
in all four, so §4.2's union fold yields all four even though those templates serve
excluded surfaces"* — is **accurate**, and I initially mis-attributed it myself
before checking. `TPL-STAFF-AUTH` depends on `PRIM-006`, `PRIM-015`, `PRIM-056`,
`PRIM-057`, `PRIM-058`, all correctly all-four because all five are also used on
public surfaces. "Recorded not repaired" is also the correct call: §4.1 constrains
primitives, not templates, and adding a template-level exclusion would be the
producer authoring the model.

What is not reported is the consequence. Six templates — `TPL-STAFF-AUTH`,
`TPL-STAFF-QUEUE`, `TPL-STAFF-WORK-DETAIL`, `TPL-PUBLICATION-EDITOR`,
`TPL-PUBLICATION-REVIEW-RELEASE`, `TPL-AUDIT-INSPECTION` — carry a four-stream
obligation and have **no stream-control host at all**. `N-01` exists precisely to
make that state detectable, and `A-07` skips them via its excluded-surface branch,
so the one assertion written to catch "obligations with no surface to satisfy them"
is switched off for the only six templates that exhibit it. Under `N-04`'s
multiplier those six obligations propagate into `A-14`'s obliged set as a demand for
`S-SEMANTIC` frames of the audit event viewer. This should be stated as an open
defect in the model with a named consequence, not as a curiosity of the fold.

### S-03 — `stream_disposition` is constant, disclosed, and still built on

To the producer's credit this one is disclosed fully, in the validator source, in
`producer-inspection.md` and in `RISKS.md`, in the right words: *"A constant column
encodes no per-batch judgement and cannot be wrong — the same shape as the defect
D-045 was decided to end, appearing inside the accepted remedy for it."* That
paragraph is the most honest thing in the package.

It is still a blocking-adjacent problem rather than an observation, because `A-13`
is defined against it (B-05.5) and because §5.4 describes the column as *"9 human
decisions about deferral"*. Nine identical values are not nine decisions. The
correct disposition for `B07`, a deferred batch, is visibly not `in_scope` on all
four streams.

### S-04 — `A-15`'s legal-token set contains an unreachable member

`$legalStreamTokens = $streamSegments + @('STREAM_SCOPE')`. The matcher is
`_(STREAM[_-][A-Z0-9]+)[_-]V\d{2}`, so `STREAM_SCOPE` can only ever be reached by a
frame named `…_STREAM_SCOPE_V01`. `STREAM-SCOPE-EXCLUDED`, the value this member
appears to be for, cannot match — the trailing `-EXCLUDED` prevents it. The member
is harmless but it is a legal value that no input can occupy, which is the same
category as a zero-member guarded profile: §2 deleted `DS-STREAM-INVARIANT` for
exactly this reason.

---

## Minor findings

- **M-01** — `A-16`'s directory exemption tests the *leaf* directory name, so any
  future directory named `reviews` or `accessibility` anywhere under the three roots
  is exempt without a decision. Small, but the exemption's whole claim is that a
  producer cannot quietly add a file to the class.
- **M-02** — `validation-report.md` line 151 states *"no package record frames the
  semantic stream as a degradation, a fallback, or an optional extra"*. Against the
  three-package scope `A-16` now claims, that statement is false (B-07). It was
  true of the 13-file design freeze when it was written; it was not re-checked when
  the scope was widened.
- **M-03** — `RISKS.md` R-041 understates `A-14` (B-04): it describes a data
  condition where the truth is a validator-asserted invariant.
- **M-04** — `TPL-QUICK-ACCESS-RECOVERY.minimum_reference_evidence` reads
  *"Loading/degraded/offline/error…"*. I adjudicate this as **not** an R-034 defect:
  `STATE-DEGRADED` is an accepted state-vocabulary member describing a service
  condition, not a stream. Recorded so the next reviewer does not re-open it.

---

## What I found sound

I want these on the record, because four consecutive FAILs make it easy to read a
fifth as a verdict on effort rather than on evidence. The following are real,
and several are genuinely good work.

- **The specification itself.** `DELIVERY_STREAM_EVIDENCE_MODEL.md` §1, §2's
  deletion of `DS-STREAM-INVARIANT` with the invariance test surviving as an
  assertion that cannot be selected into, §9.4's warning, and §11's three reviewer
  tests are correct and I used them as written. §2's rejection of the zero-member
  guarded category is the right instinct applied for the right reason.
- **Three real R-034 fixes at the primitive level.** `PRIM-042`'s anatomy went from
  `quality choice` to `delivery stream control`; `PRIM-043`'s from `quality` to
  `delivery stream control`; `PRIM-044` was renamed from *"World escape and
  **fallback**"* to *"World escape and recovery"* and lost `quality downgrade if
  valid`. `B07`'s batch name no longer reads *"Optional World HUD…"*. These were
  found and removed, not papered over.
- **`MODE_NON_WEBGL_QUICK_ACCESS` and `STATE_UNAVAILABLE`** are gone from the
  regenerated frame names, as §9.1 said they would be as a side effect. The `EC-08`
  amendment is applied consistently across all 74 names; every one carries a
  mandatory, legal `<STREAM>` segment with no omissible or aggregate form.
- **`B01.required_visual_evidence`** is a faithful implementation of §8.1, point by
  point, including the explicit exclusion of Reception, rooms, hotspots and the HUD.
- **G-4 is correctly implemented in both files.** `B01` is `future_not_authorized`
  in `design-batch-plan.csv` and in `batch-production-plan.csv`, and the six
  `authorized_released_by_pilot` rows are correctly characterised as conditional.
- **R-038 is disclosed in full and defended against.** The PowerShell comma-vs-`+`
  precedence collapse is explained accurately in both validators, every alternative
  is parenthesised, and the count is asserted in both. This is the one place in the
  package where an assertion exists *because* the producer worked out how the guard
  could silently die.
- **`A-16`'s scope is computed, not listed**, and the scope is itself asserted with
  a strict-subset condition on the exempt set. The reasoning — *"a guard's scope is
  part of its claim, and a scope stated as a literal file list ages silently"* — is
  correct and is the single best structural improvement in this iteration. It is
  undone by the exemption rule (B-07), not by the design.
- **`A-12` and `A-15`'s fixture halves are honest.** Both feed abolished spellings
  through the same matcher in the same position and require rejection. Those halves
  can fail.
- **Determinism holds.** Both freeze aggregates reproduce, the design run reproduces
  byte-for-byte in a clean sandbox, and `validation-report-counts-agreement` pins the
  report to the run that produced it. The producer's own statement that a passing
  run is a determinism check and not a review is correct and should be kept.

---

## Standing requirement

Nothing in this review authorises any external write, any Figma call, or any change
of `B01`'s held status. `R-034` stays open. `R-036` stays open and is now
additionally inaccurate. `R-038` stays open and gains a fourth instance (`A-14`).
`R-041` stays open and should be restated. `MA-029` is not discharged by this
review.

I did not modify any file in the repository other than this record. All mutation
testing was performed on an out-of-repository sandbox copy, reset from pristine
sources after each fixture; the working tree is unchanged and both validators
reproduce their pre-review output.

---

## Named pattern, carried forward again

Iteration 5 closed with a test question: *is there any record in the package whose
`stream_profile` a human had to decide?* D-045 deleted `stream_profile` and replaced
it with `stream_presence`, authored one value per primitive. That was the right
move, and it did not work, because the fold that consumes the column erases the
distinctions it records.

The pattern across four remediations is now stable enough to name precisely. It is
not that the producer writes columns nobody decided; it is that **the producer
places the point of judgement where it will be consumed by a total function.**
D-042 put it in a profile selected by a rule. D-043 put it in a column derived from
another column. D-045 put it in a column whose only consumer is a union that
saturates. Each time, the assertion written to defend it tests the presence of the
judgement rather than its consequence, and each time the assertion passes.

The test for iteration 7 is therefore not about a column. It is:

> **Take any single authored stream value in the package. Change it to something
> false. Does anything other than a freeze hash change?**

Today the answer is no, for every one of the 62 values, in both directions. Until
one authored value has one observable consequence that a validator can lose, the
delivery stream axis is a naming convention, and no amount of assertion count will
make it an evidence model.
