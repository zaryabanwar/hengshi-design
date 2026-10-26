# MA-029 current accessibility definition review

Date: 2026-10-03. Independent nonauthor reviewer. Result: **FAIL**.
Scope: current uncommitted definitions and evidence obligations, not application conformance.
Authority: D-045 accepted model/obligations, corrected model section 4.2, D-047 amendment, D-051–D-057 decisions.
Historical proposed headers and original unresolved gates are read with their superseding decisions.
No Figma call, implementation, publication, commit, push, B01 release or founder approval is granted.

## Coverage and verification

- PASS: inspected actual shared resolver; alternative host union intersects required content support.
- PASS: public navigation/booking/recovery retain four streams; World HUD excludes S-SEMANTIC; staff has explicit excluded scope.
- PASS: independent local mapping regression reproduced 1000 checks / 440 frame obligations.
- PASS: regression mutations reject altered host presence, missing hosts, malformed declarations, scope mixing and disappearing recovery states.
- PASS: per-stream evidence tokens distinguish streams; this does not verify complete manifest identity. Empty held manifests do not discharge evidence.
- PASS: native radios, checked/pending versus in-force names, explicit Apply, visible advisement, no-op and Escape exception definitions.
- PASS: D-051 privacy location, D-052 confirmed reset, D-054 native rendering, D-055 backing safeguards and D-057 exact copy remain bounded.
- PASS: requirement homes for read failure, ceiling refusal, reset and Focus Not Obscured; legal facts and measured results remain held.
- FAIL: remaining requirement homes, boundary evidence allocation, acceptance-test completeness and current contract consistency below.
- Reported producer runs: UX 113/0; design 207/1, with uncommitted-scope guard. These are determinism evidence only, not this verdict's basis.
- Visual values, geometry, bounded scene inputs and later real browser/AT measurements remain legitimate future gates, not automatic definition failures.

## Findings

### A-01 HIGH — accepted obligations lack requirement-level homes

Evidence: `accessibility/DELIVERY_STREAM_ACCESSIBILITY_OBLIGATIONS.md:918` (OBL-TRACE-02), especially lines 923–940;
`docs/active/Hengshi_Design_SRS_v3.md:150`–157 and 265–271.
Cause: the new read/reset/ceiling/focus rows do not carry explicit requirements for SC 1.4.13 expanded hotspot labels or SC 2.2.1 user time limits.
Persistent preference write-failure behavior and complete bidirectional/ancestor/announcement ordering remain specified outside requirement rows rather than fully reconciled there.
Impact: a producer can satisfy listed requirement rows while omitting accepted additional-content, timing or boundary/persistence safeguards.
Exit: mechanically reconcile the accepted obligations into requirement-level homes and resolved UX/design traces, preserving held durations and legal decisions.
For hover/focus content, state dismissibility without moving focus where applicable, hoverability, persistence and a non-navigating dismissal mechanism or supported exception.
Do not invent a new product policy or treat a generic WCAG target as the missing explicit homes.

### A-02 HIGH — required distinct boundary evidence is not allocated

Evidence: `accessibility/DELIVERY_STREAM_ACCESSIBILITY_OBLIGATIONS.md:632`–753; `design-batch-plan.csv:2`, `:8`.
Cause: B01 names same-shell STATE-STREAM-CHANGED evidence; B07 describes the announcement without moving focus, with no boundary qualifier.
Neither batch explicitly allocates distinct destination-focused boundary and nearest-ancestor frames with the required five-step tree/region/focus/message/canvas annotation.
Impact: same-shell evidence can be mistaken for the opposite boundary-focus behavior; prose alone cannot discharge OBL-BND-01/03/04.
Exit: assign the distinct boundary and ancestor evidence to appropriate existing templates/batches in both directions, retaining same-shell frames separately.
Require visible destination focus, incoming empty region before message, named location/substitution, and canvas added last only in 3D destinations.

### A-03 HIGH — stream acceptance tests do not cover the accepted obligations

Evidence: `accessibility/DELIVERY_STREAM_ACCESSIBILITY_OBLIGATIONS.md:965`–996;
`docs/phase-1-ux-architecture/CONTENT_ANALYTICS_TESTS.md:152`; `foundation-flow-coverage.csv` COV-ACT-09 linked_tests.
Cause: UXTEST-046 is the sole stream-explicit UX test; it omits empty-region-before-message, visibly focused arrival, canvas-last and ancestor substitution predicates.
There are no complete stream-specific persistence-failure and semantic-only end-to-end predicates for booking, contact, AI, handoff and media opt-in.
Impact: generic failure/motion tests plus a combined selection test can pass while the accepted T-STREAM-05/06/07 behaviors fail.
Exit: reconcile the seven accepted test obligations into independently checkable tests or explicit equivalent acceptance sections and bind their action/flow traces.
Keep future keyboard/screen-reader execution distinct from the current definition regression; approved copy is D-057, not an unresolved copy choice.

### A-04 MEDIUM — current design contract contradicts the resolved mapping and naming grammar

Evidence: `UI_REFERENCE_DESIGN_CONTRACT.md:184`–208 and `:290`;
`DELIVERY_STREAM_EVIDENCE_MODEL.md:309`–345; `scripts/validation/ui-stream-mapping.ps1:410`–428; production `evidence-capture-plan.csv:9`.
Cause: contract section 6 still omits mandatory stream/scope segments; section 9 still says union of all primitive dependencies.
Impact: following the current contract produces invalid evidence names or incorrectly expands shared-component presence, although the resolver correctly rejects these outcomes.
Exit: reconcile this active contract with approved host-union/content-intersection and per-stream / excluded-scope naming, including its worked example.

## References and disposition

- W3C Understanding SC 1.4.13: Content on Hover or Focus.
- W3C Understanding SC 2.2.1: Timing Adjustable.
These informative primary references clarify the accepted obligations; no implementation was audited.
Already accepted D-045 behavior supports mechanical requirement/test/evidence/grammar reconciliation for A-01–A-04; no new policy approval is implied.
If hotspot-label dismissal requires choosing new key precedence, geometry or an exception, an independent accessibility author must propose it before founder approval; the reviewer does not select that mechanism.
MA-029 accessibility exit is not clean. B01 remains held. Revise the identified definitions and obtain independent verification; no accepted founder choice is reopened.

## Current independent re-review — 2026-10-03

Current definition/verifier verdict: **PASS**, with zero remaining CRITICAL, HIGH or MEDIUM accessibility definition findings in the reviewed snapshot. The original FAIL above is preserved as historical review evidence.

Reviewer: `review_privacy_definition`. Producers of the reviewed corrections: `root` and `verify_r044`. This is independent definition review, not a per-batch exit review or artifact acceptance.

Scope: current design, production and UX definition packages, accepted D-045/D-047 and D-051 through D-060, requirement homes, primitive/template/profile/flow/batch mappings, tests, evidence allocation and necessary computable verifier coverage.

- A-01 closed: requirement homes now explicitly carry hotspot hover/focus dismissal and persistence, boundary ordering, preference persistence and assigned timing branches; their UX/design traces retain future execution evidence.
- A-02 closed for definition: D-060 allocates eight distinct B07 destination triples and twelve directed mapped/ancestor cases. Allocation-only states cannot leak into ordinary profiles or stream generation; destination-visible focus, ordered annotations and ancestor substitution are required. Undeclared directions, missing or duplicate origin cases and same-shell substitutions reject. Independent focused regression: PASS 44 checks, 440 ordinary obligations, eight boundary triples and twelve directed cases.
- A-03 closed: UXTEST-046 carries seven independently checkable T-STREAM predicates, including semantic end-to-end processes and persistence failures, bound to applicable actions/flows. Future execution must supply separate evidence and verdicts.
- A-04 closed: active naming grammar and mapping contract agree with stream/scope identity and host-union/content-intersection resolution. Independent mapping regression: PASS 1026 checks / 440 ordinary frame obligations.
- Current D-057 copy-hold finding closed: B01/B07 producer instructions and TR-REQ-103/TR-TEST-046 require the accepted copy bundle; verified runtime placeholders and final legal content remain gated.
- D-051 privacy coverage independently verified: the necessary coverage helper requires an actual privacy route-instance FRAME or FOCUSED_FRAME in every resolved stream; REF, Credits instances and instance sheets cannot substitute. Independent focused regression: PASS 21 checks.
- Durable acceptance and lifecycle guards preserve explicit founder authorization, frozen manifest/review/archive bindings, exact identity and required coverage. Definition mode cannot certify a batch exit; necessary computable coverage does not replace qualitative independent review.

Snapshot: 74 files; aggregate SHA256 `027E4DFCEB674AFF84B39B82B93096CB8EADB178E090CDD489509BC30FB29D2B`, supplied by the coordinating producer for binding this review record.
Recipe: ordinal-sort repository-relative paths; include the design, production and UX packages' MD/CSV/PS1 files excluding `/reviews/`, `scripts/validation/*.ps1`, and AGENTS, constitution, PROJECT, DECISIONS, TASKS, active SRS/style guide and foundation 06 route JSON. For each file use uppercase SHA256, two spaces and its path; join with LF without a terminal newline, encode UTF-8 without BOM, then SHA256 the aggregate bytes.

Remaining gates: UG-2/UG-6 visual values and direction, UG-4 implementation measurements, approved geometry and bounded scene inputs, final legal facts/content, actual browser/keyboard/screen-reader/magnifier evidence and measured conformance. Historical resolved UG choices are not reopened. These future production inputs are not current definition defects.

This PASS grants no B01/B07 visual production, external design write, runtime or visual conformance claim, pilot acceptance/release, founder phase acceptance, application implementation, publication, commit or push. B01 remains held; the founder and separate production/release gates remain authoritative.
