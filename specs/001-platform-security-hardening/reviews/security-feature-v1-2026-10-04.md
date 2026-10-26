# Independent staff security and privacy feature review — v1

Date: 2026-10-04. Reviewer: `review_security_feature_v1`, independent of the producer.
Verdict: **PASS for the bounded feature definition and producer quality checklist**.
Open actionable findings: Critical 0 / High 0 / Medium 0 / Low 0.
Task status: DOING; commits are deferred. No producer revision is required by this review.

## Exact reviewed scope

SHA-256 was independently computed before inspection and rechecked before reporting:

| Reviewed artifact | SHA-256 |
|---|---|
| [Active spec](../spec.md) | `6649110C6AC2A83F4AC8840DBF0288792F6251DCEB69E51E9DA328BB8BD59B0B` |
| [Active checklist](../checklists/requirements.md) | `4C31BB88EA372643C96E11CFEABD1C8CDF12F6F87B239F8687670EE81EC31BA7` |

Historical snapshot hashes independently match the prior [six-artifact authority-notice review](../../../docs/phase-1-architecture/contracts/reviews/security-feature-reconciliation-2026-10-04.md): `history/spec-2026-10-04.txt` is `5281DDFD3A6813ADDFA56DE0A8A499B3A8136D5D009E5BCE8A02F5EDD94F1614`; `history/requirements-2026-10-04.txt` is `822774EDA00CCE84A9C35EB80EEE2E5ECFA199AF629FAC4E28246E0C0F7AD19F`. That verdict covered preserved authority notices, not the new feature. It has not been transferred.

Applied current AGENTS.md, constitution VI–VIII and authority order, PROJECT.md, DECISIONS.md, PROJECT_STATE.yaml, software-definition README, D-025/D-065/D-068–D-070, accepted foundation requirements and the canonical security, data, interface, publication and QA contracts. The foundation README's current authority notice governs its preserved July draft labels. The six canonical security/data/interface/publication/QA/classification hashes were recomputed and match those in the [current-definition amendments review](../../../docs/phase-1-architecture/contracts/reviews/current-definition-amendments-2026-10-04.md); matching provenance does not accept their held exact mechanisms.

## Requirement and boundary assessment

| Source obligation | Feature trace and assessment |
|---|---|
| SEC-001/SEC-002: Entra roles and server authorization | FSC-01/02 and scenarios 1/2 require current identity, explicit action/object/purpose/state, direct API/job denial and scoped list/search/count/error projections. Scenario 2 preserves the independently specified 403 for an authenticated non-administrator attempting administrator operations after frontend guard removal. The permission-change interleaving is an actual mutation-boundary oracle. |
| PUB-002/PUB-003 and security action matrix: independent approval | FSC-03, primary journey 3/4 and scenario 3 bind the exact candidate, invalidate edited approvals, reject combined-role self-review/self-approval and require distinct operational activation authority. Content/admin roles do not confer private operations or publication powers. |
| SEC-004/SEC-005: browser sessions, CSRF and logout | FSC-04/05 and scenarios 4–6 preserve rotating Secure/HttpOnly/SameSite JWT cookies, the 30-minute idle/eight-hour absolute limits, actual browser/API inspection, replay/revocation denial, no localStorage token transport, side-effect-free cross-site denial and harmless repeated server logout. Exact identity/key/rotation/CSRF semantics remain held. |
| SEC-003/SEC-010: emergency access | FSC-06 and scenarios 7/8 cover both normally dormant accounts, authorized activation, bcrypt plus local MFA, activation/use alerts, post-use review/rotation, random 24+ credentials and rejection of short/weak/reused values before creation. Generator, entropy, custody, MFA and recipients remain unresolved inputs; no values enter evidence. |
| SEC-006: distributed abuse protection | FSC-07 and scenario 9 require Redis account/network counters across workers, progressive delay, bounded retry guidance and no indefinite unrelated-account lockout. Redis loss must exercise the subsequently accepted outage contract; no single-process fallback or historical threshold is selected. |
| SEC-007/SEC-008: platform controls and secrets | FSC-08/09, FSC-N02 and scenarios 10/11 require typed/context-specific controls at request, persistence and rendered-output boundaries, bounded asset/resource work, least privilege, restricted CORS/CSP/WAF, transit/at-rest encryption, redaction and alert behavior. Synthetic canaries support inspection without exposing credentials or choosing a provider configuration. |
| SEC-009 and PUB requirements: applicable public gates | FSC-13, SEO/publication requirements and scenario 15 retain legal/security review holds, private/draft isolation, coherent immutable publication and audit/export restrictions. Admin, emergency access and robots exclusions cannot bypass the applicable gates. Company facts and alias names do not prove verification, monitored delivery or certification. |
| DATA-003–DATA-009: collection, retention and deletion | Non-goals, FSC-10/11, the class table and scenarios 12/13 separate no visitor accounts/uploads, non-consented ephemeral handling, purpose/version consent, mapped 90-day expiry, no clock reset, scoped verified deletion and quarantined restore. Booking/provider, consent-proof, staff/audit and suppression records are not assigned blanket chat retention. Unknown/unmapped outcomes stay pending. Canonical classification and legal policy remain required. |
| AI-001–AI-009: evidence, classification and refusal | AI section, FSC-10/12/13 and scenarios 12/14/15 inherit approved versioned grounding/source, injection-refusal and nonbinding boundaries. Model output grants no operational authority; prohibited material is neither echoed nor retained. Approved private/PII processing remains restricted to verified Azure Europe; NVIDIA remains public/demonstrably de-identified and entitlement-gated. Outage grants no weaker failover. |
| DATA-010 and interface/private process contracts | FSC-02/12, interface table and scenarios 2/14 distinguish authorization and truthful process projection from external outcome. The canonical catalogue remains authority for visitor process proof, staff intervention, WebSocket Origin/ownership, directional fields and idempotent/reconciled effects. The feature adds no substitute endpoint, wire schema, staff grant or fabricated verification/confirmation. |
| QA/recovery and accessible equivalent journeys | FSC-N03/04/05 and scenario 16 preserve complete-process accessibility, actual isolated runtime evidence, accepted RPO/RTO and existing performance profiles. Public semantic Book/Contact remains available without staff login, visitor accounts, sound or World traversal. Browser automation, mocked responses, schema checks and documentation counts do not certify application security or accessibility. |

The feature makes its future behavior oracles explicit at `spec.md:197–217`. Denial cases have permitted controls where appropriate; concurrency/state changes, provider uncertainty, expiry clocks and restoration are covered without copying prototype behavior into expected results. Exact held inputs cannot yet yield executable pass/fail tests, and `spec.md:216–246` correctly blocks planning/implementation until those inputs and applicable approvals exist. Referenced canonical contracts remain incorporated obligations rather than silently being replaced by the shorter feature scenarios.

Current source inspection confirms the cited prototype gaps: `apps/api/app/auth/deps.py:48–51` returns the authenticated user without an admin check; `apps/web/src/admin/RequireAdmin.tsx:8` and `apps/web/src/lib/api.ts:63` read localStorage tokens; `apps/api/app/auth/routes.py:29–34` issues a token response. This verifies problem evidence only, not a security test or authorization to modify the prototype.

## Checklist and held-input assessment

The checklist distinguishes producer inspection from independent verdict, runtime security proof and implementation approval (`checklists/requirements.md:3–5, 26, 33–47`). Its control-coverage and historical-preservation claims are supported by the inspected sources. All 17 template sections are present and all 16 local Markdown references resolve. These are artifact-integrity observations only.

No actionable contradiction or silent mechanism selection was found. The following remain held downstream inputs, not defects to resolve by inventing defaults:

- Exact Entra bindings/grants, claims, cryptography/key/session/revocation/CSRF contracts, emergency generator/MFA/custody and reviewed recovery procedure.
- Rate thresholds, Redis outage response, resource/query/input bounds, schema/error/event contracts, operational authority and restricted alert/audit recipients.
- Class-specific retention clock/legal basis, provider no-training/retention/deletion evidence and restore-suppression policy, applicable legal review and approved staff/accessibility references.
- Privacy/security alias ownership is explicitly undecided under `docs/software-definition/06-entity-and-public-contact.md:106–111`; no founder, general-contact team, triage recipient or response SLA is assigned.
- D-068 defers Azure/AWS hosting/provider/region/cost planning, without replacing Entra staff identity or the approved Azure Europe private-AI route. Outlook/Teams intent remains; no Microsoft 365 prerequisite or unverified API capability is introduced.

## Review limits

This PASS is an independent security/privacy/identity/architecture consistency review of the two exact draft artifacts. It is not legal sign-off, an accessibility conformance verdict, acceptance of exact schemas/grants/mechanisms, founder feature approval, full Phase 1 acceptance, executable planning approval, runtime security certification or launch readiness. The unchecked applicable legal/accessibility, exact-input and founder gates remain valid.

No runtime test was executed, no product test was added for prose, and no application, producer file, authentication/provider/credential/database configuration, external service, installation, commit or push was changed. The only authored artifact is this review.
