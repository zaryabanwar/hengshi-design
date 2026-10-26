# Frontend and 3D compatibility evidence refresh

Status: DOING. Observed 2026-10-04. Registry/documentation/lock analysis, isolated
resolution and native-lint probes, and targeted published-archive inspection;
no production dependency selected, installed or upgraded. This supplements the
reviewed July inventory without rewriting its frozen evidence or closing MA-013.

## Current React lint stable-path recheck

The [fresh registry observations](../../output/research/compatibility-resolution-2026-10-04/react-lint-recheck-2026-10-04.json)
and their saved registry responses recheck the narrow unresolved lint chain on
2026-10-04. They confirm `eslint-plugin-react-hooks` latest stable tag 7.1.1,
whose `@babel/core` dependency is `^7.24.4`. All 27 published stable Babel versions
satisfying that range declare `gensync: ^1.0.0-beta.2`. The only published stable
gensync version is 0.1.0, which does not satisfy that range. The latest Babel
8.0.6 is outside the hook plugin's declared dependency range.

The [range analysis](../../output/research/compatibility-resolution-2026-10-04/react-lint-recheck-range-analysis.json)
uses the existing npm-bundled node-semver 7.7.4 implementation under its
[official caret/prerelease rules](https://github.com/npm/node-semver#caret-ranges-123-025-004).
It finds no stable gensync choice within any examined compatible Babel dependency
range. This is a concrete published-graph restriction; it is not evidence of a
security vulnerability, failed application behavior or an approved exception.
No resolver rerun, package installation or React/Babel code execution was needed
for this unchanged metadata restriction.

React's [current recommended preset](https://react.dev/reference/eslint-plugin-react-hooks)
still includes compiler diagnostics even without compiling the application.
Removing those checks or using only the candidate's two stable native hook rules
does not establish full preset equivalence. The unselected native topology's
experimental compiler analysis and named missing-rule dispositions remain below.
Neither an EOL downgrade, force/override, custom package rebuild nor a prerelease
exception is selected here. The
[independent recheck review](reviews/react-lint-stable-path-recheck-2026-10-04.md)
records PASS for this narrow section and its listed metadata/range inputs. The
[producer bytes inspected there](../../output/research/contract-review-reference-reconciliation-2026-10-04/refresh-evidence.pre-lint-recheck-reference.md)
are preserved; this later reference addition does not replace the receipt's hash
or extend its verdict to the other studies below. "Stable" in this observation is
published non-prerelease/channel metadata, not full transitive, security or runtime
proof. A future final gensync release might satisfy the caret; none is currently
published within the examined range.

## Sources and scope

[Machine observations](refresh-candidates-2026-10-04.json) preserve package,
registry URL, observed time, publication time, latest candidate, peer ranges,
optional-peer metadata, engines, license label and current web-lock version.
The web lock's SHA-256 identifies the input. Installed tooling reported Node
24.14.0, npm 11.11.1 and global Python 3.14.5; the last is not proof of the API
virtual environment or a backend target. No installed tool establishes cloud GA.

Context7 resolved React Three Fiber; its main repository result exposed a v10
branch, so stable guidance was queried using
`/websites/r3f_pmnd_rs_getting-started_introduction`. The official
[introduction](https://r3f.docs.pmnd.rs/getting-started/introduction) agrees that
Fiber 8 pairs with React 18 and Fiber 9 with React 19; it identifies v10 as alpha.
WebGPU/alpha documentation is not selected by availability in a search result.

Registry observations came directly from `https://registry.npmjs.org/`, not an
installed version or search snippet. A stable-looking latest tag is a candidate,
not proof of security, provenance, transitive stability or clean-install behavior.

## Observed candidates, not locks

| Family | Current web lock | Registry latest observed |
|---|---|---|
| React / React DOM | 18.3.1 / 18.3.1 | 19.3.0 / 19.3.0 |
| Fiber / Drei / Three | 8.18.0 / 9.122.0 / 0.160.1 | 9.8.1 / 10.7.9 / 0.186.1 |
| Vite / React plugin | 5.4.21 / 4.7.0 | 8.3.2 / 6.1.1 |
| Tailwind | 3.4.19 | 4.3.3 |
| TypeScript | 5.9.3 | 7.0.2 |
| Zustand / React Router DOM | 4.5.7 / 6.30.3 | 5.0.15 / 7.18.4 |
| GSAP | 3.14.2 | 3.15.0 |

These twelve rows do not claim a complete production compatibility graph. React
types, Three types, Tailwind integration packages, compiler/transitive binaries,
QA tools, backend, database, Blender, CI and Azure/provider APIs still need dated
coupling evidence, supply-chain/security review and approved reproducible locks.

## Isolated strict resolution, 2026-10-04

The current web manifest and its existing dependency families were used to construct
two disposable studies under
[`output/research/compatibility-resolution-2026-10-04/`](../../output/research/compatibility-resolution-2026-10-04/).
Fresh official npm `/latest` metadata covers the manifest's runtime/dev packages,
Three types, the Tailwind Vite adapter and the TypeScript API compatibility package.
No package code was installed or executed. The studies use the observed Node
24.14.0/npm 11.11.1 host; they do not select that runtime as the latest production
target or settle every alternative package topology.

[npm's install documentation](https://docs.npmjs.com/cli/v11/commands/npm-install/)
defines lock-only resolution and strict peer handling. Both studies ran:

```powershell
npm.cmd install --package-lock-only --ignore-scripts --strict-peer-deps --engine-strict --no-audit --no-fund --registry=https://registry.npmjs.org/ --loglevel=error
```

| Study | Observed result | Meaning |
|---|---|---|
| Independently latest direct versions | Exit 1, ERESOLVE: TypeScript 7.0.2 conflicts with parser 8.71.0's `>=4.8.4 <6.1.0` peer. | The all-latest list is not a resolvable set. No force/legacy peer override was used. |
| TypeScript 7 compiler plus TypeScript 6 API aliases | Exit 0; isolated lock generated; no `node_modules` created. | The declared graph resolves on this host. This is not import, compiler, lint, build, browser or runtime proof. |

The second study follows
[Microsoft's released TypeScript 7 guidance](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/):
alias `typescript` to `@typescript/typescript6` 6.0.2 for API consumers and
`@typescript/native` to TypeScript 7.0.2 for the `tsc` compiler. The current
[typescript-eslint support range](https://typescript-eslint.io/users/dependency-versions/)
agrees with the observed parser metadata. Context7 resolved
`/websites/typescript-eslint_io` and `/microsoft/typescript`; its snippets included
older/preview repository material, so the release article and registry metadata
govern this dated observation. Neither preview native packages nor unstable APIs
were added to the study.

**Stable-channel gate does not pass.** The resolved lint chain is
`eslint-plugin-react-hooks` 7.1.1 -> `@babel/core` 7.29.7 -> `gensync`
1.0.0-beta.2. Official registry metadata lists `gensync` 0.1.0 as its only
non-prerelease version; it does not satisfy Babel's `^1.0.0-beta.2` dependency.
A root package's stable version or npm's successful resolution cannot waive the
whole-graph stable-only rule. Do not silently force the older gensync, delete hook
validation, relabel beta bytes or accept this as a production lock. A supported
stable lint path or an explicit reviewed compatibility decision is still required.

The six nested WASI records without individual registry/integrity fields are
marked `inBundle` under the integrity-pinned `@tailwindcss/oxide-wasm32-wasi`
4.3.3 tarball. They are not six observed external non-registry downloads.
Their byte/provenance/license verification remains supply-chain work; the public
lock metadata alone does not perform it. `webgl-constants` lacks a license field
in this lock. The later targeted inspection below supplements this initial
metadata observation; it does not approve the full supply chain or selection.

Raw inputs, command outputs/exit codes, the unselected lock and source-channel
checks are linked by [the resolution analysis](../../output/research/compatibility-resolution-2026-10-04/resolution-analysis.json).
Protected root/web manifests and existing locks plus API requirements have matching
before/after SHA-256 values. No application tests ran. The prior independent refresh
review covers its older recorded hashes, not this added study; independent review
of these new findings remains TODO under the current reviewer-capacity hold.

### Stable React-lint alternative investigation

An additional unselected study evaluates the lint topology rather than forcing
the beta dependency or dropping hook-order validation. Context7 resolved React
reference documentation and `/websites/oxc_rs_guide_usage`; registry metadata,
published package sources and current official pages govern the observations.

The repository manifests declare the old hook plugin, but the inspected repository
has no ESLint configuration file or lint script. A dependency declaration is not
proof of active lint enforcement. The prototype's known fatal hook-order defect
still needs its separately authorized stabilization and reproducing application
test; no file in the application was repaired by this investigation.

| Path inspected | Evidence | Disposition |
|---|---|---|
| Official hook plugin 6.x/7.x | Inspected stable metadata uses Babel core `^7.24.4`; all 27 inspected stable Babel 7 releases in that range declare gensync `^1.0.0-beta.2`. | Choosing another inspected Babel patch does not remove the prerelease requirement. |
| Official hook plugin 5.2.0 | Integrity-verified published source exports only `rules-of-hooks`/`exhaustive-deps`; its peer declaration ends at ESLint 9 and its Effect Event identifier helper returns false. | Not a substitute for modern React coverage. [ESLint's current support policy](https://eslint.org/version-support/) records ESLint 9 EOL on 2026-08-06; its registry maintenance tag cannot override that policy. No EOL downgrade selected. |
| ESLint/TypeScript graph plus Oxlint 1.86.0 native React rules | The retained lock has 303 package records and no observed prerelease versions; its original resolver options were not retained. The separate strict recheck below exits 0 and reproduces identical lock bytes. The [official Oxlint release](https://github.com/oxc-project/oxc/releases/tag/oxlint_v1.86.0) is non-draft/non-prerelease. | Candidate topology only: the study replaces the hook-plugin dependency with Oxlint while retaining ESLint 10 and TypeScript ESLint. Application dependencies remain untouched. |

#### Recorded strict resolver correction

The [initial native-lint review](reviews/native-react-lint-evidence-review-2026-10-04.md)
reproduces the actual checker diagnostics and package-byte correspondence, but
records REVISE on NATIVE-LINT-MED-001: the original resolver output/exit does not
identify its command options. Its
[inspected producer bytes](../../output/research/contract-review-reference-reconciliation-2026-10-04/refresh-evidence.pre-native-lint-review-correction.md)
are preserved. The original study, lock and raw diagnostics remain unchanged;
this correction does not retroactively supply the original command.

A new [recheck script](../../output/research/compatibility-resolution-2026-10-04/recheck_native_resolution.py)
starts from the same pinned direct-dependency manifest in a separate fresh folder,
without an input lock or installed packages. Its
[receipt](../../output/research/compatibility-resolution-2026-10-04/native-lint-strict-resolution-recheck/receipt.json)
records argv, working directory, Node v24.14.0/npm 11.11.1 observations, timestamps,
input/output hashes and exit 0. The command explicitly enables strict peer and
engine checks, disables legacy peer resolution and force, limits work to the lock,
disables scripts, and includes dev/optional/peer dependencies. Empty explicit
user/global npm config files and child-only removal of npm-config environment
options isolate this observation; machine settings and credentials are unchanged.

The fresh result has the same 303 records, zero observed prerelease versions and
byte-identical lock SHA256 `da45dd6cb7cee7834fc5985b6595c2111780ee24d7cf87d1bdaf1749be3f37ab`.
There are zero package-record differences. All ten preserved application/source
and original study inputs match before/after; the copied manifest is unchanged
and no `node_modules` exists in the recheck. Registry metadata and one Tailwind
WASI archive were fetched to obtain bundled-package inventory; the
[archive-fetch observations](../../output/research/compatibility-resolution-2026-10-04/native-lint-strict-resolution-recheck/archive-fetch-observations.json)
identify the exact npm debug log and successful tarball URL. This was not metadata-
only HTTP traffic. No application dependency was changed or installed, and no
package/lifecycle, compiler, build or browser run occurred.
The recorded host versions are inspection tools, not a selected production matrix.

[Official npm install](https://docs.npmjs.com/cli/v11/commands/npm-install/) and
[configuration](https://docs.npmjs.com/cli/v11/using-npm/config/) documentation,
Context7 `/npm/cli` and the exact installed npm 11.11.1 config definitions were
checked 2026-10-04. The live docs describe the evolving npm 11 line; installed
source governs this run's exact option behavior and has its hash in the receipt.
This new evidence awaits the bounded correction review. It does not select the
candidate, establish full lint coverage, prove runtime compatibility or clear
licences/provenance. Earlier receipts retain their listed inputs and scopes.

The resolver created no `node_modules`. For a separate executable probe, only the
published Oxlint JS package and its Windows x64 native binding were unpacked under
the study's `tool/node_modules`, after matching registry SHA-512 integrity. No
install/lifecycle script ran and no application package was installed. Native
package size is about 13.3 MB unpacked; the probe runs on Node 24.14.0. This is
Windows tooling evidence, not Linux, full-build or browser-runtime proof.

The CLI probe explicitly enables only `react/rules-of-hooks` and
`react/exhaustive-deps`, disables other rule categories and uses a JSON config.
Actual diagnostics, rather than exit codes alone, were inspected. Eight synthetic
cases match the independent oracle from React's [hook rules](https://react.dev/reference/eslint-plugin-react-hooks/lints/rules-of-hooks)
and [Effect Event reference](https://react.dev/reference/react/useEffectEvent):

- Valid top-level hooks accepted; a hook after a conditional return rejected.
- A missing Effect dependency rejected; conditional `use` accepted.
- Valid Effect Event use accepted; an Effect Event in dependencies rejected.
- An Effect Event invoked during render or passed as a click handler rejected.

This is actual checker behavior evidence at its CLI boundary, not a documentation
test or an application regression suite. It does not prove every alias/custom-hook
case, the complete React recommended preset, TypeScript/project configuration,
editor/CI integration or the production compatibility graph. React's [current
plugin reference](https://react.dev/reference/eslint-plugin-react-hooks) includes
additional compiler diagnostics even without adopting the compiler; the native
candidate's equivalence to that entire set is not established. The [Oxlint plugin
documentation](https://oxc.rs/docs/guide/usage/linter/plugins.html) calls its native
compiler-analysis rules experimental and off by default. They were not enabled
and cannot become production requirements under the stable-only policy.

Raw metadata, source observations, isolated input/lock/exit, package provenance
and all diagnostic outputs are indexed by
[native-lint-study-analysis.json](../../output/research/compatibility-resolution-2026-10-04/native-lint-study-analysis.json)
and [native-lint-behavior-probe.json](../../output/research/compatibility-resolution-2026-10-04/native-lint-behavior-probe.json).
The original beta-bearing study remains evidence, not an accepted lock. The native
candidate must still define its complete required rule/config coverage, pass the
rest of the coupled toolchain/platform and supply-chain checks, receive independent
review and join founder compatibility acceptance before application adoption.
Protected package-input hashes still match; no application tests ran. This later
study is not covered by any prior refresh review hash.

### Protected-source check and required lint coverage

The same two explicit native rules were run read-only against three current World
source files. This is source-lint evidence, not browser execution or a regression
test of the application:

| Current source | Observed checker result | Interpretation |
|---|---|---|
| `apps/web/src/world/WorldHUD.tsx:44–55` | `rules-of-hooks` rejects `useMemo` at line 48 after the conditional return at lines 44–45. | Corroborates R-003's current source defect; entering the World can change the component's hook sequence. The candidate catches this actual project pattern. |
| `apps/web/src/world/ExteriorScene.tsx:138/193` | `exhaustive-deps` reports missing `applyKeyframe` in the Effect dependencies. | A separate diagnostic requiring lifecycle/closure analysis before any fix. Blindly adding a recreated function could change animation behavior. |
| `apps/web/src/world/WorldCanvas.tsx` | No diagnostics under these two rules. | Not a component/runtime, lifecycle or full-lint acceptance result. |

Each file's before/after SHA-256 matches in
[native-lint-protected-world-inspection.json](../../output/research/compatibility-resolution-2026-10-04/native-lint-protected-world-inspection.json).
No automatic fix, suppression or application edit was performed. R-003 remains
open; a later authorized stabilization must reproduce the entry/inside transition
at the actual React boundary and verify the fix before modernization.

PROPOSED production configuration obligations for this candidate, still subject to
complete graph/config review and acceptance:

| Coverage | Required configuration/evidence |
|---|---|
| Core JavaScript and TypeScript | Retain the supported ESLint/TypeScript ESLint path; select and lock its reviewed recommended configuration and exact parser/API coupling. The native probe cannot replace compiler/type checking or disable these checks. |
| React hook order and Effect dependencies | Explicitly enable the two inspected stable native rules as errors. Include hooks after early returns, custom/import aliases, modern `use` and Effect Event restrictions in conformance evidence. Eight fixtures cover only the recorded subset. |
| React refresh | Retain the existing refresh-plugin family; verify the reviewed Vite/export configuration against allowed and invalid component exports. No actual refresh-rule probe is claimed here. |
| Additional React recommendations | Inventory the current official plugin's broader recommended diagnostics and their dispositions before selecting the topology. The two stable hook rules are not equivalent to the entire preset; no experimental native compiler rule may become a production requirement. |
| Source and execution scope | Cover all owned application TS/TSX entry points, components, stores and World/admin code. Exclusions must identify generated/vendor/artifact paths; no blanket World or admin exclusion and no new inline suppressions to hide failures. |
| CLI, editor and CI | Bind the reviewed config and exact tool graph; mandatory diagnostics must produce a failing process result. Verify config discovery, file coverage and editor/CI behavior with actual inputs. No CI change or executable production lint script is authorized by this table. |
| Safe fixes | Require an approved bounded source change and a reproducing behavior test; avoid automatic dependency-array rewrites or treating a clean lint output as a safe animation/session fix. |

### Official recommended-rule inventory: producer evidence

Checked 2026-10-04 using Context7 `/websites/oxc_rs_guide_usage`, the official
[React recommended preset](https://react.dev/reference/eslint-plugin-react-hooks),
the exact installed Oxlint 1.86.0 `--rules --format json` inventory and official
per-rule pages. This extends the unselected study; no package/config/application
change, experimental-rule execution, new review verdict or production selection.

| Upstream identifiers | Exact candidate observation | Disposition |
|---|---|---|
| `rules-of-hooks`, `exhaustive-deps` | Matching registered identifiers; the earlier eight fixtures exercise only the documented subset | Existing two-rule evidence, not full preset equivalence |
| `error-boundaries`, `globals`, `immutability`, `incompatible-library`, `preserve-manual-memoization`, `purity`, `refs`, `set-state-in-effect`, `set-state-in-render`, `static-components`, `unsupported-syntax`, `use-memo` | Matching identifiers; each official per-rule page identifies React Compiler analysis | Native compiler rules remain excluded from production requirements while experimental |
| `component-hook-factories`, `config`, `gating` | No identical registered React rule identifier in the installed inventory | Missing identifier; do not infer coverage through a renamed/aggregate rule |

Oxlint's [plugin documentation](https://oxc.rs/docs/guide/usage/linter/plugins.html)
explicitly marks its native compiler rules experimental and off by default.
Availability in a stable package or a registered-rule list does not make that
analysis stable or prove enforcement equivalent to the upstream plugin. The
individual [purity](https://oxc.rs/docs/guide/usage/linter/rules/react/purity.html)
and [use-memo](https://oxc.rs/docs/guide/usage/linter/rules/react/use-memo.html)
pages illustrate the compiler attribution; all twelve source URLs and observations
are retained in [the rule inventory](../../output/research/compatibility-resolution-2026-10-04/native-lint-recommended-coverage.json).
Direct HTTP documentation attempts failed and remain recorded; successful web-tool
inspection is separate evidence, not a fabricated successful fetch/hash.

This replaces an unspecified broader-preset gap with named dispositions; it does
not close the gap. Required stable production lint coverage still needs a reviewed
configuration and actual conformance evidence. No coverage waiver, experimental
substitute or upstream dependency downgrade is selected. This new study and edited
document are outside any earlier frozen review verdict; the failed 61-input review
produced no verdict and cannot cover later edits.

The study's `--allow all` plus two denied rules isolates checker behavior. It is
not a production preset and must not be copied as one: doing so would suppress
unexamined core/TypeScript/refresh checks. The synthetic fixture config belongs
only to the isolated study. Required production coverage, full coupled imports/
compiler/build/browser proof and independent review remain open. A lint pass
cannot establish authentication, publication eligibility, privacy, accessible
movement, streaming disposal or booking correctness.

### Targeted published-archive licence inspection

The native-lint candidate's exact `webgl-constants` 1.1.1 and
`@tailwindcss/oxide-wasm32-wasi` 4.3.3 archives were inspected as data. Each archive
matched its recorded SHA-512 integrity. No code from these inspected packages was
executed, and no application manifest, lock or requirement changed. The six WASI
`inBundle` records' names and versions match the actual nested package manifests.
This is stronger than a lock metadata label, but does not verify the source build
or determine which bytes the eventual production build distributes.

| Exact candidate | Actual notice evidence | Remaining qualification |
|---|---|---|
| `webgl-constants` 1.1.1 | The archive contains an MIT licence with Copyright (c) 2019 Tim van Scherpenzeel. Recorded JS/TS source headers separately declare CC0 dedication. | Preserve the actual package notice and source declarations; an absent registry licence field does not make the archive unlicensed, and the source headers do not justify discarding its package notice. |
| `@emnapi/core` 1.11.1, `@emnapi/runtime` 1.11.1, `@emnapi/wasi-threads` 1.2.2 | All three nested MIT licence files are present, with Copyright (c) 2021-present Toyobayashi. | These are the recorded bundled versions, not independently newest substitutions. |
| `tslib` 2.8.1 | Its nested 0BSD licence and Microsoft copyright notice are present. | Retain this separate licence identity in the inventory. |
| `@napi-rs/wasm-runtime` 1.1.4 | Its six direct published files match the parent bundle byte for byte. Both archives omit a licence file; the npm-reported exact source commit's root licence contains two MIT notice blocks, for LongYinan and GitHub. | Preserve both source notice blocks. Matching bytes and `gitHead` are evidence, not cryptographic source-build attestation. |
| `@tybys/wasm-util` 0.10.2 | Its 39 direct published files match the parent bundle byte for byte. Both archives and the recorded exact source root lack a licence file; package metadata declares MIT. | Full copyright/permission notice remains unresolved. Do not invent notice text or assume another bundled package's notice applies. |
| `@tailwindcss/oxide-wasm32-wasi` 4.3.3 parent | Declares MIT; its official `v4.3.3` source tag resolves to a recorded commit whose root licence names Tailwind Labs, Inc. | No npm `gitHead` was reported. The tagged source-to-published-WASM build relationship is not cryptographically verified. |

The pinned [NAPI source licence](https://github.com/napi-rs/napi-rs/blob/d5c3c43b45393f99ba151770f97bd472de533671/LICENSE)
and [Tailwind source licence](https://github.com/tailwindlabs/tailwindcss/blob/c2b24dd15fed1c59dd521bd86082f520c9f5ad0d/LICENSE)
are recorded with their exact text and SHA-256. The wasm-util source README's
phrase “size limit” is not an MIT licence declaration; its substring match was
excluded from licence conclusions. A package-level MIT label alone cannot supply
a missing copyright holder or full notice.

[Targeted licence analysis](../../output/research/compatibility-resolution-2026-10-04/targeted-license-analysis.json)
indexes the archive inventories, actual notice texts, pinned source observations,
direct/bundled byte comparisons and unchanged protected-input hashes. This closes
the specific WebGL missing-field uncertainty and establishes the six bundle
versions and recorded notice locations. The wasm-util notice gap, complete-graph
licence/distribution inventory, final build SBOM, provenance, runtime/platform
checks, independent review and MA-013 acceptance remain open. This added evidence
is outside prior review hashes and does not create a licence/legal or supply-chain
PASS. No maintainer contact or external write was made.

### Candidate advisory scan and pre-build inventory

On 2026-10-04 the installed npm 11.11.1/Node v24.14.0 ran a read-only
`npm audit --package-lock-only --ignore-scripts --include=dev --include=optional
--include=peer --json --registry=https://registry.npmjs.org/ --loglevel=error`
against the isolated native-lint candidate. No `fix` was requested. The
[raw report](../../output/research/compatibility-resolution-2026-10-04/native-lint-audit-report.json)
has no error, exit status 0 and zero reported vulnerabilities at every severity;
it accounts for 302 dependencies. Development and optional scopes were included;
optional counts overlap other categories and must not be added as extra packages.
The [receipt](../../output/research/compatibility-resolution-2026-10-04/native-lint-audit-receipt.json)
records the unchanged candidate manifest/lock hashes, command and report hash.
This is a dated registry advisory observation, not absence of unknown defects,
malware, insecure application behavior or risk in non-npm artifacts. Recheck the
then-selected graph before an approved upgrade/release; this candidate is unselected.

The same unchanged lock produced a [CycloneDX 1.5 inventory](../../output/research/compatibility-resolution-2026-10-04/native-lint-candidate-sbom.cdx.json)
using npm's built-in `sbom --package-lock-only --sbom-format=cyclonedx` with all
three scopes included and scripts disabled. Its declared lifecycle is `pre-build`.
The [inventory receipt](../../output/research/compatibility-resolution-2026-10-04/native-lint-sbom-receipt.json)
and [identity crosswalk](../../output/research/compatibility-resolution-2026-10-04/native-lint-sbom-crosswalk.json)
map all 302 dependency lock occurrences to 300 component identities with no
unmatched identities or unresolved emitted references; the root adds one
dependency record. `eslint-visitor-keys@5.0.1` appears at three lock paths with
the same declared integrity and is deduplicated by the installed generator.
This does not prove physical-path or dependency-context equivalence. TypeScript
aliases retain their actual package/version identity in `bom-ref` and `purl` even
when the display name is the alias. Do not rename their factual technical versions.

Installed generator inspection verifies that this npm version emits no package-path
property and deduplicates by actual package name/version. The crosswalk uses those
identities, rather than assuming the newer documentation's example path property
exists. The receipt records corrected producer parsing/grouping attempts; the raw
npm outputs were not regenerated or changed to conceal those analysis errors.
JSON parsing and reference correspondence are artifact checks, not complete
CycloneDX conformance, installed-file verification or a product build inventory.

The generated inventory omits licence declarations for GSAP and `webgl-constants`
and individual integrity values for the six recorded WASI bundled packages.
An omitted declaration is not proof of no licence: preserve the previously
verified WebGL archive notice and continue exact GSAP terms/full-graph distribution
review. Bundled identities and selected byte comparisons already recorded do not
constitute separate published-archive hashes for every component. No signing,
source-build attestation, licence clearance or final full-product SBOM is claimed.

Context7 `/npm/cli` and official [audit](https://docs.npmjs.com/cli/v11/commands/npm-audit/)
and [SBOM](https://docs.npmjs.com/cli/v11/commands/npm-sbom/) documentation were
checked on that date; exact installed SBOM source was inspected where behavior
differed from newer examples. This evidence remains producer work outside all
prior review hashes and does not select npm/Node or the candidate production graph.
Backend/runtime/assets, full licence/provenance and coupled-platform evidence,
independent review and MA-013 remain open. No application locks or installs changed.

## Couplings and migration obligations

Registry candidate Fiber permits React/DOM `>=19 <19.4`, Drei requires Fiber
`^9.0.0` and React/DOM `^19`, and React DOM requires React `^19.3.0`. Three's
observed candidate meets the advertised minimum ranges. This is a range-level
observation, not a tested renderer/asset/type combination. Optional native Expo
peers do not silently become web requirements. Never create an accepted checkpoint
with React 19 and Fiber 8 or Drei 9.

The candidate React plugin requires Vite `^8.0.0`; their engines require Node
`^20.19.0 || >=22.12.0`. The installed Node version meets that stated range,
but this does not resolve the latest supported Node/npm pair or approve a wave.
[Vite migration guidance](https://vite.dev/guide/migration) describes its changed
build toolchain and browser target. Follow supported migration steps and test
build output, dynamic chunks, source maps and any plugin transforms; do not assume
a direct multi-major upgrade preserves the application.

[Tailwind's upgrade guide](https://tailwindcss.com/docs/upgrade-guide) names
Safari 16.4+, Chrome 111+ and Firefox 128+, and changes CSS/plugin integration.
Its Safari floor aligns with the accepted legacy floor at the documented level;
actual accessibility, tokens, CSS behavior and current evergreen browsers still
need testing. Tailwind remains required. Dedicated Vite or PostCSS integration
and companion package versions must join the graph before selection.

[Fiber's v9 guide](https://r3f.docs.pmnd.rs/tutorials/v9-migration-guide) identifies
React 19 compatibility, Strict Mode and type/renderer changes. Verify lifecycle,
loader cleanup, materials/lighting, scene transitions and HTML/World interaction.
TypeScript 7, Router 7, Zustand 5 and GSAP candidates have no completed migration,
license or advisory assessment in this slice. Their latest tags are not approval.

## Wave and rollback boundary

Stabilize the known fatal prototype defects under the separately approved bounded
contract before upgrades. Keep toolchain, coupled React/renderers/3D, backend,
database and cloud work reversible. A coupled renderer checkpoint must be valid
as a unit even when separate waves test other aspects; no half-upgraded runtime
can be accepted because an isolated package installs.

Before an authorized wave, requery the exact compatibility graph, record current
source/config/runtime/lock hashes and deterministic installation evidence.
Run focused affected tests, then one relevant full suite and browser/visual checks.
Rollback restores the prior coherent runtime/source/config/lock set under its
approved operation and repeats the affected evidence. This document performs no
restore, branch, commit, credential, dependency, schema or deployment operation.

Fresh backend/cloud/QA evidence, complete production graph, final semantic-render
pattern, exact locks, security/SBOM/license review and founder compatibility
acceptance remain required. The active app goal continues beyond this refresh.
