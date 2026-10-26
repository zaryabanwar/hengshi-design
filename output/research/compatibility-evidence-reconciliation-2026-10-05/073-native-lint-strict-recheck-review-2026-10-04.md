# Native lint strict recheck review — v1

Date: 2026-10-04. Independent correction 1 review. Disposition: **PASS**, limited to the recorded correction of NATIVE-LINT-MED-001.

## Scope and finding disposition

This receipt reviews only the corrected row at `docs/phase-1-compatibility/refresh-evidence-2026-10-04.md:155`, its “Recorded strict resolver correction” at lines 157–197, the executed script and new isolated recheck evidence, exact installed npm source relevant to option behavior, and correspondence with the original candidate and protected inputs. The whole-file hash binds the producer identity without accepting its other sections. AGENTS.md and constitution principles V, VII and VIII remain the review authority.

**NATIVE-LINT-MED-001 — closed for the corrected claim.** The producer now explicitly says the original resolver options were not retained. A separate recorded fresh resolution provides argv/configuration and reproduces the same lock bytes; it does not retroactively establish the original invocation. The initial [REVISE receipt](native-react-lint-evidence-review-2026-10-04.md), SHA256 `ABCE8AAD7ECC6E4611A93B9B2215BA8A8BD5743BD39A832D9A79F30E647BD490`, remains unchanged. Its producer bytes are preserved at their original hash `BEBB97B3679A23EBE5136D04AA085BA1E5984BFCCC6F1800F8CCDC1B0654BC13`.

No new actionable finding arises in this correction scope. The diff from preserved producer bytes contains only the replacement of the unsupported strict claim and this correction addendum. Prior review scopes, findings outside this correction and founder acceptance gates are unaffected.

## Independent inspection and correspondence

- Inspected `recheck_native_resolution.py` as source without executing it. It refuses to overwrite an existing study, creates a separate folder, copies only the original manifest, starts without a copied lock/node_modules, uses explicit empty user/global npm config files, and removes case-insensitive `npm_config_*` plus `NODE_OPTIONS` from the child environment. It records no environment values. Its subprocess is scoped to the new folder and records stdout/stderr and exit. Its writes are evidence/lock/cache writes; it contains no application/config mutation or dependency lifecycle execution.
- The receipt and actual npm debug log agree on the separate cwd, Node v24.14.0, npm 11.11.1, explicit argv and exit 0. Receipt timestamps are 13:32:57.947734–13:34:20.046073 UTC. The copied manifest is byte-identical to the original and matches its recorded SHA256.
- Actual argv contains `--package-lock-only --ignore-scripts --strict-peer-deps=true --legacy-peer-deps=false --engine-strict=true --force=false --workspaces=false`, includes dev/optional/peer dependencies, disables audit/fund, and explicitly sets the public npm registry and scoped cache/config paths. Both config files are empty; no project `.npmrc` or `node_modules` exists in the recheck folder on independent inspection.
- The installed npm CLI/config-definition hashes match the receipt. I inspected definitions for strict-peer, legacy-peer, engine-strict, force, ignore-scripts and package-lock-only, and configuration precedence/local-prefix behavior. CLI values override lower-priority configuration; disabled workspaces keeps the fresh manifest folder as local prefix. Installed `install.js:148` gates root scripts on ignore-scripts; Arborist `reify.js:272` returns before package materialization for package-lock-only and `reify.js:349` builds the ideal tree. Thus the recorded flags support this lock-only/no-lifecycle boundary.
- The exact installed `build-ideal-tree.js:182` distinguishes required and optional engine/platform checks: unsupported optional packages can be marked inert instead of causing failure. Therefore exit 0 is not proof every platform-specific optional package can execute on this host. It is the bounded resolver behavior of the recorded npm version.
- Official [npm install](https://docs.npmjs.com/cli/v11/commands/npm-install/) and [config](https://docs.npmjs.com/cli/v11/using-npm/config/) documentation were checked as primary context. They support the distinction between strict peer enforcement, disabling legacy resolution/force, and lock-only work. The live npm 11 docs now describe 11.21.0; exact installed 11.11.1 source, rather than newer behavior, governs this review.
- Independently parsed the new and original locks: both have 303 records including root, zero observed prerelease version strings, no package-record differences, and byte-identical SHA256 `DA45DD6CB7CEE7834FC5985B6595C2111780EE24D7CF87D1BDAF1749BE3F37AB`. This is a separate fresh observation yielding identical bytes, not proof of timeless registry reproducibility or a selected production lock.
- Recomputed all ten preserved application/source and original-study inputs: each matches both receipt before/after values and the original review. The five application dependency baselines also match `protected-input-hashes.json`. All other 69 inputs from the initial review snapshot remain byte-identical; only its canonical producer has the documented correction.
- The stdout hash matches its 18-byte output; stderr is **not empty**: its 212 bytes contain npm's available-update notice, and its hash matches the receipt. The exact debug-log hash matches the archive-observation JSON, including actual argv, cwd, versions and exit. No lifecycle-run lines were found.
- The log at line 1241 records a successful GET of the Tailwind WASI 4.3.3 tarball, matching the disclosed URL. The producer correctly avoids a metadata-only HTTP claim: npm fetched an archive to obtain bundled inventory. This fetch is not evidence of package installation, execution, licence clearance or source-build provenance. No fresh archive integrity/build review is added here.

## Retained limits

This review did not rerun resolution, installation, audits, the eight checker fixtures or application features. It inspected exact evidence and installed npm source read-only. The correction does not alter checker configuration, fixtures, native tool bytes or protected World source; their initial bounded diagnostic/coverage observations retain their original scope.

The graph remains unselected. Complete stable lint coverage, a production preset, application runtime behavior, browser/platform builds, accessibility, performance, vulnerability/licence clearance, grant/attribution and source-build provenance remain outside this verdict. Experimental compiler rules and the previously absent exact identifiers are not approved or waived. No founder compatibility exception, production lock, Phase 1 acceptance or MA-013 acceptance follows. No original GLB, credentials, provider settings, servers or canonical status was changed.

Artifact hashes establish identity/correspondence only; they are not feature tests or production-readiness evidence. The producer receipt's task status remains DOING and is not reclassified by this review. Product/definition naming remains v1; real schema and dependency versions retain their factual meaning.

## Exact reviewed inputs

Repository-relative paths identify evidence; `C:/nvm4w/...` paths identify the exact installed source inspected. SHA256 is over current exact bytes.

| Input | Bytes | SHA256 |
|---|---:|---|
| `docs/phase-1-compatibility/refresh-evidence-2026-10-04.md` | 34579 | `21F49D255E9D87D48D16DD216247B474F2E21C2F467B1D535A329D6A7B86A2A4` |
| `output/research/contract-review-reference-reconciliation-2026-10-04/refresh-evidence.pre-native-lint-review-correction.md` | 30962 | `BEBB97B3679A23EBE5136D04AA085BA1E5984BFCCC6F1800F8CCDC1B0654BC13` |
| `docs/phase-1-compatibility/reviews/native-react-lint-evidence-review-2026-10-04.md` | 21861 | `ABCE8AAD7ECC6E4611A93B9B2215BA8A8BD5743BD39A832D9A79F30E647BD490` |
| `output/research/compatibility-resolution-2026-10-04/recheck_native_resolution.py` | 6221 | `CC023409987551C03BA28E0C7A830290E52EC88728F02E3C3582028E613BC3D9` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-strict-resolution-recheck/receipt.json` | 5288 | `4502E1D0CE6814968B9C12435F726D173CA5BC520E3AC8347315169F7FDDE1AC` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-strict-resolution-recheck/package.json` | 1166 | `F1ECB8D6083BACB65684DEF851C69A9066618534DDFC62B088FD7242E29EB69E` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-strict-resolution-recheck/package-lock.json` | 162581 | `DA45DD6CB7CEE7834FC5985B6595C2111780EE24D7CF87D1BDAF1749BE3F37AB` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-strict-resolution-recheck/stdout.txt` | 18 | `2B2BBBF93489E72436A76087518C0EA9A2EDC890EC71F668ED8BB2124F488C60` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-strict-resolution-recheck/stderr.txt` | 212 | `E0FD7D2A46113FEC04FC2E28F48B8BEEEF0FB56CAE6010AA580F9DD6F1956706` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-strict-resolution-recheck/empty-user.npmrc` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-strict-resolution-recheck/empty-global.npmrc` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-strict-resolution-recheck/archive-fetch-observations.json` | 981 | `CEE233BC5B90AA960ECA9629AF29054759F76CC39C0DAF0D23EC3D7CDCE2CAC9` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-strict-resolution-recheck/metadata-cache/_logs/2026-10-04T13_32_58_384Z-debug-0.log` | 165469 | `C26B23762ED0A5FA4C80F7EC2FA8C37A3807748DC82DAF58D10DB791AAA7B345` |
| `output/research/compatibility-resolution-2026-10-04/protected-input-hashes.json` | 481 | `8F15A53BC1BF2C0CB92F536624E955B06725BC31B5BFF3007D8B2729527A0661` |
| `package.json` | 538 | `A07F9F12C83736625D621781A1B30C8430452EF7E698FA626902CF16CEF7946B` |
| `package-lock.json` | 76835 | `D2DA4D7206344BA45645D7BAFE4EC692BB738EA0C1C98C2680522688B5733908` |
| `apps/web/package.json` | 1136 | `83E4178348EC081922DD3D53D00C51446B655091D056EC09DDE52A2496B04E2A` |
| `apps/web/package-lock.json` | 179000 | `35486FB012489DE4C3B363198304A25F44A0396707DB328190D7E056C06D416D` |
| `apps/api/requirements.txt` | 137 | `B99F98E119CB6653F38B19D1EE83CC7F33D92A699083645CA19369A8912E89BD` |
| `apps/web/src/world/WorldCanvas.tsx` | 5704 | `8A13414D7CF091584841F278C6FBB9B19A65ADF06073DCCF49F071CB42D66847` |
| `apps/web/src/world/ExteriorScene.tsx` | 6649 | `CCA5F46A456DCB29362BF2FB89AB4052727F0AF37501ABEF16BA50E9BC74CBC0` |
| `apps/web/src/world/WorldHUD.tsx` | 4574 | `A95C352FB7BDD4B9CF4351E98BBEB730CE8200745F62C3A835F69D67F12EBB24` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/package.json` | 1166 | `F1ECB8D6083BACB65684DEF851C69A9066618534DDFC62B088FD7242E29EB69E` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/package-lock.json` | 162581 | `DA45DD6CB7CEE7834FC5985B6595C2111780EE24D7CF87D1BDAF1749BE3F37AB` |
| `C:/nvm4w/nodejs/node_modules/npm/bin/npm-cli.js` | 54 | `8E5F6F3429F8CDBE693CDC29904E9D5A7B127A494BD15C804BD54C7403BFCBE7` |
| `C:/nvm4w/nodejs/node_modules/npm/node_modules/@npmcli/config/lib/definitions/definitions.js` | 79913 | `CB921B25B4A059218FA70F7080D059889307DC1144FD809DABE4813A22F6BEB2` |
| `C:/nvm4w/nodejs/node_modules/npm/lib/commands/install.js` | 5221 | `5B6B08D68827A73812328321129E0AA99539F2D3B54A7B08ECF7CA53350B4E57` |
| `C:/nvm4w/nodejs/node_modules/npm/node_modules/@npmcli/arborist/lib/arborist/reify.js` | 60651 | `60C5AEB8CC69C1B429EAF8477D96C50D30ABDF4A64CBF42E0154AAD5146A9CF8` |
| `C:/nvm4w/nodejs/node_modules/npm/node_modules/@npmcli/arborist/lib/arborist/build-ideal-tree.js` | 58380 | `AE6809D5AB55BFABC7B1C3064E8DFA78B1A5F7F36F67DE5CCE85F70C71654C60` |
| `C:/nvm4w/nodejs/node_modules/npm/node_modules/@npmcli/config/lib/index.js` | 31757 | `464B3D63668C25C03874903B9809F97FA4508864541BC4B75ADC9F4067893CB7` |
| `C:/nvm4w/nodejs/node_modules/npm/package.json` | 6570 | `E5BDE8BE0C9E77EF3D83370C83CEF598B04C61FA785DFFBECF394B31CBC457CA` |

## Disposition

**PASS** for correction 1 and closure of NATIVE-LINT-MED-001 at these identities. The initial receipt remains historical REVISE. This receipt accepts only the corrected strict-recheck evidence and its exact correspondence; all broader approvals remain separate.

