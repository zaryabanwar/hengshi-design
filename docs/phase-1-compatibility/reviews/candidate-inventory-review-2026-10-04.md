# Candidate advisory and inventory evidence review — v1

Date: 2026-10-04. Reviewer: independent agent `review_candidate_inventory_v1`.
Review verdict: **PASS** within the scope below. Task state: DOING; uncommitted.
Findings: 0 Critical, 0 High, 0 Medium, 0 Low.

## Scope and authority

This review assesses only the newly added “Candidate advisory scan and pre-build
inventory” section at `refresh-evidence-2026-10-04.md:269–320`, its corresponding
README paragraph at `README.md:53–59`, and the exact raw inputs listed below.
The remainder of both documents is supporting context, not a newly approved
compatibility, lint, archive, licence or runtime study. Root AGENTS, constitution,
charter, decisions, state, software-definition entry point and task authority were
read. D-069 requires a complete compatible stable graph and preserves factual
technical versions; this narrow review cannot select that graph or close MA-013.

The earlier errored 61-input review still has no verdict. This receipt neither
supersedes it nor extends any earlier review to later or unlisted evidence.
The producer must keep the scope distinction when updating navigation/status.

## Independently inspected evidence

| Subject | Independent observation and assessment |
|---|---|
| Advisory result | Raw report parses, has no error, contains an empty vulnerability map and zero counts at every severity. Its dependency metadata totals 302. The receipt records exit 0, npm 11.11.1/Node v24.14.0, explicit dev/optional/peer inclusion, scripts disabled, public npm registry and no `fix`. Report, manifest and lock hashes match the receipt. Empty stderr is independently confirmed. This supports a dated known-advisory observation, not a new scan or universal absence of risk. |
| Inventory format and scope | Raw output declares CycloneDX 1.5, document version 1, npm CLI 11.11.1 and the `pre-build` lifecycle. It contains 300 components and 301 dependency records including the root. Parsing and reference correspondence do not establish complete CycloneDX schema conformance. Format 1.5 is a technical identifier, not a later product version. |
| Identity correspondence | Independently derived actual package names from each lock entry’s `name`, or from its node_modules path when absent, then matched exact actual-name/version identities to component `bom-ref`. All 302 lock occurrences match exactly one component; all 302 crosswalk rows have distinct paths and agree with the independently derived identity, version, declared integrity and match count. All 300 component refs and 301 dependency refs are distinct, and every emitted dependency ref/edge resolves. This does not prove path/context equivalence or completeness of dependency-edge semantics. |
| Deduplication | Only `eslint-visitor-keys@5.0.1` has multiple lock occurrences: three paths, with the same declared SHA-512 integrity. Installed generator source uses actual package name/version as its deduplication key and retains the first matching node. The producer correctly avoids treating this as physical-path or dependency-context equivalence. |
| TypeScript aliases | Display names `@typescript/native`, `@typescript/old` and `typescript` map respectively to actual `typescript@7.0.2`, `typescript@6.0.3` and `@typescript/typescript6@6.0.2`. Their emitted `bom-ref` and npm PURLs retain those actual identities. These are accurate dependency identifiers, not v1 product naming violations. |
| Declared integrity | Independently converted every present lock SRI digest to its algorithm/hex representation and compared it to the matched component hash; no mismatch. The six components without hashes are precisely the recorded WASI bundled identities. Declared digest correspondence is not verification of installed or published archive bytes. |
| Licence omissions | Exactly GSAP 3.15.0 and webgl-constants 1.1.1 omit emitted licence declarations. The lock contains a custom GSAP licence string and no WebGL licence field; installed generator parses SPDX expressions and omits unparsed values. The section preserves prior WebGL archive evidence, GSAP/full-graph review and bundled-notice gaps rather than claiming missing output means unlicensed or legally cleared. Archive notices and byte comparisons were supporting context, not independently re-executed in this review. |
| Analysis corrections | Receipt/crosswalk explicitly preserve the initial empty-root-key parsing issue, unsupported path-property assumption and grouping correction. Raw npm output hashes agree with their receipts. Final output corresponds to the corrected 302/300 identity analysis; no claim of concealed/raw-output regeneration is needed. |
| Protected inputs | Recomputed all five protected application manifest/lock/requirements hashes read-only. Each matches `protected-input-hashes.json`; values are listed below. This verifies current baseline correspondence, not every application/source/runtime state. |
| Limits and status | New section and README keep the candidate unselected; deny installed-content, source-build, licence-clearance, full-product graph and runtime proof; retain complete-graph review and MA-013. Their producer/unreviewed wording was accurate at commission. This PASS covers only the listed evidence claims and does not grant founder acceptance, application changes, dependency installation or release readiness. |

Duplicate lock paths are:

- `node_modules/@typescript-eslint/visitor-keys/node_modules/eslint-visitor-keys`
- `node_modules/eslint/node_modules/eslint-visitor-keys`
- `node_modules/espree/node_modules/eslint-visitor-keys`

The six omitted component hashes are `@emnapi/core@1.11.1`,
`@emnapi/runtime@1.11.1`, `@emnapi/wasi-threads@1.2.2`,
`@napi-rs/wasm-runtime@1.1.4`, `@tybys/wasm-util@0.10.2` and `tslib@2.8.1`.

## Exact commissioned input hashes

SHA-256 values below were independently computed on current bytes. Raw paths
are relative to `output/research/compatibility-resolution-2026-10-04/` unless
otherwise specified. A later edit to a listed input is outside this verdict.

| Input | SHA-256 |
|---|---|
| `docs/phase-1-compatibility/refresh-evidence-2026-10-04.md` | `091FE4FE0F5A6FD0E878705D455A6ECF29EE399756CA35295F251D195592DBD4` |
| `docs/phase-1-compatibility/README.md` | `16E456EA86DF70A988ECD4D5BE14A016490910E98A9CC0511511A52AD590C306` |
| `native-lint-audit-report.json` | `59E3AA5EB03E6E7954B32505A8B8348BB369C13C0C5960E22D36216B3E35AC91` |
| `native-lint-audit-receipt.json` | `4A820466F9CF03A07B98C284E37428CE99435412860B1DBBE29779B7AD03C23A` |
| `native-lint-audit-stderr.txt` | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `native-lint-candidate-sbom.cdx.json` | `59AF17D89CAE44938495C91535CC111919904A6FCA2E934A3A54A59A52973184` |
| `native-lint-sbom-receipt.json` | `EA78A856B87410105A9924A9E2ABCBD070354B80717AF9D1CF32C31531000DF5` |
| `native-lint-sbom-stderr.txt` | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `native-lint-sbom-crosswalk.json` | `0924988E33ADE0B8531642201FA0A4493D6E450D458EE91262B3757484239246` |
| `native-lint-probe/package.json` | `F1ECB8D6083BACB65684DEF851C69A9066618534DDFC62B088FD7242E29EB69E` |
| `native-lint-probe/package-lock.json` | `DA45DD6CB7CEE7834FC5985B6595C2111780EE24D7CF87D1BDAF1749BE3F37AB` |
| `protected-input-hashes.json` | `8F15A53BC1BF2C0CB92F536624E955B06725BC31B5BFF3007D8B2729527A0661` |

## Protected application baselines, recomputed

| Repository input | Actual SHA-256, matching preserved baseline |
|---|---|
| `package.json` | `A07F9F12C83736625D621781A1B30C8430452EF7E698FA626902CF16CEF7946B` |
| `package-lock.json` | `D2DA4D7206344BA45645D7BAFE4EC692BB738EA0C1C98C2680522688B5733908` |
| `apps/web/package.json` | `83E4178348EC081922DD3D53D00C51446B655091D056EC09DDE52A2496B04E2A` |
| `apps/web/package-lock.json` | `35486FB012489DE4C3B363198304A25F44A0396707DB328190D7E056C06D416D` |
| `apps/api/requirements.txt` | `B99F98E119CB6653F38B19D1EE83CC7F33D92A699083645CA19369A8912E89BD` |

## Primary documentation and installed-source reconciliation

Context7 resolved `/npm/cli` and was queried for lock-only SBOM scope and filtering.
The official [audit](https://docs.npmjs.com/cli/v11/commands/npm-audit/) and
[SBOM](https://docs.npmjs.com/cli/v11/commands/npm-sbom/) pages were inspected
2026-10-04. They support separating advisory reporting from remediation and
lock-derived inventory from installed contents. The web pages currently identify
11.21.0 rather than this host’s 11.11.1; Context7 includes latest-branch source.
Their examples cannot substitute for the exact installed generator behavior.

Read-only source inspection confirmed actual-name/version deduplication,
alias-derived PURLs, SPDX parsing, declared digest conversion, pre-build lifecycle
and absence of package-path properties. Source SHA-256 values:

- `C:/nvm4w/nodejs/node_modules/npm/lib/utils/sbom-cyclonedx.js`:
  `DEAA645951D410F9DEFF9674B8CE031989910FFD223F99192E6BD70D4EC52550`
- `C:/nvm4w/nodejs/node_modules/npm/lib/commands/sbom.js`:
  `88EE9041C48F325A33832E06DA70D5D06B015465287DB3F088FA4792F0AC0EB0`

No advisory endpoint/fallback behavior is certified from cross-version guidance.
No npm scan repeat, package install/fix, candidate code execution, application or
model change, credential/configuration change, external write, commit or push was
performed. Only this review report was written. Full runtime, supply-chain,
licence, backend/assets/tooling graph and compatibility acceptance remain open.
