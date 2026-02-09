# Requirements to Architecture Mapping v3.0
## Hengshi Design Digital Platform

### Document Control
- **Document ID:** RAM-HD-2026-003
- **Version:** 3.0
- **Date:** February 9, 2026
- **Status:** Active
- **Supersedes:** Requirements to Architecture Mapping v1.0 (Feb 2025)

---

## 1. Overview

This document maps requirements from the SRS v3.0 to their architectural implementation in the SAD v3.0, ensuring complete traceability. It reflects the current monorepo architecture (React/FastAPI/PostgreSQL).

---

## 2. Authentication & Authorization Mapping

| SRS Requirement | SAD Component | Implementation | Verification |
|----------------|---------------|----------------|--------------|
| FR-AUTH-001: JWT login | Backend: auth router | `POST /api/auth/login` → PyJWT token generation | ✅ test_auth.py |
| FR-AUTH-002: bcrypt hashing | Backend: auth module | `bcrypt.hashpw()` with auto-salt | ✅ test_auth.py |
| FR-AUTH-003: Token expiry | Backend: auth/jwt.py | `JWT_EXPIRES_MINUTES` env var (default 120) | ✅ test_auth.py |
| FR-AUTH-004: RBAC | Backend: auth dependency | `require_admin()` checks role='admin' | ✅ test_auth.py |
| FR-AUTH-005: Login rate limiting | **GAP** | Not implemented | Sprint 1 — slowapi |
| FR-AUTH-006: Password complexity | **GAP** | Not implemented | Sprint 1 — Pydantic validator |
| FR-AUTH-008: httpOnly cookies | **GAP** | Currently localStorage | Sprint 1 — cookie migration |

---

## 3. Content Management Mapping

### 3.1 Services

| SRS Requirement | SAD Component | Implementation | Verification |
|----------------|---------------|----------------|--------------|
| FR-SVC-001: CRUD | Backend: admin/services router | Full CRUD with Pydantic validation | ✅ test_services.py |
| FR-SVC-002: Public listing | Backend: services router | `GET /api/services?category=` | ✅ test_services.py |
| FR-SVC-003: Slug routing | Backend: services schema | Kebab-case regex validation | ✅ test_services.py |
| FR-SVC-004: Deliverables | Data Layer: services table | JSON array column, 1–20 items | ✅ Schema validation |
| FR-SVC-005: Tags | Data Layer: services table | JSON array column, max 20 | ✅ Schema validation |
| FR-SVC-008: 10 categories | Backend: seed script | 9 seeded; Category 10 pending | Sprint 4 |

### 3.2 Projects

| SRS Requirement | SAD Component | Implementation | Verification |
|----------------|---------------|----------------|--------------|
| FR-PRJ-001: CRUD | Backend: admin/projects router | Full CRUD with media management | ✅ test_projects.py |
| FR-PRJ-002: Public listing | Backend: projects router | `GET /api/projects?tag=` | ✅ test_projects.py |
| FR-PRJ-003: Media attachments | Data Layer: project_media table | 1:N FK with cascade delete | ✅ test_projects.py |
| FR-PRJ-005: S3 upload | **GAP** | URLs only, no file upload | Sprint 4 |

---

## 4. 3D World System Mapping

| SRS Requirement | SAD Component | Implementation | Verification |
|----------------|---------------|----------------|--------------|
| FR-3D-001: DB-driven config | Data Layer: world_nodes table | JSON columns for camera settings | ✅ test_world.py |
| FR-3D-002: Hotspot system | Frontend: HotspotRenderer | 3 action types with payload dispatch | ✅ test_world.py (API) |
| FR-3D-003: Camera animations | Frontend: CameraController | GSAP timeline with keyframes | Manual QA |
| FR-3D-004: Drone animation | Frontend: ExteriorScene | 5-position GSAP sequence | ⚠️ Needs coordinate fix |
| FR-3D-005: GLB exterior | Frontend: ExteriorScene | useGLTF loader with Blender model | ⚠️ Needs alignment |
| FR-3D-006: Admin world UI | Frontend: admin/world | Node + hotspot CRUD forms | ✅ Functional |
| FR-3D-007: Lobby scene | **GAP** | Not implemented | Sprint 3 |
| FR-3D-008: Room template | **GAP** | Not implemented | Sprint 3 |

---

## 5. Lead Capture Mapping

| SRS Requirement | SAD Component | Implementation | Verification |
|----------------|---------------|----------------|--------------|
| FR-LEAD-001: Rate limiting | Backend: leads/routes.py | In-memory per-IP bucket | ✅ test_leads.py |
| FR-LEAD-002: Required fields | Backend: leads schema | Pydantic model: name, email | ✅ test_leads.py |
| FR-LEAD-005: Admin viewer | Frontend: admin/leads | Search + list interface | ✅ Functional |
| FR-LEAD-006: Email notification | **GAP** | Not implemented | Sprint 4 (SendGrid/SES) |
| FR-LEAD-007: Redis rate limiting | **GAP** | In-memory only | Sprint 2 |

---

## 6. Non-Functional Requirements Mapping

### 6.1 Performance

| SRS Requirement | SAD Component | Implementation | Status |
|----------------|---------------|----------------|--------|
| NFR: API < 200ms | FastAPI async | Uvicorn ASGI server | ✅ Met (dev) |
| NFR: DB < 100ms | SQLAlchemy + PostgreSQL | Connection pooling, eager loading | ✅ Met (dev) |
| NFR: Page load < 3s | Vite build + R3F | Needs optimization (GLB loading) | ⚠️ Varies |

### 6.2 Security

| SRS Requirement | SAD Component | Status |
|----------------|---------------|--------|
| NFR-SEC-001: HTTPS | Deployment config | ❌ Sprint 5 |
| NFR-SEC-002: CORS | FastAPI middleware | ⚠️ Needs restriction (Sprint 1) |
| NFR-SEC-003: JWT secret | Environment config | ⚠️ Needs enforcement (Sprint 1) |
| NFR-SEC-004: Input sanitization | Pydantic + sanitizer | ⚠️ Partial (Sprint 1) |

---

## 7. Gap Summary

### 7.1 Critical Gaps (Sprint 1–2)

| Gap | SRS Ref | Severity | Resolution Sprint |
|-----|---------|----------|-------------------|
| Login rate limiting | FR-AUTH-005 | P0 | Sprint 1 |
| JWT secret enforcement | NFR-SEC-003 | P0 | Sprint 1 |
| httpOnly cookie migration | FR-AUTH-008 | P0 | Sprint 1 |
| CORS restriction | NFR-SEC-002 | P0 | Sprint 1 |
| Password complexity | FR-AUTH-006 | P1 | Sprint 1 |
| Redis rate limiting | FR-LEAD-007 | P1 | Sprint 2 |
| Structured logging | — | P1 | Sprint 2 |
| Error tracking (Sentry) | — | P1 | Sprint 1 |
| Frontend test suite | — | P1 | Sprint 2 |

### 7.2 Medium Gaps (Sprint 3–4)

| Gap | SRS Ref | Resolution Sprint |
|-----|---------|-------------------|
| Lobby scene | FR-3D-007 | Sprint 3 |
| Room template | FR-3D-008 | Sprint 3 |
| 3D coordinate alignment | FR-3D-004/005 | Sprint 3 |
| Category 10 seed data | FR-SVC-008 | Sprint 4 |
| S3 file upload | FR-PRJ-005 | Sprint 4 |
| Email notifications | FR-LEAD-006 | Sprint 4 |

### 7.3 Deferred Gaps (Phase 2+)

| Gap | Phase | Notes |
|-----|-------|-------|
| IoT device management | Phase 2 | MQTT + TimescaleDB |
| Multi-tenancy | Phase 3 | Row-level security |
| OAuth 2.0 / SSO | Phase 3 | Identity provider integration |
| Billing/subscriptions | Phase 3 | Stripe integration |
| AI-powered features | Phase 4 | OpenAI/Anthropic API |

---

## 8. Verification Matrix

| Test Suite | Coverage | Requirements Covered |
|-----------|----------|---------------------|
| test_auth.py | Happy paths | FR-AUTH-001 through 004 |
| test_health.py | Basic | Health endpoint |
| test_services.py | Happy paths | FR-SVC-001 through 007 |
| test_projects.py | Happy paths | FR-PRJ-001 through 004 |
| test_world.py | Happy paths | FR-3D-001, 002, 006 |
| test_leads.py | Happy paths + rate limit | FR-LEAD-001 through 005 |
| Frontend tests | **0%** | None — Sprint 2 priority |
