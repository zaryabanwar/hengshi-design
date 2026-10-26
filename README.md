# Hengshi Design — v1 system definition and protected prototype

D-097 approves incremental v1 delivery. Start with [AGENTS.md](AGENTS.md),
[PROJECT.md](PROJECT.md), [DECISIONS.md](DECISIONS.md),
[the reconciliation map](docs/software-definition/04-reconciliation-map.md) and
[the visual walkthrough](docs/software-definition/definition-walkthrough.html).
The existing web/API and Atlanta model are protected prototype evidence, not the
accepted production site. Deliver brand/shared foundations, the complete 2D
platform, then the full 3D World and launch qualification. Each assigned increment
needs its relevant definition/design/contract/compatibility approval; unfinished
future 3D work is not a universal blocker. Commits and pushes remain deferred.

## Native local operation on Windows

Docker is not required. Reuse the installed native PostgreSQL service/cluster,
Python environment and Node dependencies. Select production upgrades only through
the latest mutually compatible stable matrix; the prototype's installed versions
and the old Node/Python minimums below do not select that matrix. Redis belongs to
the future approved ephemeral architecture, but this prototype has no Redis-backed
availability/handoff implementation. An unrelated listener on 6379 is not proof of
an operating Hengshi presence service.

### 1. Inspect ownership and readiness before starting

From the repository root in PowerShell:

```powershell
Get-Service -Name '*postgres*' -ErrorAction SilentlyContinue
Get-NetTCPConnection -State Listen -ErrorAction SilentlyContinue |
  Where-Object LocalPort -in 5432,5173,8000,8001,8766 |
  Select-Object LocalAddress,LocalPort,OwningProcess
```

Verify the selected listener/process belongs to this project before reusing or
stopping it. A WSL relay can expose another application's port. Do not terminate
it, shut down WSL, or reset an existing database to clear a port conflict.

Keep `apps/api/.env` and any process-level overrides machine-local. Verify that
`DATABASE_URL` selects the intended local PostgreSQL database, and that required
JWT configuration exists, without printing credentials or connection strings.
`app/db/session.py` currently defaults to SQLite when the URL is absent (R-005);
refuse that fallback for the PostgreSQL walkthrough. `load_dotenv` leaves existing
process environment values in force, so reviewing the file alone is insufficient.
Never copy the example environment file over an existing configured environment.

### 2. Start the existing PostgreSQL cluster

The verified walkthrough cluster on this machine is the existing PostgreSQL 17
data directory under `%LOCALAPPDATA%\HengshiDesign\postgres-walkthrough\data`.
The installed `postgresql-x64-17` service points at a different directory under
Program Files; it is not this cluster. Starting that service failed from the
current non-administrative Windows token. Codex authorization does not grant a
Windows administrator token. Do not recreate its directory or change permissions
to make it serve as the walkthrough database.

First inspect the verified cluster and port ownership:

```powershell
$walkthroughRoot = Join-Path $env:LOCALAPPDATA 'HengshiDesign\postgres-walkthrough'
$walkthroughData = Join-Path $walkthroughRoot 'data'
& 'C:\Program Files\PostgreSQL\17\bin\pg_ctl.exe' status -D $walkthroughData
& 'C:\Program Files\PostgreSQL\17\bin\pg_isready.exe' -h 127.0.0.1 -p 5432
```

If that cluster is stopped and port 5432 is free, start the existing data directory:

```powershell
& 'C:\Program Files\PostgreSQL\17\bin\pg_ctl.exe' start -D $walkthroughData `
  -l (Join-Path $walkthroughRoot 'postgres-startup.log') -w -t 20 `
  -o '-h 127.0.0.1 -p 5432'
```

This was verified on 2026-10-04 with PostgreSQL 17.4 and an authenticated read-only
query of the existing `hengshi` database/schema. It is the protected prototype,
not a selected v1 production database version. These machine-specific paths do
not select another host's cluster. Diagnose startup failures read-only; do not
reinitialize, delete, recreate, relocate or broadly change permissions on its data.
A new cluster, role, database, migration or seed is a separately approved data
operation. `pg_isready` proves server readiness only, not successful application
authentication, schema currency or the intended database identity.

### 3. Run the protected API and web app

Use separate foreground terminals so startup errors remain visible. Reuse the
existing environments; installation, upgrades and migrations are not startup.
Before binding, verify that the intended API and web ports are free or already
owned by the correctly configured Hengshi process.

API terminal, using the verified machine-local runtime profile on this machine:

```powershell
Set-Location apps/api
$runtimePath = Join-Path $env:LOCALAPPDATA 'HengshiDesign\postgres-walkthrough\runtime.json'
$nativeRuntime = Get-Content -LiteralPath $runtimePath -Raw | ConvertFrom-Json
$env:DATABASE_URL = $nativeRuntime.databaseUrl
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8001
```

Web terminal, from the repository root:

```powershell
Set-Location apps/web
$env:VITE_API_BASE_URL = 'http://127.0.0.1:8001'
npm run dev -- --host 127.0.0.1 --port 5173 --strictPort
```

`apps/api/run.ps1` currently activates the virtual environment only; it does not
start Uvicorn. If port 8000 is legitimately occupied, choose and record a free API
port and configure the web's machine-local `VITE_API_BASE_URL` accordingly. Keep
web origins consistent with the API's existing CORS configuration. Do not modify
another project's process or silently point the browser at a different API.
The verified 2026-10-04 profile uses API 8001 because 8000 belongs to a WSL relay;
the relay remains untouched. Its runtime profile points to the same `hengshi`
database, port and credentials as the existing API file, using `127.0.0.1`.
Read-only comparison observed slower `localhost` connection establishment; the
IPv4 profile avoids that path. This is startup diagnosis, not a load benchmark.
Never print the profile or connection string. Both overrides above are local to
their terminal processes; the existing `.env` files remain unchanged. On another
machine, verify its own profile before applying any override.
Stop foreground servers with Ctrl+C in their own terminals.

### 4. Verify the actual journey

- API: `http://127.0.0.1:8001/health` returns the protected API's simple health
  response. This endpoint does not test PostgreSQL connectivity. Verify an
  appropriate public read route and intended database identity separately.
- Web: `http://127.0.0.1:5173/`; staff prototype sign-in:
  `http://127.0.0.1:5173/admin/login`, using the existing authorized local account.
  Never treat the historical example password as an account or role proof.
- On 2026-10-04 the native profile returned HTTP 200 for health, World and service
  reads. A browser signed in with the existing local walkthrough account and
  reached `/admin/services`, with HTTP 200 login/admin reads and no page errors.
  This verifies that prototype path, not other admin workflows or permissions.
- Rechecked on 2026-10-09 after restarting the existing cluster and installed
  servers: a read-only database transaction confirmed `hengshi`, PostgreSQL 17.4
  and the psycopg driver. Health, public services/World and the web returned HTTP
  200. Browser sign-in reached a settled Services list with all nine existing
  records and no page errors; see the [bounded inspection](output/playwright/native-resume-2026-10-09/inspect-native-resume.cjs)
  and [settled page](output/playwright/native-resume-2026-10-09/admin-services-settled.png).
  No migration, seed, account reset or dependency installation ran. The nine
  prototype records do not replace the approved ten-category v1 service taxonomy.
- Existing fatal World hook-order (R-003) and server admin-role enforcement
  (R-004) defects remain open. A successful login or visible admin page does not
  establish correct authorization, free movement, streaming or production readiness.

A static definition/model viewer is separate from the web/API/database stack. An
existing viewer on 8766 can show the documented system without those services.
If a viewer must be started, first confirm its port is free, then from the repo root:

```powershell
python -m http.server 8766 --bind 127.0.0.1
```

Open `/docs/software-definition/definition-walkthrough.html` on that viewer.
On 2026-10-09, its desktop/narrow sections loaded without horizontal overflow or
page errors, and the unchanged accepted campus study loaded with all three camera
buttons working. See the [definition view](output/playwright/native-resume-2026-10-09/definition-desktop-settled.png)
and [campus view](output/playwright/native-resume-2026-10-09/layout-overview.png).
These dated checks do not establish continuing process health, production control
behavior, accessibility conformance or final appearance acceptance.
Static browser inspection proves the presentation only. Database fixtures and
application tests must run against an approved isolated test database, never a
live database or an unrelated WSL service. See [API notes](apps/api/README.md).

## Historical scaffold instructions

The following original scaffold instructions are retained as prototype history.
Their Docker prerequisite, unconditional migrations/seeds, example account and
completion claims do not override the current native procedure or approval rules.
Do not use them as a current initialization or production-readiness checklist.

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
