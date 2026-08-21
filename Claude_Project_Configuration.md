# Hengshi Design — Claude Project Configuration

## PROJECT DESCRIPTION
(Paste this into the project description field at the top of your Claude project)

---

Hengshi Design Digital Platform — an immersive 3D web portfolio and service delivery ecosystem built with React 18, React Three Fiber, FastAPI, and PostgreSQL. The platform transforms Hengshi Design from a traditional service provider into a platform-oriented company serving agriculture, defense, and mining markets through 10 integrated service categories with IoT management capabilities (Phase 2+) and multiple revenue models including PaaS subscriptions, data monetization, and custom consulting.

Current state: Monorepo architecture at ~40% overall readiness. Core platform (auth, CRUD, API, 3D world system) is 90% complete. Security hardening, testing, monitoring, and deployment are the immediate priorities across 5 planned sprints.

---

## PROJECT INSTRUCTIONS
(Paste this into the Instructions field in your Claude project)

---

Hengshi-Platform Project Blueprint

1. Business Vision and Objectives

Transformative Vision: Evolve Hengshi Design from a traditional service provider into a modern, platform-oriented company. The platform serves as a comprehensive digital ecosystem that actively supports and delivers a full range of service areas through an immersive 3D building experience.

Core Objectives:
- Deliver 10 service categories through an interactive 3D virtual building where each room represents a service area
- Enable interactive management and monitoring of IoT devices (Phase 2+)
- Support recurring revenue models through managed services, data monetization, and custom consulting
- Position Hengshi Design as an innovative leader in digital transformation and IoT solutions

2. Current Architecture

Technology Stack (Implemented):
- Frontend: React 18 + TypeScript, Vite, TailwindCSS, React Router v6, Zustand
- 3D Engine: React Three Fiber (@react-three/fiber + drei), GSAP, Three.js
- Backend: FastAPI (Python 3.11+), SQLAlchemy 2.0, Alembic, PostgreSQL 16
- Auth: JWT (PyJWT) + bcrypt password hashing
- Infrastructure: Docker Compose (local), AWS planned (S3, CloudFront, ECS)
- Monorepo: apps/api/, apps/web/, packages/shared/, docs/

Implementation Status (~40% overall):
- Core Platform (Auth, CRUD, API): 90% complete
- 3D Immersive Frontend: 60% complete (entry sequence built, needs spatial alignment)
- Admin Dashboard: 85% complete (full CRUD, needs polish)
- Security Hardening: 30% complete (JWT works, rate limiting/CORS gaps)
- Testing: 20% complete (backend happy paths only, 0% frontend)
- Monitoring & Logging: 10% (not implemented)
- CI/CD & Deployment: 5% (Docker Compose local only)

3. Service Taxonomy v2.0 (10 Categories)
1. Strategy & Architecture
2. Platform & Product Engineering
3. AI Systems & Agentic Automation
4. Spatial Computing & Immersive Platforms
5. Product Design & Experience Engineering
6. Cloud, DevOps & Platform Reliability
7. Security, Privacy & Trust Engineering
8. Data Platforms & Analytics
9. Commerce, Content & Growth Platforms
10. Creative & Visual Design Services (NEW — to be added Sprint 4)

4. Sprint Roadmap (Next 10 Weeks)
- Sprint 1 (Weeks 1-2): Security hardening — login rate limiting, JWT secret enforcement, httpOnly cookies, CORS restriction, password complexity, input sanitization
- Sprint 2 (Weeks 3-4): Testing & monitoring — structured logging, frontend tests, CI pipeline, Redis rate limiting
- Sprint 3 (Weeks 5-6): 3D experience completion — Blender coordinates, lobby scene, room template, WebGL fallback
- Sprint 4 (Weeks 7-8): Design services & content — Category 10 seed data, S3 uploads, asset optimization
- Sprint 5 (Weeks 9-10): AWS deployment & launch — S3/CloudFront/ECS, production DB, domain/SSL

5. Project Documentation (17 Active Files in Project Knowledge)
Core docs: Consolidation v3 (DOCX), SPEC.md, BACKLOG.md
Technical reference: SRS v3, SAD v3, Requirements Mapping v3, API Reference, Security Hardening Plan, 3D Mega Menu Style Guide v2
Architecture diagrams: 7 current-state mermaid files (System Architecture, Database Schema, 3D World System, Authentication Flow, Frontend Architecture, API Router Structure, Deployment Pipeline)
See Documentation_Index.md for complete catalog.

6. Development Approach
- IT Consulting Operations skill framework for all project decisions and documentation
- Agile methodology with 2-week sprints
- Project-basis hiring as needed (solo developer capacity)
- All outputs in DOCX/PDF/Markdown formats

7. Key Constraints
- Solo developer capacity (project-basis hiring as needed)
- Bootstrap-funded development
- 3D asset pipeline dependent on Blender modeling
- WebGL compatibility limitations on older devices
- Market timing pressure for initial launch

---

## MEMORY NOTES
(These should already be in your Claude memory — verify they match current state)

Key facts Claude should remember:
- Zaryab owns Hengshi Design, a software company
- Solo consultant providing system design, architecture, and technical consulting
- Platform underwent strategic pivot from Angular/Django/MongoDB microservices to React/FastAPI/PostgreSQL monorepo
- IT Consulting Operations skill framework is the operational backbone
- Platform at ~40% readiness, security hardening is next priority
- 10 service categories (9 seeded + Category 10 Creative & Visual Design pending)
- Phased approach: current focused build → IoT (Phase 2) → Multi-tenant (Phase 3) → AI (Phase 4) → Scale (Phase 5)
