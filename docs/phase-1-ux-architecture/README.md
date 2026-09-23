# Phase 1 UX Architecture

**Status:** producer iteration 3 of 3; final SC 1.2.5 correction complete; exact-freeze independent review pending  
**Authority date:** 2026-07-20  
**Implementation status:** blocked; this package authorizes no UI, 3D, application, data, provider, or publication work

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

The package is ready for independent UX/design and accessibility review only
when the validator passes and producer inspection is complete. The producer does
not approve its own work. Founder approval is required after review. Production
UI must still be designed/referenced in Figma or Stitch before implementation.

The following remain visible gates: MA-002 legal/privacy disclosures; MA-003
claims, experts, owners and proof; MA-004 GLB provenance; MA-005 Azure capability;
MA-006 mailbox, groups, calendar and Teams consent; MA-007 NVIDIA entitlement;
MA-008 domain; MA-009 webmaster ownership; MA-010 paid envelopes; MA-011 defense;
and MA-013 compatibility-inventory acceptance.
