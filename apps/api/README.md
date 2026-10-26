# Hengshi Design API — protected prototype notes for v1

The [root native-operation guide](../../README.md#native-local-operation-on-windows)
is the current startup entry point. Docker is not required. Reuse the configured
local PostgreSQL cluster and existing Python environment; keep credentials local
and confirm port/process ownership before binding. Current application code stays
protected while [Phase 1 definition](../../docs/software-definition/README.md)
is completed and approved.

`run.ps1` only activates the environment. Explicitly run Uvicorn from `apps/api`
with the existing virtual-environment interpreter once database/configuration and
port checks pass. A successful `/health` response does not verify a database query:
see `app/main.py`. An absent `DATABASE_URL` selects the unsafe SQLite fallback in
`app/db/session.py` (R-005); do not claim that as native PostgreSQL operation.
Process environment can override `.env`; do not print either's secret values.

The verified 2026-10-04 walkthrough uses the existing user-owned PostgreSQL 17.4
cluster at `%LOCALAPPDATA%\HengshiDesign\postgres-walkthrough\data`, not the stopped
Program Files service. The machine-local runtime profile selects `hengshi` on
`127.0.0.1:5432` with the same existing credentials. API 8001 and web 5173 were
verified together; port 8000's WSL relay was left untouched. Root instructions
show process-local database/frontend overrides without modifying `.env` files.
Health, public World/service reads and the browser's existing-account sign-in to
`/admin/services` returned successful responses. These observations do not prove
schema currency, other admin workflows, role denial, free movement or readiness.

The same native setup was rechecked on 2026-10-09: a read-only identity transaction
confirmed `hengshi` on PostgreSQL 17.4, public reads succeeded, and the existing
account reached the settled nine-record Services page without page errors.
The [root guide](../../README.md#4-verify-the-actual-journey) owns the current
inspection links and limits. Existing prototype records are not the accepted v1
taxonomy; no schema, seed, account or dependency change was made by this restart.

Migrations, database/role creation, administrator creation, account resets and
seed scripts are data mutations, not routine startup. They require the applicable
explicit approval and a verified database target. Do not overwrite an existing
`.env` with `.env.example`. Run database-writing tests only on the approved isolated
test database after inspecting their actual fixtures; do not infer safety from a
command being named `pytest`.

The original authentication examples below are historical illustrations, not
verified credentials or authorization evidence. R-004 remains open:
`app/auth/deps.py` currently does not enforce an administrator role in
`require_admin`. Sign-in and admin-page visibility cannot prove the intended
production permission model. The approved staff roles/identity extension remains
definition scope until separately authorized implementation.

## Preserved scaffold snapshot

Read the original instructions below through the current boundaries above. They
do not authorize migrations, seeding, credential changes or full project launch.

# API Notes

All commands below are Windows PowerShell and should be run from `apps/api`.

## Quickstart (PowerShell)
```powershell
cd apps/api
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
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

## Migrations (Alembic)
```powershell
alembic revision --autogenerate -m "create users"
alembic upgrade head
```
Note: The initial migration is in `apps/api/alembic/versions/7310fda60e45_init.py`.

## Tests
Tests live in `apps/api/tests`.
```powershell
pytest
```

## Endpoints
- Health: http://127.0.0.1:8000/health
- Swagger: http://127.0.0.1:8000/docs
- Services list: http://127.0.0.1:8000/api/services
- Projects list: http://127.0.0.1:8000/api/projects
- World data: http://127.0.0.1:8000/api/world

## Quick auth check (PowerShell)
```powershell
$login = Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/api/auth/login `
  -ContentType "application/json" `
  -Body '{"email":"admin@example.com","password":"ChangeMe123!"}'

$token = $login.access_token
Invoke-RestMethod -Uri http://127.0.0.1:8000/api/admin/me -Headers @{ Authorization = "Bearer $token" }
```

## Services + Projects (PowerShell)
```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/api/services
Invoke-RestMethod -Uri http://127.0.0.1:8000/api/projects
```

## World data (PowerShell)
Seed the world nodes/hotspots:
```powershell
python -m app.scripts.seed_world
```
Fetch the world data:
```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/api/world
```
Note: Camera positions and hotspot coordinates are placeholders for now and will be tuned with the 3D scene.

## Leads (PowerShell)
Submit a lead:
```powershell
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/api/leads `
  -ContentType "application/json" `
  -Body '{
    "name": "Ada Lovelace",
    "email": "ada@example.com",
    "company": "Analytical Engines",
    "phone": "+1-555-0100",
    "subject": "Project inquiry",
    "message": "We need a platform rebuild for a new product launch.",
    "source_url": "https://hengshi.design/contact",
    "metadata": { "user_agent": "PowerShell" }
  }'
```

View leads as admin:
```powershell
$login = Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/api/auth/login `
  -ContentType "application/json" `
  -Body '{"email":"admin@example.com","password":"ChangeMe123!"}'

$token = $login.access_token
Invoke-RestMethod -Uri http://127.0.0.1:8000/api/admin/leads -Headers @{ Authorization = "Bearer $token" }
```
