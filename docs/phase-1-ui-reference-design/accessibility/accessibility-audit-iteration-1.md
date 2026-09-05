# Independent Accessibility Audit — UI Reference-Design Contract

**Audit date:** 2026-09-03  
**Audit iteration:** 1  
**Producer package reviewed:** Iteration 2 of 3  
**Target used for this audit:** WCAG 2.2 Level AA plus accepted Hengshi journey requirements  
**Verdict:** **REVISE**  
**Finding summary:** 0 CRITICAL, 1 HIGH, 2 MEDIUM, 0 LOW

## 1. Independence, authority, and boundary

This is an independent accessibility review of a documentation-only UI
reference-design contract. The reviewer did not produce or revise the 13 frozen
producer artifacts. This audit adds only this report.

The audit uses D-025, D-026, D-035, and D-036 as accepted authority. Historical
status labels retained inside frozen accepted inputs are subordinate to those
decisions. The review does not approve a screen, component library, application,
3D experience, public or legal copy, provider behavior, asset, publication,
deployment, or WCAG conformance.

MA-024 remains a package-proposed, definition-only founder gate that is not yet
recorded in root durable manual-action records. It cannot be presented for
approval while this report has unresolved HIGH or MEDIUM findings. MA-024 would
not authorize Figma or Stitch production. External Figma/Stitch production or
write remains a separate future gate whose current authorization is false.

## 2. Frozen scope

The reviewed producer scope contains 13 files. Files below `reviews/` and
`accessibility/` are excluded from the producer freeze. The existing design audit
was read as context but was not treated as producer evidence.

The freeze was recomputed from uppercase per-file SHA-256 values followed by two
ASCII spaces and workspace-relative forward-slash paths, sorted by full path and
LF-joined without a terminal newline.

**Expected aggregate SHA-256:**
`0E59192491A7D4493E1AAEC00960CF10A9FAD9EF9DA30146427CC6D2CA7FB754`

**Observed aggregate SHA-256:**
`0E59192491A7D4493E1AAEC00960CF10A9FAD9EF9DA30146427CC6D2CA7FB754`

**Freeze result:** MATCH

| Frozen producer artifact | SHA-256 |
|---|---|
| `component-primitives.csv` | `0C049C70EF28804DA502449732B8A4389BECF50E7F836F658932730942D4BDCB` |
| `DESIGN_SYSTEM_IMPLICATIONS.md` | `288AA82DB739802F1BC9BD4C573ACF16A648E5895644ECE82E34870D025B1FB8` |
| `design-batch-plan.csv` | `557203F86428653CDC96FA680DDBC7DF7A54B4343237CA7E981C447BF78B0E58` |
| `foundation-flow-coverage.csv` | `A5E2193A9232861568A02755413E24C92962DCEBFEF4493D99A4C990FB5BF069` |
| `foundation-route-coverage.csv` | `E2C7D1920D0A6FFC253FBCC493FB577C1642ECC4F1EE1531CFA1E87AA054A9E1` |
| `producer-inspection.md` | `46908A953C1A1D0CDE5E5CE6DB148145176099360190C219EBF83B10E2683BF2` |
| `README.md` | `B69B39C957863EABE126144EA6688135DA2B4721AF11EDB4D9C22785E8A30184` |
| `reference-template-inventory.csv` | `E21594CF76EC48416A00C738679D36FF21F57B3DACCD7DDC529A8D3B833889B7` |
| `responsive-state-mode-matrix.csv` | `23D074186AF2255D74DA46003630EDC848356F5C7A3453EC8781667D9C47C56A` |
| `traceability.csv` | `03DDA2F07748FF72C64D1CC500EBBF9B0C0A8892E4CE62676BB2040187882888` |
| `UI_REFERENCE_DESIGN_CONTRACT.md` | `702C571C04B6D27AA67EB500B921236B710B64AE9DB2ABF58E36FA9DB69D014A` |
| `validation/validate-ui-reference-design.ps1` | `5CCCD6B7C64E9BACBB15A3BD90F3401707EFD7DCEF30DC6C8A3E281C7C3AD551` |
| `validation/validation-report.md` | `A43E348178E7090066553F65AE9996274C34D09C02FDE23870267C4FD7077814` |

## 3. Standard, supported contexts, and tested scope

The audit benchmark is all applicable WCAG 2.2 Level A and AA requirements,
including complete-process and third-party-step scope, plus accepted UX-001,
UX-003 through UX-005, NFR-006, UXTEST-001 through UXTEST-045, and the D-036
accessibility corrections.

The reviewed contexts were:

- latest two stable evergreen browser releases, with Safari/iOS 16.4 as the
  minimum legacy floor, and semantic Quick Access for unsupported clients;
- 320 CSS px, 400% zoom/reflow, landscape mobile, tablet, desktop, and wide;
- keyboard and screen-reader semantics, touch/single-pointer use, forced colors
  and high contrast, grayscale, reduced motion, and low power;
- non-WebGL, unavailable font/image/asset, offline, error, stale, permission,
  expired-session, ambiguous-provider, and recovery states; and
- print for public decision/evidence/trust/insight/booking-summary and applicable
  staff audit/review surfaces.

Coverage included all 33 canonical route records; nine exclusions; 15 wayfinding
records; 12 package flow families; 32 accepted journey, flow, and subflow IDs;
53 actions; 45 UX tests; 40 reusable templates; 27 state/viewport/mode profiles;
62 primitives; and nine production batches. The complete booking lineage,
AI/human/media/contact paths, first/return visit, World/Quick Access parity,
staff/publication/auth/session processes, and shared failure recovery were
inspected rather than inferred from counts alone.

## 4. Method and evidence

1. Read the governing records, constitution, project state, tasks, decisions,
   risks, manual actions, accepted software definition, and accepted foundation,
   brand strategy, brand identity, UX architecture, and final UX accessibility
   audit.
2. Parsed every package CSV and the accepted route, exclusion, wayfinding,
   requirement, action, flow, and test sources. Compared exact ID sets and then
   inspected the content of route, flow, template, profile, primitive, and batch
   records.
3. Checked semantics; names, roles, values, and states; keyboard/focus; forms and
   errors; status/live regions; pointer cancellation, target size, label in name,
   and non-drag alternatives; contrast/non-color cues; reflow/order; motion,
   flashing, and timing; input purpose/redundant entry/authentication; media;
   degraded/recovery; non-WebGL parity; content stress; and provider-process
   scope.
4. Reviewed primitive anatomy, variants, pseudo-states, transactional states,
   redundancy, modes, expected implementation evidence, and gated facts. Also
   checked batch source ownership and sequencing for accessibility traceability.
5. Ran the package validator and independent term/freeze checks. Automated checks
   support this audit but are not proof of accessibility.

The validator returned:

```text
RESULT=PASS PASS_COUNT=145 FAIL_COUNT=0
```

That structural result is valid but does not exercise the three missing normative
requirements reported below.

## 5. Definition-level coverage evidence

| Area | Contract evidence inspected | Disposition |
|---|---|---|
| Route, exclusion, flow, and action completeness | Exact records for 33 routes, nine exclusions, 15 wayfinding entries, 12 flow families, 32 accepted experience IDs, 53 actions, and 45 tests; one resolved primary batch owner for all 154 primary source IDs | Adequate at definition level |
| Batch accessibility traceability | B01-B09 each explicitly require independent design review and independent accessibility review; B06 depends only on B01 and owns booking actions ACT-20 through ACT-31 | Adequate; earlier free-text/synthetic-ID and sequencing risks are corrected in this freeze |
| Semantics, names, roles, states, and reading order | Contract sections 7, 8, and 10; all template interaction/focus notes; primitive anatomy and evidence obligations, especially PRIM-001 through PRIM-006, PRIM-039, and PRIM-055 through PRIM-061 | Adequate at definition level |
| Keyboard and focus | Logical order, skip links, unclipped visible focus, focus entry/return, Escape/cancel, no trap, error-summary movement, no focus theft, and sticky/HUD non-obscuration | Adequate at definition level |
| Forms, errors, status, and live regions | Persistent labels/descriptions, linked errors and summaries, retained valid values, pending-versus-success separation, deduplicated announcements, refresh, and safe recovery | Adequate at definition level |
| Pointer and touch | Pointer-up cancellation, 24 by 24 CSS px target or documented exception, visible label in accessible name, keyboard and single-pointer non-drag alternatives; UXTEST-039 | Adequate at definition level |
| Contrast and non-color meaning | Per-state 4.5:1 text and 3:1 meaningful non-text/focus thresholds, forced-colors/grayscale evidence, text plus shape/icon/border/pattern/position redundancy | Adequate at definition level; rendered values remain future evidence |
| Zoom, reflow, orientation, and responsive order | VP-320, VP-NARROW, VP-LANDSCAPE, VP-TABLET, VP-DESKTOP, VP-WIDE, VP-ZOOM-400; content-stress, text-spacing, sticky-obstruction, table/list, keyboard, and safe-area annotations | Adequate at definition level |
| Motion, flashing, and time | Stable reduced-motion states, pause/stop/hide over five seconds, three-flashes limit, controlled update and preserved-state obligations | Partial; exact accepted time-limit alternatives are lost in the package (A11Y-UIR-I1-003) |
| Input purpose, repeated entry, and accessible authentication | Programmatic input purpose, autocomplete, no invented token, preserved/selectable prior input, review/correct/confirm, paste/password-manager/assistive support, and third-party steps in UXTEST-042/043 | Adequate at definition level |
| Media | Audio-only transcript, prerecorded captions, separate SC 1.2.3 handling and SC 1.2.5 audio-description obligations, live captions, per-item applicability evidence, and media-only hold | Adequate at definition level |
| Offline, unavailable assets, non-WebGL, and recovery | Named profiles and focused evidence for failure classes, authoritative-state preservation, semantic Quick Access, no canvas-only content, and no false success | Adequate at definition level |
| Target standard | Accepted UX-001 declares WCAG 2.2 AA, but the frozen package does not | Inadequate (A11Y-UIR-I1-001) |
| Browser/platform support | Trace row TR-REQ-097 asks for a browser matrix, but no package artifact states the accepted NFR-006 matrix | Inadequate (A11Y-UIR-I1-002) |

## 6. Findings

| ID | Severity | Requirement / exact location | Reproduction | Affected users and barrier/risk | Required remediation and acceptance test |
|---|---|---|---|---|---|
| A11Y-UIR-I1-001 | HIGH | UX-001; accepted `UX_ARCHITECTURE.md` section 8; WCAG 2.2 conformance target and all applicable Level A/AA criteria. Missing from the normative target/status language in `README.md`, `UI_REFERENCE_DESIGN_CONTRACT.md`, `DESIGN_SYSTEM_IMPLICATIONS.md`, and their validator assertions. The design-system file says only “AA target” for one media obligation. | Search all 13 frozen producer files for `WCAG 2.2` and `Level AA`; both return zero matches. Compare accepted UX-001, which explicitly says WCAG 2.2 AA is the target and not a current conformance claim. | All disabled users are exposed to an unstable standard baseline. A later producer or reviewer could apply a different WCAG version/level, omit applicable WCAG 2.2 criteria or accept an exception against the wrong standard, while the package still passes its validator. | Add one normative, package-wide declaration that WCAG 2.2 Level AA is the target for all applicable full pages and complete processes, including third-party steps, and that neither the definition nor future reference designs alone establish conformance. Reference it from the README, contract, evidence plan, trace row UX-001, and each production/review gate. Add a validator assertion for the exact target and non-conformance disclaimer. Acceptance: the refreshed freeze contains the explicit target, later evidence is evaluated against it, and any exception names the criterion, standards-supported rationale, affected flow, fallback, and independent-review acceptance. |
| A11Y-UIR-I1-002 | MEDIUM | NFR-006 and UX-005; `traceability.csv` record TR-REQ-097 names `responsive-state-mode-matrix.csv`, `UI_REFERENCE_DESIGN_CONTRACT.md`, and `design-batch-plan.csv`, but records only “Browser matrix; unsupported gets Quick Access.” No cited artifact defines that matrix. | Search all 13 frozen producer files for `latest two`, `Safari`, `iOS 16.4`, and `unsupported client`; each returns zero matches. The accepted NFR-006 requirement specifies the latest two stable evergreen releases, Safari/iOS 16.4 floor, and semantic Quick Access for unsupported clients. | Keyboard, screen-reader, touch, zoom, and mobile Safari users may receive reference evidence that was never required to account for the approved browser/platform floor. Unsupported-client recovery may be shown conceptually without a testable classification and handoff to semantic Quick Access. | Add a normative browser/platform profile and batch evidence rule that carries NFR-006 exactly: current latest two stable evergreen releases, Safari/iOS 16.4 minimum legacy floor, and semantic Quick Access below/otherwise unsupported. Keep current-version selection as dated later QA evidence rather than inventing versions now. Acceptance: every affected public/interactive/World reference maps to the profile; Safari mobile layout/input/safe-area concerns and unsupported-client recovery are annotated; the validator fails when the profile, exact floor, or Quick Access outcome is absent. |
| A11Y-UIR-I1-003 | MEDIUM | WCAG 2.2 success criterion 2.2.1 Timing Adjustable; accepted `UX_ARCHITECTURE.md` section 8, `STATES_AND_RECOVERY.md` timeout contract, and UXTEST-040. The package reduces this to `UI_REFERENCE_DESIGN_CONTRACT.md` section 10 item 5 “explicit timing/extension behavior,” `DESIGN_SYSTEM_IMPLICATIONS.md` section 5 “warning/extension,” and UXTEST-040 trace text “per WCAG.” | Search all 13 frozen producer files for `20 seconds`, `ten times`, and `10 times`; each returns zero matches. Inspect PRIM-039, PRIM-042, PRIM-055 through PRIM-058 and the auth/booking/session records: they request timeout evidence but do not preserve the accepted alternatives or thresholds. | Users with cognitive, motor, reading, low-vision, or assistive-technology needs could receive a warning too late or an extension too small to complete booking verification, reauthentication, staff work, or another timed step. A reference could pass the current generic wording while violating the accepted policy. | Carry the accepted rule verbatim at contract level: each user time limit is removable or adjustable before it starts, or warns with at least 20 seconds and permits a simple extension at least ten times, or has a documented criterion-supported exception. Preserve permitted data and last authoritative state, then offer accessible reauthentication. Exact session/challenge durations remain gated. Acceptance: timed route/flow/primitive records select an allowed branch, controlled-clock evidence covers warning, extension, expiry, focus/status, and recovery, and a validator check fails if the alternatives/thresholds or exception record are absent. |

## 7. Severity summary and gate

| Severity | Open | Gate effect |
|---|---:|---|
| CRITICAL | 0 | None |
| HIGH | 1 | Blocks accessibility PASS and MA-024 presentation |
| MEDIUM | 2 | Block accessibility PASS and MA-024 presentation |
| LOW | 0 | None |

**Verdict: REVISE.** Producer iteration 2 is structurally complete and has
corrected the earlier design-review batch mapping, booking dependency, provenance,
and review-gate issues. It is not yet a complete, testable accessibility contract
because the governing WCAG version/level, accepted browser floor, and accepted
timing thresholds are absent from the frozen package.

A later audit may return PASS only after all HIGH and MEDIUM findings above are
closed in a newly frozen producer revision and the validator is rerun. A standards
exception, target-standard change, or product-level accommodation tradeoff
requires human approval and later independent reviewer acceptance.

## 8. Limitations

- No Figma or Stitch file, visual screen, prototype, browser URL, application, or
  implementation exists in scope. No visual contrast value, responsive rendering,
  keyboard behavior, focus behavior, touch target, announcement, screen-reader
  output, media alternative, provider step, or browser result was executed.
- No automated accessibility scanner was applicable to this documentation-only
  package. The deterministic validator and term/set checks establish structural
  evidence only and are not accessibility or conformance proof.
- No legal/privacy copy, provider configuration, exact session/challenge duration,
  media rights, real content, asset provenance, production data, or final visual
  direction was accepted or inferred.
- Implementation, publication, deployment, production testing, and final WCAG
  conformance remain future independently reviewed gates.
