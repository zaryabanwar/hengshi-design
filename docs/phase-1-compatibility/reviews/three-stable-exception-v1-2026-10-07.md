# Three stable exception bounded review — 2026-10-07

Status: DOING; uncommitted. Verdict: **PASS** for the exact frozen proposal's evidence accuracy and exception interpretation only. No consequential finding or actionable revision established; initial review, zero revision cycles consumed. This is not founder approval, exception adoption, acceptance of a candidate lock or selection of the complete compatible stable graph.

Scope: the narrow proposed root Three 0.184.0 / @types/three 0.184.1 exception, the related frozen registry refresh, and the two prior exact-scope declaration/remedy receipts. AGENTS and constitution were read first. Previous compiler/build/browser reviews retain their stated finite authority; they were inspected, not expanded into a new whole-graph review. Historical workspace-credit review notes are prior capability evidence, not a present failure or substantive amendment. No current-source-wide verdict is given.

## Exact frozen identities

Packet: `output/research/three-upstream-recheck-2026-10-07/`. Manifest `review-inputs.json` SHA-256: `ba806466968eef67389fc39bebeeeb7209120142e6b72df75847536470cf00f0`. Its six records use `source`, root-relative `copy`, and `sha256`.

| Source | Frozen copy within packet | SHA-256 |
| --- | --- | --- |
| docs/phase-1-compatibility/THREE_STABLE_EXCEPTION_PROPOSAL.md | 00-THREE_STABLE_EXCEPTION_PROPOSAL.md.reviewed | f7910af840cc2badea8c2fed9e2407fec3a4e1b0a097ff7e6dd9fa1deccc90c3 |
| docs/phase-1-compatibility/refresh-evidence-2026-10-04.md | 01-refresh-evidence-2026-10-04.md.reviewed | 4adcd4a490cd5dad15bfecc76b70b91cb6a4e1a08a2c23b8d17969d10e9ffed1 |
| AGENTS.md | 02-AGENTS.md.reviewed | 55405cb02a96d05f7f6d68e56a588d743f83877fb2691a5a9f2c736126adbcc5 |
| .specify/memory/constitution.md | 03-constitution.md.reviewed | 33ec0bb02b0d0d9a55d0971589bd19f7242f5d56da130f8f496bc1d31a8b5d23 |
| docs/phase-1-compatibility/reviews/frontend-candidate-declaration-gate-v1-2026-10-06.md | 04-frontend-candidate-declaration-gate-v1-2026-10-06.md.reviewed | 1013a8ed5689eaf67a294c4da9cfeb15a17abfafe3bcc360eadbcddabcf38df0 |
| docs/phase-1-compatibility/reviews/frontend-three-remedy-evaluation-v1-2026-10-06.md | 05-frontend-three-remedy-evaluation-v1-2026-10-06.md.reviewed | d6e8f8c65394986fd4a74550e728d065e14583566c10b6c259c2bfad8d07269f |

Initial and final review verification on 2026-10-07 matched the manifest and all six frozen hashes. Read-only PowerShell reproduction: `Get-FileHash -LiteralPath <manifest> -Algorithm SHA256`, then parse its JSON and apply `Get-FileHash` to each exact `copy`; compare lowercase digest with `sha256`. Hash equality establishes artifact identity only. Snapshot bytes were preserved.

## Independent primary-source and archive checks

The five saved official registry response hashes match `observations.json`. Live read-only official registry retrieval on 2026-10-07 independently confirms both latest tags and numerically greatest stable version keys: Three 0.186.1, @types/three 0.186.0, three-stdlib 2.36.1, Drei 10.7.9 and Fiber 9.8.1. The greatest published stable patches in the respective 184 lines remain Three 0.184.0 and types 0.184.1. Primary sources: [Three registry](https://registry.npmjs.org/three), [types registry](https://registry.npmjs.org/@types%2fthree), [stdlib registry](https://registry.npmjs.org/three-stdlib), [Drei registry](https://registry.npmjs.org/@react-three%2fdrei), [Fiber registry](https://registry.npmjs.org/@react-three%2ffiber). These are observations, not a selected stack.

The current stdlib 2.36.1 registry publication time is 2025-11-10T21:21:28.049Z. [Official upstream PR 433](https://github.com/pmndrs/three-stdlib/pull/433) confirms the relevant declaration correction merged on 2026-06-26, commit `e0e835a267afd01d318c5ea532732af0235872da`. The closed issue/merged PR does not establish a released npm correction.

Read-only Python checks parsed registry JSON, computed SHA-512/SHA-256, and read archive members in memory with `tarfile.extractfile`; no archive extraction or package installation was performed. The saved published archive passes registry SHA-512 SRI verification and its SHA-256 is `e246431950e1f73bad0f217ab928f1e66b08fc4e003e50ed5ce6817a8150c0cc`, matching `source-comparison.json`. Both declaration members equal the saved published files and the previously failing installed files. Each differs from the saved exact-merge counterpart. Live retrieval of the two immutable merge-commit files equals the saved corrected bytes: [SVGLoader declaration](https://raw.githubusercontent.com/pmndrs/three-stdlib/e0e835a267afd01d318c5ea532732af0235872da/src/loaders/SVGLoader.d.ts), [TGALoader declaration](https://raw.githubusercontent.com/pmndrs/three-stdlib/e0e835a267afd01d318c5ea532732af0235872da/src/loaders/TGALoader.d.ts).

| Declaration | Published SHA-256 | Exact merged SHA-256 |
| --- | --- | --- |
| SVGLoader.d.ts | 5a8aa1adc0a8d6cf8a106fd8cc422e28ca130292d452b75d17678d24ab31626b | fcefcd784c75aa779261794c9e9227bb726aa4a80097dc13e86f33a0b99a8803 |
| TGALoader.d.ts | f856d3559afde2a5e3f0e4e877d0397fe673eea71ac3683abb7c6cef429c192d | 5224c60ffc7578678242487686f9cb0177345a33dc29ce85d89bdd6c62a8677a |

The comparison confirms unreleased source differences, not archive provenance/signature, advisory, licence, runtime or full-graph clearance. No compiler, build, browser, installation, upgrade, schema test or prose test was repeated during this review or receipt preservation. No capability blocker occurred.

## Frozen-file findings and disposition

All file names below refer to the exact packet copies above, not moving canonical documents.

- `00-THREE_STABLE_EXCEPTION_PROPOSAL.md.reviewed:14–29` and `01-refresh-evidence-2026-10-04.md.reviewed:1292–1302`: the newest evaluated published candidate remains blocked at its strict public-loader declaration gate. Identical published declarations preserve the applicability of the prior TS2430/TS2416 failure. Optional SVG userData and TGA parse return incompatibilities agree with the official upstream correction. Neither peer ranges nor a merged fix justify calling that npm candidate compatible.
- `04-frontend-candidate-declaration-gate-v1-2026-10-06.md.reviewed:31–47`: the failed-candidate receipt independently reproduced the strict checker controls, retained initial fixture/import corrections and kept runtime/full-graph acceptance held. It establishes the recorded candidate's rejection at that gate, not every possible future coupled graph.
- `05-frontend-three-remedy-evaluation-v1-2026-10-06.md.reviewed:32–48` and `00-THREE_STABLE_EXCEPTION_PROPOSAL.md.reviewed:7–19`: the proposed pair is the **newest proven-compatible evaluated matched line**, supported by the earlier finite checker/build/browser reproduction and bounded 185 declaration comparison. The receipt does not execute every historical patch, prove all graph combinations, or select older types with the newest runtime. This qualifier is essential to the PASS.
- `00-THREE_STABLE_EXCEPTION_PROPOSAL.md.reviewed:33–42`: founder approval would apply only to this dated exception. Complete graph/MA-013 acceptance, fresh latest-compatible resolution, reproducible locks, independent review, strict public-loader/actual coupled-fixture checks before the separately approved wave, failing controls and supply-chain evidence remain required. The candidate lock is not adopted.
- `00-THREE_STABLE_EXCEPTION_PROPOSAL.md.reviewed:46–54`: recheck no later than 2027-01-07, before adoption, and on a relevant stable helper release; continuing then requires a fresh founder decision. A later authorized wave restores its reviewed prior source, lock and generated assets together under its own rollback plan. The unchanged current application requires no rollback. These gates adequately bound this proposal; they do not execute an upgrade.
- `00-THREE_STABLE_EXCEPTION_PROPOSAL.md.reviewed:37–54`, `01-refresh-evidence-2026-10-04.md.reviewed:1262–1288`, and `05-frontend-three-remedy-evaluation-v1-2026-10-06.md.reviewed:38–48`: nested stats-gl Three 0.170.0 remains a distinct graph node; no cross-copy object sharing is approved. Clock warnings remain open. gensync 1.0.0-beta.2 remains within D-072's isolated development/CI React lint exception, expiring separately on 2027-01-05; absence from one observed JS module projection is not universal deployed exclusion or full D-072 conformance.

## Residual limits and authority

No consequential flaw was established in this narrow evidence interpretation. The disposition supports presenting the concrete temporary exception to the founder; it does not itself authorize adoption. Full stable graph/lock selection, MA-013, integrated Phase 1 and founder acceptance remain held. Required SBOM/provenance/licence/advisory/deployment exclusion, Clock resolution, GPU disposal/memory/context recovery, physical devices, Safari/Firefox, accessibility, actual campus/control/stream/audio, semantic publication, performance and production UI/security evidence remain outside this PASS.

Only this receipt was created in the preservation slice. Frozen packet, producer/candidate source/manifests/locks, protected prototype/models, other canonical documents, application, external design, machine/provider/account, Git history and goal state were not changed. The parent coordinator owns any separate checkpoint update. DOING/uncommitted is retained; PASS does not imply DONE or launch readiness.
