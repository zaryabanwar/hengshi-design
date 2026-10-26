# Scene descriptor shape v1 — independent bounded review

Date: 2026-10-05. Verdict: **PASS for the proposed shape, encoding explanation and local tooling**.
No actionable REVISE finding was identified; no corrective severity is assigned.
The shape and encoding remain proposals requiring approval. This verdict establishes
neither serving eligibility nor collision, privacy/security, accessibility or
production enforcement.

## Scope and method

Reviewed `scene-descriptor.schema.json`, the later `Closed descriptor shape
proposal` section and small encoding-availability edits in
`SCENE_ASSEMBLY_CONTRACT.md`, and `test_scene_descriptor_schema.py`. Independently
verified the fifteen-input packet and canonical/frozen byte identities, inspected
the delta against the before contract, checked local references, ran focused and
broader local schema tooling, and executed independent in-memory boundary probes.
Compared against the preceding bounded logical assembly review and controlling
publication, World/loading, wayfinding, security, feature and decision inputs.

Applied governance and root project authority read in this continuing review
session. This is a separate shape slice, not another model/composition revision.
Existing logical packaging recommendations are not selected by this review. No
scene compiler, publication coordinator, ingress parser, loader/mover, browser,
physical device, provider, Figma or application behavior was executed or certified.

## Exact reviewed identities

Manifest: `output/research/scene-descriptor-shape-2026-10-05/review-inputs.json`.
Independently observed SHA-256:
`5f9c65a09b6c1658eab8832bc5d49e252f26edc93840ff105384625ddc3d270f`.

Snapshot filenames below are relative to
`output/research/scene-descriptor-shape-2026-10-05/`. All fifteen frozen hashes
match the manifest; all fourteen corresponding canonical files equal their frozen
bytes. The before input has no current canonical source.

| Canonical source or before identity | Snapshot | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| `docs/phase-1-3d/SCENE_ASSEMBLY_CONTRACT.md` | `00-SCENE_ASSEMBLY_CONTRACT.md` | 17677 | `4643732dcdf1a6e6c6d0f41c3e114a18e76b58de6f43cb4fbb2ebec906fbc657` |
| `docs/phase-1-3d/scene-descriptor.schema.json` | `01-scene-descriptor.schema.json` | 6971 | `ab452a793a6f0fea19455aa2e82878646fada677515de37b4173dee844813867` |
| `scripts/validation/test_scene_descriptor_schema.py` | `02-test_scene_descriptor_schema.py` | 8606 | `e92f9d902f932c9503b4706115ca2603de5d20b59b9f145f60f702ede2aca60a` |
| `docs/phase-1-architecture/contracts/publication-manifest.schema.json` | `03-publication-manifest.schema.json` | 4297 | `d3620c8326246bc34040188de610c5823f1013936572d3ffb63a5eb350bc3852` |
| `docs/phase-1-3d/CAMPUS_ASSET_BUILD_SPEC.md` | `04-CAMPUS_ASSET_BUILD_SPEC.md` | 41840 | `42b0d89074b968704fa44d7ae40803ab4f5fab3f39c64a671ee75b2da66ba9e3` |
| `docs/phase-1-3d/WORLD_EXPERIENCE.md` | `05-WORLD_EXPERIENCE.md` | 31970 | `fab7bf1ec7d29621947763b45ecb9eb5e24abcad66f0a169cc4ce06a2b6adb33` |
| `docs/phase-1-architecture/contracts/PUBLICATION_CONTRACT.md` | `06-PUBLICATION_CONTRACT.md` | 32501 | `2386bec046387527a50dd8e6b4847ac11133932e2267afb96cb20ac4996f111c` |
| `docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md` | `07-SECURITY_PRIVACY_CONTRACT.md` | 24722 | `74ab420b5bec9f0aad72f59178f4ea7c626bd14edfa9d4ba02f3aa1dd0a1a254` |
| `docs/phase-1-ux-architecture/wayfinding-release-map.csv` | `08-wayfinding-release-map.csv` | 10356 | `298876f35468e7501028a77de63d1b449fd75b52183619a500700c46c2999c63` |
| `specs/003-3d-experience-completion/spec.md` | `09-spec.md` | 25605 | `2aceefa18e51bd11a450d79b2c75d0a2f3a0783baac785de12e56956fa03d4f9` |
| `DECISIONS.md` | `10-DECISIONS.md` | 72891 | `1d53a14ac3347ebeefeeb728e03862b09de111b748cef4e48d5f4ca19141b6d8` |
| `AGENTS.md` | `11-AGENTS.md` | 7686 | `55405cb02a96d05f7f6d68e56a588d743f83877fb2691a5a9f2c736126adbcc5` |
| `.specify/memory/constitution.md` | `12-constitution.md` | 16234 | `33ec0bb02b0d0d9a55d0971589bd19f7242f5d56da130f8f496bc1d31a8b5d23` |
| `docs/phase-1-3d/reviews/scene-assembly-v1-2026-10-05.md` | `13-scene-assembly-v1-2026-10-05.md` | 13402 | `c3717390c32e6e56eb9dae691f865c1dc29ccb5905a0a1c6d8b8a88ae5758023` |
| Contract before closed shape proposal | `SCENE_ASSEMBLY_CONTRACT.before.md` | 12725 | `c9d8080a0a111c7bd22af3b17120655b042f85220f7115fa4180bafd2205341c` |

## Contract delta and references

The inspected diff adds the closed-shape section, its opening cross-reference and
small wording changes distinguishing encoding approval and remaining external
resource/selection inputs. Removing that section and cross-reference and reversing
those two wording substitutions in memory exactly reproduces the complete before
bytes and SHA-256 `c9d8080a0a111c7bd22af3b17120655b042f85220f7115fa4180bafd2205341c`.
The logical record, three-graph, coordinate, publication and admission requirements
remain unchanged. The earlier logical receipt retains its original proposal hash;
the later before file is a separate reference-updated context.

All twelve current local link occurrences in the contract resolve. Its self-link
matches `Closed descriptor shape proposal`; existing loading and browser-resource
fragments match their headings. Schema references resolve through the fixed local
publication schema and its identifier/digest definitions. No instance field can
supply a schema URL. These are artifact checks, not HTTP or eligible-serving proof.

## Independently executed tooling and probes

Executed in the repository:

- `python scripts/validation/test_scene_descriptor_schema.py`: **4 test methods passed**.
- `python -B -m unittest discover -s scripts/validation -p 'test_*schema.py'`:
  **15 local schema test methods passed**.

The `-B` flag disables bytecode writes for the latter command. These methods and
their subcases validate local proposed schema shapes and fixtures only. They do
not exercise a compiler, actual JSON ingress, application request, persistence,
serving, resource fetch or movement boundary. The reviewer independently observed
installed evidence tooling `jsonschema` 4.23.0 and `referencing` 0.37.0; this does
not select the production compatibility graph.

Additional in-memory probes reused the handwritten synthetic fixture while
deriving expected results from the contract. Unknown fields were rejected at
the root and each represented nested record boundary: area, bundle, placement,
bounds, detail, anchor, pose, node binding, connection endpoints, destination,
safe-entry reference and interaction reference. Other independently observed
results are recorded below; the probes created no new source/test file.

| Boundary | Independent result and implication |
| --- | --- |
| Traversable/scenery conditions | Empty traversable collision or absence of a safe-entry purpose was rejected. Scenery walking anchors were rejected; producer fixtures also exercise scenery collision/panel exclusions. This proves those structural conditions, not authored ground or anchor safety. |
| Domain reuse | Publication-domain identifiers of length 96 were accepted; length 97, URL and final-newline values were rejected. Instance references remain opaque identifiers requiring semantic resolution. |
| Scalars/indices | Wrong vector arity, zero scale and infinity are rejected by tooling; independent probes also rejected negative-zero scale, boolean node index and boolean schema version. The maximum safe integer index passes shape but still requires an actual existing node. |
| Directed topology | Separate forward/reverse records pass shape. No reverse edge is inferred. An empty threshold list passes shape and still requires authored proof that no canonical threshold applies. |
| Absent spatial mapping | `safe_entry: null` passes for a semantic-only destination; a null connection source fails. Null entry creates no traversable permission or serving eligibility. |
| Semantic obligations | Zero/nonunit quaternion, reversed bounds, unresolved/wrong-kind opaque artifact reference, negative nonzero scale and differently populated duplicate area ID all pass shape. Contract lines 218–223 explicitly require compiler/export checks for these meanings. |
| Non-JSON NaN | A programmatic Python NaN in a scalar passes number min/max shape validation. Strict JSON constant rejection and finite parsed/calculated checks are separately required before schema/semantic validation; no such ingress parser is implemented or claimed here. |
| Registry failure | An unregistered local schema reference raised `_WrappedReferencingError`. The inspected registry uses the default fail-to-retrieve behavior rather than a network retrieval callback. Missing references cannot be treated as valid. |

## Findings and authority reconciliation

1. **Closed records and conditional forms fit the logical contract.** The schema
   closes every object and names the top-level fields explicitly. It excludes
   containing-manifest digest, URLs, approval/staff/private process fields and
   audio activation. Three 3D streams are accepted; S-SEMANTIC requires no scene
   descriptor. Traversable areas require visual/collision references and a
   safe-entry purpose. Scenery permits none of the collision/panel/anchor entries.
   Semantic-interaction anchors require both destination and route selectors,
   with paired optional bindings for other applicable purposes. Optional detail
   is structurally separate from essential bundles. No schema kind or public
   envelope field was changed.

2. **Transform and anchor encoding is explicit without asserting physical proof.**
   Proposed placement TRS and XYZW rotation exclude a competing matrix field.
   Anchor pose is already area-local; optional node binding is verification
   provenance, not an additional runtime transform. The source hierarchy is
   resolved during export preparation. Placement, geometry and variant revisions
   remain independent selectors, and interpretation resolves to a same-release
   shared artifact with its own still-held format. Unit quaternion tolerance,
   composed finite/invertible transforms, winding/scale, bounds enclosure and
   actual geometry remain semantic/export obligations. No body scale, movement
   speed, clearance or production budget is chosen by the binary64 capacity bound.

3. **Connections and null mappings preserve canonical control.** Source/target
   encode one direction and reverse travel needs a separate record. Threshold
   selectors must semantically cover the actual canonical thresholds; an empty
   list cannot bypass a held wing. Safe-entry null means no spatial mapping while
   independently eligible semantic access remains available. Correct anchor
   purpose, route/key agreement, uniqueness and coverage require compiler checks
   against wayfinding and publication. No room opening, route creation, staff
   presence, booking outcome or permission is encoded as geometry truth.

4. **Shape cannot substitute for the three graphs or admission.** The added
   section preserves index references versus acyclic required-resource closure
   versus potentially cyclic walking topology. The fixture's cyclic walking
   directions do not prove a required-resource graph. Instance IDs neither fetch
   all indexed resources nor authorize arbitrary URLs. Same-release/stream kind,
   exact bytes, interpretation, eligibility, resource reservations, late-work
   fences and one admitted render/collision/anchor context retain their existing
   loading/publication obligations. No eager whole-campus/audio fetch or automatic
   stream switch is introduced.

5. **Tool evidence is bounded accurately.** The tooling checks Draft 2020-12 schemas
   and uses two explicitly registered local resources. Synthetic dimensions and
   selectors are labelled fixture data. It checks positive forms and meaningful
   structural rejection cases without claiming actual ingestion or application
   enforcement. The explicit NaN/parser and semantic limitations above agree with
   the contract. Duplicate JSON keys and invalid Unicode require ingress handling
   before an already-parsed dictionary reaches this validator. Fixture success
   cannot establish privacy, allowed payload content or bounded production work.

6. **New encoding remains a reviewable proposal.** The earlier logical receipt does
   not cover this schema/tooling; the current notice makes that clear. Exact
   resource/interpretation/selection schemas, registration, limits and acceptance
   remain held. This review identifies no blocking contradiction with D-064/65/66/71,
   F3D-04–07/14, loading, World, publication or wayfinding. It grants no production
   permission, compatible lock selection, rights, geometry or composition revision.

## Primary schema/tool guidance

Independently read the cited official guidance on 2026-10-05:

- The validation vocabulary describes structural assertions, required/dependent
  fields and array equality/uniqueness; unique array values are not a distinct-ID
  projection. The proposal uses the existing Draft 2020-12 dialect without
  presenting it as a new final IETF RFC or production tool selection.
  [JSON Schema validation vocabulary](https://json-schema.org/draft/2020-12/json-schema-validation)
- The referencing documentation supports explicit Registry/Resource registration
  and separates registration from retrieval callbacks. Current online stable
  documentation is distinct from the locally observed tooling versions; the
  independent fail-to-retrieve probe corroborates this local setup's behavior.
  [jsonschema local referencing](https://python-jsonschema.readthedocs.io/en/stable/referencing/)

The producer's Context7 query and additional observations are separate provenance;
the reviewer did not independently replay Context7 or accept its observations as
proof in place of the executions above.

## Remaining gates and limits of PASS

Schema/encoding approval, strict parsing and finite-value enforcement, semantic
uniqueness/reference/kind/stream validation, quaternion tolerance, resource URI and
interpretation formats, descriptor registration/selection, actual dependency
closure and ownership remain required. Authored geometry, node/frame correspondence,
collision/endpoints, bounds, scene roots, safe entry, canonical opening/route
coverage and destination migration need compiler/export/reimport and runtime
evidence. Production keys/grants, payload/work/residency budgets, compatible
stable locks, rights, screens, physical devices and integrated/founder acceptance
retain their existing gates.

No application/runtime, collision/safety, privacy/security, accessibility,
performance, device, rights or Phase 1 acceptance follows from schema validity or
test counts. Prior review identities remain preserved. The reviewer authored only
this receipt; no producer document, application, protected asset, configuration,
dependency, Figma, account, commit, push or deployment was changed.
