# Validation Report — MA-025 External UI Reference-Production Contract

**Package:** `docs/phase-1-ui-reference-production/`
**Report date:** 2026-09-06
**Validator:** `validation/validate-ui-reference-production.ps1`
**Host:** Windows 11, PowerShell 7.6.1
**Repository HEAD at run:** `0461170` (`main`), clean before this slice

## Executed command

```bash
pwsh -NoProfile -File docs/phase-1-ui-reference-production/validation/validate-ui-reference-production.ps1
```

## Outcome

```
RESULT=PASS PASS_COUNT=165 FAIL_COUNT=0
```

```
FREEZE_FILE_COUNT=9
FREEZE_SHA256=4464F6C44C11E7A00C4F007C3112840C6087CB3C1321B86ED5842B9100CC50CE
```

## Assertion counts by category

| Category | Passes | What it proves |
|---|---:|---|
| `cross-artifact` | 37 | Every batch row's prerequisites, time-limit branch, and browser profile match `design-batch-plan.csv` field by field, and every accepted row still reads `future_not_authorized` |
| `sequence` | 18 | Execution order is 1-7 unique, B01 runs first, every authorized batch's prerequisites are themselves authorized and run earlier, deferred batches carry no order |
| `gate` | 14 | The D-037 hash, MA-004, MA-010, MA-013, MA-026, the host MCP gap, the unverified pricing items, the capability evidence, the call budget and ledger, the verified allowance, the `SC-05` shortfall, the non-assertion of write-tool exemption, and the absence of a purchase workaround are all recorded |
| `contract-section` | 11 | All eleven founder-requested areas exist as normative sections |
| `local-reference` | 10 | Every relative link in the package resolves on disk |
| `required-file` | 9 | The nine freeze files are present |
| `claim-scan` | 9 | No unsupported conformance, deployment, live-page, or "file created" claim |
| `authorization` | 9 | Nothing is authorized to execute, **B01 is held**, six batches are conditional, two are deferred, the deferred set is B07/B09, and each deferral cites its real blocker |
| `boundary` | 8 | No `TL-EXCEPTION`, `TEST_CAPTURE` excluded, Stitch and billing prohibited, git operations gated, `UI_SPEC.md` absent, no evidence directory |
| `id-set` | 6 | `SC-01...12`, `EC-01...30`, `PE-01...12`, `TR-001...040`, `WS-P-01...08`, `WS-X-01...11` are exact sets with no gaps or extras |
| `accepted-input` | 6 | The six accepted D-037 inputs exist and are readable |
| `secret-scan` | 5 | No Figma token, GitHub token, private key, or credential-assignment pattern anywhere in the package |
| `csv-parse` | 5 | All five CSVs parse with their exact expected row counts |
| `traceability` | 4 | Every trace row has an authority and a gate, uses the status vocabulary, and records both unresolved gates |
| `A-16` | 3 | The nine-alternative framing pattern is assembled with nine elements, its scope is the union of all three packages, and no file in scope frames a stream as a degradation |
| `A-15` | 3 | All three packages are in scope, every `STREAM_*` frame-name segment resolves against the closed four-token vocabulary, and three abolished spellings are still rejected |
| `git-write-scope` | 2 | All worktree changes are within the documentation tree plus enumerated durable root records; no application, lockfile, or migration change |
| `A-14` | 2 | The per-stream obligation set is non-empty, and every unmet obligation is explained by held authorization rather than by omission |
| `A-12` | 2 | The amended `EC-08` grammar rejects all four negative fixtures and accepts a well-formed identifier |
| `freeze` | 1 | A reproducible 64-character package hash was computed |
| `A-13` | 1 | Every `stream_disposition` key and value resolves against the accepted design package, and every `deferred_B<NN>` target is itself deferred |
| **Total** | **165** | |

## What the D-045 assertions added, and the one thing they could not settle

`A-12` through `A-16` were added in this slice under decision **D-045**. They are the
production-side half of an evidence model whose design-side half is `A-01`-`A-11`:
stream obligations are **declared** at the primitive, **computed** at the template by
a union fold, and **inherited unstored** at route and flow. No production row stores a
stream either.

Three of them are worth singling out.

- **`A-15` was first written too broadly and had to be narrowed.** Its first version
  matched any `STREAM[_-]<TOKEN>` and returned 32 false positives, because three
  legitimate vocabularies in the packages use the word — state identifiers
  (`STATE-STREAM-CHANGED`), requirement identifiers (`NFR-STREAM-01`), and file names.
  It now matches only the `EC-08` frame-name segment. The narrowing is recorded in the
  validator source with its reason: **a guard that fails on correct records teaches
  producers to widen exemptions**, which is how the design package's peer-framing guard
  acquired the hole R-034 hid in.
- **`A-16` found six live UX-package files still carrying the abolished vocabulary**,
  three days after D-039 abolished it, because no previous guard looked outside the
  design package's own thirteen freeze files. Its exemption class is **closed and
  structural** — the `reviews/` and `accessibility/` directories, which hold dated
  historical records, plus four named self-referential files — and a strict-subset
  assertion fails if the exempt set ever grows to swallow the scanned set.
- **`A-13` reports rather than fails.** `stream_disposition` is **constant across all
  nine production batches**: `INERT-REPORT batch-production-plan.csv:stream_disposition
  distinct-values=1 rows=9`. This is a direct consequence of `N-01`, which puts the
  semantic host shell in nearly every template's dependencies, so every batch inherits
  all four streams. The column is therefore inert in exactly the sense `A-11` was built
  to detect. It is implemented literally as the accepted specification requires — it is
  the hook `A-13` resolves against — and reported rather than failed, **because failing
  it would be the producer overruling an accepted specification, which is the authorship
  D-045 exists to stop.** It belongs to the same unadjudicated set as the design
  package's twenty-two inert columns and is owed a founder decision.

## Freeze algorithm

Identical to the D-037 producer freeze so the two are comparable:

1. Take the nine required relative paths.
2. Sort them with `StringComparer.Ordinal`.
3. For each, emit `UPPERCASE_SHA256` + two spaces + the forward-slash relative path.
4. Join with LF, no terminal newline.
5. Hash the result as UTF-8 without BOM.

`validation-report.md` is deliberately **excluded** from the freeze set, following
the D-037 precedent that a report about a package must not be able to mutate the
package it reports on.

## Limitations of this validation

This validator is **deterministic and documentation-only**. It proves internal
consistency and fidelity to accepted authority. It does not and cannot prove:

1. **That the contract is correct policy.** Whether Figma is the right provider,
   whether serial execution is the right trade, and whether the cost boundary is
   acceptable are judgement calls for independent review and the founder.
2. **Any provider fact.** No network call is made. **Updated 2026-09-06:** one of
   the five §7.2 items — the MCP tool-call allowance — has since been verified out
   of band at **20 calls per calendar month** and is recorded in
   `capability-evidence.md`. The other four remain unverified, and the validator
   still only asserts that they are *recorded as unverified*.
3. **Host capability.** **Superseded 2026-09-06.** The validator no longer asserts
   unconditionally that `capability-evidence.md` is absent. It derives a
   `PRE_APPROVAL`/`POST_APPROVAL` lifecycle state from the MA-025 status in
   `MANUAL_ACTIONS.md`: before approval it asserts the file's absence, and after
   approval it requires the file, the call budget, and the call ledger, plus the
   recorded allowance, the `SC-05` shortfall, and the non-assertion of write-tool
   exemption. It still makes no network call and still does not itself test
   provider connectivity — that remains the job of the recorded capability test.
   This applies the R-024 lesson: never assert that an authorized mutable input
   remains immutable.
4. **Anything about produced evidence.** No batch has run. The evidence rules in
   `evidence-capture-plan.csv` carry `verification_method` values that only become
   executable once a batch produces a manifest.
5. **Review outcomes.** Independent design and accessibility review are separate
   human obligations under Constitution 2.0.0 principle VII.

## Reproducibility note

Unlike the D-037 validator — which asserts that every worktree change begins with
`docs/phase-1-ui-reference-design/`, and therefore cannot re-run clean once durable
root records are updated in the same slice — this validator allows the documentation
tree plus the durable root records, while separately asserting that no application,
dependency-lock, migration, or `.glb` file changed. The documentation-only intent is
preserved and the run stays reproducible in place.

**Correction, 2026-09-06.** The first version of this check enumerated only this
package plus a fixed list of root records. It failed the moment two other authorized
documentation slices appeared in the worktree — `CHANGE_REQUEST_CR-002.md` and the
`HSD-ASSET-001` provenance record — which is the same defect class diagnosed one
level up in the D-037 validator: a check that assumes it is the only work in flight.
Two changes were made. The allowed set is now the documentation tree rather than an
enumerated list, and the application/dependency/migration assertion is evaluated over
**every** changed path instead of only the paths the first check had already
rejected, which is the assertion that actually carries safety.

**The freeze hash changed in this slice, and that is the correct outcome.**
`UI_REFERENCE_PRODUCTION_CONTRACT.md` is one of the nine freeze files and it gained
the D-045 supersession block in §0.1, the record of three unreviewed producer
remediations, and the `stream_id` column definition in §5.2. The package hash is
therefore now:

```
FREEZE_SHA256=4464F6C44C11E7A00C4F007C3112840C6087CB3C1321B86ED5842B9100CC50CE
```

The prior value `E3786F14…C08D` describes the pre-D-045 package. It is historical,
not wrong; every ledger citation of it must be re-pointed at the new value rather
than deleted, so the approval target the founder was previously shown remains
identifiable. The validator and this report stay outside the freeze set, for the same
reason as before: a report must not be able to mutate the package it reports on.

## Further limitations introduced by this slice

6. **The `stream_disposition` column is inert and unadjudicated.** See above. It is
   reported, not failed.
7. **`A-14` proves an obligation set exists, not that it is met.** `evidence-manifest.csv`
   does not exist, because no batch has run and B01 is held at
   `future_not_authorized` under gate G-4. Every per-stream obligation is currently
   unmet, and the assertion that passes is that **all** of those unmet obligations are
   explained by held authorization. The moment a batch runs, the same assertion starts
   demanding real manifest rows. This is the R-024 lesson applied a second time: an
   assertion about an absent input must state the condition under which the absence is
   legitimate, or it silently becomes permanent.
8. **A guard's scope is part of its claim.** `A-15` and `A-16` scan 56 files across
   three packages. Nothing outside those three packages is checked — the root ledgers,
   `docs/active/`, and `docs/software-definition/` are not swept for stream vocabulary,
   even though `Hengshi_Design_SRS_v3.md` and `3D_Mega_Menu_Style_Guide_v2.md` were
   both amended in this slice. Recorded rather than widened, because widening the scope
   is a change to what the package claims and belongs to a reviewer.
9. **No independent review has occurred.** Three producer remediations — D-042, D-043,
   and D-045 — have now been made against the design package since the last independent
   design and accessibility reviews, and **all three passed every assertion in force at
   the time.** Two prior rounds of independent review converged on defects that no
   passing assertion could see. MA-029 remains `awaiting_human` and **R-035 cannot be
   closed by the producer.**

## Non-claims

This report records a passing deterministic validation of a documentation package.
It is not an approval, not an independent review, not a provider capability
statement, and not authorization for any external write.
