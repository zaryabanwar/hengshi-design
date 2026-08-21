# Platform Security Hardening - Requirements Checklist

## Functional Requirements

- [ ] FR-01: Login endpoint is rate-limited according to the approved window.
- [ ] FR-02: `JWT_SECRET` must be present and at least 32 characters.
- [ ] FR-03: Auth token can be stored in an httpOnly cookie with Bearer header fallback.
- [ ] FR-04: CORS allows only approved development and production origins.
- [ ] FR-05: Password complexity is enforced according to the approved rule.
- [ ] FR-06: User-supplied string inputs are sanitized against HTML/script injection.

## Non-Functional Requirements

- [ ] NFR-01: Login response time remains under the target with rate limiting.
- [ ] NFR-02: Existing backend and frontend verification commands continue to pass.

## Acceptance Criteria

- [ ] Login returns 429 after the approved number of failed attempts within the approved window.
- [ ] API refuses to start with a missing or short `JWT_SECRET`.
- [ ] `/api/admin/me` accepts auth via httpOnly cookie or Bearer header.
- [ ] Login sets, and logout clears, the auth cookie.
- [ ] Unauthorized origins do not receive permissive CORS response headers.
- [ ] Weak passwords are rejected with a clear error message.
- [ ] HTML/script tags are stripped from inbound string fields before persistence.

## Approval Checklist

- [ ] Rate-limit window conflict resolved.
- [ ] Password complexity conflict resolved.
- [ ] Cookie default behavior approved.
- [ ] Rate-limit storage choice approved.
- [ ] `tasks.md` generated after the decisions above.
