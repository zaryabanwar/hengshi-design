# Accessibility Audit — CR-002 Amended Package (iteration 3)

**Review date:** 2026-09-06
**Package under review:** CR-002 amended package, design aggregate
`F16093D07D1E2634DB440ED35E4D4648ABF4F6D85C2BCD4E8F9CE5092F9C4AD6`
(the value accepted at MA-028 / D-041)
**Reviewer:** independent review agent, not the producer
**Verdict at review:** **FAIL**
**Disposition:** blocking findings remediated under **D-042** on 2026-09-06; the
remediated package has **not** been re-reviewed. **R-035 remains open.**

**Conformance target reviewed against:** WCAG 2.2 Level AA for every applicable
full page and complete process, including represented third-party steps. No
current conformance is claimed by the package and none is claimed here.

> This audit ran **after** founder acceptance of MA-028, not before it. The
> acceptance rested on the producer record and four passing deterministic
> validators. None of the findings below were detectable by those validators.

## Blocking findings and disposition

| ID | Finding | SC at stake | Disposition under D-042 |
|---|---|---|---|
| F-01 | The one-shot mid-session promotion was governed by the single word "visible". A promotion re-renders the scene, rebuilds the DOM overlay carrying every accessible name, and — given `S-LOW`'s "fewer hotspots" — **adds interactive targets to the accessibility tree mid-session**. No status message, no focus-preservation clause, no way to decline. `SP-WORLD` had a demotion state and no promotion state. | 4.1.3, 3.2.2, 2.4.3 | **Resolved by removing the construct (founder decision).** Measurement is stored and applied from the next visit; the stream never changes mid-session except by the visitor's own act. §8.2.4 governs that one case: polite status message, focus not moved, scroll / open panel / route preserved, current stream in the control's accessible name. 3.2.2 is now satisfied by construction. `STATE-QUALITY-DOWNGRADED` → `STATE-STREAM-CHANGED`. |
| F-02 | Conformance must hold independently in each stream, but the evidence ledger had no stream axis. `MODE-NON-WEBGL-QUICK-ACCESS` is not `S-SEMANTIC`; `MODE-LOW-POWER` is not `S-LOW`; **`S-MEDIUM` had no representation anywhere**. A producer could satisfy every ledger cell, pass 183/183, and produce no `S-MEDIUM` evidence at all. | §2.3 target | **Fixed.** Four `stream` profiles added, each with its own minimum evidence and critical distinct frames. Contrast, focus order, and target size are now required **per stream, against that stream's own rendering**. B07 states that aggregate evidence does not satisfy the per-stream requirement. |
| F-03 | The override control had no home in the semantic shell and no accessibility specification. The nearest existing thing was ACT-09 "Toggle quality", living in `TPL-WORLD-HUD` — absent from `S-SEMANTIC`. It was not specified as keyboard-operable, discoverable, persistent, or announced. | 2.1.1, 2.4.7, 4.1.2, 1.3.1 | **Fixed.** Control added to `PRIM-001` and `PRIM-044`; §8.2.2 step 5 specifies reversibility, cross-session persistence, and an ACT-11-style persistence-failure branch; §8.2.4 specifies the announcement and the accessible name. New `FR-3D-014`. |
| F-04 | Governance deadlock: production contract §0.1 forbade any batch relying on amendment-introduced changes, while B07 — the only artifact carrying every stream obligation — was "not authorizable" and refused by `SC-10`. The P0 elevation of `S-SEMANTIC` therefore bought a disabled user nothing on the authorized path. | contract clause | **Half fixed by founder decision.** §0.1 corrected: authorized batches may now rely on the amendment, which unblocks `/credits` in B02. **B07 remains deferred to MA-026 by explicit founder choice.** The consequence is recorded, not hidden: no four-stream reference evidence is produced under MA-025, so `S-SEMANTIC`'s P0 status is a written commitment the current production path does not discharge. Tracked as **R-036**. |

## Significant findings

| ID | Finding | Disposition |
|---|---|---|
| F-05 | "Motion suppressed" covered three things and was silent on hotspot hover/click animation, ambient/particle/lighting motion, and loading fades. Worse, §4.1's hotspot states were **scale + colour + emission with no keyboard-focus row and no static cue** — so a reduced-motion user in `S-HIGH` could receive state information only through motion, and a keyboard user might get no focus indicator at all. | **Fixed.** §7.3 now enumerates suppression exhaustively and normatively ("anything not listed continues to run"). §4.1 gains a normative **Keyboard focus** row (persistent 3 px ring at ≥3:1 against every adjacent scene colour) and a required non-colour, non-motion cue on every state. §7.2 retitled from "(Planned)" to "required; not yet implemented". |
| F-06 | Ladder vocabulary survived intact (`PRIM-044` "fallback", `FLOW-WORLD-HUD-FALLBACK`, `WORLD_HUD_FALLBACK`, `MODE-NON-WEBGL-QUICK-ACCESS`); the validator's four-alternative regex missed all of it; **R-034 had been closed prematurely.** A no-WebGL user would be built from a primitive whose states are `unsupported; loader_timeout; asset_error; …` behind a "plain failure heading" — an error surface presented as a first-class one. | **Partly fixed; R-034 reopened.** `PRIM-044` renamed and its downgrade element replaced. The three accepted upstream identifiers are not renamed here because the cascade reaches the foundation and UX packages; they stay on R-034. |
| F-07 | Route-count contradiction (normative prose 33 vs data 34) combined with §0.1's "the D-037 package governs" would make a careful producer drop `/credits` as an orphan — leaving a dangling footer link and an unmet CC BY 4.0 obligation. | **Fixed** in all six locations; §0.1 corrected. |
| F-08 | `/credits`: "Return to prior route" and "open source asset licence" were both dropped between the parity file and the coverage row; 3.1.2 Language of Parts was unaddressed on the one route where foreign-language author names are near-certain; list semantics were never required against a prose template. | **Fixed.** Both actions restored; B02 evidence and the template now require marked-up list semantics, per-entry `lang`, and in-context link purpose. |
| F-09 | §8.2 asserted equivalence in the present indicative inside a document headed `Status: Active`. | **Fixed** — §8.2.2 carries a dated decision header and §8.2.3 keeps `[MUST VERIFY AT SPECIFICATION]`; the SRS rows remain "❌ Not implemented". |

## Minor

F-10 (the `attribution` family missing from `PRIM-001`'s applicable list, and
`TPL-PUBLIC-ABOUT`'s reuse scope) — **fixed**.

## Regression check on A11Y-UIR-I1-001/002/003

- **001 conformance target — not weakened.** The full wording and the
  no-current-conformance disclaimer survive in §2.3, §14, `PRIM-001`, `PRIM-058`,
  and all nine batch rows. The reviewer noted it was previously *unenforceable per
  stream*; F-02's fix closes that.
- **002 `BP-NFR-006` — not weakened; correctly closed.** `ROUTE-CREDITS` carries
  the profile, and the renamed `immersive_stream_representation` column is
  populated. Residual: the profile is silent on which stream a below-floor
  Safari/iOS 16.4 client receives — carried on R-034.
- **003 `TL-*` — not weakened; correctly closed.** `ROUTE-CREDITS` selects
  `TL-NOT-APPLICABLE`, correct for static attribution text. The step-6 promotion
  gap that had no `TL-*` determination no longer exists.

**Disposition invalidated by the amendment:**
`accessibility-audit-iteration-2.md` records zero browser-profile gaps across
**33 routes** against freeze `97E7…`. Its PASS does not extend to `ROUTE-CREDITS`.
It is retained unedited as history.

## Standing requirement

The remediated package has had **no** independent accessibility review.
**R-035 remains open** and its exit evidence is unchanged.

---

## Correction appended 2026-09-06 under D-043

*The findings and dispositions above are the dated record of what this reviewer
found and what the producer claimed at the time. They are **not** rewritten. This
block records where the dispositions above were wrong, established by an
independent accessibility re-review of the D-042 remediation that returned
**FAIL**.*

| Row | Disposition claimed above | What was actually true |
|---|---|---|
| F-01 | "§8.2.4 governs that one case … **3.2.2 is now satisfied by construction.**" | **Withdrawn.** WCAG 2.2 **3.2.2 On Input** governs changing the setting of a user interface component. The delivery stream control *is* such a component, so removing automatic mid-session promotion does not satisfy 3.2.2 — it only removes one way of violating it. A polite status message *after* the change is **4.1.3** treatment, not 3.2.2 treatment. 3.2.2 is satisfied by **advance advisement**, which the style guide did not require. It now does, and it claims no conformance at all: both SCs are evaluated against the implementation. |
| F-02 | "**Fixed.** Four `stream` profiles added, each with its own minimum evidence and critical distinct frames." | **Overstated, and it re-created the exact defect F-02 named.** The profiles existed but nothing selected them, so "a producer could satisfy every ledger cell, pass 183/183, and produce no `S-MEDIUM` evidence at all" remained true after the fix. `stream_profile` is now required and non-empty on every route, flow, and template row; `DS-STREAM-INVARIANT` lets a record claim stream-identical rendering positively without ever marking `S-SEMANTIC` not applicable. |
| F-03 | "**Fixed.** Control added to `PRIM-001` … §8.2.4 specifies the announcement and the accessible name." | Incomplete on the case that matters most for this control. `S-SEMANTIC` and the 3D shells are **different subtrees**, so the control the visitor operates does not survive the change — yet focus behaviour, location mapping, and accessibility-tree ordering across that boundary were unspecified. §8.2.4 now names the destination (the stream control in the incoming shell), specifies bidirectional location↔canonical-route mapping with a nearest-ancestor rule, and requires the outgoing shell to leave the accessibility tree before the incoming one enters. |
| F-04 | "**Half fixed by founder decision.** … B07 remains deferred … no four-stream reference evidence is produced under MA-025." | Still half fixed, and the half that was missing is now partly bought back: `ACT-09` moved from `B07` into authorized `B01`, so the delivery stream control **is** evidenced under MA-025 even though full four-stream reference evidence still waits on MA-026. **R-036 stays open.** |

**Also found by the re-review:** the SRS carried **zero** accessibility
requirements, so the WCAG 2.2 Level AA target had no requirement-level home and
nothing to trace to. SRS **§5.6 `NFR-A11Y-001`…`007`** added under D-043, every
row unimplemented and no conformance claimed.

The standing requirement above is unchanged and still unmet: **the D-043
remediation has had no independent accessibility review. R-035 remains open.**
