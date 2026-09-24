# Independent Review — Design-System Amendment R-039 (review 1)

**Review date:** 2026-09-24
**Commissioning decision:** D-046 (2026-09-24), which executes the deferral
recorded at D-045 gate G-6 and requires an independent review of the amendment
before founder acceptance. Risk R-039.
**Subject under review:** `docs/phase-1-ui-reference-design/DESIGN_SYSTEM_AMENDMENT_R-039.md`
[PROPOSED SPECIFICATION], 1081 lines, at commit
`2c469b61d1c7457ab94be133ea15d6a9272bdca5` (2026-09-24, "docs: add [PROPOSED]
design-system amendment R-039 under the D-046 contract"), file SHA-256
`8448E86545EF64D638090DB1EE6BE012EC9918229E2A4213532996C7777CAD6C`. Both values
were taken by me from `git log -1` and `sha256sum` on a clean working tree. This
record reviews that text and nothing else; a later revision is a different
subject and needs its own record.
**Reviewer:** independent review agent. I did not author the amendment, I am not
the D-045 producer, I did not author the D-044 specifications, I wrote no
validator (including `validation/validate-ui-reference-design.ps1`), and I read
no agent transcript and no other agent's working files. I reviewed the committed
text and the sources listed below. Constitution 2.0.0 principle VII.
**Gates covered:** Part A, design-system review; Part B,
accessibility-obligations review. One record, two verdicts.
**Authority I review against, and may not overrule:** `DECISIONS.md` D-045
(resolutions 1 to 7) and D-046; `RISKS.md` row R-039; `TASKS.md` R-039 row;
`accessibility/DELIVERY_STREAM_ACCESSIBILITY_OBLIGATIONS.md` (accepted at
D-045); `DELIVERY_STREAM_EVIDENCE_MODEL.md` (accepted at D-045); the frozen
`DESIGN_SYSTEM_IMPLICATIONS.md` and `component-primitives.csv`;
`responsive-state-mode-matrix.csv`; `design-batch-plan.csv`; `traceability.csv`;
`foundation-flow-coverage.csv`;
`docs/phase-1-ui-reference-production/evidence-capture-plan.csv` and
`batch-production-plan.csv`; `docs/active/3D_Mega_Menu_Style_Guide_v2.md`;
`docs/active/Hengshi_Design_SRS_v3.md`;
`docs/phase-1-brand-identity/semantic-tokens.json`;
`docs/phase-1-ux-architecture/STATES_AND_RECOVERY.md`,
`CONTENT_ANALYTICS_TESTS.md` and `UX_ARCHITECTURE.md`; `CHANGELOG.md`;
`.specify/memory/constitution.md` (revision limits). `packages/design-system/tokens.json`
and `README.md` were read only as the [PROPOSED] input that D-046 names, never as
authority. Format and severity conventions were taken from
`reviews/design-review-iteration-6.md` and
`accessibility/accessibility-audit-iteration-5.md`.
**Conformance target reviewed against:** WCAG 2.2 Level AA for every applicable
full page and every complete process, including represented third-party steps,
holding independently within each of the four peer delivery streams. The
amendment claims no conformance, none is claimed here, and nothing is built.
**Deterministic validator state at review:** `RESULT=PASS PASS_COUNT=208
FAIL_COUNT=0`, `FREEZE_AGGREGATE_SHA256=8DF23FF106A78839581D774EE9DF842D434591ACB781A7E89DA5E2414E32635D`,
`design-system-freeze-hash` PASS at
`0E9FC68C98AC25C4F7DFBC62B10DBA1FCB197F5C82AD2FF39DCD0C16D9CFB763`,
`component-primitives-freeze-hash` PASS at
`EF0DE11B23A6C6A9C8C721D55F528237A72153315B633E6198AF0B50ADED9C78`. I ran it
from the repository root before this record existed and again after writing it;
both runs gave the same numbers and neither modified a tracked file. A passing
validator is a determinism check. It does not scan the amendment for anything
except local Markdown links, and none of the findings below is detectable by it.

**Severity scale.** HIGH: blocking (the package's "Blocking" class). MEDIUM:
significant; under the package convention an independent MEDIUM-or-higher
finding blocks founder acceptance until revised. LOW: minor; does not block, but
each must be resolved or explicitly declined in the next revision.

**Verdicts.** **Part A: PASS.** **Part B: FAIL** on one MEDIUM finding
(DSA-01). **Recommendation: accept after the listed revisions.** One revision
cycle is consumed (cycle 1 of the three the constitution allows for UI work).

---

## Part A — Design-system review — verdict: PASS

### A.1 The three OBL-GRAM-03 hits are present and substantive (Q1)

`OBL-GRAM-03` (obligations lines 274 to 292) requires that the handoff artifact
carry a per-stream contrast rule, a stream-control component, and focus-ring
tokens, and that a search for each returns a hit. I searched the amendment as it
stands and then checked that each hit is a rule a later implementer can apply.

- **(a) Per-stream contrast rule.** §1.3 (lines 156 to 195) states the rule in
  a boxed normative paragraph: every contrast, focus-order and target-size
  measurement, and every other §2.4 verification context, is taken within one
  named stream against that stream's own rendering; a measurement in one stream
  is never inherited by another; evidence whose `EC-08` identifier carries no
  `STREAM_*` token or another stream's token discharges nothing. It gives the
  numeric floors (4.5:1 normal text, 3:1 focus and non-text boundaries, 24 by
  24 CSS px targets), all of which are the frozen file's own §4 and §5 numbers.
  It reaches the frozen file through `INS-10` (a full replacement of the §5
  contrast bullet) and `INS-13` (item 7 of §8). Substantive.
- **(b) Stream-control component.** §3 (lines 296 to 640) specifies
  `HD/Shell and navigation/Delivery stream control` / `DeliveryStreamControl`
  against the `PRIM-001` anatomy: role and activation, names, advisement,
  announcement, keyboard model, above-ceiling options, pseudo-states,
  transactional states, the boundary crossing, mode obligations and reserved
  component tokens. It reaches the frozen file through `INS-06` (taxonomy rows)
  and `INS-08` (a new §3.4 of eleven bullets). Substantive.
- **(c) Focus-ring tokens.** §4.2 (lines 683 to 699) defines
  `semantic.focus.{ring,ring-width,offset}` and
  `semantic.focus.scene.{ring,ring-width,offset,layer,contrast-floor,motion}`
  with a value or rule per row and a source per row; §4.3 resolves them per
  stream. It reaches the frozen file through `INS-04` (three §2.3 rows).
  Substantive.

Three hits, each a rule. One LOW defect in the search hint the amendment offers
for hit (a) is recorded as DSA-09.

### A.2 R-039 exit evidence (Q2)

`RISKS.md` R-039 and D-045 resolution 7 name four additions. All four are
present: the delivery-stream axis as a design-system dimension (§1; `INS-02`,
`INS-05`, `INS-09`); the delivery stream control component (§3; `INS-06`,
`INS-08`); the four stream tokens `semantic.stream.{high,medium,low,semantic}`
as `--hd-stream-{high,medium,low,semantic}` (§2; `INS-04`); and the 3D
focus-ring token family `semantic.focus.scene.*` (§4; `INS-04`). The exit
evidence also requires "produced under its own contract and independently
reviewed"; this record is the review half, and it is not clean until DSA-01 is
revised.

### A.3 Naming and layer rules (Q6)

- Design paths follow `hd/{layer}/{role}/{variant}/{state}/{property}` with
  non-applicable segments omitted: `hd/semantic/stream/{variant}/{property}`,
  `hd/semantic/focus/scene/{property}`, and
  `component.delivery-stream-control.{part}.{state}.{property}`. Code names use
  the `--hd-` prefix in kebab case. The code stems omit the layer segment
  (`--hd-stream-*`, `--hd-focus-scene-*`), which is the frozen file's own
  precedent for `semantic.focus.{ring,offset}` to `--hd-focus-*` (§2.3 line 165)
  and is stated as such at §2.1. Consistent.
- Component set `HD/Shell and navigation/Delivery stream control` follows
  `HD/<Category>/<Component>` with the §3.1 taxonomy name of the authorized host
  (`PRIM-001`, `shell_navigation`); `DeliveryStreamControl` is the same final
  words in PascalCase (§2.4). Variant and state values are kebab case.
- Component tokens (§3.13) reference semantic aliases only, in a "May reference
  only" column, and the table closes with "No component token above carries a
  value in this document". Freeze §2.1 is honoured. The component pattern
  `--hd-delivery-stream-control-{part}-{state}-{property}` uses anatomy parts in
  the `{variant}` slot of the frozen `--hd-{component}-{variant}-{state}-{property}`
  pattern; the frozen text does not forbid that reading. Observation only.
- Two semantic rows carry source-exact values rather than aliases:
  `semantic.focus.scene.ring-width` = 3 px and
  `semantic.focus.scene.contrast-floor` = 3:1, both from style guide §4.1 line
  93. Freeze §2.4 restricts raw *identity* values to the identity layer and
  §2.2 already contains rule-valued rows (`radius.status`), so this is
  permitted. The amendment's distinction between the §4.1 focus row (marked in
  the style guide itself as "normative, not planned") and the §3.1/§4.1 hex
  values (prototype-era; absent from the identity source, which I confirmed by
  grep) is sound. No finding.

### A.4 Mechanical applicability of the application plan (Q5)

Every anchor in `INS-01` to `INS-14` was counted in the frozen file after
whitespace normalisation (line breaks to single spaces; runs of spaces
collapsed), as the plan specifies. All sixteen anchors (two each for `INS-04`
and `INS-06`) occur exactly once. The frozen file's SHA-256 at the time of the
count equals the validator's pinned value, so the anchors were checked against
the pinned revision. Full table at V-07. Every insertion is positionally
unambiguous; the one defect is that `INS-06` describes its anchor instead of
quoting it (DSA-06, LOW). `INS-12` (item 4: `UXTEST-045` to `UXTEST-046`) is
outside the four named additions but is a consequential correction: `UXTEST-046`
is the control's own accepted test (`CONTENT_ANALYTICS_TESTS.md` line 152;
`traceability.csv` `TR-TEST-046`; the validator's `source-ux-test-set` passes on
the 46-test set). I accept it as in scope and note it for the founder. I did not
edit the frozen file.

### A.5 Overreach and silent decisions (Q7)

- No accepted decision is changed. D-039, D-043, D-044, D-045 and D-046 are
  cited as they stand; the D-045 resolution numbers used (1, 3, 5, 6, 7) match
  `DECISIONS.md` lines 85 to 169.
- B01 is not released. The header says so; both plan files still carry
  `future_not_authorized` (design `status`, production `ma_025_disposition`);
  the validator's `design-batch-authorization` passes.
- The Figma allowance rules are not altered. No call is authorised; §1.3
  consequence 4 asserts that the rule adds no frame, and I checked that the
  per-stream `focus-visible` frames §4.4 requires already exist as obligations
  (`OBL-CTRL-04` reviewer test), so the assertion holds.
- No founder question is resolved by the author. Decisions taken without a
  gate or a recorded assumption: the §4.3 rule that `semantic.focus.scene.*`
  resolves to `semantic.focus.*` in `S-SEMANTIC` (DSA-04), and the A-2
  advisement placement written into `INS-08` as fixed anatomy (DSA-05). Both
  are safe and reversible; both need recording, not deciding.
- Listed gates the sources actually answer: none. I checked UG-1 to UG-12
  against the obligations document, the style guide, the SRS and the frozen
  file; each remains open in its named source. UG-4 restates a deferral already
  made (U-03) and is harmless.

### A.6 Format (Q8)

The header follows the D-044 specifications: title carrying **[PROPOSED
SPECIFICATION]**; a Status line stating pending founder decision and no
authority; an Author line stating independence from the D-045 producer, the
CR-002 package, the D-044 specifications and every validator; Date;
Commissioned by; Inputs; Scope of change; Not authorized by this document;
Vocabulary discipline; No conformance is claimed. PASS.

### A.7 Part A findings

DSA-02, DSA-03, DSA-04, DSA-05, DSA-06, DSA-08 and DSA-09, all LOW. No MEDIUM or
HIGH finding in the design-system scope. **PASS.**

---

## Part B — Accessibility-obligations review — verdict: FAIL

### B.1 Obligation-by-obligation result

| Obligation | Where the amendment carries it | Result |
|---|---|---|
| `OBL-INV-03` aggregate evidence discharges nothing | §1.3 rule and the physical reasoning (translucent `bg-gray-900/95 backdrop-blur` panel, style guide §6.2 line 187); `INS-10`; `INS-13` | Met |
| `OBL-GRAM-01` points 2 and 4 | §2.3 (no ordering, rank, weight or quality vocabulary in the token family); §1.2 (`MODE-SEMANTIC-SHELL` is a mode, `S-SEMANTIC` is a stream) | Met |
| `OBL-GRAM-03` three hits | A.1 above; §5 closes all three gaps in the slice that re-opens the file | Met (search hint, DSA-09) |
| `OBL-CTRL-01` role and activation | §3.3: native radios in `fieldset`/`legend`, separate always-present Apply, two-step confirmation, the prohibited patterns | Met |
| `OBL-CTRL-02` names, in-force and pending | §3.4 (group, radio, Apply names; screen-reader script structure; redundancy); §3.8 (above-ceiling text); labels gated at UG-3 | Met |
| `OBL-CTRL-03` presence in every stream | §3.1; §3.12 (`VP-320` in `S-SEMANTIC` through the disclosure); `INS-08` Presence; `INS-14` item 15 | Met |
| `OBL-CTRL-04` keyboard, 2.4.7, 2.4.11, 2.5.8, `Escape` | §3.7; §4.1 to §4.4 (`semantic.focus.scene.layer` carries the not-obscured rule); sampling gate UG-1; §7.2 conflict UG-8 | Met |
| `OBL-CTRL-05` `S-SEMANTIC` obligations | §3.8 (World radios live where the ceiling permits; reason as a fact about the client, no error styling); §1.1 canvas column | Met |
| `OBL-CTRL-06` forced colors | §3.12; `INS-09`; `INS-14` item 15 (capture bound to the control in `S-SEMANTIC`) | Met |
| `OBL-ADV-01` visible advisement | §3.5 (all four points; four user classes; 1.4.13 and `Escape` reasoning); `INS-08`; `INS-11` | Met |
| `OBL-ANN-01` polite, region named, present-and-empty first | §3.6; §3.11 | Met |
| `OBL-BND-01` to `OBL-BND-04` boundary crossing | §3.11 five-step sequence in the accepted order; focus visibly indicated on arrival with the destination host's token; `INS-08` Announcement; `INS-14` item 15 | Met |
| `OBL-STATE-01` where the states live | §3.10 preamble; `INS-07` | **Not met as written** (DSA-01) |
| `OBL-STATE-02` to `OBL-STATE-05` | §3.10 rows: retained focus and preserved properties; write failure non-blocking with the consequence stated; read failure told in the destination shell; ceiling refusal with the prior stream still reported | Met (read-failure home, DSA-01) |
| `OBL-TRACE-03` two focus rules | §3.6 and §3.11 both carried; `FR-3D-013` as amended at D-045 carries both | Met |
| `NFR-A11Y-002` per-stream measurement | §1.3; `INS-10` | Met |
| `NFR-A11Y-004` names, advisement, 400% zoom, gated copy | §3.4, §3.5, §3.12 | Met |
| `NFR-A11Y-005` 3D focus indicator | §4.2 scene tokens: width 3 px, floor 3:1, persistence; measurement method gated (UG-1) | Met |

### B.2 Vocabulary and claims (Q4)

I ran three case-insensitive scans over the amendment (patterns and every hit at
V-06).

- Peer vocabulary: zero occurrences of fallback, degraded, lesser, lower,
  minimal, basic, lite or optional. Twelve lines contain "reduced": three quote
  the accepted style guide §8.2 table verbatim ("Reduced shadows, medium
  textures"; "reduced model detail"), and nine name the reduced-motion mode
  (`prefers-reduced-motion`, `MODE-REDUCED-MOTION`, "reduced motion"). No stream
  is described by the amendment in any of the prohibited words.
- Ladder vocabulary: four lines, each a prohibition or negation (lines 70 to
  71, 272, 494).
- Conformance: seven lines. Three are the disclaimers (5, 75, 1077); one names
  the validator's scan (34); one says the anatomy "satisfies the freeze §3.2
  composite order", an ordering statement and not a WCAG claim (346); two
  quote the withdrawn D-043 satisfied-by-construction claim as withdrawn (413,
  1004). The validator's own conformance pattern returns zero matches on the
  amendment. No conformance claim.

### B.3 Fidelity of the accessibility substance (Q3)

Every accessibility claim I spot-checked traces to its source with the
exceptions recorded as findings; the list is at V-05. In particular, the quoted
human consequence at obligations lines 470 to 473, the five-step tree ordering
of `OBL-BND-04`, the four user classes of `OBL-ADV-01`, the `OBL-CTRL-02`
announcement script structure, the `DS-S-*` required-mode sets, and the
`DS-S-SEMANTIC` `exception_rule` wording are all reproduced accurately.

### B.4 Part B findings

DSA-01 (MEDIUM) and DSA-07 (LOW). Under the package convention a MEDIUM finding
blocks acceptance. **FAIL**, curable in one revision.

---

## Findings

| ID | Severity | Location (amendment) | Evidence | Required change |
|---|---|---|---|---|
| **DSA-01** | **MEDIUM** | §3.10 preamble, lines 522 to 525; block `INS-07`, lines 842 to 844 (text destined for frozen §3.3) | The amendment states that `STATE-STREAM-CHANGED`, `STATE-PREFERENCE-WRITE-FAILED`, `STATE-PREFERENCE-READ-FAILED` and `STATE-STREAM-CEILING-REFUSED` are the states "that `responsive-state-mode-matrix.csv` already carries on `SP-NAVIGATION`, `SP-WORLD` and `SP-FIRST-VISIT`", and `INS-07` would write into the frozen file that the four are "carried by `SP-NAVIGATION`, `SP-WORLD` and `SP-FIRST-VISIT`". The matrix, read by me with `Import-Csv`: `SP-NAVIGATION` carries all four; `SP-WORLD` carries three and **not** `STATE-PREFERENCE-READ-FAILED`; `SP-FIRST-VISIT` carries three and **not** `STATE-STREAM-CEILING-REFUSED`; `SP-RETURN-VISIT` carries `STATE-STREAM-CHANGED`, `STATE-PREFERENCE-WRITE-FAILED` and `STATE-PREFERENCE-READ-FAILED` and is not named. `OBL-STATE-01` (obligations lines 771 to 776) specifies exactly that distribution. The omission is not cosmetic: the read-failure state is the "on return" case (`OBL-STATE-04`, lines 833 to 842), so the component contract points an implementer at `SP-WORLD`, where the matrix requires no such state, and away from `SP-RETURN-VISIT`, where it does. Applied as written, `INS-07` would make the hash-pinned design-system file contradict the hash-pinned matrix in two cells. | In both places replace the flat list with the per-state distribution: `SP-NAVIGATION` (all four); `SP-WORLD` (`STATE-STREAM-CHANGED`, `STATE-PREFERENCE-WRITE-FAILED`, `STATE-STREAM-CEILING-REFUSED`); `SP-FIRST-VISIT` and `SP-RETURN-VISIT` (`STATE-STREAM-CHANGED`, `STATE-PREFERENCE-WRITE-FAILED`, `STATE-PREFERENCE-READ-FAILED`), and cite the matrix as the authority for the list. Add `SP-RETURN-VISIT` to the `STATE-PREFERENCE-READ-FAILED` row of the §3.10 table as the "on return" home. |
| DSA-02 | LOW | §0 summary table row 2, line 90 | "five properties each (§2)". §2.1 (lines 219 to 220), the §2.2 table (lines 244 to 249) and the `INS-04` stream row (line 813) define six: `id`, `profile`, `evidence-token`, `label`, `presentation`, `canvas`. | Change "five" to "six". |
| DSA-03 | LOW | §4.2 table, `semantic.focus.scene.motion` row, line 695 | The rule clause "never animated across the viewport" is sourced to style guide §4.1 and §7.3. Neither contains it (§4.1 line 93 says "Present whether or not the pointer is used, and unaffected by `prefers-reduced-motion`"; §7.3 lines 215 to 228 enumerate suppressed motion). The clause appears verbatim in `packages/design-system/tokens.json` line 80 and `README.md` line 73, the [PROPOSED] input. Every other borrowing from that input in the same table is marked [PROPOSED]; this one is not. | Delete the clause, or move it to the source column marked "[PROPOSED] `tokens.json`, never authority", matching the `semantic.focus.ring` row. |
| DSA-04 | LOW | §4.3 lines 710 to 716; `INS-04` third row, line 814 ("resolves to `semantic.focus.*` in `S-SEMANTIC`"); `INS-09` fourth bullet, lines 927 to 930 | The rule that the scene ring resolves to the 2D ring in `S-SEMANTIC` is the author's own. No source states it; the sources say only that `S-SEMANTIC` has no canvas and no HUD (`OBL-CTRL-05`; style guide §8.2.4). It is safe, reversible and unambiguous, which is the constitution's test for a recorded assumption, but §7 does not record it, so a reader cannot tell it from a sourced rule. | Add assumption A-4 to §7 stating the resolution rule, its reasoning and the one-line reversal; cite A-4 from §4.3 and from the `INS-04` row. |
| DSA-05 | LOW | §3.2 lines 350 to 356 (A-2 recorded); `INS-08` block lines 860 to 865 | A-2 records the advisement placement between the legend and the radios as an assumption. `INS-08` then writes the anatomy for the frozen file as the fixed order "`fieldset`; `legend` ...; persistent visible advisement; four native radio inputs ...; separate, always-present Apply" with no marker. The sources fix only that the advisement precedes Apply in DOM and visual order (`OBL-ADV-01` point 1; `NFR-A11Y-004`; `PRIM-001` `required_anatomy`). Applied as written, the frozen file would bind a placement the accepted records leave open. | In `INS-08` write "persistent visible advisement, before Apply in DOM reading and visual order (placement relative to the radios: recorded assumption A-2)", or restate the anatomy so the frozen text carries only the source-backed constraint. |
| DSA-06 | LOW | §5 table, `INS-06` row, line 757 | The plan preamble (lines 738 to 745) promises for every insertion "the anchor (the exact existing text the insertion follows or replaces)". `INS-06` gives "The two rows as they stand in §3.1". The rows are identifiable (`\| Shell and navigation \|` and `\| Overlay and immersive \|` each occur once, V-07), so the insertion is applicable, but it is the only row of fourteen that asks the applying slice to find its own anchor. | Quote the two row-start anchors literally, as the other rows do. |
| DSA-07 | LOW | §3.2 lines 354 to 356; §7 A-1 lines 1061 to 1063; §2.3 lines 272 to 274 | A-1 fixes the visible radio order as `S-HIGH`, `S-MEDIUM`, `S-LOW`, `S-SEMANTIC`. That is the accepted §8.2 table order, but it is also a richness order, and §2.3 forbids a later export from sorting the tokens "by richness". The radio order is the most public peer-framing surface the control has and is inseparable from the gated label copy (UG-3). | Keep A-1 but state that the order is inherited from the accepted table and not derived from richness, and list radio order under UG-3 so the founder decides it together with the four labels. |
| DSA-08 | LOW | §2.3 last bullet, lines 283 to 284 | "Exact session, challenge, transition and provider durations remain [GATED] (freeze §2.1 runtime policy row)". The freeze row (line 102) gates session, challenge and provider durations only; transition durations are accepted ranges in freeze §2.2 (`motion.stateTransition` 120 to 200 ms; `motion.contextShift` 240 to 400 ms). The bullet's point, that a stream token carries no timing, stands. | Delete "transition", or cite §2.2 for the accepted ranges. |
| DSA-09 | LOW | §5, lines 767 to 768 | The search hint for reviewer-test hit (a) is `search "per stream"` at `INS-10`. The `INS-10` text (lines 936 to 944) reads "per rendered state and per delivery stream" and "per-stream obligation"; the literal string "per stream" does not occur in it. After application a literal search would hit `INS-08` (line 903, "measured per stream") and not the contrast rule the hint points at. | Make `INS-10` contain the words "per stream" (for example "per rendered state and per stream") or change the hint to `search "per delivery stream"`. |

---

## Verified

**V-01 Validator.** `pwsh -NoProfile -File docs/phase-1-ui-reference-design/validation/validate-ui-reference-design.ps1`
from the repository root, twice: before this record existed and after writing
it. Both: `RESULT=PASS PASS_COUNT=208 FAIL_COUNT=0`, aggregate
`8DF23FF106A78839581D774EE9DF842D434591ACB781A7E89DA5E2414E32635D`. `git status
--short` was empty before the first run and showed only this record after the
second; the validator restored nothing because it changed nothing. The
validator's scans that touch prose (`semantic-stream-peer-framing`,
`unsupported-conformance-claim-absence`, `wcag-no-current-conformance-disclaimer`)
are scoped to the freeze files; the only assertion that reads this record or the
amendment is `local-markdown-references`, which is why this record contains no
Markdown links.

**V-02 Subject revision.** `git log -1 --format=%H -- <amendment>` =
`2c469b61d1c7457ab94be133ea15d6a9272bdca5`; `sha256sum` =
`8448e86545ef64d638090db1ee6be012ec9918229e2a4213532996c7777cad6c`; the commit
adds exactly one file, 1081 lines. Working tree clean at the start of review.

**V-03 Q1, OBL-GRAM-03 reviewer test.** Case-insensitive counts in the
amendment: "per stream" 15 lines; "Delivery stream control" 7 lines;
"focus-scene" or "focus.scene" 26 lines. Each hit substantive as set out in A.1.
Result: three hits. Defect in the hint only (DSA-09).

**V-04 Q2, exit evidence.** All four additions present (A.2). Result: present.

**V-05 Q3, fidelity spot-checks.** Thirty specific claims checked against their
sources; the ones that failed are DSA-01, DSA-02, DSA-03, DSA-08.

1. §1.1 and §2.2 `presentation` text equals the style guide §8.2 table rows
   (lines 263 to 266) verbatim. Pass.
2. `EC-08`: `<STREAM>` between `<MODE>` and `V<NN>`, mandatory, no omissible or
   aggregate form, one stream per public frame (`evidence-capture-plan.csv` row
   `EC-08`; evidence model §0 row 5). Pass.
3. `PRIM-001` `required_anatomy` contains the five control items the amendment
   quotes and `page status region` (first data row). Pass.
4. `PRIM-001` `required_variants` `stream_high;stream_medium;stream_low;stream_semantic`;
   `transactional_or_content_states` `stream-preference-write-failed;stream-in-force;stream-pending`;
   `state_redundancy` "visible text plus shape icon border pattern or
   position;never color only"; category `shell_navigation`. Pass.
5. `PRIM-042`, `PRIM-043`, `PRIM-044` names and `stream_presence`
   `S-HIGH;S-LOW;S-MEDIUM`; `PRIM-043` "does not obscure focus or content" and
   "no canvas-only control"; `PRIM-044` variant `context_loss`. Pass.
6. `OBL-CTRL-01` role, two-step activation and prohibitions (obligations lines
   303 to 331) against §3.3. Pass.
7. `OBL-CTRL-02` (lines 368 to 384) against §3.4 and §3.8; the prohibited label
   words are cited by reference (`NFR-A11Y-004`), not reproduced. Pass.
8. `OBL-CTRL-03` (lines 405 to 416) against §3.1 and §3.12. Pass.
9. `OBL-CTRL-04` (lines 442 to 473) against §3.7 and §4.1; the human
   consequence quoted from lines 470 to 473 is accurate; the sampling gate is
   carried as UG-1. Pass.
10. `OBL-CTRL-05` and `OBL-CTRL-06` against §3.8 and §3.12. Pass.
11. `OBL-ADV-01` four points, four user classes, and its frame (`VP-DESKTOP`,
    `S-SEMANTIC`, `focus-visible`) against §3.5 and §4.4. Pass.
12. `OBL-ANN-01` against §3.6 and §3.11. Pass.
13. `OBL-BND-04` five ordered steps (lines 740 to 745) against §3.11 steps 1 to
    5. Identical order. Pass.
14. `OBL-STATE-01` table (lines 771 to 776) against §3.10 and `INS-07`. **Fail,
    DSA-01.** `OBL-STATE-02` to `-05` meanings against the §3.10 rows. Pass.
15. `OBL-TRACE-03` against §3.6 and §3.11; SRS `FR-3D-013` (line 151) carries
    both cases. Pass.
16. `OBL-INV-03` reasoning and the §6.2 panel classes (`bg-gray-900/95
    backdrop-blur`, style guide line 187) against §1.3. Pass.
17. `OBL-GRAM-01` point 2 ("quality" and the other words barred from token
    vocabulary) and point 4 (`MODE-SEMANTIC-SHELL` versus `S-SEMANTIC`) against
    §2.3 and §1.2. Pass.
18. Evidence model N-03 (relocation to `TPL-WORLD-SHELL` and `TPL-WORLD-HUD`,
    B07), N-04 (baseline plus stream-critical states), N-05, N-06 (§7.3 lines
    719 to 745), §8.1 items 1 to 4, and gates G-1 to G-7 (lines 905 to 915)
    against §1.3, §3.3, §3.5, §4.4 and `INS-14` item 15. Pass.
19. Style guide §4.1 focus row (line 93) quoted exactly; "The focus row is
    normative, not planned: a stream that cannot show it cannot ship" (lines
    102 to 103); hex values `#00BFFF`, `#FFFFFF`, `#F44A25` in §3.1 and §4.1
    and `#666666` in §4.1; none present in `semantic-tokens.json` (grep, no
    match). Pass.
20. Style guide §7.2 `Escape` "Close panel / go back" (line 210); §7.3
    reduced-motion enumeration; §8.2 "Every route reachable in `S-HIGH` is
    reachable in `S-SEMANTIC` by an equivalent named action" (line 268); §8.2.2
    steps 1, 5, 6 and consequences 2 and 3 (lines 307 to 356); §8.2.3 U-03;
    §8.2.4 control model, advisement and crossing paragraphs; §8.2.5 (lines 452
    to 453); §8.2.6. Pass.
21. SRS `FR-3D-010` P0, `FR-3D-011`, `FR-3D-012`, `FR-3D-013` (both cases),
    `FR-3D-014`, `FR-3D-015`, `FR-3D-016` (lines 148 to 154) and `NFR-A11Y-001`
    to `-007` (lines 261 to 267) as cited; `NFR-A11Y-006` is P1. Pass.
22. D-045 resolutions 1, 3, 5, 6, 7 (lines 85 to 169) and D-046 (lines 196 to
    228: author independence, review against `OBL-GRAM-03`, export at `be48d55`
    as input not authority, freeze hash intact, B01 held, no Figma call, three
    cycles). Pass.
23. D-039 index row "Option A" (line 53); D-043 index row "withdraw the WCAG
    2.2 3.2.2 satisfied-by-construction claim and require advance advisement
    instead" (line 57), which is what §3.5 attributes to it. Pass.
24. Identity source: `color.signal.cyan.onDark` (`#00D4FF`) on `color.ink`
    (`#0B0F14`) at 10.86:1, use "text, focus, icons, graphics"
    (`semantic-tokens.json` line 33 with the freeze §2.2 mapping); no `stream`
    definition and no other `focus` definition in the file. Pass.
25. [PROPOSED] input values quoted in §4.2: `hd-focus-ring` light and dark
    aliases with 5.68:1, 3.22:1 and 10.86:1 (`tokens.json` line 80);
    `hd-focus-ring-width` 3px (line 184); `hd-focus-offset` 4px (line 185);
    `space.scale[0]` 4 px (freeze §2.2). All marked [PROPOSED] except the
    clause raised as DSA-03. Pass with DSA-03.
26. Frozen file §2.1 layer rules; §2.3 `semantic.focus.{ring,offset}` row; §2.4
    naming rules; §3.1 taxonomy names; §3.2 composite order; §3.3 five
    pseudo-states and "Pending never looks or reads as success"; §4 "24 by 24
    CSS px"; §5 contrast bullet; §7 prototype exclusion; §8 items 2, 4, 7 and
    14; expected hash `0E9FC68C...B763` (validator line 827). Pass. The §2.1
    runtime-policy quotation fails on one word (DSA-08).
27. Matrix `DS-S-*` required modes per stream (HIGH: reduced motion, keyboard;
    MEDIUM: keyboard; LOW: low power, keyboard; SEMANTIC: forced colors, print,
    keyboard) from `critical_distinct_frame_values`; `DS-S-SEMANTIC`
    `exception_rule` wording; `SP-NAVIGATION` carries all four stream states.
    Pass. `SP-WORLD`, `SP-FIRST-VISIT`, `SP-RETURN-VISIT`: **DSA-01**.
28. B01 `future_not_authorized` in `design-batch-plan.csv` (`status`) and
    `batch-production-plan.csv` (`ma_025_disposition`); B01
    `required_visual_evidence` consistent with `INS-14` item 15. Pass.
29. `COV-ACT-09` (`SP-NAVIGATION`; `UXTEST-046` linked; ceiling "never silently
    substituted"); `ACT-09` and `ACT-11` rows; `UXTEST-046` (line 152);
    `TR-REQ-103`, `TR-REQ-111`, `TR-TEST-046`; `UX_ARCHITECTURE.md` J-02 step 1
    "Visitor explicitly selects the World" (lines 173 to 174). Pass.
30. Internal consistency of the amendment's own counts: stream properties
    stated as five, defined as six. **Fail, DSA-02.** Scene-token property
    count (six) consistent between §0 and §4.2. Pass.

**V-06 Q4, regex scans of the amendment** (`grep -n -i -E`).

- `\b(fallback|degraded|reduced|lesser|lower|minimal|basic|lite|optional)\b`:
  12 lines, all the word "reduced": 107, 108, 248 (style guide §8.2 table
  quoted verbatim); 132, 275, 609, 611, 654, 695, 908, 1022, 1032 (the
  reduced-motion mode). Zero hits for the other eight words.
- `\b(ladder|downgrade|upgrade|promot(e|ed|ion)|demot(e|ed|ion)|quality|rung|inferior|superior|richer|poorer|contingency)\b`:
  lines 70, 71, 272, 494; each a prohibition or negation.
- `conform|complian|meets? WCAG|WCAG[- ]compliant|satisf|\bpasses\b|is accessible|fully accessible|AA[- ]compliant|accessible to all`:
  lines 5, 34, 75, 346, 413, 1004, 1077, classified in B.2. The validator's
  own pattern `(?:currently\s+)?(?:meets|achieves|certifies|is conformant with|is compliant with)\s+WCAG\s*2\.2`
  returns zero matches on the amendment and on this record. The validator's
  nine peer-framing alternatives return zero matches on the amendment and on
  this record.
- Counts: `[GATED]` 16 occurrences; `[UNRESOLVED GATE]` used once as the §7
  column heading over twelve gates.

**V-07 Q5, anchor counts in the frozen file** (whitespace-normalised literal
match; frozen SHA-256 at the count `0E9FC68C98AC25C4F7DFBC62B10DBA1FCB197F5C82AD2FF39DCD0C16D9CFB763`).

| Insertion | Anchor (as given in the amendment) | Count | Frozen line(s) | Unambiguous |
|---|---|---|---|---|
| `INS-01` | `**Amended:** 2026-09-06 under D-042 and D-043` | 1 | 4 | Yes |
| `INS-02` | `it must not hide the gap in a one-off screen component or invented product fact.` | 1 | 70 | Yes |
| `INS-03` | `Opacity, glow, blur, or material appearance cannot repair insufficient contrast.` | 1 | 151 to 152 | Yes |
| `INS-04` (row replaced) | `\| \`semantic.focus.{ring,offset}\` \| \`--hd-focus-*\` \| Thickness, offset, clipping prevention, and surface pairings \|` | 1 | 165 | Yes |
| `INS-04` (insert before) | `\| \`component.*\` \|` | 1 | 172 | Yes; six untouched rows lie between 165 and 172 |
| `INS-05` | `- Dark and light are controlled surface pairings. Forced colors, grayscale,` | 1 | 189 | Yes; last bullet of §2.4 |
| `INS-06` (row 1) | `\| Shell and navigation \|` (described, not quoted: DSA-06) | 1 | 206 | Yes once quoted |
| `INS-06` (row 2) | `\| Overlay and immersive \|` (described, not quoted: DSA-06) | 1 | 211 | Yes once quoted |
| `INS-07` | `dialogs, error summaries, and deliberate navigation may move focus under their own contract.` | 1 | 252 to 253 | Yes; end of the transactional-states paragraph |
| `INS-08` | `## 4. Responsive, input, and mode obligations` | 1 | 255 | Yes; new §3.4 goes between 253 and 255 |
| `INS-09` | `evidence status, error/success distinction, and data-series identity without depending on color or shadow.` | 1 | 278 to 279 | Yes; last bullet of §4 |
| `INS-10` | the full contrast bullet | 1 | 309 to 311 | Yes |
| `INS-11` | `- No accessible label, role, state, route title, evidence class, or recovery` | 1 | 312 | Yes; last bullet of §5 |
| `INS-12` | `UXTEST-001 through UXTEST-045.` | 1 | 375 | Yes |
| `INS-13` | `7. Contrast calculations for every rendered state and adjacent surface` | 1 | 382 | Yes; item ends at 384 |
| `INS-14` | `14. Controlled-clock evidence for every user time limit` | 1 | 403 | Yes; item ends at 407, closing paragraph at 409 |

Block sizes match their operations: `INS-09` four bullets, `INS-11` three
bullets, `INS-13` two sentences, `INS-14` items 15 to 17. Every `[GATED]`
placeholder in the blocks is inside `INS-01` only.

**V-08 Q6, naming and layers.** As A.3. Result: pass, no finding.

**V-09 Q7, overreach.** As A.5. Result: no decision changed, B01 held, Figma
rules untouched, no founder question resolved; two unrecorded assumptions
(DSA-04, DSA-05); no listed gate answered by the sources.

**V-10 Q8, format.** As A.6. Result: pass.

**V-11 Checked and found sound, not raised as findings.**

- The amendment omits "non-WebGL" when it lists the frozen §2.4 verification
  contexts (line 132 to 133). The frozen §2.4 and §4 keep "non-WebGL" as a
  mode-axis context; `INS-05` adds the stream axis beside it rather than
  replacing it. Both readings survive application; UG-11 already flags the
  pre-D-039 wording of §1.1, and the applying slice should read UG-11 as
  covering §2.4 and §4 too.
- `canvas` property values `on-explicit-entry` and `none` (§2.2) are names the
  amendment defines, not measured values; defining names is the commission.
- The §1.3 consequence 4 frame-economy claim holds: the only frames §4.4 adds
  to the ledger are the per-stream `focus-visible` frames that `OBL-CTRL-04`
  already requires and the relocated B07 frames that N-03 already requires.
- `INS-12` corrects a stale count against the accepted test set (A.4).
- The amendment's statement that the freeze file wraps at about 80 columns and
  that anchors must be matched whitespace-normalised is accurate and necessary:
  `INS-03`, `INS-07`, `INS-09` and `INS-10` span line breaks.

---

## Recommendation to the founder

**Accept after the listed revisions.** Revise DSA-01 (required) and DSA-02 to
DSA-09 (each resolved or explicitly declined), then present the revised text
for a second review record against the same sources; this consumes revision
cycle 1 of the three the constitution allows for UI work, and the freeze file
stays untouched until the acceptance decision that D-046 names as separate.

## Standing note

This record is an input to a founder decision, not a decision. It changes no
file other than itself, it did not edit the amendment, the frozen files or any
validator, it made no external call, and it claims no conformance of any kind.
