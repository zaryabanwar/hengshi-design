# Independent Accessibility Audit — UI Reference-Design Contract, Iteration 2

**Audit date:** 2026-09-03  
**Producer package reviewed:** Iteration 3 of 3; final producer freeze  
**Prior audit:** Accessibility audit iteration 1  
**Target:** WCAG 2.2 Level AA and accepted Hengshi accessible-journey requirements  
**Verdict:** **PASS**  
**Open findings:** 0 CRITICAL, 0 HIGH, 0 MEDIUM, 0 LOW

## 1. Independence and decision boundary

This is an independent, documentation-only accessibility audit. The reviewer did
not produce or revise any frozen producer artifact. The only write made by this
reviewer is this report.

The audit determines whether A11Y-UIR-I1-001 through A11Y-UIR-I1-003 are closed
and whether producer iteration 3 introduces a new accessibility-contract blocker.
It cannot approve visual direction, accept a standards exception, authorize an
external design write, or establish implementation conformance.

Accepted D-025, D-026, D-035, and D-036 control this review. Stale labels retained
inside accepted source artifacts remain subordinate to those decisions and were
not changed.

## 2. Scope and freeze proof

The producer freeze contains 13 files under
`docs/phase-1-ui-reference-design/`, excluding `reviews/**` and
`accessibility/**`. The existing design and accessibility reports were reviewed
as contextual evidence but were not included in the producer hash.

The freeze was independently recomputed by sorting package-root-relative
forward-slash paths ordinally, emitting uppercase per-file SHA-256, two ASCII
spaces, then the path, joining with LF and no terminal newline, and hashing the
UTF-8 no-BOM payload.

- Expected aggregate:
  `97E79201CC36F01718A027AD800E63BDD5AAFC47E41137D65253BAABA6B2120F`
- Observed aggregate:
  `97E79201CC36F01718A027AD800E63BDD5AAFC47E41137D65253BAABA6B2120F`
- File count: 13
- Freeze result: **MATCH**

| Frozen artifact | SHA-256 |
|---|---|
| `DESIGN_SYSTEM_IMPLICATIONS.md` | `DCF2F63D11BB45CB71568B18A0E16C95BD94F1991CBE23B5B677D832F1310AD2` |
| `README.md` | `1C40C2B8F5F9C5399754A6C68403098987865FBAC6302B75EDBB60C20B40E690` |
| `UI_REFERENCE_DESIGN_CONTRACT.md` | `1FAAA7D74A4214DA6F5453238B601380BF172AEFA07BD57AC8DAE716E2597DFD` |
| `component-primitives.csv` | `2D01496DCC7D9C062AD77E52CC9F0F110D3F7B4CE899D95A52A8B6F7311E6F4A` |
| `design-batch-plan.csv` | `CC3D8013770BA99C7C16C328CEAE8E67F1F56A0D5D550DC48F9CC046F6220E4F` |
| `foundation-flow-coverage.csv` | `40C6DBD3F6265905B7EA4AA738B1C79D32707F15AEBBC4606BEF43D74447D231` |
| `foundation-route-coverage.csv` | `8CBF812D87BF3F94CDF9BE7F8C97CFA476DBEC344D4B86AAF59833F2EDAD9928` |
| `producer-inspection.md` | `62DBE121EBF808797322E03D1F9465A1F46DE0E400D3423DDD06D0C358FFBAA0` |
| `reference-template-inventory.csv` | `BA055C1D15A1E3639A42A8E3AC3AF076EA2FB73E3A5FE88BD95FE0FCBFBCEBD3` |
| `responsive-state-mode-matrix.csv` | `2E1D86E11DFE49C619AE87EFFCE0E0A3BB8225AE660FB2F51CBAECA536658A6B` |
| `traceability.csv` | `D174505EFFF657FE6F8B829F24D3D4EFCABBBB7F24168E06AD634D398295C5A5` |
| `validation/validate-ui-reference-design.ps1` | `6AA1283040304ACC91D7DA3C72342A210ECC9CC0B0862BF818FE0D722168A495` |
| `validation/validation-report.md` | `E095C952390B8A23FF89AD0D847C989AEB9904CA47BF42E4024DBC3BD76FEA2B` |

## 3. Standard, contexts, and complete reviewed inventory

The review applies all applicable WCAG 2.2 Level A and AA success criteria to
future full pages and complete processes, including represented third-party
steps. The reference package is also evaluated against accepted UX-001, UX-003
through UX-005, NFR-006, UXTEST-001 through UXTEST-045, and the final D-036
accessibility corrections.

Supported contexts reviewed are the current latest two stable Chrome, Edge,
Firefox, and Safari release families selected at the later dated QA run;
Safari/iOS 16.4 as the minimum legacy floor; semantic Quick Access for clients
below the floor or otherwise unsupported; 320 CSS px and 400% zoom/reflow;
landscape mobile, tablet, desktop, and wide; keyboard, screen-reader semantics,
touch/single pointer, forced colors/high contrast, grayscale, reduced motion,
low power, non-WebGL, unavailable font/image/asset, offline/error/recovery, and
print where applicable.

The reviewed inventory comprises:

- 33 canonical routes, nine exclusion classes, and 15 wayfinding entries;
- 12 package flow families, 32 accepted journey/flow/subflow IDs, 53 actions,
  and 45 UX tests represented by 89 flow records;
- 40 reusable templates and 32 viewport, mode, state, browser, and time-limit
  profiles;
- 62 primitives and nine production batches; and
- complete direct-booking, AI, human-handoff, media, contact, World/Quick Access,
  staff, publication, authentication, provider-step, and shared recovery paths.

## 4. Method and validation evidence

The review read the governing records, accepted source packages, prior audit,
relevant design reviews, and every frozen producer artifact. It parsed every CSV,
compared source and package ID sets, inspected every route/flow/template/profile/
primitive/batch record, and checked the three corrected requirements in normative
prose, traceability, machine-readable mappings, batch evidence, and validation
assertions.

Manual definition-level review covered semantics; names, roles, values, and
states; keyboard/focus; contrast and non-color cues; zoom/reflow and responsive
order; forms, errors, and status announcements; motion, flashing, and time;
pointer cancellation, target size, label in name, and non-drag alternatives;
input purpose, redundant entry, and accessible authentication; media alternatives;
content stress; unavailable/offline/recovery; non-WebGL parity; and complete
third-party/provider-process scope.

Independent mapping checks found:

- zero browser-profile gaps across 33 routes, 89 flow records, 40 templates, 32
  profiles, and B01-B09;
- zero unresolved time-limit branch IDs and zero selected `TL-EXCEPTION` records;
- all 62 primitives transitively mapped through their referenced templates to
  `BP-NFR-006` and the applicable contextual `TL-*` evidence;
- all 56 interactive or composite-interactive primitives retain base, hover,
  focus-visible, pressed, and disabled variants; and
- all nine batches require the WCAG target review, independent accessibility
  review, browser-floor evidence, and an explicit time-limit branch outcome.

The validator was rerun with exit code 0:

```text
RESULT=PASS PASS_COUNT=183 FAIL_COUNT=0
FREEZE_AGGREGATE_SHA256=97E79201CC36F01718A027AD800E63BDD5AAFC47E41137D65253BAABA6B2120F
```

Automated checks are supporting evidence only; they do not prove accessibility.

## 5. Prior finding dispositions

| Prior finding | Required correction | Verified closure evidence | Disposition |
|---|---|---|---|
| A11Y-UIR-I1-001 — HIGH | State WCAG 2.2 Level AA for every applicable full page and complete process, including third-party steps, while rejecting a current conformance claim. | `README.md` normative accessibility section; `UI_REFERENCE_DESIGN_CONTRACT.md` section 2.3 and batch-review contract; `DESIGN_SYSTEM_IMPLICATIONS.md` section 1.2; trace record TR-REQ-052; B01-B09 review fields; validator positive and negative assertions. All layers use the same target and preserve the implementation-evidence requirement. | **CLOSED** |
| A11Y-UIR-I1-002 — MEDIUM | Carry exact NFR-006 browser families/floor, defer exact current versions to dated QA, require mobile Safari evidence, and recover unsupported clients to semantic Quick Access. | Profile BP-NFR-006 defines the current latest two stable Chrome/Edge/Firefox/Safari release families, Safari/iOS 16.4 floor, dated version selection, mobile layout/input/virtual-keyboard/orientation/safe-area evidence, and below-floor/otherwise-unsupported Quick Access. All routes, flows, templates, profiles, and B01-B09 map to it; all 62 primitives inherit it through template mappings. Trace records TR-REQ-056 and TR-REQ-097 and the negative fixture preserve the boundary. | **CLOSED** |
| A11Y-UIR-I1-003 — MEDIUM | Preserve every SC 2.2.1 branch, the 20-second/10-times thresholds, exception path, state/data preservation, accessible reauthentication, and gated exact durations. | Profiles TL-REMOVABLE-ADJUSTABLE, TL-WARN-EXTEND, TL-EXCEPTION, and TL-NOT-APPLICABLE are explicit. Route, flow, template, profile, primitive-through-template, and batch evidence resolves to allowed contextual branches. TL-WARN-EXTEND requires warning at least 20 seconds before expiry and a simple extension at least 10 times; exceptions require criterion-supported rationale and reviewer acceptance; no current record selects an exception. TR-TEST-040 and affected primitives require controlled-clock, preservation, focus/status, and accessible-reauthentication evidence while exact durations remain gated. | **CLOSED** |

## 6. Complete definition-level coverage

| Area | Evidence and outcome |
|---|---|
| Semantics and content order | Native landmarks/headings/lists/links/buttons/fields/tables/dialogs are preferred; composite names, roles, states, properties, reading order, and canvas-independent equivalents require annotations. Adequate. |
| Keyboard and focus | Logical order, skip paths, visible unclipped focus, focus entry/containment/return, Escape/cancel, post-navigation/error-summary focus, no trap, and no sticky/HUD obstruction are required. Adequate. |
| Forms, errors, and status | Persistent labels/descriptions, programmatic relationships, required/optional text, linked summary, preserved valid values, pending/success separation, deduplicated live announcements, and manual refresh are required. Adequate. |
| Pointer and touch | Pointer-up cancellation, 24 by 24 CSS px target or measured exception, label in name, and keyboard/single-pointer non-drag alternatives are required by UXTEST-039 and primitive evidence. Adequate. |
| Contrast and non-color cues | Per-rendered-state 4.5:1 normal-text and 3:1 meaningful non-text/focus evidence, plus text and redundant shape/icon/border/pattern/position cues, forced colors, and grayscale, are required. Adequate at definition level. |
| Zoom, reflow, and orientation | VP-320, VP-NARROW, VP-LANDSCAPE, VP-TABLET, VP-DESKTOP, VP-WIDE, and VP-ZOOM-400 include order, text-spacing, content stress, safe-area, virtual-keyboard, sticky-obstruction, and table/list requirements. Adequate. |
| Motion, flashing, and timing | Stable reduced-motion states, no essential animation wait, pause/stop/hide after five seconds, three-flashes limit, exact SC 2.2.1 branches, controlled-clock evidence, state preservation, and accessible reauthentication are required. Adequate. |
| Input and authentication | Input purpose/autocomplete, no invented tokens, redundant-entry avoidance, review/correct/confirm, paste/password-manager/assistive support, and third-party authentication steps are required. Adequate. |
| Media | Audio-only transcripts, prerecorded captions, separate SC 1.2.3 handling and SC 1.2.5 audio-description obligations, live captions, item-level applicability evidence, and media-only hold behavior are required. Adequate. |
| Degraded and recovery paths | Unsupported clients, non-WebGL, low power, missing assets/fonts, offline, stale, permission, expiry, provider ambiguity, and error states preserve truthful context and the smallest safe semantic action. Adequate. |
| Evidence and review gates | Each batch requires named evidence, route/flow/template deltas, representative responsive/mode/state coverage, browser and timing evidence, independent design review, and independent accessibility review. Adequate. |

## 7. New findings and severity summary

No new accessibility-contract finding was identified.

| Severity | Open count |
|---|---:|
| CRITICAL | 0 |
| HIGH | 0 |
| MEDIUM | 0 |
| LOW | 0 |

## 8. Verdict and retained gates

**PASS.** A11Y-UIR-I1-001, A11Y-UIR-I1-002, and A11Y-UIR-I1-003 are closed,
the 13-file producer freeze matches, the validator passes 183/183, and no new
Critical, High, or Medium accessibility-contract finding remains.

This PASS means only that the frozen definition is sufficient to direct and later
verify accessible reference production without inventing policy. It is not a
claim that any screen, implementation, complete process, third-party step, or
product currently conforms to WCAG 2.2 Level AA.

MA-024 remains definition-only and package-proposed at this freeze. It still
requires clean independent review and authorized root integration before founder
decision. External Figma/Stitch production/write remains separately gated and
currently false. Standards exceptions or target changes, product-level
accommodation tradeoffs, final visual direction, exact public/legal copy,
paid/licensed assets, implementation, publication, deployment, and production
testing remain human gates.

## 9. Limitations

- No Figma/Stitch artifact, visual screen, prototype, browser URL, application,
  UI/3D implementation, or production content exists in this review scope.
- No rendered contrast, responsive layout, keyboard sequence, focus behavior,
  touch target, screen-reader announcement, media alternative, browser behavior,
  or third-party/provider process was executed. Those require later visual and
  implementation evidence.
- No automated accessibility scanner was applicable to this documentation-only
  package. Structural validation and manual contract inspection do not establish
  conformance.
- Exact public/legal/consent/error copy, browser versions at execution time,
  session/challenge/provider durations, provider behavior, asset rights, and real
  content remain gated.
