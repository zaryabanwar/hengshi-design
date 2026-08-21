# Platform Security Hardening - Data Model

## Status

| Field | Value |
|-------|-------|
| Status | Draft |
| Spec | `specs/001-platform-security-hardening/spec.md` |
| Created | 2026-06-24 |
| Last Updated | 2026-06-24 |

## Summary

No database schema migration is planned for this slice.

The feature changes authentication transport, validation, CORS policy, and
request sanitization. Those changes should happen at API configuration,
dependency, route, and Pydantic schema boundaries.

## Existing Data Structures Used

| Model / Data | Current Use | Planned Impact |
|--------------|-------------|----------------|
| `User` | Stores admin email, bcrypt password hash, role, and active state. | No column changes. Password complexity applies before password hashing and persistence. |
| JWT payload | Includes `sub`, `email`, `role`, and `exp`. | No payload shape change required. Token transport changes from frontend localStorage to httpOnly cookie plus Bearer fallback. |
| Lead fields | Public lead/contact form strings. | Inbound strings should be sanitized before persistence. |
| Service fields | Admin-managed service content. | Inbound display strings should be sanitized before persistence. |
| Project/media fields | Admin-managed project content and media metadata. | Inbound display strings should be sanitized before persistence. |
| World node/hotspot fields | Admin-managed 3D world labels, descriptions, icons, and payload values. | Inbound editable strings should be sanitized before persistence. |

## New Runtime State

| State | Location | Notes |
|-------|----------|-------|
| Login rate-limit counters | SlowAPI in-memory storage for Sprint 1 | Volatile process memory; Redis deferred unless approved now. |
| Auth cookie | Browser cookie jar | httpOnly cookie is set/cleared by API responses and not readable by frontend JavaScript. |

## Migration Plan

No Alembic migration is required.

## Rollback Considerations

Because no schema changes are planned, rollback is source-code/configuration only:

1. Remove SlowAPI middleware/decorators.
2. Restore Bearer-only auth dependency if required.
3. Restore previous CORS method/header settings if required.
4. Remove sanitizer validators if they prove too aggressive.

## Open Data Questions

1. Should rate-limit state move to Redis in this slice or remain Sprint 2?
2. Should sanitization preserve any safe formatting tags, or should all HTML be
   stripped as plain text per the active spec?
