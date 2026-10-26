# Coupled frontend declaration-gate review — 2026-10-06

Verdict: **PASS** for accuracy of this failed-candidate evidence. No actionable revision required; initial review, zero revision cycles consumed. The candidate itself remains **REJECTED** at its strict declaration gate. This is not graph/adoption approval or founder acceptance.

Scope: only the README appendix “Later coupled frontend candidate evidence — 2026-10-06” and refresh appendix “Coupled frontend candidate and declaration gate — 2026-10-06”. Earlier material was checked for exact preservation, not re-reviewed. Authority: current AGENTS, constitution, active TASKS and D-069/D-072.

## Exact identities

Packet: `output/research/frontend-build-evaluation-2026-10-06/`.

| Input | SHA256 |
| --- | --- |
| review-inputs.json, 382 inputs | f0b377a3e599c139b140cd3b6a93847e64bcc8669679a80aeb3a633decfd220c |
| protected-before.json, 78 inputs | d7a4dce6aa6c32d94708278f204d28d3914f58859e3d77e47b39d440b9737155 |
| README.md.before | e43ee6c81f4faefb1c870593a42acb831be5842ed138c1621d3552202082985c |
| README.md.reviewed/current | c1be2fab267c35de03f4fbc674b5aedeaa483df98c69be300c48dfb7864c1a0c |
| refresh-evidence-2026-10-04.md.before | db11b13f95bb2823206f56af3a9e819dc7c63f097cf0d24e9274409ddc4f6531 |
| refresh-evidence-2026-10-04.md.reviewed/current | 9095d70bf30e83574cf5edb9c66a5fe4430664be1af8a18e45d1f000aaf02406 |
| candidate/package.json | e5a5c52b46b2b4494e3fe2a62eb5bb7fdf9111bd05f67e650380403817d3ddb4 |
| candidate/package-lock.json | d8ca6b5c36e0928f111fa2b9977c091bad5c13d7e45888139327e4fde496a78f |
| runtime/runtime-receipt.json | dca9fe0e32f0dd1d7436aacf90ab015fc92e81a0454632134a3503b616824853 |
| corrected-checker-observations.json | 6522a3afce0a27e8d2f4b2a9891d20ee369c2bafb340d4eb8a485b8ebba593b8 |
| corrected-loader-control-observations.json | df2a1e3f20dc76f55b9cb406688989666782de1b80cbc193ef4cd0350a932b67 |

All 382 frozen identities and all 78 protected inputs matched before and after reproduction. Current canonical documents equal reviewed snapshots and preserve their complete predecessor byte prefixes; only 1,166/5,436 bytes respectively are appended. Protected application source/manifests/locks, earlier candidate lock, governance and both GLBs remain unchanged.

## Independent reproduction and findings

Created only `output/research/frontend-build-independent-2026-10-06/` plus this receipt. Used existing portable `runtime/node.exe` and explicit API6/native7 CLI entrypoints with candidate cwd, cleared child environment, OS/runtime allowlist and reviewer-only profile/temp directories. Direct commands were `node.exe <candidate/node_modules/typescript/bin/tsc6 | @typescript/native/bin/tsc> --project <tsconfig.json | tsconfig.invalid.json | tsconfig.loader-control.json> --pretty false`. No producer runner, npm/install, Vite or browser command was executed.

All six actual CLI invocations reproduced saved stdout/stderr bytes exactly within the same compiler path. Corrected fixture and public loader-import control each report `[2430,2416]`; invalid numeric prop reports `[2322]`. API6 exits 2 and native7 exits 1 in every case. Reviewer `observations.json` SHA256: `13849872f6233aa461cccea7798b9c2ae0faa3c4b4d4c90058fc12e2fdae4dcd`. Complete command/raw records remain in that separate directory.

Source diagnosis agrees with public-boundary results: three-stdlib/loaders/SVGLoader.d.ts:3–9 makes userData optional while @types/three/src/extras/core/ShapePath.d.ts:38 requires it. TGALoader.d.ts:13 returns DataTexture; DataTextureLoader.d.ts:21,45 expects texture-data with PixelFormat, whereas inherited Texture.format is AnyPixelFormat. The compilers select different numeric format witnesses (36492/33776) and different message structure; shared codes do not establish raw equivalence.

The valid fixture uses strict, isolatedModules, noEmit and skipLibCheck=false and imports the stated source families. Its initial undeclared isWebGLRenderer marker/error TS2339 remains archived; the only fixture correction uses declared getContext(). The initial loader control imports unexported internal paths and returns TS2307; package.json:23–29 publishes the root type entry, and the corrected control uses its public SVGLoader/TGALoader type exports. These are declaration probes, not loader executions. Neither mistake is hidden or treated as a package runtime failure.

Direct pinned manifest versions agree with saved registry observations, including API6's @typescript/typescript6 6.0.2 alias delegating through installed @typescript/old 6.0.3 and native TypeScript 7.0.2. Existing portable Node 26.10.0 checksum matches saved official SHASUMS; npm12.2.0 archive SHA512 matches registry SRI. npm's `^22.22.2 || ^24.15.0 || >=26.0.0` engine excludes observed Node24.14.0. Official release-index evidence marks the portable runtime non-LTS; it is unselected research tooling.

Inspected strict peer/engine package-lock-only and frozen ci commands, disabled scripts, private prefix/cache, empty user/global configs, exit-0 logs and unchanged seed/final lock. Installation was not repeated. All 308 lock records reconcile as root plus 236 present metadata versions matching lock and 71 absent optional records. This checks metadata correspondence, not integrity of every installed file or reproducibility across other platforms.

The sole locked prerelease is gensync1.0.0-beta.2. Installed metadata supports React Hooks lint → Babel core → gensync ancestry; it establishes neither execution nor exclusion from other paths. Saved Context7/primary guidance is scoped source evidence. [Fiber guidance](https://r3f.docs.pmnd.rs/getting-started/introduction) supports React19/Fiber9 and labels Fiber10 alpha; [Tailwind compatibility guidance](https://tailwindcss.com/docs/compatibility) supplies a framework browser floor, not tested fixture coverage. Referenced exact-tag Vite/plugin source distinguishes transpilation/type checking and optional compiler/Babel paths; package naming alone proves no transform execution.

## Limits and remaining gates

Strict resolution/install success does not establish full coupled compatibility. The valid type gate failed, so Vite/build/browser evaluation was not invoked. No runtime renderer/loader failure or success, HTML/CSS output, transform, audio/stream/resource lifecycle, device performance, universal compiler parity or production UI is demonstrated. These finite controls neither exhaust declarations nor prove the latest mutually compatible stable graph.

D-069 selection/exception/rollback/recheck and D-072's exact lint-only scope remain intact. No general Babel/build or prerelease waiver, gensync conformance/execution/deployed-exclusion proof, supply-chain/signature/attestation/licence/advisory/SBOM/security clearance, MA-013 closure, adoption, Phase 1 approval or founder acceptance follows. No application/dependency/lock/model, Git, provider/account or machine setting was changed by this review.
