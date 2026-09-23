# Producer Inspection — UI Reference-Design Contract

**Inspection date:** 2026-09-03  
**Producer iteration:** 3 of 3; final allowed producer revision  
**Role:** UI contract producer; not an approver  
**Inspection status:** Revision complete; deterministic validation PASS; fresh independent reviews pending  
**Revision:** D-045 delivery-stream evidence model, 2026-09-06

## Scope inspected

This inspection covers the final producer-owned documentation package under
`docs/phase-1-ui-reference-design/` after the iteration-1 accessibility audit.
It checks that D-025, D-026, D-035, and D-036 remain intact and that future visual
production receives explicit accessibility, browser, time-limit, ownership, and
evidence contracts.

Frozen accepted inputs, root durable records, protected prototype/GLB files,
application source, dependencies, external design tools, reviewer/audit files,
`DESIGN_SYSTEM_IMPLICATIONS.md`, and `component-primitives.csv` were not modified.
The two design-system files were integrated read-only at SHA-256
`DCF2F63D11BB45CB71568B18A0E16C95BD94F1991CBE23B5B677D832F1310AD2`
and `2D01496DCC7D9C062AD77E52CC9F0F110D3F7B4CE899D95A52A8B6F7311E6F4A`.

**Amendment 2026-09-06 — CR-002 revision window, decision D-039.** The statement
above records the position at the 2026-09-03 producer freeze and is retained
unedited as provenance. It is **no longer current**. Under the founder-approved
CR-002 revision window, both design-system files were modified to remove the
"optional"/fallback framing for the semantic stream, and the route-coverage and
UX-parity column `optional_immersive_representation` was renamed
`immersive_stream_representation`. The amended read-only integration values are:

| Artifact | **Current — D-045, 2026-09-06** | Superseded provenance values |
|---|---|---|
| `DESIGN_SYSTEM_IMPLICATIONS.md` | `0E9FC68C98AC25C4F7DFBC62B10DBA1FCB197F5C82AD2FF39DCD0C16D9CFB763` — **unchanged under D-045 by founder gate G-6** | D-037 2026-09-03 `DCF2F63D11BB45CB71568B18A0E16C95BD94F1991CBE23B5B677D832F1310AD2`; D-039 `B4F0F9E34908B691C73CADCE33784E7D2709BFDB89F84F3B24188CF3198626BB`; D-042 `F0906F44488094F75F366EAD57F10BF00301AA003E12B8C79C68BD4778CBD8C9` |
| `component-primitives.csv` | `E6B39B5B9B5B917EAB8306E653E38E9F06934788AACB7CFF05226D21005929CB` | D-037 2026-09-03 `2D01496DCC7D9C062AD77E52CC9F0F110D3F7B4CE899D95A52A8B6F7311E6F4A`; D-039 `0EC5B81452EAF79076CF06A5F57C7982D8F581D6105466D5352796C542DF007C`; D-042 `28AAEA9CEF0F3BB6B131F541A86B6CD28B1A6DB9AB54BF72AB7EE744F4167727`; D-043 `E06D11057AF1E903E37FC0F289E994B196FD337B4E8A22AB37BB686562BB9470` |

*Table restructured 2026-09-06 under D-043.* It previously presented the D-039
values in a column headed "CR-002 amendment 2026-09-06" while the validator pinned
different constants, so the record read as current and was not. The current value
now leads and every superseded value is kept beside it, dated. These two are the
values the validator asserts; if they disagree with it, the validator is right and
this table is the defect.

Dated review artifacts under `reviews/` and `accessibility/` cite the superseded
values and are **deliberately not rewritten**; they are historical evidence of
what was inspected, not statements about the current package. **MA-028 was accepted by the
founder on 2026-09-06 (D-041)**, so the amended package now carries the authority
the D-037-accepted package did. Independent design and accessibility reviews ran
on 2026-09-06 **after** that acceptance and both returned **FAIL**; every blocking
finding was remediated under **D-042** on the same date, and the freeze values were
recomputed accordingly.

Two independent re-reviews of the D-042 remediation ran on 2026-09-06 and both
returned **FAIL**, converging on the same five defects: the stream axis was inert
(a column asserted by row count, never resolved), `COV-ACT-08`/`COV-ACT-09` still
carried demotion vocabulary, the frozen validation report described a different
package than the validator asserted, the style guide claimed WCAG 2.2 **3.2.2**
was "satisfied by construction", and the SRS held no accessibility requirement at
all. All five are remediated under **D-043**, together with the `S-SEMANTIC`
boundary-crossing specification that neither reviewer had a home for.

That is three FAIL rounds against passing validator runs of 183, 184, and 185
assertions. The lesson is recorded rather than smoothed over: **a passing
validator is a determinism check, not a review**, and an assertion that counts
rows on a new axis is a placeholder, not coverage.

**D-045, 2026-09-06.** The D-043 remediation was never re-reviewed either, and the
producer's own inspection of it found the defect repeated a second time: `A-01`'s
replacement assertion derived `stream_profile` from `state_profile`, and the guard
asserted `Count -eq 44`. The founder's response was decision **D-045** — *"the
producer now implements, and only implements"* — with two `[PROPOSED]`
specifications as the sole authority. Under D-045 the axis was rebuilt so that stream
obligations are **declared** at the primitive, **computed** at the template by a union
fold, and **inherited unstored** at route and flow. No route, flow, or template row
carries a stream column, and `A-01` now fails if one returns.

**Three producer remediations — D-042, D-043, D-045 — have now landed with no
independent review between them, and each passed every assertion in force at the
time.** **MA-029 is `awaiting_human`. R-035 remains open and cannot be closed by the
producer.**

## Accessibility finding dispositions

| Finding | Producer disposition | Deterministic evidence |
|---|---|---|
| A11Y-UIR-I1-001 — incomplete conformance target | **Addressed for fresh review.** README, contract, UX-001 trace, design-system dependency, and every B01-B09 review gate now require WCAG 2.2 Level AA for every applicable full page and complete process, including represented third-party steps. They explicitly reject a current visual/implemented conformance claim. | `wcag22aa-normative-target`; `wcag-no-current-conformance-disclaimer`; `ux001-wcag-trace-contract`; `design-batch-wcag-target-review`; `unsupported-conformance-claim-absence` |
| A11Y-UIR-I1-002 — browser/platform baseline | **Addressed for fresh review.** `BP-NFR-006` maps every route, flow, template, profile, and production batch to the latest two stable Chrome/Edge/Firefox/Safari release families selected by later dated QA, Safari/iOS 16.4 minimum floor, mobile input/layout/virtual-keyboard/safe-area proof, and unsupported-client semantic Quick Access. Exact current versions are not invented. | `nfr006-browser-profile-definition`; `nfr006-browser-profile-mapping`; `nfr006-browser-profile-content`; `design-batch-browser-evidence`; `nfr006-negative-fixture` |
| A11Y-UIR-I1-003 — time-limit specificity | **Addressed for fresh review.** Every applicable record selects removal/adjustment before start, warning at least 20 seconds plus simple extension at least 10 times, a criterion-supported documented exception, or explicit not-applicable. Preservation, accessible reauthentication, exact-duration gates, and provider/system-timeout separation are explicit; no current record selects an exception. | `wcag221-time-limit-profile-set`; `wcag221-time-limit-record-mapping`; `wcag221-time-limit-definition-content`; `design-batch-time-limit-evidence`; `wcag221-no-undocumented-exception-selection`; `wcag221-negative-fixture` |

## Prior design-review regression inspection

UIR-DR1-001 through UIR-DR1-006 remain closed in producer evidence: B06 still
hard-depends only on B01 and owns ACT-20 through ACT-31; all 155 source IDs and 40
templates retain unique exact primary owners; unknown/opaque IDs remain rejected;
all 74 baseline frame names align with their primary batch; proposed gate sources
remain package-only; and every B01-B09 row requires independent design and
accessibility review.

## Producer checklist

| Area | Producer finding |
|---|---|
| Authority | D-025 retains `/industries`; D-026, D-035, and D-036 remain accepted definition authority. Frozen source bytes were not edited. |
| Exact coverage | 34 routes (33 accepted at D-025 plus `/credits` reconciled 2026-09-06 under R-032), 12 package flow families, 32 accepted journey/flow/subflow IDs, 53 actions, nine exclusions, 15 wayfinding records, and 46 UX tests remain exact. `UXTEST-046` was added under D-045 for the stream control, the boundary crossing, and process-state survival. |
| Templates and ownership | Forty templates and 155 exact primary source IDs each have one production owner; supporting/final evidence cannot satisfy ownership. |
| Accessibility target | WCAG 2.2 Level AA governs all applicable full pages and complete processes including represented third-party steps; no current conformance is claimed. |
| Browser profile | All route/flow/template/profile/batch records resolve to `BP-NFR-006`; dated current-version selection, Safari/iOS 16.4 evidence, and unsupported Quick Access are mandatory. |
| Time limits | All covered records select an allowed `TL-*` branch. No undocumented exception or exact duration is introduced. |
| Direct booking | B06 remains independently producible after B01 with no prior AI, handoff, media, World, account, audio, upload, or B05 dependency. |
| Component consistency | All 62 primitives remain unique, resolved, referenced, and hash-verified against the stable specialist artifact. Each now declares an ordinal-sorted `stream_presence`, which is the single place where the delivery-stream axis is authored. |
| Delivery streams | Four peer streams. No stream column exists on any route, flow, or template row; template presence is a computed union fold over `primitive_dependencies`, and route and flow presence is inherited and never stored. `A-01`-`A-11` resolve the axis rather than counting it. |
| Gate truthfulness | At the 2026-09-03 producer freeze, MA-024 and the separate external-write gate are package-only proposals. Root integration may occur only after clean independent reviews; external write remains false. |
| Boundary | No screen, asset, UI/3D/application code, external write, dependency, public copy, root record, Git history, publication, or deployment was changed. |

## Changed-file scope

**Iteration 3 (2026-09-03).** Only the 11 producer-owned files were revised:

1. `README.md`
2. `UI_REFERENCE_DESIGN_CONTRACT.md`
3. `design-batch-plan.csv`
4. `foundation-flow-coverage.csv`
5. `foundation-route-coverage.csv`
6. `producer-inspection.md`
7. `reference-template-inventory.csv`
8. `responsive-state-mode-matrix.csv`
9. `traceability.csv`
10. `validation/validate-ui-reference-design.ps1`
11. `validation/validation-report.md`

**D-045 (2026-09-06).** This slice is wider than iteration 3, because the decision
covers two packages and the abolished vocabulary had spread beyond both. Inside this
package: `README.md`, `traceability.csv`, `design-batch-plan.csv`,
`foundation-flow-coverage.csv`, `producer-inspection.md`,
`validation/validate-ui-reference-design.ps1`, `validation/validation-report.md`, and
`component-primitives.csv` (the `stream_presence` column only, per §5.1 of the
accepted specification). Outside it: the production package, the UX-architecture
package, `docs/active/Hengshi_Design_SRS_v3.md`, and
`docs/active/3D_Mega_Menu_Style_Guide_v2.md`.

`DESIGN_SYSTEM_IMPLICATIONS.md` was edited during this slice and the edit was
**reverted**. Founder gate **G-6** holds that the design system's missing stream axis
is recorded now and amended later under its own bounded specialist contract, so the
file is untouched and `design-system-freeze-hash` passes against the D-043 value.

All reviewer and audit files under `reviews/` and `accessibility/` remain unchanged.
They are structurally exempt from the `A-16` vocabulary sweep as dated historical
evidence of what was inspected, and the exemption is a closed directory rule with a
strict-subset assertion rather than a list a producer can extend.

## Open gates

- Fresh independent design and accessibility reviews must pass. The producer
  cannot approve this package or close its own findings.
- **MA-024 — Phase 1 UI reference-design contract and foundation-surface
  coverage acceptance** is definition-only. At this freeze it is package-only;
  root durable integration may follow clean independent reviews.
- MA-024 does not authorize Figma or Stitch work. A separate explicit future
  external Figma/Stitch production/write gate remains required and false.
- Standards exceptions/target changes, final visual direction, exact public/legal
  copy, licensed assets, provider/owner facts, implementation, publication,
  complete Phase 1 acceptance, and deployment remain human gates.

## Inspection outcome

Producer iteration 3 addresses all three accessibility findings without changing
product or brand direction, and all prior design-review invariants remain passing.
The validator returned `RESULT=PASS PASS_COUNT=183 FAIL_COUNT=0` at that freeze.

**Amended under D-045, 2026-09-06.** The validator now returns
`RESULT=PASS PASS_COUNT=201 FAIL_COUNT=0`, and the sentence above — "there is no
unresolved producer finding" — is **withdrawn**. It was true only in the sense that
the producer had stopped looking. There are now five unresolved producer findings,
each recorded in `validation/validation-report.md` rather than repaired, because
repairing them would be the producer authoring the model D-045 barred it from
authoring:

1. Twenty-two judgement columns are inert and unadjudicated, including
   `time_limit_branch`, which founder gate G-5 recorded as **not exempt**.
2. `A-11`'s determiner set is a producer reading of an underspecified instruction.
3. `A-08` implicates eleven state profiles the specification's migration table did not
   enumerate.
4. The staff, publication, and audit templates fold to all four streams even though
   they serve excluded surfaces; §4.2's fold has no exclusion for them.
5. The design system carries no stream axis at all (gate G-6).

A sixth finding was a defect in the producer's own work rather than in the
specification, and is recorded in full in the validation report instead of being
quietly fixed: a PowerShell operator-precedence collapse left the peer-framing guard
**silently inert**, reporting zero hits across 56 files while six live UX-package
files still carried the abolished vocabulary. That is the D-045 defect shape — an
assertion that cannot fail — reintroduced while implementing the remedy for it.

The package remains ready for fresh independent design and accessibility review, and
for nothing else. Not MA-024 approval, not MA-025 execution, and not external visual
production.
