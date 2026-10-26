# Delivery Stream Evidence Model — **[PROPOSED SPECIFICATION]**

**Status: [PROPOSED SPECIFICATION]. Pending founder decision. Not accepted
authority. Nothing in this document is implemented, and no conformance of any
kind is claimed here or anywhere in the package it describes.**

**Author:** independent specification author. I did not produce the CR-002
package, the D-042 remediation, or the D-043 remediation, and I did not write any
validator under review. This document is written under the founder decision
recorded at D-044 that the delivery-stream evidence model is **defined by
reviewers, implemented by the producer, and verified by reviewers**.

**Date:** 2026-09-06
**Inputs:** `reviews/design-review-iteration-5.md` (B-01…B-06, S-01…S-04,
M-01…M-04); `accessibility/accessibility-audit-iteration-4.md` (B-01…B-05,
S-01…S-09, M-01…M-06); the 7 design CSVs; `UI_REFERENCE_DESIGN_CONTRACT.md` §4.2
and §9; `validation/validate-ui-reference-design.ps1` lines ~300–400;
`docs/phase-1-ui-reference-production/` including `evidence-capture-plan.csv`
(`EC-01`…`EC-30`), `batch-production-plan.csv`, `validation/mcp-call-budget.csv`;
`docs/active/3D_Mega_Menu_Style_Guide_v2.md` §8.1, §8.2.x.

**Scope of change:** this specification governs one bounded slice covering
**both** `docs/phase-1-ui-reference-design/` **and**
`docs/phase-1-ui-reference-production/`. Per the founder decision, the production
package's missing stream axis is not a follow-on; it is in the same slice,
because a per-stream evidence obligation that cannot be named by `EC-08` and
would be rejected by `EC-30` is not an obligation.

**Not authorized by this document:** application implementation, external writes,
Figma or Stitch MCP calls, publication, deployment, or the release of batch
**B01**. B01 remains held.

---

## 0. Summary of the decision this specification makes

**Mapping amendment authorized 2026-09-23:** the founder approved correcting
screen-to-stream mapping and its regression checks. Section 4.2 below supersedes
the original union of all dependencies. Alternative hosts determine a screen's
scope; shared content cannot expand it. The staff evidence suffix below also
supersedes EC-08 for excluded surfaces only. Other review findings and the B01
hold are unaffected.

| # | Question | Decision |
|---|---|---|
| 1 | Does stream-invariance exist? | **No.** The concept is deleted, not narrowed. `DS-STREAM-INVARIANT` is removed from the matrix and the `stream_profile` column is removed from all three record files. |
| 2 | Where do per-stream obligations attach? | **Declared at the primitive. Computed at the template. Inherited, uncomputed and unstored, at route and flow.** No per-record stream column exists at any level except the primitive. |
| 3 | What is the stream-dependence rule? | A resolvable predicate over `component-primitives.csv.stream_presence` folded across `reference-template-inventory.csv.primitive_dependencies`, cross-checked against the independently authored `foundation-route-coverage.csv.immersive_stream_representation`. |
| 4 | Net schema change | **−1 column across 3 files (163 derived cells deleted), +1 column across 1 file (62 human decisions added), −1 matrix row.** Net surface reduced. |
| 5 | `EC-08` stream token | Mandatory `STREAM_<HIGH\|MEDIUM\|LOW\|SEMANTIC>` segment, positioned between `<MODE>` and `V<NN>`, with no omissible or aggregate form. |
| 6 | B01 frame impact | Roughly **+15 frames** on a current base of roughly 14–20 under the union reading — approximately a doubling. **Zero necessary increase in metered MCP calls.** See §8. |

---

## 1. The defect this model is designed to be incapable of reproducing

Four remediations have failed independent review. The reviewers named one
pattern twice and generalised it a third time:

- **D-042:** *an assertion that passes by counting rows rather than resolving
  references.* Four `DS-S-*` profile rows existed; the assertion counted them; no
  record selected one.
- **D-043:** the same count, one level up. `delivery-stream-record-coverage`
  asserts `Count -eq 44` — a row count, written inside the assertion added to fix
  a row count.
- **Accessibility iteration 4, generalised:** *an assertion that classifies
  records by a proxy enforces the proxy, not the rule.* `stream_profile` is a
  total function of `state_profile`, so no human decided any of its 163 values,
  and a producer who correctly assigned all four `DS-S-*` to `ROUTE-BOOK` would
  **fail** `delivery-stream-assignment`.

This specification adopts three structural rules. They are normative and every
clause below is checked against them.

> **SR-1 — Single point of judgement.** A design fact is decided in exactly one
> place, by a human, on a record where being wrong is possible. Everywhere else
> it is **computed at validation time and never stored**. A stored copy of a
> computable fact is a defect, not redundancy.
>
> **SR-2 — Every assertion resolves a reference.** An assertion states which
> identifier in file A it resolves against which identifier set in file B. An
> assertion whose failure message contains a bare count of rows is prohibited.
> The one legitimate use of a count is comparing two independently derived
> counts, which is a resolution.
>
> **SR-3 — No silent default and no omissible value.** Every axis value is
> explicit on every record it governs. There is no blank, no "n/a", and no value
> whose meaning is "nobody looked". Where an obligation is genuinely deferred,
> the deferral names the batch it is deferred to.

**SR-1 has a consequence the producer must not soften.** Applying it honestly to
the current package also condemns `time_limit_branch`, which
`Get-ExpectedTimeBranchForState` computes as a total function of `state_profile`
in exactly the same shape as `stream_profile`. That is outside this
specification's mandate, and it is recorded here as **[UNRESOLVED GATE] G-5**
rather than silently fixed or silently ignored.

---

## 2. Decision 1 — Stream-invariance does not exist, and the concept is deleted

### 2.1 The finding

`DS-STREAM-INVARIANT`'s own `exception_rule` reads:

> *"This profile may never be selected by a record whose rendering depends on the
> World canvas or on the shell that hosts the delivery stream control; such
> records must select all four `DS-S-*` profiles."*

`PRIM-001` "Public semantic shell" is that shell. Its `required_anatomy` ends
`…;delivery stream control`. Its `required_variants` are
`public;no_script;offline;unsupported_browser;prior_release;stream_high;
stream_medium;stream_low;stream_semantic`. Its transactional states include
`stream-selected` and `stream-preference-write-failed`.

**All 19 route templates depend on `PRIM-001`.** I resolved
`primitive_dependencies` across `reference-template-inventory.csv` and confirmed
this directly. All 34 routes resolve to one of those 19 templates. Therefore the
`exception_rule` **prohibits the assignment the producer made, on every route and
on every route template** — 34 of 34 routes and 19 of 19 route templates.

Three further primitives — `PRIM-042` World onboarding and return choice,
`PRIM-043` World HUD, `PRIM-044` World escape and recovery — also carry
`delivery stream control` in `required_anatomy`. Between them and `PRIM-001`,
every shell in the product hosts the control.

### 2.2 The decision

**Stream-invariance is not a category any record may claim, and it is not
preserved in weakened form.**

The founder's instruction was to prefer deleting a concept over adding one, and
to delete a category that only serves to exempt if the honest answer is "almost
none" or "none". The honest answer is **none**, and the reason is not accidental:
the delivery stream control is *in the shell*, so anything rendered inside a
shell is rendered inside something that has four per-stream variants. There is no
public visitor surface that escapes it.

Accordingly:

- **`DS-STREAM-INVARIANT` is deleted** from `responsive-state-mode-matrix.csv`.
- **The `stream_profile` column is deleted** from
  `foundation-route-coverage.csv`, `foundation-flow-coverage.csv`, and
  `reference-template-inventory.csv`.
- The four `DS-S-*` profile rows are **retained**, amended per §7.1. They remain
  the definition of what per-stream evidence *is*; they are no longer selected by
  a `stream_profile` cell on any record.

I considered and rejected the accessibility reviewer's structural
recommendation 1 — retaining `DS-STREAM-INVARIANT` but making it selectable only
by a record with no `immersive_stream_representation` and no dependency on a
primitive with per-stream variants. That recommendation is correct about the
test, and the reviewer states plainly that on current data the resulting class is
**zero routes**. A category with zero members, guarded by a condition, is a
category that exists solely to be claimed later by a record nobody examined. The
test survives in this specification, as §3's resolution and §6's assertion
`A-06`. The category does not.

### 2.3 The test, stated so it can be applied and failed

Because the concept is deleted, the test is not "prove invariance" but its
inverse, applied at the only level where a human decides anything:

> **T-INV.** A primitive is present in a stream if and only if a visitor served
> that stream can perceive or operate it. For each primitive and each of the four
> streams, the producer answers a single yes/no question: *can a visitor in this
> stream reach this primitive?* A "yes" creates a per-stream evidence obligation
> for that primitive in that stream. There is no third answer meaning "yes but
> it looks the same as another stream". Two streams never share a frame.

**Why no sharing is the correct rule and not over-caution.** Style guide §8.2
distinguishes `S-HIGH`, `S-MEDIUM` and `S-LOW` by texture, shadow and richness,
which is to say by *rendered pixels*. Contrast, focus-indicator visibility
(`NFR-A11Y-005`, ≥3:1 against adjacent scene colour) and target geometry are
therefore different measurements in each of the three World streams by
construction, and different again in `S-SEMANTIC`. A shared frame would be
precisely the "aggregate evidence that names no stream" the `DS-S-*` rows already
forbid.

---

## 3. Decision 2 — Where per-stream evidence obligations attach

**This is the central design decision, and the founder's framing of it is
correct.**

### 3.1 The locus

| Level | File | Stream fact | How |
|---|---|---|---|
| **Primitive** | `component-primitives.csv` | **Declared** | New column `stream_presence`. 62 human decisions. This is the only place a stream fact is authored. |
| **Template** | `reference-template-inventory.csv` | **Computed** | Union of alternative host presences, intersected with required content presences; staff scope handled separately. Not stored. |
| **Route** | `foundation-route-coverage.csv` | **Inherited** | Via `template_id`. Not stored. Cross-checked against `immersive_stream_representation`. |
| **Flow** | `foundation-flow-coverage.csv` | **Inherited** | Via `template_ids`. Not stored. |
| **Batch** | `batch-production-plan.csv` | **Declared** | New column `stream_disposition`. 9 human decisions about deferral, not about variance. |

### 3.2 Reasoning

**Why the primitive, and not the route.** Whether a surface renders differently
per stream is a fact about the *component that renders*, not about the URL that
requests it. `ROUTE-HOME` and `ROUTE-CREDITS` do not independently decide whether
the semantic shell has four variants; `PRIM-001` decides that, once, and both
routes inherit it. Authoring the same fact 34 times at route level is what
produced 163 cells nobody decided. Authoring it 62 times at primitive level is
what makes each cell a decision someone can get wrong.

**Why the primitive is where being wrong is possible.** `PRIM-043` World HUD
exists in `S-HIGH`, `S-MEDIUM` and `S-LOW` and does not exist in `S-SEMANTIC`.
`PRIM-001` exists in all four. `PRIM-046` staff authentication exists in none,
because staff surfaces are excluded surfaces outside the four-stream visitor
experience. Those three answers are genuinely different, genuinely contestable,
and not derivable from any existing column. A reviewer can look at `PRIM-041`
Context panel — variants `semantic_inline;world_panel;staff_side_panel` — and
argue about whether it is present in `S-SEMANTIC` as `semantic_inline`. That
argument is the point. No such argument was possible about any of the 163
`stream_profile` cells.

**Why template is computed and not declared.** Once the primitives carry the
fact, the template's answer is fully determined by its composition. Storing it
would violate **SR-1** and would recreate exactly the failure mode of
`stream_profile`: a second copy that can silently disagree with the first, with
no rule for which wins. The founder's hypothesis — that attaching at template
and primitive level with routes and flows inheriting transitively may remove the
need for any per-record column — is **confirmed for routes and flows, and refined
for templates**: templates need no column either, because template composition is
already fully recorded in `primitive_dependencies`.

**Why routes and flows carry nothing at all.** A route's stream obligation is
exactly its template's. A flow's is the union across `template_ids`. Both are one
join away. This is the finding that closes design review **B-02** and **B-03** at
the root: `COV-ACT-02` "Open canonical route" — whose `template_ids` are
`TPL-GLOBAL-NAVIGATION;TPL-QUICK-ACCESS-RECOVERY`, both stream-varying — cannot
be marked invariant, because there is no cell in which to mark it. It resolves,
or the validator fails.

**Why the batch declares deferral and nothing else.** `B07` is deferred under
MA-025, so World-stream obligations for World-hosted templates cannot be
discharged on the authorized path. That is a *programme* fact, not a *rendering*
fact, and it belongs on the batch. `EC-14` already demonstrates the mechanism
(`deferred_B07;deferred_B09`); §5.4 reuses it rather than inventing one.

### 3.3 The one data correction this model requires

The model is only sound if `primitive_dependencies` is **complete**, including
the shell that hosts the template. It is currently incomplete in a way that
matters:

- `TPL-DIRECTORY-SEARCH` lists `PRIM-004;PRIM-005;PRIM-019;PRIM-020;PRIM-040;
  PRIM-057;PRIM-058;PRIM-061` — no host shell. But `PRIM-043` World HUD's
  `required_anatomy` includes `directory and search`, and the template plainly
  also renders inside `PRIM-001`. It is hosted by both and lists neither.
- `TPL-SYSTEM-RECOVERY` lists no host shell, yet is reachable in the semantic
  shell and, per `PRIM-044`'s anatomy, in World recovery.
- `TPL-AI-CONCIERGE`, `TPL-HUMAN-HANDOFF`, `TPL-MEDIA-OPT-IN` and the four
  booking flow templates list no host shell. Accessibility audit **M-01** is
  correct that a concierge panel over a 3D scene and a concierge page in the
  semantic shell are not the same rendering; under this model that is not fixed
  by a vocabulary change but by recording the host.

**Normative requirement N-01.** Every template's `primitive_dependencies` must
include every shell primitive that hosts it. A shell primitive is any primitive
whose `primitive_category` is `shell_navigation` or whose `required_anatomy`
contains `delivery stream control`. A template that resolves to no shell
primitive is a validator failure (`A-07`), unless it resolves to an excluded
surface.

This is a **correction of existing data**, not a new column. It is the reason the
model does not need one.

---

## 4. Decision 3 — The stream-dependence rule, stated as a resolvable predicate

Notation: `presence(x) ⊆ {S-HIGH, S-MEDIUM, S-LOW, S-SEMANTIC}`.

### 4.1 Primitive level — declared

```
presence(p) = value of component-primitives.csv[p].stream_presence
```

Legal values: a semicolon-separated, ordinal-sorted subset of
`S-HIGH;S-MEDIUM;S-LOW;S-SEMANTIC`, **or** the literal token
`STREAM-SCOPE-EXCLUDED`.

- `STREAM-SCOPE-EXCLUDED` is legal **only** if every template depending on `p`
  resolves to a surface enumerated in
  `docs/phase-1-ux-architecture/excluded-surfaces.csv`. It means "outside the
  four-stream public visitor experience" — staff, admin, publication, audit. It
  does **not** mean "invariant" and it does **not** waive `S-SEMANTIC` for any
  public surface. Per **SR-3**, it is an explicit token, never a blank cell.
- A primitive whose `required_anatomy` contains `delivery stream control` must
  have `presence(p) ≠ STREAM-SCOPE-EXCLUDED` and must be present in at least two
  streams. A control that exists in one stream cannot change streams.
- `S-SEMANTIC ∈ presence(p)` is required for every `p` that is not
  `STREAM-SCOPE-EXCLUDED` **and** whose `primitive_category` is not
  `overlay_immersive`. `S-SEMANTIC` may never be marked absent for a
  non-immersive public primitive, because that is the WebGL-less visitor's only
  stream and the four streams carry equivalent core journeys.

### 4.2 Template level — computed, never stored

The host roles below are explicit contract decisions, not guesses from names,
categories, or whether a shared button happens to support a stream.

| Host primitive | Role | Required presence |
|---|---|---|
| `PRIM-001` | Public semantic shell | All four public streams |
| `PRIM-042` | World onboarding/return host | HIGH, LOW, MEDIUM |
| `PRIM-043` | World HUD host | HIGH, LOW, MEDIUM |
| `PRIM-044` | World recovery host | HIGH, LOW, MEDIUM |
| `PRIM-046` | Staff shell | `STREAM-SCOPE-EXCLUDED` |

Let H be the host primitives in `primitive_dependencies`, and C the remaining
required content primitives. Host entries are alternatives: a booking template
with both `PRIM-001` and `PRIM-043` can render in the semantic shell or World HUD.
It does not require both shells simultaneously.

```
public presence(T) = (union of presence(h), h in H)
                     intersect (intersection of presence(c), c in C)
staff presence(T) = empty public set; scope(T) = STREAM-SCOPE-EXCLUDED
```

An empty C imposes no further restriction. Every template needs a resolved host.
Mixed public/staff hosts, excluded content on a public host, unknown or duplicate
dependencies, malformed stream values, and an empty public result are errors.
Shared content on a staff host cannot turn it into a public screen. A changed
declaration for any listed host must agree with this table or validation fails.
`T` is **stream-dependent** iff its public presence contains at least two streams.

The two package validators use the same resolver in
`scripts/validation/ui-stream-mapping.ps1`. Regression checks cover every live
template plus mutations of hosts, shared content, and dependencies. Public routes
retain S-SEMANTIC; World-only screens must exclude it. Directory, booking, AI,
and recovery templates with alternative public hosts retain all four streams.

An excluded staff template's frame uses `_SCOPE_EXCLUDED_V<NN>` instead of a
`_STREAM_<name>_V<NN>` suffix. This is an explicit nonpublic scope marker, not a
fifth stream or a missing evidence requirement. Its declared evidence scope is
`STREAM-SCOPE-EXCLUDED`; public frames may not use it. B08's four public stream
dispositions are `not_present`; its staff evidence remains required separately.

### 4.3 Route level — inherited, never stored

```
presence(R) = presence( foundation-route-coverage.csv[R].template_id )
```

### 4.4 Flow level — inherited, never stored

```
presence(F) = ⋃ { presence(T) : T ∈ foundation-flow-coverage.csv[F].template_ids }
```

### 4.5 The independent cross-check that makes a record capable of being wrong

`presence(R)` above is computed from primitives. `foundation-route-coverage.csv`
*already* contains a second, independently authored statement of the same fact —
`immersive_stream_representation`, non-empty on 34 of 34 routes, describing a
distinct World rendering per route ("Reception/atrium orientation panel";
"Sequenced Strategy threshold; closed/held/opening/open"; "Booking panel"). Design
review **B-02** and accessibility **B-01** both used the contradiction between
that column and `DS-STREAM-INVARIANT` as proof. This specification turns that
proof into a standing assertion:

> **N-02 (route agreement).** For every route `R`:
> `immersive_stream_representation` is non-empty **⟺**
> `presence(R) ∩ {S-HIGH, S-MEDIUM, S-LOW} ≠ ∅`.

Neither side derives from the other: the left is authored prose about World
representation, the right is a fold over primitive composition. They can
disagree, and disagreement is a failure. **This is the answer to the reviewers'
closing question — "is there any record in the package whose stream fact a human
had to decide?"** Two humans decide independently, at different levels, in
different files, and the validator makes them agree.

### 4.6 What this predicate is not

It makes no reference to `state_profile`. It is not satisfiable by editing a
state column. It contains no hard-coded list of record IDs and no literal count.
Adding a new route with a new template composed of stream-varying primitives
produces the correct answer with no validator edit; that is the property
`delivery-stream-record-coverage` (`Count -eq 44`) lacks.

---

## 5. Decision 4 and 5 — Schema

### 5.1 `docs/phase-1-ui-reference-design/component-primitives.csv` — **+1 column**

| Column | Position | Legal values | Authored by |
|---|---|---|---|
| `stream_presence` | after `required_variants` | ordinal-sorted `;`-list, non-empty subset of `S-HIGH;S-MEDIUM;S-LOW;S-SEMANTIC`, **or** `STREAM-SCOPE-EXCLUDED` | Producer, one decision per primitive, 62 total; reviewed by both independent reviewers |

Constraints per §4.1. No blank cell is legal. The producer must record, in
`producer-inspection.md`, the one-line reason for every primitive whose value is
not all four streams — a reason a reviewer can dispute.

### 5.2 Three record files — **−1 column each**

Delete `stream_profile` from:

- `foundation-route-coverage.csv` (34 rows)
- `foundation-flow-coverage.csv` (89 rows)
- `reference-template-inventory.csv` (40 rows)

163 cells removed, none of which encoded a decision.

**Do not add a replacement column at any of these three levels.** Per §3.2 the
value is one join away at every level. If a future producer proposes storing the
computed value "for readability", that is `stream_profile` returning under a new
name and assertion `A-01` fails it.

### 5.3 `responsive-state-mode-matrix.csv` — **−1 row, 4 rows amended, 2 rows amended**

- **Delete** row `DS-STREAM-INVARIANT`.
- **Amend** `DS-S-HIGH`, `DS-S-MEDIUM`, `DS-S-LOW`, `DS-S-SEMANTIC` per §7.1 —
  strip World-specific content out of `minimum_evidence`, retaining only
  stream-generic obligations. This is what makes B01 satisfiable and is a
  precondition for releasing it.
- **Amend** `SP-NAVIGATION.required_values` to add `STATE-STREAM-CHANGED` and
  `STATE-PREFERENCE-WRITE-FAILED` (accessibility **B-03**). `TPL-GLOBAL-NAVIGATION`
  is the control's authorized home and carries `SP-NAVIGATION`; a state that
  cannot be named cannot be captured under `EC-03` or encoded under `EC-08`.
- **Amend** `MP-WORLD.exception_rule` to state the precedence explicitly
  (accessibility **S-05**): where the mode axis excludes a mode that a stream in
  `presence(record)` requires, **the stream axis prevails and the frame is
  drawn**. `MODE-PRINT` is excluded from the live World canvas and required by
  `S-SEMANTIC`; both are true and the frame is drawn in `S-SEMANTIC`. No
  precedence rule may be left to the producer to infer.

### 5.4 `docs/phase-1-ui-reference-production/batch-production-plan.csv` — **+1 column**

| Column | Legal value | Meaning |
|---|---|---|
| `stream_disposition` | exactly four `key=value` pairs, `;`-separated, ordinal-sorted by key, keys exactly `S-HIGH`, `S-MEDIUM`, `S-LOW`, `S-SEMANTIC`; each value ∈ `in_scope` \| `deferred_<BATCH_ID>` \| `not_present` | Per stream, whether this batch produces it |

Every stream is named on every batch row. **There is no omissible form**
(**SR-3**): a stream a batch does not produce must say which batch produces it, or
must say `not_present` and be validated as genuinely absent from
`⋃ presence(T)` over the batch's templates. Silence — the mechanism by which the
stream axis was absent from the production package entirely — becomes
inexpressible.

`B01`'s value under this model is
`S-HIGH=in_scope;S-LOW=in_scope;S-MEDIUM=in_scope;S-SEMANTIC=in_scope` for the
semantic-shell-hosted obligations, with World-content obligations deferred at
template granularity through `presence(T)` and `B07`. See §8.

### 5.5 Production evidence manifest — **+1 column**

`UI_REFERENCE_PRODUCTION_CONTRACT.md` §5.2 manifest columns become:

```
evidence_id, batch_id, evidence_type, template_id, instance_id, state_id,
viewport_id, mode_id, stream_id, profile_ids, prim_ids, time_limit_branch,
file_relpath, sha256, export_scale, exported_on, figma_node_id, revision
```

`stream_id` is **mandatory, single-valued**, and drawn from
`S-HIGH|S-MEDIUM|S-LOW|S-SEMANTIC`. Empty is illegal. Multi-valued is illegal.
A frame shows one stream or it is not evidence.

### 5.6 Columns explicitly **not** added

| Rejected | Why |
|---|---|
| `stream_profile` on routes/flows/templates | Derivable per §4.2–§4.4. This is the D-043 defect. |
| `stream_variance` enum on primitives | Under §2.2 every in-scope primitive varies, so the column would be constant on in-scope rows and would restate `STREAM-SCOPE-EXCLUDED`. `stream_presence` alone carries the only non-derivable content: *which* streams, which is what drives frame count. |
| `stream_critical_states` on templates | Computable per §7.2 as an intersection of two existing `critical_distinct_frame_values` sets. |
| `stream_deferral` separate from `stream_scope` on batches | Folded into one `stream_disposition` column whose grammar makes silence impossible. |

**Net: −1 column × 3 files, −1 matrix row, +1 column × 3 files (one design, two
production). 163 derived cells deleted; 62 decided cells added.**

---

## 6. Decision 6 — Validator assertions

Every assertion below states the reference it **resolves**. Per **SR-2** no
assertion's pass condition is a row count, and no failure message may contain a
bare count. Assertion IDs are proposals; the producer implements them in
`validation/validate-ui-reference-design.ps1` and
`validation/validate-ui-reference-production.ps1`.

### 6.1 Design package

**`A-01 stream-column-absence`** — *Resolves:* the header row of
`foundation-route-coverage.csv`, `foundation-flow-coverage.csv`,
`reference-template-inventory.csv` against a prohibited-column list. Fails if
`stream_profile`, or any column whose name contains `stream`, exists on any of
the three. Also fails if the token `DS-STREAM-INVARIANT` or the string
`stream-invariant` appears anywhere in the design freeze. *This is a deletion
guard; without it the concept returns.*
**Negative fixture:** reinstate `stream_profile` on one route row → FAIL.

**`A-02 primitive-stream-presence-legality`** — *Resolves:* every
`stream_presence` value against the four-token stream vocabulary, and every
`STREAM-SCOPE-EXCLUDED` primitive against `excluded-surfaces.csv` via the
templates that depend on it. Fails on an illegal token, a blank cell, an unsorted
list, or a `STREAM-SCOPE-EXCLUDED` primitive reachable from a non-excluded
template.
**Negative fixture:** set `PRIM-001.stream_presence = STREAM-SCOPE-EXCLUDED` →
FAIL, because `TPL-PUBLIC-HOME` is not an excluded surface.

**`A-03 template-stream-presence-resolution`** — *Resolves:* every ID in every
template's `primitive_dependencies` against `component-primitives.csv`, and
computes `presence(T)`. Fails if any dependency does not resolve or lacks a legal
`stream_presence`. *This is the assertion whose absence is why the current
`exception_rule` binds nothing: nothing resolved `primitive_dependencies` against
primitive stream data.*
**Negative fixture:** add `PRIM-999` to `TPL-WORLD-HUD` → FAIL.

**`A-04 flow-template-stream-resolution`** — **explicitly required by the
founder.** *Resolves:* every ID in every flow row's `template_ids` against
`reference-template-inventory.csv`, computes `presence(F)`, and resolves that set
against the `stream_disposition` of every batch that owns the flow's templates.
Fails if any flow has a stream in `presence(F)` for which no owning batch declares
`in_scope` or `deferred_<BATCH>`.
**Negative fixture (the exact B-03 case):** `COV-ACT-02` has `template_ids =
TPL-GLOBAL-NAVIGATION;TPL-QUICK-ACCESS-RECOVERY`. Set
`B01.stream_disposition` to omit `S-SEMANTIC` → FAIL. Under the current package
`COV-ACT-02` is marked `DS-STREAM-INVARIANT` and passes 189/189.

**`A-05 route-immersive-representation-agreement`** — *Resolves:*
`foundation-route-coverage.csv.immersive_stream_representation` (authored prose)
against `presence(route.template_id)` (computed fold), per **N-02** §4.5. Fails on
any disagreement in either direction.
**Negative fixtures:** (a) blank `ROUTE-BOOK.immersive_stream_representation`
while `TPL-BOOKING-SHELL` still depends on `PRIM-001` → FAIL; (b) remove
`PRIM-001` from `TPL-BOOKING-SHELL` while the representation stays populated →
FAIL. *Neither fixture is detectable by any assertion in the current validator.*

**`A-06 stream-sharing-prohibition`** — *Resolves:* the set of frames obliged for
each template (§7.2) against `presence(T)`, requiring one distinct obligation per
stream. Fails if any obligation is satisfiable by a frame that names more than
one stream, or if any two streams in `presence(T)` map to the same obligation.
*This is the "one frame set discharges all four streams" loophole, made
unexpressible rather than guarded.*
**Negative fixture:** any obligation carrying two stream tokens → FAIL.

**`A-07 stream-control-host-completeness`** — *Resolves:* every template's
`primitive_dependencies` against the set of shell primitives (those with
`primitive_category = shell_navigation` or `delivery stream control` in
`required_anatomy`), per **N-01** §3.3. Fails if a non-excluded template resolves
to no shell primitive. Also fails if any primitive with `delivery stream control`
in its anatomy has `|presence(p)| < 2`.
**Negative fixture (the current state):** `TPL-DIRECTORY-SEARCH` as it stands
today, listing no shell primitive → FAIL until §3.3 is corrected.

**`A-08 stream-state-availability`** — *Resolves:* for every template depending on
a stream-control-hosting primitive, the template's `state_profile` against the
required state vocabulary `{STATE-STREAM-CHANGED, STATE-PREFERENCE-WRITE-FAILED}`.
Fails if either state is absent from that profile's `required_values`.
**Negative fixture (the current state):** `TPL-GLOBAL-NAVIGATION` on
`SP-NAVIGATION`, which contains neither → FAIL until §5.3 is applied. *This closes
accessibility **B-03**.*

**`A-09 stream-mode-precedence-resolution`** — *Resolves:* each record's mode
profile exclusions against the mode requirements of each stream in
`presence(record)`. Every intersection where a mode is excluded by the mode axis
and required by the stream axis must be named by the amended
`MP-WORLD.exception_rule`. Fails on an unnamed intersection.
**Negative fixture:** revert `MP-WORLD.exception_rule` while `DS-S-SEMANTIC` still
requires `MODE-PRINT` → FAIL. *This closes accessibility **S-05**.*

**`A-10 baseline-frame-name-token-resolution`** — *Resolves:* every
`baseline_frame_name` in `reference-template-inventory.csv` and
`foundation-route-coverage.csv` by parsing it against the amended `EC-08` grammar
(§5.5, §5.7 below) and resolving each parsed token against the accepted value
sets — `<BATCH>` against `design-batch-plan.csv`, `<TEMPLATE>` against the
template inventory, `<STATE>` against the record's `state_profile.required_values`,
`<VIEWPORT>` and `<MODE>` likewise, `<STREAM>` against `presence(record)` — with
underscore/hyphen normalisation applied in **both** directions.
**Negative fixture (the exact surviving R-034 defect):**
`TPL-QUICK-ACCESS-RECOVERY.baseline_frame_name` contains
`MODE_NON_WEBGL_QUICK_ACCESS`, which normalises to `MODE-NON-WEBGL-QUICK-ACCESS`
and resolves against no accepted mode → **FAIL**.
*This replaces a vocabulary regex with a resolution, and is why it catches what
two successive widenings of `semantic-stream-peer-framing` did not.*

**`A-11 inert-column-detection`** — *Resolves:* each declared design-judgement
column against every other column in the same file, testing whether the mapping
is single-valued across all rows. Reports every inert column; fails on any inert
column in the design-judgement set. *This is the generalised guard against the
recurring pattern, and it is the assertion that would have failed D-043 on the day
it was written.*
**Negative fixture:** reintroduce `stream_profile` as any total function of any
other column → FAIL.
**Known current result:** `browser_profile` is inert and legitimately so (one
accepted profile, declared in the contract) and must be listed as an explicit
exemption with its reason in the validator source. **`time_limit_branch` is inert
with respect to `state_profile`** and is **not** exempt — see **[UNRESOLVED
GATE] G-5**.

### 6.2 Production package

**`A-12 evidence-id-grammar-resolution`** — *Resolves:* every manifest
`evidence_id` by parsing the amended `EC-08` grammar and resolving each token
against the accepted sets, including `<STREAM>` against `stream_id` on the same
row and against `presence(template_id)`. Fails on a parse failure, an unresolved
token, or a `<STREAM>` token disagreeing with the row's `stream_id`.
**Negative fixtures:** (a) an `evidence_id` with no stream segment → FAIL;
(b) `STREAM_FALLBACK` → FAIL; (c) `stream_id = S-SEMANTIC` with
`…_STREAM_HIGH_V01` → FAIL.

**`A-13 batch-stream-disposition-resolution`** — *Resolves:* every batch's
`stream_disposition` keys against the four-stream vocabulary, every
`deferred_<BATCH>` value against `batch-production-plan.csv.batch_id`, and every
`not_present` value against `⋃ presence(T)` over the batch's templates. Fails on a
missing key, a deferral to a non-existent or non-deferred batch, or a
`not_present` claim contradicted by the computed union.
**Negative fixtures:** (a) omit the `S-SEMANTIC` key from any batch → FAIL;
(b) `S-SEMANTIC=deferred_B07` → FAIL, because `B07` is itself
`deferred_not_authorizable` and cannot receive a deferral from an authorized
batch; (c) `S-HIGH=not_present` on `B01` while `TPL-GLOBAL-NAVIGATION` depends on
`PRIM-001` → FAIL.

**`A-14 per-stream-frame-coverage-resolution`** — *Resolves:* for every template
in an authorized batch, the set of stream-critical obligations (§7.2) against the
manifest rows that resolve to that template, matching on `stream_id`. Fails if any
obliged `(template, stream-critical coordinate, stream)` triple has no resolving
manifest row and no `deferred_<BATCH>` disposition covering it.
**Negative fixture:** produce all of `B01` in one stream → FAIL naming the
missing triples. *Under the current production validator this passes, because no
rule checks a stream.*

**`A-15 stream-token-vocabulary-guard`** — *Resolves:* every `<STREAM>` token in
every `evidence_id`, filename and manifest field against the closed four-token
set, with hyphen and underscore forms normalised. Fails on any other token,
including any degradation-vocabulary spelling. Runs across the design, UX **and**
production packages.
**Negative fixture:** `STREAM_NONWEBGL` or `STREAM_FALLBACK` anywhere → FAIL.

**`A-16 framing-guard-scope`** — *Resolves:* the file set the
`semantic-stream-peer-framing` guard scans against the union of the design, UX
and production package file lists. Fails if any file in those three packages is
outside the guard's scope. *The guard's narrowing to 13 design files is the
mechanism by which both surviving R-034 instances evaded it; this makes the scope
itself a checked reference rather than a literal in the validator source.*
**Negative fixture:** the guard as scoped today → FAIL.

### 6.3 Assertions to delete

`delivery-stream-assignment` (enforces the `state_profile` proxy and forbids the
correct answer) and `delivery-stream-record-coverage` (`Count -eq 44`) are
**deleted**, not amended. `delivery-stream-token-legality` and
`profile-reference-resolution`'s stream clause are amended to operate on
`stream_presence` instead of `stream_profile`.

---

## 7. The `DS-S-*` profiles and the frame-count control

### 7.1 `minimum_evidence` must be stream-generic

Design review **B-05** is correct and this is the fix. The `DS-S-*` rows currently
carry World-shaped `minimum_evidence` — "Reception and one open room at VP-320 and
VP-DESKTOP", "keyboard focus frame on a hotspot", "screen-reader annotation of the
HUD" — while `B01`'s templates (`TPL-GLOBAL-NAVIGATION`, `TPL-DIRECTORY-SEARCH`,
`TPL-SYSTEM-RECOVERY`) contain no room, no hotspot and no HUD. The producer is
instructed to photograph things that do not exist on the surfaces assigned.

**Normative requirement N-03.** A stream profile's `minimum_evidence` states only
what is true of *any* record evidenced in that stream. It retains:

1. contrast, target size and focus order measured against **this stream's own
   rendering**, never inherited from another stream;
2. the delivery stream control shown reporting **this stream** as current, with
   its accessible name legible in the annotation;
3. the mode set this stream requires (`MODE-LOW-POWER` for `S-LOW`;
   `MODE-FORCED-COLORS` and `MODE-PRINT` for `S-SEMANTIC`; and so on);
4. the prohibition on degradation vocabulary in any annotation;
5. `DS-S-SEMANTIC`'s existing `exception_rule` **verbatim and unweakened** — never
   marked not applicable, never drawn as `STATE-WEBGL-UNSUPPORTED`, no failure
   heading, no error styling, no language of escape, recovery or fallback. Both
   reviewers found this correctly written; it is not touched.

It **relocates** to `reference-template-inventory.csv.minimum_reference_evidence`
on `TPL-WORLD-SHELL` and `TPL-WORLD-HUD`: Reception, the open room, the hotspot
focus frame, the HUD annotation. Those obligations survive intact; they attach to
the templates that actually contain those things, which are `B07` templates.

**N-03 is a precondition for releasing B01.** Without it the reviewers' B-05
contradiction stands and metered calls buy frames a later review rejects.

### 7.2 The stream axis multiplies a bounded set, not the whole matrix

Without an explicit intersection rule, a four-stream obligation crossed with
viewport × state × mode is a combinatorial explosion that nobody will produce and
whose non-production will be discovered late. The `DS-S-*` rows already gesture at
this ("Axis intersection is explicit and counted once"). This specification makes
it computable.

> **N-04 (stream multiplier).** For a stream-dependent template `T`, the
> per-stream frame obligation is exactly:
>
> **(a) Baseline** — one frame at `T`'s declared baseline coordinate, in each
> stream in `presence(T)`; **plus**
>
> **(b) Stream-critical states** — for each state in
> `criticalStates(T.state_profile) ∩ ⋃ criticalStates(DS-S-*)`, one frame in each
> stream in `presence(T)`.
>
> Every other required viewport, state and mode value is covered **once**, in any
> single stream of the producer's choice, annotated with the stream it was drawn
> in. The stream axis does **not** multiply the viewport × state × mode
> cross-product.

`criticalStates` reads `critical_distinct_frame_values`. Both operands already
exist, so `(b)` needs no column (§5.6). Applying it to `TPL-GLOBAL-NAVIGATION`
after §5.3's `SP-NAVIGATION` amendment yields
`{STATE-OPEN, STATE-STREAM-CHANGED, STATE-PREFERENCE-WRITE-FAILED}` — the state at
rest, the moment of change, and the failure of the change. Those are exactly the
three the accessibility audit names as unevidenced, and they are derived, not
listed.

### 7.3 The stream control's role and advisement — accessibility **B-04**

The audit's B-04 is blocking, so this specification must satisfy it. Two clauses,
both **[PROPOSED]** and both founder-decidable:

> **N-05 (role and activation).** The delivery stream control is a **group of
> radio inputs with an accessible group name, plus an explicit Apply control**.
> It is **not** a native `select`, in which arrowing through options changes the
> value in several browsers — the textbook 3.2.2 failure the audit describes.
> Selection changes nothing until Apply is activated. `PRIM-001`, `PRIM-042`,
> `PRIM-043` and `PRIM-044` all specify this same control.

> **N-06 (advisement surface).** The advisement — that choosing a stream reloads
> the experience in that stream and keeps the current location — is **visible
> text adjacent to the group**, programmatically associated with it. An
> accessible description alone does not discharge 3.2.2, because a sighted mouse
> or keyboard user running no assistive technology receives nothing, and several
> common combinations do not announce `aria-describedby` on a grouping element.
> The accessible description is retained **in addition**, not instead.

`FR-3D-013`'s "does not move focus" and §8.2.4's "focus moves to the delivery
stream control in the destination shell" contradict each other (accessibility
**S-07**). Under N-05 the resolution is stated rather than inferred: **within one
shell, focus does not move; across the semantic boundary, where the outgoing
subtree is destroyed, focus moves to the control in the destination shell.**
`FR-3D-013` must be amended to carry both cases. That amendment is **outside this
specification's file scope** and is recorded in §9's migration list.

---

## 8. Decision 7 — B01, and the honest frame-count answer

### 8.1 What B01 must actually require

`B01`'s `required_visual_evidence` is rewritten to require, and to require only,
what B01's three templates can show:

1. The delivery stream control in the **semantic shell** (`PRIM-001`), proven
   present, keyboard operable, and reachable **without a canvas**, in each of the
   four streams — one frame per stream showing the control reporting that stream
   as current in its accessible name.
2. `STATE-STREAM-CHANGED` on `TPL-GLOBAL-NAVIGATION`, in each of the four
   streams: polite announcement, focus not moved within the shell, scroll, open
   panel and route preserved.
3. `STATE-PREFERENCE-WRITE-FAILED` on `TPL-GLOBAL-NAVIGATION`, in each of the four
   streams, following the `ACT-11` pattern.
4. The **visible** advance advisement (N-06) and the radio-group-plus-Apply
   activation model (N-05).
5. Everything B01 already requires that is not stream-scoped: the shell frames,
   narrow disclosure, no-results / index-unavailable / offline / error, 404 / 410,
   forced-colors, grayscale, unavailable font and image, keyboard, screen reader,
   `BP-NFR-006` proof, `TL-WARN-EXTEND` proof.
6. **Explicitly not required in B01:** Reception, rooms, hotspots, the HUD, and
   every other World-content obligation. Those relocate to `B07` templates under
   N-03 and are carried on `B01.stream_disposition` only as the template-level
   deferrals `presence(T)` and `B07` already express.

The sentence "Stream-invariant records carry the `DS-STREAM-INVARIANT`
profile…" is **deleted** from `B01.required_visual_evidence`.

### 8.2 Resolving the three-way contradiction the reviewers found

B-05 identified three mutually exclusive instructions. The resolution is a stated
precedence, not a reconciliation:

- `UI_REFERENCE_PRODUCTION_CONTRACT.md` §0.1's "the four-stream reference
  evidence is therefore not produced under this contract" is **too broad and must
  be narrowed**, to: *four-stream **World** evidence is deferred to B07;
  four-stream **semantic-shell** evidence of the delivery stream control is
  produced in B01.*
- `RISKS.md` **R-036 stays open**, with its scope narrowed to the World half. Its
  standing sentence — "no document may state that the four-stream obligation is
  met" — is **retained verbatim**. B01 discharges a named part of it and does not
  close it.
- `design-batch-plan.csv` `B01.status` is `future_not_authorized` while
  `batch-production-plan.csv` carries `B01` as `authorized_pilot` at execution
  order 1 (design review **M-04**). The two files must be made to agree in this
  slice; which value is correct is a founder decision, recorded as **[UNRESOLVED
  GATE] G-4**.

### 8.3 Frame-count impact — the number the founder asked for

Counting rule, stated because the package does not state one: I use the **union
reading**, where each `critical_distinct_frame_values` entry must appear in at
least one frame, rather than the cross-product reading. That the package leaves
this ambiguous is itself a finding — see **[UNRESOLVED GATE] G-3** — and under the
cross-product reading both the base and the delta scale by roughly the same
factor, so the *ratio* below is stable and the *absolute* numbers are not.

| Template | Streams present | Today | Under this model | Δ |
|---|---|---|---|---|
| `TPL-GLOBAL-NAVIGATION` | 4 (`PRIM-001`) | ~3 | 3 stream-critical states × 4 = **12** | **+9** |
| `TPL-DIRECTORY-SEARCH` | 4 via `PRIM-001`; World-HUD hosting deferred to B07 | ~1 baseline | baseline × 4 = **4** | **+3** |
| `TPL-SYSTEM-RECOVERY` | 4 via `PRIM-001`; World recovery via `PRIM-044` deferred to B07 | ~1 baseline | baseline × 4 = **4** | **+3** |

**B01 delta ≈ +15 frames on a base of roughly 14–20. Approximately a doubling of
B01's frame count.**

### 8.4 The cost answer, stated precisely

**The metered unit is the MCP call, not the frame.** `CB-01` fixes the allowance
at 20 Figma MCP tool calls per calendar month; `CB-10` records a three-call
mandatory overhead per batch; `CB-13` directs the producer to batch evidence
capture to the coarsest granularity that still satisfies `EC-01`…`EC-06`.

Therefore: **+15 frames does not imply +15 calls, and on a correctly batched
export it need not imply any additional call at all.** Frames are composed inside
the Figma file and exported in batched operations; the additional cost is
producer time and reviewer time, not allowance.

I will not offer a call-count projection, and the producer must not either.
`CB-09` prohibits stating a schedule for any batch until B01 reports a **measured**
per-batch projection, and `CB-08` makes B01 the metering experiment precisely
because projecting from an unmeasured assumption is the failure mode that rule
exists to prevent. The honest statement to the founder is: *the frame count
roughly doubles; the call count is unknown until B01 measures it; and B01 is the
cheapest possible place to be wrong about it.*

**The countervailing saving is real and larger than the delta.** Under N-03 the
World-content obligations wrongly attached to B01's three non-World templates are
removed. Those obligations are currently **unsatisfiable** — a producer asked to
photograph a room in `TPL-DIRECTORY-SEARCH` either omits the frame (and fails a
later review) or fabricates one (and fails `EC-18` and `SC-01`). Either outcome
spends metered calls on frames that must be redrawn. Removing them is why this
slice is cheaper than releasing B01 as it stands.

---

## 9. Decision 8 — Migration

### 9.1 Design package

| File | Change |
|---|---|
| `component-primitives.csv` | **Add** `stream_presence` after `required_variants`; 62 values, each a decision, each with a one-line reason in `producer-inspection.md` for any value that is not all four streams. |
| `reference-template-inventory.csv` | **Delete** `stream_profile`. **Correct** `primitive_dependencies` per **N-01** so every template resolves to its host shell. **Relocate** the World-specific `minimum_evidence` from the `DS-S-*` rows into `TPL-WORLD-SHELL` and `TPL-WORLD-HUD` `minimum_reference_evidence` per **N-03**. **Regenerate every `baseline_frame_name`** under the amended `EC-08` grammar (§5.7), which as a side effect removes `MODE_NON_WEBGL_QUICK_ACCESS` from `TPL-QUICK-ACCESS-RECOVERY`. |
| `foundation-route-coverage.csv` | **Delete** `stream_profile`. **Regenerate** `baseline_frame_name`. `immersive_stream_representation` is retained unchanged and becomes load-bearing under `A-05`. |
| `foundation-flow-coverage.csv` | **Delete** `stream_profile`. |
| `responsive-state-mode-matrix.csv` | **Delete** `DS-STREAM-INVARIANT`. **Amend** the four `DS-S-*` rows per **N-03**, `SP-NAVIGATION.required_values` per §5.3, `MP-WORLD.exception_rule` per §5.3. |
| `design-batch-plan.csv` | **Rewrite** `B01.required_visual_evidence` per §8.1. **Resolve** the `status` disagreement per **G-4**. |
| `traceability.csv` | **Add** rows for `NFR-A11Y-001`…`007` and `FR-3D-010`…`FR-3D-014`, none of which is traced today (accessibility **B-05**). Without them the requirements that give this package a home have no downstream reference. |
| `UI_REFERENCE_DESIGN_CONTRACT.md` | **Rewrite §9's** stream paragraph: delete the `DS-STREAM-INVARIANT` sentences, state §4's predicate, state **N-04**'s multiplier, state §5.3's mode precedence. **Amend §4.2** to delete "an assigned `stream_profile`" and replace it with the route's obligation to carry an `immersive_stream_representation` that agrees with its template's computed presence (**N-02**). |
| `README.md` | **Delete** the claim that per-stream evidence is "a resolvable obligation rather than a claim in prose" (accessibility **M-03**) until `A-03`, `A-04` and `A-05` exist and a reviewer has confirmed them. |
| `DESIGN_SYSTEM_IMPLICATIONS.md` | Hash-pinned and read-only in this package; the absence of any stream axis, any delivery-stream control component, and any tokens for its four values (accessibility **S-09**) is **[UNRESOLVED GATE] G-6**. |
| `validation/validate-ui-reference-design.ps1` | **Delete** `delivery-stream-assignment` and `delivery-stream-record-coverage`. **Add** `A-01`…`A-11` with the negative fixtures of §6.1 exercised and recorded. |

### 9.2 Production package — same slice, not a follow-on

| File | Change |
|---|---|
| `evidence-capture-plan.csv` | **Amend `EC-08`** to `HSD_UIR_<BATCH>_<TEMPLATE>_<INSTANCE>_<STATE>_<VIEWPORT>_<MODE>_<STREAM>_V<NN>`, where `<STREAM>` is `STREAM_HIGH`, `STREAM_MEDIUM`, `STREAM_LOW` or `STREAM_SEMANTIC`, mandatory on every evidence ID with no omissible or aggregate form. **Amend `EC-09`** so the revision-lineage key is the tuple `(BATCH, TEMPLATE, INSTANCE, STATE, VIEWPORT, MODE, STREAM)` and `V<NN>` increments only within it. **Amend `EC-30`** so the append-only identity is the **full** `evidence_id` including `<STREAM>`, which is what makes two frames of one template in `S-HIGH` and `S-SEMANTIC` two artifacts rather than an illegal overwrite. **Add `EC-31`** (per-stream coverage, verified by `A-14`), **`EC-32`** (exactly one stream per manifest row; empty and multi-valued are illegal), **`EC-33`** (stream deferral recorded in `stream_disposition`, mirroring `EC-14`'s existing mechanism). |
| `batch-production-plan.csv` | **Add** `stream_disposition` per §5.4, on all nine rows. **Rename** `B07.batch_name` from "Optional World HUD and Quick Access parity" to the design package's "Core delivery-stream World HUD and semantic peer parity" — this is the verbatim string R-034 is recorded closed against, still in the repository. |
| `UI_REFERENCE_PRODUCTION_CONTRACT.md` | **Add** `stream_id` to the §5.2 manifest columns. **Narrow** §0.1 per §8.2. **Delete** the superseded paragraph asserting the D-042 remediation "has not been re-reviewed since" (design review **M-03**). |
| `validation/validate-ui-reference-production.ps1` | **Add** `A-12`…`A-16` with the negative fixtures of §6.2 exercised and recorded. |

### 9.3 Adjacent packages

| File | Change |
|---|---|
| `docs/active/3D_Mega_Menu_Style_Guide_v2.md` | §8.2.4: **N-05** role and activation model, **N-06** visible advisement. §8.2's opening present-indicative equivalence needs the same dated decision header §8.2.2 received (accessibility **M-06**). |
| `docs/active/Hengshi_Design_SRS_v3.md` | **Amend `FR-3D-013`** to carry both the same-shell case (focus not moved) and the boundary case (focus moves to the control in the destination shell), which today contradict §8.2.4 (accessibility **S-07**). |
| `docs/phase-1-ux-architecture/CONTENT_ANALYTICS_TESTS.md` | **Add `UXTEST-046`** exercising `ACT-09`: stream selection, keyboard operability, accessible name, the polite announcement, the visible advisement, and the semantic boundary crossing. The word "stream" appears in none of the 45 existing tests, and `COV-ACT-09` is still linked to `UXTEST-007` and `UXTEST-025`, which fitted its predecessor "Toggle quality" under failure conditions (accessibility **B-05**). |
| `docs/phase-1-ux-architecture/` — `UX_ARCHITECTURE.md`, `STATES_AND_RECOVERY.md`, `excluded-surfaces.csv`, `FLOWS.md`, `README.md` | Degradation and ladder vocabulary survives here, outside the guard's 13-file scope: "optional World are utilities", "J-02 Optional immersive discovery", "Visitor explicitly selects optional World", "Optional immersive shell; never required", "**Quality downgrade** never removes content", "ACT-06 Enter **optional World**" (design review **S-01**, accessibility **M-02**). `A-16` makes the guard's scope a checked reference so this cannot recur silently. `README.md:43`'s "All 33 route definitions" against a 34-row parity file is design review **M-01**. |

### 9.4 Ledgers

| Ledger | Entry |
|---|---|
| `DECISIONS.md` / `docs/decisions-log.md` | New **[PROPOSED]** decision recording: reviewers define the model (already at D-044); stream-invariance deleted rather than narrowed; obligations attach at primitive and template with routes and flows inheriting; the production stream axis fixed in the same slice. Record the rejected alternative (retaining a guarded `DS-STREAM-INVARIANT`) and **why** — a zero-member guarded category is a place to hide. |
| `RISKS.md` **R-034** | **Reopens, third time.** Both surviving instances are named: `batch-production-plan.csv` B07 `batch_name`, and `MODE_NON_WEBGL_QUICK_ACCESS` in `TPL-QUICK-ACCESS-RECOVERY.baseline_frame_name`, which evades a hyphen-shaped guard because frame names use underscores. **Exit evidence:** `A-10` resolves frame-name tokens against accepted value sets with both separators normalised; `A-15` closes the stream-token vocabulary; `A-16` makes the guard's file scope a checked reference; and **an independent reviewer**, not a producer sweep, confirms the sweep. R-034's own text already records that a third closure requires independent verification; that condition binds this slice. |
| `RISKS.md` **R-035** | Stays open. Exit evidence unchanged: a clean independent design review **and** a clean independent accessibility review of the package as it then stands. |
| `RISKS.md` **R-036** | Stays open, scope narrowed per §8.2. "No document may state that the four-stream obligation is met" is retained verbatim. |
| `RISKS.md` **R-032** | Closure is correct; the cited evidence cell still reads "enumerates 33 routes" and describes a state that does not exist (design review **M-02**). Correct the cell, not the closure. |
| **New risk** | The `EC-08` grammar change invalidates **every** `baseline_frame_name` in the design package, all of which predate the stream token. A partial regeneration leaves a mixed grammar that `A-10` will fail. Regeneration is all-or-nothing within this slice. |
| **New risk** | `stream_presence` is 62 producer judgements reviewed by two reviewers. If the producer sets every value to all four streams, the column becomes inert and `A-11` will not catch it, because an all-constant column is functionally dependent on nothing. **The reviewers must check `PRIM-042`, `PRIM-043` and `PRIM-044` specifically**: a World HUD present in `S-SEMANTIC` is a false claim, and it is the cheapest available way to make this column mean nothing. |
| `MANUAL_ACTIONS.md` | **MA-029 is not discharged.** Add a manual action for founder decision on this **[PROPOSED SPECIFICATION]**, and a second for reviewer verification of the producer's implementation of it. B01 stays held; no metered call is authorized. |
| `TASKS.md`, `CHANGELOG.md`, `PROJECT_STATE.yaml` | Record the slice and the held state of B01. |

---

## 10. Unresolved gates

Marked rather than invented, per the constraint that a fact not establishable
from the package is a gate.

| ID | Gate | Why it is not decided here |
|---|---|---|
| **G-1** | **Does a WebGL-capable visitor with no stored signal land in the World or in the semantic shell at first paint?** Style guide §8.2.2 makes `S-LOW` the unsignalled default and `S-LOW` is a World stream; `UX_ARCHITECTURE.md:173` says the World is entered only when the visitor explicitly selects it. Design review **S-02**. | Two accepted authorities contradict each other on a founder-decided point. It determines the single most-produced frame in B01 — what the first frame of `ROUTE-HOME` shows. It does **not** change this model's structure: `presence(R)` is computed from composition either way. It changes which stream the producer draws first. |
| **G-2** | **U-03 device-tier thresholds.** | Already deferred to implementation-phase measurement. No threshold is invented here, and none is needed: this model never reads a tier. |
| **G-3** | **Do `critical_distinct_frame_values` cross-product across axes, or must each value appear in at least one frame?** | The package does not say. §8.3 uses the union reading and says so. The absolute frame counts in §8.3 depend on this; the ratio does not. |
| **G-4** | **Is B01 authorized?** `design-batch-plan.csv` says `future_not_authorized`; `batch-production-plan.csv` says `authorized_pilot` at order 1. Design review **M-04**. | A founder decision, not a producer reconciliation. Both files must then carry the same answer. |
| **G-5** | **`time_limit_branch` is inert with respect to `state_profile`**, computed by `Get-ExpectedTimeBranchForState` in exactly the shape that condemned `stream_profile`. | Outside this specification's mandate. Surfaced rather than fixed or ignored, because `A-11` will report it and the producer must not be left to decide silently whether to exempt it. |
| **G-6** | **`DESIGN_SYSTEM_IMPLICATIONS.md` has no stream axis**, no delivery-stream control component, and no tokens for its four values or the 3D focus ring. Accessibility **S-09**. | Hash-pinned, specialist-owned, read-only inside this package. It is the artifact implementation inherits, and it currently carries none of the amendment's accessibility substance. |
| **G-7** | **The `S-SEMANTIC` boundary crossing at `STATE-SLOT-SELECTED`.** What happens to a visitor who selects `S-HIGH` mid-booking with a verified email and a held slot. Accessibility **S-01**. | If the process restarts, that is 3.3.7 Redundant Entry and a lost booking. Not decidable from the package. |

---

## 11. What a reviewer verifying the producer's implementation must check

Not "does the validator pass". Four questions, in order:

1. **Is there any record in the package whose stream fact a human had to decide?**
   There must be exactly 62, in `component-primitives.csv`, each with a stated
   reason. If they are all `S-HIGH;S-LOW;S-MEDIUM;S-SEMANTIC`, the column is inert
   and the answer is no.
2. **Can a record be wrong?** Blank `ROUTE-BOOK.immersive_stream_representation`
   and confirm `A-05` fails. Remove `PRIM-001` from `TPL-BOOKING-SHELL` and
   confirm `A-05` fails in the other direction. Run every negative fixture in §6.
3. **Does any assertion pass by counting rows?** Grep the validators for
   `-eq <literal>` in an assertion's pass condition. The only legitimate form is
   the comparison of two independently derived quantities.
4. **Can a per-stream frame be named, distinguished and validated end to end?**
   Take one obligation — `TPL-GLOBAL-NAVIGATION` at `STATE-STREAM-CHANGED` in
   `S-SEMANTIC` — and follow it from `PRIM-001.stream_presence` through
   `presence(T)`, through **N-04**, through `B01.stream_disposition`, into an
   `EC-08` evidence ID, into a manifest `stream_id`, into `A-14`. If it breaks at
   any link, the axis is inert again.

**No conformance is claimed by this document.** Nothing is built. This
specification governs what evidence must be produced, not what any produced
evidence would prove. Whether the four streams are equivalent in a running
product, whether WCAG 2.2 Level AA is met, and whether `S-SEMANTIC` is usable are
implementation and audit questions that no reference-design package can pre-empt.

**[PROPOSED SPECIFICATION] — pending founder decision. B01 remains held.**
