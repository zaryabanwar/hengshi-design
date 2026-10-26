# React lint policy proposal — independent bounded review

Date: 2026-10-05. Reviewer: `/root/review_lint_policy_v1`, independent of producer.
Verdict: **PASS for proposal consistency; no actionable findings.** Task: DOING.
This receipt is neither founder approval nor production compatibility/security proof.

## Scope and exact identities

Reviewed only the 53 added lines at `refresh-evidence-2026-10-04.md:45–97`
and the React lint policy row at `MANUAL_ACTIONS.md:19`. Removing those additions
exactly reproduces the retained before texts; no earlier body was revised.
The manual index remains 48 lines. Existing historical receipts retain their scopes.

The [frozen manifest](../../../output/research/react-lint-policy-decision-2026-10-05/review-inputs.json)
retains all 27 input paths, SHA-256 values and byte sizes, independently matched
before and after review. Its hash is `245447b077de9c9f3e979603b01dc8d96b1885269bccc769ec0478af3acc23bd`.

| Principal input | SHA-256 |
|---|---|
| Current refresh evidence and retained reviewed copy | `ccaf5a4b69a4327f47f8649ea723329ab1cb338e2eded24bfaf8dfd262687eeb` |
| Current manual index and retained reviewed copy | `c41e3a0a9848f01d6d3b2d06f0d29ae8c042c12685c210e27c3e32768f619813` |
| Registry observations | `f4959269ec5f1dfa6d75de9058f976763b261f617c7a921f9ac441fb554e8337` |
| Retained refresh before | `73456246ea0b492d4d414ff1ff3a69a056f4a9867cd0182c09cf8dcf8d0e8d50` |
| Retained manual index before | `3ed92717cf8d6e69d0287f1ae01cc3d9e4a8bb6abe7b7df5d8f2187a0fc2893e` |

## Findings and inspection

Current AGENTS, constitution, D-069 and active task boundaries require stable whole-graph selection and explicit founder exception authority. The proposal leaves that rule controlling and presents a decision rather than an approved amendment. Exact `gensync` 1.0.0-beta.2 is the sole proposed exception, restricted to isolated development/CI lint execution; it grants no general Babel/build-tool, other-prerelease, TypeScript parity, security or peer waiver. Separate candidate adoption, full graph, MA-013 and Phase 1 acceptance remain open.

Inspected the three retained official version responses and their observation projections. Fresh independent read-only official registry queries confirmed plugin 7.1.1's Babel `^7.24.4`, Babel 7.29.7's gensync `^1.0.0-beta.2`, and gensync latest beta.2 with only 0.1.0 non-prerelease. The earlier [range review](react-lint-stable-path-recheck-2026-10-04.md) supplies the broader compatible-Babel analysis and rejection of the published stable gensync; it is supporting reviewed evidence, not freshly re-executed here.

The [official React preset](https://react.dev/reference/eslint-plugin-react-hooks) independently confirms compiler diagnostics without compiler adoption. The [native conformance](native-hook-conformance-v1-2026-10-05.md) and [fresh recheck](react-lint-stable-recheck-v1-2026-10-05.md) receipts support the proposal's refusal to treat existing alias/custom-Effect misses or experimental compiler rules as an equivalent stable replacement. No new upstream/native checker parity claim is made.

The proposed gates require real preset and compiler/API/editor/build evidence, deterministic candidate locks, integrity/provenance/licence/advisory review, actual reachability and deployed-artifact exclusion beyond a devDependency label, no visitor/confidential data or production credentials, pre-wave and quarterly rechecks, and expiry on 2027-01-05. Failure rejects the candidate; expiry holds selection pending renewal or a proven stable graph. The strict-stability alternative holds only affected graph selection and preserves other safe definition work. Neither alternative authorizes an application change or release.

## Limits

Only this receipt was written. All 13 protected guard inputs remain at their packet identities. Metadata, byte-preservation and proposal inspection are artifact observations, not application tests or runtime security certification. No package installation/execution, lint/compiler/editor/build/browser test, advisory clearance, signature/attestation verification, source-build provenance, reachability/artifact exclusion or rollback exercise was performed in this review. Context7 producer usage was not independently replayed; official React guidance was checked directly. No policy, source, dependency, lock, model, credential, branch, commit, push or deployment was changed. The earlier reviewer credit error supplies no successful verdict; this receipt establishes only its own bounded review.
