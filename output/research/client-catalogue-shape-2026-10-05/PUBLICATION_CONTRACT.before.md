# Publication and immutable release contract

Status: DOING. Date: 2026-10-04. PROPOSED detailed contract under D-019/D-065,
PUB-001–PUB-006 and DATA-001/DATA-010. No schema migration or application change.

## Review coverage and public read refinement

The [later amendment review](reviews/current-definition-amendments-2026-10-04.md)
covers the visitor-refresh/eligibility refinement at its exact recorded hash.
Those [reviewed bytes](../../../output/research/contract-review-reference-reconciliation-2026-10-04/PUBLICATION_CONTRACT.pre-status.md)
are preserved; this page's later reference updates do not replace that identity.
The [public GET wire proposal](PUBLICATION_READ_HTTP.md) refines existing
IF-PUB-01/02 and has [bounded independent review PASS after revision 1](reviews/publication-read-http-2026-10-04.md).
It reuses the envelope schema and defines public request/error/cache/conditional
behavior. Exact eligibility mechanisms, resource limits, edge handling and
integrated founder acceptance remain held. Neither review proves runtime
enforcement or authorizes application development, publication or deployment.

The 2026-10-05 [semantic preparation engineering proposal](#semantic-preparation-engineering-proposal)
below is outside those earlier review inputs. Its separate
[independent review](reviews/semantic-preparation-v1-2026-10-05.md) records bounded
PASS with no material finding at the [preserved inspected bytes](../../../output/research/semantic-delivery-2026-10-05/PUBLICATION_CONTRACT.reviewed.md).
That verdict covers the proposal and specific dependency restriction, not exact
schemas, the complete compatibility graph or runtime behavior. Its
[preceding contract bytes](../../../output/research/semantic-delivery-2026-10-05/PUBLICATION_CONTRACT.pre-semantic-proposal.md)
are preserved. The new recommendation does not amend the approved publication
lifecycle or give render jobs approval/activation authority.

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

The same definition command now also checks the
[public GET error-body schema](publication-read-error.schema.json) against the
reviewed [wire proposal](PUBLICATION_READ_HTTP.md). Its
[separate schema/fixture review](reviews/publication-read-error-schema-2026-10-04.md)
covers the expanded test source at the listed hash. The
[original envelope-only test bytes](../../../output/research/contract-review-reference-reconciliation-2026-10-04/test_publication_manifest_schema.reviewed-original.py)
were mechanically reconstructed from the extension and verified against the
original publication review's exact hash. That earlier receipt remains historical
evidence for those original bytes, not coverage of the new error checks. Body
validation cannot prove HTTP status/headers, safe parsing, serving eligibility,
withdrawal, authorization or recovery behavior; actual boundary tests remain held.

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
This refinement has the bounded amendment review identified above; the original
publication review covers its earlier recorded hash only. No new endpoint,
public-envelope field or timing is selected. The separate GET wire proposal
refines transport behavior without selecting a drain or detection limit.

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

## Semantic preparation engineering proposal

PROPOSED 2026-10-05 under the founder's engineering/reconciliation direction and
existing semantic/publication requirements. Retain the web application and modular
API boundaries; compilation is a preparation job, not a third deployed web service.
No application code, build command, dependency or worker is installed here.

Recommendation: evaluate build-time rendering with React Router's data-router
APIs, React DOM's hydratable server renderer and a Vite client/server build.
Use the existing framework APIs for matching/loading/rendering and keep the
project adapter limited to approved-snapshot input, route enumeration, artifact
assembly and result verification. This is not a second content or routing engine.

The first evaluated alternative was Router framework-mode prerendering. It can
emit route HTML/data without a deployed rendering server; a plain SPA fallback
does not supply complete child-page HTML. Its observed `@react-router/dev` 8.4.0
candidate requires Babel `^7.29.7`. The only currently published stable Babel
candidate in that range declares gensync `^1.0.0-beta.2`; no published stable
gensync satisfies it. The [dated registry and semver observations](../../../output/research/semantic-delivery-2026-10-05/registry-observations.json)
record that restriction. Under D-069 it cannot be a selected production path now.
Optional Wrangler, RSC and serve peers do not select a provider or experimental
rendering. Runtime-only Router avoids this specific dev-package dependency, but
that observation is not proof of its whole stable/secure/licensed graph.

Before selecting either mechanism, resolve the complete coupled graph, validate
actual builds/hydration and release-pinned navigation, review and lock it. Recheck
the framework path if its restriction changes. No older version exception, beta
waiver or automatic fallback selection is made by this proposal.

### Preparation from one approved input

1. Publication supplies the exact approved immutable content snapshot, eligible
   canonical route set and required derivative plan. Project only allowed public
   fields for the renderer; private review identities, draft rows, conversations,
   booking proofs and provider configuration never enter its output or loader data.
2. The web build supplies fixed renderer/client code and recorded compatible
   toolchain/configuration identities. Isolate candidate contexts; concurrent
   preparation must not read a mutable global candidate or another job's data.
3. Enumerate approved concrete paths, including approved dynamic content slugs,
   from that candidate. A source-code route, generic SPA wildcard or the planning
   inventory alone cannot publish a held page. Redirects and excluded paths use
   their approved definitions rather than being rendered as indexable successes.
4. Load each route from the supplied candidate projection and await its essential
   content before rendering. Handle redirects/errors as their intended outcomes;
   never accept a Suspense/loading placeholder or error body as the complete page.
   Hydratable rendering must be used for pages requiring React interaction;
   `renderToStaticMarkup` output cannot be hydrated.
5. Produce complete initial HTML, matching metadata/structured data and deterministic
   public hydration/loader data. Browser capability/preference detection follows
   hydration without replacing essential content or automatically entering World.
   Keep browser-only WebGL/audio initialization out of build execution. Book/Contact
   access remains visible before script; transaction completion retains UXTEST-044.
6. Assemble CSS/JS and public loader data as declared immutable dependencies.
   Code/asset preload must not eagerly fetch optional World models/audio before
   their accepted entry/activation conditions. Client-side route loading must
   retain the eligible release identity; unversioned `.data` reads or a fallback
   to mutable current content cannot mix a newer page into an older context.
7. Derive sitemap, redirects, knowledge and scene-panel content from the same
   snapshot. Apply the existing seven-kind completeness/eligibility checks and
   canonical service bindings. A held department's derivative truthfully records
   its state; geometry or generation success cannot open it.
8. Verify exact final artifact bytes, route/dependency coverage and source linkage
   before calculating the manifest digest. HTML carries the independent release
   ID, not its manifest's self-referential digest. Preparation results report
   artifacts/errors to the private publication workflow; they cannot set the
   active pointer, approve content or claim successful public cutover.

### Private preparation message and acceptance proposal

PROPOSED 2026-10-05: the [closed private message schema](publication-preparation.schema.json)
refines the preceding preparation boundary. It is new material outside the
semantic-engineering review's inputs. Its separate
[independent message review](reviews/preparation-message-v1-2026-10-05.md) records
bounded PASS for the proposal/schema tooling at the
[preserved inspected contract bytes](../../../output/research/preparation-message-2026-10-05/PUBLICATION_CONTRACT.reviewed.md)
and listed schema/test hashes. It does not establish coordinator/worker runtime
behavior, current authority or activation enforcement.
No public endpoint, transport, queue, table, worker entitlement or deployment is
selected. The existing public envelope remains the public format authority.

| Message | Required meaning | Authority limit |
|---|---|---|
| `prepare` | One publisher-admitted immutable candidate, public projection key, concrete route plan, complete derivative plan and fixed build/limits identities | Not a content approval, arbitrary code/configuration instruction or visitor request. |
| `prepared` | A worker's proposed complete envelope for the same admitted attempt and binding | Not verified readiness, permission to activate, public cutover or trusted bytes merely because a hash was supplied. |
| `failed` | A closed failure code, optionally naming a planned artifact | No partial success envelope, raw exception, arbitrary diagnostic text or worker-granted retry permission. |

The private `preparation_id`, `attempt_id` and `candidate_id` use the logical data
contract's server-assigned UUID form; identifiers are selectors, not capabilities.
One preparation binds candidate ID/revision, public release ID and supplied UTC
release time, public snapshot digest, route/derivative plan digests, renderer and
client build digests, reproducible toolchain lock, render configuration and limits
profile digests. A changed binding requires a new preparation identity; a retry
with unchanged input uses a new attempt ID and strictly increasing admitted
generation. No wraparound, reset, arbitrary worker generation or UUID assumption
provides admission. Positive numeric revisions must fit the schema's exact
safe-integer range; no lossy coercion is permitted.

`route_plan_sha256` and `derivative_plan_sha256` cover RFC 8785 canonical bytes of
the exact ordered `routes` and `expected_artifacts` arrays. The snapshot digest
covers the canonical public projection, not private approval records or mutable
authoring rows. Renderer/client/configuration/lock/limits digests resolve only to
publisher-allowlisted immutable inputs; they cannot authorize loading arbitrary
code, reading secrets or performing external side effects. Relative snapshot
and output keys must resolve inside the admitted preparation namespace and pass
the existing traversal/key checks; no filesystem path or external URL is accepted.

Before work, the coordinator verifies current principal/job authority, exact
candidate approval and eligibility, all binding/input hashes, route content
revisions and complete derivative plan. Plans require unique artifact IDs/keys,
unique route identities/paths, all seven core kinds, valid dependency graphs and
the approved four-stream coverage. The fixed client build contributes its exact
CSS/JS/data dependencies to this plan. A generic route pattern or a compiler-
discovered extra route cannot silently enlarge the approved candidate.

Bind each admitted attempt to an isolated output namespace. A retry must not
overwrite another attempt's bytes or let a delayed writer alter verified output.
Preparation may write private staged artifacts under its admitted scope; it has
no public serving/active-pointer, content approval, booking, model or Graph power.
Keep authorization out of serialized public data and machine-local credentials
out of all job messages. Workers receive only the permitted content projection,
not the private workflow records needed by the coordinator's authority checks.
Exact worker identity, lease/fencing, process isolation and storage enforcement
remain reviewed mechanism inputs; the schema implements none of them.

On receiving `prepared`, the coordinator must authenticate the result origin and
recheck current attempt/generation, binding, candidate approval/eligibility and
permitted receipt scope. It independently verifies final stored bytes/checksums,
exact plan membership/dependencies, source/route coverage, public-field exclusion,
complete semantic content and matching envelope release/snapshot/routes/time.
It recomputes the manifest digest using the existing canonicalization contract;
neither an echoed binding nor a worker's envelope establishes that agreement.
Acceptance is guarded against concurrent cancellation, revocation or a newer
attempt/candidate. The later activation step separately rechecks its existing
publication preconditions and active generation. No result callback can update
the active pointer directly.

An exact duplicate result cannot create a second verified effect. Same-attempt
conflicting bytes, an unknown origin, stale generation or changed binding is
rejected and handled under the private integrity/reconciliation policy, never
silently overwritten. Cancellation, withdrawal, lost authority, resource limits,
partial writes and interrupted workers leave that attempt unverified and cannot
activate its output. A missing result is not proof that a worker stopped; fence
or prove termination before conflicting follow-up work. Retrying/cleanup and
retention require authorized coordinator policy; no unbounded retry, automatic
deletion or new retention period follows from a worker failure code. Preserve
the previous eligible release and truthful recovery under the existing contract.

The schema reuses the public envelope's identifier/key/hash/route/artifact shapes;
load reviewed schema resources from a fixed local registry without arbitrary
network retrieval. UUID and date-time formats must be enforced. Strict JSON
acceptance must reject duplicate properties, invalid Unicode and numeric values
not exactly representable by the canonicalization profile before validation or
hashing. Shape validation cannot prove the cross-message comparisons, current
authority, bytes, source disclosure, complete graphs, resource limits or safety
described above. Budget values, job timeouts/concurrency, diagnostic retention and
physical transaction/worker controls remain non-selected implementation inputs.

After authorization, exercise actual coordinator/worker/activation boundaries
with modified inputs, replayed/conflicting/stale results, partial writes, missing
dependencies, concurrent cancellation/withdrawal and interrupted/late workers.
Schema fixtures test only the closed messages and validator. This does not expand
the earlier semantic review or claim runtime tests were executed.

Definition check: `python scripts/validation/test_publication_preparation_schema.py`.
Four focused shape-test methods pass with locally registered schema resources.
The affected publication envelope/error and private-message checks pass together
under `python -m unittest discover -s scripts/validation -p 'test_publication*_schema.py'`.
These results and the independent probes are schema-tooling evidence only; they
do not exercise a running coordinator, worker, storage or activation boundary.

Primary schema/tool guidance checked 2026-10-05: Context7
`/python-jsonschema/jsonschema`, [JSON Schema validation](https://json-schema.org/draft/2020-12/json-schema-validation),
[local registry resolution](https://python-jsonschema.readthedocs.io/en/stable/referencing/)
and [format enforcement](https://python-jsonschema.readthedocs.io/en/stable/validate/).
Current official docs/Context7 main-branch examples inform the pattern, not a
production version selection. Installed definition tooling `jsonschema` 4.23.0
and `referencing` 0.37.0 expose the required registry API and reject invalid UUID
and calendar examples; the complete production graph remains unselected.

### Determinism, injection and serving boundaries

Freeze public locale, content revisions and supplied publication timestamps;
randomness, wall-clock reads or live availability cannot change compiled public
content. A live availability/booking panel obtains current state separately and
starts without an unverified live claim. Initial client markup/data must match
the generated tree; hydration warnings are defects, not routinely suppressed.

Treat reviewed authoring content as untrusted at rendering boundaries. Typed
fields, safe text/URL handling, approved rich-text sanitization and safe serialized
data/JSON-LD prevent script or markup injection. Do not embed private loader data,
secrets or raw exceptions in HTML, source maps or build logs. Verify generated
scripts/data against the reviewed CSP and exact-byte integrity policy; injecting
a fresh nonce into stored HTML cannot silently change an artifact whose hash
claims unchanged bytes. CSP/serialization details require security review.

Prerendering does not enforce serving eligibility, headers, access control or
withdrawal. The existing controlled serving/cutover contract still gates reads of
HTML, assets and any navigation data. Staff routes remain non-indexable and cannot
serialize private staff/process data into a public prerender bundle. Private
interactive screens enforce current API permissions after authorized sign-in.

### Implementation evidence required

After authorized implementation, inspect actual generated HTML for every eligible
indexable path with JavaScript disabled, then hydrate and navigate using the same
release. Check visible content/metadata/structured-data parity, direct Book access,
escaping/private-field exclusion and absence of unintended World/audio fetches.
Exercise delayed loaders, held routes, concurrent candidates, missing dependencies,
hydration mismatches, newer/withdrawn releases and failed preparation at the actual
render/publication boundary. A successful example build or schema fixture cannot
prove the whole publication or recovery system.

The private message proposal above now supplies reviewed closed shapes and
acceptance obligations. Exact process/storage isolation, serialization/CSP,
release-pinned navigation, resource limits and the complete stable toolchain
remain reviewed spike inputs.
This proposal defines the engineering route without claiming those tests ran or
accepting the unfinished Phase 1 package.

Primary guidance checked 2026-10-05: Context7 `/websites/reactrouter` and
`/vitejs/vite`; [Router data-mode rendering](https://reactrouter.com/start/data/custom),
[framework prerendering](https://reactrouter.com/how-to/pre-rendering),
[Vite production SSR builds](https://vite.dev/guide/ssr),
[React hydration](https://react.dev/reference/react-dom/client/hydrateRoot) and
[non-hydratable static output](https://react.dev/reference/react-dom/server/renderToStaticMarkup).
Context7's Vite results include main-branch references; they inform the build
pattern, not permission to select unreleased APIs. Registry observations are
dated candidate evidence, not tested production versions.

Primary format references checked 2026-10-04:
[JSON Schema validation vocabulary](https://json-schema.org/draft/2020-12/json-schema-validation)
and [RFC 8785 JCS](https://www.rfc-editor.org/rfc/rfc8785).
These specify document validation/canonicalization; they do not select a runtime
package version or prove the deployment behavior described above.

## Client build identity and registered entry proposal

PROPOSED 2026-10-05 under the existing immutable publication/preparation boundary.
The separate [independent review](reviews/scene-bootstrap-v1-2026-10-05.md)
records bounded PASS at the [preserved inspected contract](../../../output/research/scene-bootstrap-2026-10-05/00-PUBLICATION_CONTRACT.md)
and paired scene-contract hash. These later receipt-reference edits are outside
those exact inspected inputs; no runtime or catalogue encoding is accepted.
The private preparation binding and the public visual resource map already name
`client_build_sha256`; their earlier reviews do not cover this new refinement.
This section assigns its proposed meaning and registration obligations. It adds
no public-envelope field, artifact kind, API, executable permission or active
publication. Exact catalogue/HTML-binding encoding, selected toolchain and actual
compiler/serving/browser enforcement remain inputs for separate review/acceptance.

Recommend `client_build_sha256` identify SHA-256 of RFC 8785 canonical UTF-8 bytes
of a closed, independently compiled v1 client catalogue. It records build-relative
unit identities, actual final-byte digests/lengths, MIME/role, required static
dependencies, optional entry relationships, fixed interpretation-profile registry
and required decoder identities. The exact schema and finite bounds remain held;
this is a logical record obligation, not a new accepted public format. Catalogue
bytes and its referenced units are generated from the fixed build, not editable
company/scene content. Private jobs, identities, secrets, source filesystem paths,
machine settings, claims or visitor data cannot enter the public catalogue.
Store the catalogue artifact as exactly those canonical bytes, without pretty
printing or a trailing newline, so its raw-byte manifest digest equals the build
identity. A different serialization must not be relabelled with that identity.

The catalogue identifies actual emitted JS/CSS and required runtime assets, not
a Git commit, source hash, short bundler filename suffix or package peer range.
Canonicalize its metadata with the existing reviewed JCS obligations; each unit's
digest still covers its raw immutable bytes. A Vite build manifest is useful build
input for static/dynamic import discovery; it is neither this trusted catalogue
nor the public publication envelope. Inspect actual emitted imports and resources,
including transitive static edges and lazy-entry dependencies, before registration.
Do not infer complete coverage or integrity from a bundler's filename convention.

Build the code, registry and catalogue before release-specific HTML/scene assembly.
The catalogue cannot contain its own digest, generated publication/HTML bytes,
release ID, scene/resource-map identities or any containing release-manifest hash.
Its unit inventory must likewise exclude generated catalogue/binding artifacts:
code must not embed the digest of a catalogue that hashes that same code. Immutable
HTML may carry the already-computed build digest through a separately reviewed
closed public binding and serializer; its bytes then become release artifacts.
No self-identifying code rewrite, recursive hash or mutable build sidecar is allowed.

The publisher registers the catalogue against allowlisted immutable build inputs,
reproducible stable toolchain/configuration, exact emitted units, compiled profile
registry, provenance/licences, resource permissions and the proposed preparation
binding. Registration is a private controlled operation, not a public API or
content-author action. Revalidate current authority at preparation and result
acceptance; an earlier registered hash grants neither content approval, serving
eligibility, budget waiver nor permission to activate a release. A changed build,
profile, decoder byte or configuration needs a new build/preparation identity.

Recommend reserved relative artifact keys within each release namespace:

| Key | Required record and role |
|---|---|
| `client/build.json` | Exactly one `shared_asset`, with all four stream associations, containing the registered canonical client catalogue. Its manifest `sha256` must equal the admitted `client_build_sha256`; its byte length must match. |
| `world/descriptors/S-HIGH.json` | Exactly one `shared_asset` for `S-HIGH`, containing that release's high-stream scene descriptor. |
| `world/descriptors/S-MEDIUM.json` | Exactly one `shared_asset` for `S-MEDIUM`, containing that release's medium-stream scene descriptor. |
| `world/descriptors/S-LOW.json` | Exactly one `shared_asset` for `S-LOW`, containing that release's low-stream scene descriptor. |

These are proposed storage-key conventions, not HTTP endpoints or real generated
files. Their first-production v1 convention is fixed in trusted compiler/client
code. All three descriptor records are required for the full approved World
coverage; no partially missing stream is silently treated as an approved smaller
product. Only `client/build.json` participates in semantic bootstrap; semantic
HTML has no scene descriptor/model/collision/audio dependency. The catalogue may
index lazy code/resources without requiring their transfer or execution at page load.

The publication compiler owns these reserved keys and artifact IDs. Content authors,
AI projections and geometry exporters cannot overwrite them or add a competing
entry. Validate uniqueness of every artifact ID/key, exact kinds/streams, complete
planned entry coverage and catalogue-to-emitted-unit/dependency agreement before
accepting prepared output. Registered code identities must agree with same-release
manifest records and their bytes; release wrappers may associate those units with
the independent release without changing compiled code/catalogue bytes.

Required resource dependencies and optional-entry indexing remain distinct. All
genuine resources needed by a requested unit belong to its resolved required
closure; lazy World entry and audio activation cannot be reclassified as semantic
prerequisites merely because the catalogue lists them. Inspect generated HTML,
preloads, imports, service workers and cache/prefetch behavior against those gates.
The catalogue is metadata and cannot supply executable URLs or imports at runtime.
Only trusted compiled entry logic and reviewed serving/security association can
select code. No CSP keyword, module-integrity mechanism or hosting origin is chosen
by this proposal; those exact mechanisms still require their own browser evidence.

Use [scene lookup](../../phase-1-3d/SCENE_ASSEMBLY_CONTRACT.md#scene-lookup-and-build-agreement-proposal)
for the World consumer. Existing public GET eligibility, no-store/precondition
rules, controlled artifact serving and withdrawal retain authority. Actual
compiler/browser tests must reject reserved-key collisions, missing/wrong-stream
entries, forged catalogues, omitted imports, code/profile/catalogue disagreement,
self-hash cycles and delayed mismatched-build completion. Verify semantic first
load without World/audio transfer, and deliberate entry without eager campus fetch.
No such runtime or catalogue-shape test was run for this logical proposal.

Primary guidance checked 2026-10-05: Context7 `/vitejs/vite`, official
[Vite backend integration](https://vite.dev/guide/backend-integration.html) and
[production build guidance](https://vite.dev/guide/build.html) describe build-file
and static/dynamic-import relationships and lazy-load failure mechanics.
[RFC 8785](https://www.rfc-editor.org/rfc/rfc8785) supplies canonicalization, not
registration, code trust or publication authorization. Context7 main-branch
examples inform the pattern only; no preview API, package version or build config
is selected. Reserved keys and the independent catalogue are Hengshi proposals.
