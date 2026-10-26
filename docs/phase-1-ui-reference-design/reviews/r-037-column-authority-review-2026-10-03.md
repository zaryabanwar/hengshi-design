# R-037 / G-5 independent column-authority proposal review

Date: 2026-10-03. Reviewer: `review_privacy_definition`; proposal author: `verify_r044`.
Verdict: **PASS for the revised proposal**, with zero open CRITICAL, HIGH or MEDIUM findings.
Reviewed proposal SHA256: `FDDAD88D763CCC32686711A6F3EF5AE47D352F72059058AC299B80DF67006D18`.
This is nonauthor definition review, not approval of the future registry, its actual record assignments, implementation, runtime or browser conformance.

## Source observations and authority

- Independently read and recomputed the four live CSVs under the exact current A-11 classifiers/targets at `validation/validate-ui-reference-design.ps1:669-704`: 35 routes, 89 flows, 40 templates and 62 primitives; all 22 targets have multiple values; 14 targets have at least one observed classifier dependence. All proposal table counts at `COLUMN_AUTHORITY_PROPOSAL.md:36-57` agree.
- The correlated targets are route template/state/viewport/mode/activation/time-limit, flow viewport/mode/time-limit, and template surface/state/viewport/mode/time-limit. No primitive target is correlated under that classifier set. Finite-inventory dependence is not an authoritative derivation.
- Accepted `UI_REFERENCE_DESIGN_CONTRACT.md:117-140` gives route/flow assignments distinct instance/process meanings; `:282-290` distinguishes assigned states from the already computed stream axis. No accepted total resolver makes these 22 targets derived. Keeping them DECLARED therefore avoids inventing inheritance or deleting judgments from observed equality.
- `DELIVERY_STREAM_EVIDENCE_MODEL.md:583-595` and DECISIONS D-044/D-045 G-5 establish the affected authority boundary. The proposal explicitly amends A-11/G-5; it does not claim the current diagnostic-only implementation already satisfies the original general failure rule.

## Guard and timing review

- Each of the 22 recommendations has an individual decision meaning and minimum guard (`COLUMN_AUTHORITY_PROPOSAL.md:36-57`). Exact-reference guards remain necessary, while semantics are independently examined against the actual affected records.
- Initial MEDIUM finding, now closed in revision 1: the original “fail an unreviewed change” lacked an operational binding and per-record timing seam. The saved revision at `:79-129` defines exact registry/record keys, 1146 current target-cell bindings, source snapshots/selectors/quoted predicates, founder and nonauthor-review hash binding, and distinct stale-byte versus semantic-mismatch failures. It does not allow a generic approved decision or PASS receipt to certify source truth.
- The G-5 replacement at `:131-170` names each of 164 route/flow/template branch cells, its actual complete process, applicability, selected branch and typed obligations. It preserves pre-start off/adjust, at least 20-second warning, at least ten-times extension, data/authoritative-state preservation and applicable accessible reauthentication. Conditional protection does not assert a limit already exists. Durations, exceptions and implementation truth remain held.
- Negative seams cover missing/duplicate cells, mutated values, source-byte drift, irrelevant sources/processes, stale or generic approval, mismatched review hashes, unsupported timing applicability and omitted protection. Neither row counts nor nonempty rationale nor statistical variation substitutes for those criteria.
- The browser-profile exemption and exact BP-NFR-006 guard remain; the stream-presence hard legality/host/discriminator guard remains (`:173-175`). Computed template/instance stream presence is not reintroduced as stored authority. Correlation becomes diagnostic only for these approved DECLARED decisions, not a stream-axis exemption.

## Disposition and remaining gates

Present the revised 22-column DECLARED bundle and explicit G-5 authority replacement for founder acceptance. No actual registry, approval record, CSV change, proxy removal or validator implementation is approved by this review.
After that decision, actual record criteria and source relevance still require nonauthor inspection under the proposed binding before implementation acceptance. Independent implementation verification must exercise the stated negative seams; definition evidence cannot certify runtime timing or browser behavior.
B01, Figma/external writes, application changes, publication, commits and pushes remain separately gated. No new user limit, duration, exception or production claim is selected.
