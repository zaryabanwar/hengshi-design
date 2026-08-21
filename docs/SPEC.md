# Hengshi Design - Immersive Web Platform Spec (MVP)

**Version:** 2.0 | **Date:** February 9, 2026 | **Status:** Active

---

## Implementation Status

### Completed (Prompts 1–11)
- Monorepo scaffold (apps/web, apps/api, packages/shared, docs/)
- FastAPI + PostgreSQL + SQLAlchemy 2.0 + Alembic (7 migrations)
- Admin JWT authentication (login, seed admin script)
- Services CRUD (model, schemas, routes, seed data — 9 categories)
- Projects CRUD with media attachments (cascade delete)
- Leads module (rate-limited POST, admin listing)
- World system (WorldNode + WorldHotspot models, endpoints, seed data)
- Web app routing + Zustand stores + API client
- R3F engine (SceneRoot, CameraController, GSAP transitions)
- Hotspot system + panels (services/projects/contact)
- Admin UI + CRUD screens (login, protected routes, JSON editors)
- Exterior scene + drone intro (GLB model, GSAP drone path — needs spatial alignment)

### Not Yet Implemented
- Security hardening (Sprint 1 — login rate limiting, CORS, httpOnly cookies)
- Testing expansion (Sprint 2 — frontend tests, backend error paths)
- Monitoring/logging (Sprint 2 — Sentry, structlog)
- Lobby + room scenes (Sprint 3 — placeholder geometry, room template)
- Category 10: Creative & Visual Design (Sprint 4 — seed data, room node)
- S3 media upload (Sprint 4 — presigned URLs)
- CI/CD pipeline (Sprint 5 — GitHub Actions)
- AWS deployment (Sprint 5 — S3/CloudFront/ECS)

---

## Purpose

Build an immersive WebGL website for hengshidesign.com: a 3D virtual building where each room represents a service category. Visitors navigate between rooms via smooth camera transitions and interact with hotspots that open content panels (projects, services, contact). Backend supports a CMS for managing content and world configuration.

## Goals (MVP)
- Immersive 3D world (building) with camera transitions between scene nodes (rooms).
- Hotspots in rooms open overlay panels for Services, Projects, and Contact.
- Projects page with filtering and project detail panel.
- Contact flow saves leads to DB with rate limiting.
- Admin login + CRUD for Projects, Services, World nodes/hotspots, and Leads.
- Media upload to S3 via presigned URLs (Sprint 4).

## Non-goals (MVP)
- Full FPS movement / collision walking.
- Payments / billing.
- Chat / real-time.
- Multi-tenant.
- AI features.
- IoT device management.

---

## Tech Stack

### Implemented
- **Frontend:** React 18 + TypeScript, Vite, TailwindCSS, React Router v6, Zustand
- **3D Engine:** React Three Fiber (@react-three/fiber + drei), GSAP, Three.js (via R3F)
- **Backend:** FastAPI (Python 3.11+), SQLAlchemy 2.0, Alembic, PostgreSQL 16
- **Auth:** JWT (PyJWT) + bcrypt password hashing
- **Infrastructure:** Docker Compose (local PostgreSQL)

### Planned Additions
- slowapi (login rate limiting) — Sprint 1
- Redis (distributed rate limiting, session cache) — Sprint 2
- Sentry (error tracking) + structlog (structured logging) — Sprint 1–2
- Vitest + React Testing Library (frontend tests) — Sprint 2
- GitHub Actions (CI/CD) — Sprint 5
- AWS S3 + CloudFront (static assets, CDN) — Sprint 4–5
- AWS ECS/EC2 (API deployment) — Sprint 5

---

## Service Taxonomy v2.0 (2026)

10 categories, each mapping 1:1 to a world room node.

### CATEGORY 1 — Strategy & Architecture
- Digital transformation strategy & roadmaps
- Technical discovery workshops (product/tech)
- Solution architecture & system design
- Platform selection & vendor evaluation
- Technology due diligence (acquisitions/procurement)
- Risk assessment (technical, operational, delivery)

### CATEGORY 2 — Platform & Product Engineering
- Web application development (React/Next, APIs)
- Mobile application development (cross-platform + native)
- SaaS product engineering (multi-tenant, subscriptions)
- API platforms & integrations (REST/GraphQL, third parties)
- Legacy modernization & re-platforming
- Microservices & event-driven systems
- Performance engineering & scalability hardening

### CATEGORY 3 — AI Systems & Agentic Automation
- LLM application development (RAG, tools, workflows)
- Agentic systems (multi-agent orchestration, task automation)
- Private/secure AI deployment (VPC/on-prem, data isolation)
- AI evaluation & quality (benchmarks, red teaming, monitoring)
- AI governance & guardrails (policy, safety layers, auditability)
- NLP and document intelligence (classification, extraction)
- Computer vision pipelines (inspection, OCR+vision, automation)
- Automation with RPA + AI (back-office workflows)

### CATEGORY 4 — Spatial Computing & Immersive Platforms
- WebGL experiences (Three.js/R3F) for brand + product
- Virtual buildings/showrooms (interactive tours)
- Digital twins (real estate/facilities/industrial)
- AR/VR prototypes and production apps
- Spatial UX design (navigation, interaction, hotspots)
- Real-time 3D optimization (performance + asset pipeline)

### CATEGORY 5 — Product Design & Experience Engineering
- Product UX strategy & user journeys
- UI/UX design for web/mobile
- Design systems (tokens, components, guidelines)
- Prototyping (high-fidelity interactive prototypes)
- Motion design & micro-interactions
- UX audits & usability testing
- Brand identity for digital products (premium positioning)

### CATEGORY 6 — Cloud, DevOps & Platform Reliability
- Cloud architecture (AWS-focused) & migration planning
- CI/CD pipelines and release automation
- Infrastructure as Code (Terraform/CDK)
- Containerization & orchestration (Docker/K8s)
- Observability (logging/metrics/tracing) & alerting
- SRE practices (incident response, SLIs/SLOs)
- Cost optimization (FinOps) & performance tuning

### CATEGORY 7 — Security, Privacy & Trust Engineering
- Secure architecture & threat modeling
- Secure SDLC (code scanning, secrets, policies)
- Zero-trust and IAM hardening
- Pen testing coordination + remediation engineering
- Compliance readiness (ISO 27001-style controls mapping)
- Data protection & privacy engineering
- AI security (prompt injection defense, data leakage prevention)

### CATEGORY 8 — Data Platforms & Analytics
- Data engineering pipelines (ELT/ETL, orchestration)
- Analytics & BI (dashboards, KPI frameworks)
- Data warehouses/lakes (architecture + implementation)
- Data governance (quality, lineage, access control)
- Real-time streaming & event analytics
- AI-ready data preparation (feature stores)

### CATEGORY 9 — Commerce, Content & Growth Platforms
- E-commerce builds (headless or traditional)
- Payments, subscriptions, invoicing integrations
- CMS builds & migrations (headless CMS + workflows)
- SEO technical foundations + performance
- Growth analytics (events, funnels, attribution)
- CRM/marketing automation integrations

### CATEGORY 10 — Creative & Visual Design Services (NEW)
- AI-powered visual design (Midjourney, DALL-E, Stable Diffusion, Flux)
- AI video production (Runway, Kling, Sora-style generation)
- Brand & identity design (strategy, logo, guidelines, typography)
- Marketing & advertising design (campaigns, social, display, email)
- Print & physical design (packaging, publications, signage)
- Product & industrial visualization (3D rendering, mockups)
- Video & motion production (brand, explainer, motion graphics)
- Illustration & custom art (editorial, icons, character design)

---

## Service Model

```
id           uuid (server-generated)
slug         string (kebab-case, unique)
title        string
category     enum (one of 10 ServiceCategory values)
summary      text (short description)
body         text (markdown or rich text)
deliverables string[] (1-20 items)
tags         string[] (max 20)
is_featured  boolean (default false)
sort_order   integer (default 0)
created_at   datetime (server timestamp)
updated_at   datetime (server timestamp)
```

## Room Mapping (Services → World Nodes)

Each ServiceCategory maps 1:1 to a world node/room key:

| Category | Room Key | Status |
|----------|----------|--------|
| Strategy & Architecture | `strategy_architecture` | Seeded |
| Platform & Product Engineering | `platform_engineering` | Seeded |
| AI Systems & Agentic Automation | `ai_systems` | Seeded |
| Spatial Computing & Immersive | `spatial_immersive` | Seeded |
| Product Design & Experience | `product_design` | Seeded |
| Cloud, DevOps & Reliability | `cloud_devops` | Seeded |
| Security, Privacy & Trust | `security_trust` | Seeded |
| Data Platforms & Analytics | `data_platforms` | Seeded |
| Commerce, Content & Growth | `commerce_growth` | Seeded |
| Creative & Visual Design (NEW) | `creative_design` | Sprint 4 |

Hotspots in each room open a Service panel filtered by category.

---

## UX Flow

### Entry
1. Landing screen with "Enter" CTA.
2. Clicking Enter triggers drone animation (cinematic camera sequence via GSAP timeline).
3. Drone sequence: bird-eye → orbit → front approach → door level → at door.
4. At door: "Open" CTA visible. Clicking navigates to lobby.

### Navigation
- Interior navigation via hotspots (no traditional menu in world mode).
- Each room contains hotspots for viewing services, projects, or navigating to other rooms.
- Panels slide in from the right (480px desktop, full-width mobile).

### World Experience
World consists of Nodes (rooms). Each node has:
- Camera position, target, FOV (database-driven)
- Environment settings (lighting, fog — future)
- Hotspots array (interactive 3D spheres)

### Hotspots
- 3D spheres anchored at world coordinates (database-driven position).
- Hover: scale 1.2, color shift to white, cursor pointer.
- Click actions:
  - `OPEN_PANEL` — show service/project/contact panel
  - `NAVIGATE_NODE` — camera transition to target room
  - `OPEN_URL` — open external link in new tab

### Entry State Machine
```
IDLE → DRONE → AT_DOOR → INSIDE
```

---

## Routes

| Path | Component | Access |
|------|-----------|--------|
| `/` | Home (landing) | Public |
| `/world` | WorldPage (3D experience) | Public |
| `/admin/login` | AdminLoginPage | Public |
| `/admin` | AdminLayout | JWT Protected |
| `/admin/services` | ServicesAdminPage | JWT Protected |
| `/admin/projects` | ProjectsAdminPage | JWT Protected |
| `/admin/world` | WorldAdminPage | JWT Protected |
| `/admin/leads` | Leads viewer | JWT Protected |

---

## Data Model

### Public Content
- **Services** — 10 categories of consulting offerings
- **Projects** — Portfolio items with media attachments
- **ProjectMedia** — Images/videos attached to projects (cascade delete)
- **WorldNodes** — 3D scene nodes with camera configuration
- **WorldHotspots** — Interactive points within nodes

### Leads
- **Leads** — Contact form submissions (rate-limited)

### Admin
- **Users** — Admin authentication (single admin, seed script provisioned)

---

## Backend APIs

### Public
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/api/services` | Service listing (category filter) |
| GET | `/api/projects` | Project listing (tag filter) |
| GET | `/api/world` | World nodes + hotspots |
| POST | `/api/leads` | Lead submission (rate-limited) |

### Auth/Admin
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/login` | JWT token generation |
| CRUD | `/api/admin/services` | Service management |
| CRUD | `/api/admin/projects` | Project + media management |
| CRUD | `/api/admin/world/nodes` | World node management |
| CRUD | `/api/admin/world/hotspots` | Hotspot management |
| GET | `/api/admin/leads` | Lead viewer (search) |

See `API_Reference.md` for complete endpoint documentation.

---

## Frontend Architecture

- **3D Engine (R3F):** WorldCanvas → CameraController → ExteriorScene / InteriorScene → HotspotRenderer
- **UI Overlay:** WorldPanel (services/projects/contact panels), WorldHUD (navigation controls)
- **State:** Zustand stores:
  - `worldStore` (currentNode, entryPhase, activePanel, dataCache, leadSubmission)
  - `useAppStore` (general UI state)
- **Transitions:** GSAP timeline for camera animations, CSS transitions for panels.

---

## Performance Requirements
- Lazy-load heavy assets (GLB rooms, textures).
- Use DRACO/meshopt compressed GLB where possible (Sprint 4).
- Use KTX2/Basis for textures (Phase 2).
- FPS target: 45–60 desktop, 30+ mobile.
- Provide fallback: if WebGL fails, show flat mode pages.
- API response time: < 200ms.
- Page load (including 3D): < 3 seconds.

---

## Security
- ✅ Rate limit POST /api/leads (in-memory, per-IP)
- ✅ Pydantic input validation on all endpoints
- ✅ Admin JWT authentication
- ❌ Login rate limiting (Sprint 1)
- ❌ CORS locked to allowed domains (Sprint 1)
- ❌ httpOnly cookie token storage (Sprint 1)
- ❌ HTML sanitization on body/message fields (Sprint 1)
- ❌ JWT secret enforcement in production (Sprint 1)

See `Security_Hardening_Plan.md` for full remediation plan.
