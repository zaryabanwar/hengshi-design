# Independent Verification — R-043 Treatment (line endings for the production and UX-architecture packages)

**Review date:** 2026-09-25
**Commissioning decision:** D-049 (2026-09-24), which approved the R-043
treatment and requires independent verification before R-043 closes.
**Subject under review:** commit `af043fe38d576ee522bacdf3b808737e42dbb86a`
(2026-09-24, "fix: treat R-043 line endings for the production and
UX-architecture packages (D-049)"), parent
`e2905c2dad79ba6a65a7f9bc3cf57c39772ebfd3`. `git log -1 --format=%H` on the
working tree and `git rev-parse HEAD` both give that commit, which equals the
commit named in the brief; the working tree was clean at the start of this
verification. The change set, from `git show --stat af043fe` and `git diff
--numstat e2905c2 af043fe`, is four files, 64 insertions and 1 deletion:
`.gitattributes` (+7), `CHANGELOG.md` (+13), `DECISIONS.md` (+43) and
`RISKS.md` (1 line changed). No validator, no CSV, no package content.
**Freeze values at this commit:** design aggregate
`631324D0498B695B016CF7D5B052DC491C95F28D7D9B6AE88BA44EB363FE3EBF` (unchanged
since D-048); `design-system-freeze-hash` `1893D026...8B81` and
`component-primitives-freeze-hash` `575D1478...034A` (unchanged); production
emitted `FREEZE_SHA256`
`D4F8F128C20A8287BE0B91D50898D7E10D6A5A5E636D569301D2A45CC25D8435` with
`FREEZE_FILE_COUNT=10`.
**Reviewer:** the independent review agent that wrote the R-039 reviews, the
application verification and the R-042 verification which found this
condition. I did not implement the treatment, I did not author D-049, and I
read no agent transcript and no other agent's working files. Constitution
2.0.0 principle VII: I verify, I did not implement.
**Authority I verify against, and may not overrule:** D-049 and D-048 in
`DECISIONS.md`; the R-043 row in `RISKS.md`; the observation that raised
R-043 in `reviews/r-042-treatment-verification.md`; the validator method
(`Get-FileHash -Algorithm SHA256` on raw bytes, uppercase hex).
**Deterministic validator state at review, from the repository root** (no
tracked file modified by any run; `git status --short` empty after each):

- design: `RESULT=PASS PASS_COUNT=208 FAIL_COUNT=0`; both freeze hashes at
  their pinned values; `git-write-scope` PASS;
  `FREEZE_AGGREGATE_SHA256=631324D0...3EBF`, the expected value. Run before
  this record existed and again after writing it, with identical numbers.
- production: `RESULT=PASS PASS_COUNT=167 FAIL_COUNT=0`;
  `FREEZE_SHA256=D4F8F128...8435`, the expected value; `FREEZE_FILE_COUNT=10`;
  all eleven `contract-section:*` assertions PASS.
- UX architecture: `SUMMARY: PASS; pass=113; fail=0`.
- foundation: `RESULT: PASS`.
- stream mapping test: `RESULT=PASS CHECKS=987 FRAME_OBLIGATIONS=440`.

**Severity scale.** HIGH: blocking. MEDIUM: significant; blocks under the
package convention. LOW: minor; does not block.

**Verdict: PASS.** No finding at any severity against the treatment. The
treatment does exactly what D-049 authorizes, and the R-043 exit test passes:
a fresh local clone under `core.autocrlf=true` shows every text file of the
three packages and `scripts/validation` as LF and passes all four validators
and the stream-mapping test unchanged with the same freeze values.
Observation 1 in section 8 is material and outside D-049's scope: the same
clone fails the brand-identity and compatibility validators, which no
decision has yet covered.

---

## 1. `.gitattributes` (Q1)

The diff adds exactly seven lines at the end of the file; the first seven
lines (the R-042 comment pair and its five rules) are unchanged, as the hunk
context shows and as `cat -A` confirms against the content verified in
`reviews/r-042-treatment-verification.md`. The additions are one comment
line naming R-043 and six path-scoped per-extension rules:
`docs/phase-1-ui-reference-production/**/*.md`, `*.csv` and `*.ps1`, and
`docs/phase-1-ux-architecture/**/*.md`, `*.csv` and `*.ps1`, each
`text eol=lf`. The file is LF-terminated with no byte-order mark. A search for
any unscoped pattern (a line beginning with `*`, or a bare `*` pattern) finds
none: there is no repository-wide rule.

`git check-attr text eol`: `docs/phase-1-ui-reference-production/evidence-capture-plan.csv`,
`batch-production-plan.csv`, `validation/validate-ui-reference-production.ps1`
and `validation/validation-report.md`, and
`docs/phase-1-ux-architecture/UX_ARCHITECTURE.md`, `traceability.csv`,
`validation/validate-ux-architecture.ps1` and `STATES_AND_RECOVERY.md`, all
report `text: set`, `eol: lf`; `docs/phase-1-foundation/README.md` and
`docs/requirements/CR-002-signal-portability-verification.md` report
`unspecified`. A hypothetical `.json` in either package would also be
`unspecified` (the new rules cover `.md`, `.csv` and `.ps1`, which is every
extension that exists there). `git ls-files` over the two packages lists 32
files, none with an extension other than `.md`, `.csv` or `.ps1`, so no
non-text file exists under either package and no binary is declared as text.
Result: as specified.

## 2. The two normalised CSVs and the 32 package files (Q2)

`docs/phase-1-ui-reference-production/evidence-capture-plan.csv` and
`docs/phase-1-ux-architecture/traceability.csv` are absent from the commit
diff. `git ls-files --eol` over the two packages reports `i/lf w/lf
attr/text eol=lf` for all 32 files. The SHA-256 of each normalised working
file equals the SHA-256 of its `HEAD` blob (`git cat-file -p HEAD:path` piped
to `sha256sum`) and equals the implementer's value:

| File | Working file = HEAD blob | SHA-256 |
|---|---|---|
| `docs/phase-1-ui-reference-production/evidence-capture-plan.csv` | Yes | `60E2C752F1791C4F0284BA7AB81FFC83F9F78BE4C71BED7AF6A3688F44311A34` |
| `docs/phase-1-ux-architecture/traceability.csv` | Yes | `B41D77E880C45C875EF3CC448F09A4F576F02B230214EA3E9FD6ED840BEDE7B9` |

No content changed. Result: as specified.

## 3. Validators unchanged; pins and patterns (Q3)

`git diff --name-only e2905c2 af043fe` lists no validator and no `.ps1`
file. The UX-architecture validator pins four review files by SHA-256 at
lines 251 to 254; I recomputed each with `Get-FileHash -Algorithm SHA256`:

| File | Computed | Pinned (line) |
|---|---|---|
| `reviews/design-review-iteration-1.md` | `6D9939DB9FAF065857EB95FBF51CF804FF851C1497069A389E7332460567EFDF` | same (251) |
| `accessibility/accessibility-audit-iteration-1.md` | `DCF4F36F8A9C1F9FAD4E6F7E2E65B4EF09C30CBAA2267A64FDD28624C01F2D34` | same (252) |
| `reviews/design-review-iteration-2.md` | `7AB29D4EDEC5FEF3614E0A2801686C7BDE74701B907DB0BDC961BB608C26E5C7` | same (253) |
| `accessibility/accessibility-audit-iteration-2.md` | `ED633A821C2E13F06E726E979E283E2C8FE49289FE197ACDCCA4070E1FB66F41` | same (254) |

All four files are `i/lf w/lf` under the new attribute, so the pins are on
canonical LF bytes and needed no re-pin. The production validator pins no
file hash: its only hash-related assertion, `gate:D-037-freeze-hash-cited`
(line 412), checks that the contract text contains the D-037 citation string
`97E79201...120F`; its `FREEZE_SHA256` is emitted at line 608 and asserted
nowhere. Its eleven `contract-section:*` patterns (`(?m)^## N. Title$`) pass
on the LF working tree (eleven PASS lines in the root run). Result: as
specified.

## 4. Validators from the repository root (Q4)

As the header states: design `PASS 208/0` with aggregate `631324D0...3EBF`;
production `PASS 167/0` with `FREEZE_SHA256` `D4F8F128...8435`; UX
architecture `PASS 113/0`; foundation `PASS`; stream mapping test `PASS
CHECKS=987`. Both expected values match.

## 5. The R-043 exit test: fresh clone (Q5)

**Method.** `git -c core.longpaths=true clone` of the repository from its
local path (no network) into
`C:\Users\Zaryab\AppData\Local\Temp\claude\C--Users-Zaryab-Documents-Hengshi-Design-hengshi-design\9d5d05ad-a0fe-4f57-bc8c-e0f48979aca7\scratchpad\r043-verify-clone`,
nothing copied in. In the clone: `HEAD` is `af043fe`; the effective
`core.autocrlf` is `true` (inherited from the global configuration; not set
locally), so the machine-default conversion applies to every file without an
attribute.

**Line endings in the clone.** `git ls-files --eol` over the design,
production and UX-architecture packages and `scripts/validation` lists 65
files: 64 report `w/lf`, and one reports a blank `w/` field:
`docs/phase-1-ui-reference-design/reviews/design-system-amendment-r-039-application-verification.md`,
which the clone's `git status` also shows as ` M`. That entry is a Windows
path-length artifact, not a line-ending result: the file's full path in this
clone is 262 characters, above the 260-character `MAX_PATH` limit, and git's
`--eol` and status inspection fail to stat it even though the checkout under
`core.longpaths=true` wrote it. I read the file directly by its literal path:
19319 bytes, zero carriage returns, SHA-256
`23A2724E827CA82F101C7DDC7FACC916CFB74E775581AD48BE3F4C4A3AFB9C3B`, identical
to its `HEAD` blob and to the same file in the original working tree (which
reports `w/lf`); the same file also reported `w/lf` in the R-042 clone,
whose shorter folder name kept that path at 254 characters. Every text file
of the four scopes is therefore LF in the clone. Control files with no
attribute checked out as `w/crlf`: `.gitattributes`, the root `README.md`,
`docs/phase-1-foundation/README.md` and
`docs/requirements/CR-002-signal-portability-verification.md`, which shows
the conversion ran where unscoped and the rules prevented it where scoped.

**Validators from the clone root, all unchanged with the same freeze
values:** design `RESULT=PASS PASS_COUNT=208 FAIL_COUNT=0` with `PACKAGE_ROOT`
under the clone, `design-system-freeze-hash` PASS at `1893D026...8B81`,
`component-primitives-freeze-hash` PASS at `575D1478...034A` and
`FREEZE_AGGREGATE_SHA256=631324D0...3EBF`; production `RESULT=PASS
PASS_COUNT=167 FAIL_COUNT=0` with `FREEZE_SHA256=D4F8F128...8435`; UX
architecture `SUMMARY: PASS; pass=113; fail=0`; foundation `RESULT: PASS`;
stream mapping test `RESULT=PASS CHECKS=987 FRAME_OBLIGATIONS=440`. **The
R-043 exit evidence is met.** The clone folder is left in place.

**Also run from the clone root, beyond the exit test** (see observation 1):
brand strategy `RESULT: PASS`; brand identity `RESULT: FAIL` with
`FAILURES: 8` (root: `FAILURES: 0`, `RESULT: PASS`); compatibility
`VALIDATION FAILED` on "Baseline source hash drift: package.json" (root:
`VALIDATION PASSED: baselineItems=50; capabilities=6; components=50;
edges=27; deferredFamilies=9; referenceIndexEntries=149`).

## 6. Records (Q6)

- **D-049** (`DECISIONS.md` lines 311 to 353): the six rules, the two CSV
  normalisations with no content change, no validator edited, the four UX
  pins on LF bytes matching, the production validator pinning no file hash,
  the design aggregate unchanged at `631324D0...3EBF`, the production value
  `D4F8F128...8435` identical at the root and in a fresh clone, and the
  production report's dated `4464F6C4...` value left untouched: every
  statement matches sections 1 to 5. Its account of the earlier
  `72AC9D69...` value as a hash of a mixed working copy is consistent with the
  three distinct values seen for three byte states (root before treatment,
  all-CRLF clone, canonical LF now), though the mixed copy no longer exists to
  recompute. Its pre-commit validator numbers (design 207/1 and production
  166/1 on the uncommitted `.gitattributes`) cannot be reproduced after the
  commit by design; the post-commit results are consistent with that cause
  clearing at the commit. The two click-based gates are outside what I can
  verify and nothing turns on them.
- **R-043 row** (`RISKS.md` line 59): status `in_progress`; the treatment
  note names the same facts and the canonical production value; its exit
  evidence, "a fresh clone passes all four validators unchanged", is
  established in section 5.
- **CHANGELOG** entry "2026-09-24 — R-043 line-ending fragility treated for
  two more packages (D-049)": matches D-049 and the verified facts.
- **Production `validation-report.md` dated freeze value.** Lines 22, 23 and
  157 record `FREEZE_FILE_COUNT=9` and
  `FREEZE_SHA256=4464F6C44C11E7A00C4F007C3112840C6087CB3C1321B86ED5842B9100CC50CE`,
  the values of the run the report documents. The production validator
  references that report only in its required-files list (line 864) and
  asserts nothing about its content; no validator asserts `4464F6C4...`, and
  the D-045 record cites it as the production freeze of that date. The dated
  value therefore contradicts nothing asserted; it is a dated record, as the
  implementer reported.

No mismatch.

## 7. Findings

None. No `DSE` finding is raised at any severity.

## 8. Observations (not findings against this treatment)

1. **Residual line-ending exposure remains in two packages outside D-049's
   scope, and none in the foundation package or the scripts.** In the same
   clone, the brand-identity validator fails eight byte-pinned checks
   (checkpoint hashes, archive integrity, the forbidden-authority list, prior
   report hashes, the superseded archive, the D-028 source baseline and the
   `FINAL_FREEZE` manifest) over files that checked out as CRLF, including
   `.md`, `.csv`, `.json`, `.svg`, `.css`, `.html`, `.mjs` and `.ps1`, all of
   them text; and the compatibility validator fails on "Baseline source hash
   drift: package.json", a byte hash of a file outside every attribute rule.
   Both pass at the root. The foundation validator passes in the clone
   (unscoped, CRLF), the mapping test passes in the clone, and every
   `scripts/validation` file is LF under the R-042 rule. A treatment of the
   same shape (per-extension `text eol=lf` rules for
   `docs/phase-1-brand-identity` and for the compatibility package's baseline
   sources, or a re-pin under a decision) is needed there; it does not bear on
   R-043.
2. The verification folder name prescribed for this exit test pushes one
   design-package path to 262 characters, above the Windows limit, producing
   the `w/` and ` M` artifact described in section 5. Future exit tests
   should use a clone folder name short enough to keep every path under 260
   characters (the R-042 clone at 254 showed none of this), or the check
   should read the file bytes directly as done here.
3. `.gitattributes` itself carries no attribute and checked out as CRLF in
   the clone; git parsed it correctly regardless. A self-rule is optional.
4. `.json` is not covered in the two new packages; no `.json` file exists in
   either today. If one is added it would be unscoped, unlike the design
   package, whose rule set includes `.json`.

---

## 9. Verified

**V-01 Subject.** `git rev-parse HEAD` and `git log -1 --format=%H` =
`af043fe38d576ee522bacdf3b808737e42dbb86a`; `git show --stat af043fe` and
`git diff --numstat e2905c2 af043fe` agree on four files, 64 insertions,
1 deletion. Working tree clean before and after every run.

**V-02 Attributes.** Section 1: diff and `cat -A`; `git check-attr text eol`
on twelve paths; unscoped-pattern search; `git ls-files` extension filter
over the two packages (32 files, none outside `.md`, `.csv`, `.ps1`).

**V-03 CSVs.** Section 2: absent from the diff; `--eol` for all 32 files;
working-file and blob SHA-256 equal for both normalised files and equal to
the implementer's values.

**V-04 Validators unchanged; pins.** Section 3: no validator in the diff; four
UX pins recomputed and equal; production validator hash handling read at
lines 412, 608 and 864; eleven contract-section PASS lines at the root.

**V-05 Validators, repository root.** Section 4: five validators, all PASS,
expected aggregate and production value matched; design validator rerun
after writing this record with identical numbers.

**V-06 Exit test.** Section 5: clone at `af043fe` under global
`core.autocrlf=true` with `core.longpaths=true`; 64 of 65 scoped files
`w/lf` and the 65th verified LF by byte inspection with its blob hash; four
unscoped controls `w/crlf`; five validators from the clone root all PASS with
the same freeze values; brand strategy PASS, brand identity FAIL 8 and
compatibility FAIL in the clone (observation 1); clone left in place.

**V-07 Records.** Section 6: D-049, the R-043 row and the CHANGELOG entry
checked statement by statement; the production report's dated value traced
to the only place it is referenced.

**V-08 Record hygiene.** This record contains no Markdown links; the design
validator's conformance pattern and its nine peer-framing alternatives return
zero matches on it.

---

## 10. Recommendation to the founder

**R-043 may close:** a fresh clone under the machine default
`core.autocrlf=true` shows every text file of the design, production and
UX-architecture packages and `scripts/validation` as LF and passes all four
validators and the stream-mapping test unchanged with the same freeze values;
no residual line-ending exposure remains in the foundation package or the
scripts, but the brand-identity package (eight byte-pin failures in the same
clone) and the compatibility validator (`package.json` baseline hash drift)
remain exposed and should be logged as a new risk rather than hold R-043
open.

## Standing note

This record is an input to the closure decision, not a decision. It changes no
file other than itself, it did not edit `.gitattributes`, any validator, any
report or any record, it made no external call, and it claims no conformance
of any kind. The clone under the scratchpad is a verification artifact, not
part of the repository.
