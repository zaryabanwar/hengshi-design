# Phase 1 Foundation Requirements Review — Iteration 1

**Date:** 2026-07-19  
**Verdict:** **REVISE**  
**Actionable findings:** 4 (3 high, 1 medium)

## Independence statement

I did not produce or edit the reviewed foundation artifacts. This verdict is based on direct inspection of the named requirements, SEO, conversion, claims, route, and traceability artifacts plus the controlling project decisions and risks. Coordinator inspection or producer validation is not treated as independent review evidence. No web research, application inspection, private-system access, or legal conclusion was used.

## Findings

| ID | Severity | Exact locations | Problem | Required correction |
|---|---|---|---|---|
| REQ-R1-001 | High | `06-canonical-route-inventory.json:31-41,252-262,421-457`; `README.md:34-36`; `03-seo-entity-route-editorial-strategy.md:297-306` | The machine inventory conflates planned route direction with release activation. `/industries` is still founder-gated and About, Contact, and Book have unsatisfied content/owner/consent gates, yet each is `index` with `sitemap: true`. Conditional collections use different semantics. A consumer cannot determine whether `sitemap` is a future target or current release eligibility. | Define separate planned-canonical, content-approved, release-active, indexability, and active-sitemap states. Derive actual sitemap inclusion only from an approved active release. A pending founder/content gate must not serialize as currently sitemap-eligible; preserve `/industries` as pending until its decision is recorded. |
| REQ-R1-002 | High | `01-product-requirements.md:132-135`; `04-conversion-measurement-model.md:122-129,145-161,296-303` | FR-004 says a submission rejects an unverified email, while the state model must first accept an email to issue a challenge and then permits verification before slot selection/booking creation. “Submission” and “booking request” therefore identify different operations across artifacts. Expired/undeliverable verification and retry behavior appears only in recovery prose, not as explicit transition outcomes. | Split the contract into atomic operations: accept a syntactically valid address for challenge issuance; keep the lineage unverified while pending/expired/undeliverable; allow safe resend under the same lineage; block slot booking/final confirmation until verification succeeds. Align FR-004, FR-007, state transitions, API contract, and acceptance tests to those terms. |
| REQ-R1-003 | High | `01-product-requirements.md:219-225`; `04-conversion-measurement-model.md:130,309-325` | DATA-005 applies the approved 90-day rule to consented chat, brief, and lead data. The conversion model expands it to booking and “booking-related” records, while also stating that external-calendar deletion semantics require legal/privacy review. This silently resolves an unapproved retention scope and creates contradictory implementation authority. | Keep the approved 90-day scope limited to chat/brief/lead records. Mark retention and deletion for booking, meeting/provider, consent-proof, audit, and tombstone records as unresolved data-classification/legal-policy gates until approved; then trace each class to retention source, deletion behavior, and exception authority. |
| REQ-R1-004 | Medium | `01-product-requirements.md:233`; `DECISIONS.md:32`; `docs/decisions-log.md:180-188` | SEC-003 is labeled an approved constraint sourced only to D-018, but the cited decision does not establish the exact `24+` credential length. The row also bundles account count, hashing, credential generation, MFA, activation, alerts, and rotation into one acceptance unit. | Either cite a durable approved source for the exact length or mark that numeric control as a proposed security specification pending approval. Split the independently testable break-glass controls into atomic requirements (or separately enumerated acceptance cases) without weakening the approved two-account/MFA/monitoring boundary. |

## Residual human gates

- Founder: accept or reject `/industries`; approve any added mandatory booking field, KPI cadence/window/targets, named owners/backups, no-slot/service-level policy, and any pricing, timing, cost, or contractual commitment.
- Legal/privacy/security: approve consent copy/purposes, data classification, booking/calendar/consent/audit retention and deletion, crawler policy, and any active-client/legal-record exception.
- External capability: booking mailbox, Outlook/Teams/Graph permissions, attendance authority, domain/webmaster ownership, and provider capability remain unverified and inactive.

## Validation and limitations

Both JSON files parsed and the 24-row CSV imported successfully. `validation/validate-foundation.ps1` passed all 37 structural checks. KPI rows in the conversion model define formulas, owner/source status, baseline/target status, minimization, and anti-gaming; no KPI-definition finding was identified. Structural validation does not assess semantic atomicity, cross-artifact state meaning, legal correctness, live integrations, route activation, or measured baselines. Findings above are documentary evidence; recommendations are corrective inferences constrained to the approved decisions.
