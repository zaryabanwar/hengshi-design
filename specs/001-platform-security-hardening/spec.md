# Platform Security Hardening

## Status

| Field | Value |
|-------|-------|
| Status | Draft |
| Author | Zaryab |
| Created | 2026-06-24 |
| Last Updated | 2026-06-24 |
| Sprint | Sprint 1 (Weeks 1-2) |

## Problem Statement

The Hengshi Design platform currently has basic JWT authentication but lacks
comprehensive security hardening. Key gaps include: no login rate limiting,
configurable JWT secrets without enforcement, no httpOnly cookie option for
tokens, permissive CORS, no password complexity enforcement, and insufficient
input sanitization.

These gaps expose the platform to brute-force attacks, XSS via token theft,
CSRF, and injection vulnerabilities.

## Goals

1. Prevent brute-force login attempts via rate limiting
2. Enforce strong JWT secret configuration
3. Move tokens to httpOnly cookies (with Bearer header fallback)
4. Restrict CORS to known origins
5. Enforce password complexity at registration/change
6. Sanitize all user inputs against XSS and injection

## Non-Goals

1. Multi-factor authentication (Phase 2)
2. OAuth/social login (Phase 2)
3. Role-based access control expansion (separate spec)
4. API key management for external consumers

## User Stories

### As an admin user

- I want login attempts to be rate-limited so that my account is protected
  from brute-force attacks.
- I want my auth token stored in httpOnly cookies so that JavaScript-based
  attacks cannot steal my session.

### As a platform visitor

- I want to know the site uses secure practices so that I trust the platform
  with my contact information (leads).

### As a developer

- I want clear password requirements so that I implement them consistently.
- I want CORS properly configured so that only the frontend origin can call the API.

## Functional Requirements

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-01 | Rate limit login endpoint to 5 attempts per minute per IP | Must |
| FR-02 | Enforce minimum JWT_SECRET length of 32 characters | Must |
| FR-03 | Support httpOnly cookie token storage | Should |
| FR-04 | Restrict CORS to localhost:5173 (dev) and production domain | Must |
| FR-05 | Enforce password minimum 8 chars, 1 upper, 1 lower, 1 digit | Must |
| FR-06 | Sanitize all string inputs for HTML/script injection | Must |

## Non-Functional Requirements

| ID | Requirement | Target |
|----|-------------|--------|
| NFR-01 | Login response time with rate limiting | < 200ms |
| NFR-02 | No security regression in existing tests | 100% pass |

## Acceptance Criteria

- [ ] Login returns 429 after 5 failed attempts within 1 minute
- [ ] App fails to start if JWT_SECRET is less than 32 characters
- [ ] Auth token can be sent via httpOnly cookie or Authorization header
- [ ] CORS rejects requests from unauthorized origins
- [ ] Registration/password-change rejects weak passwords with clear error message
- [ ] All string fields strip HTML tags on input

## Dependencies

- `slowapi` or custom middleware for rate limiting
- `bleach` or custom sanitizer for input cleaning

## Open Questions

1. Should rate limiting use in-memory store (simple) or Redis (scalable)?
2. Should httpOnly cookies be the default or opt-in via header?

## References

- [Security Hardening Plan](../../docs/active/Security_Hardening_Plan.md)
- [API Reference](../../docs/active/API_Reference.md)
- OWASP Top 10 2021
