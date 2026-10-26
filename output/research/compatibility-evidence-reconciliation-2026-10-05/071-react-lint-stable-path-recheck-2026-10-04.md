# Independent React lint stable-path recheck — 2026-10-04

Disposition: **PASS, initial candidate**, for the new narrow registry/range recheck. Reviewer: independent agent `/root/review_publication_contract`. No actionable finding or revision was required. Only this new receipt was written; older reviews and producer/application inputs remain unchanged.

Scope: the new “Current React lint stable-path recheck” section of refresh-evidence-2026-10-04.md, its seven-key observation set, range analysis and four saved registry responses. The producer document's whole-file hash identifies inspected bytes but this receipt does not freshly approve its other historical resolution, native-lint or archive-inspection sections. Current AGENTS/constitution latest-mutually-compatible stable policy remains controlling; no compatibility exception is granted.

## Independent findings and verification

The saved official [hook-plugin registry](https://registry.npmjs.org/eslint-plugin-react-hooks) identifies 7.1.1 as latest and the highest published version without a prerelease identifier, declaring @babel/core `^7.24.4`. The [Babel registry](https://registry.npmjs.org/@babel%2Fcore) contains exactly 27 non-prerelease versions satisfying that range, all declaring gensync `^1.0.0-beta.2`. Babel latest 8.0.6 does not satisfy the hook range. The [gensync registry](https://registry.npmjs.org/gensync) contains only 0.1.0 without a prerelease identifier; it does not satisfy any of those Babel gensync ranges. Latest points to 1.0.0-beta.2, which remains a prerelease observation, not an allowed production selection.

All four raw response hashes match their observations. Latest version, publication time and captured dependency/peer/engine/license/distribution subsets match saved records; distribution metadata is a deliberately narrower subset than the complete registry dist object. Fresh independent HTTPS reads of the four official registry endpoints confirmed the recorded latest tags and captured subsets. Hook/Babel/gensync version-key sets also matched the saved responses, and the live records retained all 27 Babel dependency declarations. The [oxlint registry](https://registry.npmjs.org/oxlint) observation remains metadata only; no native lint equivalence or runtime suitability follows from it.

The range analysis's input hash and npm-bundled node-semver **7.7.4** package/source identity match the local tool. Independent in-memory recomputation from the raw saved registries reproduced all 27 result records, including null stable gensync matches and rejection of Babel latest. The installed caret source was inspected alongside [official node-semver semantics](https://github.com/npm/node-semver#caret-ranges-123-025-004). A prerelease comparator is not intrinsically beta-only: a hypothetical final gensync 1.0.0 satisfies this caret, whereas the actually published stable 0.1.0 does not. The finding is current published availability, not an assertion that a future final release could never satisfy the range. The earlier exploratory semver 5.7.2 check is not the recorded analysis evaluated here.

[React's current recommended rules](https://react.dev/reference/eslint-plugin-react-hooks) include compiler diagnostics even when the application has not adopted the compiler. Two native hook checks or removal of compiler checks cannot establish equivalence to that complete recommended preset. This recheck selects no native/experimental substitute, EOL downgrade, force/override, custom rebuild or prerelease exception. “Stable” here means published non-prerelease/channel metadata within the examined chain; it does not prove maintenance, complete transitive stability, security, provenance, installation or runtime compatibility.

The five protected dependency-input hashes match the evidence snapshot. No resolver rerun, candidate installation, React/Babel/oxlint package execution, application lint/build/test, service or dependency mutation was performed. The only executed package logic was the existing npm-bundled semver tool for metadata range recomputation. These are artifact integrity and range observations, not product tests. Full-graph resolution, supply-chain/security review, runtime/preset evidence, reproducible production lock and founder/integrated Phase 1 acceptance remain unestablished. Earlier incomplete reviews, held QA exception and other production/design gates retain their scopes.

## Exact inspected SHA256

Repository-relative paths except the two explicitly absolute machine-local tooling paths.

| Input | SHA256 |
|---|---|
| `AGENTS.md` | `55405CB02A96D05F7F6D68E56A588D743F83877FB2691A5A9F2C736126ADBCC5` |
| `.specify/memory/constitution.md` | `33EC0BB02B0D0D9A55D0971589BD19F7242F5D56DA130F8F496BC1D31A8B5D23` |
| `docs/phase-1-compatibility/refresh-evidence-2026-10-04.md` | `65C3548B3D59537DE881949A9F231C8D146B9EAF2E4C5FB844FE62C193C9468B` |
| `output/research/compatibility-resolution-2026-10-04/react-lint-recheck-2026-10-04.json` | `2ADAB595DE7EF3497140A6781D4C7767CD796F913EF84573E6BF7CFC764C5ECD` |
| `output/research/compatibility-resolution-2026-10-04/react-lint-recheck-range-analysis.json` | `419C3DD27D6485FFC598542FE0DC9FAFCC33F565AF5847E384E4D087758B7FE6` |
| `output/research/compatibility-resolution-2026-10-04/react-lint-recheck-registries/babel__core.json` | `8D91E8A563D2A3F13A02715DCF6C9187AAAAE9F0C326884F207469CE6F485D2E` |
| `output/research/compatibility-resolution-2026-10-04/react-lint-recheck-registries/eslint-plugin-react-hooks.json` | `7F140E91E5C85EEC75F2E8ACDA41101EB271216FDE497195C2FCF2ADBA10C0DA` |
| `output/research/compatibility-resolution-2026-10-04/react-lint-recheck-registries/gensync.json` | `238627D88FBC228CA4B06BD4A40FFB74FC1E9B3F5B8DC5029C82AA16DAE24FA3` |
| `output/research/compatibility-resolution-2026-10-04/react-lint-recheck-registries/oxlint.json` | `31ED7121CA6ECFA9F984B0B345C2C039D67E01798116760B829EBB4C3594C29E` |
| `C:/nvm4w/nodejs/node_modules/npm/node_modules/semver/package.json` | `BA0D1B548512E65C15B1CDDBCD6CAA16CC9070E8AF8987D02BA929A1F06C0177` |
| `C:/nvm4w/nodejs/node_modules/npm/node_modules/semver/classes/range.js` | `CF8F8EB6934663AE2A9D04838D4D71555427A2ABD3C8748EE5219507969A6B46` |
| `package.json` | `A07F9F12C83736625D621781A1B30C8430452EF7E698FA626902CF16CEF7946B` |
| `package-lock.json` | `D2DA4D7206344BA45645D7BAFE4EC692BB738EA0C1C98C2680522688B5733908` |
| `apps/web/package.json` | `83E4178348EC081922DD3D53D00C51446B655091D056EC09DDE52A2496B04E2A` |
| `apps/web/package-lock.json` | `35486FB012489DE4C3B363198304A25F44A0396707DB328190D7E056C06D416D` |
| `apps/api/requirements.txt` | `B99F98E119CB6653F38B19D1EE83CC7F33D92A699083645CA19369A8912E89BD` |
