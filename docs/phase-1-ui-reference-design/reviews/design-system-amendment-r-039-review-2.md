# Independent Review — Design-System Amendment R-039 (review 2)

**Review date:** 2026-09-24
**Commissioning decision:** D-046 (2026-09-24), executing D-045 gate G-6; risk
R-039. This is the second review under that contract, of the revision the
author produced in response to review 1 (revision cycle 1 of three).
**Subject under review:** `docs/phase-1-ui-reference-design/DESIGN_SYSTEM_AMENDMENT_R-039.md`
[PROPOSED SPECIFICATION], revision 2, 1180 lines, at commit
`cf455db9d0fc5fc285ea2153d3d924f1d7afa332` (2026-09-24, "docs: R-039 amendment
revision 2 resolving review-1 findings DSA-01 to DSA-09"), file SHA-256
`61B924951FF955FAA16AE067BA9BAF2E0A0F7987F91DF5F907F42CDA4FE0E9EA`. Both values
were taken by me from `git log -1 --format=%H` on the file and `sha256sum`; they
equal the values the coordinator named. The commit changes that one file only
(151 insertions, 52 deletions). This record reviews that text and nothing else.
**Prior record:** `reviews/design-system-amendment-r-039-review-1.md`, committed
unchanged at `740864b6a8411f8ba2663869049aba2cf9a244f2` (one file, 480 lines);
its subject was revision 1 at `2c469b6`.
**Reviewer:** the same independent review agent as review 1. I did not author
the amendment or its revision, I am not the D-045 producer, I did not author
the D-044 specifications, I wrote no validator, and I read no agent transcript
and no other agent's working files. The author's revision claims were read only
in the amendment's own closing section, "Revision history" (lines 1157 to
1180), and each was checked against the text at the line it cites and against
the sources. Constitution 2.0.0 principle VII.
**Gates covered:** Part A, design-system review; Part B,
accessibility-obligations review. One record, two verdicts.
**Authority I review against, and may not overrule:** as review 1: `DECISIONS.md`
D-045 and D-046; `RISKS.md` R-039; `TASKS.md` R-039 row;
`accessibility/DELIVERY_STREAM_ACCESSIBILITY_OBLIGATIONS.md`;
`DELIVERY_STREAM_EVIDENCE_MODEL.md`; the frozen `DESIGN_SYSTEM_IMPLICATIONS.md`
and `component-primitives.csv`; `responsive-state-mode-matrix.csv` (all 36 rows
read by me with `Import-Csv`, SHA-256
`D041CB12A6A2A9EF594639B5AC7D54B546AAB50432C0B7C06677F567EC2B1B10`);
`docs/active/3D_Mega_Menu_Style_Guide_v2.md`; `docs/active/Hengshi_Design_SRS_v3.md`;
`.specify/memory/constitution.md`. `packages/design-system/tokens.json` and
`README.md` remain [PROPOSED] input only.
**Conformance target reviewed against:** WCAG 2.2 Level AA for every applicable
full page and every complete process, holding independently within each of the
four peer delivery streams. The amendment claims no conformance, none is claimed
here, and nothing is built.
**Deterministic validator state at review:** `RESULT=PASS PASS_COUNT=208
FAIL_COUNT=0`, `FREEZE_AGGREGATE_SHA256=8DF23FF106A78839581D774EE9DF842D434591ACB781A7E89DA5E2414E32635D`,
`design-system-freeze-hash` PASS at
`0E9FC68C98AC25C4F7DFBC62B10DBA1FCB197F5C82AD2FF39DCD0C16D9CFB763`,
`component-primitives-freeze-hash` PASS at
`EF0DE11B23A6C6A9C8C721D55F528237A72153315B633E6198AF0B50ADED9C78`. Run by me
from the repository root before this record existed and again after writing
it; identical numbers; no tracked file modified by either run. The frozen file
is unchanged since review 1. A passing validator is a determinism check; it
reads the amendment only for local Markdown links.

**Severity scale.** HIGH: blocking. MEDIUM: significant; blocks founder
acceptance under the package convention. LOW: minor; does not block; each is
resolved in the applying slice under UG-9 or declined by the founder at
acceptance.

**Verdicts.** **Part A: PASS.** **Part B: PASS.** No MEDIUM or HIGH finding.
Two LOW findings (DSB-01, DSB-02), both introduced by the revision, neither
touching the substance of the three OBL-GRAM-03 hits or the R-039 exit
evidence. **Recommendation: accept as is** (revision 2 at `cf455db`), carrying
DSB-01 and DSB-02 to the applying slice under UG-9; a further author round is
not required by this record, and if the founder nonetheless requires one it
consumes revision cycle 2 of the three the constitution allows for UI work.

---

## Part A — Design-system review — verdict: PASS

### A.1 Disposition of the review-1 findings in the design-system scope

Each disposition was checked at the line the Revision history cites and
against the source that governs it (full table at V-03).

- **DSA-02** (five versus six properties). Line 94 now reads "six properties
  each (§2)"; §2.1, the §2.2 table and the `INS-04` stream row still define six.
  Present; resolves.
- **DSA-03** (unsourced motion clause). Line 730: the rule for
  `semantic.focus.scene.motion` is now "static and persistent; present whether
  or not the pointer is used; unaffected by `prefers-reduced-motion`", which is
  style guide §4.1 line 93; the clause "never animated across the viewport" is
  moved to the source column and marked as occurring only in the [PROPOSED]
  `tokens.json` and `README.md` input, "not part of the rule". Present;
  resolves.
- **DSA-04** (unrecorded resolution rule). A-4 is recorded at lines 1135 to
  1141 with the rule, its reasoning (`OBL-CTRL-05`; style guide §8.2.4), the
  statement that no source states it, and a one-line reversal; §4.3 (lines 746
  to 754) cites it; the `INS-04` scene row (line 853) and the `INS-09` fourth
  bullet (lines 985 to 989) cite it. Present; resolves.
- **DSA-05** (A-2 baked into `INS-08`). The `INS-08` anatomy bullet (lines 916
  to 923) is now labelled "Anatomy:" with no order claim and carries only the
  two source-fixed constraints (inside the fieldset; before Apply in DOM
  reading order and visual order), citing A-2 for placement relative to the
  radios. §3.2 lists the anatomy in the order `PRIM-001` records it (I checked
  the first data row: fieldset, legend, four radios, Apply, advisement), and
  its composite-order paragraph (lines 354 to 372) now states that "exactly
  two" order constraints are source-fixed, which is correct against
  `OBL-ADV-01` point 1, `NFR-A11Y-004` and `PRIM-001`, and puts the
  "advisement as context" reading inside A-2 (lines 1125 to 1131). Present;
  resolves. The reordering left the §3.2 heading stale (DSB-01).
- **DSA-06** (`INS-06` anchor described, not quoted). Line 796 points to
  "anchor block `INS-06`"; lines 868 to 873 quote the two rows. I compared
  them to the frozen file line by line: each block row is byte-identical to
  frozen line 206 and line 211 respectively, and each occurs exactly once in
  the whitespace-normalised frozen file. Present; resolves.
- **DSA-07** (radio order). UG-3 (line 1106) now includes "the visible order
  of the four radios, decided together with the labels", states the provenance
  (the style guide §8.2 table, inherited and "not derived from richness") and
  names A-1 as provisional; A-1 (lines 1120 to 1124) is rewritten with
  provenance and a reversal; §3.2 (lines 366 to 372) states that no source
  fixes the order. Present; resolves.
- **DSA-08** ("transition" in the gated list). Lines 287 to 291: session,
  challenge and provider durations remain gated; transition durations are
  cited as the accepted freeze §2.2 ranges. I checked the three ranges against
  frozen lines 136 to 138: `motion.signalReveal` 180 to 320 ms,
  `motion.stateTransition` 120 to 200 ms, `motion.contextShift` 240 to 400 ms,
  each with a reduced-motion branch. Present; resolves.
- **DSA-09** (hint string). `INS-10` (line 995) now reads "per rendered state
  and per stream"; the hint at line 807 (`search "per stream"`) matches the
  inserted text literally. Present; resolves.

### A.2 OBL-GRAM-03 three-hit test on the revised text

Case-insensitive counts: "per stream" 18 lines (15 in revision 1; the three
new ones are the `INS-10` fix, the §3.2 rewrite and the Revision history);
"Delivery stream control" 7 lines; "focus-scene" or "focus.scene" 28 lines.
The substantive content behind each hit is unchanged by the revision: §1.3 and
`INS-10` and `INS-13` for (a); §3 and `INS-06` and `INS-08` for (b); §4.2 and
`INS-04` for (c). After application, the literal hint strings now match
`INS-10` ("per stream"), `INS-06` and `INS-08` ("Delivery stream control") and
`INS-04` ("focus-scene"). Three hits, each substantive.

### A.3 R-039 exit-evidence check

The four additions are present and unchanged in substance: the delivery-stream
axis (§1; `INS-02`, `INS-05`, `INS-09`); the delivery stream control component
(§3; `INS-06`, `INS-08`); the four stream tokens
`semantic.stream.{high,medium,low,semantic}` as `--hd-stream-*` (§2;
`INS-04`); the 3D focus-ring family `semantic.focus.scene.*` (§4; `INS-04`).
The exit evidence also requires a clean independent review record; this record
carries no MEDIUM-or-higher finding.

### A.4 Mechanical applicability, re-run

All sixteen anchors of `INS-01` to `INS-14` occur exactly once in the
whitespace-normalised frozen file, whose SHA-256 at the count equals the
validator's pinned value (table at V-05). The rewritten `INS-06` now quotes its
two anchors and the rewritten `INS-07` keeps its original anchor. Every
insertion is positionally unambiguous. I did not edit the frozen file.

### A.5 Regressions in the design-system scope

I read every hunk of `git diff 2c469b6 cf455db` on the file (327 diff lines;
hunk list at V-09). Two regressions, both LOW: DSB-01 (a heading left
contradicting the list beneath it) and DSB-02 (frozen-file text now citing an
unpinned document). No accepted decision is changed, B01 stays
`future_not_authorized` in both plan files, no Figma rule is altered, no new
number appears without a source (the only new numbers are the matrix row
count of 36, which the validator asserts; the counts 14 and 10, which I
recomputed; the three freeze §2.2 ranges; and frozen lines 206 and 211, which
I verified), and no new decision is taken silently: the revision moved one
decision (radio order) from an assumption to a founder gate and recorded one
(A-4) that was previously implicit.

### A.6 Format

Header unchanged in structure; the Date line records revision 2 and the cycle;
Inputs now list review 1 (read, not edited) and the `Import-Csv` read of the
matrix. The new closing section "Revision history" gives one row per finding
with the line changed; every cited line was found to contain the change
claimed. PASS.

---

## Part B — Accessibility-obligations review — verdict: PASS

### B.1 DSA-01, verified against the matrix row by row

I read all 36 rows of `responsive-state-mode-matrix.csv` with `Import-Csv` and
computed, for each of the four stream frame states, the set of profiles
carrying it in both `required_values` and `critical_distinct_frame_values`, in
`required_values` only, and in `critical_distinct_frame_values` only.

| Frame state | Profiles carrying it in both columns (computed) | Required-only | Critical-only | Author's §3.10 table and `INS-07` |
|---|---|---|---|---|
| `STATE-STREAM-CHANGED` | `SP-PUBLIC-DOCUMENT`, `SP-PUBLIC-COLLECTION`, `SP-PUBLIC-DETAIL`, `SP-EVIDENCE-COLLECTION`, `SP-EVIDENCE-DETAIL`, `SP-NAVIGATION`, `SP-FIRST-VISIT`, `SP-RETURN-VISIT`, `SP-WORLD`, `SP-AI`, `SP-HANDOFF-MEDIA`, `SP-BOOKING`, `SP-CONTACT`, `SP-SYSTEM-RECOVERY` (14) | none | `DS-S-HIGH`, `DS-S-MEDIUM`, `DS-S-LOW`, `DS-S-SEMANTIC` | Same fourteen, same four stream profiles. Match. |
| `STATE-PREFERENCE-WRITE-FAILED` | the same fourteen | none | the same four | Match. |
| `STATE-PREFERENCE-READ-FAILED` | `SP-NAVIGATION`, `SP-FIRST-VISIT`, `SP-RETURN-VISIT` (3) | none | the same four | Same three; "not `SP-WORLD`" correct. Match. |
| `STATE-STREAM-CEILING-REFUSED` | `SP-NAVIGATION`, `SP-WORLD` (2) | none | the same four | Same two; "not `SP-FIRST-VISIT`, not `SP-RETURN-VISIT`" correct. Match. |

Further checks: the five staff profiles `SP-AUTH`, `SP-STAFF-QUEUE`,
`SP-STAFF-WORK`, `SP-PUBLICATION` and `SP-AUDIT` carry none of the four in
either column (line 557 correct); no profile of any dimension carries any of
the four in `required_values` only, so the author's "both columns" criterion
omits no home; the §3.10 state rows (lines 563 to 569) carry the homes per
state, with `SP-RETURN-VISIT` named as the on-return home of
`STATE-PREFERENCE-READ-FAILED` (line 568), which is the `OBL-STATE-04` case;
the `OBL-STATE-01` minimum (obligations lines 771 to 776) is met and stated
(lines 544 to 548); the §6 matrix row (line 1085) counts "ten further public
state profiles", which is 14 minus 4. The rewritten `INS-07` (lines 886 to
901) restates exactly this distribution and names the matrix as governing the
list, so the text destined for the frozen file can no longer contradict the
frozen matrix. **DSA-01 is resolved.**

### B.2 Obligation-by-obligation result, re-checked

The review-1 table stands for every obligation whose text the revision did not
touch (`OBL-INV-03`, `OBL-GRAM-01`, `OBL-CTRL-01` to `-06`, `OBL-ADV-01`,
`OBL-ANN-01`, `OBL-BND-01` to `-04`, `OBL-STATE-02` to `-05`, `OBL-TRACE-03`,
`NFR-A11Y-002`, `-004`, `-005`): I confirmed from the diff that §1.3, §3.3 to
§3.9, §3.11 to §3.13, §4.1, §4.4 and blocks `INS-05`, `INS-11`, `INS-13` and
`INS-14` are unchanged. `OBL-STATE-01` moves from "not met as written" to met
(B.1). `OBL-GRAM-03` remains met (A.2). `OBL-ADV-01` point 1 is now quoted
precisely as the source of the two order constraints (§3.2). No obligation
regressed.

### B.3 Vocabulary and claims, re-run on the revised text

- `\b(fallback|degraded|reduced|lesser|lower|minimal|basic|lite|optional)\b`
  (case-insensitive): 13 lines, all the word "reduced": lines 111, 112, 252
  quote the accepted style guide §8.2 table verbatim; lines 136, 279, 291, 644,
  646, 689, 730, 966, 1081, 1091 and 1177 name the reduced-motion mode or the
  freeze §2.2 reduced-motion branches. Zero hits for the other eight words. No
  stream is described in any prohibited word.
- Ladder vocabulary: lines 74, 75, 276, 511, each a prohibition or negation.
- Conformance: lines 5, 79 and 1149 are the disclaimers; line 36 names the
  validator's scan; lines 430 and 1063 quote the withdrawn D-043 claim as
  withdrawn. The review-1 hit at former line 346 ("satisfies the freeze §3.2
  composite order") no longer exists; the rewritten sentence reads "is kept
  by". The validator's own conformance pattern and its nine peer-framing
  alternatives return zero matches on the revised amendment and on this
  record. No conformance claim.

### B.4 Part B findings

None at MEDIUM or above. DSB-01 and DSB-02 are design-system editorial
findings and are listed once, under Part A. **PASS.**

---

## Findings

| ID | Severity | Location (revision 2) | Evidence | Required change |
|---|---|---|---|---|
| DSB-01 | LOW | §3.2 heading, line 337; list, lines 339 to 346; constraint sentence, lines 354 to 356 | The heading still reads "Anatomy, in DOM reading order and visual order", but the list beneath it was reordered by the DSA-05 change into `PRIM-001` record order, which places Apply (item 4) before the advisement (item 5). The same section states, correctly, that the advisement precedes Apply in DOM reading and visual order. In revision 1 the list matched its heading; in revision 2 the heading contradicts the list. No frozen text is affected: the `INS-08` bullet is labelled "Anatomy:" and makes no order claim. | Retitle §3.2 (for example "Anatomy, in `PRIM-001` record order, and the order constraints") or present the list in the assumed DOM order with the A-2 marker on the advisement item. |
| DSB-02 | LOW | `INS-04` scene row, line 853; `INS-08` anatomy bullet, lines 916 to 923; `INS-09` fourth bullet, lines 985 to 989; `INS-01`, lines 814 to 819 | Three passages destined for the hash-pinned handoff artifact now cite "recorded assumption A-2 of `DESIGN_SYSTEM_AMENDMENT_R-039.md`" or "A-4 of `DESIGN_SYSTEM_AMENDMENT_R-039.md`". The amendment is neither hash-pinned nor in the validator's required-file list, and `INS-01` cites it by filename with a gated decision ID but no revision. After application, normative text in the frozen file would depend on the content and location of an unpinned document. New in revision 2. | Add to `INS-01` a gated placeholder for the accepted revision of the amendment (commit and SHA-256), so that the three assumption citations resolve to a pinned text; or carry the A-2 and A-4 sentences inline in the three blocks. Executable by the applying slice under UG-9 at acceptance; it needs no further author cycle. |

---

## Verified

**V-01 Validator.** `pwsh -NoProfile -File docs/phase-1-ui-reference-design/validation/validate-ui-reference-design.ps1`
from the repository root, before and after writing this record: both
`RESULT=PASS PASS_COUNT=208 FAIL_COUNT=0`, aggregate
`8DF23FF106A78839581D774EE9DF842D434591ACB781A7E89DA5E2414E32635D`. `git status
--short` was empty before the first run and showed only this record after the
second; nothing needed restoring. This record contains no Markdown links, so
`local-markdown-references` has nothing to resolve in it.

**V-02 Subject revision and scope.** `git log -1 --format=%H` on the file =
`cf455db9d0fc5fc285ea2153d3d924f1d7afa332`; `sha256sum` =
`61b924951ff955faa16ae067ba9baf2e0a0f7987f91df5f907f42cda4fe0e9ea`; 1180
lines; `git show --stat cf455db` lists one file. `git show --stat 740864b`
lists only review 1 (480 lines), and `git diff --stat 740864b` on that file is
empty: review 1 is committed unchanged. Working tree clean at the start of this
review. The frozen `DESIGN_SYSTEM_IMPLICATIONS.md` still hashes to the pinned
value.

**V-03 Dispositions DSA-01 to DSA-09.**

| Finding | Cited line(s) in revision 2 | Change present at the cited line | Resolves the finding |
|---|---|---|---|
| DSA-01 | 539 to 560, 557, 568, 886 to 901, 1085, 31 | Yes (all six places) | Yes (B.1) |
| DSA-02 | 94 | Yes | Yes |
| DSA-03 | 730 | Yes | Yes |
| DSA-04 | 1135, 746 to 754, 853, 988 | Yes (all four places) | Yes |
| DSA-05 | 916 to 923, 339, 354, 1125 | Yes (all four places) | Yes (DSB-01 is a side effect, not a residue) |
| DSA-06 | 796, 868 to 873 | Yes | Yes |
| DSA-07 | 1106, 1120, 366 to 372 | Yes (all three places) | Yes |
| DSA-08 | 287 to 291 | Yes | Yes |
| DSA-09 | 995, 807 | Yes | Yes |

No finding was declined; the Revision history says so and the text agrees.

**V-04 DSA-01 matrix computation.** As B.1: `Import-Csv` over 36 rows; per
state, the sets of profiles in both columns, in `required_values` only, and in
`critical_distinct_frame_values` only. Results: 14 / 14 / 3 / 2 profiles in
both columns for the four states in the order listed in B.1; zero
required-only profiles for every state; the four `DS-S-*` rows carry all four
states in `critical_distinct_frame_values` only; the five staff profiles carry
none; the viewport, mode, browser and time-limit profiles carry none.

**V-05 Anchor counts in the frozen file** (whitespace-normalised literal match;
frozen SHA-256 at the count `0E9FC68C98AC25C4F7DFBC62B10DBA1FCB197F5C82AD2FF39DCD0C16D9CFB763`).

| Insertion | Anchor | Count | Frozen line(s) |
|---|---|---|---|
| `INS-01` | `**Amended:** 2026-09-06 under D-042 and D-043` | 1 | 4 |
| `INS-02` | `it must not hide the gap in a one-off screen component or invented product fact.` | 1 | 70 |
| `INS-03` | `Opacity, glow, blur, or material appearance cannot repair insufficient contrast.` | 1 | 151 to 152 |
| `INS-04` (replace) | the `semantic.focus.{ring,offset}` row | 1 | 165 |
| `INS-04` (insert before) | `\| \`component.*\` \|` | 1 | 172 |
| `INS-05` | `- Dark and light are controlled surface pairings. Forced colors, grayscale,` | 1 | 189 |
| `INS-06` (row 1) | the full `Shell and navigation` row as quoted in anchor block `INS-06` | 1 | 206 |
| `INS-06` (row 2) | the full `Overlay and immersive` row as quoted in anchor block `INS-06` | 1 | 211 |
| `INS-07` | `dialogs, error summaries, and deliberate navigation may move focus under their own contract.` | 1 | 252 to 253 |
| `INS-08` | `## 4. Responsive, input, and mode obligations` | 1 | 255 |
| `INS-09` | `evidence status, error/success distinction, and data-series identity without depending on color or shadow.` | 1 | 278 to 279 |
| `INS-10` | the full contrast bullet | 1 | 309 to 311 |
| `INS-11` | `- No accessible label, role, state, route title, evidence class, or recovery` | 1 | 312 |
| `INS-12` | `UXTEST-001 through UXTEST-045.` | 1 | 375 |
| `INS-13` | `7. Contrast calculations for every rendered state and adjacent surface` | 1 | 382 |
| `INS-14` | `14. Controlled-clock evidence for every user time limit` | 1 | 403 |

The two `INS-06` block rows are byte-identical to frozen lines 206 and 211
(exact-line comparison), and each appears exactly once in the amendment.

**V-06 Three-hit test.** Counts and literal hint matches as A.2. Result: three
substantive hits.

**V-07 Exit evidence.** As A.3. Result: all four additions present.

**V-08 Scans.** Patterns and every hit as B.3. Result: vocabulary clean; no
conformance claim; the validator's patterns return zero matches on the
amendment and on this record.

**V-09 Regression review, hunk by hunk.** Date line (17); Inputs (31 to 33, 50
to 51); §0 row 2 (94); §2.3 timing bullet (287 to 291); §3.2 list and
paragraph (339 to 372); §3.10 preamble, distribution table, staff sentence and
state rows (539 to 569); §4.2 motion row (730); §4.3 A-4 sentence (746 to
754); `INS-06` table row (796) and anchor block (868 to 873); `INS-04` scene
row (853); `INS-07` block (886 to 901); `INS-08` anatomy bullet (916 to 923);
`INS-09` fourth bullet (985 to 989); `INS-10` (995); §6 matrix row (1085);
UG-3 (1106); UG-11 (1114); A-1, A-2, A-4 (1120 to 1141); Revision history
(1157 to 1180). Every hunk either executes a review-1 disposition or records
it. Regressions: DSB-01, DSB-02. Observations not raised as findings: the
rewritten `INS-07` restates a fourteen-profile list that is exact today and
names the matrix as governing it, so a later matrix change would need the
frozen text re-read, which is the ordinary consequence of the freeze; the
"advisement as context" reading of the freeze §3.2 composite order is an
interpretation and is now correctly placed inside A-2; UG-11 now covers the
frozen §2.4 and §4 mode-axis wording, adopting review-1 note V-11.

**V-10 Format.** As A.6. Result: pass.

---

## Recommendation to the founder

**Accept as is:** revision 2 at `cf455db` resolves every review-1 finding, its
DSA-01 distribution matches the matrix row for row, and it carries no
MEDIUM-or-higher finding; DSB-01 and DSB-02 are LOW and can be executed by the
applying slice under UG-9 at acceptance, so a further author round is not
required, and if one is nonetheless ordered it consumes revision cycle 2 of
the three the constitution allows for UI work.

## Standing note

This record is an input to a founder decision, not a decision. It changes no
file other than itself, it did not edit the amendment, the frozen files, review
1 or any validator, it made no external call, and it claims no conformance of
any kind.
