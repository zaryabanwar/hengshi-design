# 01 — System Boundaries — v1

## Purpose

This document distinguishes the protected current prototype from the approved
production target and defines the boundaries between product surfaces.

## Current Protected Prototype

The repository currently contains a React/Vite/React Three Fiber web application,
a modular FastAPI/SQLAlchemy API, a PostgreSQL 16 Docker baseline with an unsafe
SQLite runtime fallback, browser/admin flows, seeded content, and an exterior GLB.
These are implementation and recovery evidence. They are not production product,
design, content, security, database, or version authority.

That Docker baseline is repository evidence, not a local setup requirement. The
[native operating guide](../../README.md#native-local-operation-on-windows)
records the separate Docker-free prototype setup and dated PostgreSQL 17
observations; those observations do not establish continuing service health.

The existing source and exterior GLB MUST remain untouched except through later
approved, reversible implementation tasks. A new versioned Blender source will be
created only after its Phase 1 design, provenance, and production contract is
approved.

## Visitor experience and current amendments

The visitor lands on a complete semantic website and explicitly chooses Enter
World. The four core peer streams carry equivalent information and actions:
three WebGL detail levels and the semantic Quick Access stream. Stream selection
and entry remain separate under the accepted capability, preference and override
rules. No visitor account, WebGL or sound is required to browse or book.

D-064 adds mouse/touch free steering and walking alongside destinations, with
nearby loading and reversal recovery. D-066/D-067/D-071 select an original,
nature-integrated reception and five-wing campus and accept the final-third layout
basis. Department boards, grounded AI, genuine staff availability, consented
handoff and booking use the same eligible content and authoritative API. Optional
sound starts off and follows the accepted context/control rules. See the
[World definition](../phase-1-3d/WORLD_EXPERIENCE.md) for proposed mechanics and
the [visual walkthrough](definition-walkthrough.html) for the intended journey.
These approved scope amendments retain D-065's component boundaries; detailed
appearance, mechanisms and integrated Phase 1 acceptance remain pending.

## Approved Production Target

### 1. Web application (`apps/web/`)

- **Users**: visitors, buyers, partners, experts, authors, reviewers, founder
  approvers, and administrators.
- **Families**: React, React DOM, TypeScript, Vite, TailwindCSS, React Router,
  Zustand, GSAP, React Three Fiber, Drei, and Three.js on the approved dated
  latest-compatible stable matrix.
- **Responsibilities**: semantic indexable pages, responsive Quick Access,
  the three WebGL peer-stream campus representations, staff/admin experiences,
  booking, and chat clients.
- **Rendering rule**: every indexable route returns complete semantic HTML before
  JavaScript; the four streams are core delivery obligations and explicit World
  entry remains separate. WebGL is not a conversion dependency.

### 2. Modular API monolith (`apps/api/`)

- **Users**: web clients, approved staff, jobs, rendering, and integrations.
- **Families**: stable Python, FastAPI, Starlette, Pydantic, Uvicorn, SQLAlchemy,
  Alembic, Psycopg, JWT, bcrypt, HTTPX, and pytest on the approved compatibility
  matrix.
- **Responsibilities**: public APIs, publication workflow, identity/authorization,
  leads, chat/handoff, booking, provider routing, audit/outbox, and administration.
- **Rule**: retain one modular monolith unless a later approved ADR proves a
  different boundary is necessary.

### 3. Durable and derived data

- PostgreSQL is the sole durable application source of truth.
- Target PostgreSQL 18's current stable minor when GA in the eventual approved provider/region;
  otherwise use the newest regional GA major under an ADR and quarterly recheck.
- Redis stores only ephemeral presence, fan-out, locks, rate limits,
  and routing state.
- Search stores only approved, versioned knowledge and is rebuildable.
- Generated HTML, manifests, sitemaps, social images, and 3D panels are immutable
  release artifacts derived from approved PostgreSQL publication state.

### 4. Production platform and integrations

- Edge/WAF and versioned static storage serve public release artifacts; API,
  WebSockets, admin, render and jobs retain the accepted responsibility boundaries.
- D-068 defers hosting/provider/region/SKU/cost selection. Azure and AWS are
  candidates, with lowest feasible cost/free services preferred when planning
  resumes. Earlier Azure service mappings are historical candidates, not selected
  deployment requirements. The frozen D-065 authority map remains unchanged.
- Approved AI privacy routes remain in force: deployment deferral does not
  authorize moving personal/confidential inputs to a different provider.
- Outlook/Teams and approved alert adapters remain intended for booking/staff
  workflows without a Microsoft 365 prerequisite. Exact Graph/account capabilities
  and recovery contracts still require proof before an adapter is selected.
- Observability must satisfy the approved privacy and recovery boundaries;
  provider-specific services are deferred with deployment selection.
- GitHub Actions uses OIDC/workload identity, immutable action SHAs, and immutable
  container digests.

## Shared Publication Contract

One approved immutable publication release MUST drive responsive pages, metadata,
structured data, sitemaps, redirects, search knowledge, and 3D panels. Public
reads never expose drafts or mutable authoring state. A failed render or index
operation leaves the previous release active.

## Boundary Rules

1. The web application never accesses PostgreSQL, Redis, search, Graph, or model
   providers directly; all access crosses approved API contracts.
2. Authorization is enforced server-side. Frontend guards are navigation aids, not
   security boundaries.
3. Redis and search loss must not corrupt durable state or permit ungrounded AI.
4. Every asynchronous external write uses idempotency, audit evidence, and a
   durable outbox or equivalent approved recovery contract.
5. Shared types belong in a shared package only when multiple surfaces consume the
   same approved contract.
6. WebGL is the production 3D renderer. WebGPU remains an isolated experiment
   until stable support and full parity are independently verified.
7. Exact versions are selected in the dated compatibility matrix immediately
   before an upgrade wave and are then locked reproducibly.
