# Publication and immutable release contract

Status: DOING. Date: 2026-10-04. PROPOSED detailed contract under D-019/D-065,
PUB-001–PUB-006 and DATA-001/DATA-010. No schema migration or application change.

## Representation and checksums

The [public envelope schema](publication-manifest.schema.json) defines a closed
technical manifest, not editorial authority. `manifest_sha256` is lowercase
SHA-256 of RFC 8785 canonical UTF-8 bytes of the nested `manifest` object. The
checksum field is outside that object, avoiding a self-hash cycle. Reject duplicate
JSON properties, invalid Unicode and incompatible schema versions before hashing.
Do not approximate JCS with arbitrary language-specific sorted serialization.
Each asset checksum covers exactly the immutable bytes stored under its key.

The manifest identifies one immutable approved content snapshot, route revisions,
artifact dependencies and delivery-stream applicability. Artifact keys are
relative storage keys, not visitor-supplied URLs. Application semantic validation
must also reject dot segments, encoded traversal, duplicate IDs/keys/routes and
unresolved/cyclic dependency references; the JSON shape schema alone cannot prove
approval, content truth, graph validity or active status.

Public manifests contain no staff approval identity, contact/lead/chat records,
booking tokens, provider settings or draft text. Private approval evidence remains
in PostgreSQL. JSON Schema `format` must be asserted by the selected validator;
an annotation-only date check is insufficient.

Definition check: `python scripts/validation/test_publication_manifest_schema.py`.
The local tooling uses installed `jsonschema` 4.23.0 with its optional
`rfc3339-validator` 0.1.4 checker. Setup explicitly requires `date-time`; missing
format support fails the check instead of accepting an invalid calendar date.
This is a local definition-tool capability, not the production compatibility
matrix or a production dependency selection. On another machine, install the
validator's documented format extras before running these checks.

## Private logical data, not approved database tables

| Logical record | Required responsibility |
|---|---|
| Content revision | Immutable revision identity/body hash, owner, rights/evidence references and review state; drafts remain private. |
| Release candidate | Content snapshot, manifest digest, preparation result and concurrency revision. |
| Review/approval | Authenticated role, exact reviewed snapshot hash, decision and audit time; author cannot approve their own material. |
| Artifact preparation | Expected identity/hash and completion evidence for each render/index/scene derivative. |
| Active release pointer | One release identity/digest plus monotonic activation generation, set only through guarded activation. |
| Publication intent | Durable operation identity, requested transition, known outcome and reconciliation state; no unbounded retry. |

Exact SQL fields/indexes and migrations follow separate reviewed data contracts.
An administrator cannot bypass evidence review or founder approval by changing a
pointer. Break-glass activation does not silently grant publication authority.

## Lifecycle and concurrency

Draft → specialist evidence/SEO review → founder approval → render/index → public
remains the required lifecycle. Content edits invalidate review/approval tied to
the old snapshot. Render jobs use the immutable candidate, not mutable draft rows.

PROPOSED activation preconditions:

1. Every candidate route/content item is approved, with required proof/rights and
   current legal/publication eligibility. No held defense, fictional seed or draft
   can enter HTML, knowledge, sitemap or panels.
2. All seven core derivative kinds (HTML, metadata, structured data, sitemap,
   redirects, knowledge and scene panels) are prepared and verified. Where a
   spatial representation is held, the scene-panel artifact records the truthful
   held state; it does not fabricate an open room or add missing content.
3. Routes and canonical destinations match the active candidate's approved route
   inventory. Coverage spans all four peer streams; semantic paths require no
   scene chunk, collision or audio asset. All declared dependencies resolve.
4. Candidate digest, verified index namespace and exact approval snapshot agree.
   Knowledge queries filter/verify that identity; no shared unversioned index is
   treated as current by default.
5. Activation compares the expected active generation and updates the PostgreSQL
   pointer atomically. A concurrent publish/rollback makes the losing operation
   conflict rather than overwrite newer state. Record intent/outcome durably.

## Public serving and cutover

PROPOSED mechanism: immutable per-release static namespaces with one controlled
routing identity. Prepare the entire new static namespace and release-specific
knowledge before changing public routing. Pin a visitor's document, panel and
knowledge reads to its advertised release identity/digest while that release is
within its permitted drain window; fail closed instead of silently mixing it
with a newer release. Never attach the manifest's own digest into an artifact
whose bytes are included in that same digest: clients receive the envelope via
the serving layer, while artifacts carry the independent release ID.

PostgreSQL pointer and CDN/routing propagation cannot be assumed to be one atomic
transaction. Record a cutover intent, verify routing and serving health, and
reconcile acknowledgement before claiming activation complete. During propagation,
each served view must be internally release-consistent; no mixed pages/panels/AI.
Guarding the PostgreSQL pointer alone does not fence delayed routing writes.
One durable cutover may be outstanding at a time, and its routing generation must
be conditionally enforced at the external effect boundary. Reject stale workers
and stale routing writes, not merely their later database updates. Before allowing
generation N+1, reconcile generation N's effect and prove no late N operation can
replace it. A lease expiry, request timeout or cancellation request is not that
proof. If the provider lacks enforceable conditional generations, the reviewed
adapter must prove equivalent serialization and terminal reconciliation; an
unknown outcome holds subsequent cutovers until resolved. Late acknowledgements
update only their original intent and cannot downgrade a newer routed generation.
Exact routing API, drain duration and purge controls still need dated primary
evidence and recovery tests for the eventually selected provider. Under D-068 and
the [provider scope addendum](PROVIDER_SCOPE_ADDENDUM.md), Azure/AWS hosting
selection and deployment planning remain deferred. This proposal certifies no
provider's mechanism and does not request that selection now.

Urgent content withdrawal overrides draining: suppress invalidated content from
semantic and spatial reads, sitemap and knowledge even for an old pinned session.
Stop serving/answering the withdrawn release if selective safe suppression cannot
be verified. Suppression changes serving eligibility, never immutable artifact
bytes; changed content requires a new release. Retained immutable bytes need not
remain publicly accessible. A
revoked source is not publishable merely because its previous checksum is valid.

## Visitor release refresh and eligibility

PROPOSED refinement of the accepted mid-session release-change branch in
[FLOWS.md](../../phase-1-ux-architecture/FLOWS.md): immutable identity and current
serving eligibility are separate. A valid checksum proves bytes, not permission
to keep serving them. An active pointer change does not authorize the browser to
combine derivatives from two releases or to restart a visitor's private process.
This refinement awaits independent review; prior publication review covers its
recorded hash only. No new endpoint, public-envelope field or timing is selected.

| Situation | Required serving/visitor outcome |
|---|---|
| First document/World load | Resolve an eligible approved release and advertised envelope; keep its HTML, panels, knowledge, scene/collision and enabled audio associations internally consistent. |
| Ordinary newer release available | Preserve the current safe interaction while the pinned release is eligible; announce refresh. Block stale source/action context wherever integrity requires it rather than silently presenting it as current. |
| Safe refresh | Verify a complete eligible target and its dependencies before replacing the content/scene context together. Do not inject a newer panel, answer or collision chunk into the old scene. |
| Pin expired or eligibility unknown | Stop affected reads/travel/answers and offer truthful refresh or an eligible semantic route; cached bytes are not eligibility evidence. No offline continuation promise. |
| Urgent withdrawal | Override the drain window and suppress affected reads/answers. If safe selective suppression is unproven, stop the release's public presentation and offer eligible semantic recovery. |
| Delayed old response after refresh | Discard it from the newer content context using the original release/request identity; do not let an old loader or AI fragment restore withdrawn content. |
| Existing handoff/booking | Preserve its authoritative private lineage and confirmed/pending/unknown state; refresh public context separately. A release refresh cannot duplicate, cancel or confirm the external operation. |

The server enforces release eligibility and current action authorization; the
browser cannot extend its own drain window. Staff availability and booking slots
remain live server decisions even when explanatory content is pinned. New actions
must validate their canonical service/context and ownership against current policy;
a retired service or stale source is not authorized by an old scene panel.
AI answers and citations remain bound to the eligible source context used for the
answer; interruption or withdrawal cannot be repaired by relabelling old text
with a newer release. Conversation resume follows its privacy/expiry contract.

Warm caches, browser history and in-flight responses are part of withdrawal
verification. Do not promise to erase bytes already downloaded to a visitor or
revoke an offline screenshot. The controlled serving layer must prevent new
ineligible reads; the controlled runtime must react to detected withdrawal and
stop if required eligibility cannot be established. Detection/freshness limits,
bounded drain policy, cache purge and provider delivery evidence remain exact
contract/measurement inputs, not guarantees inferred from this table.

## Failure, retry and rollback

Preparation failure leaves the previous valid release active. An unknown routing
or activation acknowledgement stays pending/reconciliation-required; retry must
reuse the operation identity and reconcile provider state first. Missing assets,
release mismatch or index failure expose truthful recovery and approved semantic
help/booking; never invent confirmation, staff presence or source evidence.

Rollback selects a previously approved, complete and still eligible release,
verifies all its derivatives, and uses the same guarded cutover. Revoked rights,
withdrawn legal content or unavailable required assets block rollback to it.
Concurrent rollback/publish is serialized by expected activation generation.

## Required conformance cases

| Case | Evidence required before implementation acceptance |
|---|---|
| Two concurrent publishers / publish versus rollback | One guarded winner, explicit conflict for loser, matching routed release and audit outcome. |
| Source edit after approval | Candidate refuses stale review/approval; no stale candidate activation. |
| Failed render/index or missing required artifact | Prior eligible release remains usable; no mixed derivative/public draft. |
| Cutover timeout or crash | Durable intent and deterministic reconciliation, not presumed success or duplicate cutover. |
| Delayed generation N after N+1 / stale worker / late acknowledgement | External fencing or proven terminal serialization prevents N replacing N+1; ambiguous N prevents a subsequent cutover and late acknowledgement cannot downgrade routing. |
| Warm cache and long-lived World/AI session | Per-view identity remains consistent; withdrawn release fails safely. |
| Mid-visit ordinary refresh / delayed old scene or answer | Safe interaction and private process truth survive; target dependencies are ready before a consistent switch, and old completions cannot populate the new context. |
| Withdrawal while a room or source panel is open / eligibility unavailable | Required content/answer suppression and safe stop; no cached eligibility guess or implicit offline promise. |
| Forged/duplicate schema keys, wrong checksum or traversal | Rejection before lookup/render; no private asset fetch. |
| Rollback with withdrawn rights/content | Refusal until an eligible release is selected. |
| Semantic delivery | Equivalent core routes/content/actions with no WebGL/audio dependency. |

This contract is incomplete for deployment until routing/retention/withdrawal
mechanisms and measured drain limits are verified. Staff/legal facts remain their
existing gates; do not choose a region/provider or promise cutover atomicity here.

Primary format references checked 2026-10-04:
[JSON Schema validation vocabulary](https://json-schema.org/draft/2020-12/json-schema-validation)
and [RFC 8785 JCS](https://www.rfc-editor.org/rfc/rfc8785).
These specify document validation/canonicalization; they do not select a runtime
package version or prove the deployment behavior described above.
