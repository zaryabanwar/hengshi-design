# Native React lint evidence review — v1

Date: 2026-10-04. Independent initial review. Disposition: **REVISE**.

## Commissioned scope and authority

This receipt reviews only the stable React-lint alternative investigation, protected-source inspection and recommended-coverage portions of `refresh-evidence-2026-10-04.md` (lines 138–267 at the input hash below), the four commissioned native-lint JSON records, and their referenced retained metadata, configuration, fixtures, package/lock and unpacked tool bytes. The whole-file hash identifies the reviewed bytes; it does not extend this verdict to the other sections. AGENTS.md and constitution principles V, VII and VIII require stable compatible technology, evidence and independent review. This is evidence review, not application feature implementation or a founder acceptance.

The previous inventory, native-operation and notice receipts retain their scopes. The earlier errored 61-input review is not superseded. No production compatibility graph, production preset, licence/provenance clearance or compatibility exception is accepted.

## Finding

**NATIVE-LINT-MED-001 — Medium — strict resolver execution is not reproducibly evidenced.**

`docs/phase-1-compatibility/refresh-evidence-2026-10-04.md:155` calls this a “Strict lock-only resolution”; `output/research/compatibility-resolution-2026-10-04/native-lint-study-analysis.json:6` records only `npm_resolution_exit: 0`. The retained native `exit-code.txt:1` is 0, and `resolver-output.txt:2` says “up to date in 2m”. Neither identifies the actual native resolver argv or effective strict-peer, legacy-peer, engine-strict and force configuration. No native command/options receipt was found in the referenced evidence. The earlier separate resolver study used different inputs and cannot establish this invocation.

The 303-record candidate lock and absence of prerelease versions are independently verifiable. This finding does **not** allege a failed resolution or prerelease content. It prevents the stronger claim that the native candidate passed an explicitly strict resolution.

Required correction: preserve original candidate and diagnostic evidence. Record a separate isolated manifest-only, lock-only strict recheck with exact input identities, cwd, tool versions, actual argv, nonsecret effective configuration (explicit `strict-peer-deps=true`, `legacy-peer-deps=false`, `engine-strict=true`, `force=false`), stdout, stderr, exit and output hashes. Avoid installation/lifecycle execution and application changes. If its graph differs, identify that graph separately instead of presenting it as the original 303-record graph. Bind any corrected claim to the new exact evidence and retain the distinction from complete compatibility acceptance.

## Independent observations

### Candidate/channel and byte provenance

The retained candidate lock has 303 package records including its root, and no prerelease version strings. Its root is `hengshi-v1-compatibility-study` version 1.0.0. ESLint is 10.12.0 and Oxlint is 1.86.0. This establishes the retained inventory; strict invocation proof remains the finding above, and stable versions alone do not select a complete coupled graph.

The retained 27 Babel 7 metadata records all require `gensync ^1.0.0-beta.2`. Inspection of the exact published `eslint-plugin-react-hooks 5.2.0` archive as data confirms its ESLint peer range ends at major 9, exports only the two named hook rules, and its `isUseEffectEventIdentifier` helper returns false. This supports the bounded rejection of that downgrade, alongside [ESLint's official support policy](https://eslint.org/version-support/); it does not establish every alternative's compatibility.

I retrieved the exact public npm archives into memory, verified their SRI against retained registry metadata, and compared every package file to the retained unpacked bytes and provenance hashes. No archive code was installed or executed during this comparison.

| Package | Archive bytes/files | Independently computed archive SHA256 |
|---|---|---|
| oxlint 1.86.0 | 378910 / 18 | `F5A58924F3902FACE87161725A1EBD4004E276913A8102543B53DEC8077829FC` |
| @oxlint/binding-win32-x64-msvc 1.86.0 | 5818980 / 3 | `285216864359F8CEA7A53EDF25B78E0E4D400DC532DA8835EF772C674940A065` |
| eslint-plugin-react-hooks 5.2.0, supporting source inspection only | 8 files | `4BD34C576DFBC6E449360A0DCDFA70DC1B592F83125198531C390D545DF240AA` |

Both Oxlint packages have zero archive-versus-unpacked byte mismatches and zero provenance-receipt hash mismatches. The native binding is 13284352 bytes, SHA256 `799188EA3137224A71B7AD085229AF72330FF7938B44656D38413DD9E7CC700A`. This is published-package byte correspondence, not a source-to-binary build attestation, signature review, vulnerability clearance or licence grant/attribution clearance.

### Actual checker executions

The already-unpacked Windows tool reports `Version: 1.86.0`. I ran its CLI through the installed Node executable, using the retained probe configuration and the following arguments after the tool path:

```text
--config <native-lint-probe>/probe-config.json
--allow all --deny react/rules-of-hooks --deny react/exhaustive-deps
--no-ignore --format json <exact fixture or protected source>
```

The JSON config enables the React plugin and only the two named stable rules. No fix option, installation, lifecycle, compiler-rule activation or application execution was used. Expected outcomes came from [React's hook rules](https://react.dev/reference/eslint-plugin-react-hooks/lints/rules-of-hooks) and [Effect Event contract](https://react.dev/reference/react/useEffectEvent), rather than copying checker logic.

| Exact fixture | Expected/observed exit | Actual diagnostic |
|---|---|---|
| valid-hooks | 0 / 0 | none |
| conditional-hook | 1 / 1 | rules-of-hooks |
| missing-dependency | 1 / 1 | exhaustive-deps |
| conditional-use | 0 / 0 | none |
| effect-event-valid | 0 / 0 | none |
| effect-event-in-deps | 1 / 1 | exhaustive-deps |
| effect-event-during-render | 1 / 1 | rules-of-hooks |
| effect-event-as-click-handler | 1 / 1 | rules-of-hooks |

All eight runs report exactly two active rules and empty stderr. Every diagnostic object matches both the retained aggregate and corresponding raw fixture JSON; timings are not asserted equal. These are actual CLI diagnostic cases on synthetic source, not browser behavior or an application React render.

The three protected source checks also reproduce the retained diagnostics, two active rules and empty stderr, with exact source hashes unchanged before and after:

| Protected source | Actual exit/result |
|---|---|
| WorldCanvas.tsx | 0, no diagnostic |
| ExteriorScene.tsx | 1, missing `applyKeyframe` dependency; source use at line 138 and dependency array at line 193 |
| WorldHUD.tsx | 1, conditional `useMemo` at line 48 after the return at lines 44–45 |

This corroborates the R-003 source lint observation and separate exterior dependency observation. It neither repairs R-003 nor demonstrates a runtime regression/fix, application authorization, accessible journey, streaming, free movement or production performance.

### Coverage limits

Re-running `--rules --format json` produces exit 0, empty stderr and raw stdout SHA256 `2A8DDFDA57F9BAA5F855F45F8A1F9C319CD357ABAB0A94C64641BC9CEF6CB98D`, identical to the retained inventory hash. All 17 entries in the recommended-coverage record match the actual inventory's identifiers/metadata. Fourteen share identifiers: the two exercised rules plus twelve compiler-related matches. The exact identifiers `component-hook-factories`, `config` and `gating` are absent. No renamed or aggregate-rule equivalence is inferred.

The twelve compiler-related rules remain experimental and were not enabled, consistent with [Oxlint's plugin documentation](https://oxc.rs/docs/guide/usage/linter/plugins.html) and its corresponding rule pages. The [React recommended set](https://react.dev/reference/eslint-plugin-react-hooks) is broader than this two-rule probe. Full parity is not established. The producer correctly holds production preset selection, retained core/TypeScript/refresh checks, owned-source coverage, custom hooks/import aliases, editor/CI behavior and safe fixes. The probe is not a production coverage waiver.

## Artifact integrity and scope limits

All 70 input identities below were independently recomputed and rechecked unchanged before writing this receipt. The five protected application dependency baselines also match the retained protected-input record. Those hash comparisons are integrity checks, not feature tests. This receipt does not validate schema fixtures as application persistence/publication behavior; it does not claim runtime app tests, complete production compatibility, licence clearance, installed candidate contents, source-build provenance or readiness. No candidate was installed, no protected source/config/lock was edited, and no credentials, providers, processes, migrations or application features were changed. Real dependency and technical format versions remain accurate; the product/definition remains v1.

## Exact reviewed input identities

Paths are repository-relative. SHA256 is over exact retained file bytes.

| Input | Bytes | SHA256 |
|---|---:|---|
| `docs/phase-1-compatibility/refresh-evidence-2026-10-04.md` | 30962 | `BEBB97B3679A23EBE5136D04AA085BA1E5984BFCCC6F1800F8CCDC1B0654BC13` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-study-analysis.json` | 1665 | `988AAB79C92F663AFB3953E4860D50944C50DE9C20BF51E0ACC5779099E92401` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-behavior-probe.json` | 13477 | `7F17D668DFB445DF7A877452162E827D4E360E263EA3952EFF3E523BC866D138` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-protected-world-inspection.json` | 5863 | `B199BF247A3C4F07136F32D661D468050CEC12369697E28F669E8F59305E06B8` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-recommended-coverage.json` | 16889 | `86BBE2D8E65BDE10D1719CD2C822E8739E4DE78FB0F1590451749E0A920CA123` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-metadata.json` | 2466 | `A0206E039A74610503F56F0F9D64975D6CF2AC634F1CCAB8B6C74AA0C89FB88B` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-win32-metadata.json` | 2456 | `FDBF0298CDB452F2379A29BF9E91D1CBD7873D2831046D581FD085F4F4A7FACD` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-tool-provenance.json` | 4013 | `8F55E1327D1D3BB9AD1DE80AEEB95EAB7F96FF1349C49A334EA1BE4355A3E984` |
| `output/research/compatibility-resolution-2026-10-04/stable-lint-babel-range-evidence.json` | 43646 | `BCB6E2EFAEE736154BCA476F733976D640B68106111E9A8CDE860EB23C3518DE` |
| `output/research/compatibility-resolution-2026-10-04/stable-lint-package-metadata.json` | 48094 | `C5DD839EB15C425D0EA608DC580EDC45481635387140C162BAF1915D431D707B` |
| `output/research/compatibility-resolution-2026-10-04/stable-lint-source-observations.json` | 8888 | `034E0BF67C05641A23851186626152971960E33F5FEB319AECA52F2D6D325BF1` |
| `output/research/compatibility-resolution-2026-10-04/protected-input-hashes.json` | 481 | `8F15A53BC1BF2C0CB92F536624E955B06725BC31B5BFF3007D8B2729527A0661` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/conditional-hook-output.json` | 852 | `B9B9D688C7733369B453367AA6E6BA11D90FC4F66937B1C4002E811FF324AF62` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/conditional-hook-stderr.txt` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/conditional-use-output.json` | 197 | `9D644A9B46E4CEBC8C5BE70EC4BC4470806FD974516A5D5B43447E6C2B12F2E0` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/conditional-use-stderr.txt` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/effect-event-as-click-handler-output.json` | 814 | `EFEA181E0B48AA662711D847118BABD3FCCCFAE6EBDB79A393F5E65ACACA6277` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/effect-event-as-click-handler-stderr.txt` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/effect-event-during-render-output.json` | 759 | `7920B71EEF7B36D5DAD6F49AB122070999A1B8738C2B353795CA6B8011E2887B` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/effect-event-during-render-stderr.txt` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/effect-event-in-deps-output.json` | 690 | `BE2EE3C74475A69BDB05D8EF2F528FE7D6A885299AE15214853B7AE104FC01A3` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/effect-event-in-deps-stderr.txt` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/effect-event-valid-output.json` | 197 | `630E29D668C8FDF42AA69F6827A9C5C9BBC4C8F8E2B36E44E96682C6581B8CA2` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/effect-event-valid-stderr.txt` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/exit-code.txt` | 3 | `13BF7B3039C63BF5A50491FA3CFD8EB4E699D1BA1436315AEF9CBE5711530354` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/missing-dependency-output.json` | 757 | `B69ABA43156ED86E662069D8D4603F2799768904535BECC7C482B0B3F4049783` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/missing-dependency-stderr.txt` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/package-lock.json` | 162581 | `DA45DD6CB7CEE7834FC5985B6595C2111780EE24D7CF87D1BDAF1749BE3F37AB` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/package.json` | 1166 | `F1ECB8D6083BACB65684DEF851C69A9066618534DDFC62B088FD7242E29EB69E` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/probe-config.json` | 136 | `62F9D0789FBCBD0C4232B4A70CF972A3E8084BD21A7C194BEB86393C27EDF431` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/resolver-output.txt` | 20 | `6C6100B1E38130900F947B09DBA989B4FE8C8D23FF8AD5D1C1FB61CDC98A202F` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/valid-hooks-output.json` | 197 | `7524934340599F35B7D3A2A6FF8C7CEDBDB0A426815829F5A1A73B9D3257ED99` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/valid-hooks-stderr.txt` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/fixtures/conditional-hook.tsx` | 163 | `DBE025A6B36BA677B43E225911BD29AD134DA2DC25250A405B989E9866CE1E38` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/fixtures/conditional-use.tsx` | 142 | `B06D92F2C3C05793CFFADB94F464C39DEC272E08556EE04B7EFFEB4B90CD7373` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/fixtures/effect-event-as-click-handler.tsx` | 182 | `5D5601045578223A84FF3F76E1315AA59A2079945D1C157679B1FC329B53AEEF` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/fixtures/effect-event-during-render.tsx` | 154 | `66D747CEE459CF89ED8A0BD12DF0CEED5701DF3E4BE3869395968EC43A308304` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/fixtures/effect-event-in-deps.tsx` | 196 | `FA72507867708DABDADCDD87AAA0912CBA30175D348E2315BB5D543F24572960` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/fixtures/effect-event-valid.tsx` | 185 | `1607706EA843C19E926F24711173B20A980F17EA585C326E9AA03820875F44DF` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/fixtures/missing-dependency.tsx` | 120 | `893F0A2A3CB9D4056C74E81E7B48F677E88DFDA7F6E51AD62369CA9B306EBB6E` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/fixtures/valid-hooks.tsx` | 163 | `0D94F59F497B0E0AFAE4510A8C11E3D6898382A4E2F0F08DE2FFA0FA204EDF2A` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/tool/node_modules/oxlint/configuration_schema.json` | 763718 | `E15361EFF2CEFCC8AFAC585351981315BD0275A04B19E930F35B575A1FAEA1E0` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/tool/node_modules/oxlint/LICENSE` | 1119 | `95CED5ECF1133FBF41D409B5555C86C344F83F3B019926057DDBC07CFDCC27B3` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/tool/node_modules/oxlint/package.json` | 3096 | `74705E78A65F1272491481987357B1E1A8FF999C8B2A7D029276C05CD9256382` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/tool/node_modules/oxlint/README.md` | 2502 | `1E2175A447DC67ABFE4B712E1A706EC357F9F7131E544C05A3CCBA88EB4A40D7` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/tool/node_modules/oxlint/bin/oxlint` | 46 | `ECAB4E2F1BEBAAB1A3306620BEE562EC16E8CB83DD5FB739B94A5AAE3C9E34BD` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/tool/node_modules/oxlint/dist/bindings.js` | 24942 | `5693F32A8103DA80016EA9D2AAD4AE95318EBA40CA226721721192AED322FD7D` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/tool/node_modules/oxlint/dist/cli.js` | 4255 | `0DB31AEED17873535FDC4215CB496980701D4A0E0BEA0DB335D30415A163158D` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/tool/node_modules/oxlint/dist/index.d.ts` | 254303 | `DFECA985972E516966339D4CCEFA6E158D3ECB7B7AB47B0D88C0C10A5EEEFB3F` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/tool/node_modules/oxlint/dist/index.js` | 253 | `BCD7D20DA966AD0DAF2BBB9386D2F3E325E68A9B33C695DE240D4A69E7B9F59A` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/tool/node_modules/oxlint/dist/js_config.js` | 7508 | `27596DA272E54931618D1B959BECDF200D6B992F972B831A54026D8352EA4BDC` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/tool/node_modules/oxlint/dist/lint.js` | 1145886 | `0F14570575CDA93E5E58DDA814CB6C5B2CD58F8F59504CFBFBB515778EB02681` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/tool/node_modules/oxlint/dist/plugins-dev.d.ts` | 160690 | `2FA3E1D5FDD954EDBA75D2A57193EB94B7FB7A62C0C8D6E2E27B03253DCE38A6` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/tool/node_modules/oxlint/dist/plugins-dev.js` | 41272 | `9160DBC594C8F9FA6E624CC358CB2093DC19281C5233168F0352203FC11B5C16` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/tool/node_modules/oxlint/dist/plugins.js` | 940 | `81E4C275F6200AB4B6AED66BA2836B2A8E68756A8609CED02DAF91E226377E2D` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/tool/node_modules/oxlint/dist/rolldown-runtime.js` | 1506 | `5FC650D7F3C5B72629DA633623BF7BC72FD972051FE82268C703B2681F26EB51` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/tool/node_modules/oxlint/dist/utils.js` | 1057 | `591682F61F6FF1EE264F9DF278C71EB4F8F426D34F7EA9B14F77DBD30C989778` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/tool/node_modules/oxlint/dist/workspace.js` | 289 | `07D934175FFA28DEDBFFF3BA1B16BB96158D7FB9C5EBCDD91B7AD6FB1DF4C160` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/tool/node_modules/oxlint/dist/workspace2.js` | 1017 | `BFC5EFA892C05854DFC783625A03087861CBEAD465FE72C1DCF96E2C01629061` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/tool/node_modules/@oxlint/binding-win32-x64-msvc/oxlint.win32-x64-msvc.node` | 13284352 | `799188EA3137224A71B7AD085229AF72330FF7938B44656D38413DD9E7CC700A` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/tool/node_modules/@oxlint/binding-win32-x64-msvc/package.json` | 743 | `3C2A11004627A12CED4B8DAD6B7D2F91C61AF25E929432E47AE42F5715726156` |
| `output/research/compatibility-resolution-2026-10-04/native-lint-probe/tool/node_modules/@oxlint/binding-win32-x64-msvc/README.md` | 104 | `295B1FBFB009D78D3234658E3140DA9AF1B33CBF0017EF976743A39FA43C0314` |
| `apps/web/src/world/WorldCanvas.tsx` | 5704 | `8A13414D7CF091584841F278C6FBB9B19A65ADF06073DCCF49F071CB42D66847` |
| `apps/web/src/world/WorldHUD.tsx` | 4574 | `A95C352FB7BDD4B9CF4351E98BBEB730CE8200745F62C3A835F69D67F12EBB24` |
| `apps/web/src/world/ExteriorScene.tsx` | 6649 | `CCA5F46A456DCB29362BF2FB89AB4052727F0AF37501ABEF16BA50E9BC74CBC0` |
| `package.json` | 538 | `A07F9F12C83736625D621781A1B30C8430452EF7E698FA626902CF16CEF7946B` |
| `package-lock.json` | 76835 | `D2DA4D7206344BA45645D7BAFE4EC692BB738EA0C1C98C2680522688B5733908` |
| `apps/web/package.json` | 1136 | `83E4178348EC081922DD3D53D00C51446B655091D056EC09DDE52A2496B04E2A` |
| `apps/web/package-lock.json` | 179000 | `35486FB012489DE4C3B363198304A25F44A0396707DB328190D7E056C06D416D` |
| `apps/api/requirements.txt` | 137 | `B99F98E119CB6653F38B19D1EE83CC7F33D92A699083645CA19369A8912E89BD` |

## Disposition

**REVISE** for NATIVE-LINT-MED-001. The diagnostic, byte-correspondence and bounded coverage observations above are substantiated for these exact inputs. A corrected strict-resolution claim requires a fresh exact-hash review; it cannot silently replace this initial receipt. No canonical phase status was amended.

