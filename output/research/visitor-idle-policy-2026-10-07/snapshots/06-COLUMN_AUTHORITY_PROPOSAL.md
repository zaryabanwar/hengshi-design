# R-037 / G-5 column-authority proposal

**PROPOSED — independent model author; nonauthor review and founder decision required.**
Date: 2026-10-03. Definition only: no CSV/schema, validator, application, provider,
time-limit value, publication or approval state is changed by this proposal.

## Actual source observation and authority

Recomputed the current A-11 algorithm over all four live CSVs: 35 route rows,
89 flow rows, 40 templates and 62 primitives. There are 22 target columns;
14 nonconstant targets have at least one observed classifier dependence.
These are correlations in this finite inventory, not authoritative derivations.
R-037's historical count is not the current measured result. Every target below
has more than one distinct value; none is being excused as constant.

D-044/D-045 SR-1 prohibits stored copies of an authoritative derived fact, not
independent decisions that happen to agree. Contract §4.2 assigns profiles to
route instances; §4.3 assigns them to flows; §9 assigns state profiles in both
coverage files. No accepted function mandates those assignments from a family,
another profile, reuse_scope, or a primary key. In particular all 35 route
profile/TL values currently equal their template values, but that observation
does not authorize deleting instance-level judgments or inventing inheritance.
The stream axis is different: its accepted derivation already exists in model
§4.2–4.4 and remains computed/inherited, never reintroduced as a stored column.

## Recommendation for each target

All 22 remain **DECLARED**, with the distinct decision meaning and guard below.
There is **no DERIVED deletion recommended**: no unambiguous accepted derivation
for any of these 22 was found. This is not a blanket inertness exemption.
An asterisk marks one of the 14 currently correlated targets; the number is its
distinct values. R/F/T/P identify the four existing CSVs, not new records.

| Owner / column | Values | Reviewed decision retained; minimum meaningful guard |
|---|---:|---|
| R template_id * | 19 | Route's reusable reference assignment; resolve its approved route ID/intent and exactly one existing template, never map solely from route_family. |
| R state_profile * | 7 | States owed by this route instance; resolve a state-dimension profile and instance success/failure/recovery evidence, plus baseline membership. |
| R viewport_profile * | 2 | Instance reflow/layout evidence; resolve a viewport profile with the mandatory BP-NFR-006 set and instance stress obligations. |
| R mode_profile * | 2 | Instance input/accessibility contexts; resolve a mode profile, applicable semantic journey and explicit approved exception rules. |
| R semantic_quick_access | 26 | The actual semantic instance journey; retain its canonical content/actions and equivalent destination, not a stream/family-derived slogan. |
| R immersive_stream_representation | 35 | The route's distinct immersive representation; retain A-05 agreement with resolved template presence and review the named representation. |
| R content_or_policy_gate | 26 | Instance-specific facts/permission/publication holds; resolve applicable source gates and prevent fixture or planning status becoming public approval. |
| R activation_status * | 2 | Current instance/pattern activation meaning; reconcile canonical route/release authority, enforce inactivity in this definition, and retain truthful-pattern holds. |
| R time_limit_branch * | 2 | Instance complete-process timing protection; apply the individual G-5 criterion below, not state_profile or route_family. |
| F state_profile | 16 | States owed by this action/flow; resolve the approved source success/pending/error/recovery contract and profile dimension. |
| F viewport_profile * | 4 | Flow's responsive evidence; resolve the required set and source interaction/layout obligations independently of its mode profile. |
| F mode_profile * | 4 | Flow's accessibility/input contexts; resolve the profile and source semantics independently of its viewport profile. |
| F gate | 82 | Flow-specific permission/content/operation conditions; resolve its source_id and applicable gate authority, not merely a nonempty cell. |
| F time_limit_branch * | 3 | Flow's complete-process timing protection; apply the individual G-5 criterion. |
| T surface_kind * | 3 | Reusable surface's actual composition role; validate the accepted kind and its host/content purpose, not reuse_scope text. |
| T state_profile * | 19 | Template's reusable state evidence contract; resolve its primitive/action obligations and distinct states, not reuse_scope. |
| T viewport_profile * | 4 | Master composition's responsive obligation; resolve the profile and its full-frame/critical/intermediate rules independently of mode_profile. |
| T mode_profile * | 4 | Master composition's verification contexts; resolve required modes and explicit precedence/exceptions independently of viewport_profile. |
| T time_limit_branch * | 3 | Template's complete-process timing protection; apply the individual G-5 criterion. |
| P primitive_category | 10 | Primitive's actual architectural role; validate the accepted vocabulary and anatomy/host/interaction contract. |
| P interaction_class | 4 | Primitive's actual operation/semantics; validate against required anatomy/actions and input/focus obligations, not category correlation. |
| P stream_presence | 3 | Primitive-level reachability judgment; preserve the existing hard legality/host/discriminator guard and independently review each declared presence. |

R=`foundation-route-coverage.csv`; F=`foundation-flow-coverage.csv`;
T=`reference-template-inventory.csv`; P=`component-primitives.csv`.
Sources: accepted UI_REFERENCE_DESIGN_CONTRACT.md §§4.2–4.3, 7–10.1, 13;
DELIVERY_STREAM_EVIDENCE_MODEL.md §§1, 4.2–4.5, 6.1 A-11 and gate G-5;
approved requirements/actions/UX tests referenced by the current rows.

## Minimal future guard and G-5 resolution

Replace the producer's undeclared A-11 interpretation with a reviewed 22-column
authority registry keyed by exact file/column. Each DECLARED target names its
actual decision meaning, source/criterion and applicable reference/evidence
guard from the table. Validate that registry exhaustively against the target set;
fail missing authority, unresolved criterion/references, forbidden derivation or
an unreviewed change. Report functional dependencies diagnostically, with the
actual determiner names; do not infer correctness or derivation from correlation.
Do not use row counts, primary-key uniqueness or mandatory statistical variation
as substitutes for resolving the declared authority. Necessary reference checks
remain machine-checked; semantic criterion truth requires independent review of
the actual affected records, not a producer-written assertion or receipt alone.

### Exact future artifact and approval binding

Use one future `column-authority.json` with `schema_version: 1` and closed
top-level fields `columns`, `source_snapshots`, `records`. `columns` contains the
exact 22 unique `(file,column)` entries above, each with `authority_kind: DECLARED`,
`criterion_id` and the table's decision meaning/guard. Do not generate a column's
authority from a classifier. Each snapshot is `(path,raw_sha256)`; paths are
repository-relative forward-slash paths and SHA-256 values are uppercase 64-hex.
Pin all four target CSVs and every criterion source file; reject duplicate paths.

`records` exhaustively resolves actual target cells, keyed by `(file,row_id,column)`.
Row keys are route_id, coverage_id, template_id and primitive_id respectively.
Each record has `declared_value`, `criterion_id`, `sources`, `rationale`, and,
only for time_limit_branch, `timing_criterion`. Resolve exactly one live row and
require declared_value to equal its cell verbatim. Require the record-key set to
equal the independently enumerated live 22-column target-cell set: 1146 currently,
but the exact keys, not that number, govern. Missing/extra/duplicate keys fail.

Each source has `path`, `selector`, `quoted_fact` and `supports` (the named
process/decision predicate it witnesses). Selectors have only these closed forms:
CSV `{kind: csv_record, key_field, key_value, field}` resolves one row/field;
JSON `{kind: json_pointer, pointer}` uses RFC 6901 and resolves one value;
Markdown `{kind: markdown_section, heading_path}` resolves an exact hierarchy of
heading texts uniquely, excluding child sections; `{kind: markdown_table_id,
id}` resolves exactly one first-cell identifier row, including requirement/action
IDs. Ambiguous headings/IDs, absent fields/pointers and wildcard/range selectors
fail. After line-ending normalization only, quoted_fact must occur verbatim in
that selected content. A registry value or its own target cell is not its sole
criterion witness. Requirement/action/route/process identity must resolve to the
approved source named by the record; unrelated generic policy is not sufficient
evidence of that record's applicability. Semantic relevance of supports and the
actual quoted fact is explicitly examined by the nonauthor reviewer.

A future accepted founder decision records `column_authority_registry_path`,
`column_authority_registry_sha256`, `column_authority_review_path` and
`column_authority_review_sha256`. The review is by a nonauthor and pins the same
registry raw hash and target snapshots, reports PASS with zero critical/high/medium
findings, and names its examined record keys and source/criterion conclusions.
Machine validation resolves that exact decision/registry/review binding and the
exact reviewed-key set; a generic approved decision or a PASS receipt alone cannot
certify criterion truth. The review must actually inspect the recorded cells and
source predicates. All three artifacts are immutable evidence of that approval.
No approval record is inserted by this proposal or automatically by a validator.

Raw-byte drift is a stale snapshot/approval failure even when meaning is unchanged;
refreshing it requires a reviewed scoped repin with provenance. Semantic mismatch
is separate: a resolved/pinned source contradicting the claimed process/predicate
fails review and needs an authorized correction, not a hash refresh. Proposed
edits cannot reuse the old receipt. Review a source/record delta and pin a new
complete registry/snapshot set after the applicable founder approval; preserve
the predecessor and its hashes. This is the concrete meaning of unreviewed change.

For each R/F/T time_limit_branch separately, name the affected complete process
and the accepted user-time-limit protection it represents. TL-NOT-APPLICABLE
means the definition introduces no user limit; provider delay/retry/system timeout
cannot justify or replace a branch. TL-REMOVABLE-ADJUSTABLE requires pre-start
off/adjust behavior; TL-WARN-EXTEND requires the accepted ≥20-second warning and
≥10-times extension, with data/authoritative-state preservation and accessible
reauthentication when applicable. Reject TL-EXCEPTION in this baseline; choosing
an exception or changing a branch is separately governed. Exact durations remain
gated. A branch's actual implemented truth is later QA, not this definition review.
Remove enforcement by Get-ExpectedTimeBranchForState only after approval of this
authority amendment; retain existing branch cells unless an individually reviewed
source contradiction requires a separately authorized correction. G-5 is not
exempted: its proxy rule is replaced by explicit per-record criterion assignment.

For each of the 164 current R/F/T branch cells, timing_criterion has closed fields
`process_source` (one of the source locators above), `applicability`,
`selected_branch`, `obligations`, `implementation_truth: future_qa_required`.
Applicability is `no_user_limit_declared`, `defined_user_limit`, or
`protection_required_if_user_limit_introduced`; it must describe the actual approved
complete-process definition, not be inferred from its profile. The first permits
only TL-NOT-APPLICABLE and no protection claims. The other two require the already
declared TL-WARN-EXTEND or TL-REMOVABLE-ADJUSTABLE branch and the applicable
obligations below; conditional protection does not claim a limit already exists.
selected_branch must equal the target cell. WARN obligations carry
`warning_seconds_min: 20`, `extension_factor_min: 10`,
`preserve_permitted_data: true`, `preserve_authoritative_state: true`, and
`accessible_reauthentication: required_if_protected_session`. REMOVABLE obligations
carry `before_start: turn_off_or_adjust`, the same preservation/reauthentication
obligations, and `adjustment_range: criterion_supported`. These are existing
protection constraints, never invented exact durations or implemented results.
No runtime-evidence assertion, duration field, new limit or exception is accepted.

Negative seams: remove/duplicate one record; mutate a cell without a new binding;
change source bytes while retaining its pin; resolve an unrelated process or
quote; supply a generic approved decision; mismatch review/registry hashes;
name only a family/profile as the timing process; mark NOT-APPLICABLE with a
defined user limit; omit WARN warning/extension or REMOVABLE pre-start control;
claim implementation truth from definition evidence. Each must fail at its
specific resolver/criterion seam. A source/profile change must never silently
rewrite a declared branch; any newly observed functional dependence is reported
for inspection, not treated as approval or an automatic branch generator.

Keep browser_profile's accepted BP-NFR-006 exemption and its exact resolution
guard. Keep stream_presence's current hard discriminator guard; this proposal
does not turn that axis into a diagnostic-only column or permit all-four copying.

## Derived changes, rollback and the actual founder decision

No inheritance or schema removal occurs now. A later DERIVED proposal must name
one already accepted source of truth, its exact total resolver, instance/flow
exception policy and negative tests; remove stored copies only after approval.
Its rollback restores the previous schema/approved row values and validator pins
from the preserved Git revision, without altering accepted product behavior.
Correlation, equal current values and a proposed resolver are insufficient authority.

Founder decision: accept or revise each of the 22 DECLARED recommendations and
their guard meanings in this one bundle; specifically accept the per-record G-5
authority replacement. This does not ask again about settled timing protection,
stream equivalence or browser policy, nor choose new durations or user limits.
If inheritance/deletion is preferred for a column, an explicit resolver/exception
contract is the missing material choice and needs independent definition first.
After nonauthor review and founder acceptance, implement only the approved
registry/guard reconciliation, revalidate, independently inspect and return for
the applicable governance acceptance. B01/Figma/application/Git gates stay held.
