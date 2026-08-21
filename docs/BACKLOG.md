# Hengshi Design - Backlog

**Version:** 2.0 | **Date:** February 9, 2026 | **Status:** Active

**Overall Readiness:** ~40% | **Core Platform:** 90% | **Security:** 30% | **Testing:** 20%

Service taxonomy v2.0 (10 categories) locked in SPEC.md and Consolidation v3.

---

## Completed (Prompts 1–11)

### EPIC 0 — Foundation
#### Story 0.1 — Monorepo scaffold ✅ DONE
- apps/web and apps/api created, docker-compose PostgreSQL working, README with run steps

#### Story 0.2 — Shared typing ✅ DONE
- packages/shared exports Zod schemas + TS types for core models

### EPIC 1 — Backend Core
#### Story 1.1 — API skeleton + health ✅ DONE
- GET /health → {"status": "ok"}

#### Story 1.2 — PostgreSQL + SQLAlchemy + Alembic ✅ DONE
- SQLAlchemy 2.0 base/session, Alembic configured, 7 migrations, DATABASE_URL

#### Story 1.3 — Auth (admin) ✅ DONE
- POST /api/auth/login returns JWT, require_admin dependency, create_admin seed script

### EPIC 2 — Content Models + CRUD
#### Story 2.1 — Services CRUD ✅ DONE
- Admin CRUD + public list endpoints, slug validation, 9 categories seeded, deliverables/tags

#### Story 2.2 — Projects CRUD + Media ✅ DONE
- Project list/detail, project_media table, cascade delete, tag filtering

#### Story 2.3 — Leads ✅ DONE
- POST /api/leads rate-limited (per-IP), GET /api/admin/leads with search

### EPIC 3 — World System
#### Story 3.1 — World schema + seed ✅ DONE
- world_nodes + world_hotspots tables, seed script with exterior + 9 room nodes

#### Story 3.2 — Public world endpoint ✅ DONE
- GET /api/world returns nodes + hotspots (eager loaded)

#### Story 3.3 — Admin world CRUD ✅ DONE
- CRUD for nodes and hotspots via /api/admin/world

### EPIC 4 — Frontend Foundation
#### Story 4.1 — Web app scaffold ✅ DONE
- React + Vite + TS + Tailwind configured, routing, Zustand stores

#### Story 4.2 — API client ✅ DONE
- Typed fetch client with VITE_API_BASE_URL, handles JWT for admin routes

### EPIC 5 — Immersive Engine (R3F)
#### Story 5.1 — SceneRoot + CameraController ✅ DONE
- R3F Canvas with GSAP-driven camera transitions

#### Story 5.2 — NodeManager ✅ DONE
- Loads node camera settings from /api/world, GSAP timeline transitions

#### Story 5.3 — HotspotSystem ✅ DONE
- Renders hotspots from API, hover/click with 3 action types

#### Story 5.4 — Exterior + drone intro ✅ DONE (needs alignment)
- GLB model loaded, GSAP drone path (5 keyframes), door hotspot
- ⚠️ Magic numbers in ExteriorScene — needs Blender coordinate extraction

### EPIC 6 — UI Overlay
#### Story 6.1 — Panels ✅ DONE
- ServicesPanel, ProjectsPanel, ContactPanel with lead submit

### EPIC 7 — Admin UI
#### Story 7.1 — Admin login ✅ DONE
- Login form, JWT stored (localStorage — needs httpOnly migration), protected routes

#### Story 7.2 — Admin CRUD screens ✅ DONE
- Services, Projects, World node/hotspot CRUD with JSON editors

---

## Sprint 1: Security & Stability (Weeks 1–2)

### Story S1.1 — Login rate limiting 🔴 P0
- Install slowapi, add to POST /api/auth/login (5 per 15 min per IP)
- Return 429 with Retry-After header, log failed attempts
- **Files:** requirements.txt, auth/routes.py, main.py

### Story S1.2 — JWT secret enforcement 🔴 P0
- Refuse startup if JWT_SECRET='change-me' when ENVIRONMENT=production
- Validate minimum 32 character length
- **Files:** main.py, auth/jwt.py

### Story S1.3 — httpOnly cookie migration 🔴 P0
- Set JWT as httpOnly/Secure/SameSite=Lax cookie on login
- Update frontend API client to credentials:'include', remove localStorage
- **Files:** auth/routes.py, auth/jwt.py, web/src/lib/api.ts, main.py

### Story S1.4 — CORS restriction 🔴 P0
- Restrict allow_methods, allow_headers, block wildcard in production
- Set allow_origins from CORS_ORIGINS env var
- **Files:** main.py

### Story S1.5 — Password complexity 🟡 P1
- Pydantic validator: min 12 chars, 1 upper, 1 lower, 1 digit, 1 special
- Apply to create_admin script
- **Files:** auth/schemas.py, scripts/create_admin.py

### Story S1.6 — Input sanitization 🟡 P1
- Install nh3, sanitize body/message/description fields
- **Files:** requirements.txt, services/schemas.py, leads/schemas.py

### Story S1.7 — Sentry error tracking 🟡 P1
- Install sentry-sdk[fastapi] + @sentry/react
- Configure DSN from env, add React ErrorBoundary
- **Files:** requirements.txt, main.py, package.json, App.tsx

### Story S1.8 — Expand backend tests 🟡 P1
- Add negative tests (invalid input, 401, 403, 409, 422)
- Add edge cases (empty arrays, null values, constraint violations)
- **Files:** tests/*

---

## Sprint 2: Testing & Monitoring (Weeks 3–4)

### Story S2.1 — Structured logging 🟡 P1
- Install structlog, JSON-formatted request/response logs
- Log security events: login attempts, rate limit hits, token validation failures
- **Files:** requirements.txt, main.py, auth/routes.py

### Story S2.2 — Frontend test suite 🟡 P1
- Set up Vitest + React Testing Library
- Component tests for admin forms, panel rendering, API client
- **Files:** web/package.json, web/vitest.config.ts, web/src/**/*.test.tsx

### Story S2.3 — GitHub Actions CI pipeline 🟡 P1
- Lint (ESLint + Ruff) → Test (Vitest + pytest) → Build (Vite + Docker)
- **Files:** .github/workflows/ci.yml

### Story S2.4 — Enhanced health check
- Verify DB connectivity, include version/environment
- Add /health/ready for deployment readiness
- **Files:** main.py or health/routes.py

### Story S2.5 — Redis for rate limiting 🟡 P1
- Add Redis to docker-compose.yml, replace in-memory rate limiter
- Use slowapi with Redis backend
- **Files:** docker-compose.yml, requirements.txt, leads/routes.py, main.py

---

## Sprint 3: 3D Experience Completion (Weeks 5–6)

### Story S3.1 — Extract Blender coordinates
- Get precise door and building center coords from Blender export
- Fix drone animation path with exact coordinates
- **Files:** web/src/world/ExteriorScene.tsx

### Story S3.2 — Lobby placeholder scene
- Build lobby scene with room navigation hotspots
- Prevents blank page when clicking door hotspot
- **Files:** web/src/world/ (new InteriorScene components)

### Story S3.3 — Room template
- Reusable room component for all 10 service categories
- Placeholder geometry with hotspots for service panel + back navigation
- **Files:** web/src/world/ (new RoomScene component)

### Story S3.4 — Loading progress indicator
- Show GLB model loading progress
- **Files:** web/src/world/WorldCanvas.tsx

### Story S3.5 — WebGL fallback
- Detect WebGL capability, show static gallery if unsupported
- **Files:** web/src/pages/WorldPage.tsx

---

## Sprint 4: Design Services & Content (Weeks 7–8)

### Story S4.1 — Category 10 seed data
- Add Creative & Visual Design to service seed data
- Create corresponding world room node + hotspots
- **Files:** scripts/seed_services.py, scripts/seed_world.py

### Story S4.2 — S3 presigned upload
- Admin media upload via presigned URLs
- **Files:** requirements.txt, new upload router, admin UI file input

### Story S4.3 — Populate service content
- Full body, deliverables for all 10 categories
- **Files:** scripts/seed_services.py

### Story S4.4 — Project portfolio entries
- Seed design work samples as projects
- **Files:** scripts/seed_projects.py

### Story S4.5 — Asset optimization pipeline
- DRACO compression for GLB models
- **Files:** Build scripts, public/models/

---

## Sprint 5: Deployment & Launch (Weeks 9–10)

### Story S5.1 — AWS infrastructure
- Configure S3 bucket, CloudFront distribution, ECS/EC2 for API
- **Files:** Infrastructure config (Terraform or manual)

### Story S5.2 — Production database
- RDS PostgreSQL setup, connection string, backups
- **Files:** .env.production

### Story S5.3 — Deploy frontend
- Vite build → S3 sync → CloudFront invalidation
- **Files:** .github/workflows/deploy.yml

### Story S5.4 — Deploy API
- Docker build → ECS deployment with env vars
- **Files:** Dockerfile, .github/workflows/deploy.yml

### Story S5.5 — Domain + SSL
- Route 53 DNS, ACM certificate
- **Files:** Infrastructure config

### Story S5.6 — Performance testing + final QA
- k6 load tests on key flows
- Full QA across all routes

---

## Phase 2+ (Deferred)

### IoT & Data Platform (Months 4–6)
- MQTT broker (EMQX) for device communication
- TimescaleDB for time-series telemetry
- Device management module
- Real-time data pipeline

### Multi-Tenant Enterprise (Months 7–10)
- Row-level security multi-tenancy
- Organization management
- Stripe billing integration
- White-label capabilities

### AI & Advanced Analytics (Months 11–14)
- AI-powered design generation
- Predictive analytics for IoT
- Natural language data queries
- Data monetization APIs

### Scale & Optimization (Months 15+)
- Kubernetes orchestration
- Global CDN / edge computing
- SOC 2 compliance
- React Native mobile app
