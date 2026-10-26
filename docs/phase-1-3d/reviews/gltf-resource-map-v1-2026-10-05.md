# Visual glTF resource-map shape review — v1

Date: 2026-10-05. Independent reviewer: separate nonproducer reviewer agent.
Verdict: **PASS — bounded definition/schema/tooling review.** No blocking
contradiction or actionable defect was found in these exact proposed bytes.
This verdict does not accept the proposed format for publication or authorize
application implementation. Founder and integrated acceptance remain separate.

## Reviewed scope and authority

This first review covers only `gltf-resource-map.schema.json`, the appended
“Visual resource interpretation proposal” at `SCENE_ASSEMBLY_CONTRACT.md:251–348`,
and `test_gltf_resource_map_schema.py`. The previous contract, descriptor shape
and prior receipt supply controlling context; this verdict does not reaccept them
or cover later amendments. Root governance and checkpoints were reconciled in
this continuing independent review session. The frozen AGENTS/constitution and
D-064/D-065/D-066/D-071 govern this material definition slice. No substantial
campus composition revision is introduced or permitted.

The map remains an explicitly proposed visual interpretation of same-release
`shared_asset` data. Publication kinds, canonical destinations, serving eligibility,
accepted streams, protected assets, audio intent and security authority remain
unchanged. This review grants no provider, decoder, worker, WASM, resource origin,
production tool selection, permission, rights or numerical operating policy.

## Exact input identities

Packet: `output/research/gltf-resource-map-2026-10-05/review-inputs.json`.
Manifest SHA256:
`a38692f4b6d81afbb1156f9e638c1aa5ebc31443fff64e4a7bb51957e11b1d29`.
Snapshot names below are relative to that packet directory. The reviewer
independently calculated all 15 frozen hashes. All 14 real canonical source files
also match their corresponding frozen bytes. The fifteenth entry is a preserved
before snapshot, not an existing canonical source path.

| Source identity | Frozen snapshot | Bytes | SHA256 |
|---|---|---:|---|
| `docs/phase-1-3d/SCENE_ASSEMBLY_CONTRACT.md` | `00-SCENE_ASSEMBLY_CONTRACT.md` | 25504 | `d3d47782dfb2a8c2fd6479efeddc397220f1b7a77ef87568155a26bc722283d2` |
| `docs/phase-1-3d/gltf-resource-map.schema.json` | `01-gltf-resource-map.schema.json` | 3015 | `8d5cece4c921823c96e02c8f35707d991f391f560d261dcf2d9ff07e8c9fd939` |
| `scripts/validation/test_gltf_resource_map_schema.py` | `02-test_gltf_resource_map_schema.py` | 5986 | `9f09dd62f9b1678a98222ecee19b0a1181678f5c0e0563330c6865c84b474092` |
| `docs/phase-1-3d/scene-descriptor.schema.json` | `03-scene-descriptor.schema.json` | 6971 | `ab452a793a6f0fea19455aa2e82878646fada677515de37b4173dee844813867` |
| `docs/phase-1-architecture/contracts/publication-manifest.schema.json` | `04-publication-manifest.schema.json` | 4297 | `d3620c8326246bc34040188de610c5823f1013936572d3ffb63a5eb350bc3852` |
| `docs/phase-1-3d/CAMPUS_ASSET_BUILD_SPEC.md` | `05-CAMPUS_ASSET_BUILD_SPEC.md` | 41840 | `42b0d89074b968704fa44d7ae40803ab4f5fab3f39c64a671ee75b2da66ba9e3` |
| `docs/phase-1-3d/WORLD_EXPERIENCE.md` | `06-WORLD_EXPERIENCE.md` | 31970 | `fab7bf1ec7d29621947763b45ecb9eb5e24abcad66f0a169cc4ce06a2b6adb33` |
| `docs/phase-1-architecture/contracts/PUBLICATION_CONTRACT.md` | `07-PUBLICATION_CONTRACT.md` | 32501 | `2386bec046387527a50dd8e6b4847ac11133932e2267afb96cb20ac4996f111c` |
| `docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md` | `08-SECURITY_PRIVACY_CONTRACT.md` | 24722 | `74ab420b5bec9f0aad72f59178f4ea7c626bd14edfa9d4ba02f3aa1dd0a1a254` |
| `specs/003-3d-experience-completion/spec.md` | `09-spec.md` | 25605 | `2aceefa18e51bd11a450d79b2c75d0a2f3a0783baac785de12e56956fa03d4f9` |
| `DECISIONS.md` | `10-DECISIONS.md` | 72891 | `1d53a14ac3347ebeefeeb728e03862b09de111b748cef4e48d5f4ca19141b6d8` |
| `AGENTS.md` | `11-AGENTS.md` | 7686 | `55405cb02a96d05f7f6d68e56a588d743f83877fb2691a5a9f2c736126adbcc5` |
| `.specify/memory/constitution.md` | `12-constitution.md` | 16234 | `33ec0bb02b0d0d9a55d0971589bd19f7242f5d56da130f8f496bc1d31a8b5d23` |
| `docs/phase-1-3d/reviews/scene-descriptor-shape-v1-2026-10-05.md` | `13-scene-descriptor-shape-v1-2026-10-05.md` | 15000 | `169d8e15d6d7e8bc90f758c7316a3fa2fe773c68d4c6fffce6f5d9034b7bc7bc` |
| `before visual resource-map proposal` | `SCENE_ASSEMBLY_CONTRACT.before.md` | 18408 | `b41ef9983f4187d34d65793e6dbaf8820c6d0901f82f21764f89a69cb7142779` |

The previous contract is exactly the first 18,408 bytes of the current 25,504-byte
contract. Removing the sole 7,096-byte appended block restores the entire before
file byte-for-byte, SHA256
`b41ef9983f4187d34d65793e6dbaf8820c6d0901f82f21764f89a69cb7142779`.
No earlier contract body changed in this slice. The appendix's local schema link
resolves. Its three official external source targets were independently opened.
The producer's optional observations file is supplemental reported evidence, not
one of these frozen inputs and not a substitute for the checks below.

## Findings and coverage

**No severity-rated correction is required for this proposed slice.** The following
conclusions are bounded to the definition and local shape tooling:

- **Visual scope and authority:** contract lines 253–270 correctly limit the map to
  visual interpretation. Collider/navigation interpretation is expressly separate
  and unselected; the visual map cannot complete a traversable bundle by itself.
  The exact immutable client/build descriptor, its registration and selection
  remain held. A build/profile selector cannot deliver callbacks, imports, options
  or code. Absent or mismatched compiled registry entries reject preparation.
- **Verified glTF coverage:** lines 272–308 require declarations to match actual
  verified model bytes, existing selected scene/node indices, container/version/
  minVersion, used and required extensions, complete core and supported extension
  resource inventory, MIME/use compatibility and exact artifact references. A GLB
  is not assumed self-contained. Required extensions cannot be ignored. Unsupported
  resource-bearing mechanisms require a reviewed amendment rather than arbitrary
  pointer or network behavior.
- **Proposed URI and pointer domains:** the conservative ASCII relative-path subset
  is described as a Hengshi packaging choice, not all valid glTF URI syntax.
  Embedded GLB BIN/bufferView resources remain permitted; data-URI exclusion is a
  production-export recommendation, not a vendor prohibition. Checksums follow
  compliant export; the loader cannot silently normalize published content.
  Core pointer canonical indices and actual JSON-location resolution are explicit
  semantic obligations beyond the broad pointer shape.
- **Graphs and loading:** lines 310–329 preserve the distinction between inventory
  references and required dependency edges. Each selected model requires its
  declared resource/decoder closure, while parsing the map cannot eagerly acquire
  every indexed model or optional area/audio. Reciprocal model/map dependencies
  and containing-manifest digest cycles remain prohibited. The independent build
  identity also excludes a map/manifest digest cycle. Existing same-release/stream,
  readiness, safe-ground, finite ownership, late completion and withdrawal rules
  continue to govern admission; a successful parse gives no movement permission.
- **Public payload and fetch control:** closed objects expose only declared scalar
  selectors and records, with no public URL/code/options field. Profile and decoder
  IDs are inventory checked against trusted compiled behavior, not executable-code
  authorization. Actual core/plugin/decoder fetch paths must be controlled before
  requests, unknown requests fail without fallback, and origin/redirect/CORS/MIME/
  integrity plus temporary Blob ownership follow security/publication contracts.
  Neither a base URL nor a URL modifier claims to establish those boundaries.

These conclusions align with the preceding logical assembly and closed-descriptor
proposals, publication preparation/serving/withdrawal rules, browser-resource
security proposal, loading/residency contract and F3D-04–07/F3D-14. They do not
change D-071's accepted composition or consume another model revision. Historical
logical-review test wording remains in preserved context and does not represent
this later shape-tooling execution.

## Independent tooling and adversarial probes

Executed against the matching canonical bytes, with Python `-B` and no dependency
changes:

- `python -B scripts/validation/test_gltf_resource_map_schema.py`: **4 methods PASS**.
- `python -B -m unittest discover -s scripts/validation -p 'test_*schema.py'`:
  **19 methods PASS**. This broader run checks local schema tooling only.

The schema and fixed publication-schema references are registered locally by the
test fixture. A separate in-memory probe using an unregistered schema reference
fails with `_WrappedReferencingError`; no network schema discovery is provided by
that local registry. The appendix's held “registry” means the production compiled
profile registry, not this existing local schema-reference registry.

Additional independent in-memory mutations established the following boundaries;
no fixtures or producer files were edited:

| Probe | Observed shape result | Interpretation |
|---|---|---|
| Unknown profile ID | Accepted | Registry membership/build agreement must reject it in preparation, lines 263–270. |
| Required extension absent from used | Accepted | Verified-asset/semantic subset and actual-use checks are required, lines 276–282. |
| Duplicate model ID with different scene index | Accepted | `uniqueItems` compares entire records; semantic ID uniqueness is explicit, lines 304–308. |
| Duplicate URI with different artifact mapping | Accepted | Exact URI uniqueness and complete mapping are semantic obligations. |
| Duplicate location with different usage | Accepted | Location uniqueness and MIME/use agreement are semantic obligations. |
| `/images/00/uri`, `/images/a/uri`, `/uri`, unknown extension location | Accepted | Broad pointer shape does not establish canonical core indices, existing locations or supported profile semantics, lines 298–303. |
| Unknown artifact ID or image pointer labelled buffer | Accepted | Same-release/kind/existence/verified-byte/use checks must enforce the obligation. |
| `a.`, `a..`, ordinary nested ASCII filename | Accepted | These are exact permitted names, not standalone dot segments. No filesystem normalization or native-path resolver was exercised. |
| `.`, `..`, hidden leading-dot segment, parent traversal, percent escape, CR/tab/NUL | Rejected | Matches the documented restrictive path subset. The focused suite also rejects schemes, absolute/authority paths, double slashes, backslash, data/blob URLs, query/fragment, spaces and non-ASCII. |
| NaN/Infinity/bool/negative/unsafe integer scene index | Rejected | Local index-type/capacity checks only; no strict JSON ingress parser or actual glTF scene validation exists. |
| Extra `module_path` at root/model/resource/use records; null external mapping | Rejected | Nested records are closed and required arrays do not accept null. |

The accepted malformed semantic examples are intentional schema limitations
already explicitly held by the proposal. They do not reveal an unintended gap
between the claimed shape guarantees and the required preparation boundary.
Strict JSON decoding, duplicate-key/Unicode/non-JSON-constant rejection and finite
calculated-value checks remain controlling obligations inherited from the
preceding descriptor explanation; green schema tests do not implement them.

## Independently corroborated primary mechanisms

The reviewer opened these official sources on 2026-10-05, separately from the
producer's reported Context7 query:

- [Khronos glTF 2.0 specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html),
  sections 2.8, 3.12 and 4.1–4.4: glTF permits data URIs and relative/Unicode/escaped
  paths beyond the proposed subset; GLB can retain external references; required
  extensions must also appear among used extensions; the container version does
  not replace the asset-version check. These support the appendix's scoped claims,
  without requiring Hengshi's packaging choice.
- [Three GLTFLoader documentation](https://threejs.org/docs/pages/GLTFLoader.html):
  parsing accepts data plus a base path, and decoder integrations are optional
  loader mechanisms. This does not prove controlled fetching, eligibility or an
  exact selected package/binary.
- [Three LoadingManager documentation](https://threejs.org/docs/pages/LoadingManager.html):
  URL modification receives resource URLs before requests; without a modifier,
  resolution returns the original URL. This supports the need for explicit
  controlled request handling, not a claim that all plugin/decoder paths or
  permissions have been proven.

No Context7 graph, production library version, extension or decoder selection is
accepted by this source inspection. No actual GLB parser or loader was exercised.

## Remaining gates and limits

Before format/bundle acceptance, resolve and independently review the exact
build-descriptor identity and map/profile registration/selection binding, supported
extensions and safe-ignore rules, decoder formats/provenance, separate collider
binding, measured finite operating limits, resource origins/worker/WASM permissions,
rights, complete mutually compatible stable graph and applicable founder approval.

After implementation authorization, actual public/compiler/inspector/resolver/
loader boundaries must reject the semantic counterexamples above and exercise
external GLB inventory (including mixed-use resources), absent/mismatched bytes,
invalid scene/minVersion and undeclared extensions, changed build/profile/decoder,
unexpected plugin/decoder requests and redirects, prohibited data URIs, complete
required closure without eager whole-campus or pre-consent audio fetch, partial
failure/disposal, shared final-owner release, withdrawal and stale completion.
Those cases require actual boundaries; a duplicated semantic checker in test
expectations would not establish enforcement.

This receipt establishes no public format approval, production resource,
publication eligibility, privacy/security enforcement, collision/appearance,
movement/audio operation, accessibility, physical-device performance, whole Phase 1
acceptance or launch readiness. Only this receipt was authored; producer inputs,
application, assets, dependencies and configuration were not changed. No commit,
push, provider/Figma action or external write was performed.
