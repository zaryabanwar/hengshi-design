# Phase 1 UI Reference-Design Contract — Independent Design Review, Iteration 1

**Review date:** 2026-09-03  
**Reviewer:** independent design/UX reviewer; not the producer of the reviewed package  
**Producer iteration:** 1 of the maximum 3 UI revisions  
**Decision boundary:** documentation-contract review only; this report does not grant MA-024, approve a visual direction, or authorize Figma/Stitch production, application implementation, publication, deployment, assets, or public/legal copy  
**Verdict:** **REVISE**

## 1. Scope and independence

I reviewed the frozen producer package under `docs/phase-1-ui-reference-design/**`, excluding `reviews/**`. I did not create or edit any producer artifact. Repository inspection was read-only except for this review report.

The review used the authority order in `AGENTS.md` and `.specify/memory/constitution.md`, then the current root project records, software-definition package, accepted Phase 1 foundation, D-026 Evidence in Motion strategy, D-035 Signal Ledger + Framework Relay identity, and D-036 UX architecture. Stale status text inside frozen predecessor packages was treated as subordinate to D-035 and D-036.

No Figma/Stitch file, rendered reference screen, prototype, video, image set, or 3D scene exists in this documentation-only slice. Accordingly, this pass assesses whether the contract is complete and safe enough to govern later visual production; it does not assess an actual visual result.

## 2. Freeze proof

The producer scope contains these 13 files:

1. `README.md`
2. `UI_REFERENCE_DESIGN_CONTRACT.md`
3. `DESIGN_SYSTEM_IMPLICATIONS.md`
4. `foundation-route-coverage.csv`
5. `foundation-flow-coverage.csv`
6. `reference-template-inventory.csv`
7. `responsive-state-mode-matrix.csv`
8. `component-primitives.csv`
9. `design-batch-plan.csv`
10. `traceability.csv`
11. `producer-inspection.md`
12. `validation/validate-ui-reference-design.ps1`
13. `validation/validation-report.md`

I independently recomputed the aggregate SHA-256 from uppercase per-file hashes followed by two spaces and workspace-relative forward-slash paths, sorted by full path, LF-joined without a terminal newline.

- Expected: `D967C30FD56DF799294D8B84E35E78ABE7DEA73ED5104EC629EB4C5E1A7332B0`
- Actual: `D967C30FD56DF799294D8B84E35E78ABE7DEA73ED5104EC629EB4C5E1A7332B0`
- File count: `13`
- Freeze result: **MATCH**

This report is outside the frozen producer scope and does not change that result.

## 3. Method and review criteria

The review included:

- full reading of the governing/root records and all 13 producer files;
- CSV parsing with `Import-Csv`, source-route JSON parsing, uniqueness/set comparisons, and independent record sampling rather than reliance on stated totals;
- comparison of every route ID/path, all exclusion IDs, all wayfinding IDs, ACT-01 through ACT-53, UXTEST-001 through UXTEST-045, and the required non-route flow families;
- inspection of template versus route-instance identities, profile references, baseline evidence names, batch prerequisites, and every free-text/semicolon-delimited batch reference;
- comparison of booking, AI/handoff, World, contact, staff, publication, recovery, and accessibility obligations to accepted D-025/D-026/D-035/D-036 authority;
- review of content, asset, claims, evidence, provider, privacy, and human-approval gates; and
- scan for external URLs, secret-like assignments, binary/design assets, and current-operation claims.

The acceptance criteria were completeness, internal coherence, source traceability, feasible production sequencing, brand/UX alignment, visible accessibility obligations, exact gate separation, and enough named future evidence for a later producer to work without inventing product behavior.

## 4. Reproduced validation and positive evidence

Command rerun:

```powershell
pwsh -NoProfile -File docs/phase-1-ui-reference-design/validation/validate-ui-reference-design.ps1
```

Result: `RESULT=PASS PASS_COUNT=108 FAIL_COUNT=0`.

Independent checks confirmed:

| Evidence | Result |
|---|---|
| Canonical routes | 33/33 IDs and paths; unique route IDs, paths, and route-instance IDs |
| Exclusions | 9/9 exact accepted IDs in `foundation-flow-coverage.csv` |
| Wayfinding | 15/15 exact room IDs; five wings and ten services retain route/path/title/release semantics |
| Actions | ACT-01 through ACT-53 present exactly once as action coverage rows |
| UX tests | UXTEST-001 through UXTEST-045 present in traceability and linked-test unions |
| Non-route families | All 12 required package flow families represented |
| Reusable references | 40 unique `TPL-*` records; route instances use distinct `INST-*` identities |
| Responsive/mode contract | Required 320, narrow, landscape, tablet, desktop, wide, 400% reflow, standard, reduced-motion, low-power, non-WebGL, forced-colors, grayscale, unavailable-font/image, print, keyboard, and screen-reader values are named |
| State contract | Rest, loading, empty, pending, success, unavailable, offline, error, permission, session, asset, checksum, focus, and surface-specific states are named |
| Authority | D-025, D-026, D-035, and D-036 are explicit and correctly treated as accepted definition authority |
| Booking behavior | Route/template/flow records state that Book is direct, non-WebGL, and requires no prior help; the defect is the later batch prerequisite described below |
| Content/asset/evidence gates | Exact public/legal/provider/owner facts, rights, and operational capability remain held; unsupported claims and false success are prohibited |
| Future visual evidence | `DESIGN_SYSTEM_IMPLICATIONS.md:331-371` names the later inventory, tokens, primitive states, all source families, responsive captures, focus/keyboard, contrast/modes, screen-reader semantics, content review, trace ledgers, and implementation parity evidence |
| Review gates | `README.md:99-115` and `UI_REFERENCE_DESIGN_CONTRACT.md:378-397` require later independent design and accessibility review plus founder visual approval |
| MA-024 boundary | `UI_REFERENCE_DESIGN_CONTRACT.md:423-427` defines MA-024 as documentation acceptance only and keeps external-write authority false and separate |
| Safety scan | No external URL, credential/private-key assignment pattern, binary asset, provider asset, or external design write was found |

The deterministic validator is therefore structurally green. It is not semantically sufficient for the batch plan, as findings UIR-DR1-002 and UIR-DR1-003 demonstrate.

## 5. Findings

| ID | Severity | Location and evidence | Finding | User / implementation impact | Concrete acceptance condition |
|---|---|---|---|---|---|
| UIR-DR1-001 | HIGH | `design-batch-plan.csv:7`, B06 `prerequisites`; `DECISIONS.md:30`; `PROJECT.md:64-65`; `docs/phase-1-ux-architecture/UX_ARCHITECTURE.md:5-10,158-166,327-328`; `docs/phase-1-ux-architecture/FLOWS.md:99-105` | B06 may start only after B05 AI/handoff/media/contact visual evidence is accepted. This makes production of the core booking reference depend on optional assistance work, despite the accepted direct-booking independence rule. A production dependency is not itself an end-user step, but this contract is the sequencing authority and therefore creates an avoidable coupling contrary to the approved journey boundary. | The later visual producer could postpone or reshape the primary conversion journey around optional AI/handoff readiness. Booking would no longer be independently producible when optional help is unavailable or blocked by separate provider/privacy decisions. | Remove B05 acceptance from the B06 prerequisite. B06 may depend on the shared semantic shell/recovery foundation and its own held booking-policy inputs, while explicitly retaining no prior AI, human, media, World, account, audio, or upload dependency. Any cross-surface consistency review with B05 must be non-blocking. |
| UIR-DR1-002 | HIGH | `design-batch-plan.csv:2,6-7,9`; accepted flow IDs at `docs/phase-1-ux-architecture/FLOWS.md:10,65,99,131,161,179,191,204,343`; accepted action ownership at `docs/phase-1-ux-architecture/STATES_AND_RECOVERY.md:31-70`; exact exclusions at `docs/phase-1-ux-architecture/excluded-surfaces.csv:2-10`; canonical evidence families at `DESIGN_SYSTEM_IMPLICATIONS.md:345-348` | The batch instance/source map contains invented IDs, invalid ranges, vague placeholders, and misassigned actions. B01 assigns staff-queue action ACT-43 to the semantic shell. B05 names nonexistent `AI-01`, `HF-01`, and `MF-01`, uses unbounded “related ACT records,” and does not name `ROUTE-CONTACT`. B06 names nonexistent `BF-02` through `BF-07`, assigns AI/handoff ACT-14 through ACT-19, and omits booking ACT-29 through ACT-31. B08 invents `EXCL-ADMIN-WILDCARD`, `EXCL-LOGIN`, `EXCL-API`, `EXCL-PREVIEW`, and `EXCL-PREVIEW-WILDCARD`, and assigns booking/contact ACT-29 through ACT-32 to staff/publication work. | A later producer cannot follow the batch contract without guessing which accepted flows, actions, route instance, and exclusion states to design. It can yield missing booking reconciliation/reschedule/cancel evidence, staff controls in public-shell work, fabricated excluded surfaces, and duplicated or orphaned references. | Replace every batch reference with explicit accepted IDs and document one primary production batch per route/flow/action/exclusion, with deliberate shared/final-proof duplication labeled separately. At minimum: B01 must name ACT-01 through ACT-05 only; B04 must own ACT-13; B05 must name `ROUTE-CONTACT`, AF-01, AF-02, CF-01, ACT-14 through ACT-19, and ACT-32; B06 must name `ROUTE-BOOK`, `FLOW-BOOKING-LINEAGE`, BF-01, BF-01A through BF-01E, and ACT-20 through ACT-31; B07 must explicitly name ACT-06 through ACT-12 and ACT-40; and B08 must use only exact accepted exclusion IDs plus ACT-33 through ACT-39 and ACT-41 through ACT-53. Expand these accepted ranges into individually resolvable IDs in the executable field. Eliminate “related,” count-only, synthetic, and nonexistent range references. |
| UIR-DR1-003 | MEDIUM | `validation/validate-ui-reference-design.ps1:329-336`; reproduced validator result `PASS 108/0`; invalid batch values at `design-batch-plan.csv:2,6-7,9` | The validator checks batch ID set, sequence, authorization status, and `template_ids`, but never parses or resolves `route_or_flow_instances`, never validates primary ownership, and never checks the B06 dependency boundary. The invalid references in UIR-DR1-002 therefore pass deterministically. | A green report currently gives false confidence about the most operational part of the handoff contract. The same class of typo or semantic misassignment could recur in later revisions without detection. | Extend the validator to resolve every exact route, accepted flow/subflow, action, exclusion, wayfinding, and UX-test reference used by batches; reject unknown IDs, opaque ranges, and unresolved prose; verify primary-batch completeness/ownership; and assert that booking production is not gated by AI/handoff/media/World evidence. The revised package must rerun with zero failures. |
| UIR-DR1-004 | MEDIUM | `UI_REFERENCE_DESIGN_CONTRACT.md:154-168`; `reference-template-inventory.csv:21-22,27,41`; primary template assignments in `design-batch-plan.csv:2,8-10` | Four canonical baseline evidence names disagree with their primary production batch: global navigation and directory search are named B02 but assigned to B01; Quick Access recovery is named B09 but assigned to B07; system recovery is named B09 but assigned to B01. B09 is the final evidence freeze, not the first production owner. | Stable evidence IDs can be created under the wrong batch, confusing review ownership, dependency completion, deltas, and later one-to-one design/implementation parity. Because IDs are specified as stable, correcting them after visual production would be expensive. | Align each baseline frame's `<BATCH>` token with its declared primary production batch, or define a distinct, validator-enforced rule for cross-batch/final-proof representatives that preserves one unambiguous primary owner. Add a validator assertion for the chosen rule before any external design write. |
| UIR-DR1-005 | MEDIUM | `traceability.csv:271-272`; no `MA-024` or `GATE-EXTERNAL-DESIGN-WRITE` record exists in current `MANUAL_ACTIONS.md`; package definitions at `README.md:108-113` and `UI_REFERENCE_DESIGN_CONTRACT.md:423-427` | The two new gate rows claim `MANUAL_ACTIONS.md` as a source artifact even though neither identifier exists there. The gate wording inside the package is correct, but its provenance field is not currently truthful. | Reviewers may believe the durable manual-action ledger already contains an actionable gate and external-write denial when it does not, weakening handoff and resume reliability. | Until an authorized coordinator separately creates the root records, cite only the package files that actually define these proposed gates and label their durable-record state accurately. If root write authority is later granted, add exact, separate records for definition-only MA-024 and the false future external-write gate, then update traceability without merging their authority. |
| UIR-DR1-006 | MEDIUM | `design-batch-plan.csv:3` B02 and `design-batch-plan.csv:5` B04; global requirement at `UI_REFERENCE_DESIGN_CONTRACT.md:380-393`; `README.md:99-115`; `DESIGN_SYSTEM_IMPLICATIONS.md:331-348` | The normative contract says every batch produces independent design and accessibility findings, but B02 names only independent design review and B04 says only “independent review.” All other batch rows name accessibility explicitly. | A later producer using the CSV as the execution checklist could close core public/evidence batches without the required independent accessibility review, leaving responsive, focus, contrast, reflow, and semantic issues unreviewed until the final batch. | Make both B02 and B04 explicitly require independent design **and** accessibility review, or reference one validator-enforced mandatory review rule from every batch row. Add a check that all B01-B09 rows carry both obligations. |

## 6. Severity summary

| Severity | Count | Disposition |
|---|---:|---|
| CRITICAL | 0 | None |
| HIGH | 2 | Must resolve before founder decision |
| MEDIUM | 4 | Must resolve before founder decision |
| LOW | 0 | None |

There are six unresolved findings. No item is merely a visual preference; each is a contract, traceability, validation, or mandatory-review defect. The corrections align to already accepted authority and do not require a new visual direction or product decision.

## 7. Limitations

- This is a documentation-contract review. Visual quality, actual component anatomy, responsive rendering, motion, asset quality, screen-reader output, browser behavior, and implementation parity cannot be judged before separately authorized reference production exists.
- No live provider, mailbox, calendar, AI, media, staff identity, deployment, or publication capability was tested or inferred.
- The green validator result is reported as reproduced structural evidence, not as proof that the batch semantics are correct.
- This pass does not approve compatibility inventory MA-013, MA-024, external design write, final visual direction, complete Phase 1, or implementation.

## 8. Verdict and next review condition

**REVISE.** The package is broad, mostly well-gated, and structurally complete, but it is not ready for founder decision while two HIGH and four MEDIUM findings remain.

Producer iteration 2 should correct the batch mapping and booking prerequisite first, then strengthen validation, reconcile frame/batch ownership, make gate provenance truthful, and make every batch's design/accessibility review obligation explicit. After the producer reruns the validator, records a new 13-file freeze hash, and updates producer inspection, submit that frozen revision for one independent review pass. No external Figma/Stitch write or application implementation is authorized in the meantime.
