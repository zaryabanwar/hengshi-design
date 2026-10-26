# Compatibility evidence reconciliation — independent v1 review

Date: 2026-10-05. Reviewer: independent agent `/root/review_world_audio_v1`.
Verdict: **REVISE**. Task status: DOING; receipt uncommitted.
Findings: 0 Critical, 0 High, 1 Medium (P2), 0 Low.

## Exact scope and authority

This review assesses the current evidence reconciliation in `README.md`,
`refresh-evidence-2026-10-04.md` and `backend-evidence-2026-10-04.md` against the
frozen resolver, native-checker, targeted-notice and subsequent evidence packet.
It accepts or rejects accuracy and current-authority consistency of those claims;
it does not select a production graph. AGENTS.md, constitution principles V/VII,
current founder instructions, D-068/D-069, PROJECT.md, TASKS.md and the current
software-definition entry control this review. The July compatibility body is
expressly historical/amended context, not a current Azure-only instruction.

Frozen manifest:
`output/research/compatibility-evidence-reconciliation-2026-10-05/review-inputs.json`.
SHA-256: `c879a4577ebb334d110c11b9f1eb53f889345ac0d86f130a25611e1fc483bb06`.
Manifest size: 58,894 bytes. It binds 175 inputs totaling 5,533,223 frozen bytes.
All 175 frozen SHA-256/byte lengths were independently recomputed; each canonical
source was also byte-compared to its frozen copy. All matched, including a final
recheck immediately before receipt creation. The exhaustive identities are below.

The preserved original ledger at input 061 has 61 entries. Independently comparing
its digests to the current source bytes reproduced **58 unchanged and exactly
three amended producer documents**, the three pages named above. This is not a
verdict for the original interrupted session. That session produced none. Its
historical incomplete review is neither retroactively completed nor converted to
PASS; this receipt assesses the current frozen bytes and the explicitly inspected
claims below. Later narrow receipts retain their exact original inputs and limits.

## Actionable finding

**CER-MED-001 — Medium / P2 — Current backend obligations still assume Azure hosting and a production OS.**

Location: `docs/phase-1-compatibility/backend-evidence-2026-10-04.md:177–178`,
with related wording at `:124–126`. The current “Required selection and rollback
evidence” section unconditionally requires “Azure GA and production image/OS
graphs”; the marker paragraph describes “Linux production markers”. D-068
(`DECISIONS.md:804–822`) supersedes exclusive Azure hosting and defers deployment,
provider/cost planning with Azure and AWS as candidates. The constitution
`:236–246` makes the same distinction. The compatibility README's current
`:116–120` already preserves that deferral. No production OS/packaging choice is
established by this Windows resolver observation. The current backend checklist
therefore carries a provider-specific obligation beyond the present approved
selection scope, and its OS language can imply a deployment target is selected.

Required correction: retain actual-target Python support/ABI, JWT crypto, Uvicorn
extras and database/libpq evidence, while making provider GA and production
OS/packaging graph evidence conditional on the later approved target after D-068
planning resumes. Describe this Windows graph as insufficient for any separately
selected production OS/extra graph, rather than fixing Linux as production.
Preserve immutable-artifact/image-digest rules where applicable to the eventual
approved packaging; this finding does not waive those existing release controls.
Explicitly retain Entra staff identity and the separately approved Azure EU
personal/confidential AI data route. Hosting deferral does not remove those
specific Microsoft/AI constraints (`constitution.md:154–160`, D-068:821–822).
No resolver input/result or protected application change is needed to correct it.

Disposition: revise that current authority wording and obtain a bounded correction
review at fresh identities. The factual study results below do not need to be
repeated solely for this wording correction. No broader compatibility exception,
provider replacement or implementation permission follows from this finding.

## Independently inspected claims

| Claim | Independent inspection and assessment |
|---|---|
| All independently newest frontend candidates | Read the exact manifest and raw resolver failure. Exit 1 is ERESOLVE: TypeScript 7.0.2 cannot satisfy parser 8.71.0's `>=4.8.4 <6.1.0` peer; the matching plugin requires that parser. This substantiates the recorded peer failure, not an assertion that every other edge has failed or that a different complete graph is selected. No force/legacy-peer exception is accepted. |
| TypeScript alias bridge | Parsed its exact manifest/313-record lock and exit/output. The `typescript` path has actual package identity `@typescript/typescript6` 6.0.2 and the retained compiler arrangement has distinct factual version identities. The bridge resolves metadata but includes `gensync` 1.0.0-beta.2 through Babel 7.29.7. Independently scanning every lock version reproduced the one prerelease record. Stable-only acceptance therefore remains blocked for this graph; aliasing does not make TypeScript 7 peer-compatible or transform beta into stable. |
| Native candidate resolution | Independently parsed the original and strict-recheck locks: 303 records including root, zero prerelease version identifiers, and byte-identical SHA-256 `da45dd6cb7cee7834fc5985b6595c2111780ee24d7cf87d1bdaf1749be3f37ab`. The original missing invocation/configuration evidence remains accurately acknowledged. The later receipt records a fresh no-lock/no-node_modules starting point, explicit strict peer/engine checks, disabled force/legacy peer/scripts/workspaces, separate empty configs and child-environment scoping. Its exit 0 and unchanged lock do not prove the original invocation, a selected supported graph, installed contents or runtime compatibility. The initial REVISE and correction-1 bounded PASS are preserved. |
| Original eight native-checker cases | Read every fixture, the explicit two-rule config, case commands, saved diagnostics and empty stderr. Valid hooks/Effect Event and conditional `use` accept; early-return hook, missing Effect dependency and the three recorded invalid Effect Event uses reject with named diagnostics. These are saved Windows Oxlint 1.86.0 CLI observations. Only two explicitly enabled stable rules were inspected; isolated `--allow all` is not a production preset. Earlier independent CLI reproduction need not be rerun here and is not claimed as a new execution. |
| Protected World inspection | Read the raw source-lint record and its protected-source identities. The recorded HUD diagnostic identifies a hook after the early return; ExteriorScene reports missing `applyKeyframe`; WorldCanvas has no diagnostics under only those two rules. The dependency/source protected hashes still match current bytes. No runtime crash is resolved by these observations, and blindly adding animation dependencies is not an authorized safe fix. R-003 remains open. |
| Later alias/custom Effect/configuration evidence | Read the eleven retained source fixtures, configurations, recorded fourteen invocations and raw outputs; diagnostic codes/file counts agree with the receipt. Hook-shaped aliases and namespace subset reject appropriately, but renamed `state`/`effect` and shared custom-Effect configuration miss semantically invalid cases. Rule-level `additionalHooks` without CLI overrides rejects the missing dependency and accepts the complete list; the paired allow/deny override invocation loses that enforcement. Invalid config and nonexistent source exit 1; the latter reports no files. Directory scope examines seven base fixtures and reports four expected violations. These are explicit limits, not waiver or equivalence to upstream alias behavior. No new editor/CI/application enforcement is claimed. |
| Recommended-rule inventory and source support | Read the seventeen-row disposition inventory and tagged native rule sources. Two identifiers have the bounded fixture scope; twelve compiler-analysis identifiers remain experimental/excluded; `component-hook-factories`, `config` and `gating` have no identical registered identifier. Tagged dependency source supports the rule-level custom-hook option; source and raw CLI observations are distinct from binary provenance. The later separate conformance receipt reports actual reproduction and inventory inspection at its own hashes; its PASS is evidence accuracy, not full stable preset parity. The separate registry/range recheck's PASS remains only that recheck, not a license/native/compiler waiver. |
| Backend resolver and Pydantic coupling | Parsed the actual pip report, pinned twelve-family study, raw output and exit 0. Independently evaluated the recorded Windows environment and Uvicorn `standard`/Psycopg `binary` active clauses: 40 distributions, 45 active Requires-Dist clauses, no missing/out-of-range target, and no Requires-Python mismatch. Every report URL names a wheel, and no yanked record or prerelease version is observed. Pydantic 2.13.5's exact core is 2.46.5, not independently newest 2.49.0. Wheel eligibility/metadata closure is not imports, native ABI, Linux/other-target validation, SQL/database behavior or a reproducible production install. Development classifiers are retained separately from release-version flags. |
| Pydantic source-channel amendment | Independently peeled both saved tag references to their annotated objects: both point to `001dea020e0809844e5b17666432c9135a976f46`. Parsed pinned Cargo/pyproject versions and exact core dependency. Tag and immutable-commit pyproject copies match; policy copies match. The core tag's annotation says 2.46.3 while the tag/source version is 2.46.5, and both objects explicitly report unsigned/unverified. The recorded 404 release lookup remains a 404. This is source-location/version association, not source-to-wheel attestation, a fabricated release object, erased Alpha classifier or whole stable graph approval. |
| Original targeted notices and bundled identities | Read the saved archive inventories/notice texts, direct-to-bundle correspondence and pinned source notices as data. All embedded notice SHA-256 values recompute; the six nested manifest names/versions match their lock records. WebGL's actual package MIT notice and separate CC0 source declarations are distinguished. Three emnapi MIT notices and tslib's separate 0BSD/copyright notices remain explicit. Saved direct comparisons report six matching NAPI files and 39 matching wasm-util files; their package archives lack licence files. Pinned NAPI source has both LongYinan and GitHub notice blocks; Tailwind's tagged source notice is separate from attestation of its WASM build. This review does not claim a fresh unpack/reproduction of those non-packet original package archives or legal clearance; earlier native/archive inspection and its narrow receipt remain supporting evidence. |
| Audit and SBOM amendment | Raw audit output has empty vulnerabilities, zero counts and 302 dependency occurrences; recorded argv includes all three scopes, lock-only and no scripts/fix. Independently derived actual-name/version SBOM correspondence from lock entries, rather than trusting the crosswalk: 302 occurrences map to 300 component identities and 301 emitted dependency records including root; no unresolved ref or digest mismatch for a declared SRI. The three `eslint-visitor-keys@5.0.1` paths share one declared integrity. Exactly GSAP/WebGL omit emitted licence declarations and the six bundled identities omit individual hashes. This is dated advisory and pre-build identity metadata, not installed-file/path-context equivalence, complete edge semantics, full CycloneDX conformance, final product SBOM or universal security proof. |
| wasm-util/Node notice amendment | Read the frozen ZIP in memory without extraction/execution. Its 87 regular-file paths equal the non-truncated tree's 87 blobs; every byte length and computed Git blob SHA-1 matches. The filename inventory lacks conventional licence/copying/notice names. The TypeScript path source acknowledges adapting Node's resolver; retained Node comparison source/licence has the copyright/permission preservation condition. The specific Node version is a comparison reference, not an established copied revision. Selected-text/filename absence does not settle original-code rights or third-party mapping. The missing authoritative complete notice remains held. |
| GSAP notice/source amendment | Independently recomputed archive SHA-512 against the lock and exact saved registry response. All 179 regular files match the saved path/size/SHA-256 inventory; no conventional notice-named file is present. README/core/unminified/minified core equal the four pinned tag-source copies byte for byte. Read saved official licence HTML and incorporated terms as dated evidence: custom licence/competitive-product and notice restrictions, amendment/termination provisions and dates are accurately bounded; it is not MIT or an unrestricted grant. No npm gitHead/full-plugin/source-build attestation or actual-build distribution clearance is inferred. The earlier GSAP PASS remains precisely its listed evidence scope. |
| Current navigation and review coverage | README/current producer text keeps original interrupted review without verdict, preserves initial native REVISE/correction PASS, and identifies separate backend, inventory, notice, range and conformance receipts. Current source correspondence for all listed receipts and retained inputs is verified. Whole-file producer hashes identify bytes; they do not enlarge any old narrow review. Aside from CER-MED-001, no additional material contradiction or newly selected graph is found in the inspected reconciliation. |

## Coverage limits and held obligations

This is filesystem evidence review plus independent in-memory parsing, hashes,
marker/range evaluation, archive reading and identity recomputation. No fresh
registry/current-release certification was commissioned or performed. Saved HTTP
claims remain dated observations; their digests do not independently authenticate
remote origin. Previously reproduced CLI cases were not rerun, no resolver/audit
or install command was newly executed, and no downloaded/experimental checker,
package, source-build or application code was executed. No new application or
schema tests are warranted for this evidence-only slice. Artifact correspondence
is reported separately from product behavior.

Five dependency-input hashes and the ten-file dependency/source conformance map
were independently compared with current protected files and match. This does not
claim a complete repository build audit or protected GLB runtime inspection. Only
this receipt is authored; producer documents, receipts, source, locks, settings,
services, accounts and external systems are unchanged by the reviewer.

Held inputs remain: latest mutually compatible **supported stable** complete graph
and coupled tool/config selection; actual deterministic installations and imports;
all owned source/rule/config/editor/CI coverage; compiler/type/refresh/build,
renderer/exporter/browser/OS/database/API behavior; actual packaging/provider
planning when authorized; full advisory/licence/provenance/distribution inventory,
wasm-util notice resolution, final build SBOM and source-build associations;
privacy/security/accessibility/performance/recovery evidence; reviewed reversible
modernization waves and founder approval. Provider-neutral correction must retain
mandatory Entra and approved private-AI routes. This REVISE does not accept MA-013,
Phase 1, the full original interrupted review, an application/runtime-compatible
stack, legal clearance, installation/implementation permission or production
selection. The product remains first-production v1.

## Exhaustive frozen input identities

All snapshot filenames below are relative to the manifest folder. Source paths
are repository-relative. A later source amendment falls outside this receipt's
identity, even where its earlier saved evidence is unchanged.

| Index | Source | Frozen snapshot | Bytes | SHA-256 |
|---|---|---|---:|---|
| 000 | `docs/phase-1-compatibility/backend-evidence-2026-10-04.md` | `000-backend-evidence-2026-10-04.md` | 12407 | `f04d8fbf7330ae9d58a135c92cd745c0c973f472791929c96ebe17555ea21061` |
| 001 | `docs/phase-1-compatibility/README.md` | `001-README.md` | 21254 | `f197b6a8f5534c10fd0c9d96dea043870eabd703d8d3027008a8befb8037bdec` |
| 002 | `docs/phase-1-compatibility/refresh-evidence-2026-10-04.md` | `002-refresh-evidence-2026-10-04.md` | 42698 | `ae2f8a87c378147461d7606616ce5118cf83e10bcb3e5889091d7ef8f0d87964` |
| 003 | `output/research/compatibility-resolution-2026-10-04/backend-windows/pip-report.json` | `003-pip-report.json` | 452688 | `b9a135fa96ee978af2011ea4e4b8f848fd44235db46349caed74cc61ecc2c8f6` |
| 004 | `output/research/compatibility-resolution-2026-10-04/backend-windows/requirements-study.txt` | `004-requirements-study.txt` | 234 | `2d588f1262f7c04d8baa100e18bfd6aab903c501e7b5408fcf2d298fd469fcae` |
| 005 | `output/research/compatibility-resolution-2026-10-04/backend-windows/resolver-exit-code.txt` | `005-resolver-exit-code.txt` | 3 | `13bf7b3039c63bf5a50491fa3cfd8eb4e699d1ba1436315aef9cbe5711530354` |
| 006 | `output/research/compatibility-resolution-2026-10-04/backend-windows/resolver-output.txt` | `006-resolver-output.txt` | 9640 | `e55ed332da06a98619c29d7c7d4dbd5bb12941ee552a332631ba67e55a24fae5` |
| 007 | `output/research/compatibility-resolution-2026-10-04/bundled-license-correspondence.json` | `007-bundled-license-correspondence.json` | 9133 | `25f8485798477ad323b3479c93f009a56ae2e552930d25b23f4b8a6367e203a7` |
| 008 | `output/research/compatibility-resolution-2026-10-04/frontend-package-metadata.json` | `008-frontend-package-metadata.json` | 46632 | `c9e0733159326163cb220beaba2d63b6675c7c7605a8a211964776b69444cc20` |
| 009 | `output/research/compatibility-resolution-2026-10-04/independently-latest/package.json` | `009-package.json` | 1094 | `8536a1f7907aaad128a14ed03cd8e741750c83a5406d893466fff6c15b7ae91d` |
| 010 | `output/research/compatibility-resolution-2026-10-04/independently-latest/resolver-exit-code.txt` | `010-resolver-exit-code.txt` | 3 | `f1b2f662800122bed0ff255693df89c4487fbdcf453d3524a42d4ec20c3d9c04` |
| 011 | `output/research/compatibility-resolution-2026-10-04/independently-latest/resolver-output.txt` | `011-resolver-output.txt` | 1290 | `edd3cd717b7538a346f7ef72134f13fc6e7651e8a7d0dee1b5ec13ee27eaeaa2` |
| 012 | `output/research/compatibility-resolution-2026-10-04/native-lint-behavior-probe.json` | `012-native-lint-behavior-probe.json` | 13477 | `7f17d668dfb445df7a877452162e827d4e360e263ea3952eff3e523bc866d138` |
| 013 | `output/research/compatibility-resolution-2026-10-04/native-lint-metadata.json` | `013-native-lint-metadata.json` | 2466 | `a0206e039a74610503f56f0f9d64975d6cf2ac634f1ccab8b6c74aa0c89fb88b` |
| 014 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/conditional-hook-output.json` | `014-conditional-hook-output.json` | 852 | `b9b9d688c7733369b453367aa6e6ba11d90fc4f66937b1c4002e811ff324af62` |
| 015 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/conditional-hook-stderr.txt` | `015-conditional-hook-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 016 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/conditional-use-output.json` | `016-conditional-use-output.json` | 197 | `9d644a9b46e4cebc8c5be70ec4bc4470806fd974516a5d5b43447e6c2b12f2e0` |
| 017 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/conditional-use-stderr.txt` | `017-conditional-use-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 018 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/effect-event-as-click-handler-output.json` | `018-effect-event-as-click-handler-output.json` | 814 | `efea181e0b48aa662711d847118babd3fcccfae6ebdb79a393f5e65acaca6277` |
| 019 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/effect-event-as-click-handler-stderr.txt` | `019-effect-event-as-click-handler-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 020 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/effect-event-during-render-output.json` | `020-effect-event-during-render-output.json` | 759 | `7920b71eef7b36d5dad6f49ab122070999a1b8738c2b353795ca6b8011e2887b` |
| 021 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/effect-event-during-render-stderr.txt` | `021-effect-event-during-render-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 022 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/effect-event-in-deps-output.json` | `022-effect-event-in-deps-output.json` | 690 | `be2ee3c74475a69bdb05d8ef2f528fe7d6a885299ae15214853b7ae104fc01a3` |
| 023 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/effect-event-in-deps-stderr.txt` | `023-effect-event-in-deps-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 024 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/effect-event-valid-output.json` | `024-effect-event-valid-output.json` | 197 | `630e29d668c8fdf42aa69f6827a9c5c9bbc4c8f8e2b36e44e96682c6581b8ca2` |
| 025 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/effect-event-valid-stderr.txt` | `025-effect-event-valid-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 026 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/exit-code.txt` | `026-exit-code.txt` | 3 | `13bf7b3039c63bf5a50491fa3cfd8eb4e699d1ba1436315aef9cbe5711530354` |
| 027 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/fixtures/conditional-hook.tsx` | `027-conditional-hook.tsx` | 163 | `dbe025a6b36ba677b43e225911bd29ad134da2dc25250a405b989e9866ce1e38` |
| 028 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/fixtures/conditional-use.tsx` | `028-conditional-use.tsx` | 142 | `b06d92f2c3c05793cffadb94f464c39dec272e08556ee04b7effeb4b90cd7373` |
| 029 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/fixtures/effect-event-as-click-handler.tsx` | `029-effect-event-as-click-handler.tsx` | 182 | `5d5601045578223a84ff3f76e1315aa59a2079945d1c157679b1fc329b53aeef` |
| 030 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/fixtures/effect-event-during-render.tsx` | `030-effect-event-during-render.tsx` | 154 | `66d747cee459cf89ed8a0bd12df0ceed5701df3e4be3869395968ec43a308304` |
| 031 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/fixtures/effect-event-in-deps.tsx` | `031-effect-event-in-deps.tsx` | 196 | `fa72507867708dabdadcdd87aaa0912cba30175d348e2315bb5d543f24572960` |
| 032 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/fixtures/effect-event-valid.tsx` | `032-effect-event-valid.tsx` | 185 | `1607706ea843c19e926f24711173b20a980f17ea585c326e9aa03820875f44df` |
| 033 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/fixtures/missing-dependency.tsx` | `033-missing-dependency.tsx` | 120 | `893f0a2a3cb9d4056c74e81e7b48f677e88dfda7f6e51ad62369ca9b306ebb6e` |
| 034 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/fixtures/valid-hooks.tsx` | `034-valid-hooks.tsx` | 163 | `0d94f59f497b0e0afae4510a8c11e3d6898382a4e2f0f08de2ffa0fa204edf2a` |
| 035 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/missing-dependency-output.json` | `035-missing-dependency-output.json` | 757 | `b69aba43156ed86e662069d8d4603f2799768904535becc7c482b0b3f4049783` |
| 036 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/missing-dependency-stderr.txt` | `036-missing-dependency-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 037 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/package-lock.json` | `037-package-lock.json` | 162581 | `da45dd6cb7cee7834fc5985b6595c2111780ee24d7cf87d1bdaf1749be3f37ab` |
| 038 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/package.json` | `038-package.json` | 1166 | `f1ecb8d6083bacb65684def851c69a9066618534ddfc62b088fd7242e29eb69e` |
| 039 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/probe-config.json` | `039-probe-config.json` | 136 | `62f9d0789fbcbd0c4232b4a70cf972a3e8084bd21a7c194beb86393c27edf431` |
| 040 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/resolver-output.txt` | `040-resolver-output.txt` | 20 | `6c6100b1e38130900f947b09dba989b4fe8c8d23ff8ad5d1c1fb61cdc98a202f` |
| 041 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/valid-hooks-output.json` | `041-valid-hooks-output.json` | 197 | `7524934340599f35b7d3a2a6ff8c7cedbdb0a426815829f5a1a73b9d3257ed99` |
| 042 | `output/research/compatibility-resolution-2026-10-04/native-lint-probe/valid-hooks-stderr.txt` | `042-valid-hooks-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 043 | `output/research/compatibility-resolution-2026-10-04/native-lint-protected-world-inspection.json` | `043-native-lint-protected-world-inspection.json` | 5863 | `b199bf247a3c4f07136f32d661d468050cec12369697e28f669e8f59305e06b8` |
| 044 | `output/research/compatibility-resolution-2026-10-04/native-lint-study-analysis.json` | `044-native-lint-study-analysis.json` | 1665 | `988aab79c92f663afb3953e4860d50944c50de9c20bf51e0acc5779099e92401` |
| 045 | `output/research/compatibility-resolution-2026-10-04/native-lint-tool-provenance.json` | `045-native-lint-tool-provenance.json` | 4013 | `8f55e1327d1d3bb9ad1de80aeeb95eab7f96ff1349c49a334ea1be4355a3e984` |
| 046 | `output/research/compatibility-resolution-2026-10-04/native-lint-win32-metadata.json` | `046-native-lint-win32-metadata.json` | 2456 | `fdbf0298cdb452f2379a29bf9e91d1cbd7873d2831046d581fd085f4f4a7facd` |
| 047 | `output/research/compatibility-resolution-2026-10-04/pinned-source-license-evidence.json` | `047-pinned-source-license-evidence.json` | 5924 | `c2b4780c1555c86ed440e35b2bb77e932203576062bf50fa4f2b051453db3662` |
| 048 | `output/research/compatibility-resolution-2026-10-04/protected-input-hashes.json` | `048-protected-input-hashes.json` | 481 | `8f15a53bc1bf2c0cb92f536624e955b06725bc31b5bff3007d8b2729527a0661` |
| 049 | `output/research/compatibility-resolution-2026-10-04/release-channel-checks.json` | `049-release-channel-checks.json` | 3454 | `6e42a028d39a9286490ad7f19d730c989a160e27cf32514ec59fcb8c1cb68813` |
| 050 | `output/research/compatibility-resolution-2026-10-04/resolution-analysis.json` | `050-resolution-analysis.json` | 12332 | `8f08d32270dfbf06ed11bf72c5639acf0fa08e07e1dfc28567cc9fdd50a994d0` |
| 051 | `output/research/compatibility-resolution-2026-10-04/stable-lint-babel-range-evidence.json` | `051-stable-lint-babel-range-evidence.json` | 43646 | `bcb6e2efaee736154bca476f733976d640b68106111e9a8cde860eb23c3518de` |
| 052 | `output/research/compatibility-resolution-2026-10-04/stable-lint-package-metadata.json` | `052-stable-lint-package-metadata.json` | 48094 | `c5dd839eb15c425d0ea608dc580edc45481635387140c162baf1915d431d707b` |
| 053 | `output/research/compatibility-resolution-2026-10-04/stable-lint-source-observations.json` | `053-stable-lint-source-observations.json` | 8888 | `034e0bf67c05641a23851186626152971960e33f5feb319aeca52f2d6d325bf1` |
| 054 | `output/research/compatibility-resolution-2026-10-04/targeted-license-analysis.json` | `054-targeted-license-analysis.json` | 7094 | `9951e7b9c94e03c8cd29628588386b967780f6dcc8fa86de1f384ce8ee5866a5` |
| 055 | `output/research/compatibility-resolution-2026-10-04/targeted-license-archive-evidence.json` | `055-targeted-license-archive-evidence.json` | 30051 | `8ba7e6e3f75132d411bece717992178b9b0ec99c925b2b92542e2f7dc104c810` |
| 056 | `output/research/compatibility-resolution-2026-10-04/targeted-license-metadata.json` | `056-targeted-license-metadata.json` | 7276 | `01c7fd8651e9e6274c7dc276f20631213f803142a4f18300e3aeb2711913e60e` |
| 057 | `output/research/compatibility-resolution-2026-10-04/ts7-api6-bridge/package-lock.json` | `057-package-lock.json` | 164514 | `d9e70a50b925087e7bb5d2c2f95d6acf7cf337de3e5bb3b1fd47f8c291bd0de9` |
| 058 | `output/research/compatibility-resolution-2026-10-04/ts7-api6-bridge/package.json` | `058-package.json` | 1173 | `330b6ee9a8abeceed3afe0c868dc7107c7e1a1fe129171d1e6557781d37fdef0` |
| 059 | `output/research/compatibility-resolution-2026-10-04/ts7-api6-bridge/resolver-exit-code.txt` | `059-resolver-exit-code.txt` | 3 | `13bf7b3039c63bf5a50491fa3cfd8eb4e699d1ba1436315aef9cbe5711530354` |
| 060 | `output/research/compatibility-resolution-2026-10-04/ts7-api6-bridge/resolver-output.txt` | `060-resolver-output.txt` | 20 | `6c163cceef75764a14ba2be8b69a742ba88f407dfc199cb179c375882ab5da96` |
| 061 | `output/research/compatibility-review-current-scope-2026-10-04.json` | `061-compatibility-review-current-scope-2026-10-04.json` | 10386 | `a0853a0ff6561764ede1404722824df4218b2e8c8c22cc1a47905c4a35f10973` |
| 062 | `AGENTS.md` | `062-AGENTS.md` | 7686 | `55405cb02a96d05f7f6d68e56a588d743f83877fb2691a5a9f2c736126adbcc5` |
| 063 | `.specify/memory/constitution.md` | `063-constitution.md` | 16234 | `33ec0bb02b0d0d9a55d0971589bd19f7242f5d56da130f8f496bc1d31a8b5d23` |
| 064 | `PROJECT.md` | `064-PROJECT.md` | 10942 | `a483bd2713fe420322772ab7fb07c848aaf103088697c05ab91f35d2e5ea1461` |
| 065 | `DECISIONS.md` | `065-DECISIONS.md` | 72891 | `1d53a14ac3347ebeefeeb728e03862b09de111b748cef4e48d5f4ca19141b6d8` |
| 066 | `TASKS.md` | `066-TASKS.md` | 3811 | `158e06c0d8cd67859c8b459b96dce3449cb4d16788d3c520e99d8823f72edcd3` |
| 067 | `docs/software-definition/README.md` | `067-README.md` | 15180 | `c454e744daeaff518e28b4095b47dd86fd3fb10e3298265c7cd159f142fa919c` |
| 068 | `docs/phase-1-compatibility/reviews/candidate-inventory-review-2026-10-04.md` | `068-candidate-inventory-review-2026-10-04.md` | 9525 | `55eeeca3faf02a11495afdd69c861e519b3c5566c64b641373b3d74922d2633a` |
| 069 | `docs/phase-1-compatibility/reviews/refresh-backend-2026-10-04.md` | `069-refresh-backend-2026-10-04.md` | 7105 | `1b68031e3e82ea79ab8b039f6132bb51ee65a618b73a984aeef0cad477a8fb6c` |
| 070 | `docs/phase-1-compatibility/reviews/wasm-util-notice-review-2026-10-04.md` | `070-wasm-util-notice-review-2026-10-04.md` | 6591 | `fc3ef1727922b82467326ae6736cfead6292a0584410a1e8ad7f008104559493` |
| 071 | `docs/phase-1-compatibility/reviews/react-lint-stable-path-recheck-2026-10-04.md` | `071-react-lint-stable-path-recheck-2026-10-04.md` | 6713 | `0ac0c4a4a9ee0edd3a4130d26ffdd9aad1f44179c5295a203b13c6e1f2458391` |
| 072 | `docs/phase-1-compatibility/reviews/native-react-lint-evidence-review-2026-10-04.md` | `072-native-react-lint-evidence-review-2026-10-04.md` | 21861 | `abce8aad7ecc6e4611a93b9b2215ba8a8bd5743bd39a832d9a79f30e647bd490` |
| 073 | `docs/phase-1-compatibility/reviews/native-lint-strict-recheck-review-2026-10-04.md` | `073-native-lint-strict-recheck-review-2026-10-04.md` | 12431 | `6c557c8ebfdb482634f3422d551263cf0d047e227bc8ad2ac695c5ba9883de3e` |
| 074 | `docs/phase-1-compatibility/reviews/native-hook-conformance-v1-2026-10-05.md` | `074-native-hook-conformance-v1-2026-10-05.md` | 7660 | `318bd11635e0c2c62fdab343f40007ce1c76e90287f037e7b1362e03d1d22b4d` |
| 075 | `docs/phase-1-compatibility/reviews/gsap-notice-evidence-2026-10-04.md` | `075-gsap-notice-evidence-2026-10-04.md` | 8960 | `2726d61ffdbdc587a7cefa8a2cab2c892fbc71f104fcbeb4159787d55bed98cb` |
| 076 | `docs/phase-1-compatibility/wasm-util-notice-evidence-2026-10-04.md` | `076-wasm-util-notice-evidence-2026-10-04.md` | 4050 | `bba46a0f8337fde3af03f8bf8e0ac8f9066039ac925a1d575cf0d10bfc677ef8` |
| 077 | `output/research/compatibility-resolution-2026-10-04/native-lint-recommended-coverage.json` | `077-native-lint-recommended-coverage.json` | 16889 | `86bbe2d8e65bde10d1719cd2c822e8739e4de78fb0f1590451749e0a920ca123` |
| 078 | `output/research/compatibility-resolution-2026-10-04/native-lint-strict-resolution-recheck/package.json` | `078-package.json` | 1166 | `f1ecb8d6083bacb65684def851c69a9066618534ddfc62b088fd7242e29eb69e` |
| 079 | `output/research/compatibility-resolution-2026-10-04/native-lint-strict-resolution-recheck/package-lock.json` | `079-package-lock.json` | 162581 | `da45dd6cb7cee7834fc5985b6595c2111780ee24d7cf87d1bdaf1749be3f37ab` |
| 080 | `output/research/compatibility-resolution-2026-10-04/native-lint-strict-resolution-recheck/receipt.json` | `080-receipt.json` | 5288 | `4502e1d0ce6814968b9c12435f726d173ca5bc520e3ac8347315169f7fdde1ac` |
| 081 | `output/research/compatibility-resolution-2026-10-04/native-lint-strict-resolution-recheck/stdout.txt` | `081-stdout.txt` | 18 | `2b2bbbf93489e72436a76087518c0ea9a2edc890ec71f668ed8bb2124f488c60` |
| 082 | `output/research/compatibility-resolution-2026-10-04/native-lint-strict-resolution-recheck/stderr.txt` | `082-stderr.txt` | 212 | `e0fd7d2a46113fec04fc2e28f48b8beeef0fb56cae6010aa580f9dd6f1956706` |
| 083 | `output/research/native-lint-conformance-2026-10-05/review-inputs.json` | `083-review-inputs.json` | 11837 | `d61a3d279a383648619d0765938be8e14c5fdf28a567a0353b4330f77f332201` |
| 084 | `output/research/native-lint-conformance-2026-10-05/run_probe.py` | `084-run_probe.py` | 9158 | `749219e45932f92ab8b73c9489a4adcf9597e240b745c770fedc3758d09d3ca7` |
| 085 | `output/research/native-lint-conformance-2026-10-05/receipt.json` | `085-receipt.json` | 22285 | `ad2050d7537d5adde4cf4ef8aed268b930b7e5e3ce5c4427cdd76cdd4b7606ca` |
| 086 | `output/research/native-lint-conformance-2026-10-05/tag-source-receipt.json` | `086-tag-source-receipt.json` | 499 | `fe3a7c312a94594299a37267f67f22edde0d6eafbb3248b5331e6c9151300b97` |
| 087 | `output/research/native-lint-conformance-2026-10-05/exhaustive_deps.rs` | `087-exhaustive_deps.rs` | 149508 | `0c9a8372f5a72398dd63a747d35a978b4015626cd40d50573cf4fcfa062ddd3d` |
| 088 | `output/research/native-lint-conformance-2026-10-05/rules_of_hooks.rs` | `088-rules_of_hooks.rs` | 90995 | `35e4a166253a27d0990bddfdb66b14772b986db2af5ea2083f4cfa1da2d4682b` |
| 089 | `output/research/native-lint-conformance-2026-10-05/probe-config.json` | `089-probe-config.json` | 136 | `62f9d0789fbcbd0c4232b4a70cf972a3e8084bd21a7c194beb86393c27edf431` |
| 090 | `output/research/native-lint-conformance-2026-10-05/invalid-config.json` | `090-invalid-config.json` | 13 | `1bde13a215e156fc5595ea1047823eb14132bc054b87cac3a3f3e92b475fcd69` |
| 091 | `output/research/native-lint-conformance-2026-10-05/refresh-evidence.reviewed.md` | `091-refresh-evidence.reviewed.md` | 42197 | `0ddacac850efef76d26b9044043dee1c683714988b59271bdad5c405cf8c6325` |
| 092 | `output/research/native-lint-conformance-2026-10-05/base-fixtures/custom-hook-conditional.tsx` | `092-custom-hook-conditional.tsx` | 218 | `fa16240b49c9d19a6d483d3916b9ad3812283f11227587867dac31a7458a6b47` |
| 093 | `output/research/native-lint-conformance-2026-10-05/base-fixtures/named-hook-alias-conditional.tsx` | `093-named-hook-alias-conditional.tsx` | 186 | `c5c100fe1ca682d72d32545320e9fd464483fbd87c292e4f2d1d12899ea6d5e1` |
| 094 | `output/research/native-lint-conformance-2026-10-05/base-fixtures/namespace-conditional.tsx` | `094-namespace-conditional.tsx` | 176 | `5bece0488a4c415a10dada7b396675e9130e128719fa94f97a13fe3c4f5deb98` |
| 095 | `output/research/native-lint-conformance-2026-10-05/base-fixtures/namespace-missing-dependency.tsx` | `095-namespace-missing-dependency.tsx` | 165 | `057bba621e22d6a6a953897f0e0793215941f822dcc75939d745790417fc8a0f` |
| 096 | `output/research/native-lint-conformance-2026-10-05/base-fixtures/namespace-valid.tsx` | `096-namespace-valid.tsx` | 170 | `087a597ad7123a2f49151db3ed01ac525b61016ce5312005abe36c5fee5b8348` |
| 097 | `output/research/native-lint-conformance-2026-10-05/base-fixtures/renamed-effect-missing-dependency.tsx` | `097-renamed-effect-missing-dependency.tsx` | 167 | `8277a73b7cd2b42317d5abc3e38fb4a68ecbacdcc803bd1d57c71660efe757a8` |
| 098 | `output/research/native-lint-conformance-2026-10-05/base-fixtures/renamed-hook-conditional.tsx` | `098-renamed-hook-conditional.tsx` | 176 | `6de9e0d543413dadf94d1b593eb4caa19a64b08a61aa2d33456005a95c6fc882` |
| 099 | `output/research/native-lint-conformance-2026-10-05/custom-fixtures/custom-effect-rule-invalid-cli-override.tsx` | `099-custom-effect-rule-invalid-cli-override.tsx` | 185 | `396534736cd82f460f8b4f05c50d4157a6eba48343f71a5753bdd59b7a0eada6` |
| 100 | `output/research/native-lint-conformance-2026-10-05/custom-fixtures/custom-effect-rule-invalid.tsx` | `100-custom-effect-rule-invalid.tsx` | 185 | `396534736cd82f460f8b4f05c50d4157a6eba48343f71a5753bdd59b7a0eada6` |
| 101 | `output/research/native-lint-conformance-2026-10-05/custom-fixtures/custom-effect-rule-valid.tsx` | `101-custom-effect-rule-valid.tsx` | 190 | `ad1cc07b8a474aa72e178d3bdea7b9f1646131f9692baa86426261e426ad3ee8` |
| 102 | `output/research/native-lint-conformance-2026-10-05/custom-fixtures/custom-effect-shared-invalid.tsx` | `102-custom-effect-shared-invalid.tsx` | 185 | `396534736cd82f460f8b4f05c50d4157a6eba48343f71a5753bdd59b7a0eada6` |
| 103 | `output/research/native-lint-conformance-2026-10-05/namespace-valid-stdout.json` | `103-namespace-valid-stdout.json` | 197 | `44194e3a8391f08e593f335bea2d13398eb1f6cc49082d1bdc8f7cf72c6708d5` |
| 104 | `output/research/native-lint-conformance-2026-10-05/namespace-valid-stderr.txt` | `104-namespace-valid-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 105 | `output/research/native-lint-conformance-2026-10-05/namespace-conditional-stdout.json` | `105-namespace-conditional-stdout.json` | 790 | `97993de055c6faf6623d41bc039bada37f945c02a0d3556d1de9bf3e17591119` |
| 106 | `output/research/native-lint-conformance-2026-10-05/namespace-conditional-stderr.txt` | `106-namespace-conditional-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 107 | `output/research/native-lint-conformance-2026-10-05/namespace-missing-dependency-stdout.json` | `107-namespace-missing-dependency-stdout.json` | 700 | `c876631eadfa7265134d8b87a5c65043c605a4846c8a3735d16a864c20affc40` |
| 108 | `output/research/native-lint-conformance-2026-10-05/namespace-missing-dependency-stderr.txt` | `108-namespace-missing-dependency-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 109 | `output/research/native-lint-conformance-2026-10-05/custom-hook-conditional-stdout.json` | `109-custom-hook-conditional-stdout.json` | 794 | `05acf6c82f741df11f368cdf0344bef4ada90de9e7095767d60c9aa82eda05aa` |
| 110 | `output/research/native-lint-conformance-2026-10-05/custom-hook-conditional-stderr.txt` | `110-custom-hook-conditional-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 111 | `output/research/native-lint-conformance-2026-10-05/named-hook-alias-conditional-stdout.json` | `111-named-hook-alias-conditional-stdout.json` | 799 | `b07dc1eb36a052235115ce1d98481ebb585f7d0e68bdc42005c14d71b3cfc569` |
| 112 | `output/research/native-lint-conformance-2026-10-05/named-hook-alias-conditional-stderr.txt` | `112-named-hook-alias-conditional-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 113 | `output/research/native-lint-conformance-2026-10-05/renamed-hook-conditional-stdout.json` | `113-renamed-hook-conditional-stdout.json` | 197 | `5fcde5e1377842c06d51c1c11fb1aee2f11789513ac163c27745c303e509f598` |
| 114 | `output/research/native-lint-conformance-2026-10-05/renamed-hook-conditional-stderr.txt` | `114-renamed-hook-conditional-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 115 | `output/research/native-lint-conformance-2026-10-05/renamed-effect-missing-dependency-stdout.json` | `115-renamed-effect-missing-dependency-stdout.json` | 197 | `75e92ff6d28488679cda0ae66e0a093fed8a4aa4389caa9833143f03d10024a3` |
| 116 | `output/research/native-lint-conformance-2026-10-05/renamed-effect-missing-dependency-stderr.txt` | `116-renamed-effect-missing-dependency-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 117 | `output/research/native-lint-conformance-2026-10-05/invalid-config-stdout.txt` | `117-invalid-config-stdout.txt` | 256 | `87395855d4a140a4feedd56b2c1809fee524f3cb7fc50ea48f52e8a9bf881846` |
| 118 | `output/research/native-lint-conformance-2026-10-05/invalid-config-stderr.txt` | `118-invalid-config-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 119 | `output/research/native-lint-conformance-2026-10-05/unmatched-file-stdout.txt` | `119-unmatched-file-stdout.txt` | 267 | `eb8f4680fd2ea69b4824e2931795f84fccfb3e85b9cf5d0f6c57653f61817bdb` |
| 120 | `output/research/native-lint-conformance-2026-10-05/unmatched-file-stderr.txt` | `120-unmatched-file-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 121 | `output/research/native-lint-conformance-2026-10-05/directory-scope-stdout.txt` | `121-directory-scope-stdout.txt` | 2501 | `f4b91bcac4b741e5372009840dff6581a665e78d956ed3913eb278516e40eda2` |
| 122 | `output/research/native-lint-conformance-2026-10-05/directory-scope-stderr.txt` | `122-directory-scope-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 123 | `output/research/native-lint-conformance-2026-10-05/custom-effect-shared-invalid-stdout.json` | `123-custom-effect-shared-invalid-stdout.json` | 197 | `615c607737cad5ebe465cf3a108f4391328412a555a1a467fd86892b2b4840aa` |
| 124 | `output/research/native-lint-conformance-2026-10-05/custom-effect-shared-invalid-stderr.txt` | `124-custom-effect-shared-invalid-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 125 | `output/research/native-lint-conformance-2026-10-05/custom-effect-shared-invalid-config.json` | `125-custom-effect-shared-invalid-config.json` | 290 | `2b6077ba85dce91dec25ddfc12c5a0049fa089707ca6b6da1db7668dd9d32f3d` |
| 126 | `output/research/native-lint-conformance-2026-10-05/custom-effect-rule-invalid-stdout.json` | `126-custom-effect-rule-invalid-stdout.json` | 714 | `de00ffc8192f3cf2be9d2aac37347eaf3b4bd1cd348069a154c277713fd2f725` |
| 127 | `output/research/native-lint-conformance-2026-10-05/custom-effect-rule-invalid-stderr.txt` | `127-custom-effect-rule-invalid-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 128 | `output/research/native-lint-conformance-2026-10-05/custom-effect-rule-invalid-config.json` | `128-custom-effect-rule-invalid-config.json` | 269 | `7f1a71cf9486290de43f6a4170cf737903bf5a930339d62bfe61dbcb610534e2` |
| 129 | `output/research/native-lint-conformance-2026-10-05/custom-effect-rule-valid-stdout.json` | `129-custom-effect-rule-valid-stdout.json` | 197 | `5b2bd23dd030ee648720b01ce82596cf860c28d6371ed2a6a9039862d2dbafdc` |
| 130 | `output/research/native-lint-conformance-2026-10-05/custom-effect-rule-valid-stderr.txt` | `130-custom-effect-rule-valid-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 131 | `output/research/native-lint-conformance-2026-10-05/custom-effect-rule-valid-config.json` | `131-custom-effect-rule-valid-config.json` | 269 | `7f1a71cf9486290de43f6a4170cf737903bf5a930339d62bfe61dbcb610534e2` |
| 132 | `output/research/native-lint-conformance-2026-10-05/custom-effect-rule-invalid-cli-override-stdout.json` | `132-custom-effect-rule-invalid-cli-override-stdout.json` | 197 | `eeae7eb0d807c4e19b4c256789aab5506c811760f98c8873ca41962d8cb3400a` |
| 133 | `output/research/native-lint-conformance-2026-10-05/custom-effect-rule-invalid-cli-override-stderr.txt` | `133-custom-effect-rule-invalid-cli-override-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 134 | `output/research/native-lint-conformance-2026-10-05/custom-effect-rule-invalid-cli-override-config.json` | `134-custom-effect-rule-invalid-cli-override-config.json` | 269 | `7f1a71cf9486290de43f6a4170cf737903bf5a930339d62bfe61dbcb610534e2` |
| 135 | `output/research/compatibility-resolution-2026-10-04/backend-windows/core_cargo_pinned.source.txt` | `135-core_cargo_pinned.source.txt` | 2875 | `178d537feb822d845526eeac2438f817cf25ad15d15fe1261b81b9b3452edbb3` |
| 136 | `output/research/compatibility-resolution-2026-10-04/backend-windows/core_pyproject.source.txt` | `136-core_pyproject.source.txt` | 5643 | `80f7cf0e108619c32894e828db550bfe6928d4f14ce244ef492fe782609f9926` |
| 137 | `output/research/compatibility-resolution-2026-10-04/backend-windows/core_pyproject_pinned.source.txt` | `137-core_pyproject_pinned.source.txt` | 5643 | `80f7cf0e108619c32894e828db550bfe6928d4f14ce244ef492fe782609f9926` |
| 138 | `output/research/compatibility-resolution-2026-10-04/backend-windows/core_tag.source.txt` | `138-core_tag.source.txt` | 357 | `ec17ce0958d2914bf70a0aa8a09bf7917162c838e543101300e43a823913a047` |
| 139 | `output/research/compatibility-resolution-2026-10-04/backend-windows/core_tag_object.source.txt` | `139-core_tag_object.source.txt` | 700 | `a2d944024d8501218ee099223d2174fca81a05fe65c9d3e4aa32cbd2a3e81108` |
| 140 | `output/research/compatibility-resolution-2026-10-04/backend-windows/current_policy_pinned.source.txt` | `140-current_policy_pinned.source.txt` | 6635 | `08250a1f910b862b9c2349ce21dd4aa8d67e8b41aa32d5fe89acb9fa988335b7` |
| 141 | `output/research/compatibility-resolution-2026-10-04/backend-windows/pydantic_main_ref.source.txt` | `141-pydantic_main_ref.source.txt` | 337 | `fe401b5df447eaa692a63e8d5cb2eb69b0cdb85bd65a6497b703b110ae07d383` |
| 142 | `output/research/compatibility-resolution-2026-10-04/backend-windows/pydantic_pyproject.source.txt` | `142-pydantic_pyproject.source.txt` | 8849 | `5b72b7bec36d50131da5f0932176e5a2a14511d7e9f7f48a4ced20ddb8e3e783` |
| 143 | `output/research/compatibility-resolution-2026-10-04/backend-windows/pydantic_pyproject_pinned.source.txt` | `143-pydantic_pyproject_pinned.source.txt` | 8849 | `5b72b7bec36d50131da5f0932176e5a2a14511d7e9f7f48a4ced20ddb8e3e783` |
| 144 | `output/research/compatibility-resolution-2026-10-04/backend-windows/pydantic_tag.source.txt` | `144-pydantic_tag.source.txt` | 339 | `2d4eec2f7ca90dec8a358d26d417736188a7335bcc34eaf2dbf46050c6d0b356` |
| 145 | `output/research/compatibility-resolution-2026-10-04/backend-windows/pydantic_tag_object.source.txt` | `145-pydantic_tag_object.source.txt` | 680 | `d74a7934c1f6a803e4ec874e953bc42fee563b7d6f2dd61b9454f60d59f4c2d9` |
| 146 | `output/research/compatibility-resolution-2026-10-04/backend-windows/version_policy.source.txt` | `146-version_policy.source.txt` | 6635 | `08250a1f910b862b9c2349ce21dd4aa8d67e8b41aa32d5fe89acb9fa988335b7` |
| 147 | `output/research/compatibility-resolution-2026-10-04/backend-windows/pydantic-source-channel-evidence.json` | `147-pydantic-source-channel-evidence.json` | 4771 | `a6eb0c83a2431f0baae0242aa63ed07f55e28558c8638beef2a4aaeb2392dd89` |
| 148 | `output/research/compatibility-resolution-2026-10-04/gsap-notice-3.15.0/archive-README.md` | `148-archive-README.md` | 6199 | `66a79667b0538b19634b5a000a9a3debe588c98d390424e73e5d4de847270828` |
| 149 | `output/research/compatibility-resolution-2026-10-04/gsap-notice-3.15.0/gsap-3.15.0.tgz` | `149-gsap-3.15.0.tgz` | 1697897 | `d2e33ad202d4811e9084883f7ff9a27967ac4095caef51ca4c9d20697a253b1c` |
| 150 | `output/research/compatibility-resolution-2026-10-04/gsap-notice-3.15.0/incorporated-webflow-terms.html` | `150-incorporated-webflow-terms.html` | 365097 | `48bb54b8be09d84feaa261932f5df8fd27d4fdf1fa1b42341a65ae18d878aac1` |
| 151 | `output/research/compatibility-resolution-2026-10-04/gsap-notice-3.15.0/inspection.json` | `151-inspection.json` | 39490 | `a86f05e4f9443562406662ad95ec04a88ebf5a5f4e7c1389beae8c2e9ce48f0a` |
| 152 | `output/research/compatibility-resolution-2026-10-04/gsap-notice-3.15.0/official-standard-license.html` | `152-official-standard-license.html` | 76456 | `e26081f97d79030c9d5db9ec5a2ac1f6e499df661c37de6eb3c576483e11ec2e` |
| 153 | `output/research/compatibility-resolution-2026-10-04/gsap-notice-3.15.0/official-tag.json` | `153-official-tag.json` | 333 | `ab9f292df193b8f16a03a4bb7ed1160c4f768f5b6f5f627e54a3b6826616df57` |
| 154 | `output/research/compatibility-resolution-2026-10-04/gsap-notice-3.15.0/registry.json` | `154-registry.json` | 2137 | `787e4fdba7edc45b2a67af281508c4e518ad985ee0d972b9238847fa807768a9` |
| 155 | `output/research/compatibility-resolution-2026-10-04/gsap-notice-3.15.0/source-association.json` | `155-source-association.json` | 4303 | `95e7d668aeb10be68b983cec3e9bcec0d5e770e5ebf5ca4859f228a758e40d7f` |
| 156 | `output/research/compatibility-resolution-2026-10-04/gsap-notice-3.15.0/source-dist--gsap.js` | `156-source-dist--gsap.js` | 179557 | `01effe0e121c22ba0f885a3f091f3dc6d1f0d445c4fba37dcb298e314eca5cfb` |
| 157 | `output/research/compatibility-resolution-2026-10-04/gsap-notice-3.15.0/source-dist--gsap.min.js` | `157-source-dist--gsap.min.js` | 72927 | `92bb9a96476f983d212a2bc4f54c889039c1696dd4461d40a736860938570fbb` |
| 158 | `output/research/compatibility-resolution-2026-10-04/gsap-notice-3.15.0/source-README.md` | `158-source-README.md` | 6199 | `66a79667b0538b19634b5a000a9a3debe588c98d390424e73e5d4de847270828` |
| 159 | `output/research/compatibility-resolution-2026-10-04/gsap-notice-3.15.0/source-src--gsap-core.js` | `159-source-src--gsap-core.js` | 151046 | `8063816e0e7c3e6c07970fb06feafb06146fd266db5d8346419176b3d496e284` |
| 160 | `output/research/compatibility-resolution-2026-10-04/native-lint-audit-report.json` | `160-native-lint-audit-report.json` | 364 | `59e3aa5eb03e6e7954b32505a8b8348bb369c13c0c5960e22d36216b3e35ac91` |
| 161 | `output/research/compatibility-resolution-2026-10-04/native-lint-audit-receipt.json` | `161-native-lint-audit-receipt.json` | 1001 | `4a820466f9cf03a07b98c284e37428ce99435412860b1dbbe29779b7ad03c23a` |
| 162 | `output/research/compatibility-resolution-2026-10-04/native-lint-audit-stderr.txt` | `162-native-lint-audit-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 163 | `output/research/compatibility-resolution-2026-10-04/native-lint-candidate-sbom.cdx.json` | `163-native-lint-candidate-sbom.cdx.json` | 293948 | `59af17d89cae44938495c91535cc111919904a6fca2e934a3a54a59a52973184` |
| 164 | `output/research/compatibility-resolution-2026-10-04/native-lint-sbom-receipt.json` | `164-native-lint-sbom-receipt.json` | 2775 | `ea78a856b87410105a9924a9e2abcbd070354b80717af9d1cf32c31531000df5` |
| 165 | `output/research/compatibility-resolution-2026-10-04/native-lint-sbom-stderr.txt` | `165-native-lint-sbom-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 166 | `output/research/compatibility-resolution-2026-10-04/native-lint-sbom-crosswalk.json` | `166-native-lint-sbom-crosswalk.json` | 151620 | `0924988e33ade0b8531642201fa0a4493d6e450d458ee91262b3757484239246` |
| 167 | `output/research/compatibility-resolution-2026-10-04/wasm-util-full-source-notice-scan.json` | `167-wasm-util-full-source-notice-scan.json` | 1595 | `dd2f230cc56f3d7a7b744b8c8d00faaff2c396a8d22a35b00494fbcf9245837c` |
| 168 | `output/research/compatibility-resolution-2026-10-04/wasm-util-node-source-references.json` | `168-wasm-util-node-source-references.json` | 474 | `350b0ce19fd4521be036e10798db1b3d248ebfe8b518ea6f6ee5be9ed224c2b5` |
| 169 | `output/research/compatibility-resolution-2026-10-04/wasm-util-pinned-tree.json` | `169-wasm-util-pinned-tree.json` | 24360 | `416a22f0793a470166bf0a6b79355df65a95f56d4e850178db7f987453379fb9` |
| 170 | `output/research/compatibility-resolution-2026-10-04/wasm-util-pinned-source.zip` | `170-wasm-util-pinned-source.zip` | 78391 | `68444b71d4285abe742e370faf8d9b9c88f67ade023cddfcb170c8bb86f7b84f` |
| 171 | `output/research/compatibility-resolution-2026-10-04/node-v24.14.0-path.js` | `171-node-v24.14.0-path.js` | 52691 | `dd326ecdc2d6ad2025c4991f4b480d76a9f1d52b7f6d0988a5dc0a1d02de5209` |
| 172 | `output/research/compatibility-resolution-2026-10-04/node-v24.14.0-LICENSE.txt` | `172-node-v24.14.0-LICENSE.txt` | 156926 | `4573185d56580da2b890ba34a85a409257640f1c5632eade4300137266194d18` |
| 173 | `docs/phase-1-compatibility/backend-candidates-2026-10-04.json` | `173-backend-candidates-2026-10-04.json` | 228236 | `a9e5485aeb506a8746787b77c2510da00983d4ad26da146790bf3a7187008bc0` |
| 174 | `docs/phase-1-compatibility/refresh-candidates-2026-10-04.json` | `174-refresh-candidates-2026-10-04.json` | 11337 | `7158f2d37ec06b116c474814193c7e9db85d9b4e61ff365c8b1eb6e554d24df2` |

## Correction 1 — bounded superseding disposition

Date: 2026-10-05. Independent reviewer: `/root/review_world_audio_v1`.
Verdict: **PASS for the current evidence reconciliation at the corrected identities below**.
CER-MED-001 is closed. Remaining actionable findings in this commissioned scope: 0.
Task status remains DOING; receipt uncommitted. The original REVISE, finding,
inspected claims and exhaustive original input identities above remain preserved.
This disposition supersedes that current-reconciliation REVISE only for the
verified correction; it does not rewrite or give a verdict to the historical
interrupted 61-input review.

### Exact correction inputs and preservation

Packet: `output/research/compatibility-evidence-reconciliation-2026-10-05/correction-1/review-inputs.json`.
SHA-256: `fa190559f05af597c7fb497ab1663e0db4fdd0d20a2b1b29b8c0d2a0112d2b7f`;
1,012 bytes. Snapshot paths in this table are relative to that correction folder.

| Input | Bytes | SHA-256 |
|---|---:|---|
| `backend-evidence.before.md` | 12,407 | `f04d8fbf7330ae9d58a135c92cd745c0c973f472791929c96ebe17555ea21061` |
| `backend-evidence.corrected.md` / canonical `docs/phase-1-compatibility/backend-evidence-2026-10-04.md` | 12,960 | `53eb8f8f6b36ec5e2d17c76266f8780a05b0ff64464142f4a575626a90b7fa18` |
| `correction.patch` | 2,244 | `e3b42eba94e27a1894b66c84e6b562fbcb88ef28f7027e03c8d7639639f60118` |

Independently recomputed each correction hash/size and byte-compared the corrected
snapshot to the canonical producer file. The before snapshot exactly equals
original frozen input 000. Independent line comparison finds only the two intended
paragraph replacements: original lines 123–125 become corrected 123–127;
original 177–178 become corrected 179–186. All other lines retain their exact
bytes, including unchanged LF encoding. The independently computed two-hunk
unified diff agrees with the saved patch content after line-ending normalization
of the patch representation; no third hunk or hidden producer-body change occurs.

The original manifest still has exact SHA-256
`c879a4577ebb334d110c11b9f1eb53f889345ac0d86f130a25611e1fc483bb06`.
All 175 original snapshots retain their recorded hashes/sizes, and all **174 other
original canonical inputs** remain byte-identical to their snapshots. Only the
canonical backend producer now uses the corrected identity explicitly listed
above. The receipt's complete pre-append body was verified at SHA-256
`1507751904441ff9aa0c58d8b56fe54f756a2b6ef4c01e4258b1e133440e4d58`
and is preserved as an exact byte prefix. No original receipt finding/input row
was edited or silently relabeled.

### Finding closure and limits

Corrected backend lines 123–127 no longer assume Linux is the production OS.
They accurately limit this Windows observation and retain the distinction
between the snapshot's no-extra edge flags and the separate resolver evidence.
Corrected lines 179–187 retain actual-target Python support/ABI, JWT crypto,
Uvicorn extras, database/libpq and focused behavior/suite obligations, while making
hosting GA and production OS/packaging graphs conditional on the later approved
target when D-068 planning resumes. Azure/AWS remain candidates; no host, OS or
container requirement is selected by this correction.

The paragraph explicitly retains applicable immutable-artifact/image-digest
controls, Entra identity and the approved Azure EU personal/confidential AI route.
Non-preview supported selection, complete extras/transitive closure, reproducible
hash-locked installation, build/SBOM/licence/advisory evidence, reversible waves,
rollback and MA-013/full Phase 1 gates are unchanged. No permission or production
policy is weakened. This closes the specific authority mismatch rather than
waiving future target evidence.

Review work was limited to exact correction/preservation checks and comparison
with the already inspected governing authority. No broad study, resolver, native
checker, archive/audit or application test was repeated; unchanged evidence
retains the bounded assessment above and earlier receipts retain their scopes.
Only this receipt was appended. PASS accepts current evidence accuracy and its
corrected authority wording; it does not accept the full stable production graph,
legal/distribution clearance, installed/runtime compatibility, MA-013, founder
approval, full Phase 1, implementation or provider/deployment permission.
