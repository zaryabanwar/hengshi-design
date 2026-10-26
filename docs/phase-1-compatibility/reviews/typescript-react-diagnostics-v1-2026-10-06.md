# React declaration diagnostics — independent v1 review

Date: 2026-10-06. Reviewer: `/root/review_lint_policy_v1`, independent of producer.
Verdict: **PASS for bounded evidence accuracy; no actionable findings.** Task: DOING.
Initial review; no correction cycle consumed. At most two normal revisions apply.

## Scope and exact identities

Reviewed only the final React declaration sections added to the compatibility
README and refresh evidence. Their 10-line/51-line additions preserve complete
predecessor byte prefixes; both retained reviewed snapshots match current files.
Earlier reviews remain bounded to their own inputs; this is no lint-policy adoption.

The [138-input manifest](../../../output/research/typescript-react-parity-2026-10-06/review-inputs.json)
has SHA-256 `2cc11906cf4f39b80c02a729bf65b18a72660d8b807bb6a11ffb5509c10d6b28`.
All listed hashes and all 15 protection guards independently match before/after review.
The manifest retains complete source, archive, fixture, command and raw-output identities.

| Principal input | SHA-256 |
|---|---|
| Current README | `61554b7f8e501846a85cc1c888eaaf8ca0d8c5c5dd9bdc786c3bdc4bd93930b3` |
| Current refresh evidence | `b859d1aefe32e36401b77c9e49625de5f6b6cfca7c3a7f3a9b1a9b14530379eb` |
| README predecessor | `69a58432ea278f7429a37597edd8ffe970b716cac8f16dc1eebbbcb8786c158a` |
| Refresh predecessor | `9d0a629093761bafe3f7f4030a1e2c2f8b08639d7295204d43ec51fe3dc71a8b` |
| Observations | `c20308968e92ad1044a6df988142d2d86ffe5cb0bb91797cf7194c28eec04b9a` |
| Declaration package observations | `21e9643de5862bde7e44fbf3ae6471c7e6418b729c962caaf6bd79d71f227b3e` |
| Read-only API probe | `713c1fcce2b2ba982e4de426b63fe7ec41104e09489aa5918595514417a7835a` |
| Read-only range/source probe | `8515321971f2b92086e965e902f4d9ae39476c549675573948f3c5adc99387c3` |

## Independent artifact and executable checks

Independently recomputed each archive's SHA-512 SRI against its saved official registry record, confirming @types/react 19.3.0, @types/react-dom 19.3.0 and csstype 3.2.3. Read all regular archive entries in memory: 16 React, 17 ReactDOM and five csstype files match their unpacked bytes. No extraction, installation or package script was executed by this inspection. This association establishes neither signatures/attestations, source-build provenance, advisory clearance, licences nor a full dependency graph.

Read both stdout-only Node probes and the evidence-writing Python runner before execution; the runner was not rerun. Independently replayed all sixteen fixture CLI commands, the API compiler/in-process language-service probe, the range/source probe and both valid-component source-list commands: twenty existing read-only commands. Used explicit existing Node/API6/native7 entry points, with child environments cleared and only allowlisted OS/runtime paths supplied. Each exit and captured stdout/stderr text, including its own line endings, reproduces its retained record. No ambiguous .bin executable was used; no frozen producer file was overwritten.

| Fixture group | Reproduced diagnostic and acceptance result |
|---|---|
| Valid component and async component | No diagnostics; both CLIs exit 0. |
| Wrong prop; missing prop; wrong numeric-state action | TS2322; TS2741; TS2345. |
| Div ref on button; absent button-event property; string DOM-root container | TS2322; TS2339; TS2345. |

All six invalid cases reject with API6 exit 2 versus native7 exit 1. Raw invalid stdout pairs remain different; only CRLF-to-LF conversion makes their diagnostic text equal. Independently matched all eight saved CLI/API compiler/language-service projections and raw text-comparison claims against the unchanged oracles. No paths, messages, codes or positions were normalized to create diagnostic agreement.

The replayed source/range probe reports API delegate 6.0.3 and actual semver 7.8.5, satisfying ReactDOM's `^19.3.0` React peer and React's `^3.2.2` csstype dependency. Both CLI source listings and the API program contain the same seven isolated fixture/declaration paths. Each compiler's own standard-library files remain distinct and excluded from that correspondence; source coverage is not itself diagnostic or standard-library equivalence.

## Oracle meaning and limits

Inspected all strict/react-jsx/noEmit configurations with skipLibCheck=false, explicit React/DOM types and DOM/ES2022 libraries, plus every TSX fixture. No custom JSX stub or diagnostic-suppression directive appears. [React TypeScript guidance](https://react.dev/learn/typescript) and [TypeScript JSX guidance](https://www.typescriptlang.org/docs/handbook/jsx.html) support typed props/state/events and JSX checking. Pinned React declarations explicitly allow Promise ReactNode component returns; that supports the async typing control without establishing client execution, server-component behavior or a rendering architecture. Invalid setter/event/ref/root fixtures exercise declared type constraints, not Hook-order or application runtime correctness. Numeric diagnostic identifiers are actual boundary observations. Context7's versioned/legacy/main examples are appropriately limited; they are not treated as the current declaration contract or compiler-equivalence proof.

Only this receipt was written; no separate reviewer files were needed. Application and existing candidate manifests/locks, protected models and all other frozen inputs remain unchanged. No new React runtime, emit, lint-rule/preset evaluation, compiler transform, R3F/Drei, Vite/hydration/build/browser, native LSP/editor UI, cross-platform, complete provenance/licence/SBOM, deployed-exclusion, security or full stable graph is established. D-072 remains the named lint-only exception; MA-013, toolchain/adoption and integrated/founder acceptance stay open. No policy, provider/auth, configuration, branch, commit, push or deployment changed. Artifact identities and finite type-tooling probes are separate from product tests/readiness.
