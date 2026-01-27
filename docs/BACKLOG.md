# Hengshi Design - Backlog (MVP)

Status summary:
- Prompt 1 complete (monorepo scaffold + shared package + docs)
- Prompt 2 complete (DB foundation + Alembic + tests)
- Prompt 3 next (JWT auth)

Service taxonomy (v1 - 2026) locked in SPEC.md; changes require updating shared schema.

## Completed (Prompt 1-2)
### Story 0.1 - Monorepo scaffold (DONE)
- AC:
  - apps/web and apps/api created
  - docker-compose Postgres working
  - README has run steps

### Story 0.2 - Shared typing (DONE)
- AC:
  - packages/shared exports zod schemas + TS types for core models

### Story 1.1 - API skeleton + health (DONE)
- AC:
  - GET /health -> {status: "ok"}

### Story 1.2 - Postgres + SQLAlchemy + Alembic (DONE)
- AC:
  - SQLAlchemy 2.0 base/session wired
  - Alembic configured and reads DATABASE_URL
  - init migration present (apps/api/alembic/versions/7310fda60e45_init.py)
  - migrations run from a clean DB

### Story 4.1 - Web app scaffold (DONE)
- AC:
  - React + Vite + TS + Tailwind configured
  - Routing works
  - Zustand store set up

---

## Next (Prompt 3)
### Story 1.3 - Auth (admin)
- AC:
  - POST /api/auth/login returns JWT
  - GET /api/admin/me works with token

---

## Upcoming

### EPIC 2 - Content Models + CRUD
#### Story 2.1 - Services CRUD
- AC:
  - admin CRUD endpoints + DB migrations
  - public list/detail endpoints
  - Backend Service model MUST validate against packages/shared ServiceCreate/ServiceUpdate schemas.
  - Seed initial services based on Service taxonomy (v1 - 2026) with at least 1 featured service per category.
  - Frontend uses ServiceCategory for filtering and room panels.

#### Story 2.2 - Projects CRUD + Media
- AC:
  - project list/detail
  - project_media table

#### Story 2.3 - Leads
- AC:
  - POST /api/leads saves to DB
  - GET /api/admin/leads returns list

---

### EPIC 3 - World System (Data-driven 3D)
#### Story 3.1 - World schema + seed
- AC:
  - world_nodes, world_hotspots tables + seed script

#### Story 3.2 - Public world endpoint
- AC:
  - GET /api/world returns nodes + hotspots

#### Story 3.3 - Admin world CRUD
- AC:
  - CRUD nodes/hotspots

---

### EPIC 4 - Frontend Foundation (React)
#### Story 4.2 - API client
- AC:
  - typed fetch client with base URL env var
  - handles auth token for admin

---

### EPIC 5 - Immersive Engine (R3F)
#### Story 5.1 - SceneRoot + CameraController
- AC:
  - renders base scene
  - transitionTo(nodeId) moves camera

#### Story 5.2 - NodeManager (world nodes)
- AC:
  - loads node camera settings from /api/world
  - switching nodes uses GSAP timeline

#### Story 5.3 - HotspotSystem
- AC:
  - renders hotspots from API
  - hover + click triggers panel

---

### EPIC 6 - UI Overlay
#### Story 6.1 - Navigation
- AC:
  - Index / Projects / Contact nav
  - route change triggers scene transition

#### Story 6.2 - Panels
- AC:
  - ServicePanel
  - ProjectPanel
  - ContactPanel with lead submit

---

### EPIC 7 - Admin UI
#### Story 7.1 - Admin Login
- AC:
  - login form, token stored securely
  - protected routes

#### Story 7.2 - Admin CRUD screens
- AC:
  - list/create/edit Services
  - list/create/edit Projects
  - edit world nodes/hotspots

---

### EPIC 8 - Deployment (AWS)
#### Story 8.1 - Build and deploy web
- AC:
  - static build output deployable to S3 + CloudFront

#### Story 8.2 - Deploy API
- AC:
  - dockerized api deployable (ECS or EC2)
  - env vars documented
