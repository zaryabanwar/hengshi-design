# Platform Security Hardening - Research

## Status

| Field | Value |
|-------|-------|
| Status | Draft |
| Spec | `specs/001-platform-security-hardening/spec.md` |
| Created | 2026-06-24 |
| Last Updated | 2026-06-24 |

## Purpose

Capture the technical research and source-of-truth notes used to plan the
Sprint 1 security-hardening slice.

## Local Sources Reviewed

| Source | Finding |
|--------|---------|
| `.specify/memory/constitution.md` | Auth/security work must follow Spec Kit and approval gates. |
| `docs/software-definition/03-autonomous-ai-development-workflow.md` | Requires official docs/Context7 for version-sensitive choices and pytest/Playwright verification. |
| `docs/active/Security_Hardening_Plan.md` | Defines the larger security roadmap and older sprint assumptions. |
| `docs/active/API_Reference.md` | Documents current Bearer-token auth, CORS env vars, and existing API behavior. |
| `apps/api/app/main.py` | CORS is env-driven and credentials are enabled, but methods/headers are wildcarded. |
| `apps/api/app/auth/deps.py` | Auth dependency currently reads Bearer tokens only. |
| `apps/api/app/auth/jwt.py` | JWT secret is required but length/default-strength enforcement is incomplete. |
| `apps/web/src/lib/api.ts` | Admin token is currently read from `localStorage`. |

## External Primary References

| Topic | Reference |
|-------|-----------|
| FastAPI response cookies | https://fastapi.tiangolo.com/advanced/response-cookies/ |
| FastAPI CORS | https://fastapi.tiangolo.com/tutorial/cors/ |
| SlowAPI route limits | https://slowapi.readthedocs.io/ |
| Pydantic v2 validators | https://pydantic.dev/docs/validation/latest/concepts/validators/ |
| nh3 sanitization | https://nh3.readthedocs.io/ |
| HTTP cookie attributes | https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie |

## Decisions Proposed In Plan

| Area | Proposed Choice | Reason |
|------|-----------------|--------|
| Login rate limiting | SlowAPI on `POST /api/auth/login` | Direct FastAPI integration and documented route-level limits. |
| Rate-limit storage | In-memory for Sprint 1 | Redis-backed limiting is documented as a later hardening step. |
| Auth cookie | httpOnly cookie by default with Bearer fallback | Reduces token exposure while preserving API compatibility. |
| Cookie flags | `HttpOnly`, `SameSite=Lax`, `Path=/`, `Secure` in production | Matches browser cookie security guidance. |
| Sanitizer | `nh3` | Current Python HTML sanitizer option; avoids adopting unmaintained Bleach. |

## Conflicts Requiring Approval

1. Active spec says login limit is 5 attempts per minute; older hardening plan
   says 5 attempts per 15 minutes.
2. Active spec says passwords need 8 characters with uppercase, lowercase, and
   digit; older hardening plan says 12 characters with uppercase, lowercase,
   digit, and special character.
3. Active spec asks whether httpOnly cookies should be default or opt-in.
4. Active spec asks whether rate limiting should use in-memory storage or Redis.

## Research Outcome

The implementation approach is technically straightforward, but task generation
and implementation should wait until the conflicts above are resolved.
