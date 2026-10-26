# System definition and reconciliation map — v1

Status: DOING. Prepared 2026-10-04 from founder direction. This navigation map
does not accept unfinished definitions or authorize application implementation.

## The system being defined

Hengshi Design is an evidence-led innovation delivery platform. Visitors first
reach a semantic, search-first website containing services, sectors, evidence,
and discovery booking. They may explicitly enter an immersive World. Detailed,
Balanced, Simplified 3D and Quick Access are peer delivery streams; automatic
selection and an optional override preserve equivalent content and actions.
Quick Access provides the accessible non-WebGL journey.

The founder's free-movement addition selects mouse controls on desktop and touch
controls on mobile, free steering/walking, and spatial loading around the visitor.
Clickable destinations remain available; WASD is not selected. Streaming loads
areas as movement changes, including reversals; it is separate from graphics
detail selection. The [World definition](../phase-1-3d/WORLD_EXPERIENCE.md) records proposed gestures,
loading and sound behavior; final budgets and device thresholds still require
definition and validation. This behavior is selected scope, not built code.

Staff manage approved content and publication. Semantic pages, World panels and
AI guidance share approved published truth. The target retains a React web
application and modular FastAPI API, PostgreSQL durable data,
approved-knowledge guidance, human handoff and booking. Existing application code
and the exterior GLB remain protected prototype evidence.

D-068 defers deployment/provider/region/cost planning, leaving Azure and AWS as
candidates and lowest feasible cost/free services preferred for later planning.
Outlook/Teams remain intended without a Microsoft 365 prerequisite; exact API
capabilities and approved Entra/AI privacy restrictions remain gates. D-069 names
the current product/definition v1 and requires the complete latest mutually
compatible stable graph. D-070 targets Europe first and supplies editable company
facts plus founder-approved dedicated contact aliases, not verified operations.
D-071 accepts the final-third campus composition as the layout basis: central
reception, five wings and connected landscape. Detailed appearance, dimensions,
safe traversal, production budgets and full Phase 1 acceptance remain held.

## One controlling source per subject

| Subject | Controlling entry point | Reconciliation needed |
|---|---|---|
| Governance and approvals | [Constitution](../../.specify/memory/constitution.md) and [decisions](../../DECISIONS.md) | Preserve accepted authority; proposals cannot approve themselves. |
| Product, claims, routes and SEO | [Accepted foundation](../phase-1-foundation/README.md) | Carry accepted requirements into feature specs by reference. |
| Brand and identity | [Accepted identity](../phase-1-brand-identity/README.md) | Preserve accepted assets and evidence. |
| Journeys and recovery | [UX flows](../phase-1-ux-architecture/FLOWS.md) and [states/recovery](../phase-1-ux-architecture/STATES_AND_RECOVERY.md) | Reconcile free movement, World entry and equivalent access. |
| Production UI references | [Reference design](../phase-1-ui-reference-design/README.md) and [reference production](../phase-1-ui-reference-production/README.md) | Definitions are not completed screen production. |
| Architecture | [Accepted boundary baseline](../phase-1-architecture/ARCHITECTURE.md) and [movement addendum](../phase-1-architecture/MOVEMENT_STREAMING_ADDENDUM.md) | D-065 accepts the baseline's recorded bytes; its original proposal status, constitution identifier and directed-navigation/cloud wording are frozen evidence. D-064, D-068 and D-069 supply current amendments. Use the addendum and detailed contracts without reopening the accepted responsibility split. |
| 3D production | [World definition](../phase-1-3d/WORLD_EXPERIENCE.md), [spatial storyboard](../phase-1-3d/SPATIAL_STORYBOARD.md) and [asset build specification](../phase-1-3d/CAMPUS_ASSET_BUILD_SPEC.md) | D-071 accepts the final-third layout basis. The internal inventory and researched engineering proposal now have [bounded independent review PASS](../phase-1-3d/reviews/campus-asset-engineering-v1-2026-10-05.md). Complete detailed appearance, dimensions, collision, measured budgets, provenance and approved production specification. |
| Client loading and residency | [Controlling section in the campus build specification](../phase-1-3d/CAMPUS_ASSET_BUILD_SPEC.md#loading-and-residency-contract) | [Correction-1 independent review PASS](../phase-1-3d/reviews/campus-loading-contract-v1-2026-10-05.md#correction-1-verification--superseding-bounded-verdict) covers staged readiness, shared leases, reversal, draining work/reservations, safe eviction, release refresh and context recovery. Walking topology may loop; manifest dependencies cannot. Keep the lifecycle here instead of copying it into journey/spec documents. Exact profiles, scene schema, authored clearance/borders, controls, compatible graph, cleanup mechanisms, rights and actual runtime evidence remain held. No model revision or implementation permission. |
| Visitor-enabled sound | [Controlling lifecycle in the World definition](../phase-1-3d/WORLD_EXPERIENCE.md#audio-lifecycle-and-ownership-proposal) | [Bounded independent review PASS](../phase-1-3d/reviews/world-audio-lifecycle-v1-2026-10-05.md) covers intent/browser/release gates, shared media ownership, late-work fencing, draining resources, zone blends and silent recovery. Keep this lifecycle here by reference; it creates no second audio specification or model revision. Exact assets/rights, codecs, levels/timings, finite named-device profiles, compatible wrappers, production screens and actual audio/browser/phone proof remain held. |
| Published scene assembly | [Logical assembly proposal](../phase-1-3d/SCENE_ASSEMBLY_CONTRACT.md) and [closed descriptor shape proposal](../phase-1-3d/SCENE_ASSEMBLY_CONTRACT.md#closed-descriptor-shape-proposal) | Separate [logical review](../phase-1-3d/reviews/scene-assembly-v1-2026-10-05.md) and [shape/encoding/tooling review](../phase-1-3d/reviews/scene-descriptor-shape-v1-2026-10-05.md) record bounded PASS at their own exact inputs. Areas, geometry/collision references, transforms, anchors, directed crossings and semantic-only destination mapping now have a proposed closed shape; local shape tests are not compiler, loader, eligibility or movement proof. Later receipt-reference edits are outside reviewed bytes. Schema/encoding and descriptor packaging/selection approval, strict parsing/semantic enforcement, resource-format acceptance, collider binding, authored geometry/clearance, finite profiles, compatible graph, rights and actual compiler/loader/mover evidence remain held. No new endpoint, model revision or implementation permission. |
| Visual glTF resources | [Resource interpretation proposal](../phase-1-3d/SCENE_ASSEMBLY_CONTRACT.md#visual-resource-interpretation-proposal) and [closed shape](../phase-1-3d/gltf-resource-map.schema.json) | [Bounded independent review PASS](../phase-1-3d/reviews/gltf-resource-map-v1-2026-10-05.md) covers exact appended explanation, schema and local tooling: build/profile binding, external GLB resource inventory, proposed URI subset, manifest dependency obligations and controlled decoder references. Original contract bytes are preserved; later receipt references are outside reviewed inputs. Shape tests do not prove profile membership, extension support, mapping completeness or controlled fetching. Exact build/registry registration, supported extensions/decoder formats, separate collider interpretation, measured limits, resource permissions/origins, provenance/rights, complete stable graph, actual compiler/resolver/loader enforcement and integrated/founder acceptance remain held. No new artifact kind, resource authorization or geometry change. |
| Static collision interpretation | [Logical static profile and binding](../phase-1-3d/SCENE_ASSEMBLY_CONTRACT.md#static-collision-interpretation-proposal) and [publication-owned lookup](../phase-1-architecture/contracts/PUBLICATION_CONTRACT.md#collision-map-registration-proposal) | [Bounded independent review PASS](../phase-1-3d/reviews/collider-binding-v1-2026-10-05.md) covers only the exact additive proposals: separate static collision GLBs, complete placed primitive inventory, same-release/stream/build consumer binding, reserved lazy lookup, transform-once baking, staged query exclusion, guarded admission and safe instance retirement. Earlier bodies and closed schemas are unchanged; later receipt references are outside inspected bytes. Collision is distinct from visual profiles, route planning and current room permission. Collision map/profile/engine-unit format acceptance, actual build association, controller/geometry/clearance and numeric profiles, measured budgets, rights/permissions, the complete stable graph, runtime and integrated/founder acceptance remain held. No model revision or movement implementation is authorized. |
| Collision-map closed shape | [Proposed encoding](../phase-1-3d/SCENE_ASSEMBLY_CONTRACT.md#closed-collision-map-shape-proposal) and [schema](../phase-1-3d/collision-resource-map.schema.json) | DOING. [Bounded independent review PASS](../phase-1-3d/reviews/collision-map-shape-v1-2026-10-05.md) covers only the exact new schema, real-validator tooling and additive encoding appendix at 29 frozen inputs. The retry reproduced five focused methods and records the earlier completed independent 31-method schema suite separately from the interrupted attempt, which had no verdict. Closed release/stream/build/collision-profile and scene/node/primitive records are structural checks; key uniqueness, complete actual-byte coverage, eligibility and safe movement remain separate. Later receipt-reference edits are outside the inspected bytes. Collision consumer/engine-unit format acceptance, actual-byte and build association, geometry/clearance, budgets, rights, full stable graph, runtime and integrated/founder acceptance remain held. No model revision or implementation permission. |
| Collision-consumer catalogue | [Typed consumer/unit amendment](../phase-1-architecture/contracts/PUBLICATION_CONTRACT.md#collision-consumer-catalogue-amendment-proposal) and [catalogue schema](../phase-1-architecture/contracts/client-build-catalogue.schema.json) | DOING. [Bounded independent review PASS](../phase-1-architecture/contracts/reviews/client-collision-catalogue-v1-2026-10-05.md) covers only the collision profile inventory, distinct wrapper/WASM role candidates, labelled World gate/MIME conditions, corresponding validator tooling and additive explanation. Seven focused and 34 broader schema methods were independently reproduced. Actual emitted resources must account for embedded versus separate WASM without invented artifacts or decoder relabelling. Prior visual-only receipts retain their exact input/scope; later reference reconciliations are outside this new receipt. Actual compiled roots/code association, graph/roles/permissions, engine/version/format acceptance, geometry/budgets/rights, full stable selection, runtime and integrated/founder acceptance remain held. No engine, provider, browser grant, model revision or application development is authorized. |
| Client build and scene entry lookup | [Publication-owned build/registration proposal](../phase-1-architecture/contracts/PUBLICATION_CONTRACT.md#client-build-identity-and-registered-entry-proposal), [closed catalogue shape](../phase-1-architecture/contracts/client-build-catalogue.schema.json) and [World lookup proposal](../phase-1-3d/SCENE_ASSEMBLY_CONTRACT.md#scene-lookup-and-build-agreement-proposal) | [Bootstrap review PASS](../phase-1-architecture/contracts/reviews/scene-bootstrap-v1-2026-10-05.md) covers its exact additive logical proposals. The separate [catalogue shape review PASS](../phase-1-architecture/contracts/reviews/client-catalogue-shape-v1-2026-10-05.md) covers its exact closed records, fixed entry gates, profile/decoder metadata and local tooling; four focused and 23 broader schema methods were independently reproduced. Previous contract bodies are preserved; later receipt references are outside inspected bytes. Shape checks cannot establish graph/gate enforcement, supported profiles or actual code-registry association. Binding/format acceptance, registration/serving mechanisms, emitted import coverage, trusted runtime association, separate collider formats, finite bounds, permissions/provenance, full stable graph, actual compiler/browser enforcement and integrated/founder acceptance remain held. No new envelope field/kind, endpoint or implementation permission. |
| Public document release/build context | [HTML binding proposal](../phase-1-architecture/contracts/PUBLICATION_CONTRACT.md#public-html-binding-proposal) and [closed shape](../phase-1-architecture/contracts/public-html-binding.schema.json) | [Bounded independent review PASS](../phase-1-architecture/contracts/reviews/public-html-binding-v1-2026-10-05.md) covers the exact additive proposal: one compiler-owned inert data block, canonical restricted-ASCII JSON, independent release/route/planned HTML/build identifiers without self-hash cycles, pinned IF-PUB-02 resolution and separate admission/executed-code trust. Three focused and 26 broader schema methods were independently reproduced; none tests actual HTML parsing, serialization, hydration, served code or eligibility enforcement. Later receipt references are outside inspected bytes. Format/integrated/founder acceptance, real renderer/router/parser, registered code/HTML/policy association, integrity/serving mechanisms, finite limits/origins/permissions, stable graph and runtime evidence remain held. No public executable instruction, private process field, new endpoint or entry/consent permission. |
| Visual publication explanation | [One-publication walkthrough](definition-walkthrough.html#publication-flow) | [Bounded independent review PASS](reviews/publication-walkthrough-v1-2026-10-05.md) covers only the added navigation/detail block and exact complete desktop/mobile captures: content review, preparation, page pinning, deliberate matching World entry and explained recovery. Previous board/CSS bytes are unchanged. Producer keyboard, layout, five HTTP links and zero-console-error observations are separate from independent source/image inspection. No actual publication, parser, serving/code trust, loading, full accessibility, physical-phone or whole-board/founder acceptance is certified. |
| Exact interfaces and data | [Interface/process contract](../phase-1-architecture/contracts/INTERFACE_CATALOG.md), [publication contract](../phase-1-architecture/contracts/PUBLICATION_CONTRACT.md) and [logical data contract](../phase-1-architecture/contracts/DATA_CONTRACT.md) | Complete exact schemas and policy mappings here; feature contracts refine them by reference after acceptance. |
| Semantic preparation | [Publication engineering proposal](../phase-1-architecture/contracts/PUBLICATION_CONTRACT.md#semantic-preparation-engineering-proposal) and [private message/acceptance proposal](../phase-1-architecture/contracts/PUBLICATION_CONTRACT.md#private-preparation-message-and-acceptance-proposal) | Separate [engineering](../phase-1-architecture/contracts/reviews/semantic-preparation-v1-2026-10-05.md) and [message/schema](../phase-1-architecture/contracts/reviews/preparation-message-v1-2026-10-05.md) reviews pass their bounded inputs. Exact worker/transaction/resource/retention mechanisms, the full stable graph and actual rendering/navigation/activation proof remain; preparation has no publication authority. |
| Security and privacy | [Security/privacy contract](../phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md), its [action/object matrix](../phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md#proposed-action-and-object-authorization) and [data classification](../phase-1-architecture/contracts/data-classification.csv) | Shared controls govern feature 001 by reference. The [browser-resource/serialization proposal](../phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md#browser-resource-and-serialized-content-proposal) has a [separate bounded review PASS](../phase-1-architecture/contracts/reviews/browser-resource-security-v1-2026-10-05.md); exact permissions, origins, style mechanisms and actual enforcement remain held. The [private-process proof proposal](../phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md) and [correction-1 bounded PASS](../phase-1-architecture/contracts/reviews/private-process-proof-v1-2026-10-05.md#correction-1-disposition--superseding-bounded-pass) refine anonymous access without accounts: per-process protected cookie, two-phase chat/booking creation, separate CSRF and current HTTP/socket checks. Reviewed exact bytes remain preserved; later references are outside them. Exact formats, validity/recovery, finite bounds, physical enforcement, identity methods, grants, retention/legal mappings, full stable graph and integrated/founder acceptance remain. |
| QA and recovery | [QA/recovery contract](../phase-1-architecture/contracts/QA_RECOVERY.md) and [acceptance matrix](../phase-1-architecture/contracts/acceptance-matrix.csv) | Shared evidence obligations govern feature 002 by reference. Its browser-release wording repair is held separately; definition checks do not prove runtime conformance. |
| Compatibility and operations | [Compatibility entry](../phase-1-compatibility/README.md) and [native local guide](../../README.md#native-local-operation-on-windows) | Complete approved compatibility; D-068 defers deployment/cost/region planning. Dated prototype observations do not prove continuing service health. |
| Feature execution | [Feature index](../../specs/README.md) | Generate feature plans/tasks only from reconciled requirements. |
| Current checkpoint | [Project state](../../PROJECT_STATE.yaml) | Distinguish approved definitions, tested code and deferred commits. |

## Engineering responsibility and the client brief

On 2026-10-05 the founder directs the producer to act as the development provider:
translate the client's vision into researched technical recommendations, identify
alternatives and tradeoffs, and propose the complete architecture and build path.
The founder's descriptions of a horizon, free look and nearby loading express the
desired experience; they are not assumed engine designs. The founder approves
continuing that engineering direction and the existing goal. This does not select
every proposed library or accept the unfinished integrated Phase 1 package.

The [campus engineering proposal](../phase-1-3d/CAMPUS_ASSET_BUILD_SPEC.md#researched-engineering-recommendation)
separates input/camera, collision-aware movement, destination planning, connected-
area loading, resource residency, rendering and server-authoritative help/content.
The [asset inventory](../phase-1-3d/asset-manifest.json) assigns all 117 observed
mesh nodes once to 15 authoring families, preserving source identities and
canonical destinations. Neither changes the accepted authority boundaries or
creates a second public publication manifest.

After the applicable definition approval, prove one complete arrival → reception
→ first eligible department → information/help → booking journey before campus
expansion. All-around landscape depth and an eye-level walking camera carry the
client's vision; the study's orbit/target zoom is an inspection control. Additional
libraries need complete stable compatibility and measured benefit before selection.
Their [independent review](../phase-1-3d/reviews/campus-asset-engineering-v1-2026-10-05.md)
now records bounded PASS for exact source accounting and proposal coherence.
Appearance, physical traversal, devices, numerical budgets, rights and runtime
behavior remain separate evidence obligations.

## Retain, supersede and retire

Retain governance, canonical requirements, contracts, design sources, feature
plans and tests. Retain accepted review evidence and historical artifacts without
treating them as additional live specifications. Replace duplicated live prose
with references when its canonical successor is established.

The legacy SRS/SAD, SPEC/BACKLOG and current-state diagrams are prototype/history
evidence, as already stated in this directory's README. Their names do not give
them production authority. The older documentation index's Phase 1-not-started
statement has been reconciled; its [current successor table](../active/Documentation_Index.md#current-successors-for-historical-documents)
now assigns exact historical document families to controlling requirements,
architecture, contracts, tasks and deferred deployment records. The old
requirements-to-architecture mapping is explicitly historical: its admin-role
verification claim contradicts the current `require_admin` implementation and
does not close R-004. The foundation entry point now distinguishes D-025's
accepted status from its preserved July pre-approval review snapshot. Its accepted
requirements, route data and review evidence remain intact.
The [deferred deployment entry](../../specs/005-azure-deployment-launch/README.md)
records current D-068 over both historical provider folders; their names select
neither Azure nor AWS. The security feature's six June artifacts
were classified as historical and independently reviewed for authority/readiness
reconciliation. The active [security feature](../../specs/001-platform-security-hardening/spec.md)
now has a proposed v1 definition and producer checklist; their prior reviewed bytes
are preserved in its `history/` text snapshots. The old review covers those snapshots,
not the replacement draft. June research/data/plan remain historical and its tasks
file remains a blocked readiness placeholder, not an executable plan.

No file deletion or folder move is authorized by this map. A retirement list must
name each successor and preserve decision, review and asset provenance first.

## Route to a coherent checkpoint

1. Inventory current definitions, code evidence and outstanding gates; assign
   each subject a canonical source and classify legacy material explicitly.
2. Reconcile the system and user journeys, including founder-selected movement
   and streaming; identify only genuinely unresolved material choices.
3. Complete architecture, interfaces, security/privacy, 3D, QA, compatibility and
   operating-envelope definitions against that same system description.
4. Reconcile Spec Kit features to the canonical definition; avoid copying whole
   product documents into each feature. Review obsolete assumptions and tasks.
5. Validate references and behavior traceability, independently review material
   definitions, and present the coherent package for founder acceptance.
6. Begin approved implementation afterward. Commits and pushes remain deferred.

Phase 1 closes through the controlling [task exit contract](../../TASKS.md#exit-and-later-phases):
coherent non-deferred definitions, required production UI references, a complete
compatible stable graph or approved dated exception, proportionate validation and
independent review, and founder acceptance. Define actual HTTP, movement, recovery
and other runtime qualification methods and criteria here; application feature
implementation and its runtime qualification follow in the later approved phases.
They are not circular prerequisites for Phase 1 acceptance, and remain unauthorized
before that acceptance. Missing required designs, material contracts and legal-policy
choices cannot be inferred as approved. D-068 still defers hosting/provider/region/
cost selection. This clarification changes no acceptance or later implementation gate.

## Coverage against the fourteen Phase 1 deliverables

Task statuses describe work still required; accepted definitions are identified
separately. Deferred commits prevent code tasks being called DONE.

| Deliverable | Status | Evidence and remaining work |
|---|---|---|
| 1. Product requirements | DOING | D-025 accepts the foundation. The [current requirements authority](../phase-1-foundation/01-product-requirements.md#current-v1-authority--reconciled-2026-10-05) and [conversion-model authority](../phase-1-foundation/04-conversion-measurement-model.md#current-v1-authority--reconciled-2026-10-05) reconcile later audience, streams/movement, no-JS transaction boundary, deferred hosting, stable v1 technology, editable facts/campus and process/data refinements over preserved July rows and metrics. Their [bounded independent review PASS](../phase-1-foundation/reviews/current-authority-references-v1-2026-10-05.md) covers exact additive headers and sources only. Production references, complete contracts/graph, verified content/legal inputs and integrated acceptance remain; no new metric, policy, grant, runtime proof or implementation permission. |
| 2. Claims/content evidence | DOING | Foundation ledger retained; [entity/contact addendum](06-entity-and-public-contact.md) records founder-supplied Pakistan company facts and identifier-display research. Certificate correspondence, PSEB validity, legal review, expert/owner/proof evidence remain held. |
| 3. SEO/content strategy | DOING | The accepted foundation's [current SEO authority](../phase-1-foundation/03-seo-entity-route-editorial-strategy.md#current-v1-authority--reconciled-2026-10-05) links Europe-first targeting, supplied editable company facts, current route inventory and one-snapshot publication over its preserved July context. The [visual SEO explanation](definition-walkthrough.html#semantic-seo) and authority header have [bounded independent review PASS](reviews/semantic-seo-definition-v1-2026-10-05.md) for exact additions, source references and complete inspected desktop/mobile captures; producer live keyboard/layout/link checks are separate. Verified copy/briefs, legal disclosure, production references, rendering/security mechanisms, stable graph and actual HTTP/no-JS/browser/sitemap evidence remain; no generation pipeline, submission or whole Phase 1 acceptance. |
| 4. Brand/identity | DOING | D-026/D-035 accepted. [World materials/assets](../phase-1-3d/WORLD_EXPERIENCE.md#scene-materials-and-reusable-asset-families) scopes D-067 to scene appearance while retaining accepted identity, interface/evidence tokens and accessibility. This expansion has scoped independent review PASS; it creates no new logo or brand palette and does not accept production appearance. |
| 5. UX/journeys | DOING | D-036 and later refinements accepted. The [flow amendment](../phase-1-ux-architecture/FLOWS.md#current-world-scope-amendment--v1) and [recovery amendment](../phase-1-ux-architecture/STATES_AND_RECOVERY.md#current-world-scope-amendment--v1) now link D-064's selected mouse/touch movement to the controlling proposed gestures/loading/audio definitions. Their [bounded independent review PASS](../phase-1-ux-architecture/reviews/world-authority-reference-v1-2026-10-05.md) verifies exact unchanged baseline bodies and reference accuracy only. The UX entry/core page now direct readers to those amendments; these later navigation references are outside that receipt. Production controls, profiles, visual references and integrated acceptance remain held; no additional substantive UX revision or runtime proof. |
| 6. Production UI references | TODO | Design/production contracts exist; actual Figma foundation screens and pilot proof remain gated. |
| 7. Production 3D definition | DOING | The [World definition](../phase-1-3d/WORLD_EXPERIENCE.md), [spatial storyboard](../phase-1-3d/SPATIAL_STORYBOARD.md) and [browser board](../phase-1-3d/spatial-storyboard.html) link their bounded review and preserved inspected bytes. Material families, sound zones and connected-campus obligations are defined proposals. Final geometry, collision/entrance/river continuity, measured budgets, screen references, rights and appearance acceptance remain. The earlier [connector assessment](../phase-1-3d/reviews/connector-geometry-inspection-2026-10-04.md) remains evidence of the unchanged earlier composition. Independent accounting corrected its premature exhaustion gate. The [final third layout study](../../artifacts/nature-campus-layout-study/README.md) now has three same-export views; its [bounded review](../phase-1-3d/reviews/final-third-layout-study-2026-10-04.md) reproduces sampled floor coverage, no tested obstruction/buried-floor points and viewer behavior. It has 16 solid materials without textures and an over-budget whole GLB. This does not certify continuous/body clearance, construction, collision, appearance or runtime features. The founder accepts this composition as the layout basis under D-071; detailed appearance, dimensions, safe traversal and production evidence remain held. All three normal model revisions are used; acceptance grants no further substantial composition exception. The [numerical measurement/loading profile](../phase-1-3d/WORLD_MEASUREMENT_PROFILE.md) has [correction-1 bounded review PASS](../phase-1-3d/reviews/world-measurement-profile-v1-2026-10-06.md#correction-1-disposition--superseding-bounded-pass): complete CPU World-frame submission sampling, actual transfer versus resident inventory, finite cost/work targets and sustained qualification method. Numerical values remain unmeasured proposals; named devices/workloads/calibration, approved references and actual runtime qualification remain. The [mouse/touch body/camera/traversal profile](../phase-1-3d/WORLD_EXPERIENCE.md#mouse-touch-traversal-and-camera-profile-proposal--2026-10-06) also has [bounded independent review PASS](../phase-1-3d/reviews/world-traversal-profile-v1-2026-10-06.md): no-drag/keyboard alternatives, finite human/camera/speed/clearance targets, stalled-frame handling and current swept support/readiness. These are proposed definitions; pad cancellation mapping, production screens/geometry, physical comfort/accessibility, selected adapter/runtime and integrated/founder acceptance remain. |
| 8. Architecture/ADRs | DOING | D-065 accepts the frozen [boundaries](../phase-1-architecture/ARCHITECTURE.md). The [movement addendum](../phase-1-architecture/MOVEMENT_STREAMING_ADDENDUM.md) links its bounded review and preserved inspected bytes: initial release resolution, eligible visit pins and safe refresh remain separate. Detailed contracts and integrated acceptance remain. |
| 9. API/data/publication contracts | DOING | [Interface/process fields](../phase-1-architecture/contracts/INTERFACE_CATALOG.md), [publication](../phase-1-architecture/contracts/PUBLICATION_CONTRACT.md) and [logical data](../phase-1-architecture/contracts/DATA_CONTRACT.md) link their bounded reviews and preserved inspected bytes. The later HTTP, error-schema and availability refinements are listed below. The [common scalar helper](../phase-1-architecture/contracts/process-value.schema.json) and [bounded independent review](../phase-1-architecture/contracts/reviews/common-process-values-v1-2026-10-06.md) cover reused UUID/revision/digest representation and seven validator-boundary tests only; field adoption and raw-parser enforcement remain held. The [shared raw JSON admission proposal](../phase-1-architecture/contracts/DATA_CONTRACT.md#raw-json-admission-proposal--2026-10-06) and [independent review](../phase-1-architecture/contracts/reviews/raw-json-admission-v1-2026-10-06.md) now define the logical intake boundary with reproduced installed-parser observations; they do not prove a compliant alternative decoder or actual HTTP enforcement. Exact remaining directional schemas, proofs, bounds, retention, physical constraints and provider mechanisms remain; no implementation authority follows from review. The later [booking creation request schema](../phase-1-architecture/contracts/booking-creation-request.schema.json) and [independent review](../phase-1-architecture/contracts/reviews/booking-creation-request-v1-2026-10-06.md) close the proposed bootstrap/create client bodies only; eight new and seven common validator tests pass. The subsequent [server projection schema](../phase-1-architecture/contracts/booking-creation-response.schema.json) and [transport/lifetime/work profile](../phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md#booking-creation-transport-and-response-profile-proposal--2026-10-06) have [bounded independent review PASS](../phase-1-architecture/contracts/reviews/booking-creation-http-v1-2026-10-06.md): eight response, eight request and seven common validator methods pass. Proposed capacities/lifetimes are unmeasured; legal/store/ingress/Origin/cookie/CSRF/fencing enforcement, other private protocols, stable graph and integrated/founder acceptance remain. The [shared private-browser JSON profile](../phase-1-architecture/contracts/DATA_CONTRACT.md#private-browser-json-admission-profile-proposal--2026-10-06) has [bounded definition review PASS](../phase-1-architecture/contracts/reviews/private-json-profile-v1-2026-10-06.md); its finite limits are unmeasured proposals, with no decoder or HTTP enforcement implemented. |
| 10. Security/privacy/AI controls | DOING | Scoped independent review PASS covers the listed hashes of the [security/privacy proposal](../phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md), role/action/object matrix and availability-classification amendment. The later [security feature draft](../../specs/001-platform-security-hardening/spec.md) and producer checklist have their own [bounded independent review PASS](../../specs/001-platform-security-hardening/reviews/security-feature-v1-2026-10-04.md). No administrator inheritance, self-approval or automatic operational grants are introduced. Exact identity/session/permission/control and legal/provider policies, applicable legal/accessibility review and founder acceptance remain; durable availability intent retention is unmapped. Privacy/security alias ownership stays undecided. No runtime security proof follows from either definition review. |
| 11. QA/recovery strategy | DOING | Scoped independent review PASS covers the listed hashes of [cross-layer QA/recovery](../phase-1-architecture/contracts/QA_RECOVERY.md) and matrix amendments. The later [QA feature draft](../../specs/002-testing-and-monitoring/spec.md) and checklist have [independent review REVISE](../../specs/002-testing-and-monitoring/reviews/qa-feature-v1-2026-10-04.md): the addendum supersedes its initial PASS. The one-word browser families-to-releases repair awaits a founder revision-limit exception and exact-hash re-review. Physical-phone access, exact measurement/SLI/recovery/retention inputs, isolated test authorization and runtime evidence remain held. The controlling targets remain approved obligations, not measured results; the feature wording conflict remains held. |
| 12. Compatibility graph | DOING | The [compatibility entry](../phase-1-compatibility/README.md#current-authority-and-dated-evidence) controls dated candidates and preserved scoped receipts. The newest coupled frontend candidate fails loader declarations; the matching Three184 candidate has [independent compiler/build/browser evidence PASS](../phase-1-compatibility/reviews/frontend-three-remedy-evaluation-v1-2026-10-06.md), retaining bundle/Clock warnings and browser/tool mismatch. Its separate [supply-chain accuracy review PASS](../phase-1-compatibility/reviews/frontend-supply-chain-v1-2026-10-06.md) retains the failed virtual optional-WASM inventory, partial attestations and licence/notice limits; zero reported known advisories is no security clearance. D-072 is lint-only through 2027-01-05. Complete conformance, provenance/licences/deployed inventory and exclusion, supported-platform/rollback evidence, full graph/MA-013 and any D-069 exception/founder selection remain. D-068 keeps hosting/packaging conditional without changing Entra/private-AI constraints. |
| 13. Costed operating envelope | TODO | Explicitly deferred by founder D-068. Azure/AWS candidates; lowest feasible cost/free services preferred when planning resumes. No region/SKU/budget/spend/provider selected. |
| 14. Legacy/feature reconciliation | DOING | The [successor catalogue](../active/Documentation_Index.md#current-successors-for-historical-documents) and [feature index](../../specs/README.md) control historical records and current v1 drafts. Security, World and content have separate exact-input bounded review PASS; QA has the held correction above. The [visual walkthrough](definition-walkthrough.html#features) presents their remaining inputs. Exact definitions, approved plans/tasks and integrated acceptance remain; historical security tasks and deferred deployment are not executable authority. |

This coverage does not infer implementation or runtime conformance from the
existence of documents or passing definition validators.

### Later contract refinements

The [governed consultation lifecycle](../phase-1-architecture/contracts/HANDOFF_LIFECYCLE.md)
now connects existing AF-02/SOF-01 and handoff/assignment/text interfaces. Its
[bounded independent review PASS](../phase-1-architecture/contracts/reviews/handoff-lifecycle-v1-2026-10-05.md)
covers exact preserved requirements and proposal inputs. One current request/
owner, consented projections, acceptance versus text connection, uncertain
operations, ending/off, old-owner replay and separate media consent are defined
obligations. Teams remains an alert destination. Exact policies/grants/owners,
retention, schemas, bounds, revocation/transaction enforcement, provider capability,
screen references and actual runtime proof remain held; no consultation is built
or activated. Later catalogue reference changes do not replace frozen review
identities or imply integrated acceptance.

The [staff availability write proposal](../phase-1-architecture/contracts/AVAILABILITY_WRITE_HTTP.md)
now refines existing IF-STAFF-09 and SOF-01A/B with closed declarations,
authorized subject resolution, initial/current binding checks, immutable
operation replay, uncertain-write recovery and minimal response/error projections.
Its [bounded independent review PASS](../phase-1-architecture/contracts/reviews/availability-write-http-v1-2026-10-05.md)
covers the exact preserved proposal and source inputs. An accepted declaration
is distinct from the [guarded public live offer](../phase-1-architecture/contracts/AVAILABILITY_READ_HTTP.md)
and human acceptance. Off cannot complete while an older on can still take effect;
replay is historical and cannot renew validity. Exact grants, expiry/renewal,
transport/work limits, staff/operation retention, physical constraints and actual
HTTP/transaction/browser proof remain held. No second availability authority,
new route, account, migration or application behavior is introduced.

The later [directional write encoding](../phase-1-architecture/contracts/availability-write.schema.json)
has [bounded independent review PASS after correction 1](../phase-1-architecture/contracts/reviews/availability-write-shape-v1-2026-10-05.md#correction-1-disposition--superseding-bounded-pass).
It closes the proposed command/response shapes, decimal revision range and error
correlations. The correction repairs canonical schema-ID resolution; the earlier
REVISE remains preserved. The HTTP sample ID also now matches its existing
32-character rule. Four corrected focused methods were independently reproduced;
the corrected broader schema suite is producer evidence. These are definition
and schema-tooling results, not strict raw parsing, authorization, current-state,
HTTP, mutation or live-presence proof. Later navigation edits remain outside the
inspected bytes; operational/legal/mechanism and integrated acceptance gates stay open.

The 2026-10-05 [semantic preparation engineering proposal](../phase-1-architecture/contracts/PUBLICATION_CONTRACT.md#semantic-preparation-engineering-proposal)
and [private preparation boundary](../phase-1-architecture/contracts/INTERFACE_CATALOG.md#private-preparation-boundary)
connect approved snapshots to complete HTML, matching hydration/navigation data
and the existing publication derivatives. The recommendation evaluates framework
data APIs and a bounded build adapter while retaining the two deployables and
publication authority. Its [registry evidence](../../output/research/semantic-delivery-2026-10-05/registry-observations.json)
records the current framework-mode dev candidate's beta dependency restriction;
neither that candidate nor the alternative is selected. This new material is
outside the earlier contract receipts; its separate
[independent review](../phase-1-architecture/contracts/reviews/semantic-preparation-v1-2026-10-05.md)
records bounded PASS at the preserved inspected hashes. Actual
rendering, hydration, release-pinned navigation, security, resource bounds and
the full stable graph require implementation evidence after their approval gates.

The later [private preparation messages](../phase-1-architecture/contracts/publication-preparation.schema.json)
and [coordinator acceptance proposal](../phase-1-architecture/contracts/PUBLICATION_CONTRACT.md#private-preparation-message-and-acceptance-proposal)
now have their own [bounded independent review PASS](../phase-1-architecture/contracts/reviews/preparation-message-v1-2026-10-05.md).
They bind closed requests/results to an admitted candidate and attempt, require
independent final-byte/input/coverage verification, and deny stale, conflicting
or partial results activation authority. Shape fixtures and independent schema
probes are definition-tooling evidence only. Authorization, actual byte checks,
fencing, cancellation, retention and resource enforcement need runtime evidence;
no job transport, public API or worker deployment is selected.

The [browser-resource and serialized-content proposal](../phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md#browser-resource-and-serialized-content-proposal)
connects unchanged published HTML to resource admission, typed public data and
safe parser-context serialization. Its [separate independent review](../phase-1-architecture/contracts/reviews/browser-resource-security-v1-2026-10-05.md)
passes the bounded proposal and primary/source observations. Same-document World
entry cannot relax the page's HTTP policy; decoder workers and WASM need explicit
reviewed permissions, while denial preserves the semantic recovery journey.
Exact origins, style/serializer mechanisms, the complete stable graph, actual
build/parser/browser/worker enforcement, reporting privacy and founder acceptance
remain held. This selects no deployed policy, decoder, provider or application
change, and does not extend the earlier identity/privacy review to new bytes.

The [public release-read HTTP proposal](../phase-1-architecture/contracts/PUBLICATION_READ_HTTP.md)
now defines eligible current/pinned reads, conditional requests and safe error
responses. Its [bounded HTTP review](../phase-1-architecture/contracts/reviews/publication-read-http-2026-10-04.md)
and [separate error-schema review](../phase-1-architecture/contracts/reviews/publication-read-error-schema-2026-10-04.md)
cover their listed inputs. Four focused schema-tooling tests pass; they exercise
envelope/error validation, not a running HTTP handler or publication service.

The [availability consistency protocol](../phase-1-architecture/contracts/AVAILABILITY_CONSISTENCY.md)
refines current intent, matching fresh presence, decision-time expiry and uncertain
withdrawal outcomes. Its [independent review](../phase-1-architecture/contracts/reviews/availability-consistency-2026-10-04.md)
passes the bounded proposal. Admission/fencing, physical constraints, measured
timing, operational grants and runtime evidence remain required. The later
[public availability GET proposal](../phase-1-architecture/contracts/AVAILABILITY_READ_HTTP.md)
now specifies proposed canonical department keys, closed state/expiry and error
bodies, strict raw JSON acceptance, conditional requests and stale/reordered client
recovery. Its [bounded independent review](../phase-1-architecture/contracts/reviews/availability-read-http-2026-10-04.md#correction-1-verification--superseding-bounded-pass)
passes after one strict-decoding correction; its exact inspected bytes are preserved.
Two schema-tooling tests pass for body correlation and calendar validation only.
Public disclosure/key/profile acceptance, lifetime/clock/resource rules and actual
decoder, HTTP, guard and client enforcement remain held. Neither review changes
accepted architecture or assigns an email owner.
The [typed company-facts proposal](06-entity-and-public-contact.md#typed-prepared-facts-proposal)
now has a closed [draft subdocument schema](../phase-1-architecture/contracts/company-facts.schema.json)
and [bounded independent review PASS after fixture correction 1](../phase-1-architecture/contracts/reviews/company-facts-shape-2026-10-04.md).
Its synthetic shape test checks identifier strings, month precision and exclusion
of workflow/private fields. Fact verification, disclosure, semantic/resource
policies, admin authorization, persistence and publication enforcement remain
held; schema validation cannot establish those outcomes.

Later reference edits link preserved inspected bytes rather than replacing the
hashes in earlier receipts. Full Phase 1 acceptance remains separate.

The [bounded amendment review](../phase-1-architecture/contracts/reviews/current-definition-amendments-2026-10-04.md)
records PASS with no open findings for its fifteen exact artifact hashes. That
bounded verdict supersedes older unreviewed/credit-failure notices for those
inputs only. It is not founder acceptance, full Phase 1 acceptance, production
appearance approval or application behavior proof. Compatibility studies remain
outside that review scope.
