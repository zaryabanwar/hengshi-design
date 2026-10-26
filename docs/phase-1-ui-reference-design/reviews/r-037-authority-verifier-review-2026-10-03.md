# R-037 authority verifier — independent implementation review

Date: 2026-10-03. **Final verdict: PASS for the D-062 helper implementation scope.**
Independent reviewer: `reset_definition`; helper producer: `root`.
Open findings in reviewed scope: **CRITICAL 0; HIGH 0; MEDIUM 0**.
Two scoped repair cycles completed. The reviewer made no implementation edits;
only this final review artifact was written.

## Scope and inspected inputs

Reviewed `scripts/validation/ui_column_authority.py` and
`scripts/validation/test_ui_column_authority.py` against the accepted
`docs/phase-1-ui-reference-design/COLUMN_AUTHORITY_PROPOSAL.md` model (D-062).
This is not the actual 1146-cell semantic authority review, registry approval,
validator integration approval, R-037 closure or public/application acceptance.

Reviewed helper SHA-256:
`D82070400B543208CBA607465606D1DC0930CF70F31ECE741E4960C8DAAC2988`.
Reviewed test SHA-256:
`F4659DDFB004BAA1FD6E6A4613A28DE21DFCC4699DEE3BA0CAD51177D4E96DBE`.

Verified exact 22-column authority set and live target-cell key enumeration;
closed record/source/review schemas; duplicate JSON/CSV/key rejection; declared
cell equality; pinned source locators and quoted selected facts; independent
source-witness requirement; branch/applicability/protection constraints without
runtime claims; exact founder decision/registry/review binding; nonauthor review
identity, zero finding counts, matching source snapshots and exact examined keys.
Source parsing caches are verification-local; source pins are checked again at
the end of registry verification. The helper creates no approval artifacts.

## Findings and repairs

- Cycle 1 HIGH: selecting the same target cell through a different unique CSV
  lookup field bypassed self-authority detection. The corrected check uses the
  resolved row's actual primary identity and selected field, not lookup spelling.
- Cycle 1 HIGH: decision lookup accepted prefix collisions such as requested
  D-999 resolving D-9999. The corrected regex requires an exact token delimiter.
- Cycle 2 HIGH: Windows path-case aliases bypassed the remaining textual file
  comparison. The corrected check uses physical file identity (`samefile`);
  duplicate physical source snapshots and registry-file aliases are rejected.

All three findings are closed in the inspected implementation. Focused
regressions cover alternate CSV lookup, decision-prefix collision and physical
path aliases (Windows case alias, or a hardlink on case-sensitive hosts).

## Verification and limits

Independent command: `python -B scripts/validation/test_ui_column_authority.py`.
**Nine tests PASS**, including positive complete binding and negative schema,
source, stale-pin, selector, timing/runtime, review and approval seams. Initial
in-memory probes reproduced the findings before their repairs; final inspection
and regression execution verify the repaired comparisons.

Machine checks resolve structural source/approval bindings; they cannot establish
that a quoted fact semantically justifies the cell or that a nonauthor actually
performed the claimed review. Actual source/criterion conclusions remain the
separately commissioned independent registry review and founder acceptance.
No final registry decision exists by virtue of this report, and the helper must
not replace baseline authority guards before that separately pinned approval.
This report grants no B01/Figma/application permission, time-limit change,
implementation conformance, publication, commit, push or deployment.
