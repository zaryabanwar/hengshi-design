# Native TypeScript LSP bounded evidence review — 2026-10-06

Verdict: **PASS** for evidence accuracy within this slice; no actionable revision required. Initial independent review, zero revision cycles consumed. This receipt is not founder acceptance, compatibility-graph approval or adoption permission.

Scope: only the new README appendix “Later native language-server evidence — 2026-10-06” and refresh appendix “Native TypeScript language-server probe — 2026-10-06”. Earlier material was checked for byte preservation, not re-reviewed.

## Exact frozen identities

Packet root: `output/research/typescript-native-lsp-2026-10-06/`.

| Input | SHA256 |
| --- | --- |
| review-inputs.json, 112 inputs | c19b7eba02bbc65926cf7f99f7f998bf4dc43f34aa4b83f2e02063d7c629646a |
| protected-inputs.json, 15 guards | c7d8fdff3e3867d719f10242e7c7f3e52001d273b2dba16095afd9d4bdf48bf8 |
| README.md.before | 88de3472ca5b84ccedbd911807193fe61e120df3a17fae553aa59d9eeb00e754 |
| README.md.reviewed/current | 1ddbb67bc3f1b63f6abc6b6b982f17a1dd1416486ad238fb4e45e2d74db98a6e |
| refresh-evidence-2026-10-04.md.before | 5fbac75f86e5ad7ffc9a9786d6623252c1b8a92de15563a8b4c5cf811bc9ad7a |
| refresh-evidence-2026-10-04.md.reviewed/current | 2b57aa6a516e0b5f303dc81868ce16e4df1d3f8b1be70029aeb2bb0c5ad1a6af |
| probe_lsp.initial.py | 6d3c7a10b855c54eed61b4ac60b2b056e92a4fdf0c76c0962067caf5db0c04a4 |
| probe_lsp.py | 941d827d03fc64ceb780f40ae8f29939467d0f5a037d2c22775fd6ae19f92def |
| existing native platform lib/tsc.exe | f9ecfbdc93753d2c972d66a8d0d75f5bd737fd4a5f88b422d9091ea282bcb2c7 |
| producer-run/observations.json | dc3610b86b5886c384982b9bc85ef0aa8e45a641dc28b090a4c06ad20355051b |
| producer-corrected-run/observations.json | b85bfcbf8cbdae8e5cc71c69e3e08238d2235f7b0ae2ca67d636e7601c8f0a25 |

All 112 manifest identities and 15 protected guards matched before and after reproduction. Both current documents equal reviewed snapshots and retain entire predecessor byte prefixes; only 799 and 3,984 bytes respectively are appended. Application manifests/locks, candidate manifests/lock, governance records and protected GLBs remain unchanged.

## Independent reproduction and inspection

Read the complete runner before execution. Ran `C:/Python314/python.exe -B output/research/typescript-native-lsp-2026-10-06/probe_lsp.py --output output/research/typescript-native-lsp-independent-2026-10-06` with cleared outer environment and explicit OS allowlist. Existing executable only; no install or editor/account/settings change. The runner refused existing output and wrote its own new evidence directory.

Independent `observations.json`: SHA256 `aa83ed60600becffa3be04a787b2c207f55bd17d443b128e21991ed9e0b0fe34`; `protocol.json`: `d513fbdca0081350e6ba4ffa515e44731c4d757f0382c9a1c1441b583e085f6d`. Parent probe exit 0; server PID 19360 absent after shutdown. All 72 run guards match; redirected runtime directories contain no observed files.

Parsed actual Content-Length client/server frames independently and checked them against observations. Eight full pull reports match unchanged fixture oracles and prior reviewed CLI/API6 compiler/in-process-service code projections: valid component/async control `[]`; invalid prop `2322`; missing prop `2741`; state action `2345`; ref `2322`; event property `2339`; DOM root `2345`. Prior invalid numeric CLI exits remain unequal (API6 2, native7 1).

Negotiation identifies typescript-go 7.0.2, UTF-16, open/close, incremental sync kind 2 and typescript pull diagnostics. Actual range-based whole-buffer replacement at version 2 clears the prop diagnostic; version 3 restores `2322`. Each edit precedes its awaited pull response; fixtures remain unchanged. This does not exercise arbitrary Unicode, fine-grained edits or API6 edit parity.

Original raw exchange rejects `client/registerCapability` with -32601 before any completed fixture report. Its historical runner guard matches the archived initial script, not the corrected current file. Runner differences are confined to configuration capabilities and finite registration/configuration replies. Corrected raw exchange advertises support, accepts configuration-change registration and replies null for unavailable settings. Exact [v7.0.2 server source](https://github.com/microsoft/TypeScript/blob/v7.0.2/tsc/internal/lsp/server.go) registers that watcher unconditionally; the first failure remains evidence against assuming universal interoperability. [Official configuration semantics](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#workspace_configuration) permit null for unavailable settings.

Raw protocol orders shutdown request, null response, then exit notification. Actual server exit is 0 and no process remains. Both corrected producer and reviewer stderr contain `error handling method 'exit': EOF`; source handleExit returns io.EOF. The appendix preserves this accurately and makes no clean-stderr claim. The [exact launcher](https://github.com/microsoft/TypeScript/blob/v7.0.2/tsc/cmd/tsgo/lsp.go) supports the observed stdio launch. Saved official LSP sources support this feature baseline; they do not select the newest protocol. The packet's Context7 no-match narration is producer-reported, not an independently replayed lookup or runtime premise.

## Limits and authority

These observations establish finite native stdio diagnostic and buffer behavior only. Async typing is not React runtime/server-component support; code equality is not universal message/range/library equality. No full protocol conformance, actual editor/plugin integration, build/emit, cross-platform, rendering, compiler transformation, supply-chain/provenance/licence/SBOM, deployed exclusion, security certification or complete mutually compatible stable graph is established. Environment containment is not an OS network sandbox.

D-072 remains the exact isolated React lint exception; this evidence neither expands it nor selects Babel/build/prerelease dependencies. MA-013, Phase 1/integrated approval, adoption and founder acceptance remain held. Only this receipt and the separate reviewer reproduction directory were authored.
