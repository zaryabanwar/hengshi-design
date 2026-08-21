# Platform Security Hardening - Implementation Plan

## Status

| Field | Value |
|-------|-------|
| Status | Draft - Needs Review |
| Spec | `specs/001-platform-security-hardening/spec.md` |
| Author | Zaryab |
| Created | 2026-06-24 |
| Last Updated | 2026-06-24 |

## Summary

This plan covers the Sprint 1 security-hardening slice for the FastAPI API and
React admin surface. The implementation will add login rate limiting, JWT secret
validation, httpOnly cookie auth with Bearer-token fallback, restricted CORS,
password complexity validation, and HTML/script sanitization for incoming string
fields.

The plan is intentionally scoped to reversible source-code changes. It does not
create database migrations, Git commits, production deployments, or remote
configuration changes.

## Planning Inputs

| Source | Notes |
|--------|-------|
| `.specify/memory/constitution.md` | Requires Spec Kit before security/auth work, latest compatible docs, and verification. |
| `docs/software-definition/README.md` | Defines product-level source of truth and linked security/API docs. |
| `docs/software-definition/01-system-boundaries.md` | Confirms backend, admin dashboard, frontend, and database boundaries. |
| `docs/software-definition/03-autonomous-ai-development-workflow.md` | Defines approval gates and required verification. |
| `specs/001-platform-security-hardening/spec.md` | Active feature spec for this plan. |
| `docs/active/Security_Hardening_Plan.md` | Older security roadmap; conflicts recorded below. |
| `docs/active/API_Reference.md` | Current auth/API behavior and environment variables. |
| Official docs | FastAPI response cookies, FastAPI CORS, SlowAPI, Pydantic v2 validators, nh3, and MDN cookie guidance. |

## Official Documentation References

| Topic | Primary reference |
|-------|-------------------|
| FastAPI response cookies | https://fastapi.tiangolo.com/advanced/response-cookies/ |
| FastAPI CORS | https://fastapi.tiangolo.com/tutorial/cors/ |
| SlowAPI route limits | https://slowapi.readthedocs.io/ |
| Pydantic v2 validators | https://pydantic.dev/docs/validation/latest/concepts/validators/ |
| nh3 sanitization | https://nh3.readthedocs.io/ |
| HTTP cookie attributes | https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie |

## Architecture Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Login rate limiting | Use SlowAPI on `POST /api/auth/login` with an IP-based `5/minute` limit pending approval. | Matches `FR-01` in the active spec. SlowAPI documents route limits such as `5/minute` and returns 429 for excess requests. |
| Rate-limit storage | Use in-memory SlowAPI storage for Sprint 1; defer Redis to Sprint 2 unless user approves a scope change. | `docs/active/Security_Hardening_Plan.md` lists Redis rate limiting as Sprint 2. This avoids adding infrastructure in this slice. |
| JWT secret enforcement | Centralize validation in `app.auth.jwt` and call it during startup. Require `JWT_SECRET` to be present and at least 32 characters. | Matches `FR-02` and avoids starting the API with weak signing material. |
| Auth transport | Set an httpOnly access-token cookie on successful login and keep Bearer header auth as fallback. | Matches `FR-03` and preserves existing API clients while migrating the admin UI away from `localStorage`. |
| Cookie policy | Default to `httponly=True`, `samesite='lax'`, `path='/'`; set `secure=True` when `ENVIRONMENT=production`. | FastAPI exposes `Response.set_cookie`; MDN guidance supports HttpOnly/Secure/SameSite for sensitive cookies. |
| Logout support | Add `POST /api/auth/logout` to clear the httpOnly cookie. | Once tokens are httpOnly, the frontend cannot clear them directly. A server endpoint is required for reliable logout. |
| CORS | Keep env-driven origins, block wildcard origins in production, restrict methods and headers, and keep credentials enabled. | Matches `FR-04`; FastAPI CORS docs require explicit allowed origins for credentialed cross-origin requests. |
| Password validation | Enforce active-spec rule: minimum 8 characters, at least 1 uppercase, 1 lowercase, and 1 digit. | Matches `FR-05`. The older security plan asks for 12 characters plus special character; this conflict needs user review before tasks. |
| Sanitization package | Use `nh3` instead of `bleach`. | The active spec allows a sanitizer dependency. Current Bleach project notices mark it unmaintained; `nh3` is actively documented for Python HTML sanitization. |
| Sanitization timing | Sanitize at Pydantic schema boundaries before model persistence. | Keeps cleaning close to request validation and avoids modifying database models for this slice. |
| Database | No migration. | Rate limits are in-memory for Sprint 1; JWT/CORS/cookie/password/sanitization changes do not require schema changes. |

## Proposed Changes

### Backend (FastAPI)

#### Files to Create

| File | Purpose |
|------|---------|
| `apps/api/app/security/__init__.py` | Package marker for shared security helpers. |
| `apps/api/app/security/rate_limit.py` | Configure the SlowAPI limiter, key function, exception handler, and login limit string. |
| `apps/api/app/security/sanitize.py` | Provide reusable plain-text sanitization helpers built on `nh3`. |

#### Files to Modify

| File | Change |
|------|--------|
| `apps/api/requirements.txt` | Add `slowapi` and `nh3`. |
| `apps/api/app/main.py` | Register rate-limit middleware/handler, validate JWT secret at startup, restrict CORS methods/headers, block wildcard origins in production. |
| `apps/api/app/auth/routes.py` | Add request-aware login rate limiting, set the httpOnly cookie on login, log failed attempts without logging passwords, add `POST /logout` to clear the cookie. |
| `apps/api/app/auth/deps.py` | Read token from Bearer header first, then from the httpOnly cookie fallback. |
| `apps/api/app/auth/jwt.py` | Enforce `JWT_SECRET` length, keep token creation/decoding centralized, expose cookie/security config helpers if needed. |
| `apps/api/app/auth/password.py` | Add password-complexity validation helper used by schemas and admin creation. |
| `apps/api/app/auth/schemas.py` | Add password validation for request schemas that accept passwords. |
| `apps/api/app/scripts/create_admin.py` | Reject weak `ADMIN_PASSWORD` values before creating an admin user. |
| `apps/api/app/leads/schemas.py` | Sanitize all inbound string fields, including `name`, `company`, `phone`, `subject`, `message`, and `source_url`. |
| `apps/api/app/services/schemas.py` | Sanitize display fields such as `title`, `summary`, `body`, `deliverables`, and `tags` while preserving slug/category validation. |
| `apps/api/app/projects/schemas.py` | Sanitize display fields such as `title`, `summary`, `body`, `tags`, media `url`, and media `caption` where appropriate. |
| `apps/api/app/world/schemas.py` | Sanitize user-editable text fields such as `title`, `description`, `icon`, and URL payload strings where appropriate. |
| `apps/api/tests/conftest.py` | Update test `JWT_SECRET` to a 32+ character value and isolate rate-limit state between tests if needed. |
| `apps/api/tests/test_auth.py` | Add tests for login 429 behavior, cookie issuance, cookie auth fallback, logout cookie clearing, Bearer fallback, weak secret validation, and weak password rejection. |
| `apps/api/tests/test_leads.py` | Add XSS payload sanitization assertions for public lead submission. |
| `apps/api/tests/test_services.py` | Add sanitization assertions for admin-managed service fields. |
| `apps/api/tests/test_projects.py` | Add sanitization assertions for project and media fields. |
| `apps/api/tests/test_world.py` | Add sanitization assertions for world node/hotspot text fields. |
| `apps/api/README.md` | Document JWT secret generation, auth cookie behavior, CORS origins, and security verification commands. |
| `docs/active/API_Reference.md` | Update auth docs for cookie support, logout endpoint, CORS, and new/changed env variables. |

### Frontend (React)

#### Files to Create

| File | Purpose |
|------|---------|
| None expected. | Keep frontend changes scoped to the existing admin auth and API client files unless implementation reveals a cleaner local pattern. |

#### Files to Modify

| File | Change |
|------|--------|
| `apps/web/src/lib/api.ts` | Add `credentials: 'include'` to authenticated requests, stop reading/writing `localStorage` auth headers, add `fetchAdminMe`, and add `logoutAdmin`. |
| `apps/web/src/admin/AdminLoginPage.tsx` | Stop storing the returned token in `localStorage`; rely on the login response cookie and route navigation. |
| `apps/web/src/admin/RequireAdmin.tsx` | Replace synchronous `localStorage` guard with an async `/api/admin/me` check using cookie credentials. |
| `apps/web/src/admin/AdminLayout.tsx` | Call `logoutAdmin` before navigating to `/admin/login`; remove `localStorage` deletion. |

### Database

#### Migrations

| Migration | Description |
|-----------|-------------|
| None | This slice does not require database schema changes. |

### Infrastructure

| Area | Change |
|------|--------|
| Environment | Confirm or add `ENVIRONMENT=development|production`, `JWT_SECRET`, and `CORS_ORIGINS`. |
| Docker Compose | No change for Sprint 1 unless Redis is approved now. |
| Production config | Production must provide a non-wildcard `CORS_ORIGINS` list and a 32+ character `JWT_SECRET`. |

## API Changes

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/api/auth/login` | Rate-limited login. On success, returns the existing token response and sets an httpOnly auth cookie. | None |
| POST | `/api/auth/logout` | Clears the auth cookie so the browser session can end cleanly. | Cookie or Bearer accepted; endpoint should be idempotent. |
| GET | `/api/admin/me` | Existing endpoint; updated dependency accepts Bearer header or auth cookie. | Admin |

## Data Model Changes

No tables, columns, relationships, or indexes are planned for this slice.

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `slowapi` | Latest compatible with current FastAPI/Starlette stack | Login rate limiting and 429 handling. |
| `nh3` | Latest compatible Python package | HTML/script sanitization for inbound string fields. |

No frontend dependency is expected for this slice.

## Verification Plan

### Automated Tests

```powershell
cd apps/api
pytest
```

```powershell
cd apps/web
npm run build
```

If Playwright is installed/configured when implementation starts, run the admin
auth flow against the changed login/logout surfaces:

```powershell
cd apps/web
npx playwright test
```

### Backend Test Cases

| Area | Expected Coverage |
|------|-------------------|
| Login rate limit | Sixth failed login attempt from the same client inside the approved window returns 429. |
| JWT secret | Weak/missing secret raises a clear startup/configuration error. |
| Cookie auth | Login sets an httpOnly cookie; `/api/admin/me` works with the cookie and still works with Bearer header. |
| Logout | Logout clears the cookie and is safe to call repeatedly. |
| CORS | Allowed origins succeed; unauthorized origins do not get permissive CORS response headers. |
| Password complexity | Weak admin password is rejected with a clear validation message. |
| Sanitization | HTML/script tags are stripped from lead, service, project, media, world node, and hotspot string fields before persistence/response. |

### Manual Verification

1. Generate a 32+ character `JWT_SECRET` and confirm the API starts.
2. Temporarily set a short `JWT_SECRET` and confirm the API refuses to start with a clear error.
3. Start the API and web app locally.
4. Log in through `/admin/login` and confirm DevTools shows an httpOnly auth cookie.
5. Confirm JavaScript cannot read the auth cookie through `document.cookie`.
6. Refresh an admin page and confirm the cookie-based session still works.
7. Log out and confirm the auth cookie is removed or expired.
8. Submit a lead containing HTML/script input and confirm stored/returned text is sanitized.
9. Send a request with an unauthorized `Origin` header and confirm CORS is not permissive.

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Spec and older hardening plan disagree on rate-limit window and password strength. | Implementation could lock in the wrong policy. | Keep this plan in Draft and require user approval before task creation. |
| In-memory rate limiting does not scale across multiple API workers. | Brute-force protection can be bypassed in multi-process production. | Treat Redis-backed rate limiting as Sprint 2 unless approved for this slice. |
| Cookie auth can introduce CSRF concerns. | Admin actions could be exposed if cookie policy is too permissive. | Use SameSite=Lax, restricted CORS, JSON requests, and Bearer fallback; consider CSRF tokens in a future auth-hardening spec if needed. |
| Sanitizing every string field may alter legitimate content. | Admin-entered service/project content could lose formatting. | Active spec says string fields strip HTML tags; tests should assert plain-text behavior. |
| Rate-limit tests can be flaky if limiter state leaks between tests. | Test suite could fail depending on execution order. | Provide a test-specific limiter reset or isolated key strategy. |
| Frontend guard becomes asynchronous. | Admin routes need a loading state to avoid flicker/false redirects. | Implement a small loading state inside `RequireAdmin` and verify with build/browser checks. |

## Conflicts & Pending Decisions

1. Rate-limit window: active spec says 5 attempts per minute; `docs/active/Security_Hardening_Plan.md` says 5 attempts per 15 minutes.
2. Password complexity: active spec says minimum 8 characters with uppercase, lowercase, and digit; older hardening plan says minimum 12 characters with uppercase, lowercase, digit, and special character.
3. Cookie default: active spec asks whether httpOnly cookies should be default or opt-in. This plan proposes default cookie issuance with Bearer fallback.
4. Rate-limit storage: active spec asks in-memory vs Redis. This plan proposes in-memory for Sprint 1 because Redis is documented as Sprint 2.

## Review Gate

Before creating `tasks.md` or implementing, approve or revise the four pending
decisions above. After approval, the next step is to create an ordered task list
for this plan and keep implementation blocked until that task list is reviewed.
