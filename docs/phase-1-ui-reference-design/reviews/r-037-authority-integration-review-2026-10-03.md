# R-037 — Independent D-063 guard integration review

Date: 2026-10-03. **PASS for the approved guard integration scope.**
Reviewer: `reset_definition`; integration producer: `root`.
Open findings: **CRITICAL 0; HIGH 0; MEDIUM 0**.
Only this review artifact was written by the reviewer; no baseline edits.

## Reviewed input bindings

| Repository path | Raw SHA-256 |
|---|---|
| docs/phase-1-ui-reference-design/validation/validate-ui-reference-design.ps1 | D5F41A797B93431C6A98CA1B1A740EEB267CD1F5F398438EFE729D1709BCA16D |
| docs/phase-1-ui-reference-design/validation/validation-report.md | 013762DD3244A4BAE6E26160C1A300535D2E689E0A8C322E4A7323DDC5488963 |
| scripts/validation/ui_column_authority.py | D82070400B543208CBA607465606D1DC0930CF70F31ECE741E4960C8DAAC2988 |
| docs/phase-1-ui-reference-design/column-authority.json | E786B29985DDD0A553622AA1ADAF4029543D2F0ABB395A5AC7DAE64B3DD21554 |
| docs/phase-1-ui-reference-design/reviews/r-037-column-authority-actual-review-2026-10-03.json | B4EF38E65AD984D7D4B2C51F2D0193C1345796BC045515D0086B8A3DE10A9957 |

The registry/review hashes match the explicit Approved D-063 decision. The helper
is byte-identical to the independently reviewed verifier. Its successful actual
registry verification confirms pinned sources and live target cells still agree;
this integration does not alter or repin those cells/sources.

## Inspection and verification

The design validator invokes the reviewed read-only helper with exact D-063
binding. Native nonzero exit or invocation exception records a failed authority
assertion; it cannot become a declaration PASS. An independent in-memory probe
of the actual invocation block with native exit 19 produced
`FAIL_CLOSED=declared-column-authority`, without modifying source or approvals.
Standalone actual verification independently returned **1146 source-bound
declarations PASS**. An independent design run also reached the authority PASS.

Package JSON scope permits exactly the approved registry and review paths, not a
general JSON exemption. Both are required, along with helper/tests. The empty
unexpected-JSON diagnostic uses a pipeline safe under StrictMode. Removal of the
state-profile timing proxy does not remove branch vocabulary/reference checks,
batch-branch constraints, browser resolution or stream hard legality guards.
Classifier correlations remain diagnostic; exact reviewed authority now governs
the retained cells. The validator writes no approval or source evidence.

The independent first run identified stale freeze/report counts. Final inspected
reconciliation includes 20 required frozen files and package_json=2 in a dated
report append, preserving historical counts. The producer's final run confirms
both reconciled assertions PASS and **212 PASS / 1 FAIL**, only the cumulative
uncommitted write-scope guard. Production reports **172 PASS / 1 FAIL**, the same
known scope guard; `BATCH_EXIT_CERTIFIED` remains false. The nine focused helper
tests pass. These residual guard failures are disclosed, not waived or labelled
overall validator PASS. Commits/pushes remain deferred.

## Limits

This review verifies activation of the accepted helper and exact approval binding,
not a repeat of the independently completed actual-cell semantic review. Machine
source binding cannot certify implemented timing behavior or accessibility.
No full Phase 1 acceptance, B01/Figma authority, visual production, application
development, publication, external write, commit, push or deployment follows.
