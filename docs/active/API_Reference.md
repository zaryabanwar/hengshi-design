# API Reference
## Hengshi Design Digital Platform

**Version:** 1.0 | **Date:** February 9, 2026 | **Base URL:** `http://localhost:8000`

**Auto-generated docs:** FastAPI provides interactive docs at `/docs` (Swagger UI) and `/redoc` (ReDoc).

---

## Authentication

All admin endpoints require a JWT Bearer token in the `Authorization` header:
```
Authorization: Bearer <access_token>
```

Tokens are obtained via `POST /api/auth/login` and expire after 120 minutes (configurable via `JWT_EXPIRES_MINUTES`).

---

## Endpoints

### Health

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/health` | None | Health check — returns `{"status": "ok"}` |

---

### Authentication

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/api/auth/login` | None | Authenticate and receive JWT token |

**POST /api/auth/login**

Request:
```json
{
  "email": "admin@hengshi.com",
  "password": "string"
}
```

Response (200):
```json
{
  "access_token": "eyJ...",
  "token_type": "bearer"
}
```

Response (401): `{"detail": "Invalid credentials"}`

---

### Services (Public)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/api/services` | None | List services with optional category filter |

**GET /api/services**

Query Parameters:
- `category` (optional): Filter by category slug (e.g., `ai_systems`, `cloud_devops`)

Response (200):
```json
[
  {
    "id": "uuid",
    "slug": "ai-systems-consulting",
    "title": "AI Systems & Agentic Automation",
    "category": "ai_systems",
    "summary": "...",
    "body": "...",
    "deliverables": ["Discovery workshop", "Architecture blueprint"],
    "tags": ["ai", "automation", "llm"],
    "is_featured": true,
    "sort_order": 3,
    "created_at": "2026-02-09T00:00:00Z",
    "updated_at": "2026-02-09T00:00:00Z"
  }
]
```

**Service Categories:**
`strategy_architecture`, `platform_engineering`, `ai_systems`, `spatial_immersive`, `product_design`, `cloud_devops`, `security_trust`, `data_platforms`, `commerce_growth`, `creative_design` (pending)

---

### Projects (Public)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/api/projects` | None | List projects with optional tag filter |

**GET /api/projects**

Query Parameters:
- `tag` (optional): Filter by tag

Response (200):
```json
[
  {
    "id": "uuid",
    "slug": "immersive-portfolio",
    "title": "Immersive 3D Portfolio Platform",
    "summary": "...",
    "body": "...",
    "tags": ["three.js", "react", "webgl"],
    "is_featured": true,
    "sort_order": 1,
    "media": [
      {
        "id": "uuid",
        "type": "image",
        "url": "https://...",
        "caption": "Homepage screenshot",
        "sort_order": 1
      }
    ],
    "created_at": "2026-02-09T00:00:00Z",
    "updated_at": "2026-02-09T00:00:00Z"
  }
]
```

---

### World (Public)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/api/world` | None | Full world structure (nodes + hotspots) |

**GET /api/world**

Response (200):
```json
[
  {
    "id": "uuid",
    "key": "exterior",
    "title": "Hengshi HQ Exterior",
    "description": "...",
    "is_entry": true,
    "camera_position": {"x": 0, "y": 5, "z": 10},
    "camera_target": {"x": 0, "y": 2, "z": 0},
    "camera_fov": 50,
    "environment": {},
    "sort_order": 0,
    "hotspots": [
      {
        "id": "uuid",
        "key": "door",
        "title": "Enter Building",
        "description": "Click to enter",
        "kind": "NAVIGATE_NODE",
        "position": {"x": 0, "y": 1.5, "z": 3},
        "normal": {"x": 0, "y": 0, "z": 1},
        "radius": 0.5,
        "icon": "door",
        "payload": {"target_node": "lobby"},
        "sort_order": 0,
        "is_enabled": true
      }
    ]
  }
]
```

**Hotspot Kinds:**
- `OPEN_PANEL` — payload: `{"panel": "services|projects|contact"}`
- `NAVIGATE_NODE` — payload: `{"target_node": "node_key"}`
- `OPEN_URL` — payload: `{"url": "https://..."}`

---

### Leads (Public, Rate-Limited)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/api/leads` | None (rate-limited) | Submit a contact/lead form |

**POST /api/leads**

Rate limit: 5 requests per 60 seconds per IP (configurable).

Request:
```json
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "company": "Acme Inc",
  "phone": "+1234567890",
  "subject": "Consulting inquiry",
  "message": "We are interested in your AI systems services...",
  "source_url": "/world",
  "metadata": {}
}
```

Response (201):
```json
{
  "id": "uuid",
  "name": "Jane Doe",
  "email": "jane@example.com",
  "created_at": "2026-02-09T00:00:00Z"
}
```

Response (429): `{"detail": "Rate limit exceeded. Try again later."}`

---

### Admin CRUD Endpoints

All admin endpoints are prefixed with `/api/admin/` and require JWT Bearer authentication.

#### Admin Services

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/admin/services` | List all services |
| POST | `/api/admin/services` | Create service |
| GET | `/api/admin/services/{id}` | Get service by ID |
| PUT | `/api/admin/services/{id}` | Update service |
| DELETE | `/api/admin/services/{id}` | Delete service |

#### Admin Projects

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/admin/projects` | List all projects |
| POST | `/api/admin/projects` | Create project (with media) |
| GET | `/api/admin/projects/{id}` | Get project by ID |
| PUT | `/api/admin/projects/{id}` | Update project |
| DELETE | `/api/admin/projects/{id}` | Delete project (cascades media) |

#### Admin World

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/admin/world/nodes` | List all world nodes |
| POST | `/api/admin/world/nodes` | Create world node |
| PUT | `/api/admin/world/nodes/{id}` | Update world node |
| DELETE | `/api/admin/world/nodes/{id}` | Delete node (cascades hotspots) |
| POST | `/api/admin/world/hotspots` | Create hotspot |
| PUT | `/api/admin/world/hotspots/{id}` | Update hotspot |
| DELETE | `/api/admin/world/hotspots/{id}` | Delete hotspot |

#### Admin Leads

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/admin/leads` | List leads (with search) |

---

## Error Responses

All errors follow a consistent format:

```json
{
  "detail": "Human-readable error message"
}
```

| Status | Meaning |
|--------|---------|
| 400 | Bad request / validation error |
| 401 | Unauthorized (missing/invalid JWT) |
| 403 | Forbidden (insufficient role) |
| 404 | Resource not found |
| 409 | Conflict (duplicate slug/key) |
| 422 | Validation error (Pydantic) |
| 429 | Rate limit exceeded |
| 500 | Internal server error |

---

## Environment Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `DATABASE_URL` | `postgresql+psycopg://hengshi:hengshi@localhost:5432/hengshi` | PostgreSQL connection string |
| `JWT_SECRET` | `change-me` | **Must be changed in production** |
| `JWT_EXPIRES_MINUTES` | `120` | Token lifetime |
| `CORS_ORIGINS` | `http://localhost:5173` | Allowed CORS origins |
| `LEAD_RATE_LIMIT_MAX_REQUESTS` | `5` | Leads per IP per window |
| `LEAD_RATE_LIMIT_WINDOW_SECONDS` | `60` | Rate limit window |
