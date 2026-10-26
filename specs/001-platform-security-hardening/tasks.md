# Platform Security Hardening — task readiness

Task status: BLOCKED for implementation. Reconciled 2026-10-04.

This file is a readiness placeholder, not an executable task plan. The June plan
is historical; no implementation tasks have been generated or completed.

## Settled constraints — do not ask again

D-018 and foundation SEC-001–SEC-010 select Entra staff roles, mandatory controlled
emergency MFA, rotating HttpOnly/Secure/SameSite browser cookies, CSRF protection,
Redis-backed production account/network limits and 24+ character emergency
credentials. The former questions about optional cookies and in-memory production
storage are resolved. Eight versus twelve-character prototype password rules
do not determine the selected emergency policy. No visitor registration is added.

## Remaining task-generation inputs

1. Complete Phase 1 acceptance and current bounded feature specification/plan.
2. Reviewed exact Entra/role mapping, session/token/CSRF and emergency procedures.
3. Approved rate thresholds, Redis-outage behavior and tested rollback boundaries.
4. Approved class-specific legal retention/deletion and provider policy evidence.
5. Approved staff surface references and negative authorization/QA coverage.

Use the proposed [security/privacy contract](../../docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md)
and [QA/recovery definition](../../docs/phase-1-architecture/contracts/QA_RECOVERY.md)
to prepare those inputs. Generate dependency-ordered implementation tasks only
from the then-approved specification and plan. No application, dependency,
credential or migration change is authorized here.

Historical context: the original placeholder requested founder choices between
five attempts/minute versus fifteen minutes, eight versus twelve-character
passwords, optional versus default cookies and in-memory versus Redis limits.
It contained no executable task list. Threshold details remain open; settled
transport, role and storage constraints must not be reopened as those choices.
