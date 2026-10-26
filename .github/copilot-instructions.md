# Hengshi Design - Copilot Instructions

## Required Starting Point

Before changing this repository, read these files in order:

1. `AGENTS.md`
2. `.specify/memory/constitution.md`
3. `PROJECT.md`, `DECISIONS.md`, `PROJECT_STATE.yaml`, and `TASKS.md`
4. `docs/software-definition/README.md`
5. The relevant approved feature spec under `specs/`
6. For Spec Kit features, the active `spec.md`, `research.md`, `data-model.md`,
   contracts, `plan.md`, and `tasks.md` where those files exist

Do not bypass the approval gates in
`docs/software-definition/03-autonomous-ai-development-workflow.md`.

## Binding Workflow Gates

- Product scope, auth, security, infrastructure, API/data/AI/publication contracts,
  app structure, and repo-structure changes require approved definition and Spec
  Kit artifacts for the assigned increment before code. D-097 supersedes the
  whole-Phase-1 build gate: brand/shared foundations, complete 2D platform, full
  3D World, then launch. Unfinished future 3D work does not block unrelated 2D.
- One work chat delivers one founder-assigned outcome, reports and stops.
  Independently review material design batches, requested reviews and changes
  touching money/security/external systems. No routine review of each prose edit.
  No hard revision cap: safe in-scope fixes continue; repeated failures require
  changed diagnosis and only genuine material choices need founder input.
- Production UI work must reference a Stitch or Figma screen before
  implementation.
- Version-sensitive framework/library/API/cloud work must use Context7 plus
  official primary sources, evaluate coupled components as a graph, and select
  only newest mutually compatible stable versions. Preview/beta/RC/nightly
  dependencies cannot be production requirements.
- This first product and current definition are v1 (D-069). Keep factual package,
  API/schema and historical evidence identifiers accurate. Individually newest
  releases are observations, not a selected stack; resolve, test and lock the
  latest mutually compatible stable graph across all coupled tools and runtimes.
- D-068 defers deployment/provider/region/cost planning: Azure and AWS are
  candidates; prefer lowest feasible cost/free services when planning resumes.
  Retain Outlook/Teams without assuming Microsoft 365 is required or that each
  needed API capability is available on a free/personal account.
- D-070 targets Europe first without implying a European office. Company facts
  are admin-editable reviewed content; separate privacy/security aliases are
  founder-approved but their operation is not verified.
- Product tests exercise actual behavior. Documentation phrase/count/hash guards
  and isolated schema checks are separate artifact evidence, not runtime proof.
- Frontend UI/UX changes require Playwright verification for changed routes and
  states.
- Branches, Git commits/pushes/PRs, migrations, remotes, paid activations,
  credential changes, external design writes, deployments, and irreversible
  actions need explicit applicable approval.

## Architecture Overview

**Protected prototype:** the current code and exterior GLB are evidence, not
production design or version authority. The approved target retains two
deployables: a React/Vite frontend and modular FastAPI monolith.

- `apps/api/` - FastAPI, SQLAlchemy, Alembic, PostgreSQL, JWT/bcrypt, and Entra
  staff identity on the approved dated compatibility matrix.
- `apps/web/` - React, TypeScript, Vite, TailwindCSS, React Router, Zustand,
  React Three Fiber, and Three.js on the approved dated compatibility matrix.
- `packages/shared/` - optional shared TypeScript types/schemas.
- `docs/` - approved product definitions plus preserved historical evidence.
- `specs/` - approved feature-level Spec Kit artifacts; drafts are not authority.

## Local Commands

```powershell
# API tests
npm run test

# Frontend build
cd apps/web
npm run build

# Browser checks
npm run test:e2e
npm run qa:axe
npm run qa:lighthouse
```

## Starting Local Environment

```powershell
# Database: use the approved native PostgreSQL instance, without Docker.
# Confirm the project database and current service state before startup changes.

# Terminal 2: API
cd apps/api
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --port 8000

# Terminal 3: web
cd apps/web
npm run dev
```

Database migration is deliberately omitted from generic startup. If the current
schema is not ready, stop and obtain the explicit migration approval, validate the
exact project-scoped PostgreSQL target, backup/recovery path, and migration plan
before running any Alembic mutation.
The founder requires native local operation; historical Docker instructions do
not authorize restoring images/data or changing an existing database service.

## Backend Patterns

- Database sessions come from `app.db.session.get_db`.
- SQLAlchemy models live under `app/models/` and inherit from
  `app.db.base.Base`.
- Admin routes must use `require_admin` or a stricter dependency.
- JWT helpers live in `app/auth/jwt.py`; password helpers live in
  `app/auth/password.py`.
- Request/response schemas live in `app/{domain}/schemas.py`.
- Use FastAPI's generated Swagger docs at `http://127.0.0.1:8000/docs` when
  validating API behavior.

## Frontend Patterns

- Routes are defined in `apps/web/src/App.tsx`.
- API calls go through `apps/web/src/lib/api.ts`.
- Global client state uses Zustand in `apps/web/src/store/` or
  `apps/web/src/stores/`.
- 3D assets live in `apps/web/public/models/`.
- Do not remove TailwindCSS or replace the approved technology families without
  founder approval. Exact versions come from the dated compatibility matrix and
  reproducible locks.

## Security Notes

- Do not copy secrets from `%APPDATA%\Code\User\mcp.json`, `.env`, or local
  machine config into docs, code comments, or chat.
- Current security-hardening work is tracked under
  `specs/001-platform-security-hardening/`.
- If auth behavior changes, update `docs/active/API_Reference.md` and relevant
  tests in the same change set.
