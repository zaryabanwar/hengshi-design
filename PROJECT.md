# Hengshi Design — Project Charter

**Document status:** D-097 incremental v1 delivery; prior accepted baselines retained
**Classification:** Business confidential
**Last reconciled:** 2026-10-25

## Purpose

Hengshi Design is being developed as a premium, platform-oriented innovation
delivery partner for mid-market and enterprise buyers, targeting Europe first
with broader global reach. The public product
combines a complete semantic, search-first website with a visitor-elected immersive World using four peer delivery streams, approved-knowledge AI guidance, human handoff, and discovery booking.

This charter adopts the approved SEO-first, future-ready delivery plan without
re-bootstrapping or replacing the existing repository. Current application code,
documentation, data seeds, and the exterior GLB are protected prototype evidence;
they are not proof of production readiness and do not independently authorize new
product development.

## Authority Bridge

Use the authority order in the current v1 constitution:

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

The founder reaffirmed latest mutually compatible stable technology and v1 naming
on 2026-10-04 (D-069). This is the first development toward the first production
release; actual dependency/schema versions and historical evidence identifiers
remain accurate. D-068 supersedes the earlier exclusive Azure target: deployment,
provider, region and cost planning are deferred, with Azure and AWS candidates and
the lowest feasible operating cost/free services preferred when planning resumes.
Existing technical references, backlog, diagrams and draft feature specs remain
prototype or historical evidence until reconciled. Neither historical cloud plan
selects a provider or authorizes application, database or cloud implementation.

## Product Direction

- **Primary outcome:** win qualified discovery bookings.
- **Audience:** English-speaking mid-market and enterprise decision-makers in
  Europe first, retaining global ambition. This establishes no European office.
- **Sector order:** agriculture, mining, then separately gated defense content.
- **Positioning:** innovation delivery partner providing strategy-to-delivery
  programs through custom discovery and proposals.
- **Brand:** Hengshi Design; D-035 accepts the exact frozen Signal Ledger system +
  Framework Relay logo hybrid for Phase 1 definition. The marks remain
  unregistered and trademark-not-cleared, and production UI remains unauthorized.
- **Experience:** complete semantic Quick Access and three WebGL delivery streams,
  with explicit World entry, automatic capability selection and accepted override
  rules. All public representations share one immutable approved release.
- **Movement:** D-064 adds mouse/touch free steering and walking, nearby spatial
  streaming and retained destinations; WASD is not selected.
- **Virtual headquarters:** D-066 selects an original modular building; D-067
  selects nature-integrated organic architecture. Appearance and production
  asset acceptance remain distinct from this direction. Preserve the Atlanta GLB.
- **Search:** every indexable route must return complete semantic HTML without
  requiring JavaScript or canvas interaction.
- **Conversion:** a globally available 30-minute discovery booking; visitors may
  book directly without first using AI.
- **Evidence:** only verified client work or clearly labeled Hengshi-owned
  capability demonstrations may be published.
- **Company facts:** D-070 records founder-supplied Pakistan company details as
  admin-editable, reviewed content. Dedicated privacy/security aliases are
  accepted and will be created by the founder; delivery and ownership remain
  unverified. See [entity and contact definitions](docs/software-definition/06-entity-and-public-contact.md).
- **Outlook/Teams:** retain the integration intent without making Microsoft 365
  setup a prerequisite. Required account/API capabilities need separate proof;
  provider deferral does not replace approved staff identity or AI privacy routes.

Accepted product/design baselines and their amendments are recorded in DECISIONS.md.
D-025 accepts foundation, D-035 identity, D-036 UX, D-037 reference-design coverage,
D-061/D-063 the reviewed definition/authority refinements, and D-065 architecture
boundaries. The full Phase 1 package is not yet accepted. Specific older counts,
freeze hashes and tool-exposure snapshots belong in their evidence records, not
this timeless charter.

The [reconciliation map](docs/software-definition/04-reconciliation-map.md) names
canonical subjects and remaining deliverables. The [World definition](docs/phase-1-3d/WORLD_EXPERIENCE.md)
and [architecture addendum](docs/phase-1-architecture/MOVEMENT_STREAMING_ADDENDUM.md)
carry the current movement/spatial proposal. Independent review is required; no
proposal self-approves. Generated concepts and browser blockouts are reviewable
studies, not accepted production screens or proof of implemented journeys.

D-097 replaces B01-as-universal-prerequisite sequencing with scoped increment
assignments. Existing Figma references and their evidence remain protected.
D-095 governs MCP-first routing within included availability, then computer use
with available included Design agent/Make features; repeated per-call/method
prompts within approved scope are superseded. Extra allowance, paid activation,
new scope, destructive cleanup and account/sharing/publication changes retain
separate approval. The tooling inventory and B01 brief own dated capability and
interruption evidence. Compatibility acceptance and exact locks remain separate
at MA-013. Legal/content/staff/provider facts must remain verified or held.

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
  supported in the eventual approved provider/region; otherwise use the newest supported GA
  major and retain a dated exception.

## Delivery Workflow

Every material phase follows:

```text
create -> validate -> inspect -> independent review -> revise -> validate again -> founder approval
```

- The Hengshi project manager coordinates phase work through bounded specialist
  contracts.
- Producers and reviewers remain independent.
- No hard revision cap. Continue safe in-scope corrections; diagnose repeated
  failures and escalate material decisions rather than iteration counters.
- Durable project records, not chat history, carry state between phases.
- External writes, destructive actions, paid activation, credential changes,
  migrations, commits, pushes, and production deployment require their explicit
  approval gate.
- Each assigned increment needs its relevant definition, approved visual design,
  contracts and coupled compatibility before implementation. Unfinished future
  3D or deferred hosting work does not block unrelated 2D delivery under D-097.

## Current Readiness

| Level | Status | Evidence-based statement |
|---|---|---|
| Local | In progress | A prototype repository and test/build scaffolding exist, but deterministic frontend, authorization, database, dependency, and documentation conflicts remain. |
| UAT | Not started | There is no approved UAT definition, persistent UAT environment, complete test evidence, or accepted release candidate. |
| Launch | Blocked | Production definitions, verified content and legal evidence, identity/design approval, infrastructure, CI/CD, observability, security review, accessibility evidence, DNS, and provider entitlements are incomplete. |

Historical percentage scorecards in the February 2026 consolidation are snapshots,
not current acceptance evidence.

## Current Phase and Next Action

Phase 0 and the accepted definition baselines remain accepted. D-097 (2026-10-25)
changes delivery to brand/shared foundations, complete 2D content and service
platform, then the full 3D World and integrated launch qualification. The complete
agreed scope remains in [the consolidated scope](docs/software-definition/05-consolidated-goal.md).
TASKS.md names the next bounded assignment; PROJECT_STATE.yaml preserves prior
evidence separately from current work. The founder starts each work chat with a
prompt from the discussion chat, returns the result and selects the next task.
Finish one outcome and stop; do not edit active app goals or start adjacent work.
Commits and pushes remain deferred. Visual, legal and external-action gates apply
to the affected increment, not as a universal hold on unrelated development.
