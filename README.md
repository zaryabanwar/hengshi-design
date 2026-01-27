# Hengshi Design - Immersive Web Platform

Monorepo scaffold for a cinematic portfolio website with a FastAPI backend and shared schemas.

## Repo Layout
- apps/web - React + Vite + Tailwind + React Router + Zustand
- apps/api - FastAPI backend (SQLAlchemy 2.0 + Alembic)
- packages/shared - shared zod schemas/types
- docs - spec and backlog
- docker-compose.yml - local Postgres

## Prerequisites
- Node 18+
- Python 3.11+
- Docker Desktop with Docker Compose

## Local Development (Windows PowerShell)

### 1) Start Postgres
```powershell
docker compose up -d db
```

### 2) Run the API
```powershell
cd apps/api
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Create local env file once, then edit as needed:
Copy-Item .env.example .env
notepad .env

# If you have not applied the latest migrations (including Leads), run this:
alembic upgrade head

python -m app.scripts.create_admin
python -m app.scripts.seed_services  # Optional if already seeded
python -m app.scripts.seed_projects
python -m app.scripts.seed_world
uvicorn app.main:app --reload --port 8000
```
You can also run `apps/api/run.ps1` after activating the venv.

### 3) Run the web app
```powershell
cd apps/web
npm install
npm run dev
```

## Assets
- Place 3D assets in `apps/web/public/models` so they can be served directly by Vite.
- Exterior HQ GLB: `apps/web/public/models/hengshi-hq-atlanta-exterior-web.glb`

## URLs
- Web: http://localhost:5173
- API health: http://127.0.0.1:8000/health
- Swagger: http://127.0.0.1:8000/docs
- Services list: http://127.0.0.1:8000/api/services
- Projects list: http://127.0.0.1:8000/api/projects
- Leads list (admin): http://127.0.0.1:8000/api/admin/leads
- World data: http://127.0.0.1:8000/api/world

## Migrations (Alembic)
Run from `apps/api` (ensure `.env` exists):
```powershell
alembic revision -m "init"
alembic upgrade head
```
Note: The initial migration is already in `apps/api/alembic/versions/7310fda60e45_init.py`. Use a new message for additional revisions.

## Tests (API)
```powershell
cd apps/api
.\.venv\Scripts\Activate.ps1
pytest
```

## Shared package (optional)
```powershell
cd packages/shared
npm install
npm run build
```

## Status
- Prompt 1 (monorepo scaffold) done
- Prompt 2 (DB + Alembic + tests) done
- Prompt 3 (JWT auth) done
- Prompt 4 (services CRUD) done
- Prompt 5 (projects CRUD) done
- Prompt 6 (leads) done
