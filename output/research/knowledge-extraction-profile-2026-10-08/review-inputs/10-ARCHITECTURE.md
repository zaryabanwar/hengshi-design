# Phase 1 architecture authority and boundaries

Date: 2026-10-04. Producer: root. Status: DOING; proposed decomposition awaiting
independent review and founder acceptance. No application implementation is authorized.

## Authority and scope

This package defines responsibility and evidence boundaries, not production
readiness, deployed resources, exact API schemas or version locks. D-001 through
D-024, Constitution 2.0.0 and the approved software system boundaries govern;
D-025/D-036 govern foundation and journeys, D-039/D-045 govern the four peer
streams, and D-051 through D-063 supply their accepted refinements. Later detailed
contracts must resolve these constraints rather than silently replacing them.

The companion authority map identifies each constraint's local source, proposed
owner, failure invariant and required downstream contract. Current SAD/API/source
files remain prototype evidence. Their SPA-only, fixed-version or AWS assumptions
cannot override semantic HTML, latest-compatible stable families or Azure intent.
No legacy document is deleted or given retroactive production approval.

## Deployment and responsibility boundaries

Retain two primary deployables: the web application at `apps/web/` and the modular
API monolith at `apps/api/`. Generated public releases are artifacts of the web
deployable. API background jobs and render/index workloads may run separately for
operation while sharing the API application and approved contracts; this is not
permission for additional independently designed microservices or repository moves.

| Proposed responsibility | Owns | Must not own |
|---|---|---|
| Web semantic delivery | Complete public HTML, metadata, canonical navigation and equivalent conversion journeys | Publication approval, authoritative booking confirmation or provider credentials |
| Web immersive delivery | Required WebGL peer-stream representations of the same release, visitor-chosen World entry, directed exploration and accepted stream controls | Independent public claims, a separate content database or required canvas conversion |
| Web staff surface | Authoring/review/admin interaction and server-provided permission presentation | Authorization enforcement or direct database/provider access |
| API identity and authorization | Server-enforced staff roles, session and break-glass policy | Public visitor accounts or client-controlled role elevation |
| API publication | Reviewed authoring state, approval, immutable release identity and active-release selection | Public exposure of drafts, unsupported claims or partial releases |
| API conversation and handoff | Approved evidence routing, consent boundary and truthful human availability | Binding commercial/legal promises, model training or invented availability |
| API booking | Approved discovery-booking workflow and integration reconciliation | Confirmation before authoritative provider evidence or AI-controlled commitments |
| API privacy lifecycle | Permitted retention, expiry and verified deletion orchestration | Indefinite retention, undeclared exceptions or deletion claims before verification |
| API integration and audit | Durable external-write intent, idempotency, outcome reconciliation and permitted audit evidence | Unbounded retries, duplicate actions or confidential payloads in general logs |

These are proposed logical responsibilities, not new folder/module names, tables,
API paths or permission grants. Those belong in independently reviewed downstream
interface/data/security contracts before implementation.

## Semantic and immersive reads

Every indexable public route must deliver complete meaningful HTML before client
JavaScript. The active immutable release governs content, metadata, structured
data, canonical routes, sitemaps, redirects, knowledge and immersive panels.
Planned route membership is not release activation: the current 35-route planning
inventory does not grant publication, indexing or legal-copy approval.

Hydration and WebGL add approved interaction. Canvas entry is a visitor choice;
the high, medium, low and semantic peer streams remain core delivery definitions.
JavaScript loss preserves complete initial semantic content and direct Book access;
transaction scripting failure must report unavailable/not completed and offer the
approved retry or verified Contact route. No no-JS transaction completion is
asserted (UXTEST-044). Canvas or asset loss preserves equivalent core journeys
through the semantic peer. Use the accepted four peer streams with their
explicit user control, ceiling, preference/error and recovery rules. No WASD or
free-roam requirement is introduced. Production screens and scene geometry still
require their approved reference and provenance gates.

## Publication consistency and recovery

PostgreSQL is authoritative for authoring, evidence review, founder approval and
durable publication state. A candidate release has one immutable identity and
checksum. Rendered artifacts and versioned search knowledge must be prepared and
verified for that same candidate before public activation. Reads must resolve the
active identity; mixed-release content or knowledge must not be served as current.

A failed candidate render or index keeps the previous approved release active.
Search/AI reads must verify release identity or fail closed with the approved human
or booking route. Release activation, interruption, rollback, concurrent approval,
cache propagation and index cutover need an exact publication contract and fault
tests; this package chooses no SDK operation or distributed-transaction mechanism.
Rollback must restore one previously accepted complete release, not combine old
HTML with new knowledge or silently approve new content.

## Durable, ephemeral and external state

PostgreSQL remains the sole durable application source of truth. Redis holds only
approved ephemeral presence, fan-out, locks, routing and rate-limit state. Search,
HTML, sitemaps and immersive panels are rebuildable release derivatives; none may
become an alternative approval authority. Cache/search loss must not corrupt
durable records, extend consent retention or permit ungrounded AI.

External Graph/booking, alert, render/index and provider writes cross server-side
contracts with durable intent, idempotency and outcome evidence. A missing or
ambiguous provider acknowledgment is not success. The downstream integration
contract must establish provider-supported retry/reconciliation semantics before
any automatic retry can claim safety. Provider errors must not overwrite an
authoritative prior booking or falsely report a confirmed discovery appointment.

## Identity, privacy and AI boundaries

Staff use approved Entra SSO roles separating author, reviewer, founder approver
and administrator. Server authorization applies to API and job execution.
Two dormant monitored local break-glass accounts retain the approved JWT/bcrypt,
MFA, randomly generated 24+ character credentials, controlled activation,
alerting and post-use rotation requirements. Least privilege and layered rate
limits remain mandatory. Secure rotating HttpOnly,
SameSite cookie sessions require CSRF protection; frontend guards are only aids.
This package changes no authentication configuration or credential.

Visitors have no launch accounts or uploads. Non-consented chat is ephemeral;
consented chat, brief and lead data expire after 90 days unless an approved
active-client/legal policy applies. Verified deletion includes derived traces and
lead profiles. Audit/observability cannot provide a hidden retention or training
exception. Analytics remain first-party, cookieless and aggregate-only.
Unknown or sensitive data must fail closed rather than be retained or sent to an
unapproved provider; the approved refusal/human path remains available.
Exact data classes, deletion evidence, backup expiry, lawful disclosure,
consent text and policy ownership remain downstream privacy/legal gates.

AI uses approved versioned evidence, exposes sources for substantive answers and
fails closed when it cannot verify. It cannot bind price, scope, schedule or legal
terms. PII/confidential traffic requires the approved Azure EU route; NVIDIA is
public/de-identified only until its separate entitlement, DPA, residency and
security gates pass. No visitor conversation trains models. Defense remains
unpublished/unindexed pending founder, independent legal and security approval.

## Platform and local operation

The approved production target is Azure Front Door/WAF and versioned static
storage, Container Apps workloads, PostgreSQL, Managed Redis, AI Search and
Monitor/Application Insights, with Graph and policy-routed AI adapters. These are
approved target families, not verified regional availability or provisioned assets.
Exact region, SKU, capacity, cost, API version, DPA and entitlement require dated
primary evidence, compatibility resolution and applicable founder approval.

Native local Node/Python/PostgreSQL operation is the founder's current preference;
Docker is not a prerequisite for definition or local walkthrough. This grants no
runtime upgrade, service repair, data mutation or migration. Local machine state
and credentials remain machine-local. PostgreSQL 18's current stable minor is the
production policy only when GA in the approved region; otherwise the constitution
requires a dated exception and quarterly recheck. No exact version is locked here.

## Release and acceptance evidence

Implementation follows separately reversible stabilization and compatibility
waves after complete Phase 1 acceptance. Future release evidence must include
immutable action SHAs/container digests, OIDC/workload identity, deterministic
locks, SBOM/license review, a zero-traffic candidate, explicit promotion and
tested rollback. Initial approved 99.9% availability, RPO <=24h and RTO <=8h are
targets requiring tested evidence, not present service-level achievements.

The following downstream work remains required: exact API/WebSocket schemas;
publication/data contracts; security/privacy threat and control definitions;
booking/provider reconciliation; QA/fault and restoration strategy; cost/regional
compatibility evidence; approved visual/3D references. None is certified by this
boundary map. Independently review architecture and security/privacy implications
of this package, resolve findings within two producer revisions, then obtain
founder acceptance of this decomposition. That acceptance does not approve the
complete Phase 1 package or authorize implementation, external writes or spending.
