# Hengshi Design — Project Charter

**Document status:** Phase 0 accepted; Phase 1 definition in progress
**Classification:** Business confidential
**Last reconciled:** 2026-09-03

## Purpose

Hengshi Design is being developed as a premium, platform-oriented innovation
delivery partner for global mid-market and enterprise buyers. The public product
combines a complete semantic, search-first website with an optional immersive 3D
campus, approved-knowledge AI guidance, human handoff, and discovery booking.

This charter adopts the approved SEO-first, future-ready delivery plan without
re-bootstrapping or replacing the existing repository. Current application code,
documentation, data seeds, and the exterior GLB are protected prototype evidence;
they are not proof of production readiness and do not independently authorize new
product development.

## Authority Bridge

Use the authority order ratified in Constitution 2.0.0:

1. Current explicit founder approval, recorded in the operational index
   `DECISIONS.md` and detailed `docs/decisions-log.md`.
2. `.specify/memory/constitution.md`, `AGENTS.md`, and project safety/governance
   rules.
3. Approved decisions and compatibility-exception ADRs.
4. Approved product requirements and feature specifications.
5. Approved software-definition and design artifacts.
6. Source code, tests, generated artifacts, and live observations as current
   implementation evidence.
7. Active-but-unreconciled documents, consolidation files, research, drafts, and
   chat history as supporting evidence only.

Approved decisions outrank approved requirements; approved requirements outrank
research and drafts. A conflict stops implementation and is recorded before work
resumes.

The founder approved the latest-compatible-stable technology policy and Azure
target on 2026-07-18. Phase 0 implemented that policy in Constitution 2.0.0,
`AGENTS.md`, project rules, software-definition workflow documents, Copilot
instructions, and Spec Kit templates. This resolves the fixed-version/AWS
governance conflict. Existing v3 product documents, active technical references,
backlog, diagrams, and draft feature specs remain unreconciled prototype or
historical evidence; Phase 1 must supersede or reconcile them before application,
database, or cloud implementation.

## Product Direction

- **Primary outcome:** win qualified discovery bookings.
- **Audience:** global English-speaking mid-market and enterprise decision-makers
  in technology, data, product, transformation, and innovation.
- **Sector order:** agriculture, mining, then separately gated defense content.
- **Positioning:** innovation delivery partner providing strategy-to-delivery
  programs through custom discovery and proposals.
- **Brand:** Hengshi Design; D-035 accepts the exact frozen Signal Ledger system +
  Framework Relay logo hybrid for Phase 1 definition. The marks remain
  unregistered and trademark-not-cleared, and production UI remains unauthorized.
- **Experience:** a semantic, responsive Quick Access website and an optional 3D
  campus powered by one approved publication manifest.
- **Search:** every indexable route must return complete semantic HTML without
  requiring JavaScript or canvas interaction.
- **Conversion:** a globally available 30-minute discovery booking; visitors may
  book directly without first using AI.
- **Evidence:** only verified client work or clearly labeled Hengshi-owned
  capability demonstrations may be published.

The founder accepted the bounded Phase 1 UX architecture through D-036 after final
deterministic validation and independent design/accessibility review. Semantic
Quick Access and optional 3D journeys now have an accepted definition-level model
for equivalent content, actions, recovery, and accessibility. A reviewed,
documentation-only UI reference-design contract now covers all 33 routes, nine
exclusions, 15 wayfinding records, 53 actions, and 45 UX tests through 40 reusable
templates and 32 responsive/state/accessibility profiles. Its final producer
freeze passes 183/183 checks and both independent reviews, and awaits founder
decision at MA-024. No visual reference screen exists yet. UI production,
application implementation, public copy, publication, and external Figma/Stitch
writes remain unauthorized. Compatibility inventory acceptance remains separately
pending at MA-013, and the complete Phase 1 package is not accepted.

## Service Architecture

The product retains ten service categories grouped into five campus wings:

1. **Strategy & Transformation** — Strategy & Architecture.
2. **Digital Products & Growth** — Platform & Product Engineering; Product
   Design & Experience Engineering; Commerce, Content & Growth Platforms.
3. **AI, Data & Automation** — AI Systems & Agentic Automation; Data Platforms &
   Analytics.
4. **Immersive & Creative** — Spatial Computing & Immersive Platforms; Creative &
   Visual Design Services.
5. **Cloud, Reliability & Trust** — Cloud, DevOps & Platform Reliability;
   Security, Privacy & Trust Engineering.

Shared spaces are a verified Work Gallery, Industry Hub, Trust Center, Insights
Library, and private Meeting Suite. Their public release is gated by approved
content, proof, named ownership, and the relevant security/privacy controls.

## Technology Policy

- Preserve the technology families: React, TypeScript, Vite, TailwindCSS, React
  Three Fiber/Three.js, FastAPI, SQLAlchemy, Alembic, PostgreSQL, JWT, and bcrypt.
- Select the newest mutually compatible stable versions at the time of each
  approved upgrade wave. Preview, beta, release-candidate, nightly, or
  experimental packages may not become production requirements.
- Treat compatibility as a graph across runtimes, frameworks, peers, browsers,
  cloud services, build tools, and deployment targets.
- Use Context7 and official primary documentation for every version-sensitive
  decision. If Context7 is configured but not exposed by the active host, use the
  documented safe direct MCP fallback. Record the Context7 library ID/query date,
  official source, compatibility result, breaking changes, and rollback evidence.
- If the newest stable major is blocked, use the newest proven-compatible stable
  release, record the blocker in an ADR, and recheck quarterly.
- Lock all production dependencies and artifacts reproducibly. Production images
  and GitHub Actions must use immutable references, not `latest` tags.
- Keep WebGL as the production renderer. WebGPU remains an isolated experiment
  until official support and full parity are stable.
- PostgreSQL 18 is the intended target only if it is generally available and
  supported in the approved Azure region; otherwise use the newest supported GA
  major and retain a dated exception.

## Delivery Workflow

Every material phase follows:

```text
create -> validate -> inspect -> independent review -> revise -> validate again -> founder approval
```

- The Hengshi project manager coordinates phase work through bounded specialist
  contracts.
- Producers and reviewers remain independent.
- Default maximum revision iterations are two; brand, UI, motion, and 3D allow
  three.
- Durable project records, not chat history, carry state between phases.
- External writes, destructive actions, paid activation, credential changes,
  migrations, commits, pushes, and production deployment require their explicit
  approval gate.
- No application development is authorized until Phase 1's complete definition,
  SEO, design, architecture, security, test, deployment, and compatibility package
  is independently reviewed and founder-approved.

## Current Readiness

| Level | Status | Evidence-based statement |
|---|---|---|
| Local | In progress | A prototype repository and test/build scaffolding exist, but deterministic frontend, authorization, database, dependency, and documentation conflicts remain. |
| UAT | Not started | There is no approved UAT definition, persistent UAT environment, complete test evidence, or accepted release candidate. |
| Launch | Blocked | Production definitions, verified content and legal evidence, identity/design approval, infrastructure, CI/CD, observability, security review, accessibility evidence, DNS, and provider entitlements are incomplete. |

Historical percentage scorecards in the February 2026 consolidation are snapshots,
not current acceptance evidence.

## Current Phase and Next Action

The founder explicitly accepted Phase 0 on 2026-07-19 after independent review
iteration 2 passed with no remaining actionable finding. Phase 1 is now in progress
under the precise definition-only contract recorded in `TASKS.md` and
`PROJECT_STATE.yaml`. Application implementation remains blocked until the complete
Phase 1 package is independently reviewed and explicitly accepted by the founder.

The founder accepted the bounded requirements, claims, SEO, routes, and conversion
foundation through D-025 and retained `/industries`. D-026 approves the
independently reviewed **Evidence in Motion** brand strategy, opening brand-identity
definition. The compatibility inventory passed independent review iteration 2 and
awaits the separate MA-013 founder gate; its exact production locks remain
deliberately unselected. D-035 accepts the frozen brand identity. D-036 accepts the
final UX architecture after 113/113 plus independent design and accessibility PASS.
D-037 accepts the frozen UI reference-design contract and foundation-surface
coverage package. The exact next action is founder review at MA-025 of a bounded
external Figma/Stitch production contract. UI production, external design writes,
and application implementation remain unauthorized until their applicable gates.
