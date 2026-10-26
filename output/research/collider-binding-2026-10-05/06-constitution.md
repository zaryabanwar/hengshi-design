<!--
SYNC IMPACT REPORT
Version normalization: v1.0.0, the first production-definition package.
Reason: Explicit founder instructions 2026-10-04 retain latest mutually compatible
stable technology, normalize current product/definition naming to v1, prioritize
Europe, defer Azure/AWS deployment selection and keep Outlook/Teams without making
Microsoft 365 a prerequisite. This is a founder-directed naming reset; historical
governance revisions do not become product release numbers.

Modified principles:
- I. Product Surfaces Stay Separate -> Product Surfaces Share Published Truth
- II. Platform Vision Is Transformative -> Evidence-Led Platform Positioning
- III. Spec Kit Before Implementation -> Durable Authority Before Implementation
- IV. Design-First UI -> Design-First, Semantic, and Accessible Experience
- V. Latest Compatible Tooling -> Latest Mutually Compatible Stable Technology
- VI. AI Toolchain Order Is Mandatory -> AI, Data, and Trust Boundaries
- VII. Verification Is Mandatory -> Evidence and Independent Review Are Mandatory
- VIII. Approval Gates Are Binding -> Approval Gates and Phase State Are Binding

Added sections:
- Durable authority and conflict resolution
- Technology selection and compatibility exception policy
- Delivery phase and revision governance
- Publication, SEO, AI, privacy, and release constraints

Updated dependent artifacts:
- AGENTS.md
- .github/copilot-instructions.md
- docs/PROJECT_RULES.md
- docs/software-definition/README.md
- docs/software-definition/01-system-boundaries.md
- docs/software-definition/02-ai-dev-tooling-and-mcp.md
- docs/software-definition/03-autonomous-ai-development-workflow.md
- .specify/templates/constitution-template.md
- .specify/templates/plan-template.md
- .specify/templates/spec-template.md
- .specify/templates/tasks-template.md
- .specify/templates/checklist-template.md

Deferred reconciliation:
- Provider/region/SKU/cost and exact Microsoft account/API capabilities remain
  held. Canonical records/templates are synchronized in bounded two-document
  slices; reviewed historical artifacts remain evidence, not current deployment
  or product-release authority. Full Phase 1 acceptance remains separate.
-->

# Hengshi Design Constitution

## Core Principles

### I. Product Surfaces Share Published Truth

Hengshi Design MUST retain two primary deployables: a React-based public and staff
web application, and a modular FastAPI monolith. The public semantic experience,
3D campus, staff tools, API, background jobs, and shared contracts MUST remain
separable by responsibility. All public representations of a release MUST derive
from one approved, immutable publication manifest and checksum. PostgreSQL is the
durable source of truth; Redis, search indexes, caches, generated HTML, and 3D
panels are derived or ephemeral and MUST be rebuildable.

The existing application and exterior GLB are protected prototype evidence. They
MUST NOT be deleted, overwritten, or treated as production design authority. A
replacement Blender master or production experience requires its own approved,
versioned source and provenance.

### II. Evidence-Led Platform Positioning

Hengshi Design is a premium, platform-oriented innovation delivery partner for
mid-market and enterprise buyers, targeting the European market first with global
reach as a broader ambition. This establishes no European office or legal entity.
Public claims MUST be truthful,
substantiated, and attributable. Verified client work and Hengshi-owned capability
demonstrations MUST be separate collections; fictional seeds MUST remain
quarantined. “World-first” is an internal ambition and MUST NOT become a public
claim without independent substantiation and legal approval.

Agriculture is the first launch sector and mining is second. Defense content MUST
remain unpublished and unindexed until founder, independent legal, and security
review approve every claim, demo, dataset, and AI route.

### III. Durable Authority Before Implementation

Material product, architecture, workflow, repository structure, API, auth,
security, infrastructure, data, production UI, 3D, AI, or publication work MUST
start from approved durable artifacts. The required set is `PROJECT.md`,
`PROJECT_STATE.yaml`, `DECISIONS.md`, the software definition, and the relevant
Spec Kit artifacts under `specs/`. When present, read `spec.md`, `research.md`,
`data-model.md`, contracts, `plan.md`, and `tasks.md` before implementation.

No application feature development may begin until the Phase 1 definition, SEO,
design, architecture, security, privacy, QA, deployment, and technology
compatibility package is approved. Missing information may be derived only when
unambiguous, reversible, within approved scope, and recorded as an assumption. A
choice that materially changes scope, risk, cost, public claims, or architecture
requires founder approval.

### IV. Design-First, Semantic, and Accessible Experience

Production UI creation and material UI/UX changes MUST reference an approved
Google Stitch or Figma design before implementation. Brand, UI, motion, sound,
and 3D work follow `create -> validate -> inspect -> independent review -> revise
-> validate again -> founder approval`, with at most three revision cycles.

Every indexable route MUST deliver complete, meaningful semantic HTML before
client JavaScript executes. The responsive Quick Access route MUST provide
equivalent content, navigation, AI or human help, and booking without requiring
WebGL. The product MUST target WCAG 2.2 AA and provide keyboard, reduced-motion,
low-power, asset-failure, and non-WebGL paths. Visual novelty MUST never obstruct
the primary discovery or booking journey.

### V. Latest Mutually Compatible Stable Technology

Production MUST use the newest mutually compatible stable versions across the
approved technology families. “Latest” means officially stable and supported,
compatible with directly coupled frameworks, runtimes, browsers, cloud services,
and deployment targets, covered by official migration guidance, reproducibly
locked, and proven through migration, security, accessibility, visual,
performance, data, and rollback tests. Preview, beta, release-candidate, nightly,
and experimental dependencies MAY be evaluated only in isolated non-production
spikes and MUST NOT become production requirements.

Version selection MUST be evaluated as a compatibility graph, not as isolated
package numbers. Resolve official library identifiers and current guidance through
Context7, confirm releases in primary vendor documentation and package registries,
and record the query date, current and target versions, peer/runtime requirements,
breaking changes, security status, evidence, and rollback. Exact versions MUST be
locked only after the compatibility spike is re-run immediately before the
relevant upgrade wave.

Independently newest registry versions MUST remain unselected observations until
the complete chosen graph is proven compatible. Peer ranges alone are insufficient.
This rule governs all project tools, runtimes, frameworks, libraries, renderers,
asset exporters, databases, browsers and external APIs, not only application code.
The first product and current production-definition package MUST be called v1.
Actual package versions, schema/protocol identifiers and dated historical evidence
MUST remain accurate and MUST NOT be relabeled to fabricate compatibility/history.

If the newest stable major is blocked, select the newest proven-compatible stable
release, record the exact blocker and evidence in an ADR, and schedule a quarterly
recheck. Compatibility exceptions are temporary and require founder approval.

### VI. AI, Data, and Trust Boundaries

AI MUST answer only from approved, versioned evidence, expose sources for
substantive answers, and fail closed with “cannot verify” plus a human or booking
route when evidence is missing. AI MUST NOT bind price, scope, timeline, legal
terms, or delivery commitments. Draft or rejected content MUST NOT reach public
HTML, sitemaps, search notification, retrieval indexes, or AI context.

No visitor accounts or uploads are permitted at launch. Non-consented chat is
ephemeral. Consented chat, brief, and lead data expire after 90 days unless an
approved active-client or legal record policy applies. Verified deletion MUST
remove chat, derived traces, brief, and lead profile. Visitor conversations MUST
NOT train models. PII and confidential conversations use the approved Azure EU
route; NVIDIA adapters initially receive only public or de-identified data.

Staff identity uses Entra SSO with separately enforced author, reviewer, founder
approver, and administrator roles. Two monitored dormant local break-glass
accounts retain bcrypt-backed emergency access under approved MFA, activation,
alerting, and rotation controls. Browser sessions use rotating JWTs in secure,
HttpOnly, SameSite cookies with CSRF protection. Secrets MUST never enter source,
documentation, logs, chat, or generated evidence.

### VII. Evidence and Independent Review Are Mandatory

Every material phase and upgrade wave MUST produce proportionate, repeatable
evidence. Frontend changes require builds, focused tests, Playwright browser
verification, accessibility checks, and visual inspection for affected states.
Backend changes require typing/import checks, contract and integration tests, and
negative authorization coverage. 3D changes require asset, loading, interaction,
color, memory, performance, fallback, and screenshot comparisons. Database and
deployment changes require backup, restore, migration, rollback, and candidate
release evidence.

The producer MUST NOT approve their own material output. Independent reviewers are
required for design, code, accessibility, security, QA, and deployment gates as
applicable. Release evidence MUST include deterministic locks, an SBOM and license
inventory, no unbounded production dependencies, and no unresolved
production-critical deprecation warning.

### VIII. Approval Gates and Phase State Are Binding

All phase work follows:

`create -> validate -> inspect -> independent review -> revise -> validate again -> founder approval`

Permitted phase states are `not_started`, `in_progress`, `blocked`,
`awaiting_human`, `in_review`, and `accepted`. Only founder approval moves a
material phase to `accepted`. Revision limits are two cycles by default and three
for brand, UI, motion, and 3D. Exhausted revisions MUST be recorded as unresolved
findings and presented for a decision instead of silently looping.

No branch, commit, migration, paid-service activation, credential change,
external design write, production promotion, or deployment may occur without its
explicit applicable approval. A blocked integration MUST be recorded in
`MANUAL_ACTIONS.md`; independent work continues when safe and the next action
remains resumable.

## Durable Authority and Conflict Resolution

Project truth is applied in this order:

1. Current explicit founder approval, recorded in `DECISIONS.md` and the detailed
   decision log.
2. This constitution and project safety/governance rules.
3. Approved decisions and compatibility-exception ADRs.
4. Approved product requirements and feature specifications.
5. Approved software-definition and design artifacts.
6. Source code, tests, generated artifacts, and live observations as evidence of
   current implementation behavior.
7. Active-but-unreconciled documents, consolidation files, research, drafts, and
   chat history as supporting evidence only.

Approved decisions outrank approved requirements. Current implementation evidence
cannot silently override approved intent. A material conflict MUST stop the
affected work, be recorded, and be resolved by the founder; unrelated safe work
may continue.

## Technical Standards

- Frontend families: React, React DOM, TypeScript, Vite, TailwindCSS, React
  Router, Zustand, GSAP, React Three Fiber, Drei, and Three.js on the approved
  latest-compatible stable matrix. Tailwind remains required unless the founder
  explicitly approves a change.
- Backend families: stable Python, FastAPI, Starlette, Pydantic, Uvicorn,
  SQLAlchemy, Alembic, Psycopg, JWT, bcrypt, HTTPX, and pytest, exactly locked by
  a deterministic standards-based Python workflow.
- Database: target the current stable PostgreSQL generation. Use PostgreSQL 18's
  current stable minor when it is GA in the eventually approved provider/region; otherwise use
  the newest regionally available GA major under an ADR and quarterly recheck.
- Rendering: WebGL remains the production 3D renderer. WebGPU is an isolated
  experiment until official support and complete parity are stable.
- Architecture: two deployables; deterministic static prerendering for all
  indexable pages; immutable static release storage/routing; PostgreSQL durable
  truth; ephemeral Redis; rebuildable approved search; policy-routed approved AI;
  observability; and GitHub Actions with OIDC/workload identity. Deployment,
  provider/region/SKU and cost planning are deferred by the founder. Azure and AWS
  are candidates, not selected platforms; prioritize lowest feasible cost/free
  services when planning resumes. Earlier Azure service mappings remain historical
  candidates. Approved personal/confidential AI route policy is not silently
  replaced by opening hosting alternatives. No resources or paid activation.
- Integrations: retain Outlook/Teams intent. Microsoft 365 subscription/setup is
  not a prerequisite; verify exact account types, API permissions and entitlement
  for each automated calendar/meeting/presence/notification operation. Free client
  access does not establish every Graph capability. Entra staff identity remains
  approved; no provider/identity replacement is inferred.
- Release: immutable artifacts, production images pinned by digest, GitHub Actions
  pinned by commit SHA, zero-traffic candidate revisions, manual promotion, and
  tested rollback. Production artifacts MUST NOT use `latest` tags.
- Browser support: latest two stable evergreen browser releases with Safari/iOS
  16.4 as the minimum legacy floor; unsupported clients receive the semantic
  Quick Access path.
- Quality: pytest, frontend unit tests, Playwright, axe, Lighthouse, WCAG 2.2 AA,
  contract tests, security review, visual review, performance budgets, and
  rollback evidence as applicable.

## Development Workflow

1. Read `AGENTS.md`, this constitution, and the durable root project records.
2. Read `docs/software-definition/README.md` and the relevant approved feature
   artifacts.
3. Confirm the current phase, task contract, write scope, exclusions, revision
   limit, evidence requirements, and human gate in `PROJECT_STATE.yaml` and
   `TASKS.md`.
4. Resolve version-sensitive decisions through Context7 and official primary
   sources before selecting exact versions.
5. Reference approved Stitch/Figma output before production UI work.
6. Stabilize known fatal baseline defects before modernization; keep upgrade waves
   separate from feature development.
7. Create, validate, inspect, independently review, revise, and validate again.
8. Record decisions, risks, manual actions, evidence, and status before requesting
   founder approval.
9. Perform Git, migration, external-write, paid-service, and deployment actions
   only after their separate approval gates.

## Governance

This v1 constitution supersedes conflicting fixed-version, standalone all-latest,
provider-selection, prototype-readiness or ad hoc implementation claims. Amendments
require a documented rationale, founder approval, and synchronized updates to affected
templates, project rules, software definitions, specs, state, and decision
records.

During this first-development reconciliation, v1 remains the current product and
definition label. Dated decisions and reviewed evidence identify internal changes;
they do not invent subsequent production releases. A later release/versioning policy
requires a real approved release decision. Technical schema/protocol and dependency
versioning retain their own accurate compatibility semantics.

**Version**: 1.0.0 | **Ratified**: 2026-06-24 | **Last Amended**: 2026-10-04
