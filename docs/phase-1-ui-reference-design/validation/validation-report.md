# UI Reference-Design Contract Validation Report

**Evidence date:** 2026-09-06  
**Package revision:** CR-002 revision window, delivery-stream evidence model D-045  
**Supersedes:** the 2026-09-03 producer-freeze report (iteration 3 of 3), which
described a 33-route, 32-profile package, and the D-043 report, which described a
37-profile package with an assigned stream column; both are retained only in git
history  
**Status:** deterministic validation PASS; **the package has not been
independently re-reviewed and R-035 remains open**

## Command

```powershell
pwsh -NoProfile -File docs/phase-1-ui-reference-design/validation/validate-ui-reference-design.ps1
```

## Result

```text
COUNTS routes=34 exclusions=9 wayfinding=15 actions=53 ux_tests=46 flow_families=12 source_experience_ids=32 flow_rows=89 templates=40 primary_template_owners=40 route_template_refs=19 flow_template_refs=29 profiles=36 browser_profiles=1 time_limit_profiles=4 primitives=62 batches=9 primary_source_owners=155 trace_rows=287 package_csv=7 package_json=0
RESULT=PASS PASS_COUNT=208 FAIL_COUNT=0
```

## What this report is not

**A passing validator is a determinism check, not a review.** This has now been
demonstrated three times, and this run adds a fourth demonstration from inside the
validator itself (see below). The 2026-09-03 report recorded `PASS_COUNT=183
FAIL_COUNT=0`; an independent design review and an independent accessibility
review then returned **FAIL** with four blocking findings each, none of which any
of those 183 assertions could detect. The D-042 remediation again passed every
assertion, and two further independent re-reviews again returned **FAIL** —
converging on five identical defects, including one in this very file.

Nothing below should be read as approval. Under Constitution 2.0.0 §VII the
producer does not approve their own material output, and this report was written
by the producer.

## Two defects this run found that no prior run could

`A-10` replaces a vocabulary regex with a resolution, and it immediately caught two
frame names that had passed every previous validator:

- `TPL-QUICK-ACCESS-RECOVERY.baseline_frame_name` contained
  `MODE_NON_WEBGL_QUICK_ACCESS`, which normalises to a mode that resolves against no
  value in `MP-PUBLIC`. This is the **surviving R-034 instance**. It evaded the
  `semantic-stream-peer-framing` guard for a mechanical reason worth recording: the
  guard's alternation matched `MODE-NON-WEBGL` with hyphens, and the defect was
  spelled with underscores inside an identifier. The guard has been widened to both
  spellings, but the widening is not why the defect was found — the resolution is.
- `ROUTE-CONTACT.baseline_frame_name` contained `STATE_UNAVAILABLE`, which is not in
  `SP-CONTACT.required_values`. **No reviewer reported this one.** It is a token that
  looks plausible and resolves against nothing; corrected to
  `STATE_CHANNEL_UNAVAILABLE`.

All 74 baseline frame names were regenerated in one pass under the amended `EC-08`
grammar. This was deliberately all-or-nothing: a partial regeneration leaves a mixed
grammar in which `A-10` resolves the old-form names cleanly and fails only the
corrected ones, so the migration would punish exactly the rows it fixed.

## A third defect, found in this validator's own guard

The peer-framing pattern was one long string literal, and five of its own
alternatives matched it. That was tolerable only because a reader could be told to
discount them. Assembling the alternatives at run time removes the need for that
instruction — but the first run-time version was **silently inert**, and the way it
failed is worth recording because no runtime warning was emitted.

In PowerShell the comma operator binds tighter than `+`. An array literal written as
`@('a' + 'b', 'c' + 'd')` therefore does **not** build two elements: it parses as
`'a' + ('b','c') + 'd'` and collapses into a **single** string joined by `$OFS`. The
nine alternatives became one element, `-join '|'` had nothing to join, the
alternation degraded to one space-separated literal, and the guard reported zero hits
across 56 files while six live UX-package files still carried the abolished
vocabulary. Every element is now parenthesised, and
**`degradation-pattern-alternative-count`** asserts the count is nine, so a
collapsed literal fails loudly instead of passing quietly.

This is the D-045 defect shape — an assertion that cannot fail — reintroduced by the
producer *while implementing the remedy for it*, and caught only because the
production package's `A-16` scans a wider file set and was cross-checked by hand
against a phrase known to be present. It is recorded here rather than quietly fixed,
because the frequency of this defect class is itself the finding.

## Why this report was rewritten

The report frozen at D-042 stated `routes=33 … profiles=32 … PASS_COUNT=183`
while the validator in the same freeze asserted 34 routes and 36 profiles. A
freeze that certifies a report describing a different package certifies nothing.
Both re-reviewers found this independently.

Two guards were added so the defect cannot recur silently:

- **`validation-report-counts-agreement`** — the `COUNTS` line in this file must
  be a literal substring match against the counts the validator computes in the
  same run. If this file drifts from the package, the run fails.
- **`evidence-date`** — this file must carry the current evidence date.

## Coverage

The validator parses all seven package CSV files, the accepted source route JSON,
and seven accepted-source CSV files. It preserves the prior exact-set, ownership,
frame-alignment, booking-independence, review-gate, local-reference, secret,
extension, date, and scope checks, and verifies the two stable specialist
artifacts by their supplied SHA-256 hashes.

It proves deterministically that:

- the normative target is WCAG 2.2 Level AA for every applicable full page and
  complete process, including represented third-party steps, while no current
  visual or implemented conformance is claimed;
- all 34 routes, 89 flow/source records, 40 templates, 36 profiles, and B01–B09
  map to `BP-NFR-006`;
- **the delivery-stream axis resolves rather than counts (D-045, `A-01`–`A-11`).**
  No route, flow, or template row carries a stream column and `A-01` fails if one
  returns. Every primitive declares an ordinal-sorted `stream_presence` drawn from
  the closed four-token vocabulary or the single `STREAM-SCOPE-EXCLUDED` token, and
  no excluded primitive is reachable from a routed surface (`A-02`). Every
  template's `primitive_dependencies` resolve against that column and fold to a
  computed presence set (`A-03`), which every route-reachable template must contain
  `S-SEMANTIC` in. Flows resolve their templates and every stream in the computed
  presence is owned by a batch owning one of those templates (`A-04`). Authored
  `immersive_stream_representation` agrees with the computed fold in both
  directions (`A-05`). No stream-critical obligation names more than one stream and
  no two streams collapse onto one obligation (`A-06`) — this is the whole of what
  the deleted invariance profile used to claim, expressed as a test that cannot be
  selected into. Every non-excluded template resolves to a host shell primitive and
  every stream-control host is present in at least two streams (`A-07`). Every
  template hosted by a stream-control surface selects a state profile offering
  `STATE-STREAM-CHANGED` and `STATE-PREFERENCE-WRITE-FAILED` (`A-08`). Every mode
  excluded by a mode profile and required by a stream in that record's presence is
  named by a written precedence rule (`A-09`). Every `baseline_frame_name` parses
  under the amended `EC-08` grammar, which carries a mandatory single-valued
  `<STREAM>` segment with no aggregate form, and each parsed token resolves against
  the value set the record itself selects (`A-10`);
- `BP-NFR-006` fixes the current latest two stable Chrome, Edge, Firefox, and
  Safari release families at the later dated QA run, Safari/iOS 16.4 as the
  minimum legacy floor, mobile Safari layout/input/virtual-keyboard/safe-area
  evidence, and the semantic stream for below-floor or otherwise unsupported
  clients;
- all route, flow, template, profile, and batch records select a resolvable
  `TL-*` branch, derived from the state profile rather than asserted; warning and
  extension evidence uses at least 20 seconds and at least 10 times, preserves
  permitted data and last authoritative state, and provides accessible
  reauthentication while exact durations remain gated;
- no current record selects undocumented `TL-EXCEPTION`; negative fixtures reject
  a mockup-only conformance claim, vague browser support, and threshold-free
  timeout language;
- no package record frames the semantic stream as a degradation, a fallback, or
  an optional extra; and
- MA-024 and the separate external-write gate remain package-only proposals at
  the 2026-09-03 producer freeze, with root integration deferred until clean
  independent design and accessibility reviews.

## Known limits of the assertion set

Recorded because the reviewers named them, not because they are resolved:

- **Twenty-two judgement columns are inert and unadjudicated.** `A-11` emits an
  `INERT-REPORT` line for every column that is a total function of a classification
  the package already makes. `stream_presence` is **not** among them — that is a
  hard failure and the run passes it — but `template_id`, `state_profile`,
  `viewport_profile`, `mode_profile`, `activation_status`, `surface_kind`, `gate`'s
  neighbours and `time_limit_branch` variously are. `browser_profile` is the one
  declared exemption, with its reason in the validator source: exactly one accepted
  profile exists, so a constant column asserts nothing and hides nothing.
  **`time_limit_branch` is inert with respect to `state_profile` and is not
  exempt.** No decision has been taken on the remaining twenty-two. They are
  reported and not failed, because failing them would be the producer choosing
  which of the package's own columns carry judgement — the exact authorship the
  producer is barred from. **This is the largest open finding in this run.**
- **`A-11`'s determiner set is a producer reading, not a specified one.** The
  accepted specification says to test each judgement column "against every other
  column in the same file". Taken literally that is vacuous — every column is a
  total function of its file's primary key, so the literal reading fails every
  column including `stream_presence`. The implemented reading restricts determiners
  to columns that are themselves classifications, which is the shape the defect
  actually took. The determiner set is written out in one place in the validator
  source so a reviewer can disagree with it there.
- **`A-08` implicates eleven state profiles the specification's migration table
  did not enumerate.** `N-01` puts the semantic shell in almost every template's
  dependencies, and `A-08` requires every stream-control-hosted template's state
  profile to offer `STATE-STREAM-CHANGED` and `STATE-PREFERENCE-WRITE-FAILED`.
  Fourteen profiles are implicated; the table named one. The other eleven were
  amended as a mechanical derivation, not a design choice.
- **The staff, publication and audit templates fold to all four streams.** They
  depend on primitives that are legitimately present in all four, so §4.2's union
  fold yields all four even though those templates serve excluded surfaces. The
  fold has no exclusion for excluded-surface templates. Implemented literally as
  specified and recorded here rather than repaired, because repairing it would be
  the producer authoring the model again.
- **The UX architecture package still carried the abolished vocabulary until this
  run.** Six files — `UX_ARCHITECTURE.md`, `STATES_AND_RECOVERY.md`, `FLOWS.md`,
  `README.md`, `excluded-surfaces.csv`, and `CONTENT_ANALYTICS_TESTS.md` — described
  the World as optional and the stream axis as a quality ladder, more than three days
  after D-039 abolished that framing in the design package. The design validator
  never looked outside its own thirteen freeze files, so nothing was wrong and
  nothing was checked. `A-16` now scans all three packages. **The general lesson is
  that a guard's scope is part of its claim**, and a scope stated as a literal file
  list ages silently.
- **The design system has no stream axis, and the file that would carry it was
  deliberately left untouched.** `DESIGN_SYSTEM_IMPLICATIONS.md` is one of the
  fourteen hash-pinned freeze files. It declares no stream axis, no stream-control
  component, no four stream tokens, and no 3D focus-ring token, so nothing in the
  design system yet expresses the axis this run made normative everywhere else. The
  founder's decision (gate G-6) was to **record the gap now and commission the
  amendment later as its own bounded specialist contract**, precisely so the producer
  does not author design-system content while implementing an evidence model. One
  edit to that file was made during this run and **reverted**; the freeze hash is
  intact and `design-system-freeze-hash` passes. Tracked as an open risk.
- **`U-03`** — exact device-tier thresholds are deferred to implementation-phase
  measurement and cannot be validated here.
- Nothing here proves visual quality, runtime or assistive-technology behaviour,
  current browser behaviour, provider or third-party behaviour, legal
  sufficiency, WCAG conformance, production readiness, route activation, or
  publication. No Figma screen exists and external design-write authorization
  remains false.

## Finding disposition

The deterministic evidence supports **producer** closure of A11Y-UIR-I1-001,
A11Y-UIR-I1-002, and A11Y-UIR-I1-003, and prior UIR-DR1-001 through UIR-DR1-006
regression checks remain passing. Closure is subject to independent design and
accessibility re-review of the D-043 remediation. **R-035 cannot be closed by the
producer.**

## Freeze hashing

The validator emits one SHA-256 for each of the 14 required files and a single
aggregate. It sorts relative forward-slash paths, formats each entry as uppercase
SHA-256, two spaces, then path, joins entries with LF and no terminal newline, and
hashes that UTF-8 no-BOM payload. The final command output is the authoritative
freeze manifest; embedding its aggregate in this included report would create a
self-referential hash.
