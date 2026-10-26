# Candidate wasm-util notice evidence review — v1

Date: 2026-10-04. Reviewer: independent agent `review_candidate_inventory_v1`.
Review verdict: **PASS**, limited to the exact evidence claims below.
Task state: DOING; uncommitted. Findings: 0 Critical, 0 High, 0 Medium, 0 Low.

## Scope

This is an accuracy and provenance-boundary review of the new
`wasm-util-notice-evidence-2026-10-04.md` addendum and its listed raw inputs.
It is not licence clearance, acceptance of a dependency, proof of a source build,
whole-code origin mapping, a selected production graph or a superseding review
of the compatibility README. Governance and D-069 retain latest mutually
compatible stable selection, factual dependency identifiers and the separate
complete-graph/release gates. Existing application, QA and previously reviewed
producer files were not changed.

## Assessment

| Claim and location | Independent evidence and limit |
|---|---|
| Earlier archive comparison, addendum lines 7–14 | The exact correspondence input records wasm-util 0.10.2, 39 matching direct-package files, zero different/absent files, and no licence-named files. Its npm metadata records the quoted source `gitHead` and MIT label. The addendum correctly attributes this to the earlier comparison. Published tarballs were not provided as retained files for this commission and that byte comparison was not rerun; it is supporting historical evidence, not fresh archive or source-build attestation. |
| Source inventory, lines 16–24 | Independently parsed the recursive tree and read the ZIP in memory as data. Tree is explicitly not truncated and contains 87 blobs; ZIP contains 87 regular files. Their complete relative-path sets agree. Every ZIP entry’s byte length and independently computed Git blob SHA-1 agree with its tree record. This establishes correspondence of these retained inputs, not an authenticated source-build chain. Neither inventory has a filename matching LICENSE/LICENCE/COPYING/NOTICE, case-insensitively with ordinary suffixes. This filename search does not cover every possible naming convention or embedded rights declaration. |
| Selected text and source hashes, lines 21–24 and 49–54 | The selected package.json bytes hash to the recorded value and its line 37 declares MIT. The selected `src/wasi/path.ts` bytes hash to the recorded value and line 40 explicitly attributes an adapted Node Windows resolver. Both recorded trimmed line texts match. The selected-text claim does not assert a complete repository rights audit. All retained tree/ZIP/Node-reference byte counts and SHA-256 values match their receipts. |
| Node comparison, lines 26–33 | Inspected the actual retained Node path source and wasm-util resolver as text. Node lines 190–343 and wasm-util lines 43–137 visibly correspond in resolver state, reverse traversal, per-drive current directory, drive/root parsing and normalized tail assembly. Node source lines 1–20 contain the Joyent/Node copyright and permission header. The TypeScript version adapts guards and structure; no byte identity, exact copied revision, origin completeness or runtime equivalence is established. The addendum expressly keeps Node v24.14.0 a comparison reference. |
| Notice condition and authority limit, lines 35–41 | The pinned official Node licence and path header contain the preservation condition for applicable copyright/permission notices. The addendum accurately keeps that evidence limited to the Node contribution and does not use it as the missing grant for wasm-util’s original code. Determining actual applicable portions and complete distribution obligations remains held, rather than being declared cleared from an MIT label or this review. |
| Remaining work and prior-review scope, lines 56–68 | Authoritative package notice, third-party attribution, actual distribution contents and reviewed notice/provenance evidence remain required. No holder is invented, no other package’s licence is borrowed, no downgrade/replacement is selected, and no production graph or native-prototype operation is claimed affected. Earlier inventory PASS is correctly limited to its original input identities; this addendum has its own narrow receipt. |

## Exact commissioned and linked raw input identities

SHA-256 values were independently recomputed. Raw paths below are relative to
`output/research/compatibility-resolution-2026-10-04/` unless fully specified.
Later changes are outside this verdict.

| Input | SHA-256 |
|---|---|
| `docs/phase-1-compatibility/wasm-util-notice-evidence-2026-10-04.md` | `BBA46A0F8337FDE3AF03F8BF8E0AC8F9066039AC925A1D575CF0D10BFC677EF8` |
| `wasm-util-full-source-notice-scan.json` | `DD2F230CC56F3D7A7B744B8C8D00FAAFF2C396A8D22A35B00494FBCF9245837C` |
| `wasm-util-node-source-references.json` | `350B0CE19FD4521BE036E10798DB1B3D248EBFE8B518EA6F6EE5BE9ED224C2B5` |
| `wasm-util-pinned-tree.json` | `416A22F0793A470166BF0A6B79355DF65A95F56D4E850178DB7F987453379FB9` |
| `wasm-util-pinned-source.zip` | `68444B71D4285ABE742E370FAF8D9B9C88F67ADE023CDDFCB170C8BB86F7B84F` |
| `node-v24.14.0-path.js` | `DD326ECDC2D6AD2025C4991F4B480D76A9F1D52B7F6D0988A5DC0A1D02DE5209` |
| `node-v24.14.0-LICENSE.txt` | `4573185D56580DA2B890BA34A85A409257640F1C5632EADE4300137266194D18` |
| `bundled-license-correspondence.json` | `25F8485798477AD323B3479C93F009A56AE2E552930D25B23F4B8A6367E203A7` |

Selected source SHA-256 values, independently recomputed directly from ZIP bytes:

- `package.json`: `195DD41458BCE39A8E8EE247E2D24B4AB9D7BC106F37BD1E29573D2D0F894F36`
- `src/wasi/path.ts`: `38BB04DBFD29AF002C56C3D6886F979BECA3148455908FEECA5F5027E6277465`

## Primary-source inspection and operation limits

On 2026-10-04 the reviewer also inspected the pinned official
[wasm-util path source](https://raw.githubusercontent.com/toyobayashi/wasm-util/cded8e894fe40c7c6200a3fdb2bd33e328b7bb65/src/wasi/path.ts)
and [Node licence](https://raw.githubusercontent.com/nodejs/node/v24.14.0/LICENSE).
They corroborate the attribution and notice condition; their retrieval is not a
legal clearance or cryptographic build attestation.

Only local data/text inspection, public source reads and this review write were
performed. ZIP entries were read in memory without extraction; downloaded source
was not imported or executed. No maintainer contact, package install/replacement,
application/configuration/QA edit, external write, runtime restart, commit, push,
publication or production acceptance occurred. Earlier inventory and native
operation reports retain their scopes and were preserved unchanged.
