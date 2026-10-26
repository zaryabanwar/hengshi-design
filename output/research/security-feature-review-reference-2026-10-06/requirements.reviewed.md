# Specification quality checklist — Staff security and privacy v1

Status: DOING. Created/inspected 2026-10-04 by the specification producer.
Feature: [spec.md](../spec.md). Definition quality only; no runtime security proof,
independent feature verdict or implementation approval.

## Content quality

- [x] Staff/visitor outcomes and actual prototype gaps are separated from targets.
- [x] Every mandatory project-template section is populated.
- [x] Accepted roles/MFA/cookies/CSRF/Redis/credential constraints are not reopened.
- [x] Historical spec/checklist preserved byte-for-byte before replacement.
- [x] Existing review scopes remain historical; their verdicts do not cover this draft.
- [x] No new dependency, threshold, schema, algorithm, provider or grant selected.

## Requirement completeness

- [x] Identity, action/object/purpose/state and combined-role separation have denial cases.
- [x] Read/projection leakage and authorization changes at mutation have scenarios.
- [x] Rotating sessions, exact accepted timeouts, CSRF/logout and emergency lifecycle covered.
- [x] Distributed rate protection retains held thresholds/outage methods.
- [x] Typed/context-specific validation replaces historical blanket-strip assumptions.
- [x] Consent/class/provider/training and expiry/deletion/restore boundaries are covered.
- [x] Audit/private operations, public claims and truthful fallback are bounded.
- [x] Alias ownership stays explicitly undecided; no monitoring recipient inferred.
- [ ] Exact identity/control/schema/resource and legal/provider pass/fail inputs accepted.
- [x] Producer source comparison and local-reference inspection completed; accepted SEC-002's administrator-operation 403 case is explicit.

## Feature readiness

- [x] Native operation, v1 naming and latest compatible stable policy retained.
- [x] D-068 hosting deferral does not replace Entra/private-AI restrictions.
- [ ] Nonproducer security/privacy/identity/architecture and applicable legal/accessibility review complete.
- [ ] Founder feature and full Phase 1 acceptance recorded.
- [ ] Approved current research/data/contracts/plan/tasks ready for execution.

## Producer findings and next action

1. The June feature deferred or weakened settled launch controls. The current
   draft uses accepted SEC/DATA/AI/PUB constraints and canonical boundaries;
   no application code or configuration changed.
2. Historical research/data/plan/tasks remain nonexecutable evidence/readiness.
   Exact methods and legal/grant mappings are still inputs, not defaults.
3. Producer inspection resolves all local references and all 17 template sections;
   both historical snapshot hashes match the earlier review. Revision 1 makes
   SEC-002's explicit 403 oracle visible. Obtain independent feature review;
   no old verdict, integrity check or checklist certifies runtime security.
