# Independent Verification — R-042 Treatment (line-ending freeze fragility)

**Review date:** 2026-09-24
**Commissioning decision:** D-048 (2026-09-24), which approved the R-042
treatment and requires independent verification before R-042 closes.
**Subject under review:** commit `e99e3c58adf047a2b49c79dd38332c31747cd713`
(2026-09-24, "fix: treat R-042 line-ending freeze fragility (D-048)"), parent
`f450a76cc74df96c564175d44a61d092484ccdf3`. `HEAD` is that commit and the
working tree was clean at the start of this verification. The change set, from
`git show --stat e99e3c5` and `git diff f450a76 e99e3c5`, is six files, 70
insertions and 5 deletions: `.gitattributes` (new, 7 lines), `CHANGELOG.md`
(+14), `DECISIONS.md` (+42), `RISKS.md` (1 line changed),
`validation/validate-ui-reference-design.ps1` (+3, -1) and
`validation/validation-report.md` (3 lines changed). No CSV, no
`DESIGN_SYSTEM_IMPLICATIONS.md`, no other package.
**Pinned values at this commit:** `component-primitives-freeze-hash`
`575D1478893C090E9B367E75C2D14CF645E80EEB67BCE09C2383C08294FA034A`;
`design-system-freeze-hash` unchanged at
`1893D026E6B17E98C3267D80AE929760780639FEB499A49F999C9E64C9168B81`; emitted
design freeze aggregate
`631324D0498B695B016CF7D5B052DC491C95F28D7D9B6AE88BA44EB363FE3EBF`.
**Reviewer:** the independent review agent that wrote the R-039 reviews and
the application verification which found this condition. I did not implement
the treatment, I did not author D-048, and I read no agent transcript and no
other agent's working files. Constitution 2.0.0 principle VII: I verify, I did
not implement.
**Authority I verify against, and may not overrule:** D-048 in
`DECISIONS.md`; the R-042 row in `RISKS.md`; the observation that raised R-042
in `reviews/design-system-amendment-r-039-application-verification.md`; the
validator method (`Get-FileHash -Algorithm SHA256` on raw bytes, uppercase
hex).
**Deterministic validator state at review, from the repository root** (no
tracked file modified by any run):

- design: `RESULT=PASS PASS_COUNT=208 FAIL_COUNT=0`;
  `component-primitives-freeze-hash` PASS at `575D1478...034A`;
  `design-system-freeze-hash` PASS at `1893D026...8B81`; `git-write-scope`
  PASS; `FREEZE_AGGREGATE_SHA256=631324D0498B695B016CF7D5B052DC491C95F28D7D9B6AE88BA44EB363FE3EBF`.
  Run before this record existed and again after writing it, with identical
  numbers.
- production: `RESULT=PASS PASS_COUNT=167 FAIL_COUNT=0`
  (`FREEZE_SHA256=72AC9D693856A8AC9D191B75E582670920AD645DC857F44BBAB09CBE1BC688CA`).
- UX architecture: `SUMMARY: PASS; pass=113; fail=0`.
- foundation: `RESULT: PASS`.
- stream mapping test: `RESULT=PASS CHECKS=987 FRAME_OBLIGATIONS=440`.

**Severity scale.** HIGH: blocking. MEDIUM: significant; blocks under the
package convention. LOW: minor; does not block.

**Verdict: PASS.** No finding at any severity against the treatment. The
treatment does exactly what D-048 authorizes, and the R-042 exit test passes:
a fresh local clone under `core.autocrlf=true` passes the design validator
unchanged with the re-pinned primitive hash and the same aggregate.
Observation 1 in section 9 is material and outside D-048's scope: the same
clone fails the production and UX-architecture validators, which the
treatment did not cover; the recommendation in section 11 conditions closure
on logging it.

---

## 1. `.gitattributes` (Q1)

**Content** (seven lines, LF-terminated, no byte-order mark): two comment
lines naming R-042 and the scoping rule, then five rules:
`docs/phase-1-ui-reference-design/**/*.md text eol=lf`, the same for `*.csv`,
`*.ps1` and `*.json`, and `scripts/validation/**/*.ps1 text eol=lf`. Every
rule is path-scoped and per-extension. There is no repository-wide rule (no
unscoped `*` pattern) and no rule naming a binary type.

**`git check-attr text eol`** results: `docs/phase-1-ui-reference-design/README.md`,
`component-primitives.csv`, `validation/validate-ui-reference-design.ps1`,
`validation/validation-report.md`, `reviews/design-review-iteration-6.md`,
`accessibility/DELIVERY_STREAM_ACCESSIBILITY_OBLIGATIONS.md` and a
hypothetical `hypothetical.json` in the package all report `text: set`,
`eol: lf` (the `**/` form matches the package root and every subdirectory);
`scripts/validation/ui-stream-mapping.ps1` and
`scripts/validation/test-ui-stream-mapping.ps1` report `eol: lf`; the root
`README.md`, `docs/phase-1-ux-architecture/UX_ARCHITECTURE.md`,
`docs/phase-1-ui-reference-production/batch-production-plan.csv` and a
hypothetical `scripts/validation/hypothetical.md` all report `unspecified`.

**No binary declared as text:** `git ls-files` under the two scoped paths
lists no file whose extension is not `.md`, `.csv`, `.ps1` or `.json`, so the
rules cover text files only. Result: as specified.

## 2. The five CSVs (Q2)

`component-primitives.csv`, `design-batch-plan.csv`,
`foundation-flow-coverage.csv`, `foundation-route-coverage.csv` and
`traceability.csv` are absent from the commit diff. `git ls-files --eol`
reports `i/lf w/lf attr/text eol=lf` for all five. The SHA-256 of each working
file equals the SHA-256 of its `HEAD` blob (`git cat-file -p HEAD:path` piped
to `sha256sum`), and each equals the number the implementer reported:

| File | Working file = HEAD blob | SHA-256 |
|---|---|---|
| `component-primitives.csv` | Yes | `575D1478893C090E9B367E75C2D14CF645E80EEB67BCE09C2383C08294FA034A` |
| `design-batch-plan.csv` | Yes | `1E3EBF7E1FF29D58D04A6202BF1E0CB757DCD11CCE9BCC2DE249AB5ABEA17BB8` |
| `foundation-flow-coverage.csv` | Yes | `045FA7CEA00728A5FECFE1E124B5D9EE828F960732C9C9920F8C9114C20038F7` |
| `foundation-route-coverage.csv` | Yes | `77D3C13DA712544685209206EF7CE3EE16EFA63C216741863DBB0083C3DD66AF` |
| `traceability.csv` | Yes | `1BE5D2A7C621824EF37E66641B4C7E40AECD7DE69911246FD7254EB11B669492` |

The working copies were normalised to their committed LF bytes; no content
changed. Result: as specified.

## 3. Re-pin (Q3)

`Get-FileHash -Algorithm SHA256` on `component-primitives.csv` gives
`575D1478893C090E9B367E75C2D14CF645E80EEB67BCE09C2383C08294FA034A`, which is
the `$expectedPrimitiveHash` constant at validator line 837. Two comment lines
were added above it: line 835 records the old value
`EF0DE11B23A6C6A9C8C721D55F528237A72153315B633E6198AF0B50ADED9C78` as "pinned
on a CRLF working copy until R-042", and line 836 records the R-042 re-pin on
the canonical LF bytes. The validator diff is those two comment lines and the
new constant, with the old constant line removed, and nothing else (numstat
3/1). Result: correct.

## 4. Frozen report (Q4)

The report diff (numstat 3/3) contains exactly three single-line numeric
edits: line 22 `PASS_COUNT=201` to `PASS_COUNT=208`; line 204 "thirteen
hash-pinned freeze files" to "fourteen"; line 230 "each of the 13 required
files" to "14". No other line changed. The report's `COUNTS` line (line 21) is
byte-identical to the `COUNTS` line the design validator emits (354 bytes
each, compared with `cmp`), and the validator's
`validation-report-counts-agreement` assertion passes. Result: as specified.

## 5. Validators from the repository root (Q5)

As the header states: design `PASS 208/0` with `component-primitives-freeze-hash`
at `575D1478...034A`, `git-write-scope` PASS and aggregate
`631324D0498B695B016CF7D5B052DC491C95F28D7D9B6AE88BA44EB363FE3EBF` (the
expected value); production `PASS 167/0`; UX architecture `PASS 113/0`;
foundation `PASS`; stream mapping test `PASS CHECKS=987`. `git status --short`
was empty after every run.

## 6. The R-042 exit test: fresh clone (Q6)

**Method.** `git clone` of the repository from its local path (no network)
into `C:\Users\Zaryab\AppData\Local\Temp\claude\C--Users-Zaryab-Documents-Hengshi-Design-hengshi-design\9d5d05ad-a0fe-4f57-bc8c-e0f48979aca7\scratchpad\r042-clone`.
The first attempt with default settings completed the object transfer but
failed at checkout with "Filename too long" for ten archived brand-identity
files under `docs/phase-1-brand-identity/archive/`, whose paths exceed the
Windows path limit under the scratchpad prefix; that failure is unrelated to
line endings. I discarded that clone and repeated it with
`-c core.longpaths=true`, a Windows path-length setting that affects no
line-ending conversion. In the resulting clone: `HEAD` is `e99e3c5`; the
effective `core.autocrlf` is `true` (inherited from the global configuration;
not set locally), so the machine-default conversion applies.

**Line endings in the clone.** `git ls-files --eol` over
`docs/phase-1-ui-reference-design` and `scripts/validation` lists 32 files,
all `w/lf`. Control files with no attribute checked out as `w/crlf`:
`.gitattributes`, the root `README.md`,
`docs/phase-1-ux-architecture/UX_ARCHITECTURE.md` and
`docs/phase-1-ui-reference-production/batch-production-plan.csv`. So the
conversion did run where unscoped and the attribute rules prevented it where
scoped, which is the intended effect.

**Design validator from the clone root.** `PACKAGE_ROOT` is the clone path;
`design-system-freeze-hash` PASS at `1893D026...8B81`;
`component-primitives-freeze-hash` PASS at `575D1478...034A`;
`git-write-scope` PASS; `FREEZE_AGGREGATE_SHA256=631324D0...3EBF`;
`RESULT=PASS PASS_COUNT=208 FAIL_COUNT=0`. Identical to the repository-root
run; the clone reported a clean `git status` before and after. **The R-042
exit evidence is met.** The clone folder is left in place.

**Also run from the clone root, beyond the exit test:** stream mapping test
`PASS CHECKS=987 FRAME_OBLIGATIONS=440` and foundation `PASS`; production
`RESULT=FAIL PASS_COUNT=156 FAIL_COUNT=11` and UX architecture `SUMMARY: FAIL;
pass=107; fail=6`. See observation 1.

## 7. Records (Q7)

- **D-048** (`DECISIONS.md` lines 269 to 310) states the scope of the
  attribute rules, the five CSV normalisations with no content change, the
  hash move from `EF0DE11B...9C78` to `575D1478...034A` with provenance, the
  three report count refreshes, and the aggregate `631324D0...3EBF`. Every
  one of those statements matches what I verified in sections 1 to 5. Its
  pre-commit validator numbers (design 207/1 and production 166/1, failing
  only `git-write-scope` on the uncommitted root file) cannot be reproduced
  after the commit by design; the post-commit results (208/0 and 167/0) are
  consistent with the stated cause clearing at the commit. The four
  click-based gates are outside what I can verify and nothing turns on them.
- **R-042 row** (`RISKS.md` line 58): status `in_progress`; the treatment
  note names the same five facts and the same aggregate; the exit evidence is
  "a fresh clone, or a clean checkout after deleting the working copies,
  passes the design validator unchanged", which section 6 establishes.
- **CHANGELOG** entry "2026-09-24 — R-042 line-ending freeze fragility
  treated (D-048)": matches D-048 and the verified facts.

No mismatch. Two wording nuances, neither a finding: the records say "with
provenance comments" and the validator carries two, of which one holds the old
hash and the other the rationale; and the R-042 description column still
describes the condition as found ("no `.gitattributes`", CSVs "CRLF or
mixed"), which is the risk statement rather than the current state.

## 8. Findings

None. No `DSD` finding is raised at any severity.

## 9. Observations (not findings against this treatment)

1. **The same fragility class persists outside D-048's scope, and a fresh
   checkout exposes it.** In the clone of section 6, whose unscoped packages
   checked out as CRLF, the production validator fails eleven
   `contract-section:*` assertions (`RESULT=FAIL PASS_COUNT=156
   FAIL_COUNT=11`): they match `(?m)^## N. Title$` against the contract text,
   and `$` does not match before a carriage return. Its emitted
   `FREEZE_SHA256` is `4CA808D86CE100A63A7DD7E4C46074D3E275545EC5CA8817379B82D19CE53379`
   in the clone against `72AC9D69...88CA` in the LF working tree; the
   production hash is emitted, not pinned, so no assertion fails on it, but
   the value recorded in decisions and reports is not reproducible from a
   checkout. The UX-architecture validator fails six assertions (`pass=107;
   fail=6`): the action-matrix count (it parses `actions=0`), ACT contiguity,
   and four "iteration-N review or audit is unchanged" byte pins. D-048
   scoped the treatment to the design package and `scripts/validation`, and
   R-042 as logged names only the design validator, so this is not a defect
   of the treatment; it is the reason closure should not be read as
   repository-wide relief. A treatment of the same shape (attribute rules for
   `docs/phase-1-ui-reference-production` and
   `docs/phase-1-ux-architecture`, or CRLF-tolerant patterns and re-pins under
   a decision) is needed there.
2. `.gitattributes` itself carries no attribute and checked out as CRLF in
   the clone; git parsed it correctly regardless (the rules took effect). A
   `.gitattributes text eol=lf` line would remove the inconsistency; optional.
3. The frozen `validation-report.md` is now a hybrid: a 2026-09-06 narrative
   with refreshed numbers. Its line 204 still says the design-system file
   "declares no stream axis", which was true of the run it reports and is no
   longer true of the file; D-048 authorised the count refresh only, and the
   validator asserts only the `COUNTS` line. Editorial, for a future report
   refresh.

---

## 10. Verified

**V-01 Subject.** `git rev-parse HEAD` = `e99e3c58adf047a2b49c79dd38332c31747cd713`;
`git show --stat e99e3c5` and `git diff --stat f450a76 e99e3c5` agree on six
files, 70 insertions, 5 deletions; per-file numstat as in the header. Working
tree clean before and after every run.

**V-02 Attributes.** Section 1: content read with `cat -A` (LF, no BOM);
`git check-attr text eol` on thirteen paths; `git ls-files` extension filter
under the two scoped paths returns nothing.

**V-03 CSVs.** Section 2: absent from the diff; `--eol` `i/lf w/lf` for all
five; working-file and blob SHA-256 equal for all five and equal to the
implementer's numbers.

**V-04 Re-pin.** Section 3: `Get-FileHash` equals line 837; lines 835 and 836
are the provenance comments; validator numstat 3/1.

**V-05 Report.** Section 4: numstat 3/3; the three edits read from the diff;
`COUNTS` lines byte-identical (354 bytes, `cmp`);
`validation-report-counts-agreement` PASS.

**V-06 Validators, repository root.** Section 5: five validators, all PASS,
values as stated; design validator rerun after writing this record with
identical numbers.

**V-07 Exit test.** Section 6: clone at `e99e3c5` with global
`core.autocrlf=true` in effect and `core.longpaths=true` disclosed; 32 of 32
scoped files `w/lf`; four unscoped controls `w/crlf`; design validator from
the clone root `PASS 208/0` with the same two freeze hashes and the same
aggregate; mapping test and foundation PASS in the clone; production and UX
architecture FAIL in the clone (observation 1); clone left in place.

**V-08 Records.** Section 7: D-048, the R-042 row and the CHANGELOG entry
checked statement by statement against sections 1 to 6.

**V-09 Record hygiene.** This record contains no Markdown links; the design
validator's conformance pattern and its nine peer-framing alternatives return
zero matches on it.

---

## 11. Recommendation to the founder

**R-042 may close on its stated exit evidence** — a fresh clone under the
machine default `core.autocrlf=true` passes the design validator unchanged
with the re-pinned primitive hash and the same aggregate — **provided the
production and UX-architecture exposures found in that same clone (production
156/11, UX architecture 107/6 under a CRLF checkout) are logged as a new risk
or R-042 is widened before the closure record is written**, so that closing
R-042 is not read as resolving the repository-wide fragility.

## Standing note

This record is an input to the closure decision, not a decision. It changes no
file other than itself, it did not edit `.gitattributes`, any validator, any
report or any record, it made no external call, and it claims no conformance
of any kind. The clone under the scratchpad is a verification artifact, not
part of the repository.
