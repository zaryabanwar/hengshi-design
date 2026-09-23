# Software Requirements Specification (SRS) v3.0
## Hengshi Design Digital Platform

### Document Control
- **Document ID:** SRS-HD-2026-003
- **Version:** 3.0
- **Date:** February 9, 2026
- **Status:** Active
- **Supersedes:** SRS v1.0 (Feb 2025), SRS v2.0 (Feb 2025)

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification defines the functional and non-functional requirements for the Hengshi Design Digital Platform in its current implementation state. It reflects the strategic architectural pivot from the original microservices design (Angular/Django/MongoDB) to the focused React/FastAPI/PostgreSQL monorepo.

### 1.2 Project Scope
The platform is an immersive 3D web portfolio and service delivery ecosystem that transforms Hengshi Design from a traditional service provider into a platform-oriented company. The current implementation focuses on the core platform with extensibility preserved for future enterprise capabilities (IoT, multi-tenancy, advanced analytics).

### 1.3 Definitions and Abbreviations
- **R3F:** React Three Fiber — React renderer for Three.js
- **GSAP:** GreenSock Animation Platform
- **GLB/GLTF:** GL Transmission Format — 3D model format
- **JWT:** JSON Web Token
- **ORM:** Object-Relational Mapping
- **SPA:** Single Page Application
- **SSR:** Server-Side Rendering (planned, not currently implemented)

### 1.4 References
- Hengshi Design Project Consolidation v3.0 (HD-CONSOL-2026-003)
- Codebase Analysis Report (2026-02-09)
- MEMORY.md (Development reference)

---

## 2. System Description

### 2.1 System Context
The platform serves as an integrated digital ecosystem combining an immersive 3D portfolio experience with a content management backend. It showcases 10 service categories through an interactive building metaphor where users navigate 3D rooms corresponding to service areas.

### 2.2 Business Models Supported
1. **Managed Services / PaaS** — Multi-tenant platform (Phase 3)
2. **Data Monetization** — Analytics and insight APIs (Phase 4)
3. **Custom Development & Consulting** — Extensible architecture for client deployments
4. **Design Services** — AI-augmented creative production (Category 10, new)

### 2.3 Target Markets

| Tier | Industries | Key Drivers |
|------|-----------|-------------|
| Primary | Agriculture, Defense, Mining | High IoT adoption, operational efficiency |
| Secondary | Manufacturing, Healthcare, Smart Cities | Digital transformation, data analytics |
| Emerging | Creative Agencies, E-commerce, Startups | AI-powered design, immersive experiences |

---

## 3. User Classes and Characteristics

### 3.1 Current Implementation

#### 3.1.1 Platform Administrator
- Full access to admin dashboard
- CRUD operations on all content (services, projects, world configuration, leads)
- JWT-authenticated with role='admin'
- Single admin user (seed script provisioned)

#### 3.1.2 Public Visitor
- Accesses the immersive 3D experience
- Views service listings and project portfolio
- Submits contact/lead forms
- No authentication required

### 3.2 Future User Classes (Phase 2–3)

#### 3.2.1 Organization Admin
- Manages organization-specific settings and user permissions
- Service module configuration
- Billing and subscription management

#### 3.2.2 Dashboard User
- Accesses assigned service modules
- Real-time data interaction
- Basic report generation

#### 3.2.3 IoT Device Manager
- Device provisioning and management
- Firmware updates and monitoring
- Performance optimization

---

## 4. Functional Requirements

### 4.1 Authentication and Authorization

| ID | Requirement | Status | Priority |
|----|-------------|--------|----------|
| FR-AUTH-001 | JWT-based admin login with email/password | ✅ Implemented | P0 |
| FR-AUTH-002 | bcrypt password hashing with salt generation | ✅ Implemented | P0 |
| FR-AUTH-003 | Configurable token expiry (default 120 min) | ✅ Implemented | P0 |
| FR-AUTH-004 | Role-based access control (admin role) | ✅ Implemented | P0 |
| FR-AUTH-005 | Login rate limiting (brute force prevention) | ❌ Not implemented | P0 |
| FR-AUTH-006 | Password complexity requirements | ❌ Not implemented | P1 |
| FR-AUTH-007 | Refresh token rotation | ❌ Not implemented | P2 |
| FR-AUTH-008 | httpOnly cookie token storage (replace localStorage) | ❌ Not implemented | P0 |
| FR-AUTH-009 | Multi-factor authentication | ❌ Not implemented | Phase 2 |
| FR-AUTH-010 | OAuth 2.0 / SSO integration | ❌ Not implemented | Phase 3 |

### 4.2 Content Management — Services

| ID | Requirement | Status | Priority |
|----|-------------|--------|----------|
| FR-SVC-001 | CRUD operations for services (admin) | ✅ Implemented | P0 |
| FR-SVC-002 | Public service listing with category filter | ✅ Implemented | P0 |
| FR-SVC-003 | Slug-based routing (kebab-case validation) | ✅ Implemented | P0 |
| FR-SVC-004 | Deliverables array (1–20 items) | ✅ Implemented | P0 |
| FR-SVC-005 | Tags for filtering (max 20) | ✅ Implemented | P0 |
| FR-SVC-006 | Featured flag and sort ordering | ✅ Implemented | P1 |
| FR-SVC-007 | Full-text search on title/summary/body | ✅ Implemented | P1 |
| FR-SVC-008 | 10 service categories (9 seeded + 1 new Design) | ⚠️ 9 of 10 seeded | P1 |
| FR-SVC-009 | Draft/preview system | ❌ Not implemented | Phase 2 |
| FR-SVC-010 | Scheduled publishing | ❌ Not implemented | Phase 2 |

### 4.3 Content Management — Projects

| ID | Requirement | Status | Priority |
|----|-------------|--------|----------|
| FR-PRJ-001 | CRUD operations for projects (admin) | ✅ Implemented | P0 |
| FR-PRJ-002 | Public project listing with tag filter | ✅ Implemented | P0 |
| FR-PRJ-003 | Multiple media attachments per project | ✅ Implemented | P0 |
| FR-PRJ-004 | Cascade delete media on project removal | ✅ Implemented | P0 |
| FR-PRJ-005 | Image/file upload via S3 presigned URLs | ❌ Not implemented | P1 |

### 4.4 3D World System

| ID | Requirement | Status | Priority |
|----|-------------|--------|----------|
| FR-3D-001 | Database-driven world node configuration | ✅ Implemented | P0 |
| FR-3D-002 | Hotspot system (OPEN_PANEL, NAVIGATE_NODE, OPEN_URL) | ✅ Implemented | P0 |
| FR-3D-003 | GSAP camera animation transitions | ✅ Implemented | P0 |
| FR-3D-004 | Drone entry animation sequence | ✅ Implemented (needs alignment) | P1 |
| FR-3D-005 | Exterior building scene with GLB model | ✅ Implemented (needs alignment) | P1 |
| FR-3D-006 | Admin UI for world node/hotspot management | ✅ Implemented | P0 |
| FR-3D-007 | Lobby placeholder scene | ❌ Not implemented | P1 |
| FR-3D-008 | Room template (reusable for 10 categories) | ❌ Not implemented | P1 |
| FR-3D-009 | Loading progress indicator | ❌ Not implemented | P2 |
| FR-3D-010 | `S-SEMANTIC` delivery stream — a peer surface carrying the core journey without WebGL, not a fallback | ❌ Not implemented | P0 |
| FR-3D-011 | Four peer delivery streams (`S-HIGH`, `S-MEDIUM`, `S-LOW`, `S-SEMANTIC`) carrying equivalent core journeys | ❌ Not implemented | P0 |
| FR-3D-012 | Stream selection precedence per `3D_Mega_Menu_Style_Guide_v2.md` §8.2.2 (corrected D-042): WebGL ceiling, `hardwareConcurrency` tiering, `S-LOW` unsignalled default, stored measurement applied only from the next visit, reversible persisting user override that outranks stored measurement, `prefers-reduced-motion` affecting motion only | ❌ Not implemented | P0 |
| FR-3D-013 | The stream is resolved once before first paint and never changes mid-session except by the visitor's own act; that change is announced politely, does not move focus, and preserves scroll, open panel, and route (§8.2.4). **Across the semantic boundary the two shells are different subtrees, so focus does not survive on the operated element: it moves to the delivery stream control in the destination shell, which is the same control by role and name and reports the new stream** (D-045) | ❌ Not implemented | P0 |
| FR-3D-014 | The stream control is present and keyboard operable in every stream, including `S-SEMANTIC`, where it lives in the semantic shell rather than the World HUD. **It is a native radio group with a separate explicit Apply control; selection alone changes nothing, and streams above the capability ceiling are shown disabled with a stated reason rather than hidden** (D-045, `N-05`) | ❌ Not implemented | P0 |
| FR-3D-015 | The stream in force does not determine whether the World canvas is entered. The canvas is entered only on an explicit visitor action in every stream, and `ROUTE-HOME`'s first frame is a non-World shell carrying the stream control, including in `S-HIGH` (D-045, gate G-1) | ❌ Not implemented | P0 |
| FR-3D-016 | A stream change never discards booking process state — a held slot, a verified email, and entered field values survive every boundary **including the semantic one**, where process state is rehydrated into the incoming shell before that shell is announced. If it cannot be carried, the change is refused and explained under the `ACT-11` pattern and the visitor keeps their work; it is never silently reset (D-045, gate G-7) | ❌ Not implemented | P0 |

**Amended 2026-09-06 under CR-002, decision D-039.** `FR-3D-010` previously read
"WebGL fallback for unsupported devices" at priority P2. The four streams are
**peers**, so the no-WebGL surface is a core requirement, not a contingency, and
its priority rises to P0 accordingly. Stream thresholds are uncertainty **U-03**
and remain `[MUST VERIFY AT SPECIFICATION]`; no schedule is offered. Network-class
signals (`effectiveType`, `prefers-reduced-data`, `deviceMemory`) were verified
unusable and must not appear in any implementation of `FR-3D-012` — see
`docs/requirements/CR-002-signal-portability-verification.md`.

**Amended again 2026-09-06 under decision D-045.** `FR-3D-013` and `FR-3D-014` were
narrowed and `FR-3D-015`/`FR-3D-016` were added, all derived from the two accepted
delivery-stream specifications rather than authored here. Two of these close gaps
that the earlier wording left open by omission rather than by intent: `FR-3D-013`
said focus "does not move" without saying what happens when the element holding
focus ceases to exist, and nothing said whether a visitor who changes stream
mid-booking keeps their slot. An unstated answer to either question is a defect,
because implementation will supply one. `NFR-A11Y-004` continues to carry the
accessibility obligations for the control itself.

### 4.5 Lead Capture

| ID | Requirement | Status | Priority |
|----|-------------|--------|----------|
| FR-LEAD-001 | Rate-limited lead submission (per-IP) | ✅ Implemented | P0 |
| FR-LEAD-002 | Required fields: name, email | ✅ Implemented | P0 |
| FR-LEAD-003 | Optional fields: company, phone, subject, message | ✅ Implemented | P0 |
| FR-LEAD-004 | Auto-captured source URL | ✅ Implemented | P0 |
| FR-LEAD-005 | Admin lead viewer with search | ✅ Implemented | P0 |
| FR-LEAD-006 | Email notification on new lead | ❌ Not implemented | P1 |
| FR-LEAD-007 | Redis-backed distributed rate limiting | ❌ Not implemented | P1 |

### 4.6 Admin Dashboard

| ID | Requirement | Status | Priority |
|----|-------------|--------|----------|
| FR-ADM-001 | Protected admin routes with JWT | ✅ Implemented | P0 |
| FR-ADM-002 | CRUD interfaces for all content types | ✅ Implemented | P0 |
| FR-ADM-003 | Real-time form validation | ✅ Implemented | P0 |
| FR-ADM-004 | Bulk operations | ❌ Not implemented | P2 |
| FR-ADM-005 | Audit log / change history | ❌ Not implemented | Phase 2 |
| FR-ADM-006 | Image upload (currently URL-only) | ❌ Not implemented | P1 |

---

## 5. Non-Functional Requirements

### 5.1 Performance Requirements (Current Targets)

| Metric | Target | Notes |
|--------|--------|-------|
| Page load (initial) | < 3 seconds | Includes 3D asset loading |
| API response time | < 200ms | FastAPI endpoints |
| Database queries | < 100ms | SQLAlchemy with PostgreSQL |
| 3D scene transition | < 500ms | GSAP camera animations |
| Lead form submission | < 1 second | Including rate limit check |

### 5.2 Performance Requirements (Phase 3+ Enterprise Targets)

These are aspirational targets from the original SRS v2.0, preserved for future reference:

| Metric | Target | Phase |
|--------|--------|-------|
| API Gateway Response | < 100ms | Phase 3 |
| IoT Data Ingestion | 10,000 msg/sec | Phase 2 |
| Concurrent Users | 10,000 sessions | Phase 3 |
| Real-time Event Processing | 5,000 events/sec | Phase 3 |

### 5.3 Security Requirements

| ID | Requirement | Status | Priority |
|----|-------------|--------|----------|
| NFR-SEC-001 | HTTPS enforcement in production | ❌ Not implemented | P0 |
| NFR-SEC-002 | CORS restricted to allowed origins | ⚠️ Partially (overly permissive) | P0 |
| NFR-SEC-003 | JWT secret from environment (not default) | ⚠️ Configurable but not enforced | P0 |
| NFR-SEC-004 | Input validation and sanitization | ⚠️ Pydantic validation, no HTML sanitization | P1 |
| NFR-SEC-005 | Encryption at rest (AES-256) | ❌ Not implemented | Phase 2 |
| NFR-SEC-006 | Key rotation policy | ❌ Not implemented | Phase 2 |
| NFR-SEC-007 | Audit logging | ❌ Not implemented | Phase 2 |

### 5.4 Reliability Requirements

| Metric | Current | Phase 3+ Target |
|--------|---------|-----------------|
| Availability | No SLA (single instance) | 99.9% uptime |
| Backup | No automated backups | Daily, 30-day retention |
| Disaster Recovery | None | RTO < 4 hours |

### 5.5 Scalability Requirements

| Dimension | Current Capacity | Phase 3+ Target |
|-----------|-----------------|-----------------|
| Concurrent users | ~100 (single process) | 10,000+ |
| Database size | < 1 GB | 1 TB/month growth |
| IoT devices | 0 (not implemented) | 100,000 |
| API throughput | ~200 req/sec (est.) | 1,000 req/sec per service |

### 5.6 Accessibility Requirements

*Added 2026-09-06 under D-043. The SRS carried no accessibility non-functional
requirement, so the WCAG 2.2 Level AA target held by the UI reference-design
package had no requirement-level home and nothing to trace to. No current
conformance is claimed; every row below is unimplemented.*

| ID | Requirement | Status | Priority |
|----|-------------|--------|----------|
| NFR-A11Y-001 | WCAG 2.2 Level AA for every full page and every complete process, including represented third-party steps | ❌ Not implemented | P0 |
| NFR-A11Y-002 | Conformance holds independently within each delivery stream `S-HIGH`, `S-MEDIUM`, `S-LOW`, `S-SEMANTIC`; aggregate evidence does not satisfy it, and contrast, focus order, and target size are measured against each stream's own rendering | ❌ Not implemented | P0 |
| NFR-A11Y-003 | `S-SEMANTIC` is a peer delivery stream carrying the equivalent core journey, never an error surface and never a fallback | ❌ Not implemented | P0 |
| NFR-A11Y-004 | The delivery stream control is present, discoverable, and keyboard operable in every stream, reports its current value in its accessible name, and advises before it acts. **The advisement is visible text adjacent to the control, not an accessible description alone** (D-045, `N-06`), because a description exposed only to assistive technology leaves the sighted keyboard user, the low-vision user at 400% zoom, and the cognitively loaded user unwarned (see `FR-3D-014`) | ❌ Not implemented | P0 |
| NFR-A11Y-005 | Every interactive 3D state carries a non-colour, non-motion cue and a persistent keyboard focus indicator at ≥3:1 against every adjacent scene colour | ❌ Not implemented | P0 |
| NFR-A11Y-006 | `prefers-reduced-motion` suppression is exhaustive and normative; anything not enumerated continues to run | ❌ Not implemented | P1 |
| NFR-A11Y-007 | Independent accessibility review before any phase acceptance; the producer does not approve their own output (Constitution 2.0.0 §VII) | ❌ Not implemented | P0 |

> Verification for every row is deferred to implementation. These are
> requirements on the built system, not claims about the current one.

---

## 6. Technical Requirements

### 6.1 Frontend

| Technology | Version | Purpose |
|------------|---------|---------|
| React | 18 + TypeScript | Core UI framework |
| Vite | Latest | Build tooling and dev server |
| TailwindCSS | Latest | Utility-first styling |
| React Router | v6 | Client-side routing |
| Zustand | Latest | State management |
| React Three Fiber | @react-three/fiber + drei | 3D rendering engine |
| GSAP | Latest | Camera animation sequences |
| Three.js | Via R3F | WebGL 3D rendering |

### 6.2 Backend

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.11+ | Core language |
| FastAPI | Latest | REST API framework |
| SQLAlchemy | 2.0 (Mapped types) | ORM with async support |
| Alembic | Latest | Database migrations |
| PostgreSQL | 16 (Docker) | Primary database |
| bcrypt + PyJWT | Latest | Authentication |
| pytest + httpx | Latest | API testing |

### 6.3 Infrastructure (Current)

| Technology | Status | Purpose |
|------------|--------|---------|
| Docker Compose | Implemented | Local PostgreSQL |
| AWS S3 + CloudFront | Planned | Static assets and CDN |
| AWS ECS/EC2 | Planned | API deployment |
| GitHub Actions | Planned | CI/CD pipeline |

---

## 7. Data Requirements

### 7.1 Database Schema

Six primary tables in PostgreSQL:

1. **users** — Admin authentication (UUID PK, email, password_hash, role, is_active)
2. **services** — Service listings (UUID PK, slug, title, category, summary, body, deliverables[], tags[], is_featured, sort_order)
3. **projects** — Portfolio items (UUID PK, slug, title, summary, body, tags[], is_featured, sort_order)
4. **project_media** — Media attachments (UUID PK, project_id FK, type, url, caption, sort_order)
5. **world_nodes** — 3D scene nodes (UUID PK, key, title, camera_position{}, camera_target{}, camera_fov, environment{})
6. **world_hotspots** — Interactive points (UUID PK, node_id FK, key, kind, position{}, payload{})
7. **leads** — Contact form submissions (UUID PK, name, email, company, phone, message, source_url, metadata{})

### 7.2 Data Integrity

- Unique constraints on slugs (services, projects) and keys (world_nodes)
- Composite unique constraint on (node_id, key) for hotspots
- Cascade deletes: projects → project_media, world_nodes → world_hotspots
- UUID primary keys throughout

### 7.3 Data Lifecycle (Current)

- Active data retention: Indefinite (no purge policy)
- Backups: Manual only (Docker volume)
- Archive: Not implemented
- Export: Not implemented

---

## 8. Interface Requirements

### 8.1 User Interfaces

1. **Immersive 3D Experience** (`/world`)
   - Full-viewport Three.js canvas
   - Cinematic drone entry animation
   - Interactive hotspot navigation
   - Content panels (services, projects, contact form)

2. **Admin Dashboard** (`/admin`)
   - Protected login page
   - CRUD interfaces for all content types
   - JSON editors for complex fields
   - Sort ordering controls

3. **Home Page** (`/`)
   - Landing page with entry to 3D experience

### 8.2 API Interfaces

- REST API served by FastAPI at port 8000
- Public endpoints: GET-only for services, projects, world, health
- Admin endpoints: Full CRUD with JWT Bearer authentication
- Lead endpoint: Rate-limited POST
- See `API_Reference.md` for complete specification

---

## 9. Service Taxonomy v2.0

The platform delivers 10 service categories, each mapping 1:1 to a 3D world room:

1. Strategy & Architecture
2. Platform & Product Engineering
3. AI Systems & Agentic Automation
4. Spatial Computing & Immersive Platforms
5. Product Design & Experience Engineering
6. Cloud, DevOps & Platform Reliability
7. Security, Privacy & Trust Engineering
8. Data Platforms & Analytics
9. Commerce, Content & Growth Platforms
10. Creative & Visual Design Services (NEW — to be added)

Full service taxonomy details are in `Hengshi_Design_Project_Consolidation_v3.docx`, Section 3.

---

## 10. Constraints

### 10.1 Technical Constraints
- Single-developer capacity (project-basis hiring as needed)
- No dedicated DevOps infrastructure yet
- 3D asset pipeline dependent on Blender modeling
- WebGL compatibility limitations on older devices

### 10.2 Business Constraints
- Bootstrap-funded development
- Phased delivery to manage scope
- Market timing pressure for initial launch

---

## 11. Future Requirements (Phase 2–5)

Requirements from the original SRS v1.0/v2.0 that remain valid for future phases:

### Phase 2: IoT & Data Platform
- MQTT device communication (EMQX broker)
- TimescaleDB for time-series telemetry
- Device management: registration, provisioning, monitoring
- Real-time data pipeline with event streaming

### Phase 3: Multi-Tenant Enterprise
- Multi-tenant architecture with row-level security
- Organization management with hierarchical roles
- Billing and subscription management (Stripe)
- Service module marketplace

### Phase 4: AI & Advanced Analytics
- AI-powered design generation
- Predictive analytics for IoT device health
- Natural language data query interface
- Data monetization APIs

### Phase 5: Scale & Optimization
- Kubernetes orchestration
- Global CDN and edge computing
- SOC 2 compliance readiness
- Mobile application (React Native)

---

## Appendices

### Appendix A: Traceability to Consolidation Document
All requirements in this SRS trace to sections in `Hengshi_Design_Project_Consolidation_v3.docx`:
- Sections 4–5 → Technical stack and architecture
- Section 6 → Implementation status and gap analysis
- Section 7 → Technology additions by phase
- Section 8 → Sprint roadmap

### Appendix B: Change History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | Feb 2025 | Zaryab | Initial SRS for Angular/Django/MongoDB architecture |
| 2.0 | Feb 2025 | Zaryab | Added detailed performance metrics, IoT requirements |
| 3.0 | Feb 2026 | Zaryab | Complete rewrite for React/FastAPI/PostgreSQL monorepo; aligned with consolidation v3 |
