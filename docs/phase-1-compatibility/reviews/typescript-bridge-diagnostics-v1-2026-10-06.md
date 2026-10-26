# TypeScript bridge diagnostics — independent v1 review

Date: 2026-10-06. Reviewer: `/root/review_lint_policy_v1`, independent of producer.
Verdict: **REVISE — one collateral-byte finding.** Task: DOING.
The new diagnostic claims otherwise reproduce within their stated finite limits.

## Exact scope and identities

Reviewed only the appended TypeScript bridge section and new README paragraph,
with retained predecessor/reviewed copies, source, commands, fixtures and raw results.
The [frozen manifest](../../../output/research/typescript-bridge-parity-2026-10-06/review-inputs.json)
has SHA-256 `2562137e7020f565ed7d341c378dafa93fbefd0754bdbf4f08c638adc7e95385`.
All 76 listed input hashes match before and after review; the complete list is retained there.

| Principal input | SHA-256 |
|---|---|
| Current refresh evidence | `517208cb23ab578c6bfdfbf680283b3edbd404fdb4452192ba5ea459efb31953` |
| Current README | `d5105a2055d02d44717efcad2f750473214d7b05bc5dd35387c1b652bd1c0241` |
| Refresh predecessor | `f50a4168ae77ea91e5f8e1e0708c2585c383ccd28cf85c01835536cb3e24758a` |
| README predecessor | `9243f54dbd895f1496bdbc3c7805d7038db7649d34b57f037cdcc043cd7eabed` |
| Observations | `e4d47d0e909661c7badbfe03f214adc0910d238282eee9d74c857654573860a1` |
| Separate comparison | `de434388484b55ac5e2646a36364781ab76d8297b02170edebca811fc79e6628` |
| Read-only API probe | `bb6bda8d191a24c4a093148ba3d873a3719d0e23f03f494f7a3d2d3af87b2bb8` |

## Actionable finding

**[P2] Restore the predecessor newline outside the new README paragraph.** At `docs/phase-1-compatibility/README.md:87`, the existing sentence “Select the latest mutually compatible stable graph across all coupled tools,” changed from CRLF to LF. Removing the eight added lines leaves 25,514 characters versus the predecessor's 25,515. Independently inserting the missing CR immediately before that line's LF exactly restores the entire predecessor; there is no other residual difference. This is an artifact-preservation finding, not a wording, compiler or product-behavior defect. Restore only that byte, preserve this packet, freeze the corrected candidate and re-review its identity/restoration. The 39-line refresh addition already restores its predecessor exactly when removed.

## Independent source and executable checks

Inspected `run-probes.py` without executing it because it writes the frozen evidence. Inspected `api-probe.cjs`, both compiler wrappers, installed npm shims and all five no-emit plain-TypeScript projects before replay. [Microsoft's release guidance](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) supports the side-by-side API/compiler arrangement; exact source delegates the 6.0.2 wrapper to `@typescript/old` 6.0.3, as the existing lock records. Installed `tsc.cmd` points to native7; `tsc6.cmd` points to the API6 wrapper. This is this installation's observed selection, not every installation order/platform.

Independently replayed eleven existing read-only commands: direct API/native versions, both shim versions, the API/in-process-language-service probe, and valid-union/invalid-assignment/invalid-readonly projects on both CLIs. Child environments were cleared and received only allowlisted OS/runtime path variables. Every replay reproduces its own saved stdout/stderr text and exit. Versions are 6.0.3 and 7.0.2. Valid union exits 0 on both; invalid assignment/readonly report TS2322/TS2540 with exits 2 and 1 respectively.

Independently checked all five projects' saved CLI diagnostics and API program/language-service projections against the unchanged oracle: no diagnostics for valid narrowing; TS2322, TS2540, TS2532 and TS2307 for the four invalid cases. [Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html), [readonly object properties](https://www.typescriptlang.org/docs/handbook/2/objects.html) and [unchecked-index guidance](https://www.typescriptlang.org/tsconfig/noUncheckedIndexedAccess.html) support their validity distinctions. Numeric codes are observations at the actual boundaries, not inferred from prose. All four original exact-exit oracles remain false: API6 exits 2, native7 exits 1. Both reject; equal numeric-exit semantics are not established.

The separate comparison preserves raw inequality for every invalid pair and equality only after CRLF-to-LF conversion. No path, position, message or diagnostic-code normalization is needed. This finite diagnostic agreement does not establish general type-system equivalence. The wrapper/delegate distinction, failed exit expectations and unproven editor/build subjects are accurately stated in both additions; D-072's broader conformance/adoption conditions remain open.

## Limits and preservation

Only this receipt was written. All nine protected application/package/lock/model inputs remain unchanged; the candidate lock stays `86dd64aae77da6ab9a0d0f7a88338494c15f68620838ffd40140f254b1e9ca2d`. No evidence-writing runner, install, npm/network, cache, fix, emit or output-file operation ran in the replays. No application, alias, binary, editor/configuration, provider/auth, policy, branch, commit, push or deployment changed. No React-type, native LSP/editor UI, Vite/build/emit, cross-platform, security/provenance/licence, deployed-exclusion, full-graph, MA-013, adoption or founder acceptance follows. The finite input guards are not a whole-repository forensic proof. This is the initial review; no correction cycle has yet been consumed. At most two normal revisions are permitted.

## Correction 1 disposition — 2026-10-06

**PASS after correction 1; the sole P2 finding is resolved.** This consumes correction 1 of the two permitted normal revisions. The initial review above remains verbatim historical evidence.

Correction manifest: `output/research/typescript-bridge-parity-2026-10-06/correction-1/review-inputs.json`, SHA-256 `68cb4a4d72769160abf80a648466057be1069ef66f6bf72e6a0231d00e8bba83`. All 78 input identities matched before this authorized receipt append. Corrected README/current retained copy: `c8b07c0b4dd6475593189271a999080dd8f435b5770bee6cfe39908f4a68992e`.

Independent byte comparison confirms exactly one CR byte inserted before the existing LF at README line 87. Removing that byte exactly reproduces the original reviewed README. Removing the new paragraph from the corrected README exactly reproduces `README.md.before`; no prose, fixture, command, raw result, source, configuration or diagnostic claim changed. The initial receipt body matches the preserved `correction-1/initial-review.md`, SHA-256 `dd11e5d7d8b0d55767d2d135cca62396661b16c811004b55e6473436a9c2f9de`.

After append, all other 77 manifest inputs remain at their frozen hashes, and the receipt's original byte prefix remains identical. Only this authorized disposition is excluded from the unchanged-input assertion. Unchanged executable cases were not rerun. This PASS accepts bounded evidence accuracy and scope preservation only; the earlier unequal exits, finite diagnostic/line-ending observations and all editor/build, security, full-graph, adoption, MA-013 and founder-acceptance limits remain.
