# Platform Security Hardening - Tasks

## Status

Task generation is blocked pending review of
`specs/001-platform-security-hardening/plan.md`.

## Required Decisions Before Task Generation

1. Rate-limit window: 5 attempts per minute vs. 5 attempts per 15 minutes.
2. Password complexity: 8 characters plus upper/lower/digit vs. 12 characters
   plus upper/lower/digit/special.
3. Cookie behavior: httpOnly cookie default vs. opt-in.
4. Rate-limit storage: in-memory Sprint 1 vs. Redis now.

## Next Step

After the decisions above are approved, replace this placeholder with an ordered
task list generated from the approved plan.
