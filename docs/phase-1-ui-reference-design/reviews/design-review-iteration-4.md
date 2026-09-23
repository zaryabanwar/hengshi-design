# Design Review — CR-002 Amended Package (iteration 4)

**Review date:** 2026-09-06
**Package under review:** CR-002 amended package, design aggregate
`F16093D07D1E2634DB440ED35E4D4648ABF4F6D85C2BCD4E8F9CE5092F9C4AD6`
(the value accepted at MA-028 / D-041)
**Reviewer:** independent review agent, not the producer
**Verdict at review:** **FAIL**
**Disposition:** blocking findings remediated under **D-042** on 2026-09-06; the
remediated package has **not** been re-reviewed. **R-035 remains open.**

> This review ran **after** founder acceptance of MA-028, not before it. That
> ordering is recorded here rather than tidied away: the acceptance rested on the
> producer record and four passing deterministic validators, and a passing
> validator is a determinism check, not a review. None of the findings below were
> detectable by the validators that passed 184/184 at the time.

## Blocking findings and disposition

| # | Finding | Disposition under D-042 |
|---|---|---|
| 1 | The step-3 stream control was required "in every stream, including `S-SEMANTIC`" but existed only in `PRIM-042`/`PRIM-043`, both `overlay_immersive` — inside a World canvas that `S-SEMANTIC` does not have. `PRIM-001` had no such control. | **Fixed.** `delivery stream control` added to `PRIM-001` anatomy and to its mode obligations ("present and keyboard operable in every stream including S-SEMANTIC"). Style guide §8.2.2 now states the control lives in the semantic shell primitive, not only the HUD. New `FR-3D-014`. |
| 2 | `S-LOW` was defined as "fewer hotspots" while claiming an equivalent core journey — unfalsifiable, and no rule said which hotspots to drop. | **Fixed by founder decision.** `S-LOW` now reduces fidelity only: "every hotspot and every destination retained". `DS-S-LOW` requires explicit proof that every destination present in `S-HIGH` is present. §8.1 additionally states viewport never removes a destination. |
| 3 | "Equivalent core journey" asserted four times, defined zero times. The stream IDs appeared exactly once in the whole design package. CR-002 §4 promised a stream axis in `responsive-state-mode-matrix.csv`; it was never added. | **Fixed.** Four `stream`-dimension profiles `DS-S-HIGH`/`DS-S-MEDIUM`/`DS-S-LOW`/`DS-S-SEMANTIC` added, each with its own `minimum_evidence` and `critical_distinct_frame_values`. B07 now states per-stream evidence is mandatory and that aggregate evidence does not satisfy it. New validator assertion `delivery-stream-profile-set`; `profile-count` 32 → 36. |
| 4 | Step 3 (override) was evaluated before the stream it modified existed — circular. Reversibility, interaction with the step-6 promotion, and cross-session persistence were undetermined or contradictory. | **Fixed by founder decision.** §8.2.2 reordered: ceiling → device tier → default → stored measurement → override → reduced motion. The override is reversible under the ceiling, persists across sessions, and outranks stored measurement. |

## Significant findings

| # | Finding | Disposition |
|---|---|---|
| 5 | The peer rename was largely lexical: `PRIM-044` still named "World escape and fallback" with "quality downgrade if valid"; `STATE-QUALITY-DOWNGRADED` present with no promotion state; the semantic stream still modelled as `MODE-NON-WEBGL-QUICK-ACCESS`; flow family still `FLOW-WORLD-HUD-FALLBACK`; `route-room-parity.csv` still said "optional World". | **Partly fixed.** `PRIM-044` renamed "World escape and recovery"; "quality downgrade if valid" → "delivery stream control"; `STATE-QUALITY-DOWNGRADED` → `STATE-STREAM-CHANGED`; "optional World" removed from the UX parity file. **Not fixed:** `FLOW-WORLD-HUD-FALLBACK`, the `WORLD_HUD_FALLBACK` journey key, and `MODE-NON-WEBGL-QUICK-ACCESS` are accepted upstream identifiers whose rename cascades into the foundation and UX packages. **R-034 is reopened** to carry them. |
| 6 | `ROUTE-CREDITS` was assigned `TPL-PUBLIC-ABOUT`, whose `reuse_scope` excluded it and whose anatomy had no attribution list. | **Fixed.** Template scope is now `ROUTE-ABOUT;ROUTE-CREDITS`, with attribution-list anatomy, per-entry language marking, in-context link purpose, return-to-invoker, and a long-dense-list content stress case. |
| 7 | B02 owned `ROUTE-CREDITS` with no credits evidence obligation. | **Fixed.** B02 objective and `required_visual_evidence` now name the attribution frame explicitly. |
| 8 | `/credits` next-actions contradicted between the parity file and the coverage row. | **Fixed.** The coverage row now carries "Return to the invoking route; open the source asset licence" ahead of About/Trust/Contact. |
| 9 | Contract and README still said 33 routes while the CSV had 34; producer inspection said 154 source IDs where the count was 155. | **Fixed** in all six locations plus the two counts. |
| 10 | Production contract and producer inspection still asserted the amended package was unaccepted, after D-041 accepted it. | **Fixed.** Both updated. §0.1 now states the authorized batches may rely on the amendment, and names the two limits that still apply. |
| 11 | Step 6 was unspecifiable: "early in the session" undefined, measured quantity undefined, threshold neither specified nor formally deferred. | **Resolved by removing the construct.** Mid-session promotion is gone; measurement is stored and applied from the next visit. There is no promotion window left to specify. |

## Minor findings

12–14 (residual "graceful degradation" wording in §2.1/§2.2/§10; §8.1 conflating
viewport with stream; reduced motion undefined inside `S-SEMANTIC`) — **all fixed**.

## What the reviewer found sound

- `CR-002-signal-portability-verification.md` — quotes Baseline banners verbatim,
  states its own scope limit up front, and §7 records the evidence it did **not**
  obtain. It does not overclaim.
- The substance of the founder's precedence decisions: WebGL as a hard ceiling,
  motion decoupled from content, no measurement-driven demotion, `S-LOW` designed
  first. The defects were in ordering and specification, not intent.
- Provenance discipline: superseded hashes retained, dated reviews not rewritten,
  D-041 stating plainly that the required reviews had not run.
- The `/credits`-in-all-four-streams reasoning (CC BY 4.0 does not vary by tier).

## Standing requirement

The producer does not approve its own output. This package requires an
**independent re-review** of the D-042 remediation before these findings can be
treated as closed.

---

## Correction appended 2026-09-06 under D-043

*The findings and dispositions above are the dated record of what this reviewer
found and what the producer claimed at the time. They are **not** rewritten. This
block records where the dispositions above were wrong, established by an
independent re-review of the D-042 remediation that returned **FAIL**.*

| Row | Disposition claimed above | What was actually true |
|---|---|---|
| 3 | "**Fixed.** Four `stream`-dimension profiles added … New validator assertion `delivery-stream-profile-set`; `profile-count` 32 → 36." | **Overstated.** The four profiles were added to `responsive-state-mode-matrix.csv` and the validator asserted their existence — by counting rows. **No route, flow, or template record selected one.** A producer could satisfy every ledger cell and produce no per-stream evidence, which is the defect finding 3 was raised against. Genuinely fixed under D-043: `stream_profile` is now a required non-empty column on all three record files, 36 flows and 8 templates select all four `DS-S-*`, and `ACT-09` moved from deferred `B07` into authorized `B01` so the axis is evidenced on a batch that will run. `profile-count` 36 → 37 (`DS-STREAM-INVARIANT`). |
| 2 | "**Fixed by founder decision.** `S-LOW` now reduces fidelity only." | Correct, but incomplete: §2.1 "Performance First: visual richness must never compromise performance" was left standing as the one clause readable as licence to drop a hotspot in `S-LOW`. Scoped to fidelity under D-043. |
| 5 | "**Not fixed:** … accepted upstream identifiers whose rename cascades into the foundation and UX packages. **R-034 is reopened**." | The **cascade claim was false**, and it was the producer's, not the reviewer's. All 47 occurrences were in the design package and in history documents. The rename is complete under D-043. |

**Also found by the re-review and not visible above:** the `validation-report.md`
inside the D-042 freeze described a 33-route, 32-profile package while the
validator in the same freeze asserted 34 and 36. A new assertion
`validation-report-counts-agreement` now forbids that drift.

**Named pattern, carried forward:** *assertions that pass by counting rows rather
than resolving references.* A row-count assertion on a new axis is a placeholder,
not coverage. This is the third time a package passing every assertion has failed
independent review.

The standing requirement in §"Standing requirement" above is unchanged and still
unmet: **the D-043 remediation was written by the producer and has not been
independently re-reviewed. R-035 remains open.**
