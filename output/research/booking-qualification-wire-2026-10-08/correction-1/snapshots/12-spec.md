# Staff security and privacy enforcement — v1

## Status and Authority

| Field | Value |
|---|---|
| Status | DOING — proposed feature definition; planning/implementation remain blocked |
| Product/definition | v1; D-069 |
| Product/decision references | Constitution VI/VII; D-015–D-019, D-065, D-068–D-070, D-076; accepted SEC-001–SEC-010, DATA-003–DATA-010, AI-001–AI-009 and PUB requirements |
| Author/producer | Repository definition producer |
| Specialist reviewers | Bounded feature-definition consistency review PASS at preserved inputs; applicable legal/accessibility, exact mechanisms, founder and integrated acceptance remain held |
| Founder approver | Founder; feature and integrated Phase 1 acceptance pending |
| Created / last updated | 2026-10-04 / 2026-10-07 |

The [security/privacy contract](../../docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md)
owns shared control boundaries; this feature binds them to observable enforcement
outcomes. Accepted requirements control; detailed proposals require acceptance.
The [bounded contract review](../../docs/phase-1-architecture/contracts/reviews/current-definition-amendments-2026-10-04.md)
covers its listed hashes, not this feature or implementation.

The earlier [security-feature reconciliation review](../../docs/phase-1-architecture/contracts/reviews/security-feature-reconciliation-2026-10-04.md)
covered authority notices in six June artifacts. The prior spec and checklist are
preserved as byte-identical [spec](history/spec-2026-10-04.txt) and
[checklist](history/requirements-2026-10-04.txt) snapshots taken before this rewrite.
That review does not cover the new active definitions. Historical research, data
model, plan and task-readiness file remain evidence, not executable authority.

## Review-reference reconciliation — 2026-10-06

The [independent feature review](reviews/security-feature-v1-2026-10-04.md)
records bounded definition-consistency PASS with no actionable findings for the
exact [spec](../../output/research/security-feature-review-reference-2026-10-06/spec.reviewed.md)
and [checklist](../../output/research/security-feature-review-reference-2026-10-06/requirements.reviewed.md)
preserved here. This later reference/status reconciliation is outside those
inspected bytes. It changes no requirement, scenario, control, grant or approval
boundary. Applicable legal/accessibility evidence, exact inputs, founder feature
and integrated Phase 1 acceptance remain held; no implementation is authorized.

## Founder amendment reconciliation — 2026-10-07

[D-076](../../DECISIONS.md#d-076--visitor-inactivity-eu-privacy-baseline-and-production-data-deferrals)
settles visitor conversations at 30 minutes of inactivity or authorized explicit
End, with no absolute conversation duration. Staff authentication still has its
separate accepted 30-minute idle/eight-hour absolute bounds. Concrete admission,
warning, More time and End mechanisms in the amended [visitor access profile](../../docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md#access-lifetime-retention-and-pending-cleanup)
and [handoff timing definition](../../docs/phase-1-architecture/contracts/HANDOFF_LIFECYCLE.md#timing-conflict-requiring-a-scoped-decision)
remain mechanism proposals requiring acceptance and actual enforcement evidence. The later [26-input visitor-control review](../../docs/phase-1-architecture/contracts/reviews/visitor-lifetime-controls-v1-2026-10-07.md) gives bounded control-definition PASS; it selects no concrete credential/store/fencing mechanism or complete-process accessibility solution. The earlier feature PASS does not cover this amendment.

The [EU privacy/retention proposal](../../docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md#eu-privacy-and-retention-policy-proposal--2026-10-07)
has a separate [eight-input bounded recommendation review](../../docs/phase-1-architecture/contracts/reviews/eu-privacy-retention-v1-2026-10-07.md) and remains the working source for proposed lawful purposes, class clocks, rights, copies
and transfers. New periods/bases are not accepted defaults, a blanket 90-day rule
or legal clearance; the classification matrix is not silently rebound. D-076
defers public registration details and the supplied registered address while
preserving admin-editable private facts and mandatory disclosure assessment.
Use fictional non-sensitive local data; real records arrive later through the
intended admin workflow under applicable review/privacy/publication controls.
Alias ownership stays undecided. No account, service or implementation task is
created by this amendment.

## Problem, Audience, and Evidence

Staff need to edit, independently review, approve and operate within explicit
permissions. Visitors need usable public information and permitted help without
unnecessary accounts, private-data leakage or false security claims. An
administrator role cannot substitute for publication, conversation, booking or
privacy authority.

Current source inspection shows `apps/api/app/auth/deps.py:48–51` returns any
current authenticated user from `require_admin`, preserving R-004's authorization
gap. `apps/web/src/admin/RequireAdmin.tsx:8` and `apps/web/src/lib/api.ts:63` read
browser localStorage tokens; `apps/api/app/auth/routes.py:29–34` returns a token
response. These are protected prototype gaps, not launch behavior or authorization
to repair application code before Phase 1 acceptance.

## Goals and Success Measures

| Goal | Measurable outcome | Evidence source |
|---|---|---|
| Enforce staff authority | Every protected action/read is permitted only for current approved identity, grant, object/purpose and state; wrong/missing/stale authority denies | Actual API/job and concurrent mutation/projection tests |
| Protect staff authentication sessions | Approved rotating staff cookie session, CSRF, logout and 30-minute idle/eight-hour absolute bounds enforced | Actual browser/API and clock-controlled evidence |
| Control emergency access | Exactly two dormant accounts; activation, bcrypt verification, local MFA, alerts, review and rotation enforced | Isolated emergency-procedure and denial evidence |
| Prevent hidden data use | No prohibited persistence, provider transfer, training or telemetry path; class-specific expiry/deletion survives restore | Actual stores/adapter boundaries and isolated recovery evidence |
| Preserve truthful public access | Held private functionality cannot fabricate availability/confirmation or make public content require staff/visitor login | Semantic/browser and process-boundary cases |

No test count, documentation pass or new login latency number certifies security.

## Non-Goals and Protected Scope

- No visitor registration, upload, social-login option or public API-key service.
- No new role hierarchy, administrator override, delegated permission or identity
  assignment; unresolved grants deny the affected action.
- No selected cookie name, signing algorithm/key scheme, MFA method, CSRF package,
  rate threshold, sanitizer or retention clock from the historical proposal.
- No tenant/account/mailbox setup, credential change, migration, package upgrade,
  WAF/cloud activation, paid resource, commit, push or deployment.
- Preserve the application, Atlanta GLB and other accepted artifacts. Cloud hosting,
  region and cost planning remain deferred under D-068; Azure/AWS are candidates.

## User Journeys and Failure Journeys

### Primary journey

1. Authorized staff authenticate using approved Entra identity; ambiguous, absent
   or disabled membership cannot create a permitted session.
2. The console exposes permitted work. The API/job separately checks current
   identity, action grant, object/purpose and exact revision at its boundary.
3. Content contributions require independent applicable review and founder
   approval of the exact current candidate. Editing invalidates old evidence.
4. Private assignment, booking reconciliation, activation and audit inspection
   require their separately approved authority; content roles do not grant it.
5. Logout revokes the applicable session and clears its browser credentials;
   repeated logout remains harmless. Emergency access has a separate controlled
   procedure and never bypasses publication/legal/consent restrictions.

### Accessibility and non-WebGL equivalent

1. Staff authentication, expiry, error recovery and permitted actions need approved
   keyboard/screen-reader references and WCAG 2.2 AA complete-process validation.
2. Public semantic information and independent Book/Contact paths remain usable
   without staff authentication, visitor registration, World traversal or sound.
3. Denial/error information must be understandable without exposing another
   person's private record, account existence or hidden operation details.

### Failure and recovery

1. Missing/revoked identity, unmapped grants, stale object revision or missing
   purpose/consent denies the affected operation rather than guessing authority.
2. Rotation/replay, cross-site writes, expired sessions and uncertain distributed
   limiter state follow accepted exact controls; no historical Bearer/localStorage
   fallback or single-process production bypass is assumed.
3. Unknown provider/deletion/booking outcomes stay pending or denied as applicable;
   they do not become successful transfer, deletion or booking confirmation.
4. Restore remains quarantined until approved expiry/deletion/withdrawal decisions
   and privacy-safe serving prerequisites are verified.

## Functional Requirements

| ID | Requirement | Priority | Verification |
|---|---|---|---|
| FSC-01 | Enforce Entra-backed staff identity and separate author, reviewer, founder approver and administrator responsibilities; missing/disabled/ambiguous mapping denies | Must | Actual authentication and role/action/object denial cases |
| FSC-02 | Recheck authenticated identity, explicit action grant, object/purpose scope and valid state/revision at every protected read/mutation/job boundary; no client role, ID or queued payload grants authority | Must | Direct API/job, list/search/count/error projection and interleaving tests |
| FSC-03 | Deny same-material author review/approval even with combined roles; edited snapshots invalidate prior reviews/approval; activation requires separate permitted operational authority | Must | Exact-candidate and concurrent contribution/review/activation cases |
| FSC-04 | Use rotating JWT staff authentication sessions in Secure/HttpOnly/SameSite cookies, 30-minute idle/eight-hour absolute limits, validated token identity and revocation; exclude browser localStorage credential transport. These staff clocks do not limit visitor conversation proof/access, governed separately by FSC-14 | Must | Actual cookie/client-store, rotation/replay/revocation and controlled-clock tests |
| FSC-05 | Enforce approved CSRF proof on state-changing browser requests and idempotent server logout; explicit approved production origins replace wildcard trust | Must | Actual browser/API cross-site denial, CORS and repeat-logout cases |
| FSC-06 | Keep exactly two local emergency accounts dormant normally; require controlled activation, bcrypt verification, local MFA, alerts, review and post-use rotation; random credentials at least 24 characters with approved entropy/custody | Must | Isolated lifecycle, negative factor/activation and credential-policy evidence without values |
| FSC-07 | Use Redis-backed account/network counters and progressive delay across workers; exact thresholds/outage behavior require acceptance; no indefinite unrelated-account lockout or unprotected default bypass | Must | Distributed limiter/outage and account/network separation cases |
| FSC-08 | Validate typed inputs and render safely for their output context; rich content needs an approved allowlist; bound resource/asset work using exact reviewed contracts | Must | Actual request, persistence, rendered output and malicious URL/content/asset denial cases |
| FSC-09 | Apply least privilege, restricted CORS/CSP/WAF, encryption in transit/at rest, approved secret storage, redacted logs and alertable security events without inventing provider configuration | Must | Configuration/bundle/log inspection and actual control/alert behavior |
| FSC-10 | Enforce purpose/version-specific consent, non-consented ephemeral handling, no training and approved class/provider routes; unknown/unmapped/prohibited data denies transfer and unauthorized persistence | Must | Actual network/store/adapter denial and no-content diagnostic evidence |
| FSC-11 | Apply approved 90-day expiry only to mapped consented chat/brief/lead; enforce verified scoped deletion and restore suppression with class-specific legal/provider policies; unknown outcome remains unresolved | Must | Controlled-clock storage/derived-copy/provider and quarantined restore cases |
| FSC-12 | Preserve current availability, consent and separately authorized handoff/booking truth; security or administrator access must not fabricate people, consent, verification, slots or confirmation | Must | Actual private-operation and projection denial cases referencing canonical process contracts |
| FSC-13 | Restrict/redact audit and diagnostic inspection/export to approved purpose/grants, preserve event integrity and audit inspection; require applicable legal/security review before public claims/notices or defense release | Must | Scope/export/event and release-hold cases; separate applicable review evidence |
| FSC-14 | Under D-076, visitor conversations expire after 30 minutes of inactivity or authorized explicit End, with no absolute conversation duration. Retain accepted accessible warning/extension and permitted-progress obligations; staff, booking, resource and retention clocks remain separate | Must | Actual controlled-clock visitor, cross-tab and End journeys; concrete mechanisms need reviewed contracts |

## Non-Functional Requirements

| ID | Area | Measurable target | Verification |
|---|---|---|---|
| FSC-N01 | Boundary integrity | No authorization decision based solely on the UI, stale session labels or historical approval | Public-boundary denial/interleaving evidence |
| FSC-N02 | Privacy | No real secrets/private payloads in source, docs, bundles, general logs or generated assurance artifacts | Actual bundle/store/log inspection with synthetic canaries and approved scan scope |
| FSC-N03 | Accessibility | WCAG 2.2 AA target; no conformance claim until complete-process evidence | Approved staff references and keyboard/assistive-tech checks |
| FSC-N04 | Recovery | Preserve accepted RPO 24h/RTO 8h targets and privacy-safe reconciliation; unknown mappings cannot certify recovery | Feature 002 and canonical QA/recovery evidence |
| FSC-N05 | Performance | Preserve existing accepted website/device/load targets; exact security request/limiter/resource profiles remain held | Accepted named-profile runtime evidence; no inherited June 200ms target |
| FSC-N06 | Diagnostics | Purpose-bound redacted events; no permanent exact movement history/device fingerprint or invented alias owner | Actual diagnostic/network/storage access evidence |

## SEO and Publication Requirements

Staff/private/draft surfaces and records must not enter public HTML, retrieval,
sitemaps, indexable metadata or World assets. Robots exclusions are not access
control. Security controls cannot publish pending content or turn Trust targets
into achieved certification. Public company/contact/security/privacy content uses
reviewed exact facts/copy and coherent immutable publication, including any later
operational contact claims. D-070 supplies company facts and aliases, not legal
sign-off or functioning mailboxes. The nature campus creates no physical office
or environmental performance claim.

## Data, Privacy, and Security

| Data/actor | Classification | Purpose/consent | Retention/deletion | Access/control | Region/provider |
|---|---|---|---|---|---|
| Staff identity, session and emergency records | Private/secret as mapped | Approved identity/security purpose | Exact class policy held; no blanket chat duration | Current scoped authority; secret values excluded from evidence | Exact identity/store configuration held |
| Non-consented chat | Personal/confidential as applicable | Ephemeral approved guidance only | No durable application/log/training copy; vendor policy must also satisfy route | No implicit operational sharing | Approved verified route; unknown classification denies |
| Consented chat/brief/lead | Mapped personal/confidential | Specific accepted purpose/consent | Approved 90-day rule; clock/legal wording held; no reset on resume/restore | Purpose-bound approved staff/process grants | PII/confidential AI restricted to verified Azure Europe route |
| Booking/provider, consent proof, audit and suppression records | Separate canonical classes | Separately reviewed operational/legal purpose | No inferred 90-day or indefinite tombstone; mappings held | Explicit approved operation/read/export grants | Reviewed contracts and capabilities required |
| Diagnostic/aggregate evidence | Classification/policy still required | Minimal approved assurance purpose | Exact retention/small-cohort rules held | Redacted and restricted; no visitor profile | No new monitoring/provider route selected |

Use the canonical classification matrix; it supplies proposed boundaries, not
legal authority. Privacy/security alias ownership stays undecided by explicit
founder instruction. No default monitoring/triage recipient or response SLA is
created. Source byte snapshots contain only existing documentation, no credentials.

## AI and Human-Handoff Requirements

Approved evidence/version eligibility, visible substantive sources, injection
refusal and nonbinding answers follow AI-001–AI-009. Model output cannot grant a
role, call arbitrary tools or approve content/price/scope/booking. Prohibited data
is refused without echoing or retaining the sensitive value. Approved PII/private
AI remains on its verified Azure Europe route; NVIDIA initially receives only
public or demonstrably de-identified material under its entitlement gates. An
outage cannot authorize less protected failover.

Staff help requires current explicit availability and separately consented
purpose-permitted context. Teams presence can suppress false availability;
alerts neither assign a conversation nor confirm a booking. The feature cannot
infer mailbox ownership, staff grants or Microsoft 365 necessity. Exact approved
Outlook/Teams/Entra account and API capabilities still require separate evidence.

## Interfaces and Data Contracts

| Contract | Producer/consumer | Compatibility | Idempotency/recovery |
|---|---|---|---|
| Security authorization/session contract | Identity and approved principal → protected API/job | Exact claims, binding, CSRF/rotation/key/session rules held | Current identity/scope checks; approved logout/revocation semantics |
| Staff/process/interface catalogue | Authorized principal → content/private operations | Logical fields are not accepted wire schemas/grants | Stale revisions/uncertain effects cannot grant authority |
| Classification and logical data contracts | Permitted collection → durable/derived/provider copies | Class-specific purpose, access and legal policy required | Deletion/expiry and restore suppression verified across approved scope |
| Immutable publication contract | Reviewed exact candidate → approved activation | All derivatives/streams and eligibility checks agree | Concurrent or unknown effects use authoritative reconciliation |
| QA/recovery contract and feature 002 | Canonical owners → actual runtime assurance | Approved isolated scope and actual implementation required | Failure, concurrency and restoration evidence; no mocks-only certification |

This feature selects no new endpoint, status/error envelope, schema, SQL column,
cryptographic algorithm, rate number, service identity or permission grant.

## Technology Constraints

Retain FastAPI, SQLAlchemy, Alembic, PostgreSQL, JWT/bcrypt, React/TypeScript and
approved Entra identity/Redis protection families. Exact packages/mechanisms need
Context7, primary documentation and the latest mutually compatible stable graph;
no historical dependency or independently newest release is selected here. Native
local operation needs no Docker. D-068 defers hosting/provider/cost selection;
this does not replace accepted Entra or private-AI routing constraints.

## Acceptance Scenarios

1. **Given** absent, disabled or ambiguous staff mapping, **when** an actual protected request/job executes, **then** access is denied and no browser or supplied role can elevate it; a separately permitted control case succeeds.
2. **Given** a valid staff session, **when** wrong action/object/purpose, stale revision or unmapped operational grant is used, **then** direct/read/list/search/count/error projections and mutation deny without leaking private records; changing a grant between initial inspection and mutation is respected. Accepted SEC-002 specifically requires an authenticated non-administrator to receive 403 for administrator operations even after the frontend guard is removed; other exact error mappings remain held.
3. **Given** a contributor with combined author/reviewer/founder/administrator labels, **when** they review/approve their own material or activate without separate authority, **then** denial persists; an independent eligible exact-candidate path succeeds and an edit invalidates it.
4. **Given** a staff browser session, **when** actual cookies, stores and token lifecycle are inspected, **then** approved attributes, rotation and identity/key checks hold, no localStorage staff token is used, and replay/invalid issuer/audience/revocation fail under the accepted exact contract.
5. **Given** a staff JWT authentication session and a controlled clock, **when** idle reaches 30 minutes or absolute duration reaches eight hours despite ongoing use, **then** the staff session expires at its accepted boundary; repeat logout is harmless and the staff credential/session cannot be reused. Visitor conversation proof/access retains FSC-14's separate inactivity/End policy and no absolute-duration limit.
6. **Given** cross-site or missing/invalid CSRF proof, **when** a state-changing browser request is made, **then** it fails before a side effect; CORS cannot authorize the action, and approved-origin/valid-proof controls still require scoped identity.
7. **Given** both emergency accounts dormant, **when** normal login or unauthorized activation is attempted, **then** access denies; authorized activation still requires bcrypt and local MFA, creates activation/use alerts and audit, and requires post-use review/rotation without bypassing role/legal/consent restrictions.
8. **Given** synthetic candidate emergency credentials, **when** the approved generator/entropy/storage policy is exercised, **then** short, weak or reused values are rejected before account creation; evidence contains metadata/outcomes only and exactly two approved dormant accounts are maintained.
9. **Given** multiple workers and account/network attempt combinations, **when** accepted limits/progressive delays or Redis loss occur, **then** shared counters and approved outage behavior hold with bounded retry guidance, no default bypass and no indefinite unrelated-account lockout. Exact thresholds/outage controls remain inputs.
10. **Given** malicious strings, rich content, URL/asset paths and boundary inputs, **when** actual requests, persistence and rendering occur, **then** typed/context-specific controls prevent execution, unsafe fetch and unbounded work without treating blanket tag stripping or fixture validation as proof.
11. **Given** synthetic secrets/private canaries and critical security events, **when** bundles/logs/diagnostics and alert controls are inspected, **then** no credential/private-content leakage or wildcard trust exists; approved restricted event recipients work and unmapped recipients are not invented.
12. **Given** no collection consent or unknown/unmapped/prohibited data, **when** actual persistence, telemetry, AI adapter and training destinations are exercised, **then** unauthorized copies/transfers deny; permitted classified controls use only their verified approved route, and outage does not authorize fallback.
13. **Given** mapped consented chat/brief/lead at its approved expiry, **when** resume, derived-copy use, deletion or restoration is attempted, **then** expiry is not reset and approved removal/suppression holds across scoped copies. Unmapped classes/unknown provider outcomes keep completion pending; a quarantined restore cannot serve resurrected records.
14. **Given** stale availability, withdrawn consent, unauthorized assignment or uncertain booking evidence, **when** a content/admin role attempts private operations or public projection, **then** no presence, consent, verified email, slot or confirmation is fabricated; approved independent Book/Contact recovery remains available.
15. **Given** audit/privacy/export requests or pending Trust/legal/defense content, **when** read/export/publication is attempted, **then** purpose/grants/redaction, audit integrity and applicable review holds apply; author/admin status or robots directives cannot bypass them.
16. **Given** keyboard/assistive technology and non-WebGL visitors, **when** authentication/denial/expiry and public alternatives are used, **then** approved complete-process references govern focus/error recovery and equivalent public access; browser automation alone cannot establish full accessibility conformance.

17. **Given** a visitor conversation legitimately active beyond the former two-hour proposal, **when** time advances, **then** elapsed age alone does not end it; 30 minutes of inactivity or authorized explicit End terminates visitor authority. Staff authentication retains its independent accepted limits.
18. **Given** a visitor reading an offered preview, **when** idle warning appears, **then** accepted usable response time, accessible extension and permitted-progress obligations apply. Reviewed More time must acknowledge current server admission; polls, duplicates and provider output cannot manufacture activity, and expired or ended authority cannot be resurrected. Specific mechanism bindings and actual enforcement remain held despite bounded control-definition review.
19. **Given** End racing a message or pending operation, **when** authority and outcomes reconcile, **then** terminal authority prevents later delivery under that process, unknown ending is not reported complete, and neither booking cancellation nor completed scoped deletion is inferred. Exact ordering and response mechanisms follow accepted process contracts.

These are future behavior oracles from requirements, not executed tests. Exact
methods and pass/fail inputs must be accepted before planning and implementation.

## Dependencies and Manual Inputs

| Dependency/input | Owner | Needed by | Blocking behavior |
|---|---|---|---|
| Exact Entra bindings, grants, session/key/CSRF/emergency controls | Identity/security authorities and founder | Authentication/authorization planning | Unmapped action denies; no invented identity or bypass |
| Limiter thresholds/outage/resource/input policies | Security/architecture authorities | Distributed and boundary controls | Historical numbers/packages cannot supply acceptance |
| Class-specific legal retention/deletion/provider agreements | Legal/privacy/data authorities | Collection, transfer, expiry and restore | Affected route/completion remains held |
| Final staff/visitor references and actual test scope | Design/accessibility/QA authorities | Browser and isolated behavioral evidence | Drafts and protected prototypes cannot substitute |
| Exact alert/diagnostic recipients and channel readiness | Operational roles not assigned here | Activating controls/contact claims | Alias owners remain undecided; no implied recipient |
| Applicable specialist evidence and full Phase 1 acceptance | Nonproducer specialists and founder | Planning and application implementation | Bounded definition review PASS; exact inputs, applicable legal/accessibility and founder acceptance remain held; no implementation permission |

## Open Decisions and Assumptions

| Item | Type | Material impact | Proposed default | Approval required |
|---|---|---|---|---|
| Exact identity, session/CSRF/key and emergency procedure | Decision | Privileged access and revocation | Retain accepted controls; methods held | Relevant independent review and founder acceptance |
| Thresholds, outage, safe input/resource and response contracts | Decision | Abuse protection, correctness and availability | Do not inherit June defaults | Security/architecture review and acceptance |
| Retention clock/legal/provider/restore mappings | Decision | Private-data persistence and legal disclosure | Fail closed for unmapped use; unknown deletion stays pending | Legal/privacy/data review and acceptance |
| Operational grants/recipients and alias ownership | Held input | Access, alerts and public operation claims | No assignment; ownership explicitly undecided | Separate supplied/approved scope before activation |
| Historical source preservation | Recorded assumption | Audit trail and one active definition | Byte-identical text snapshots retain prior reviewed source | Safe reversible preservation; no historical verdict transferred |

## Review and Approval

- [x] Bounded security/privacy, identity and architecture feature-definition consistency review PASS at the preserved inputs linked above; no runtime security verdict or acceptance of exact mechanisms.
- [ ] Applicable legal/public-content and accessibility review complete.
- [ ] Exact mechanisms, grants, class mappings and held assumptions accepted.
- [ ] Founder feature and integrated Phase 1 acceptance recorded.
- [ ] Current research/data/contracts/plan/tasks generated from accepted inputs.

No producer inspection self-approves the draft or converts historical review into a
current verdict. No runtime tests, security certification or release claim follow.

## References

- [Accepted product requirements](../../docs/phase-1-foundation/01-product-requirements.md), SEC/DATA/AI/PUB sections.
- [Security/privacy contract](../../docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md).
- [Data classification](../../docs/phase-1-architecture/contracts/data-classification.csv) and [logical data](../../docs/phase-1-architecture/contracts/DATA_CONTRACT.md).
- [Process/interface catalogue](../../docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md) and [publication contract](../../docs/phase-1-architecture/contracts/PUBLICATION_CONTRACT.md).
- [QA/recovery](../../docs/phase-1-architecture/contracts/QA_RECOVERY.md) and [QA feature](../002-testing-and-monitoring/spec.md).
- [Company/contact facts](../../docs/software-definition/06-entity-and-public-contact.md), D-070 and held ownership.
- Root DECISIONS.md, constitution and [reconciliation map](../../docs/software-definition/04-reconciliation-map.md).
