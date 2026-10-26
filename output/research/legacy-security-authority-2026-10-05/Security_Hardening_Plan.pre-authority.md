# Security Hardening Plan
## Hengshi Design Digital Platform

**Document ID:** SEC-HD-2026-001 | **Version:** 1.0 | **Date:** February 9, 2026

---

## 1. Current Security Posture

**Overall Score: 30%** — JWT authentication works but critical gaps exist.

### 1.1 Vulnerability Summary

| ID | Vulnerability | Severity | CVSS Est. | Status |
|----|--------------|----------|-----------|--------|
| V-01 | No login rate limiting | P0 Critical | 7.5 | Open |
| V-02 | JWT_SECRET default value | P0 Critical | 9.0 | Open |
| V-03 | Credentials in localStorage | P0 Critical | 6.5 | Open |
| V-04 | Overly permissive CORS | P1 High | 5.5 | Open |
| V-05 | No password complexity | P1 High | 5.0 | Open |
| V-06 | In-memory rate limiter | P1 High | 4.5 | Open |
| V-07 | No refresh token mechanism | P2 Medium | 4.0 | Open |
| V-08 | No HTML input sanitization | P2 Medium | 5.0 | Open |
| V-09 | No HTTPS enforcement | P2 Medium | 5.5 | Open |

---

## 2. Sprint 1 Remediation (Weeks 1–2)

### 2.1 V-01: Login Rate Limiting

**Risk:** Brute force attacks on admin credentials.

**Implementation:**
- Install `slowapi` package
- Add rate limiter to `POST /api/auth/login`: 5 attempts per 15 minutes per IP
- Return `429 Too Many Requests` with `Retry-After` header
- Log failed login attempts with IP and email

**Files to modify:**
- `apps/api/requirements.txt` — add `slowapi`
- `apps/api/app/auth/routes.py` — add rate limit decorator
- `apps/api/app/main.py` — configure slowapi middleware

**Acceptance criteria:**
- [ ] 6th login attempt within 15 minutes returns 429
- [ ] Rate limit resets after window expires
- [ ] Failed attempts are logged with IP address
- [ ] Test case covers rate limit behavior

### 2.2 V-02: JWT Secret Enforcement

**Risk:** Default secret enables token forgery.

**Implementation:**
- Add startup validation in `main.py`: refuse to start if `JWT_SECRET == 'change-me'` in production
- Generate strong secret: `python -c "import secrets; print(secrets.token_urlsafe(64))"`
- Document secret generation in deployment guide

**Files to modify:**
- `apps/api/app/main.py` — add startup check
- `apps/api/app/auth/jwt.py` — validate secret length (minimum 32 chars)

**Acceptance criteria:**
- [ ] Application refuses to start with default secret when `ENVIRONMENT=production`
- [ ] Clear error message instructs how to generate a proper secret
- [ ] Minimum secret length enforced (32 characters)

### 2.3 V-03: httpOnly Cookie Migration

**Risk:** XSS attacks can steal tokens from localStorage.

**Implementation:**
- Set JWT as httpOnly, Secure, SameSite=Lax cookie on login response
- Remove localStorage token storage from frontend
- Update API client to rely on cookie-based auth (credentials: 'include')
- Update CORS to allow credentials

**Files to modify:**
- `apps/api/app/auth/routes.py` — set cookie on login response
- `apps/api/app/auth/jwt.py` — read token from cookie OR header (backward compat)
- `apps/web/src/lib/api.ts` — remove localStorage, add `credentials: 'include'`
- `apps/api/app/main.py` — update CORS `allow_credentials=True`

**Acceptance criteria:**
- [ ] JWT stored in httpOnly cookie (not accessible via JS)
- [ ] Cookie has Secure flag (HTTPS only in production)
- [ ] SameSite=Lax prevents CSRF
- [ ] Frontend API client sends credentials with requests
- [ ] Logout clears the cookie

### 2.4 V-04: CORS Restriction

**Risk:** Unintended API access from unauthorized origins.

**Implementation:**
- Restrict `allow_methods` to `["GET", "POST", "PUT", "DELETE", "OPTIONS"]`
- Restrict `allow_headers` to `["Authorization", "Content-Type"]`
- Set `allow_origins` from `CORS_ORIGINS` env var (comma-separated)
- Block wildcard origins in production

**Files to modify:**
- `apps/api/app/main.py` — update CORS middleware configuration

**Acceptance criteria:**
- [ ] Only listed origins can make cross-origin requests
- [ ] Wildcard blocked when `ENVIRONMENT=production`
- [ ] Preflight OPTIONS requests handled correctly

### 2.5 V-05: Password Complexity

**Risk:** Weak passwords easily cracked.

**Implementation:**
- Add Pydantic validator for password field:
  - Minimum 12 characters
  - At least 1 uppercase, 1 lowercase, 1 digit, 1 special character
- Apply to admin creation script and any future registration endpoint

**Files to modify:**
- `apps/api/app/auth/schemas.py` — add password validator
- `apps/api/app/scripts/create_admin.py` — enforce complexity

**Acceptance criteria:**
- [ ] Weak passwords rejected with clear error message
- [ ] Existing admin password updated if below threshold
- [ ] Password requirements documented

### 2.6 Input Validation & Sanitization

**Risk:** HTML injection in body/message fields.

**Implementation:**
- Install `bleach` or `nh3` for HTML sanitization
- Sanitize `body`, `message`, `description` fields before database storage
- Strip dangerous tags while preserving safe formatting

**Files to modify:**
- `apps/api/requirements.txt` — add `nh3`
- `apps/api/app/services/schemas.py` — add sanitizer to body field
- `apps/api/app/leads/schemas.py` — add sanitizer to message field

---

## 3. Sprint 2 Remediation (Weeks 3–4)

### 3.1 V-06: Redis Rate Limiting

**Implementation:**
- Add Redis service to docker-compose.yml
- Replace in-memory rate limiter with Redis-backed implementation
- Use `slowapi` with Redis backend for all rate-limited endpoints
- Enables multi-process scaling

**Files to modify:**
- `docker-compose.yml` — add Redis service
- `apps/api/requirements.txt` — add `redis`
- `apps/api/app/leads/routes.py` — switch to Redis rate limiter
- `apps/api/app/main.py` — configure Redis connection

### 3.2 Structured Logging

**Implementation:**
- Install `structlog` for JSON-formatted logging
- Log all requests with: method, path, status, duration, IP
- Log security events: login attempts (success/fail), rate limit hits, token validation failures
- Configure log levels per environment

**Files to modify:**
- `apps/api/requirements.txt` — add `structlog`
- `apps/api/app/main.py` — add logging middleware
- `apps/api/app/auth/routes.py` — add security event logging

### 3.3 Error Tracking (Sentry)

**Implementation:**
- Install `sentry-sdk[fastapi]` for backend
- Install `@sentry/react` for frontend
- Configure DSN from environment variable
- Add React ErrorBoundary for graceful failure handling

**Files to modify:**
- `apps/api/requirements.txt` — add `sentry-sdk[fastapi]`
- `apps/api/app/main.py` — initialize Sentry
- `apps/web/package.json` — add `@sentry/react`
- `apps/web/src/App.tsx` — wrap with Sentry ErrorBoundary

### 3.4 Enhanced Health Check

**Implementation:**
- Expand `/health` to verify database connectivity
- Include application version and environment
- Add `/health/ready` for deployment readiness checks

---

## 4. Post-Sprint Security Tasks

| Task | Timeline | Notes |
|------|----------|-------|
| HTTPS enforcement | Sprint 5 (deployment) | AWS ALB/CloudFront handles TLS |
| Refresh token rotation | Phase 2 | Reduces token theft impact |
| Audit logging | Phase 2 | User activity + system events |
| Pen testing | Pre-launch | External assessment recommended |
| Dependency scanning | CI/CD setup | `safety` (Python), `npm audit` (JS) |

---

## 5. Testing Requirements

Each security fix must include:
- [ ] Unit test for the security control
- [ ] Negative test (bypass attempt)
- [ ] Integration test with full request lifecycle
- [ ] Documentation update

---

## 6. Rollback Plan

All security changes should be deployable independently. If a change causes issues:
1. Revert the specific commit
2. Redeploy previous version
3. Document the failure mode
4. Fix and re-deploy with additional test coverage
