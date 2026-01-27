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
