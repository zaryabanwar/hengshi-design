# Software Architecture Document (SAD) v3.0
## Hengshi Design Digital Platform

### Document Control
- **Document ID:** SAD-HD-2026-003
- **Version:** 3.0
- **Date:** February 9, 2026
- **Status:** Active
- **Supersedes:** SAD v1.0 (Feb 2025), SAD Implementation Specs v1.0 (Feb 2025)

---

## 1. Introduction

### 1.1 Purpose
This document describes the software architecture of the Hengshi Design Digital Platform as currently implemented. It replaces the original SAD v1.0 which described a microservices architecture (Docker/K8s/Kafka/Consul) that was descoped during the strategic pivot to a monorepo pattern.

### 1.2 Architectural Decision
**ADR-001: Monorepo over Microservices**
- **Decision:** Adopt a React/FastAPI/PostgreSQL monorepo instead of the 11-service microservices architecture.
- **Rationale:** Reduce time-to-market for a solo developer; eliminate operational complexity of K8s/Kafka; maintain clean module boundaries for future decomposition.
- **Trade-offs:** Simpler deployment and operations now; requires refactoring for Phase 3 multi-tenant/IoT capabilities.
- **Extensibility:** Module boundaries, clean API contracts, and database schema design preserve the ability to decompose into microservices when scale demands it.

---

## 2. Architectural Overview

### 2.1 Architecture Style
**Modular Monorepo** with the following characteristics:
- Single deployable backend (FastAPI) with modular routers
- Single deployable frontend (React SPA) with feature-based organization
- Shared types package for cross-boundary contracts
- PostgreSQL as the single source of truth
- REST API as the integration boundary between frontend and backend

### 2.2 Architecture Layers

```
┌─────────────────────────────────────────────────┐
│                  Client Layer                    │
│         Web Browsers (Desktop/Mobile)            │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────┴───────────────────────────────┐
│               Frontend Layer                     │
│  React 18 + TypeScript + Vite                    │
│  ┌──────────┐ ┌──────────┐ ┌──────────────────┐ │
│  │  Pages   │ │  Admin   │ │  3D World (R3F)  │ │
│  │ (public) │ │ (CRUD)   │ │  GSAP + Zustand  │ │
│  └──────────┘ └──────────┘ └──────────────────┘ │
└─────────────────┬───────────────────────────────┘
                  │ REST API (HTTP/JSON)
┌─────────────────┴───────────────────────────────┐
│                 API Layer                        │
│  FastAPI + Pydantic + JWT Auth                   │
│  ┌────────┐ ┌──────────┐ ┌────────┐ ┌────────┐ │
│  │  Auth  │ │ Services │ │Projects│ │ World  │ │
│  │ Router │ │  Router  │ │ Router │ │ Router │ │
│  └────────┘ └──────────┘ └────────┘ └────────┘ │
│  ┌────────┐ ┌──────────────────────────────────┐ │
│  │ Leads  │ │    Admin CRUD Routers            │ │
│  │ Router │ │  (services, projects, world,     │ │
│  └────────┘ │   leads — JWT protected)         │ │
│             └──────────────────────────────────┘ │
└─────────────────┬───────────────────────────────┘
                  │ SQLAlchemy 2.0 ORM
┌─────────────────┴───────────────────────────────┐
│                Data Layer                        │
│  PostgreSQL 16 (Docker)                          │
│  ┌──────┐ ┌────────┐ ┌────────┐ ┌───────────┐  │
│  │Users │ │Services│ │Projects│ │World Nodes│  │
│  └──────┘ └────────┘ └────────┘ └───────────┘  │
│  ┌─────────────┐ ┌───────────────┐ ┌────────┐  │
│  │Project Media│ │World Hotspots │ │ Leads  │  │
│  └─────────────┘ └───────────────┘ └────────┘  │
└─────────────────────────────────────────────────┘
```

### 2.3 Monorepo Structure

```
hengshi-design/
├── apps/
│   ├── api/                    # FastAPI backend
│   │   ├── app/
│   │   │   ├── admin/          # Admin CRUD routes (JWT protected)
│   │   │   ├── auth/           # JWT auth (login, token validation)
│   │   │   ├── db/             # Database session + engine
│   │   │   ├── models/         # SQLAlchemy ORM models
│   │   │   ├── leads/          # Lead capture + rate limiting
│   │   │   ├── projects/       # Project routes + schemas
│   │   │   ├── services/       # Service routes + schemas
│   │   │   ├── world/          # World node/hotspot routes + schemas
│   │   │   ├── scripts/        # Seed scripts (admin, services, world)
│   │   │   └── main.py         # FastAPI app entry point
│   │   ├── alembic/            # Database migrations (7 revisions)
│   │   ├── tests/              # pytest suite
│   │   └── requirements.txt
│   │
│   └── web/                    # React + Vite frontend
│       ├── src/
│       │   ├── admin/          # Admin CRUD interfaces
│       │   ├── pages/          # Public pages (Home, World)
│       │   ├── world/          # 3D visualization components
│       │   ├── stores/         # Zustand state stores
│       │   ├── lib/            # API client, types, utilities
│       │   └── App.tsx         # React Router configuration
│       └── public/models/      # GLB 3D model assets
│
├── packages/shared/            # Shared Zod schemas + TypeScript types
├── docs/                       # SPEC.md, BACKLOG.md, documentation
└── docker-compose.yml          # Local PostgreSQL
```

---

## 3. Backend Architecture

### 3.1 FastAPI Application

**Entry Point:** `apps/api/app/main.py`

The FastAPI application mounts modular routers with prefix-based routing:

| Router | Prefix | Auth | Purpose |
|--------|--------|------|---------|
| auth | `/api/auth` | None | Login, token generation |
| services | `/api/services` | None | Public service listing |
| projects | `/api/projects` | None | Public project listing |
| world | `/api/world` | None | Public world structure |
| leads | `/api/leads` | None (rate-limited) | Lead submission |
| admin_services | `/api/admin/services` | JWT | Service CRUD |
| admin_projects | `/api/admin/projects` | JWT | Project CRUD |
| admin_world | `/api/admin/world` | JWT | World node/hotspot CRUD |
| admin_leads | `/api/admin/leads` | JWT | Lead viewer |

**Middleware:**
- CORS middleware (currently overly permissive — needs hardening)
- No structured logging middleware (gap)
- No request tracing middleware (gap)

### 3.2 Authentication Flow

```
Client                    FastAPI                   PostgreSQL
  │                         │                          │
  ├─POST /api/auth/login──►│                          │
  │  {email, password}      │                          │
  │                         ├─SELECT user by email────►│
  │                         │◄─User record─────────────┤
  │                         │                          │
  │                         ├─bcrypt.verify(password)  │
  │                         │                          │
  │                         ├─Generate JWT             │
  │                         │  {sub, email, role, exp} │
  │                         │                          │
  │◄─{access_token, type}──┤                          │
  │                         │                          │
  ├─GET /api/admin/* ──────►│                          │
  │  Authorization: Bearer  │                          │
  │                         ├─Decode JWT               │
  │                         ├─Verify role='admin'      │
  │                         ├─Process request──────────►
  │◄─Response──────────────┤◄──────────────────────────┤
```

**Implementation Details:**
- Signing algorithm: HS256 (PyJWT)
- Token lifetime: 120 minutes (JWT_EXPIRES_MINUTES env var)
- Password hashing: bcrypt with auto-generated salt
- Admin seed: `python -m app.scripts.create_admin`

### 3.3 Database Layer

**ORM:** SQLAlchemy 2.0 with `Mapped` type annotations

**Session Management:** Dependency injection via `Depends(get_db)` — yields a session per request with automatic cleanup.

**Migrations:** Alembic with 7 revision files tracking schema evolution.

**Connection:** `postgresql+psycopg://` driver string via `DATABASE_URL` environment variable.

**Key Patterns:**
- Eager loading for nested relationships (projects → media, nodes → hotspots)
- UUID primary keys generated server-side
- JSON columns for flexible data (deliverables, tags, camera_position, payload)
- Unique constraints on slugs and keys

### 3.4 Rate Limiting

**Lead Endpoint:** Per-IP rate limiting with configurable thresholds:
- `LEAD_RATE_LIMIT_MAX_REQUESTS`: 5 (default)
- `LEAD_RATE_LIMIT_WINDOW_SECONDS`: 60 (default)
- Implementation: In-memory bucket tracking (thread-safe)
- Limitation: Does not scale across multiple processes — Redis replacement planned (Sprint 2)

---

## 4. Frontend Architecture

### 4.1 Application Structure

**React Router v6 Routes:**

| Path | Component | Access |
|------|-----------|--------|
| `/` | Home | Public |
| `/world` | WorldPage | Public |
| `/admin/login` | AdminLogin | Public |
| `/admin` | AdminDashboard | JWT Protected |
| `/admin/services` | ServicesCRUD | JWT Protected |
| `/admin/projects` | ProjectsCRUD | JWT Protected |
| `/admin/world` | WorldCRUD | JWT Protected |
| `/admin/leads` | LeadViewer | JWT Protected |

### 4.2 State Management

**Zustand Store** (`worldStore.ts`) centralizes:
- **World navigation:** Current node, node history, transition state
- **Panel UI:** Active panel type (services/projects/contact), open/closed state
- **Data caching:** Services cached per category, projects cached globally
- **Lead submission:** Form state and submission handling
- **Entry phase:** State machine (idle → drone → atDoor → inside)

### 4.3 3D World System

The immersive 3D experience is the platform's primary differentiator. It is powered by a database-driven configuration system that allows the entire experience to be modified via the admin UI without code changes.

**Architecture:**
```
WorldPage
├── WorldCanvas (R3F Canvas)
│   ├── CameraController (GSAP animations)
│   ├── ExteriorScene (GLB model, drone animation)
│   ├── InteriorScene (room rendering)
│   ├── HotspotRenderer (interactive spheres)
│   └── Lighting (ambient + directional)
└── PanelOverlay (HTML/CSS panels)
    ├── ServicesPanel
    ├── ProjectsPanel
    └── ContactPanel
```

**Entry Flow:**
1. **Idle** → Landing state, waiting for user interaction
2. **Drone** → Cinematic fly-in: bird-eye → orbit → door approach (5 GSAP keyframes)
3. **AtDoor** → Paused at building entrance, "Open" CTA visible
4. **Inside** → Interior navigation with hotspot-driven room transitions

**Database Configuration:**
- `WorldNode` defines each scene (exterior, lobby, service rooms) with camera settings (position, target, FOV)
- `WorldHotspot` defines interactive points within each node with action type and payload
- Each service category maps 1:1 to a world room node (see Appendix A in Consolidation v3)

### 4.4 API Client

Centralized API client (`lib/api.ts`) handles:
- Base URL from `VITE_API_BASE_URL` environment variable
- JWT token attachment for admin requests
- Response parsing and error handling
- Token storage (currently localStorage — migration to httpOnly cookies planned)

---

## 5. Data Architecture

### 5.1 Schema Design

The database schema supports the current content management and 3D configuration needs with extensibility for future phases.

**Core Entities:**

| Table | Purpose | Key Fields | Relationships |
|-------|---------|------------|---------------|
| users | Admin authentication | email, password_hash, role | — |
| services | Service catalog | slug, category, deliverables[], tags[] | — |
| projects | Portfolio items | slug, tags[], is_featured | → project_media |
| project_media | Media attachments | type, url, caption | → projects |
| world_nodes | 3D scene definitions | key, camera_position{}, camera_fov | → world_hotspots |
| world_hotspots | Interactive points | kind, position{}, payload{} | → world_nodes |
| leads | Contact submissions | name, email, message, metadata{} | — |

### 5.2 Data Patterns

- **JSON columns** for semi-structured data: deliverables, tags, camera positions, hotspot payloads, metadata
- **UUID primary keys** for all tables — avoids sequential ID enumeration
- **Soft delete not implemented** — hard deletes with cascade for related records
- **No versioning** — single current state per record (versioning planned for Phase 2)

### 5.3 Migration Strategy

Alembic manages schema migrations with:
- Auto-generated migrations from model changes
- Revision chain: 7 migrations from initial schema to current state
- Rollback capability via `alembic downgrade`
- Applied via: `alembic upgrade head`

---

## 6. Security Architecture

### 6.1 Current State

| Control | Status | Details |
|---------|--------|---------|
| Authentication | ✅ Implemented | JWT with bcrypt password hashing |
| Authorization | ✅ Implemented | Role-based (admin only) |
| HTTPS | ❌ Not enforced | Planned for production deployment |
| CORS | ⚠️ Overly permissive | `allow_methods=['*']` needs restriction |
| Input validation | ✅ Pydantic | Schema validation on all endpoints |
| HTML sanitization | ❌ Missing | Body/message fields accept raw HTML |
| Rate limiting (login) | ❌ Missing | Brute force vulnerability |
| Rate limiting (leads) | ✅ Implemented | In-memory per-IP (needs Redis) |
| Token storage | ⚠️ localStorage | XSS vulnerable; httpOnly cookies planned |
| Structured logging | ❌ Missing | No request/security event logging |

### 6.2 Security Hardening Plan

See `Security_Hardening_Plan.md` for the detailed Sprint 1–2 remediation plan covering:
- Login rate limiting (slowapi)
- JWT secret enforcement
- CORS restriction
- httpOnly cookie migration
- Input sanitization
- Password complexity

### 6.3 Future Security Architecture (Phase 2–3)

- OAuth 2.0 / OpenID Connect integration
- Multi-factor authentication
- Attribute-based access control (ABAC)
- Encryption at rest (AES-256)
- Key rotation (90-day policy)
- Audit logging with 1-year retention
- AI security (prompt injection defense)

---

## 7. Deployment Architecture

### 7.1 Current State (Development)

```
Developer Machine (Windows)
├── Docker Compose
│   └── PostgreSQL 16 (port 5432)
├── FastAPI (uvicorn --reload, port 8000)
└── Vite Dev Server (port 5173)
```

### 7.2 Planned Production (Sprint 5)

```
┌─────────────────────────────────────────────┐
│                    AWS                       │
│                                              │
│  ┌──────────┐    ┌──────────────────────┐   │
│  │ Route 53 │───►│     CloudFront       │   │
│  │  (DNS)   │    │   (CDN + SSL)        │   │
│  └──────────┘    └────────┬─────────────┘   │
│                           │                  │
│              ┌────────────┴────────────┐     │
│              │                         │     │
│     ┌────────┴───────┐    ┌───────────┴──┐  │
│     │   S3 Bucket    │    │   ECS/EC2    │  │
│     │ (React build)  │    │  (FastAPI)   │  │
│     └────────────────┘    └──────┬───────┘  │
│                                  │          │
│                          ┌───────┴───────┐  │
│                          │ RDS PostgreSQL│  │
│                          │  (managed)    │  │
│                          └───────────────┘  │
└─────────────────────────────────────────────┘
```

### 7.3 CI/CD Pipeline (Planned)

GitHub Actions workflow:
1. **Trigger:** Push to main / PR
2. **Lint:** ESLint (frontend), Ruff (backend)
3. **Test:** Vitest (frontend), pytest (backend)
4. **Build:** Vite build (frontend), Docker image (backend)
5. **Deploy:** S3 sync (frontend), ECS update (backend)

---

## 8. Monitoring and Observability

### 8.1 Current State
- Health check endpoint: `GET /health`
- No structured logging
- No error tracking
- No metrics collection
- No alerting

### 8.2 Planned (Sprint 1–2)

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Error tracking | Sentry | Exception capture + performance |
| Structured logging | structlog | JSON request/response logs |
| Health checks | Enhanced /health | DB connectivity, version info |
| Metrics | (Phase 2) | Prometheus/CloudWatch |
| Dashboards | (Phase 2) | Grafana/CloudWatch |

---

## 9. Testing Strategy

### 9.1 Current Coverage

| Layer | Coverage | Tools | Status |
|-------|----------|-------|--------|
| Backend unit tests | ~30% (happy paths) | pytest + httpx | ⚠️ Needs expansion |
| Backend integration | 0% | — | ❌ Not started |
| Frontend unit tests | 0% | — | ❌ Not started |
| Frontend integration | 0% | — | ❌ Not started |
| E2E tests | 0% | — | ❌ Not started |
| Performance tests | 0% | — | ❌ Not started |

### 9.2 Target Coverage (Sprint 2)

| Layer | Target | Tools |
|-------|--------|-------|
| Backend unit | 80%+ | pytest + httpx |
| Frontend unit | 60%+ | Vitest + React Testing Library |
| API contract | All endpoints | OpenAPI validation |
| Performance | Key flows | k6 (Phase 2) |

---

## 10. Extensibility for Future Phases

The monorepo architecture preserves extensibility through:

1. **Modular router pattern:** New service domains add as new router modules without touching existing code
2. **Clean API contracts:** Pydantic schemas serve as interface contracts that can become service boundaries
3. **Database schema design:** UUID PKs, JSON columns, and migration tooling support schema evolution
4. **3D world system:** Database-driven configuration means new rooms/scenes require only data, not code
5. **Shared types package:** Cross-boundary type contracts ready for service decomposition

**Phase 2 additions** (IoT, billing) will add as new router modules within the existing FastAPI app before any microservice extraction.

**Phase 3 extraction** (if needed for scale) will decompose routers into separate services behind an API gateway, with Kafka for event streaming.

---

## Appendices

### Appendix A: Technology Decisions Log

| Decision | From | To | Rationale |
|----------|------|----|-----------|
| Frontend framework | Angular 19 | React 18 + TypeScript | Faster development, R3F ecosystem for 3D |
| Backend framework | Django + DRF | FastAPI + SQLAlchemy 2.0 | Async support, Pydantic validation, OpenAPI auto-docs |
| Database | MongoDB | PostgreSQL | Relational integrity, mature tooling, TimescaleDB extension path |
| State management | NGRX | Zustand | Simpler API, sufficient for current complexity |
| 3D rendering | Three.js (direct) | React Three Fiber | Declarative 3D, React integration, drei helpers |
| Animation | Angular Animations | GSAP | Industry-standard, timeline support, R3F compatibility |
| Architecture | 11-service microservices | Monorepo | Solo developer velocity, reduced ops complexity |
| Cloud | Azure-first | AWS-planned | Broader ecosystem, better pricing for startup scale |

### Appendix B: Change History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Feb 2025 | Initial SAD: microservices, K8s, Kafka, Consul, MongoDB |
| 3.0 | Feb 2026 | Complete rewrite: monorepo, React/FastAPI/PostgreSQL |
