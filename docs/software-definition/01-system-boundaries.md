# 01 — System Boundaries

## Purpose

This document distinguishes the protected current prototype from the approved
production target and defines the boundaries between product surfaces.

## Current Protected Prototype

The repository currently contains a React/Vite/React Three Fiber web application,
a modular FastAPI/SQLAlchemy API, a PostgreSQL 16 Docker baseline with an unsafe
SQLite runtime fallback, browser/admin flows, seeded content, and an exterior GLB.
These are implementation and recovery evidence. They are not production product,
design, content, security, database, or version authority.

The existing source and exterior GLB MUST remain untouched except through later
approved, reversible implementation tasks. A new versioned Blender source will be
created only after its Phase 1 design, provenance, and production contract is
approved.

## Approved Production Target

### 1. Web application (`apps/web/`)

- **Users**: visitors, buyers, partners, experts, authors, reviewers, founder
  approvers, and administrators.
- **Families**: React, React DOM, TypeScript, Vite, TailwindCSS, React Router,
  Zustand, GSAP, React Three Fiber, Drei, and Three.js on the approved dated
  latest-compatible stable matrix.
- **Responsibilities**: semantic indexable pages, responsive Quick Access,
  progressive WebGL campus, staff/admin experiences, booking, and chat clients.
- **Rendering rule**: every indexable route returns complete semantic HTML before
  JavaScript; WebGL is progressive enhancement, not a conversion dependency.

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
- Target PostgreSQL 18's current stable minor when GA in the approved Azure region;
  otherwise use the newest regional GA major under an ADR and quarterly recheck.
- Azure Managed Redis stores only ephemeral presence, fan-out, locks, rate limits,
  and routing state.
- Azure AI Search stores only approved, versioned knowledge and is rebuildable.
- Generated HTML, manifests, sitemaps, social images, and 3D panels are immutable
  release artifacts derived from approved PostgreSQL publication state.

### 4. Production platform and integrations

- Azure Front Door/WAF and versioned static storage serve public release artifacts.
- Azure Container Apps runs API, WebSockets, admin, render, and job workloads.
- Azure and production-licensed NVIDIA providers sit behind one policy router.
- Microsoft Graph and approved alert adapters support booking and staff workflows.
- Application Insights/Azure Monitor provides approved observability.
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
