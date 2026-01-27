# Hengshi Design - Immersive Web Platform Spec (MVP)

## Current Implementation Status
- Completed: monorepo scaffold, Postgres compose, FastAPI health route, SQLAlchemy 2.0 base/session, Alembic config with init migration, API pytest, service taxonomy + shared schemas.
- Not implemented yet: auth, business models, CRUD APIs, R3F scenes, admin UI.

## Purpose
Build an Unseen-style immersive WebGL website for hengshidesign.com: a 3D virtual building where each room represents a service. Visitors navigate between rooms via smooth camera transitions and interact with hotspots that open content panels (projects, services, contact). Backend supports a small CMS for managing content and world configuration.

## Goals (MVP)
- Immersive 3D world (building) with camera transitions between scene nodes (rooms).
- Hotspots in rooms open overlay panels for Services, Projects, and Contact.
- Projects page with filtering and project detail panel.
- Contact flow saves leads to DB.
- Admin login + CRUD for Projects and Services + World nodes/hotspots.
- Media upload to S3 via presigned URLs (MVP can be local storage if needed, but target S3).

## Non-goals (MVP)
- Full FPS movement / collision walking.
- Payments.
- Chat/real-time.
- Multi-tenant.
- AI features.

---

## Tech Stack

### Current (Prompt 1-2)
- React 18 + TypeScript
- Vite
- TailwindCSS
- React Router
- Zustand
- FastAPI
- SQLAlchemy 2.0
- Alembic
- PostgreSQL
- Docker + Docker Compose

### Planned additions
- Three.js via React-Three-Fiber
- @react-three/drei
- GSAP (camera + UI transitions)
- JWT authentication (admin)
- Optional S3 integration for assets
- CI/CD + cloud deployment

## Service taxonomy (v1 - 2026)

CATEGORY 1 - Strategy & Architecture
Offerings:
- Digital transformation strategy & roadmaps
- Technical discovery workshops (product/tech)
- Solution architecture & system design
- Platform selection & vendor evaluation
- Technology due diligence (for acquisitions / procurement)
- Risk assessment (technical, operational, delivery)

CATEGORY 2 - Platform & Product Engineering
Offerings:
- Web application development (React/Next, APIs)
- Mobile application development (cross-platform + native)
- SaaS product engineering (multi-tenant, subscriptions)
- API platforms & integrations (REST/GraphQL, third parties)
- Legacy modernization & re-platforming
- Microservices & event-driven systems
- Performance engineering & scalability hardening

CATEGORY 3 - AI Systems & Agentic Automation
Offerings:
- LLM app development (RAG, tools, workflows)
- Agentic systems (multi-agent orchestration, task automation)
- Private/secure AI deployment (VPC/on-prem, data isolation)
- AI evaluation & quality (benchmarks, red teaming, monitoring)
- AI governance & guardrails (policy, safety layers, auditability)
- NLP and document intelligence (classification, extraction)
- Computer vision pipelines (inspection, OCR+vision, automation)
- Automation with RPA + AI (back-office workflows)

CATEGORY 4 - Spatial Computing & Immersive Platforms
Offerings:
- WebGL experiences (Three.js/R3F) for brand + product
- Virtual buildings/showrooms (interactive tours)
- Digital twins (real estate / facilities / industrial)
- AR/VR prototypes and production apps
- Spatial UX design (navigation, interaction, hotspots)
- Real-time 3D optimization (performance + assets pipeline)

CATEGORY 5 - Product Design & Experience Engineering
Offerings:
- Product UX strategy & user journeys
- UI/UX design for web/mobile
- Design systems (tokens, components, guidelines)
- Prototyping (high-fidelity interactive prototypes)
- Motion design & micro-interactions
- UX audits & usability testing
- Brand identity for digital products (premium positioning)

CATEGORY 6 - Cloud, DevOps & Platform Reliability
Offerings:
- Cloud architecture (AWS-focused) & migration planning
- CI/CD pipelines and release automation
- Infrastructure as Code (Terraform/CDK)
- Containerization & orchestration (Docker/K8s)
- Observability (logging/metrics/tracing) & alerting
- SRE practices (incident response, SLIs/SLOs)
- Cost optimization (FinOps) & performance tuning

CATEGORY 7 - Security, Privacy & Trust Engineering
Offerings:
- Secure architecture & threat modeling
- Secure SDLC (code scanning, secrets, policies)
- Zero-trust and IAM hardening
- Pen testing coordination + remediation engineering
- Compliance readiness (ISO27001-style controls mapping)
- Data protection & privacy engineering
- AI security (prompt injection defense, data leakage prevention)

CATEGORY 8 - Data Platforms & Analytics
Offerings:
- Data engineering pipelines (ELT/ETL, orchestration)
- Analytics & BI (dashboards, KPI frameworks)
- Data warehouses/lakes (architecture + implementation)
- Data governance (quality, lineage, access control)
- Real-time streaming & event analytics
- AI-ready data preparation (feature stores optional)

CATEGORY 9 - Commerce, Content & Growth Platforms
Offerings:
- E-commerce builds (headless or traditional)
- Payments, subscriptions, invoicing integrations
- CMS builds & migrations (headless CMS + workflows)
- SEO technical foundations + performance
- Growth analytics (events, funnels, attribution)
- CRM/marketing automation integrations (HubSpot etc.)

## Service model (MVP fields)
- id (uuid, server-generated)
- slug (kebab-case, unique)
- title
- category (one of ServiceCategory)
- summary (short)
- body (markdown or rich text)
- deliverables (string[])
- tags (string[])
- is_featured (boolean)
- sort_order (number)
- created_at, updated_at (server timestamps)

## Room mapping (services -> world nodes)
Each ServiceCategory maps 1:1 to a world node/room key:
- `strategy_architecture`
- `platform_engineering`
- `ai_systems`
- `spatial_immersive`
- `product_design`
- `cloud_devops`
- `security_trust`
- `data_platforms`
- `commerce_growth`

Hotspots in each room open a Service panel filtered by category.

---

## UX Flow

### Entry
1. Landing screen with Enter (and Enter without audio).
2. Clicking Enter triggers a transition into the world (camera animation / shader-like wipe).
3. User lands in the Index node (reception scene).

### Navigation
- Primary nav: Index / Projects / Contact / World
- Changing route triggers a scene transition, not a hard reload.

### World Experience
- World consists of Nodes (rooms). Each node has:
  - camera position, target, fov
  - environment preset (lighting/postprocessing)
  - ambient audio preset
  - hotspots array

### Hotspots
- 3D icons anchored at world coordinates.
- Hover: pulse + cursor change
- Click actions:
  - OPEN_PANEL (service/project/contact/insight)
  - NAVIGATE_NODE (move to another room)
  - OPEN_URL (external; should open new tab)
- UI overlay panel slides in; background stays interactive but input may be locked during panel open.

---

## Routes
- / Landing (enter gate)
- /world World mode (default node index)
- /projects Projects list (can still be within world or flat overlay)
- /contact Contact room / contact overlay
- /admin Admin SPA
- /admin/login Admin login
- /admin/* Admin CRUD sections

---

## Data Model (MVP)
### Public Content
- Services
- Projects
- ProjectMedia
- Insights (optional in MVP)
- WorldNodes
- WorldHotspots
- Assets

### Leads
- Leads (contact submissions)

### Admin
- Users (admin/editor)

---

## Backend APIs (planned MVP)
### Public
- GET /api/world
- GET /api/services
- GET /api/services/{id}
- GET /api/projects
- GET /api/projects/{id}
- POST /api/leads

### Auth/Admin
- POST /api/auth/login
- GET /api/admin/me
- CRUD /api/admin/services
- CRUD /api/admin/projects
- CRUD /api/admin/world/nodes
- CRUD /api/admin/world/hotspots
- POST /api/admin/assets/presign (S3 upload URL)
- GET /api/admin/leads

---

## Frontend Architecture
- 3D Engine (R3F): renders scene, camera, hotspots.
- UI Overlay: nav, panels, forms.
- State: Zustand stores:
  - worldStore (currentNode, transitionState, selectedHotspot)
  - uiStore (activePanel, panelData, audioEnabled, loading)
- Transitions: GSAP timeline, optional shader-like full-screen overlay.

---

## Performance Requirements
- Lazy-load heavy assets (GLB rooms, textures).
- Use DRACO/meshopt compressed GLB where possible.
- Use KTX2/Basis for textures (phase 2).
- FPS target: 45-60 desktop, 30+ mobile.
- Provide fallback: if WebGL fails, show flat mode pages (projects/contact).

---

## Security (planned)
- Rate limit POST /leads
- Validate and sanitize inputs
- Admin JWT auth
- CORS locked to allowed domains in production
