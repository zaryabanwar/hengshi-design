# Candidate dependency notice evidence — v1

Date: 2026-10-04. Task status: DOING. Research only; no production selection,
licence clearance or application dependency change.

## Finding

The isolated native-lint candidate contains `@tybys/wasm-util` 0.10.2,
including its bundled copy in `@tailwindcss/oxide-wasm32-wasi` 4.3.3.
Earlier archive comparisons in
[`bundled-license-correspondence.json`](../../output/research/compatibility-resolution-2026-10-04/bundled-license-correspondence.json)
found 39 matching direct package files; the separately published archive and
bundled copy omit a licence file. Matching bytes do not attest how the package
was built or clear its distribution notices.

The npm-reported source commit is
`cded8e894fe40c7c6200a3fdb2bd33e328b7bb65` in
[`toyobayashi/wasm-util`](https://github.com/toyobayashi/wasm-util/tree/cded8e894fe40c7c6200a3fdb2bd33e328b7bb65).
The full recursive tree is not truncated and has 87 blobs; the source ZIP contains
87 regular files. Neither inventory contains a LICENSE, LICENCE, COPYING or NOTICE
named file. The selected UTF-8 text scan finds an MIT declaration in
`package.json:37` and an explicit acknowledgement of adapted Node path-resolution
code in `src/wasi/path.ts:40`. This is a filename and selected-text search, not
proof that every file has no applicable rights information.

The official comparison reference,
[`nodejs/node` v24.14.0 `lib/path.js`](https://github.com/nodejs/node/blob/v24.14.0/lib/path.js),
contains a Joyent and Node contributors copyright/permission header at lines
1–20. Its Windows resolver at lines 190–343 has visibly corresponding resolver
state, per-drive working-directory lookup, root parsing and tail normalization.
The wasm-util function is adapted TypeScript; no byte identity, precise copied
Node revision or complete code-origin mapping is asserted. v24.14.0 is a pinned
comparison reference, not an assertion about the version used by the author.

Node's [official licence](https://github.com/nodejs/node/blob/v24.14.0/LICENSE)
requires preservation of the applicable copyright and permission notice when
copies or substantial portions are distributed. Its notice addresses the Node
contribution; it cannot establish the rights holder or grant for wasm-util's
remaining original code. The MIT package label alone does not resolve the absent
notice or the full attribution mapping.

## Evidence and remaining work

The source tree/ZIP were read as data without extracting or executing package
code. Raw inputs and SHA-256 receipts are retained in
[`wasm-util-full-source-notice-scan.json`](../../output/research/compatibility-resolution-2026-10-04/wasm-util-full-source-notice-scan.json)
and
[`wasm-util-node-source-references.json`](../../output/research/compatibility-resolution-2026-10-04/wasm-util-node-source-references.json).
The selected wasm-util path source hash is
`38bb04dbfd29af002c56c3d6886f979beca3148455908feeca5f5027e6277465`.
Node path source and licence hashes are respectively
`dd326ecdc2d6ad2025c4991f4b480d76a9f1d52b7f6d0988a5dc0a1d02de5209` and
`4573185d56580da2b890ba34a85a409257640f1c5632eade4300137266194d18`.

Before accepting a production graph that includes this package, resolve the
authoritative package notice and applicable third-party attribution, determine
which files the actual distribution includes, retain the required notices, and
independently review the resulting provenance/notice evidence. Do not invent a
copyright holder, borrow another package's licence as the missing grant, or
silently choose an older dependency. No maintainer contact, external write,
dependency replacement or production publication was performed.

This finding affects candidate provenance acceptance, not the existing native
prototype's operation. Earlier advisory/SBOM inventory review PASS covers its
listed inputs only and does not cover this addendum. A separate exact-input
review may assess the accuracy of this evidence; it cannot clear the unresolved
package notice or accept the complete compatibility graph.
