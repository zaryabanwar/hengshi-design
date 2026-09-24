# Independent Verification — Application of the R-039 Design-System Amendment to the Frozen Baseline

**Review date:** 2026-09-24
**Commissioning decision:** D-047 (2026-09-24), which accepted
`DESIGN_SYSTEM_AMENDMENT_R-039.md` revision 2 (commit `cf455db`, SHA-256
`61b924951ff955faa16ae067ba9baf2e0a0f7987f91df5f907f42cda4fe0e9ea`), authorized
the mechanical application of its fourteen insertions to the hash-pinned
`DESIGN_SYSTEM_IMPLICATIONS.md`, and requires independent verification before
R-039 closes. Risk R-039.
**Subject under review:** commit `c07e455a9458b0d3094cdb749a34cd6ee2031d7d`
(2026-09-24, "docs: apply the accepted R-039 amendment to
DESIGN_SYSTEM_IMPLICATIONS.md (D-047)"), parent
`31ebf4db512690591ed3ca556d6a04eaaf87d17e`. `HEAD` is that commit and the
working tree was clean at the start of this verification. The change set,
from `git diff 31ebf4d c07e455`, is three files: `DESIGN_SYSTEM_IMPLICATIONS.md`
(+178, -7 lines; 413 to 584 lines), `validation/validate-ui-reference-design.ps1`
(+3, -1) and `DESIGN_SYSTEM_AMENDMENT_R-039.md` (+2, -1). The amended frozen
file at `c07e455` has SHA-256
`1893D026E6B17E98C3267D80AE929760780639FEB499A49F999C9E64C9168B81` by the
validator's method (`Get-FileHash -Algorithm SHA256` on the raw bytes, uppercase
hex), identical for the git blob and for the working-tree file.
**Reviewer:** the independent review agent that wrote reviews 1 and 2. I did
not implement the application, I did not author the amendment, I am not the
D-045 producer, I wrote no validator, and I read no agent transcript and no
other agent's working files; the implementer's account was read only in the
amendment's Revision 3 row (line 1181) and in D-047. Constitution 2.0.0
principle VII: I verify, I did not implement.
**Authority I verify against, and may not overrule:** D-047 and D-046 in
`DECISIONS.md`; the accepted amendment at `cf455db` (its section 5 application
plan is the specification of this slice); `RISKS.md` R-039; the parent revision
of the frozen file at `31ebf4d` (identical to the `0E9FC68C...B763` revision
reviewed in reviews 1 and 2); reviews 1 and 2 for DSB-01 and DSB-02.
**Deterministic validator state at review** (all run by me from the
repository root; no tracked file modified by any run):

- design: `RESULT=PASS PASS_COUNT=208 FAIL_COUNT=0`; `design-system-freeze-hash`
  PASS at `1893D026E6B17E98C3267D80AE929760780639FEB499A49F999C9E64C9168B81`;
  `component-primitives-freeze-hash` PASS at
  `EF0DE11B23A6C6A9C8C721D55F528237A72153315B633E6198AF0B50ADED9C78`;
  `FREEZE_AGGREGATE_SHA256=0C59C413DFAB27DE03AA564BB3986D1CE377DCBA21B4E3F5BBA5BE3495C1BF6F`
  (the aggregate before this slice was `8DF23FF1...635D`; it changed because
  the frozen file changed). Run before this record existed and again after
  writing it, with identical numbers.
- production: `RESULT=PASS PASS_COUNT=167 FAIL_COUNT=0`
  (`FREEZE_SHA256=72AC9D693856A8AC9D191B75E582670920AD645DC857F44BBAB09CBE1BC688CA`,
  `FREEZE_FILE_COUNT=10`).
- stream mapping test: `RESULT=PASS CHECKS=987 FRAME_OBLIGATIONS=440`.
- foundation: `RESULT: PASS`.
- UX architecture: `SUMMARY: PASS; pass=113; fail=0`.

**Severity scale.** HIGH: blocking. MEDIUM: significant; blocks under the
package convention. LOW: minor; does not block.

**Verdict: PASS.** No finding at any severity. The fourteen insertions were
applied verbatim, once each, at their anchors, in plan order; the only wording
not in the plan is the `INS-01` pin that D-047 directs; the change set contains
nothing else; the re-pin is correct; the handoff artifact now passes the
OBL-GRAM-03 three-hit test. Observations are recorded in section 7 and are not
defects of this slice.

---

## 1. Block-by-block verification (Q1)

**Method.** I extracted every fenced block that follows a `**Block INS-nn**`
heading in the amendment as committed at `c07e455` (thirteen blocks; `INS-12`
is a literal replacement with no block) by its line range, then searched the
amended frozen file for each block three ways: exact raw text with the block's
own line breaks, an exact contiguous line sequence, and whitespace-normalised
text. I then checked position against the anchor the plan names and order
across the file. Line numbers below are in the file at `c07e455`.

| Insertion | Amendment lines (block) | Applied at frozen lines | Verbatim | Placement against the plan |
|---|---|---|---|---|
| `INS-01` | 814 to 818 | 5 to 12 | Yes, with the two `[GATED]` placeholders filled and the D-047 pin (section 1.1) | Immediately after the `**Amended:**` line (line 4). No `[GATED` token remains in the frozen file. |
| `INS-02` | 824 to 832 (9 lines) | 79 to 87 | Exact | Immediately after the `**Bounded inventory:**` bullet (ends line 78); gap 1, continuing the bullet list |
| `INS-03` | 838 to 844 (7 lines) | 171 to 177 | Exact | After the closing paragraph of section 2.2 (ends 169) with one blank line |
| `INS-04` | 851 to 853 (3 rows) | 190; 197; 198 | Exact, row by row | Row 1 replaces the `semantic.focus.{ring,offset}` row in place (old row absent); rows 2 and 3 are the two lines immediately before the `component.*` row (199); the six intervening rows are untouched |
| `INS-05` | 859 to 865 (7 lines) | 219 to 225 | Exact | Immediately after the last bullet of section 2.4 (ends 218) |
| `INS-06` | 879 to 880 (2 rows) | 240; 245 | Exact, row by row | Replace the `Shell and navigation` and `Overlay and immersive` rows in place (old rows absent; the four intervening rows untouched) |
| `INS-07` | 886 to 901 (16 lines) | 289 to 304 | Exact | After the transactional-states paragraph (ends 287) with one blank line |
| `INS-08` | 907 to 970 (64 lines) | 306 to 369 | Exact | New `### 3.4` after section 3.3 (264) and before `## 4.` (371), one blank line each side |
| `INS-09` | 976 to 989 (14 lines) | 396 to 409 | Exact | Immediately after the last bullet of section 4 (ends 395) |
| `INS-10` | 995 to 1003 (9 lines) | 439 to 447 | Exact | Replaces the contrast bullet in place within section 5 (411 to 463); the old bullet is absent |
| `INS-11` | 1009 to 1020 (12 lines) | 451 to 462 | Exact | Immediately after the last bullet of section 5 (ends 450) |
| `INS-12` | table row 802 (literal) | 523, inside item 4 (520) | `UXTEST-001 through UXTEST-046.` once; no `UXTEST-045` anywhere | In place |
| `INS-13` | 1026 to 1029 (4 lines) | 533 to 536 | Exact | Appended to item 7 (530 to 532), before item 8 (537) |
| `INS-14` | 1035 to 1053 (19 lines) | 560 to 578 | Exact | Items 15 to 17 after item 14 (555 to 559) and before the closing paragraph (580) |

**Order.** Block start lines are strictly increasing from `INS-01` (5) to
`INS-14` (560), with the non-contiguous `INS-04` rows (190, 197, 198) and
`INS-06` rows (240, 245) falling in sequence. Plan order holds.

**Nothing else changed.** The frozen-file diff has twelve hunks. Its seven
removed lines are exactly the five replaced items: the old focus row, the two
old taxonomy rows, the three lines of the old contrast bullet, and the
`UXTEST-045` line. Its 178 added lines reconcile hunk by hunk to the insertions
(+8 `INS-01`; +9 `INS-02`; +8 `INS-03` with its separating blank; +2 net
`INS-04`; +7 `INS-05`; 0 net `INS-06`; +82 `INS-07` and `INS-08` with their
blanks; +14 `INS-09`; +18 net `INS-10` and `INS-11`; 0 net `INS-12`; +4
`INS-13`; +19 `INS-14`), a net +171 lines: 413 + 171 = 584. I read every added
line; each belongs to a block. Section numbering is intact (`### 3.4` is the
only new heading).

### 1.1 `INS-01` and the mechanical mandate

The applied line reads: "**Amended (R-039):** 2026-09-24 under D-046 and
D-047, applying `DESIGN_SYSTEM_AMENDMENT_R-039.md` at its accepted revision 2
(commit `cf455db9d0fc5fc285ea2153d3d924f1d7afa332`; SHA-256
`61b924951ff955faa16ae067ba9baf2e0a0f7987f91df5f907f42cda4fe0e9ea`; accepted at
D-047 on 2026-09-24): adds the delivery-stream axis, the four stream tokens,
the delivery stream control component, and the focus-ring tokens including the
3D focus ring. No inherited identity value, primitive ID, route, flow or state
profile changed." With the two placeholders substituted (2026-09-24; D-047) and
the phrase "at its accepted revision 2 (...)" removed, the block matches the
plan text exactly once. The plan (section 5, lines 780 to 782 of the amendment)
says the placeholders "are filled only by the acceptance decision", and D-047
is that decision; D-047 further directs that the "applied text pins the
accepted revision by commit and SHA-256". The added phrase states only facts
D-047 records (revision 2, its commit, its SHA-256, the acceptance date) and no
design content. **Judgement: within the mechanical mandate.** The clause
"accepted at D-047 on 2026-09-24" repeats what "under D-046 and D-047" and the
leading date already say; harmless, not a finding.

## 2. DSB-02 (Q2)

Review 2 wrote DSB-02 with two alternatives: "Add to `INS-01` a gated
placeholder for the accepted revision of the amendment (commit and SHA-256),
so that the three assumption citations resolve to a pinned text; or carry the
A-2 and A-4 sentences inline in the three blocks." The implementer took the
first: `INS-01` now pins revision 2 by commit and SHA-256, and the A-2 citation
applied by `INS-08` (frozen lines 319 to 321) and the A-4 citations applied by
`INS-04` (line 198) and `INS-09` (lines 408 to 409) keep the wording
"recorded assumption A-2/A-4 of `DESIGN_SYSTEM_AMENDMENT_R-039.md`", which
resolves through that pin. **Option one satisfies DSB-02 as my record wrote
it.** D-047 summarised the handling as pinning "instead of citing the
amendment by name"; the citations by name remain, as option one allowed, and
they now resolve to a pinned revision. The summary is loose, the effect is the
prescribed one, and no change is required.

## 3. DSB-01 (Q3)

The amendment at `c07e455` retitles its section 3.2 heading to "Anatomy, in
`PRIM-001` record order, and the order constraints" (line 337), the example
wording DSB-01 offered, and adds a "Revision 3 (application, 2026-09-24)" row
to its Revision history (line 1181) stating that this revision changes only the
heading and the row. The amendment diff contains exactly those two changes.
The Date line (17) still reads "Revision 2, 2026-09-24" and the
`[PROPOSED SPECIFICATION]` marker is retained. **Not a finding.** The Date
line correctly identifies the accepted specification revision, and revision 3
is an application record, not a specification revision, which its own row
says; the marker follows the D-044 precedent, under which
`DELIVERY_STREAM_ACCESSIBILITY_OBLIGATIONS.md` and
`DELIVERY_STREAM_EVIDENCE_MODEL.md` kept their `[PROPOSED SPECIFICATION]`
headers after acceptance at D-045 and acceptance is recorded in `DECISIONS.md`.
At the next editorial opportunity the Date line could add "Revision 3
(application)"; nothing turns on it.

## 4. Freeze re-pin (Q4)

`Get-FileHash -Algorithm SHA256` on the amended frozen file gives
`1893D026E6B17E98C3267D80AE929760780639FEB499A49F999C9E64C9168B81` for the git
blob at `c07e455` and for the working-tree file (the file is LF-only: 584 LF,
0 CRLF, 0 lone CR; 42812 bytes in both). The validator constant at line 829 is
that value. Lines 827 and 828 are two new comment lines: line 827 records the
old hash `0E9FC68C98AC25C4F7DFBC62B10DBA1FCB197F5C82AD2FF39DCD0C16D9CFB763` as
"pinned until D-047"; line 828 records the application under D-047 from
revision 2 at `cf455db`. The validator diff is three added lines and one
removed line (the old constant) and nothing else. The `design-system-freeze-hash`
assertion passes at the new value. Correct.

## 5. R-039 exit test on the handoff artifact (Q5)

Searched in the amended `DESIGN_SYSTEM_IMPLICATIONS.md`:

- **(a) per-stream contrast rule:** section 5 bullet at lines 439 to 447,
  "Contrast is checked per rendered state and per stream ... never inherited
  by another stream; aggregate evidence that names no stream, or another
  stream, discharges no per-stream obligation"; also lines 360, 561, 569.
- **(b) stream-control component:** section 3.1 row at 240, `### 3.4 Delivery
  stream control component` at 306 with the component contract at 308 to 369,
  and item 15 at 560.
- **(c) focus-ring tokens:** section 2.3 row at 198
  (`semantic.focus.scene.{ring,ring-width,offset,layer,contrast-floor,motion}`
  as `--hd-focus-scene-*`, width 3 px, 3:1 floor, rendered above
  `semantic.elevation.panel`), the replaced 2D row at 190, and uses at 360,
  406, 461, 572, 576.
- **Stream axis:** header line 10, section 1.1 bullet at 79, section 2.2
  paragraph at 171, section 2.4 bullet at 219 to 225.
- **Four stream tokens:** section 2.3 row at 197
  (`semantic.stream.{high,medium,low,semantic}` as `--hd-stream-*`), the
  variant grammar at 224, `--hd-stream-*-label` at 333, and item 17 at 575.

Three hits, each substantive; the axis and the four tokens are present.
OBL-GRAM-03 is discharged on the artifact implementation inherits.

## 6. Validator runs (Q6)

As the header states: design `RESULT=PASS PASS_COUNT=208 FAIL_COUNT=0` with
`design-system-freeze-hash` at the new value; production `RESULT=PASS
PASS_COUNT=167 FAIL_COUNT=0`; stream mapping test `RESULT=PASS CHECKS=987
FRAME_OBLIGATIONS=440`; and, because D-047 names them, foundation `RESULT:
PASS` and UX architecture `SUMMARY: PASS; pass=113; fail=0`. `git status
--short` was empty after every run.

## 7. Observations (not findings of this slice)

1. **`validation/validation-report.md` line 22** states `RESULT=PASS
   PASS_COUNT=201 FAIL_COUNT=0` while the validator has returned 208 since
   before this slice. The validator's `validation-report-counts-agreement`
   asserts only the `COUNTS` line, so the stale `RESULT` line is not caught.
   D-047 speaks of re-pinning the aggregate "in the validator and its frozen
   report", but the report deliberately does not embed the aggregate (its
   "Freeze hashing" section, lines 228 to 235, explains that embedding it would
   be self-referential) and the validator carries no aggregate constant, so
   there was nothing of that kind to re-pin. The stale count predates the slice
   and should be corrected at the next report refresh.
2. **Line endings and the byte-level pins.** The repository has
   `core.autocrlf=true` and no `.gitattributes`. I compared the working-tree
   bytes of the fourteen freeze files with their git blobs at `c07e455`. The
   amended `DESIGN_SYSTEM_IMPLICATIONS.md` and every other `.md` and `.ps1`
   file are LF-only and hash identically in both places, so the R-039 pin
   `1893D026...8B81` is reproducible from repository content. Five CSVs are
   not: `foundation-route-coverage.csv` (35 CRLF, 0 LF in the working tree),
   `foundation-flow-coverage.csv` (89 CRLF, 1 LF), `design-batch-plan.csv` (9
   CRLF, 1 LF), `component-primitives.csv` (59 CRLF, 4 LF) and
   `traceability.csv` (285 CRLF, 3 LF) each differ from their LF blobs. In
   particular the pinned `component-primitives-freeze-hash`
   `EF0DE11B...9C78` is the hash of the mixed-ending working-tree bytes; the
   blob hashes to `575D1478893C090E9B367E75C2D14CF645E80EEB67BCE09C2383C08294FA034A`.
   A fresh checkout on any platform (LF, or all-CRLF under `autocrlf=true`)
   would therefore fail `component-primitives-freeze-hash` and produce a
   different `FREEZE_AGGREGATE_SHA256`, even though the content is unchanged.
   This condition predates this slice (the primitives hash was pinned at
   D-045) and does not affect the R-039 application. I recommend it be logged
   as its own risk and resolved under a decision: add a `.gitattributes`
   fixing `eol=lf` for the package, renormalise the working tree, and re-pin
   the affected hashes.
3. **Closure records.** `RISKS.md` R-039 still reads `in_progress` and names
   the file "at `0E9FC68C...B763`"; the `TASKS.md` R-039 row is still
   `in_progress`. D-047 sequences their update after this verification; they
   are the closure step, not part of this slice.
4. **Frozen header `**Status:**` line** (line 13: "producer revision 3 of 3;
   accessibility correction only") is unchanged because the plan directed no
   change to it; it now under-describes the file. Editorial, for a later slice
   under a decision, in the same family as UG-11.
5. **Historical references** to the old hash and the 201 count in
   `producer-inspection.md` (lines 34 and 171), `DECISIONS.md` line 174,
   `MANUAL_ACTIONS.md` and `CHANGELOG.md` are dated records of earlier runs and
   are correct as history.

---

## Findings

None. No `DSC` finding is raised at any severity.

---

## Verified

**V-01 Subject.** `git rev-parse HEAD` = `c07e455a9458b0d3094cdb749a34cd6ee2031d7d`;
`git show --stat c07e455` lists the three files above with parent `31ebf4d`;
`git diff --stat 31ebf4d c07e455` agrees (183 insertions, 9 deletions). Frozen
file: 584 lines; `sha256sum` `1893d026...8b81` (lowercase of the validator
value). Working tree clean before and after every run.

**V-02 Change set beyond the frozen file.** Validator diff: line 827 (old hash
as provenance), line 828 (application note), line 829 (new constant); old
constant line removed; nothing else. Amendment diff: line 337 heading; line
1181 Revision 3 row; nothing else.

**V-03 Blocks.** Thirteen fenced blocks extracted by line range at `c07e455`
(section 1 table); twelve match exactly as raw text and as contiguous line
sequences; `INS-04` and `INS-06` match row by row at the positions the plan
directs; `INS-01` matches after placeholder substitution and pin removal;
`INS-12` literal present once with the old literal absent. Old focus row, old
taxonomy rows, old contrast bullet and old `UXTEST-045` literal: zero
occurrences. Retained anchors (`**Amended:**` line, `component.*` row): one
occurrence each. Adjacency gaps and order as tabulated. Hunk reconciliation
as stated in section 1.

**V-04 Re-pin.** Section 4. Working-tree and blob hashes equal; equal to the
line-829 constant; assertion passes.

**V-05 Exit test.** Section 5: three hits, axis present, four tokens present.

**V-06 Validators.** Section 6: five validators, all PASS; design validator
rerun after writing this record with identical numbers.

**V-07 Line endings.** `git ls-files --eol` and a byte count per freeze file
(CRLF, LF, lone CR; tree bytes versus blob bytes; hash equality), as reported
in observation 2.

**V-08 Record hygiene.** This record contains no Markdown links; the
validator's conformance pattern and its nine peer-framing alternatives return
zero matches on it.

---

## Recommendation to the founder

**R-039 may close:** the accepted amendment was applied mechanically and
verbatim, the handoff artifact now carries the per-stream contrast rule, the
delivery stream control component, the four stream tokens and the 3D focus-ring
tokens, the freeze is correctly re-pinned and every validator passes; the line-
ending fragility in observation 2 should be logged as a separate risk rather
than hold R-039 open.

## Standing note

This record is an input to the closure decision, not a decision. It changes no
file other than itself, it did not edit the frozen file, the amendment, any
validator or any review, it made no external call, and it claims no
conformance of any kind. The twelve `[UNRESOLVED GATE]` items in the
amendment's section 7 remain open founder decisions, as D-047 states.
