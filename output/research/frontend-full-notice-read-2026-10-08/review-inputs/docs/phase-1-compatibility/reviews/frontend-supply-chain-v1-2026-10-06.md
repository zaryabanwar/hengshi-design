# Matched-candidate supply-chain evidence review — 2026-10-06

Verdict: **PASS — bounded evidence accuracy only.** No actionable discrepancy in this initial review; no revision cycle consumed. This is independent review of the two new supply-chain appendices, not founder acceptance, security/legal clearance or adoption approval.

Scope: README heading `Matched-candidate supply-chain follow-up — 2026-10-06` and refresh heading `Matched-candidate supply-chain observations — 2026-10-06`. Earlier matched-build/type/browser sections were not reviewed anew. Current AGENTS, constitution, project/decision/state and TASKS authority retain D-069 graph/exception/rollback/recheck and D-072's exact isolated lint exception; this slice expands neither.

## Frozen identities

Paths below are relative to `output/research/frontend-supply-chain-2026-10-06/` unless stated otherwise. SHA256:

| Input | Identity |
| --- | --- |
| review-inputs.json, 815 inputs | `ef4760f0531966bc4eee4071499e75dd8b93a844dac1510a0c2dd97fba74ace8` |
| protected-before.json, 78 inputs | `9bb8f003769b335983ea004bb8caeb085669baee1a7a8cbc816db07367c1c63f` |
| README.md.before → reviewed/current | `b32039951ea70fb645a9c410ff56c9079812fe623a68a793b1859e56ef1689e6` → `27f5bddc4664afea1e0e55aa8942eecd2c9b877f24da8d7d091f2081926f10ba` |
| refresh-evidence-2026-10-04.md.before → reviewed/current | `504b5ee82ec84bb731d00ac7df5094a4a9000d9b9a44f2a2ca2713cfb49464fe` → `2aada7413b9fe489948989cf5ef67e85d57f89c1c075307a07ecb276ec43d324` |
| observations.json | `aa7e62a409f8c948bd0ed87828236539840564a569ed3650e0dfe3f7fd0e422f` |
| licence-inventory.json | `14a962173da1bee387c5b961baf68f2a456645b4b7935381670ad2b7e7d19215` |
| advisory-audit.stdout.json | `5e76da8092d8f1e0a4e92058f0a2cc1a60c630b66bb33d70b29ae592ae074f7e` |
| lock-sbom.stderr.txt | `342db79b566f6a3f8f289b90198eedc875dff5e61cc5de29766bfb9738311078` |
| installed-sbom.stdout.json | `ac99298d413fe3d6ed69e0cc291ac30415b6b263b6d1e48b0b505903047155ed` |
| installed-signatures.stdout.json | `539ea4684b22e24869bace50b48bda695776477f892861b08d51d219f0d08faf` |
| detailed-signatures.stdout.json | `be123afea1b86bfa5513287c2a448aaf3fefdf2243094873212304aff4250d55` |
| npm12-verify-signatures.js | `7c39ad2ca991d5edf6ddcd9623aea1ff1820007484e6e0bc6a422330df278b6c` |
| Matched candidate package-lock.json (sibling remedy packet) | `fa903a8d901357aacf80863524e0e00ae2ece69126daf218256cdd2656b2da4c` |

## Findings and independent reproduction

Both current documents equal their reviewed snapshots. Their complete predecessor bytes are exact prefixes: README adds 1,159 bytes and refresh adds 5,209 bytes. All 815 manifest identities and 78 protected identities matched before and after review; no producer, app, lock, protected model or machine setting changed. Historical 2,668-input guards are dated producer records, not an assertion that later authorized navigation references remain their older bytes.

The five saved explicit Node26.10.0/npm12.2.0 commands use empty configs, a separate cache, fixed registry, `--ignore-scripts`, no workspaces and explicit dev/optional inclusion. Audit `--json --package-lock-only` exits0 with no reported vulnerabilities at any severity; this is a dated known-advisory result, not absence of vulnerabilities. Virtual SPDX exits1 `ESBOMPROBLEMS`, with empty stdout and six absent dependencies of optional `@tailwindcss/oxide-wasm32-wasi`: `@emnapi/core`, `@emnapi/runtime`, `@emnapi/wasi-threads`, `@napi-rs/wasm-runtime`, `@tybys/wasm-util`, `tslib`. No fix/install/scripts ran in these commands.

Independent read-only Python correlations against the saved JSON and current package metadata reproduce 301 non-root lock records, 236 installed locations and 65 missing optional records. Those locations reduce to 233 unique name/version pairs (semver6.3.1 appears twice; eslint-visitor-keys5.0.1 three times). Installed SPDX exits0 and contains exactly those pairs plus the private fixture root: 234 packages, 398 relationships with valid endpoints. Root Three0.184.0 and nested Three0.170.0 remain distinct. `NOASSERTION` covers the root and webgl-constants; an installed inventory does not repair the virtual all-platform gap or establish all-file integrity.

Both saved signature invocations exit0 with empty invalid/missing arrays. The detailed output contains 78 unique installed-location attestation records; every emitted name/version/location agrees with actual metadata. It is not a registry-signature count. Bundles contain 78 publish predicates, 77 SLSA v1 predicates and one SLSA v0.2 predicate. Gensync1.0.0-beta.2 has no emitted attestation record. These correlations do not independently authenticate the remote bundles or establish provenance availability for all dependencies.

The retained npm command files match installed source bytes. `npm12-audit.js:122` loads the actual tree; `npm12-sbom.js:41` selects virtual versus actual and reports tree problems. `npm12-verify-signatures.js:257` skips ineligible/missing/local/nonregistry inputs; registry keys and omitted dependency types affect coverage. Its `pacote.manifest` path at line301 verifies registry metadata signatures/attestations; lines347/360/364 separate signature accounting from emitted attestation records. It does not compare every installed file with a published archive. Official [npm12 audit](https://docs.npmjs.com/cli/v12/commands/npm-audit/) and [npm12 SBOM](https://docs.npmjs.com/cli/v12/commands/npm-sbom/) guidance agrees. Historical Context7 lookup is producer-reported; no raw Context7 response is retained in this packet.

All 301 licence declarations reproduce MIT207, ISC13, Apache-2.0 44, CC-BY-4.0 1, BSD-2-Clause6, BSD-3-Clause3, MPL-2.0 24, BlueOak-1.0.0 1, GSAP standard declaration1 and absent1. Every available metadata identity and all 227 retained top-level text copies match current bytes, sizes and SHA256. The collector's narrow top-level name-prefix rule leaves exactly 11 installed names without such files: @humanfs/types, @mediapipe/tasks-vision, @react-three/fiber, @rolldown/binding-win32-x64-msvc, draco3d, esrecurse, gsap, imurmurhash, maath, natural-compare, stats-gl. This does not mean their distributions contain no terms. Earlier GSAP3.15.0 and targeted WASM archive/pinned-source notice inspections retain their stated candidate-only scopes; they confer no full-graph or legal clearance.

Reviewer evidence: `output/research/frontend-supply-chain-independent-2026-10-06/correlations.json`, SHA256 `dfde7e7dfbb8ba2a00377440927993140fbd9c8319c05a9c7ee06dc545944e35`. Independent work recomputed saved-result/installed-metadata/licence-text correlations without invoking producer scripts or mutating frozen inputs. Remote advisory/signature/SBOM CLI runs were inspected, not freshly rerun; no new cryptographic certification follows.

Limits: no recursive notice completeness, licence interpretation/attribution assembly, deployed-artifact or all-platform complete SBOM, publisher/source safety, general gensync exclusion/conformance, full graph, newest-compatible selection, D-069 exception approval, D-072 clearance, MA-013 or integrated founder acceptance. The known inventory and evidence gaps remain held exactly as the appendices state.


## Later bounded notice discovery — 2026-10-08

The [independent discovery receipt](installed-notice-discovery-v1-2026-10-08.md)
extends evidence for the eleven packages missed by the root-name-prefix collector:
394 own files, 356 eligible text files, 129 hit files and 281 retained excerpts.
It preserves eight exact input identities and reproduced installed-file identities.
The 38 outside-whitelist exclusions include 31 text JSON source maps; they are not
38 binary files. Prefixes, twelve-line caps, metadata-only hits and linked terms
leave applicable notices and attribution completeness unresolved. This later
accuracy PASS neither changes the preceding review's hashes/scope nor confers
licence/provenance clearance, deployed coverage or complete graph acceptance.
