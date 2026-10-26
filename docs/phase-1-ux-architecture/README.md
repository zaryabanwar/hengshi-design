# Phase 1 UX Architecture

**Status:** accepted UX baseline under D-036 and subsequent accepted amendments; current v1 references reconciled 2026-10-05. The July three-iteration record remains historical evidence.

**Authority:** [Current decisions](../../DECISIONS.md), including D-039–D-045 and D-064's mouse/touch free-movement addition.

**Implementation status:** BLOCKED until complete Phase 1 acceptance; this entry creates no UI, 3D, application, data, provider or publication permission.

The current World scope references in [flows](FLOWS.md#current-world-scope-amendment--v1)
and [states/recovery](STATES_AND_RECOVERY.md#current-world-scope-amendment--v1)
retain the accepted destination journeys while referencing selected free movement
and the separate proposed movement/loading/audio refinements. They do not accept
gestures, production screens or numerical profiles, reopen accepted stream controls
or grant another substantive UX revision.

## Purpose and boundary

This package turns the accepted Phase 1 foundation, Evidence in Motion strategy,
and frozen Signal Ledger / Framework Relay identity into implementation-relevant
experience flows and states. It defines information architecture and behavior,
not screen design. Semantic Quick Access and visitor-elected immersive exploration are
equal primary journeys; WebGL is progressive enhancement and cannot own exclusive
content, help, or conversion.

The package does not select consent wording, legal identity, staff, service
owners, response times, challenge expiry/rate limits, booking mailbox/calendar
rules, analytics retention or thresholds, external providers, or public claims.
Those choices remain founder or specialist gates.

## Authority and labels

Authority is applied in this order: D-025/D-026/D-035 and project governance;
accepted requirements and foundation artifacts; accepted brand strategy and
identity; current implementation only as protected prototype evidence. D-025
supersedes `ROUTE-INDUSTRIES.plannedCanonicalStatus=founder_decision_pending`:
`/industries` is retained in the planned architecture. No route is currently
content-approved, release-active, or sitemap-active.

Every normative statement uses one of these labels:

- **[APPROVED]** — directly required by accepted authority.
- **[PROPOSED UX]** — reversible interaction detail proposed to implement an
  approved requirement; it still needs independent review and founder approval.
- **[HYPOTHESIS]** — a research or measurement proposition, not a product fact.
- **[UNRESOLVED GATE]** — a choice this package deliberately does not make.

## Artifact map

| Artifact | Purpose |
|---|---|
| [UX architecture](UX_ARCHITECTURE.md) | Actors, jobs, objects, IA, navigation, core journeys, equivalence, first/return visits, content families, controls, responsive and accessibility rules |
| [Route and room parity](route-room-parity.csv) | All 33 route definitions and their Quick Access / immersive stream representation |
| [Excluded surfaces](excluded-surfaces.csv) | All nine exclusion classes and safe UX behavior |
| [Wayfinding and wing release map](wayfinding-release-map.csv) | Exact five-wing/ten-service sign-to-title mapping, room/canonical IDs, release sequence, and closed/held/opening/open behavior |
| [AI, booking, and staff flows](FLOWS.md) | Detailed AI/handoff, booking, search/directory/HUD, and author/reviewer/founder flows |
| [States and recovery](STATES_AND_RECOVERY.md) | Action contracts and comprehensive loading, empty, error, offline, permission, session, provider, Redis, Graph, WebGL, and asset recovery |
| [Content, analytics, and tests](CONTENT_ANALYTICS_TESTS.md) | Content/data needs, missing evidence, privacy-safe analytics hypotheses, and UX acceptance hypotheses |
| [Traceability](traceability.csv) | Requirement/decision-to-artifact mapping and acceptance evidence |
| [Producer inspection](producer-inspection.md) | Scope, consistency, edge-case, and unresolved-gate inspection |
| [Validator](validation/validate-ux-architecture.ps1) | Deterministic route, exclusion, ID, link, label, forbidden-claim, and secret-like-value checks |
| [Validation report](validation/validation-report.md) | Executed command, timestamp, counts, result, and limitations |

## Acceptance boundary

D-036 accepted the exact reviewed UX baseline; subsequent accepted decisions
control its amendments. Producer validation cannot grant acceptance, and historical
review status does not reopen that decision. Material new definitions retain their
own review and founder gates. Production UI still needs approved Figma or Stitch
references before implementation, and complete Phase 1 acceptance remains separate.

Use the [current manual-action index](../../MANUAL_ACTIONS.md) for affected gates,
resolved actions and later activation. MA-004's recorded Atlanta provenance decision
does not clear new production assets. D-068 defers hosting/provider/region/cost
planning with Azure and AWS as candidates; the July Azure-capability wording is
not a current provider selection. No previously resolved action is requested again.
