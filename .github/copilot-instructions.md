# Hengshi Design - Copilot Instructions

## Architecture Overview

**Monorepo structure:** FastAPI backend + React/Vite frontend + shared schemas
- `apps/api/` - Python FastAPI with SQLAlchemy 2.0 + Alembic migrations + JWT auth
- `apps/web/` - React 18 + TypeScript + Tailwind + React Router + Zustand + Three.js (3D visuals)
- `packages/shared/` - Zod schemas/types (optional, not currently integrated)
- **Database:** PostgreSQL (Docker) with UUID primary keys and timezone-aware timestamps

## Critical Development Workflows

### Starting Local Environment (Windows PowerShell)
```powershell
# Terminal 1: Start database
docker compose up -d db

# Terminal 2: Activate venv once, then use run.ps1
cd apps/api
.\.venv\Scripts\Activate.ps1
python -m app.scripts.create_admin  # First time only
python -m app.scripts.seed_projects
python -m app.scripts.seed_world
# Then either: uvicorn app.main:app --reload --port 8000
# Or: ./run.ps1

# Terminal 3: Start frontend
cd apps/web
npm run dev  # Vite dev server on port 5173
```

### Database Migrations (Alembic)
- Run from `apps/api/` with `.env` file present
- `alembic revision -m "description"` → create new migration
- `alembic upgrade head` → apply all pending migrations
- **Important:** Models in `app/models/` must have `Base` as parent class and use `Mapped` type hints

### API Testing
```powershell
cd apps/api
pytest  # Runs tests in apps/api/tests/
```

## Key Patterns & Conventions

### Backend (FastAPI/SQLAlchemy)

**Database session dependency:**
```python
from app.db.session import get_db
from sqlalchemy.orm import Session

def route_handler(db: Session = Depends(get_db)):
    # Use db.execute(select(...)) for queries
    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
```

**Authentication/Authorization:**
- JWT tokens created in `app/auth/jwt.py` with payload: `sub` (user_id), `email`, `role`, `exp`
- All admin routes use `require_admin` dependency (validates JWT + role='admin')
- Auth token passed in `Authorization: Bearer <token>` header
- Password hashing via bcrypt in `app/auth/password.py`

**Model definitions:**
- Use SQLAlchemy 2.0 Annotated Mapped syntax (see `app/models/user.py`)
- All models inherit from `app.db.base.Base`
- Always use `server_default` for DB-side defaults (e.g., timestamps, UUIDs)
- String primary keys are UUIDs: `sa.String(36), default=lambda: str(uuid.uuid4())`

**CRUD routes pattern:**
- Public list/get routes in `/api/{resource}` (e.g., services, projects, world data)
- Admin create/update/delete in `/api/admin/{resource}`
- Use `selectinload()` for eager loading relationships when needed
- Filter queries with SQLAlchemy expressions, support pagination via `limit`/`offset` Query params

**Response schemas:**
- Define in `app/{resource}/schemas.py` using Pydantic BaseModel
- Separate schemas for Create/Update (input) vs. Out (response)
- Response models declared on route with `response_model=` parameter

### Frontend (React + TypeScript)

**State management:**
- Zustand stores in `src/store/` for global client state
- Routes defined in `src/App.tsx` using React Router v6
- Admin routes protected by `<RequireAdmin>` wrapper (checks localStorage auth token)

**API calls:**
- HTTP client configured in `src/lib/api.ts`
- Base URL points to `http://127.0.0.1:8000` (development)
- Token sent in `Authorization: Bearer` header for admin requests
- Error responses from FastAPI return HTTP status codes + JSON `detail` field

**3D assets:**
- Place GLB files in `apps/web/public/models/` for static serving
- Three.js with react-three-fiber for rendering (see WorldPage component)
- GSAP for animations

## Critical Integration Points

1. **JWT Secret:** Set `JWT_SECRET` in `.env` (API won't run without it)
2. **CORS:** Configured in `app/main.py`, defaults to `localhost:5173` (frontend dev server)
3. **Database URL:** `DATABASE_URL` in `.env`, defaults to PostgreSQL at `localhost:5432`
4. **Token expiration:** `JWT_EXPIRES_MINUTES` env var (default 120 minutes)

## Common Tasks

**Adding a new admin endpoint:**
1. Add route to `app/{resource}/routes.py`
2. Add `require_admin` dependency to protect it
3. Query models from `app/models/`, return response schema
4. Frontend calls via `src/lib/api.ts` with token from localStorage

**Seeding initial data:**
- Scripts in `app/scripts/`: `create_admin.py`, `seed_projects.py`, `seed_services.py`, `seed_world.py`
- Run manually after migrations: `python -m app.scripts.seed_services`

**Testing API changes:**
- Use Swagger at `http://127.0.0.1:8000/docs`
- Unit tests in `apps/api/tests/test_{resource}.py` use `conftest.py` fixtures
