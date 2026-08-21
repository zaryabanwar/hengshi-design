# Phase 1 Foundation Slice

**Project:** Hengshi Design

**Snapshot:** 2026-07-19 (Asia/Karachi)

**Workflow state:** Definition foundation passed two independent review loops and final deterministic validation; ready for bounded founder review, not founder-approved, and not authority for application development or publication

## Purpose

This folder contains the first bounded Phase 1 definition slice. It converts the approved Phase 0 decisions into reviewable product requirements, market and SEO evidence, route and entity rules, a conversion model, and explicit evidence quarantine. It does not complete Phase 1 and does not authorize application, UI, 3D, dependency, database, cloud, AI-provider, publication, deployment, or external-account work.

The existing application and exterior GLB remain protected prototype evidence. Historical requirements, seeded cases, prototype copy, people, legal details, contact details, social profiles, locations, metrics, and commercial claims remain non-public unless the claims ledger explicitly records approved evidence and the later publication workflow approves them.

## Artifact map

| Artifact | Role | Current authority |
|---|---|---|
| [01-product-requirements.md](01-product-requirements.md) | Atomic business, product, SEO, publication, experience, AI, data, security, quality, and operating requirements | Phase 1 proposal derived from D-001 through D-024; founder acceptance still required |
| [02-market-competitor-seo-evidence.md](02-market-competitor-seo-evidence.md) | Dated comparison of the founder-supplied references and current primary SEO/crawler guidance | Research evidence and hypotheses; it does not approve claims, keywords, routes, or reference-inspired features |
| [03-seo-entity-route-editorial-strategy.md](03-seo-entity-route-editorial-strategy.md) | Entity, search-intent, route, rendering, schema, crawler, editorial, and measurement policy proposal | Phase 1 proposal; legal, founder, security, privacy, content, and platform gates remain |
| [04-conversion-measurement-model.md](04-conversion-measurement-model.md) | Visitor-to-qualified-booking state, KPI, privacy, recovery, and data-quality contract | Phase 1 proposal; baselines and external integrations do not yet exist |
| [05-evidence-and-claims-ledger.json](05-evidence-and-claims-ledger.json) | Machine-readable evidence eligibility and quarantine ledger | Binding safety input for this slice; it grants no publication approval |
| [06-canonical-route-inventory.json](06-canonical-route-inventory.json) | Machine-readable planned canonicals, content/release states, indexing policy, active-sitemap state, schema limits, and deterministic exclusions | Proposed inventory; no route is active in this planning snapshot, `/industries` remains founder-pending, and detail instances activate only through an approved release |
| [07-decision-requirement-traceability.csv](07-decision-requirement-traceability.csv) | D-001 through D-024 coverage and next-slice dependencies | Traceability evidence; later-slice dependencies remain open by design |
| [evidence/libreoffice-capability-2026-07-19.md](evidence/libreoffice-capability-2026-07-19.md) | Independent local LibreOffice document-rendering capability evidence | Capability evidence only; source-document layout defects remain source defects |
| [validation/validate-foundation.ps1](validation/validate-foundation.ps1) | Deterministic structural, integrity, traceability, link, and whitespace checks | Validation tool; a passing result is necessary but not sufficient for approval |
| [validation/validation-report.md](validation/validation-report.md) | Executed commands, results, limitations, and revision record | Created after review and final revalidation |
| `reviews/` | Independent requirements and SEO evidence review records | Created by reviewer agents; producer and reviewer roles remain separate |

## Route and publication interpretation

- The canonical host proposal is `https://hengshidesign.com`; ownership, DNS, and production activation remain manual gates.
- The route inventory separates planned canonical status, content approval, release activation, indexability policy, and active-sitemap membership. No planned route is serialized as currently active or sitemap-eligible in this Phase 1 snapshot.
- A pattern is not a public URL. Each truthful instantiated route enters an active sitemap only when its content is approved, its exact route belongs to the active immutable release, and it returns a canonical indexable `200` response.
- `/industries` is the only derived route proposal in this slice. Founder acceptance is required before it becomes an approved canonical route.
- Nine exclusion classes keep `/world`, admin, previews/drafts, chat/sessions, internal search, tracking variants, filter/sort variants, staging, and defense behavior distinct. Private content relies on access control; query classes use their explicit status/canonical/link/parameter rules rather than an ambiguous `noindex or canonical` value.

## Evidence boundary

The claims ledger is fail-closed:

- `quarantine`, `hold_until_verified`, `internal_only`, and `reference_only` are never publishable dispositions.
- `eligible_after_phase_1_and_publication_approval` means only that later evidence and approval may make a statement eligible; it is not current publication authority.
- No keyword volume, ranking forecast, market share, customer outcome, expert identity, location, award, certification, client relationship, or legal fact is asserted without evidence.
- The six prototype project seeds remain quarantined and cannot appear as client work.

## Production and review history

- Requirements and conversion artifacts were produced through bounded specialist contracts.
- The market/SEO producer was interrupted after creating and locally validating the complete artifact. The coordinator independently inspected the stable file before accepting it into the review package; interruption is not represented as a completed producer handoff.
- Independent iteration-1 requirements and SEO reviews both returned `REVISE` and are preserved under `reviews/`. Revision 1 addressed all six findings. Independent iteration-2 requirements review closed all four findings and both optional clarifications, while independent iteration-2 SEO review closed both findings against current official Google and OpenAI documentation. Both returned `PASS` with no new actionable HIGH or MEDIUM finding.
- The final validator requires both complete two-iteration review chains and passes 49 checks. This makes the bounded foundation slice ready for founder review only; it does not approve the complete Phase 1 package or authorize implementation, publication, or launch.
- Three requirements-review attempts that never persisted a report are recorded operationally but are not presented as independent evidence. The durable report came from a separate business analyst with no producer write access.
- Findings are resolved within the two-revision maximum for this slice or escalated as an explicit unresolved gate.
- Root coordination owns `PROJECT_STATE.yaml`, `TASKS.md`, decisions, risks, approvals, and advancement to another Phase 1 slice.

## Open founder and external gates

The integrated artifacts retain, rather than silently resolve, the principal gates:

1. legal organization identity, public contact/disclosure facts, naming clearance, canonical-domain ownership, and approved profiles;
2. public positioning language and category descriptor;
3. verified customers, outcomes, cases, demos, experts, authors, owners, images, datasets, awards, certifications, sector expertise, and licenses;
4. acceptance or rejection of the derived `/industries` hub;
5. crawler policy after legal, privacy, and security review;
6. Search Console, Bing Webmaster, IndexNow, DNS, Azure/Microsoft 365, booking mailbox, NVIDIA, and paid-research activation;
7. the full Phase 1 brand, UX/UI references, 3D design, technical compatibility, architecture, API/data, security/privacy, QA/deployment, and cost package.

## Acceptance boundary

This slice is ready for founder review only when:

1. `validation/validate-foundation.ps1` passes;
2. independent requirements and SEO evidence reviews pass, or every unresolved finding is explicitly accepted and recorded;
3. any revisions are revalidated within the two-revision limit;
4. root durable state records the gate accurately.

Even after founder acceptance of this slice, application development remains blocked until the complete Phase 1 package is approved.
