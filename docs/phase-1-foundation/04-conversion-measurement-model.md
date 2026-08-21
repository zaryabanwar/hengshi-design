# Visitor-to-Qualified-Booking Value and Measurement Model

**Status:** Phase 1 draft for specialist review; not founder-approved

**Classification:** Business confidential

**Prepared:** 2026-07-19

**Decision scope:** D-005, D-008, D-016, D-017, D-019, and D-020

## Executive Summary

Hengshi Design's approved conversion outcome is a verified, consented, confirmed
30-minute qualified discovery booking. Raw traffic, time in the 3D campus, AI-chat
volume, and generic contact-form submissions are not substitutes for that outcome.
Attendance is the first downstream quality check, but revenue, proposal, and sales
qualification are outside this model because no approved commercial process or
baseline exists.

The booking journey must work directly from the semantic Quick Access experience,
including non-WebGL and reduced-motion paths. AI and live-human help may assist a
visitor, but neither is a prerequisite. The model therefore compares direct, AI,
and human-assisted paths without steering visitors toward any one path.

No conversion, attendance, response-time, or funnel target is approved yet. This
document defines what to measure, the minimum privacy-safe evidence required, and
the baselines that must be established before the founder sets numerical targets.
The only numbers treated as approved targets are the performance, capacity,
availability, RPO, and RTO constraints already recorded in D-020.

## 1. Decision Frame and Source Authority

### 1.1 Decision this model supports

This model supports product, SEO, UX, API/data, privacy, QA, and booking-operations
decisions about whether the public experience helps an intended buyer reach a
trustworthy, recoverable, qualified discovery booking without unnecessary data
collection or dependence on AI, WebGL, or dark patterns.

The decision users are the founder and the future named product/measurement,
SEO/content, booking-operations, privacy, and platform owners. Those roles are not
yet assigned to named people.

### 1.2 Controlling facts

| Fact | Authority | Effect on this model |
|---|---|---|
| Primary audience is global English-speaking mid-market and enterprise technology, data, product, transformation, and innovation buyers; agriculture leads, mining follows, and defense is separately gated. | D-005 | Segment only by approved audience/sector context; defense remains outside public measurement. |
| Primary conversion is a verified 30-minute qualified discovery booking. | D-005 | A generic lead or unverified calendar request does not count. |
| Qualification requires verified email, organization, role, desired outcome, matched wing, timing, and consent; budget is optional. | D-005 detailed record | These are the complete approved qualification fields. No scoring weights are implied. |
| Quick Access must provide equivalent semantic discovery and conversion without canvas. | D-008 | Direct booking and the same qualification contract must work on responsive, non-WebGL, asset-failure, and reduced-motion paths. |
| Anonymous AI, human help, and direct booking are separate valid paths. | D-016 | AI use and human handoff are optional; Teams presence cannot by itself claim staff availability. |
| Non-consented chat is ephemeral; consented chat, brief, and lead data expire after 90 days unless another approved record policy applies; verified deletion includes derived traces. | D-017 | Funnel analytics must not persist chat content or silently turn anonymous chat into a lead. |
| Public content is an approved immutable release; drafts and rejected content never reach public HTML, search, or AI. | D-019 | Public journey evidence must carry a valid public release checksum. |
| Qualified organic discovery/bookings matter more than traffic alone; approved performance and reliability targets apply. | D-020 | Outcome metrics lead the scorecard; traffic is diagnostic context only. |

### 1.3 Evidence classes

- **Approved fact:** the decision records and constitution define intended scope.
- **Prototype evidence:** the current `POST /api/leads`, lead model, contact panel,
  and tests show present behavior but cannot redefine the target.
- **Hypothesis:** audience jobs, funnel drivers, and metric usefulness below must
  be tested through research and measured data before being treated as fact.
- **Unavailable evidence:** no production booking records, approved analytics
  dataset, funnel baseline, buyer interviews, calendar integration, or attendance
  source presently exists.

## 2. Business Outcome Tree

```text
Approved business outcome
└── Win verified 30-minute qualified discovery bookings
    ├── Intended-buyer value
    │   ├── Find a relevant service or sector path without canvas
    │   ├── Understand whether Hengshi may fit the desired outcome
    │   ├── Evaluate verified proof, expertise, and trust information
    │   ├── Choose direct booking, optional AI, or optional human help
    │   └── Book in local time with clear consent, status, and recovery
    ├── Hengshi value
    │   ├── Receive complete, verified, service-matched discovery context
    │   ├── Avoid duplicate meetings and false confirmations
    │   ├── Route confirmed bookings to an approved owner and backup
    │   └── Learn which approved content and paths support qualified outcomes
    └── Trust guardrails
        ├── No fabricated proof or draft-content exposure
        ├── No AI, WebGL, budget, account, upload, or voice/video requirement
        ├── No persistent cross-site or cross-session visitor tracking
        ├── No retention without the approved consent boundary
        └── Verified deletion, expiry, auditability, and prior-release recovery
```

An attended discovery is a downstream validation of booking quality. Proposal,
pipeline, revenue, retention, and client outcomes require a later approved sales
and delivery process and are not inferred from attendance.

## 3. Actors and Jobs-to-be-Done Hypotheses

These jobs are hypotheses, not researched buyer claims. They define what discovery
evidence is needed and do not authorize public messaging.

| Actor | Job-to-be-done hypothesis | Evidence needed before treating it as fact |
|---|---|---|
| Technology, data, product, transformation, or innovation leader | “Help me determine quickly whether Hengshi can credibly address my outcome and give me a low-friction way to discuss it.” | Interviews with verified target-role participants; organic query and booking evidence after launch. |
| Agriculture decision-maker | “Map my sector problem to a practical strategy-to-delivery capability and show relevant, verified proof.” | Agriculture discovery interviews; approved claim/proof inventory; service-fit correction data. |
| Mining decision-maker | “Show that the service and trust model fits a high-risk operational context before I disclose sensitive details.” | Mining discovery interviews; legal/security-reviewed content; privacy-path observations. |
| Trust or technical evaluator | “Let me inspect evidence, experts, security/privacy posture, and delivery approach before I book.” | Trust-page research, proof interactions, interview findings, and booking-path comparisons; interaction is not treated as causal proof. |
| Visitor uncertain about service fit | “Let me ask a bounded question or reach a person, but still let me book directly if help is unavailable.” | Direct versus optional-help journey evidence, refusal/handoff tests, and availability failure tests. |
| Human reception or service owner | “Give me a verified, consented brief and a reconciled meeting without duplicate alerts or ambiguous ownership.” | Approved owner/backups, mailbox/team policy, safe Graph capability tests, and staff workflow research. |
| Founder/content approver | “Show which approved releases and evidence support qualified bookings without rewarding traffic or unsupported claims.” | Release-checksum attribution, proof-status controls, and a reconciled first-party aggregate report. |
| Privacy/security owner | “Minimize collection, preserve consent and deletion evidence, and keep anonymous chat separate from retained leads.” | Legal review, data-flow validation, retention/deletion tests, and audit evidence. |

## 4. Value and State Model

### 4.1 State definitions

| State | Entry condition and visitor value | Exit predicate | Valid alternatives and recovery |
|---|---|---|---|
| `DISCOVERY` | Visitor reaches a public canonical semantic route from organic, direct, or referral entry. The page is meaningful before JavaScript. | Visitor continues to service, sector, proof/trust, help, or booking. | A 3D entry may enhance the route; WebGL failure returns to equivalent Quick Access without losing booking access. |
| `SERVICE_FIT` | Visitor reviews a wing, service, or sector intersection and can understand its formal title and scope. | A service wing is explicitly selected or a context-prefilled wing is confirmed by the visitor. | Visitor may change a prefilled wing; no invisible lead-scoring assignment. |
| `TRUST_PROOF` | Visitor reviews approved work, a clearly labeled Hengshi demo, an expert, insight, or Trust content from the current public release. | Visitor continues, returns to fit, requests help, or books. | Proof review is optional and must never be forced before booking. |
| `HELP_OPTIONAL` | Visitor chooses direct continuation, anonymous Reception AI, or explicitly available human help. | Help ends, hands off, or the visitor proceeds to booking. | AI missing evidence returns “cannot verify” plus human/booking routes. Human unavailability leaves direct booking available. Teams presence may suppress false availability but cannot create availability. |
| `BOOKING_STARTED` | Visitor intentionally opens the canonical booking journey or equivalent booking action. A session-scoped booking lineage is created. | Required qualification data is valid or the visitor exits. | No account, upload, AI conversation, or WebGL state is required. Duplicate starts within the same lineage do not create multiple bookings. |
| `QUALIFICATION_COMPLETE` | Organization, role, desired outcome, matched wing, desired timing, a syntactically valid email address, and consent record are present and valid at the contract level. | One email-ownership challenge is issued or an already current verified state is recognized under the approved verification policy. | This state is not email ownership, slot eligibility, an external booking write, or confirmation. Budget may be supplied but cannot block or improve qualification. Additional mandatory fields require approval. |
| `EMAIL_PENDING` | A current verification challenge exists for the lineage; no confirmed qualified booking is counted. | The challenge becomes verified, expired, undeliverable, or abandoned. | A pending result cannot expose slot selection or booking submission. Safe resend remains under the same lineage and rate-limit/audit policy. |
| `EMAIL_EXPIRED` | The current challenge passed its approved expiry without successful verification. | A safe resend issues a new bounded challenge under the same lineage, or the visitor abandons. | Expiry is explicit, never counts as verification, and cannot create a second lineage or confirmed booking. |
| `EMAIL_UNDELIVERABLE` | The delivery service records a bounded undeliverable outcome; ownership is unverified. | The visitor supplies a syntactically valid corrected address or an approved safe retry/resend returns the lineage to `EMAIL_PENDING`. | The failed address is never promoted to verified. Correction, retry, and retention behavior remain subject to the approved privacy and abuse-control contract. |
| `VERIFIED` | Email ownership has been verified and the qualification/consent record remains valid. | Visitor selects an available 30-minute slot. | No available slot produces an honest unavailable state and a retry or approved human route, never a false confirmation. |
| `SLOT_SELECTED` | Visitor selects a 30-minute time shown in visitor-local time. | An idempotent booking request is durably accepted. | Offline/timeout keeps the request pending or retryable under the same lineage and idempotency key. |
| `BOOKING_PENDING` | The local durable request exists but calendar/meeting confirmation is absent or ambiguous. | Local and approved external booking states reconcile to confirmed, failed, expired, or cancelled. | Provider timeout triggers reconciliation before retry; alerts can retry independently; the UI must not claim confirmation. |
| `CONFIRMED_QUALIFIED` | The qualification definition below passes and exactly one reconciled 30-minute meeting exists for the booking lineage. | Meeting is attended, rescheduled, cancelled, or reaches an unknown/no-show outcome. | A reschedule retains the same lineage and is not counted as a second qualified booking. |
| `ATTENDANCE_HANDOFF` | The scheduled time has passed and the approved status source records attended, no-show, cancelled, rescheduled, or unknown. | Outcome is reconciled and operational ownership is clear. | Unknown remains visible; it is not silently excluded to improve attendance. |
| `RETENTION_DELETION` | Consented chat, brief, and lead records enter the approved 90-day lifecycle; other record classes enter only the lifecycle assigned by the approved data-classification/legal-policy matrix. | A mapped record expires, becomes an approved active-client/legal record, or verified deletion completes across every system explicitly in scope. | Non-consented chat never enters retained lead state. Booking, meeting/provider, consent-proof, audit, and tombstone behavior remains unresolved until mapped; an unmapped class prevents a truthful completion claim. |

### 4.2 Allowed journey shortcuts

- A visitor may move directly from any public discovery route to
  `BOOKING_STARTED`.
- Quick Access, 3D, reduced-motion, low-power, and non-WebGL journeys use the same
  booking and qualification contract.
- `TRUST_PROOF` and `HELP_OPTIONAL` are helpful but never mandatory.
- Declining retention/booking consent does not block continued public browsing or
  ephemeral AI use, but it prevents creation of a retained qualified booking.
- Leaving a state is not treated as failure or used to coerce completion.

## 5. Definition of a Qualified Discovery Booking

A booking counts as one **confirmed qualified discovery booking** only when every
condition below is true for one durable booking lineage:

1. The meeting duration is 30 minutes.
2. Email ownership is verified under the approved verification policy.
3. Organization is present.
4. Role is present.
5. Desired outcome is present in the consented booking record.
6. A formal Hengshi service wing is selected and explicitly confirmed by the
   visitor.
7. Desired project timing is present and is distinct from the scheduled meeting
   time.
8. A valid, purpose-specific consent record exists with timestamp and policy/copy
   version. Exact legal copy remains subject to independent legal review.
9. Exactly one booking request survives idempotency and reconciliation.
10. One 30-minute calendar/meeting record is confirmed for the selected visitor-
    local time and linked to the same booking lineage.

Qualification is a completeness, verification, and service-fit definition. It is
not a lead score and does not assert budget, purchasing authority, organization
size, sales readiness, or commercial fit.

**Budget is optional.** Its presence, absence, or amount cannot determine whether
the booking qualifies. **AI use is optional.** Direct bookings count identically
when the same qualification and confirmation rules pass.

The existing prototype requires `name`, `email`, and `message`, keeps company
optional, and lacks role, matched wing, desired timing, consent, email
verification, availability, idempotency, booking state, attendance, and deletion
state. It is therefore a generic contact-lead implementation, not evidence of a
qualified booking. Making `name` or any other field mandatory in the target
qualification contract requires founder approval.

### 5.1 Current generic-lead workflow and cutover boundary

| Evidence or target | Confirmed state | Unknowns and cutover rule |
|---|---|---|
| Current world-panel form (`apps/web/src/world/WorldPanel.tsx`) | Requires name, syntactically valid email, and message; company, phone, and subject are optional; the success state says only that a message was sent. | It is a prototype contact path, not booking or consent evidence. Production copy, accessibility, privacy notice, retention, and route ownership remain unapproved. |
| Current `POST /api/leads` (`apps/api/app/leads/schemas.py` and `routes.py`) | Validates the generic lead payload, rate-limits with process-local network buckets, immediately commits a lead, and returns `201` with an ID/time. It has no email-ownership challenge, booking lineage, consent record, idempotency key, availability, or provider reconciliation. | FR-015 preserves its documented contract during migration; no existing row is silently reclassified as a verified or qualified booking. Deprecation/versioning and historical-record treatment require the later API/data/privacy contract. |
| Target booking journey | Separates qualification input, challenge issuance, pending/expired/undeliverable/resend outcomes, successful verification, slot selection, durable idempotent acceptance, external reconciliation, and final confirmation. | Exact API operations, challenge provider, expiry/rate limits, consent wording, owner/mailbox, and cutover date remain later Phase 1 gates. Contact and booking may coexist only under an approved route/data contract that states which records each creates. |

This map is current implementation evidence, not authorization to change or migrate
the current endpoint or its data.

## 6. Measurement Contract

### 6.1 Unit and cohort rules

- The business outcome unit is a **booking lineage**, not an event, email address,
  calendar write, visitor, or chat session.
- One booking lineage survives retries, provider timeouts, and reschedules.
- A **valid booking start** is an intentional public booking initiation after
  documented staff/test/crawler exclusions. Repeated starts for the same lineage
  count once.
- Rates use booking-start cohorts and expose unresolved pending lineages at the
  reporting cutoff. Pending records are not silently dropped.
- Organic attribution is limited to the first known entry in the same cookieless,
  session-scoped journey. Cross-session or cross-device influence is reported as
  unknown, not reconstructed through fingerprinting.
- Channel, entry experience, wing, route class, and help path are dimensions, not
  qualification criteria.

### 6.2 Primary outcome KPIs

| ID and type | Definition and formula | Owner and operating status | Measurement source and source status | Baseline and target status | Data minimization and anti-gaming |
|---|---|---|---|---|---|
| **KPI-P01 — Confirmed qualified discovery bookings** (lagging, primary) | Count distinct booking lineages in `CONFIRMED_QUALIFIED` during the reporting period where all ten qualification/confirmation predicates pass. | Business outcome owner; named role holder unassigned. Proposed Phase 1 definition. | Future PostgreSQL booking, verification, consent, and booking-reconciliation records. Source unavailable today; current lead table is insufficient. | Baseline not established. No numerical target approved. | Count one lineage through retries/reschedules; exclude declared staff/test records; never infer qualification from email or calendar events alone. |
| **KPI-P02 — Confirmed qualified organic bookings** (lagging, primary organic outcome) | Count KPI-P01 lineages whose first known same-session public entry is classified `organic_search`. Report `unknown` separately. | SEO/growth outcome owner; named role holder unassigned. Proposed Phase 1 definition. | Future aggregate first-party entry classification joined by session-scoped lineage to KPI-P01 plus valid publication checksum. Source unavailable today. | Baseline not established. No numerical target approved. | Do not use persistent identity, third-party attribution, raw referrer storage, or cross-session inference. Do not hide unknown attribution. |
| **KPI-P03 — Attended qualified discovery rate** (lagging quality outcome) | Distinct KPI-P01 lineages marked `attended` after their final scheduled start, divided by all KPI-P01 lineages whose final scheduled start has passed. Cancelled, no-show, and unknown remain in the denominator; reschedules use the final occurrence. | Booking-operations owner; assignment blocked by MA-006. Proposed Phase 1 definition. | Future staff-console status and/or approved Graph reconciliation. Exact authoritative source is unselected and unavailable. | Baseline not established. No numerical target approved. | Never remove unknown/no-show outcomes to improve the rate; do not collect recordings or transcripts for this metric. |

### 6.3 Driver and diagnostic metrics

| ID and type | Definition and formula | Owner and operating status | Measurement source and source status | Baseline and target status | Data minimization and anti-gaming |
|---|---|---|---|---|---|
| **KPI-D01 — Booking-start-to-qualified completion rate** (leading driver) | KPI-P01 booking lineages divided by valid booking-start lineages in the same start cohort; pending lineages are shown separately at the cutoff. | Product/measurement owner; unassigned. Proposed. | Future aggregate booking-start event reconciled to durable booking state. Unavailable. | Baseline not established; no target approved. | Collapse retry events; publish counts with the rate; document bot/test rules; do not optimize by hiding the booking entry point. |
| **KPI-D02 — Qualification completion rate** (leading driver) | Distinct lineages reaching `QUALIFICATION_COMPLETE` divided by valid booking-start lineages. | Product/measurement owner; unassigned. Proposed. | Future booking state transitions. Unavailable. | Baseline not established; no target approved. | Required fields cannot be prefilled without visitor confirmation; budget cannot affect completion; validation errors remain visible diagnostically. |
| **KPI-D03 — Email verification completion rate** (leading driver) | Distinct lineages reaching `VERIFIED` divided by distinct lineages for which a verification challenge was issued. Expired and undeliverable outcomes remain visible. | Platform/booking owner; unassigned. Proposed. | Future verification challenge and completion records. Unavailable. | Baseline not established; no target approved. | Count a lineage once; do not count message opens; do not store email in aggregate analytics. |
| **KPI-D04 — Verified-slot confirmation rate** (leading operational driver) | Distinct lineages reaching `CONFIRMED_QUALIFIED` divided by verified, qualified lineages that selected an available slot. Pending, failed, expired, and reconciliation-error states are reported separately. | Platform/booking and booking-operations owners; unassigned. Proposed. | Future durable booking/outbox and approved calendar reconciliation. Unavailable. | Baseline not established; no target approved. | Provider timeout is not failure until reconciled; no duplicate retry; never call a locally pending request confirmed. |
| **KPI-D05 — Funnel transition family** (diagnostic) | For each adjacent state, distinct lineages entering the next state divided by distinct lineages entering the prior state. Report counts, exits, validation errors, and pending states. | Product/measurement owner; unassigned. Proposed. | Future aggregate state-transition events reconciled to booking records. Unavailable. | Baselines not established; no targets approved. | Do not rank teams on raw stage volume; preserve voluntary exits and small/unknown cohorts; never introduce coercive UI to move a rate. |
| **KPI-D06 — Entry-experience outcome parity** (diagnostic) | Report KPI-D01 and KPI-P01 by `quick_access`, `3d`, `reduced_motion`, `low_power`, and `non_webgl_or_asset_failure`; compare rates only with cohort sizes and uncertainty visible. | UX/accessibility and product/measurement owners; unassigned. Proposed. | Future first-party entry-experience dimension and booking lineage. Unavailable. | Baselines not established; no numerical parity threshold approved. | No fingerprinting; capability dimension is session-scoped and coarse; do not send visitors to a worse path to manufacture comparison. |
| **KPI-D07 — Assistance-path outcome mix** (diagnostic) | For booking starts, report count and KPI-D01 by `direct`, `ai_assisted`, and `human_assisted`; a lineage may record multiple help interactions but has one declared final assistance path plus `mixed` where necessary. | Concierge/handoff and product/measurement owners; unassigned. Proposed. | Future aggregate help-path transitions joined to booking lineage without chat content. Unavailable. | Baselines not established; no target or preferred path approved. | Do not force AI/human use, claim causality, store conversation content in analytics, or reward chat volume. Direct completion must remain visible. |
| **KPI-D08 — Matched-wing correction rate** (diagnostic content/fit signal) | Booking starts with a route-context-prefilled wing that the visitor changes, divided by booking starts with a prefilled wing. Separately report starts with no prefill. | Product/content owner; unassigned. Proposed. | Future user-confirmed wing state plus public route/release key. Unavailable. | Baseline not established; no target approved. | A prefilled wing never counts until confirmed; changing it cannot reduce qualification or trigger a score. |

### 6.4 Trust, privacy, and operational guardrails

| ID and type | Definition and formula | Owner and operating status | Measurement source and source status | Baseline and target status | Data minimization and anti-gaming |
|---|---|---|---|---|---|
| **KPI-G01 — Duplicate booking creation rate** (idempotency guardrail) | Calendar/meeting records beyond one active meeting for a booking lineage, divided by lineages that initiated an external booking write. Report both count and rate. | Platform/booking owner; unassigned. Proposed. | Future local idempotency/outbox records and approved calendar reconciliation. Unavailable. | Required contract invariant: zero duplicates caused by retries; no observed baseline. | Reconcile provider timeouts before retry; keep reschedule lineage distinct from accidental duplicate creation. |
| **KPI-G02 — Consent integrity exceptions** (privacy invariant) | Count confirmed qualified lineages with missing, expired, mismatched-purpose, or unversioned consent at confirmation. | Privacy owner; assignment and legal review blocked by MA-002. Proposed. | Future versioned consent and booking records. Unavailable. | Required contract invariant: zero confirmed exceptions; no observed baseline. | Consent is not inferred from browsing or chat; no prechecked control; an exception cannot be excluded from audit to protect the KPI. |
| **KPI-G03 — Verified deletion completion and age** (privacy guardrail) | Completion rate: verified deletion requests reaching completed across approved in-scope primary/derived systems divided by all verified deletion requests. Age: elapsed time for each open/completed request, reported in privacy-safe aggregates. | Privacy/data owner; unassigned and legal review required. Proposed. | Future deletion workflow, acknowledgements only from systems mapped in scope, derived-index confirmations, and approved backup/tombstone evidence. Unavailable. | Baseline not established; completion-time target and record-class scope are not approved. | A request stays pending until every approved in-scope system acknowledges it; do not mark success after deleting only the visible lead row or assume an external provider is in scope. |
| **KPI-G04 — Matured booking outcome mix** (quality diagnostic) | Among KPI-P01 lineages whose final scheduled time has passed, report attended, cancelled, no-show, rescheduled, and unknown counts/rates. | Booking-operations owner; assignment blocked by MA-006. Proposed. | Future approved attendance/status source. Unavailable. | Baseline not established; no target approved. | Preserve unknown and late status; keep one lineage through reschedules; do not infer attendance from calendar acceptance alone. |
| **KPI-G05 — Public-release attribution integrity** (publication invariant) | Count public funnel events or booking lineages referencing a missing, draft, rejected, or never-public-at-event-time publication checksum. | Publication/SEO and platform owners; unassigned. Proposed. | Future immutable publication manifest and aggregate event envelope. Unavailable. | Required public-state invariant: zero invalid public references; no observed baseline. | Invalid records are quarantined for investigation, not reassigned to another release; draft interactions are never mixed into public conversion. |

## 7. Approved Targets and Baselines to Establish

### 7.1 Approved targets inherited from D-020

These are engineering and service guardrails for the conversion journey, not
conversion targets. Their detailed test method belongs in the Phase 1 QA and
operability artifacts.

| Guardrail | Approved target | Conversion implication |
|---|---:|---|
| Quick Access LCP | `<= 2.5 s` at p75 | Search visitors can understand and act without a slow canvas path. |
| Quick Access INP | `<= 200 ms` at p75 | Booking and navigation remain responsive. |
| Quick Access CLS | `<= 0.1` at p75 | CTAs and consent controls do not move unexpectedly. |
| Initial 3D transfer | `<= 8 MB` desktop; `<= 4 MB` mobile | Optional 3D cannot consume the semantic booking budget. |
| Incremental room transfer | `<= 5 MB` desktop; `<= 2.5 MB` mobile | Later rooms remain progressive enhancement. |
| Initial load proof | 25 concurrent visitors and 3 simultaneous chats | Foundation capacity includes discovery and help entry. |
| Monthly public site/API/AI-booking-entry target | `99.9%` | Direct booking and recovery must remain available even when an optional subsystem fails. |
| Initial RPO / RTO | `<= 24 h` / `<= 8 h` | Booking and consent recovery must be rehearsed; adequacy remains an explicit launch risk. |

### 7.2 Baselines that do not yet exist

The project must establish, rather than invent, baselines for every KPI in section
6. Baseline collection begins only after the event/booking contracts, privacy
review, exclusions, test markers, and reconciliation checks are approved and
implemented. The measurement owner must then:

1. select a founder-approved observation window and reporting cadence;
2. reconcile aggregate transitions to durable booking lineages;
3. quantify missing, unknown, late, bot, staff, and test records;
4. validate organic and entry-path classification without persistent identity;
5. review cohort sizes and uncertainty before comparing paths; and
6. present measured baselines before proposing numerical conversion, attendance,
   verification, handoff, or response-time targets.

## 8. Minimal First-Party Measurement Envelope

The implementation may choose different internal names, but the approved contract
must support these conceptual facts:

- public release checksum;
- canonical route key and route class, not a raw URL containing query-string PII;
- coarse entry channel: `organic_search`, `direct`, `referral`, or `unknown`;
- entry experience: Quick Access, 3D, reduced motion, low power, or non-WebGL/
  asset recovery;
- random session-scoped journey identifier with no cross-session identity;
- booking lineage identifier only after booking intent;
- formal wing key and whether it was prefilled, confirmed, or changed;
- help path: direct, AI, human, mixed, or none;
- state transition, result, and bounded error class;
- event time; and
- consent purpose/copy version only on the governed consent/booking record.

Aggregate analytics must not contain email, name, organization, role, desired
outcome text, chat content, free-form message, phone, IP address, exact location,
calendar description, or a device fingerprint. Network identifiers required for
security/rate limiting are operational security data, not analytics, and must use
their own approved retention/access controls.

Raw third-party referrers should be classified at collection and discarded.
Unknown attribution remains a valid value. Small-segment suppression and analytics
event-retention periods require privacy/legal approval before reporting.

## 9. Failure, Recovery, Offline, and Idempotency Contract

| Failure or ambiguity | Required process behavior | Measurement consequence |
|---|---|---|
| JavaScript, WebGL, 3D asset, motion, or audio failure | Preserve semantic discovery and direct booking through Quick Access; do not lose the selected service context. | Record only a coarse recovery path; compare outcomes without fingerprinting. |
| AI unavailable, timed out, or lacks evidence | Fail closed with “cannot verify” where applicable and show human/direct-booking routes. | AI failure is diagnostic; direct bookings still count identically. |
| Human not explicitly available | Do not claim live availability. Keep direct booking available; Teams presence can only suppress availability. | Record honest unavailable status, not a failed handoff attributed to the visitor. |
| Qualification validation fails | Explain the affected field and preserve only what the approved privacy/UX contract permits. Do not convert the draft into a lead. | Record bounded validation class, never field content. |
| Consent declined | Continue public browsing and eligible ephemeral help; do not persist chat/brief/lead/booking data. | Record only privacy-approved aggregate outcome; no retained booking lineage. |
| Email challenge expires or delivery fails | Keep state unverified; allow safe reissue under the same lineage; do not confirm a booking. | Show expired/undeliverable separately in KPI-D03. |
| Visitor is offline before durable acceptance | Make non-submission explicit. Do not claim success or create a hidden retained record. | No accepted booking event; optional local recovery must not persist PII without approved controls. |
| Retry or double-submit | Reuse the same idempotency key and return the same accepted result. | One booking lineage and one KPI-P01 outcome. |
| Calendar/meeting provider times out | Keep `BOOKING_PENDING`, reconcile provider state, and retry only after ambiguity is resolved. | Pending stays visible; it is neither success nor failure at cutoff. |
| Calendar confirms but alert fails | Keep the confirmed booking; retry the governed alert separately and expose the staff-console record. | Booking outcome remains valid; alert failure is operational diagnostic. |
| No suitable slot exists | Show an honest no-availability state and an approved retry/human route without promising response time. | Not counted as confirmed; policy and ownership remain a founder gate. |
| Reschedule | Reconcile the existing lineage and final meeting occurrence. | No additional qualified booking; final attendance uses the final scheduled occurrence. |
| Cancellation or no-show | Preserve the terminal status and reason category only where approved. | Remains in outcome mix and attendance denominator as defined. |
| Deletion fails in one approved in-scope primary, derived, or provider system | Keep deletion pending, alert the owner, and follow the approved retry/tombstone rule. A provider is not presumed in scope and a tombstone is not presumed retainable without the data-classification/legal-policy matrix. | KPI-G03 cannot count completion until every approved in-scope acknowledgement exists. |
| Publication render/index fails | Keep the prior approved public release active. | New release receives no public funnel attribution until atomically active. |

## 10. Privacy, Retention, and Deletion Boundaries

1. Anonymous AI text may begin without a visitor account; its content is
   ephemeral unless explicit approved consent creates a retained brief/lead.
2. Voice and video are opt-in and cannot be required for help or booking.
3. A direct booking creates retained data only after the approved consent step.
4. The approved 90-day rule applies to consented chat, brief, and lead data unless
   an approved active-client or legal-record policy applies. It does not, by this
   document alone, set retention for booking, meeting/provider, consent-proof,
   audit, or tombstone records.
5. Verified deletion covers chat, derived traces, brief, and the lead profile.
   Booking, meeting/provider, consent-proof, audit, operational-copy, and
   tombstone behavior remains pending until the approved data-classification and
   legal-policy matrix maps each class, system, authority, retention, exception,
   restoration control, and deletion outcome.
6. Visitor conversations never train models.
7. Aggregate cookieless measurement contains no conversation or qualification
   content and cannot be used to rebuild a visitor profile.
8. Exact consent copy, lawful basis, data-controller details, aggregate retention,
   external-calendar deletion semantics, and small-cell suppression require
   independent legal/privacy review under MA-002.

## 11. Measurement Guardrails and Data-Quality Checks

- Use first-party, cookieless, aggregate-only analytics. No third-party pixels,
  advertising identifiers, persistent visitor IDs, or browser fingerprinting.
- Optimize and report qualified outcomes first; pageviews and 3D engagement are
  supporting diagnostics only.
- Keep direct, AI-assisted, and human-assisted outcomes visible. No path receives
  a preferred target without founder approval.
- Do not report a “qualified opportunity,” sales-accepted lead, won/lost result,
  or revenue influence until a separate founder-approved sales qualification
  taxonomy names its owner, authoritative source, feedback timing, privacy basis,
  and reconciliation rule. A confirmed qualified booking is not automatically a
  sales-qualified opportunity.
- Report counts alongside rates, cohort dates, denominators, pending records, and
  unknown classifications.
- Reconcile `booking_confirmed` measurement with durable booking and provider
  state; event counts alone cannot prove a booking.
- Validate uniqueness by booking lineage and idempotency key, not by email.
- Mark staff, automated QA, preview, and synthetic load traffic at source and
  exclude it through documented rules. Do not retrospectively remove inconvenient
  sessions.
- Confirm every public event checksum exists in the active/recent immutable
  publication ledger; quarantine invalid release references.
- Validate that aggregate event payloads contain no qualification fields, chat
  text, raw referrer, raw IP, secrets, or unrestricted error messages.
- Preserve unknown source, help path, attendance, and failure states rather than
  reallocating them to improve results.
- Treat segment comparisons as descriptive until sample adequacy and uncertainty
  are reviewed; do not claim a page, proof item, AI exchange, or 3D path caused a
  booking from observational data.
- Audit consent-version and deletion reconciliation separately from business
  reporting; a privacy exception cannot be hidden by aggregation.

## 12. Requirement Impacts

| Downstream package | Requirement impact from this model |
|---|---|
| Product requirements | Define qualified booking exactly as section 5; keep budget and AI optional; distinguish generic contact, booking pending, confirmed qualified, and attendance outcomes. |
| SEO/content | Primary CTA routes to canonical semantic booking; organic outcome attribution uses the active publication checksum; draft/rejected releases never appear in public measurement. |
| UX/accessibility | Direct booking remains available from Quick Access and all recovery modes; service-wing prefill requires confirmation; consent is unbundled and not prechecked; failures never claim success. |
| AI/human handoff | AI uses approved knowledge and can refuse; human availability is explicit; neither path is required; no chat content enters aggregate analytics. |
| API/data | Add a versioned booking lineage/state contract, qualification fields, consent record, email verification, availability, idempotency, outbox/reconciliation, attendance status, retention, and deletion evidence. |
| Security/privacy | Separate security rate-limit data, aggregate analytics, ephemeral chat, consented lead data, and later-mapped booking/provider record classes; enforce least privilege and verified deletion only across systems approved in scope. |
| Publication | Attach a valid immutable public release checksum to source context; reject or quarantine draft/invalid attribution. |
| QA | Cover direct booking without AI, non-WebGL parity, required/optional fields, pending/expired/undeliverable/resend/verified transitions, duplicate submit, provider timeout, no-slot recovery, consent decline, 90-day expiry for the approved chat/brief/lead scope, gated record-class behavior, verified deletion, and event/record reconciliation. |
| Operations | Assign booking owner/backups, authoritative attendance/status source, alert fallback, no-slot policy, reconciliation ownership, and reporting cadence before launch. |

## 13. Assumptions and Evidence Gaps

### 13.1 Safe assumptions used

- “Timing” means the visitor's desired project timing and is separate from the
  selected calendar slot; this avoids losing an approved qualification field.
- A route-context wing may be suggested only if the visitor confirms or changes
  it before qualification completes.
- A booking lineage is the minimum unit needed to make retries, reschedules, and
  provider reconciliation truthful without identifying a visitor in analytics.
- Current implementation artifacts are evaluated only to identify migration gaps.

### 13.2 Evidence gaps that do not block this definition

- No approved buyer interview evidence validates the jobs-to-be-done hypotheses.
- No measured funnel, conversion, verification, attendance, or organic baseline
  exists.
- No approved claim/proof/expert inventory exists, so trust-content influence
  cannot be assessed.
- No production booking API, email-verification service, availability source,
  idempotent outbox, Graph reconciliation, attendance source, or deletion workflow
  exists.
- The current lead API and UI collect a generic message and cannot satisfy the
  qualification or privacy contract.
- Named KPI, booking-operations, privacy, content, and platform owners are not
  assigned.
- Legal consent copy, analytics retention, small-cell reporting, and external
  deletion obligations are not approved.
- Booking, calendar/provider, consent-proof, audit, operational-copy, and
  tombstone retention/deletion behavior has no approved class-by-class matrix.
- No approved sales qualification taxonomy, owner, CRM/authoritative source, or
  qualified-opportunity feedback contract exists.
- The booking mailbox, Entra groups, owner/backups, Teams app, and Graph consent
  remain blocked under MA-006.

## 14. Founder and Specialist Decisions Required

These decisions remain open; this document does not make them:

1. Assign named owners and backups for business outcome, SEO/content,
   measurement, booking operations, platform, privacy, and deletion reconciliation.
2. Approve the KPI review cadence, initial baseline observation window, and later
   numerical conversion, attendance, verification, response-time, and no-slot
   targets after measured evidence exists.
3. Decide whether any field beyond the approved qualification set—such as a
   required personal name—may be mandatory. Budget must remain optional under
   D-005 unless that decision is explicitly amended.
4. Approve any future lead-scoring method or weights. None are defined here.
5. Approve sales ownership, response/service levels, no-slot follow-up policy,
   booking mailbox, service owner/backups, attendance authority, and Graph/Teams
   permissions under MA-006.
6. Obtain independent legal/privacy approval for consent wording and purposes,
   controller/contact details, analytics retention, suppression rules, verified
   deletion, calendar-provider deletion, and any active-client/legal exception.
7. Approve any paid analytics or messaging tool. This model selects no vendor and
   requires a first-party cookieless implementation regardless of tooling.
8. Approve a class-by-class retention/deletion matrix for booking,
   calendar/provider, consent-proof, audit, operational-copy, and tombstone
   records without broadening the approved 90-day chat/brief/lead rule by
   inference.
9. If post-booking sales feedback is desired, approve a separate opportunity
   taxonomy, owner, authoritative source, privacy basis, reconciliation cadence,
   and reporting boundary before measuring it.

## 15. Traceability

| Decision | Model sections | Verification implication |
|---|---|---|
| D-005 | 2, 3, 5, 6, 13, 14 | Required qualification fields, optional budget, target audience/sector context, and outcome-first reporting. |
| D-008 | 4, 6.3, 9, 12 | Semantic Quick Access and recovery modes produce equivalent direct-booking outcomes. |
| D-016 | 4, 5, 6.3, 9, 12, 14 | Optional AI/human paths, explicit availability, visitor-local booking, idempotency, reconciliation, and owner gates. |
| D-017 | 4, 6.4, 8, 9, 10, 11, 14 | Consent, 90-day retention, ephemeral non-consented chat, no training, deletion, and aggregate cookieless measurement. |
| D-019 | 4, 6.4, 8, 9, 11, 12 | Active release checksum, draft isolation, prior-release recovery, and attribution integrity. |
| D-020 | 2, 6, 7, 11 | Qualified organic outcomes, approved performance/reliability targets, baselines to establish, and quality guardrails. |

## 16. Phase 1 Validation Checklist

- Every primary, driver, diagnostic, and guardrail KPI has a definition/formula,
  role owner/status, source/status, baseline/target status, minimization rule, and
  anti-gaming note.
- All approved qualification fields are present; budget and AI remain optional.
- Direct booking is available without AI, WebGL, proof review, or human handoff.
- Consent, ephemeral chat, the approved 90-day chat/brief/lead retention scope,
  gated booking/provider record classes, verified deletion, no training, and
  aggregate cookieless analytics remain intact.
- Approved numerical targets are limited to D-020 engineering/reliability targets;
  other baselines and targets are explicitly unestablished.
- Prototype contact-lead behavior is identified as a gap, not promoted as target
  authority.
- Failure, offline, idempotency, pending, reconciliation, reschedule, attendance,
  and deletion states are explicit.
- Evidence, inference, assumptions, and founder decisions are separated.
