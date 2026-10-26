# Isolated React lint evaluation — independent v1 review

Date: 2026-10-06. Reviewer: `/root/review_lint_policy_v1`, independent of producer.
Verdict: **PASS for bounded evidence accuracy; no actionable findings.** Task: DOING.
This receipt does not accept candidate conformance, security, adoption, MA-013 or Phase 1.

## Exact scope and identities

Reviewed only the new “Founder-approved isolated React lint evaluation” section
and its new compatibility README paragraph. The retained diffs add 61 and 10 lines
respectively; removing them exactly restores both predecessors. Existing D-072
reconciliation and historical studies retain their separate authority/review scopes.

The [frozen manifest](../../../output/research/react-lint-approved-evaluation-2026-10-06/review-inputs.json)
has SHA-256 `b8ccc1f8f83cc614f785d9ecfe4053db8ddc0f0eecc5bec92d41f3dbeaa6c93f`.
All 207 listed hashes independently match before and after inspection/replay.
The manifest retains the complete identity set, including raw results and guards.

| Principal input | SHA-256 |
|---|---|
| Refresh evidence/current reviewed copy | `ade4db0c73bfc1da0a023476d3083d51a499db651d7f2b1b52080f5c8c1117d7` |
| README/current reviewed copy | `f62e38a14291b766116e8a10f5730186bc260c36ed659af017785a048cb28367` |
| Refresh predecessor | `67f4513c2188a47eb52c640c513fbc9b092d29a3378b0065cfa5fca8b22dfe09` |
| README predecessor | `fa669ee53473bf3dc345e77e965e7815487f4c076a9eb70e6f249ecafe1b3657` |
| D-072 decision file | `0290e6bed5d983fa1f2162db72f1a9d3167695ff98c867c88987ee1e2c4bcc99` |
| Candidate lock | `86dd64aae77da6ab9a0d0f7a88338494c15f68620838ffd40140f254b1e9ca2d` |
| Strict guarded observations | `29d10b9f2ae2ead679c3e7bf784bfa237ce5c450cc238a6b7d35779e2de22efa` |
| Published Hook-plugin development source | `d401e94560ab2660e40fe59a3408828b96d78e9929a22358386aa51acbe32e2b` |

## Independent inspection and CLI reproduction

Inspected commands/configurations/fixtures before replay. Directly executed 12 existing read-only ESLint CLI cases and one effective-configuration query, using the recorded Node executable and candidate directory. Each child environment was cleared and received only allowlisted OS/runtime path variables; no inherited provider/auth/npm variables or coverage output variable. No npm, network, installation, lifecycle script, fix, cache or output-file operation ran in these replays.

| Replayed witness | Observed result |
|---|---|
| Valid Hooks, valid custom Effect, valid Hook-shaped alias and valid purity controls | Exit 0; no diagnostics. |
| Bare `useState as state` after early return | Exit 0; semantic violation remains missed. |
| Guarded conditional alias and top-level non-Hook-shaped alias | Exit 1, `no-restricted-syntax`; naming restriction, not alias/dataflow proof. |
| Shared custom Effect missing dependency | Exit 1, `react-hooks/exhaustive-deps` warning; maximum-zero-warning enforcement retained. |
| Invalid rule/config; ignored target with no matching config | Exit 2 naming the missing rule; exit 1 with the ignored-file warning. |
| Impure render; nested component | Exit 1, respectively `react-hooks/purity` and `react-hooks/static-components`. |

All sample exit codes and diagnostic identities/severities reproduce the retained results. Independently matched 48 saved bare/guarded/strict diagnostic projections and three compiler-result projections to their raw CLI JSON. The effective query reproduces saved rules/settings and sixteen active Hook rules. Inspected actual source: `component-hook-factories` maps to the deprecated 7.1.0 rule whose `create()` returns an empty visitor. [React's current list](https://react.dev/reference/eslint-plugin-react-hooks) still names it; source controls this exact package behavior. The producer preserves that mismatch and holds replacement/deprecation disposition rather than claiming universal compiler equivalence.

## Findings and limits

D-072 permits only the named gensync beta in isolated development/CI lint evaluation, with no deployed execution or general Babel/build/prerelease waiver. The producer retains these boundaries, expiry/rechecks/rejection and separate adoption authority. The bare alias invocation is rejected; the built-in [syntax restriction](https://eslint.org/docs/latest/rules/no-restricted-syntax) remains an unselected candidate tested on a finite subset, including a top-level naming control that is not a runtime-order violation. Earlier warning-suppressed commands and the failed first configuration probe remain preserved and are not accepted as final controls.

Independent lock inspection confirms 162 records, only `gensync 1.0.0-beta.2` prerelease and the recorded TypeScript API6/native7 aliases. Seven saved registry observations match their response versions/hashes; parser/plugin 8.71.1 still declare `>=4.8.4 <6.1.0`. Recorded strict resolution/install flags, empty npm configs, lock identity, zero-advisory result and empty signature invalid/missing arrays support the precise observations; these historical operations were not rerun and do not certify safety, complete provenance or licences. Coverage inspection confirms gensync's actual module has 31 positive ranges out of 50 during synthetic linting; no deployed-exclusion proof follows.

Only this receipt was written. All protected package/lock/model identities remain unchanged. This finite guard check is not a whole-repository forensic proof. No application behavior, complete preset/alias semantics, compiler/API/editor/build parity, complete supply-chain/SBOM clearance, deployment exclusion, rollback, full graph or production readiness is established. No application, policy, dependency, lock, model, provider/auth setting, branch, commit, push or deployment was changed. Founder candidate acceptance and all remaining D-072/MA-013/Phase 1 gates remain separate.
