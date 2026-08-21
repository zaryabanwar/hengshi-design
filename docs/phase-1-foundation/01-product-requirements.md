# Hengshi Design — Phase 1 Product and Business Requirements

**Document status:** Draft for independent review and founder acceptance  
**Approval status:** Phase 1 is in progress; this document is not yet an approved requirements baseline  
**Classification:** Business confidential  
**Effective date:** 2026-07-19  
**Owner:** Product requirements function; named individual assignment is pending  
**Revision limit:** Two producer revisions under the active Phase 1 contract

## 1. Purpose and authority

This document defines the product and business requirements foundation for the
SEO-first, future-ready Hengshi Design platform. It continues the existing
repository non-destructively and translates approved decisions D-001 through
D-024 into atomic, testable requirements for downstream SEO, brand, UX, 3D,
architecture, security, data, QA, and deployment work.

It does not authorize application implementation. Phase 2 remains blocked until
the complete Phase 1 package is independently reviewed and explicitly accepted by
the founder.

Authority is applied in this order:

1. Approved decisions in `DECISIONS.md` and `docs/decisions-log.md`.
2. `.specify/memory/constitution.md`, `AGENTS.md`, and project safety rules.
3. Approved software boundaries and the active Phase 1 contract.
4. Current code, tests, diagrams, and API documents as implementation evidence.
5. The February 2026 SRS, SAD, mapping, style guide, backlog, and draft specs as
   historical or prototype evidence only.

### 1.1 Source key

| Key | Source and use |
|---|---|
| `D-###` | Approved founder decision in the operational index and detailed decision log; binding. |
| `CON` | Constitution 2.0.0; binding governance and product constraints. |
| `PROJECT` | Current charter and Phase 1 scope. |
| `STATE` / `TASKS` | Current workflow state and bounded Phase 1 contract. |
| `SB-01` | Approved software-definition system boundaries. |
| `R-###` / `MA-###` | Active risk or manual human/external gate. |
| `MP` | Approved SEO-first master plan as durably adopted by D-001 through D-023; details not repeated in the decision log remain proposed specification until Phase 1 acceptance. |
| `LEG-*` | Legacy/prototype evidence only; never sufficient by itself to approve a target requirement. |

### 1.2 Status and priority key

- **Approved constraint**: directly required by an approved decision or binding
  governance. This describes approved intent, not implementation completion.
- **Proposed specification**: a testable Phase 1 decomposition awaiting acceptance
  with the complete package.
- **Pending founder**: a material value or policy choice that cannot be inferred.
- **P0**: blocks the relevant launch or implementation gate.
- **P1**: required for an approved later-phase capability or operational gate.
- **P2**: required after launch as part of the approved lifecycle cadence.

## 2. Input inventory and evidence limitations

| Input | State | Consequence |
|---|---|---|
| Approved lead intake | No approved lead-intake artifact was found in the repository. | Approved decisions and the charter supply the current business scope; a future intake may enrich but cannot silently change it. |
| Interview notes | No approved interview-note artifact was found. | No buyer quotations, pain-point rankings, budget bands, or persona-specific claims are asserted here. |
| Target users | Defined in D-005, D-016, D-018, and `PROJECT.md`. | Sufficient for the definition baseline; named personas and research evidence remain a later research input. |
| Constraints | Defined in the constitution, project charter, risks, manual actions, and Phase 1 contract. | Safety, publication, privacy, technology, external-action, and phase gates are binding. |
| Approved product direction | D-001 through D-024. | All decisions are covered explicitly in section 14. |
| Existing implementation | SRS/SAD/API/current-state diagrams and repository observations. | Useful for migration and regression planning; it does not prove readiness or authorize legacy targets. |

The absence of intake and interview artifacts does not block this bounded draft
because the founder has already approved the audience, sectors, service taxonomy,
conversion outcome, product boundaries, and delivery sequence. It does prevent
inventing detailed buyer motivations, proof, legal facts, or budget/timeline
commitments.

## 3. Product scope and required outcomes

The product is one evidence-led Hengshi Design presence with two equivalent public
journeys: a complete responsive semantic website and an optional progressive 3D
campus. Both derive from the same approved publication release and lead visitors
to verified service evidence, approved AI or human guidance, and a qualified
30-minute discovery booking.

Required outcomes are:

1. Qualified organic discovery and bookings from global English-speaking
   mid-market and enterprise buyers.
2. Truthful presentation of ten services, starting with agriculture and then
   mining, without fictional proof or unsupported superiority claims.
3. Equivalent accessible discovery and conversion without WebGL or JavaScript.
4. Governed publication, AI, human handoff, booking, retention, deletion, and
   staff authorization.
5. A reproducible, supportable, observable Azure-targeted platform on the newest
   mutually compatible stable technology set approved at each upgrade wave.

## 4. Users and actors

| Actor | Definition | Primary need | Evidence boundary |
|---|---|---|---|
| Buyer visitor | A global English-speaking mid-market or enterprise leader in technology, data, product, transformation, or innovation. | Understand relevant capability and reach a qualified discovery booking quickly. | No individual persona detail is claimed without research. |
| Agriculture buyer | The first sector audience. | See credible service-to-agriculture relevance and verified proof. | No fabricated sector outcome or client claim. |
| Mining buyer | The second sector audience. | See credible service-to-mining relevance and verified proof. | No fabricated sector outcome or client claim. |
| Defense visitor | A separately gated future audience. | Reach approved public information or a secure human route. | No defense content, dataset, demo, or AI route before founder, legal, and security approval. |
| Anonymous visitor | A visitor without an account. | Browse, use initial text chat, request help, or book directly. | No launch account or upload. |
| Content author | Staff member allowed to draft approved content types. | Create content without being able to self-publish. | Entra-mapped author role. |
| Specialist reviewer | Qualified evidence/SEO/domain reviewer. | Verify claims, sources, and usefulness before founder approval. | Cannot be the sole author and final approver of the same release. |
| Founder approver | Final publication and phase authority. | Accept or reject material scope, claims, releases, and risks. | Approval must be recorded durably. |
| Administrator | Least-privilege platform operator. | Manage authorized configuration and recovery operations. | Server-side authorization; frontend guards are not security controls. |
| Live staff / room owner | Explicitly available Hengshi specialist with an approved backup. | Receive handoffs, respond in the Hengshi console, and accept qualified bookings. | Identity, assignment, and availability must be verified. |
| External reviewer | Independent legal, security, accessibility, design, SEO, QA, or deployment reviewer. | Provide evidence-based gate findings. | Cannot approve their own production output. |

## 5. Business requirements

| ID | Requirement | Priority | Owner | Source | Status | Acceptance criteria |
|---|---|---:|---|---|---|---|
| BR-001 | The primary measurable product conversion shall be a qualified 30-minute discovery booking. | P0 | Product | D-005 | Approved constraint | Every primary journey exposes the booking action; conversion reporting distinguishes qualified completed bookings from clicks or raw traffic. |
| BR-002 | The primary audience shall be global English-speaking mid-market and enterprise technology, data, product, transformation, and innovation decision-makers. | P0 | Product | D-005; PROJECT | Approved constraint | Audience definitions and launch content name only these approved buyer groups unless a later decision expands scope. |
| BR-003 | Sector delivery shall prioritize agriculture first and mining second. | P0 | Product and Content | D-005 | Approved constraint | Agriculture and mining receive separate approved hubs; no lower-priority sector displaces agriculture at launch without a recorded decision. |
| BR-004 | Hengshi Design shall sell strategy-to-delivery programs through custom discovery and proposal rather than fixed public pricing. | P0 | Product and Sales | D-005 | Approved constraint | Public pages contain no fixed package price or binding quote; pricing requests route to discovery, and AI/human previews do not invent terms. |
| BR-005 | The public service architecture shall contain exactly the approved ten formal services grouped into five approved wings. | P0 | Product | D-010; PROJECT | Approved constraint | The source taxonomy contains: Strategy & Architecture; Platform & Product Engineering; Product Design & Experience Engineering; Commerce, Content & Growth Platforms; AI Systems & Agentic Automation; Data Platforms & Analytics; Spatial Computing & Immersive Platforms; Creative & Visual Design Services; Cloud, DevOps & Platform Reliability; Security, Privacy & Trust Engineering. No legacy category silently replaces one. |
| BR-006 | The public name shall remain “Hengshi Design,” supported by a complete premium identity and an evidence-led expert voice. | P0 | Brand and Product | D-006 | Approved constraint | Approved brand artifacts consistently use “Hengshi Design”; public copy contains no unapproved alternate entity name. |
| BR-007 | Public novelty, superiority, performance, customer, award, rating, and outcome claims shall require independent substantiation and applicable legal approval. | P0 | Evidence and Legal | D-006; D-007 | Approved constraint | Unsupported claims remain absent or held; “world-first” never appears publicly without a linked substantiation and legal approval record. |
| BR-008 | Verified client work and Hengshi-owned capability demonstrations shall be separate public collections. | P0 | Evidence and Content | D-007 | Approved constraint | Each published item has an approved `verified_case` or `hengshi_demo` classification; fictional seeds and ambiguous portfolio items remain unavailable publicly. |
| BR-009 | Defense-facing content, demos, datasets, campaigns, and AI routes shall remain unpublished and unindexed until all required founder, independent legal, and security gates pass. | P0 | Founder, Legal, Security | D-005; D-017; MA-011 | Approved constraint | A negative test confirms no defense route, sitemap entry, retrieval document, AI answer source, or campaign is public before all three approvals are recorded. |
| BR-010 | Launch shall be English-only while content and route structures remain localization-ready. | P1 | Product and Content | D-009 | Approved constraint | Launch exposes one English canonical per item; no translation selector or `hreflang` is emitted for a language without a real approved translated URL. |
| BR-011 | The responsive foundation, reception/atrium experience, Reception AI Concierge, handoff, and booking shall launch before specialist wings. | P0 | Product | D-011 | Approved constraint | Release sequencing evidence shows the complete foundation accepted before any wing is marked open. |
| BR-012 | Specialist wings shall open in the approved order: AI/Data, Strategy, Immersive/Creative, Digital Products/Growth, then Cloud/Reliability/Trust. | P1 | Product | D-011; D-023 | Approved constraint | Release records prevent a later wing from opening before earlier sequence gates unless a new founder decision changes the order. |

## 6. Functional requirements

| ID | Requirement | Priority | Owner | Source | Status | Acceptance criteria |
|---|---|---:|---|---|---|---|
| FR-001 | Quick Access shall make all ten services immediately discoverable on responsive devices without requiring the 3D experience. | P0 | Product and UX | D-008; D-010 | Approved constraint | From any public entry route, a visitor can reach each formal service page by semantic links with WebGL disabled. |
| FR-002 | The responsive and 3D experiences shall render the same approved publication release. | P0 | Publication and Product | D-008; D-019 | Approved constraint | A release checksum comparison shows matching titles, summaries, service mappings, proof status, and canonical destinations; mismatch blocks activation. |
| FR-003 | The immersive foundation shall include a lightweight loader, skippable arrival, entrance, reception, central atrium, and visibly closed future wings. | P1 | 3D and UX | D-011; MP | Proposed specification | Each state is represented in the approved storyboard and acceptance flow; asset failure or intro skip still reaches reception/Quick Access without lost content. |
| FR-004 | The booking journey shall collect a syntactically valid email address, organization, role, desired outcome, matched wing, timing, and consent, with budget optional, before issuing an email-ownership challenge. | P0 | Product and Booking | D-005 | Approved constraint | Missing required fields or an invalid email shape prevents challenge issuance; a syntactically valid address may enter `EMAIL_PENDING`, but it is not treated as verified, slot-eligible, submitted to the calendar provider, or confirmed. Omission of budget alone does not block challenge issuance. |
| FR-005 | Visitors shall be able to book without first using AI or live chat. | P0 | Product and Booking | D-016 | Approved constraint | A clean session can reach and complete the booking flow from semantic navigation with chat disabled or unavailable. |
| FR-006 | Booking availability shall be presented in the visitor’s local time and route to an approved owner or backup. | P0 | Booking Operations | D-016 | Approved constraint | Time-zone conversion tests cover daylight-saving boundaries; no slot is offered when neither approved owner nor backup is eligible. |
| FR-007 | After email ownership is verified, booking creation shall be idempotent and reconciled with the approved Outlook/Teams record. | P0 | Booking Operations | D-016; SB-01 | Approved constraint | No slot booking or external calendar write is accepted before verification; repeated verified requests with the same idempotency key create at most one booking; failures do not display confirmation; reconciliation identifies and repairs or escalates mismatches. |
| FR-008 | A visitor shall be able to begin anonymous text chat without an account. | P1 | AI and Product | D-016; D-017 | Approved constraint | A new visitor can create one bounded initial session without registration; upload and account controls remain unavailable. |
| FR-009 | Live-human availability shall require explicit staff availability, while Teams presence may only suppress a false available state. | P1 | Handoff Operations | D-016 | Approved constraint | Presence alone never marks a person available; stale or unavailable staff yields a clear offline/booking route rather than a false promise. |
| FR-010 | Staff shall handle governed visitor conversations in the Hengshi console, with Teams used for approved alerts rather than as the public system of record. | P1 | Handoff Operations | D-016 | Approved constraint | A handoff is auditable in the Hengshi system; a missing or failed Teams alert does not lose the durable handoff and is surfaced for retry. |
| FR-011 | Human voice or video interaction shall require explicit visitor opt-in. | P1 | Handoff Operations | D-016 | Approved constraint | Text handoff never activates microphone/camera; declined or unsupported media leaves text and booking paths usable. |
| FR-012 | First-visit onboarding shall explain audio, quality, navigation, AI, human help, Skip Intro, and Skip Guide controls. | P1 | UX | D-012; MP | Proposed specification | Each control is reachable by keyboard and assistive technology before commitment; skipping onboarding preserves all core navigation and conversion actions. |
| FR-013 | Returning visitors shall be offered Resume, Reception, Replay, and Quick Access choices using non-sensitive local preferences. | P1 | UX and Privacy | D-012; MP | Proposed specification | No account is required; clearing storage resets choices safely; an invalid saved location falls back to Reception or Quick Access. |
| FR-014 | The public experience shall provide a persistent searchable directory with location, room links, booking, accessibility, quality, audio, and exit controls. | P1 | UX | D-012; MP | Proposed specification | The directory remains operable in keyboard, reduced-motion, mobile, and non-WebGL modes; unavailable rooms are labeled closed and do not dead-end. |
| FR-015 | Migration shall preserve existing public APIs until approved replacement contracts and deprecation behavior are available. | P0 | Architecture and API | MP; SB-01 | Proposed specification | Existing documented endpoints retain contract tests during migration; any incompatible removal requires an approved versioned contract, consumer evidence, and rollback. |
| FR-016 | The target interface set shall support publication retrieval, chat-session creation, room presence, booking availability, idempotent booking creation, resumable chat WebSockets, and governed admin release/SEO/knowledge/chat/assignment/audit operations. | P0 | Architecture and API | MP; D-014 through D-019 | Proposed specification | The Phase 1 API contract assigns a versioned interface and failure behavior to every named capability; no implementation starts while a required contract is absent. |
| FR-017 | Launch content shall include five wing hubs, ten complete service pages, agriculture and mining hubs, verified Work and separate Demos collections, About, verified experts, Trust Center, contact, booking, and six expert-reviewed cornerstone insights. | P0 | Content and Product | D-009; D-010 | Approved constraint | The prelaunch inventory contains every required item with owner, evidence state, review state, canonical route, and publication status; a missing required launch item blocks launch, while an unsupported candidate remains held rather than being used to fill the gap. |
| FR-018 | After the editorial workflow stabilizes, Hengshi Design shall publish two expert-reviewed original insights monthly and one substantial research asset, useful tool, benchmark, or visual explainer quarterly. | P2 | Content Operations | D-009 | Approved constraint | The editorial calendar records named ownership, expert review, original contribution, publication result, and missed-cadence reason without substituting mass-generated pages. |
| FR-019 | Email ownership verification shall preserve one booking lineage across pending, expired, undeliverable, corrected-address, resend, and verified outcomes. | P0 | Product and Booking | D-005; D-016 | Proposed specification | Pending, expired, and undeliverable outcomes remain unverified and cannot expose slot booking or final confirmation; a safe resend or corrected address reuses the lineage, rate-limit and expiry policy, and audit context without creating a second booking; only a successful current challenge moves the lineage to `VERIFIED`. |

## 7. SEO and entity requirements

These are binding product requirements. Detailed keyword selection, route
inventory, editorial briefs, and measurement design belong to the separate SEO
strategy artifact.

| ID | Requirement | Priority | Owner | Source | Status | Acceptance criteria |
|---|---|---:|---|---|---|---|
| SEO-001 | Every indexable route shall return complete, meaningful semantic HTML before client JavaScript runs. | P0 | SEO and Frontend Architecture | D-008 | Approved constraint | With JavaScript and canvas disabled, the response contains a unique title, H1, core body content, navigation, relevant links, and conversion path. |
| SEO-002 | The canonical public host shall be `https://hengshidesign.com`, with lowercase, hyphenated, stable URLs and no trailing slash except root. | P0 | SEO and Platform | D-008 | Approved constraint | Host/path variants resolve by one-hop permanent redirect to one canonical; no duplicate canonical returns 200. |
| SEO-003 | `/world`, admin, preview, session/chat, staging, filter, internal-search, draft, rejected, and unpublished-release surfaces shall be excluded from indexes and sitemaps. | P0 | SEO and Publication | D-008 | Approved constraint | Robots/canonical/header/sitemap tests confirm exclusion; protected or unpublished content never appears in generated public artifacts. |
| SEO-004 | Canonical route families shall cover home, service wing, service room, agriculture, mining, verified work, labeled demos, insights, experts, trust, about, contact, and booking. | P0 | SEO and Product | D-009 | Approved constraint | The route inventory assigns one unique canonical and content owner to each approved public entity; collisions or orphan routes fail validation. |
| SEO-005 | Every public document shall have unique metadata, one canonical, one visible H1, a robots directive, social metadata, breadcrumbs, and crawlable internal links. | P0 | SEO and Publication | D-019; MP | Proposed specification | Automated validation rejects missing, duplicate, contradictory, or content-mismatched fields before release activation. |
| SEO-006 | Structured data shall describe only visible, verified content using the approved Organization, WebSite, BreadcrumbList, Service, Article, Person, ImageObject, and VideoObject types. | P0 | SEO and Evidence | MP; D-007; D-019 | Proposed specification | JSON-LD fields match visible facts; fabricated reviews, prices, customers, awards, people, or locations fail evidence review. |
| SEO-007 | Every 3D room and content panel shall link to its canonical semantic page. | P0 | SEO and 3D | D-008 | Approved constraint | Each room-to-service mapping resolves to a crawlable canonical URL; a missing or closed room still exposes the semantic page through Quick Access when approved public content exists. |
| SEO-008 | Publication shall generate sitemap, redirect, retired-URL, robots, and correct 404/410 outputs from the approved release. | P0 | SEO and Publication | D-019; MP | Proposed specification | Unknown URLs return 404; intentionally retired content returns 410 or an approved relevant redirect; no redirect loop, soft 404, or stale sitemap entry passes release validation. |
| SEO-009 | Entity presentation shall consistently use “Hengshi Design,” verified organization facts, approved experts, policies, contact details, and only approved `sameAs` profiles. | P0 | SEO and Evidence | D-006; D-009; R-010 | Approved constraint | Every entity fact has a source/owner; unrelated “Hengshi” organizations and unverified profiles are absent. |
| SEO-010 | `hreflang` shall be emitted only for real approved translated URLs. | P1 | SEO | D-009 | Approved constraint | English-only launch emits no fabricated alternate-language URL; later alternates are reciprocal and canonical-consistent. |
| SEO-011 | AI-assisted content shall receive named expert verification, original human value, evidence review, and founder publication approval. | P0 | Content and Evidence | D-007; D-019 | Approved constraint | Content without named review, source evidence, original contribution, and founder approval cannot enter public HTML or retrieval. |
| SEO-012 | Organic authority work shall prohibit paid links, fabricated reviews, link networks, bulk-directory schemes, deceptive geographic pages, and mass-generated search pages. | P0 | SEO and Legal | D-007; D-009; MP | Approved constraint | Outreach/content audit finds no prohibited tactic; any geographic page requires a real approved business basis and unique useful content. |
| SEO-013 | The crawler registry shall separately classify automatic search/answer crawlers, training crawlers, user-triggered fetchers, mixed-purpose tokens, and unknown automation before assigning provider-specific policy. | P1 | SEO, Legal, and AI Governance | MP | Proposed specification | Each entry records request identity or token, documented purpose, whether `robots.txt` applies, whether uses are technically separable, official source/date, proposed default, owner, and founder/legal/privacy/security gate. `ChatGPT-User` is not governed as `OAI-SearchBot`; a mixed-purpose token such as `Google-Extended` is not represented as separable when the provider does not expose separate controls. Exact production directives remain unapproved and are reviewed at least quarterly. |

## 8. Publication and evidence requirements

| ID | Requirement | Priority | Owner | Source | Status | Acceptance criteria |
|---|---|---:|---|---|---|---|
| PUB-001 | One approved immutable publication manifest and checksum shall drive HTML, metadata, schema, sitemaps, redirects, AI knowledge, and 3D panels. | P0 | Publication Architecture | D-019; CON | Approved constraint | Release verification proves all public representations reference one checksum; a mismatch prevents activation. |
| PUB-002 | Publication lifecycle shall be Draft → specialist evidence/SEO review → founder approval → render/index → public. | P0 | Publication Operations | D-019 | Approved constraint | State-transition tests reject skipped, reversed, or unauthorized transitions. |
| PUB-003 | An author shall not approve their own material output. | P0 | Publication Operations | D-019; CON | Approved constraint | Negative authorization tests show the author cannot perform specialist or founder approval on the same release where separation is required. |
| PUB-004 | Draft, rejected, and superseded-unapproved content shall not enter public HTML, sitemaps, search notifications, retrieval indexes, AI context, or 3D panels. | P0 | Publication and AI Governance | D-019 | Approved constraint | Cross-surface isolation tests seed a draft/rejected marker and prove it is absent from every public/AI artifact. |
| PUB-005 | A failed render, index, or activation operation shall leave the previous approved release active. | P0 | Publication Operations | D-019 | Approved constraint | Failure-injection evidence shows no partial release, mixed checksum, public outage, or draft exposure and demonstrates safe retry/rollback. |
| PUB-006 | Every publishable case, demo, expert, claim, image, and video shall have an owner, provenance, rights status, evidence status, and approval status. | P0 | Evidence Operations | D-007; MA-003 | Approved constraint | Missing ownership, rights, evidence, or approval produces a held state and prevents public rendering. |
| PUB-007 | Public content shall distinguish verified facts from Hengshi-owned capability demonstrations. | P0 | Evidence and Content | D-007 | Approved constraint | Labels and structured data never imply an unverified demo is client work or a measured customer outcome. |

## 9. Experience, accessibility, and 3D requirements

| ID | Requirement | Priority | Owner | Source | Status | Acceptance criteria |
|---|---|---:|---|---|---|---|
| UX-001 | All launch journeys shall meet WCAG 2.2 AA. | P0 | Accessibility and UX | D-012; CON | Approved constraint | Independent accessibility review and automated/manual evidence cover semantics, focus, input, contrast, errors, status messages, zoom, and reflow with no unresolved launch-blocking finding. |
| UX-002 | Quick Access shall provide content, navigation, AI or human help, and booking equivalent to the 3D route. | P0 | UX and Product | D-008; D-012 | Approved constraint | A parity matrix maps every core 3D task to a non-WebGL task; no exclusive content or conversion exists only in canvas. |
| UX-003 | Core journeys shall be operable by keyboard and screen reader. | P0 | Accessibility and UX | D-012 | Approved constraint | A visitor can discover services, open/close navigation, use help, submit errors, and book without pointer input; focus order and announcements remain meaningful. |
| UX-004 | Reduced-motion users shall receive an equivalent authored journey with intro and guide skips. | P0 | Accessibility and Motion | D-012 | Approved constraint | `prefers-reduced-motion` suppresses nonessential camera/ambient movement without removing content, state feedback, help, or booking. |
| UX-005 | Low-power, non-WebGL, 3D-asset-failure, network-failure, and unsupported-browser states shall recover to semantic Quick Access. | P0 | UX and Reliability | D-012; R-011 | Approved constraint | Failure-mode tests reach a labeled recovery action and retain location/context where safe; no blank canvas or unrecoverable loop is accepted. |
| UX-006 | Immersive navigation shall use directed point-and-click transitions with optional free-look. | P1 | 3D and UX | D-012 | Approved constraint | Approved flows require no WASD, collision walking, gamification, or easter eggs; free-look can be disabled without blocking navigation. |
| UX-007 | Audio shall be off until a visitor makes an informed interaction choice, and captions/transcripts shall accompany meaningful media. | P0 | Accessibility, Motion, and Sound | D-012 | Approved constraint | No autoplay audio occurs before consent; mute remains persistent and reachable; meaningful spoken content has an equivalent text alternative. |
| UX-008 | Concise campus signs shall map unambiguously to the approved formal service titles. | P1 | UX and Content | D-010 | Approved constraint | Each sign-to-service mapping is unique in the publication manifest and the full title is available in accessible/semantic text. |
| UX-009 | The current exterior GLB shall remain untouched as comparison evidence. | P0 | 3D Asset Governance | D-001; D-013 | Approved constraint | File identity/provenance checks detect overwrite; production does not claim the asset as the editable master. |
| UX-010 | Production 3D shall use a versioned project-owned Blender master with approved provenance, scale/origin, entrance, atrium, modular interiors, materials, LODs, and exports. | P1 | 3D Asset Governance | D-013 | Approved constraint | Reuse occurs only with documented commercial modification rights; otherwise original geometry is created; side-by-side founder approval precedes switching. |
| UX-011 | WebGL shall remain the production renderer, while WebGPU experiments remain isolated and non-required. | P1 | 3D Architecture | D-004; D-014 | Approved constraint | Production and fallback journeys work with WebGPU disabled; no production dependency, acceptance test, or browser floor requires experimental WebGPU support. |

## 10. AI, handoff, and provider requirements

| ID | Requirement | Priority | Owner | Source | Status | Acceptance criteria |
|---|---|---:|---|---|---|---|
| AI-001 | Visitor AI shall answer only from an approved, versioned grounding bundle tied to the active publication release. | P0 | AI Governance | D-015; D-019 | Approved constraint | An answer cannot retrieve draft, rejected, stale, or checksum-mismatched evidence. |
| AI-002 | Substantive AI answers shall expose the supporting approved sources. | P0 | AI Governance | D-015 | Approved constraint | Citation evaluation maps each material factual claim to an accessible approved source; missing support triggers refusal rather than fabrication. |
| AI-003 | Missing or conflicting evidence shall produce a clear “cannot verify” response and a human or booking route. | P0 | AI Governance and Product | D-015 | Approved constraint | Adversarial tests for missing, contradictory, and out-of-scope evidence never produce a confident unsupported answer. |
| AI-004 | AI shall not bind price, scope, timeline, legal terms, delivery commitments, or acceptance decisions. | P0 | AI Governance and Legal | D-015 | Approved constraint | Commitment-seeking prompts yield a nonbinding explanation plus discovery/human route; generated language is not stored as an approved proposal. |
| AI-005 | Azure and production-licensed NVIDIA adapters shall sit behind one policy router for task, quality, cost, safety, data classification, residency, and availability. | P1 | AI Architecture | D-015 | Approved constraint | Every route decision is explainable/auditable and denies a provider when any policy dimension is unmet. |
| AI-006 | Approved PII or confidential visitor conversations shall use the approved Azure Europe route. | P0 | AI Governance and Privacy | D-015; D-017 | Approved constraint | Residency/routing tests prove classified payloads do not reach a non-approved region/provider; unavailable approved routing fails closed to human/booking. |
| AI-007 | NVIDIA shall initially receive only public or demonstrably de-identified data. | P0 | AI Governance and Privacy | D-015; MA-007 | Approved constraint | Test fixtures containing direct/indirect identifiers are blocked or routed elsewhere; production NVIDIA traffic remains disabled until entitlement and policy evidence pass. |
| AI-008 | AI input/output controls shall detect prompt-injection attempts and refuse secrets, classified material, controlled defense data, or requests to bypass evidence policy. | P0 | AI Security | D-017; D-018 | Approved constraint | Red-team cases cannot reveal hidden instructions, unapproved knowledge, secrets, or controlled content and always offer an approved safe route. |
| AI-009 | Public AI role names shall be transparent, including “Reception AI Concierge” and approved specialist labels. | P1 | Product and AI Governance | D-011; MP | Proposed specification | Every AI surface identifies itself as AI and does not impersonate a named human or imply unavailable specialist authority. |

## 11. Data and privacy requirements

| ID | Requirement | Priority | Owner | Source | Status | Acceptance criteria |
|---|---|---:|---|---|---|---|
| DATA-001 | PostgreSQL shall be the sole durable application source of truth. | P0 | Data Architecture | D-014; CON | Approved constraint | Production startup rejects missing/invalid PostgreSQL configuration; SQLite is explicit test-only and cannot silently receive production data. |
| DATA-002 | Redis, AI Search, caches, generated HTML, sitemaps, metadata, and 3D panels shall be ephemeral or rebuildable from approved durable state. | P0 | Data Architecture | D-014; CON | Approved constraint | Loss/rebuild tests restore derived state without data corruption, draft exposure, or ungrounded AI. |
| DATA-003 | Launch shall provide no visitor account and no visitor upload. | P0 | Product and Privacy | D-017 | Approved constraint | Public routes expose neither registration nor upload; attempts receive a safe refusal without persisting file content. |
| DATA-004 | Non-consented chat shall be ephemeral. | P0 | Privacy and AI Operations | D-017 | Approved constraint | Ending/expiry removes content from durable stores, retrieval, analytics, and logs except non-identifying operational counters allowed by policy. |
| DATA-005 | Consented chat, brief, and lead data shall expire after 90 days unless an approved active-client or legal-record rule applies; the rule shall not be silently extended to booking, meeting/provider, consent-proof, audit, or tombstone records. | P0 | Privacy Operations | D-017 | Approved constraint | Clock-controlled tests expire only data classes mapped to the approved 90-day rule and preserve only records with a valid, auditable exception basis. Booking/calendar, consent-proof, audit, and tombstone retention remain blocked until the Phase 1 data-classification and legal-policy matrix records their source, duration, exception authority, and deletion behavior. |
| DATA-006 | Verified deletion shall remove chat, derived traces, brief, and lead profile and shall prevent deleted records from reappearing after restore; any booking, meeting/provider, consent-proof, audit, or tombstone behavior requires an approved data-classification and legal-policy mapping. | P0 | Privacy and Data Operations | D-017 | Approved constraint | End-to-end deletion and backup-restore tests prove removal or tombstone enforcement across every class explicitly approved in scope. An unmapped class keeps deletion pending and cannot be reported complete; the specification does not infer deletion of a provider record or retention of a tombstone without approved authority. |
| DATA-007 | Visitor conversations shall never train models. | P0 | AI Governance and Privacy | D-017 | Approved constraint | Provider/configuration evidence and data-flow tests show no training/feedback destination receives visitor conversation content. |
| DATA-008 | Analytics shall be first-party, cookieless, aggregate-only, and focused on qualified organic discovery and booking outcomes. | P0 | Analytics and Privacy | D-017; D-020 | Approved constraint | No cross-site identifier or individual behavioral profile is stored; reports suppress or aggregate small cohorts per approved privacy rules. |
| DATA-009 | Phase 1 shall approve a data-classification matrix covering public, de-identified, personal, confidential, secret/credential, legal-record, and defense-sensitive data before provider or retention implementation. | P0 | Privacy, Security, and Legal | D-015 through D-018; MA-002; MA-011 | Proposed specification | Every collected field and provider route maps to one class, residency, retention, access, deletion, and refusal rule; unmapped data fails closed. |
| DATA-010 | Asynchronous external writes shall use idempotency, audit evidence, and a durable outbox or approved equivalent recovery contract. | P0 | Data and Integration Architecture | SB-01; D-016; D-019 | Approved constraint | Duplicate, timeout, and partial-failure tests produce no duplicate booking/notification/publication and leave a resumable auditable state. |

## 12. Security requirements

| ID | Requirement | Priority | Owner | Source | Status | Acceptance criteria |
|---|---|---:|---|---|---|---|
| SEC-001 | Staff identity shall use Entra SSO mapped to separately enforced author, reviewer, founder approver, and administrator roles. | P0 | Identity and Security | D-018 | Approved constraint | Role-matrix and negative authorization tests prove each role can perform only approved actions; group absence or ambiguity denies access. |
| SEC-002 | Authorization shall be enforced server-side for every protected action. | P0 | Security and Backend | D-018; SB-01; R-004 | Approved constraint | An authenticated non-admin receives 403 for administrator operations; removing a frontend guard does not bypass the API boundary. |
| SEC-003 | Exactly two dormant monitored local break-glass accounts shall use bcrypt, local MFA, controlled activation, alerts, and post-use rotation. | P0 | Identity and Security | D-018 | Approved constraint | Independent cases prove: both accounts are dormant during normal login; bcrypt verification and local MFA are both required after authorized activation; activation and use each create alert/audit evidence; use forces rotation and post-use review; and credential values never enter repository evidence. |
| SEC-004 | Browser staff sessions shall use rotating JWTs in `HttpOnly`, `Secure`, `SameSite` cookies with a 30-minute idle timeout and eight-hour absolute timeout. | P0 | Identity and Security | D-018 | Approved constraint | Cookie inspection and clock-controlled tests verify attributes, rotation, idle expiry, absolute expiry, and rejection after expiry. |
| SEC-005 | State-changing browser requests shall use CSRF protection and explicit idempotent logout. | P0 | Security and Backend | D-018 | Approved constraint | Cross-site requests without a valid CSRF proof fail; logout revokes/clears the session and repeated logout is harmless. |
| SEC-006 | Production rate limits shall use Redis-backed account and network counters with progressive delay. | P0 | Security and Operations | D-018; D-014 | Approved constraint | Distributed-worker tests enforce the same limit, return bounded retry guidance, and do not allow a single network to lock unrelated accounts indefinitely. |
| SEC-007 | Production controls shall include least privilege, restricted CORS, CSP, WAF, encryption in transit/at rest, redacted logs, and alertable security events. | P0 | Security and Platform | D-018 | Approved constraint | Independent review finds no wildcard production trust, plaintext sensitive path, secret/PII logging, or unmonitored critical authentication event. |
| SEC-008 | Secrets and credential material shall never enter source, documentation, logs, chat, generated evidence, or public client bundles. | P0 | Security and All Owners | CON; D-018; D-022 | Approved constraint | Secret scanning and client-bundle inspection pass; authentication uses approved OAuth/secret storage without printing values. |
| SEC-009 | Privacy, AI, consent, retention, SEO claims, responsible disclosure, and defense behavior shall receive independent legal/security review before their applicable public gate. | P0 | Legal and Security | D-017; D-018; MA-002; MA-011 | Approved constraint | Each applicable release links dated findings, resolution evidence, and founder disposition; missing review keeps only affected content/capability held. |
| SEC-010 | Each local break-glass credential shall be randomly generated with at least 24 characters and approved high entropy. | P0 | Identity and Security | D-018; MP | Approved constraint | The security specification records and tests the approved generator, 24+ length/entropy threshold, storage and rotation owner, and rejection of weak or reused credentials before account creation; every generated value remains outside source, documentation, logs, chat, and evidence. |

## 13. Non-functional and operational requirements

### 13.1 Quality and reliability

| ID | Requirement | Priority | Owner | Source | Status | Acceptance criteria |
|---|---|---:|---|---|---|---|
| NFR-001 | Quick Access shall meet p75 LCP ≤2.5 seconds, INP ≤200 milliseconds, and CLS ≤0.1 on the approved measurement profile. | P0 | Performance and Frontend | D-020 | Approved constraint | Lab and field-ready evidence uses documented devices/networks and passes all three thresholds; lazy 3D work cannot regress the semantic path. |
| NFR-002 | Initial lazy 3D transfer shall be ≤8 MB desktop and ≤4 MB mobile, with each incremental room ≤5 MB desktop and ≤2.5 MB mobile. | P0 | 3D and Performance | D-020 | Approved constraint | Compressed transfer manifests at the defined cache state pass each budget; budget failure triggers lower tier/Quick Access rather than blocking conversion. |
| NFR-003 | The foundation shall prove 25 concurrent visitors and three simultaneous chats. | P0 | QA and Operations | D-020 | Approved constraint | A repeatable load profile completes representative browse, chat, and booking-entry flows without integrity error or unhandled failure. |
| NFR-004 | The public site, API, and AI/booking entry shall target 99.9% monthly availability. | P0 | Operations | D-020 | Approved constraint | The SLI/SLO definition specifies numerator, denominator, exclusions, and measurement source; alerts and error-budget reporting can detect breach. |
| NFR-005 | Launch recovery shall target RPO ≤24 hours and RTO ≤8 hours while retaining both as explicit reassessment risks. | P0 | Operations and Founder | D-020; R-014 | Approved constraint | Backup/restore and timed recovery drills meet targets; founder risk review remains open until commercial/contractual value confirms adequacy. |
| NFR-006 | Browser support shall cover the latest two stable evergreen releases, with Safari/iOS 16.4 as the minimum legacy floor. | P0 | Frontend and QA | CON; MP | Approved constraint | Browser matrix tests the approved current versions; unsupported clients receive semantic Quick Access rather than a broken or misleading experience. |
| NFR-007 | Phase 1 shall define numerical device-tier frame-time, memory, and thermal/degradation targets before 3D implementation. | P0 | 3D and Performance | D-020; R-011 | Approved constraint | The approved 3D specification names device tiers, measurement method, pass/fail thresholds, and fallback trigger; legacy 45–60/30 FPS numbers are not inherited automatically. |
| NFR-008 | The first-visit arrival shall target approximately eight seconds and remain skippable. | P1 | Motion and UX | MP; D-011; D-012 | Proposed specification | Storyboard timing is measured from user activation to reception; skip reaches an equivalent stable state promptly and reduced motion bypasses nonessential travel. |

### 13.2 Delivery, technology, and operations

| ID | Requirement | Priority | Owner | Source | Status | Acceptance criteria |
|---|---|---:|---|---|---|---|
| OPS-001 | Material work shall use Codex-native project-manager/specialist coordination with independent producer/reviewer separation and durable phase state. | P0 | Project Management | D-003 | Approved constraint | No separate workflow service is introduced; deliverables record create, validate, inspect, review, revise, validate-again, and founder-approval evidence. |
| OPS-002 | Existing source, user-owned dirty-tree work, and the exterior GLB shall be preserved as protected prototype evidence. | P0 | Project Management and Engineering | D-001; R-002 | Approved constraint | Scope/diff checks show no unrelated overwrite, relocation, staging, cleanup, or production-readiness claim. |
| OPS-003 | Application feature work, dependency upgrades, migrations, infrastructure changes, and production design implementation shall remain blocked until Phase 1 acceptance. | P0 | Project Management | D-002; D-024; STATE | Approved constraint | State remains Phase 1 `in_progress`; no prohibited file/action appears in Phase 1 evidence; only explicit founder acceptance can open Phase 2. |
| OPS-004 | Production shall retain the approved React/TypeScript/Vite/Tailwind/R3F and FastAPI/SQLAlchemy/Alembic/PostgreSQL families on the newest mutually compatible stable set. | P0 | Architecture | D-004; D-014 | Approved constraint | The compatibility matrix evaluates coupled runtimes/frameworks/peers and contains no preview, beta, RC, nightly, or experimental production requirement. |
| OPS-005 | Every version-sensitive choice shall use a dated Context7 query plus official primary release, registry, runtime, browser, cloud, and migration evidence. | P0 | Architecture and Supply Chain | D-004 | Approved constraint | Each matrix row records library ID, query date, current/target, constraints, breakages, security status, evidence, tests, and rollback; missing evidence prevents lock selection. |
| OPS-006 | Exact production dependencies and artifacts shall be reproducibly locked, with SBOM and license inventory for every release. | P0 | Supply Chain | D-004; D-021 | Approved constraint | Fresh deterministic builds resolve identical artifacts; no unbounded production dependency, floating image/action, prohibited license, or unresolved production-critical deprecation remains. |
| OPS-007 | A blocked newest stable major shall use only the newest proven-compatible stable alternative under a dated approved ADR with rollback and quarterly recheck. | P0 | Architecture | D-004; D-021 | Approved constraint | Exception evidence states the exact blocker and expiry/recheck date; removing the blocker reopens evaluation rather than making the exception permanent. |
| OPS-008 | Known WorldHUD, RBAC, and database-configuration defects shall be reproducibly covered and stabilized before modernization waves. | P0 | Engineering and QA | PROJECT; R-003; R-004; R-005 | Approved constraint | Failing regression/negative tests exist before fixes; a trustworthy baseline passes after the bounded fixes and before dependency upgrades. |
| OPS-009 | Toolchain, React, 3D, backend, database, and cloud modernization shall run as separately reversible waves. | P0 | Architecture and QA | D-004; D-023 | Approved constraint | Each wave has baseline, migration, build/test, independent review, rollback evidence, and no hidden feature work before the next wave starts. |
| OPS-010 | The production target shall use approved Azure-managed boundaries: Front Door/versioned static storage, Container Apps, PostgreSQL, Managed Redis, AI Search, Azure/NVIDIA policy adapters, Monitor/Application Insights, and GitHub Actions OIDC. | P0 | Architecture and Platform | D-014; D-015 | Approved constraint | Phase 1 architecture assigns responsibilities and failure boundaries to every component; obsolete AWS targets are absent from the approved target. |
| OPS-011 | PostgreSQL 18’s current stable minor shall be targeted only when GA and supported in the approved Azure region; otherwise the newest regional GA major requires an ADR and quarterly recheck. | P0 | Data and Platform Architecture | D-004; D-014 | Approved constraint | Dated regional availability evidence selects one supported major and documents upgrade/restore/rollback; no unsupported database target enters production. |
| OPS-012 | Production releases shall use immutable artifacts, container digests, GitHub Action commit SHAs, zero-traffic candidate revisions, manual promotion, and tested rollback. | P0 | Deployment and Supply Chain | D-014; D-021 | Approved constraint | Candidate verification completes before traffic; rollback restores the prior release; no production artifact references `latest`. |
| OPS-013 | Dependency proposals shall be grouped weekly, security alerts immediate, major upgrades never auto-merged, next-stable canaries monthly, and database/cloud major availability reviewed quarterly. | P1 | Supply Chain Operations | D-021 | Approved constraint | Governance configuration and monthly/quarterly records show human approval and full CI; critical exploitable issues are triaged immediately and supported high-severity fixes target seven days. |
| OPS-014 | Paid deployment and production AI require approved envelopes; every other paid item requires separate approval with cost and a free alternative. | P0 | Founder and Finance | D-022; MA-010 | Approved constraint | No billing/provisioning action occurs without a dated envelope, provider/SKU, region, limits, alerts, and stop conditions; unapproved options remain inactive. |
| OPS-015 | Delivery shall follow Phases 0 through 9 in the approved order, with each material phase accepted before its dependent phase opens. | P0 | Project Management | D-023; D-024 | Approved constraint | `PROJECT_STATE.yaml` exposes only the earliest approved executable phase; later-phase markers cannot authorize implementation. |

## 14. Decision coverage matrix

| Decision | Covered by requirements | Coverage result |
|---|---|---|
| D-001 | OPS-002; UX-009 | Existing repository and GLB remain protected prototype evidence. |
| D-002 | OPS-003 | Complete Phase 1 definition precedes application development. |
| D-003 | OPS-001 | Codex-native orchestration, reviewers, state, and gates are required. |
| D-004 | UX-011; OPS-004 through OPS-009; OPS-011 | Latest mutually compatible stable graph and reversible modernization are binding. |
| D-005 | BR-001 through BR-004; BR-009; FR-004; FR-019 | Audience, sectors, custom discovery, booking qualification input, and email-verification boundary are defined. |
| D-006 | BR-006; BR-007; SEO-009 | Identity and substantiated-claim boundaries are defined. |
| D-007 | BR-007; BR-008; SEO-006; SEO-011; PUB-006; PUB-007 | Proof, demos, experts, and human evidence review are covered. |
| D-008 | FR-001; FR-002; SEO-001 through SEO-003; SEO-007; UX-002 | Semantic/Quick Access equivalence and index rules are covered. |
| D-009 | BR-010; FR-017; FR-018; SEO-004; SEO-010; SEO-012 | Routes, English launch, content floor/cadence, and ethical authority are covered. |
| D-010 | BR-005; FR-001; FR-017; UX-008 | Five wings, ten services, signs, and shared content spaces are covered. |
| D-011 | BR-011; BR-012; FR-003; AI-009; NFR-008 | Foundation and wing sequence are covered. |
| D-012 | FR-012 through FR-014; UX-001 through UX-008; NFR-008 | Interaction, onboarding, audio, and recovery paths are covered. |
| D-013 | UX-009; UX-010; PUB-006 | Protected GLB, new Blender master, provenance, and approval are covered. |
| D-014 | FR-016; DATA-001; DATA-002; SEC-006; OPS-004; OPS-010 through OPS-012 | Azure architecture, PostgreSQL truth, Redis, and immutable delivery are covered. |
| D-015 | AI-001 through AI-008; DATA-009; OPS-010 | Grounding, provider policy, residency, and nonbinding AI are covered. |
| D-016 | FR-005 through FR-011; FR-016; FR-019; DATA-010 | Anonymous chat, explicit availability, console, alerts, handoff, verification states, and booking are covered. |
| D-017 | BR-009; DATA-003 through DATA-009; AI-006 through AI-008; SEC-009 | Consent, retention, deletion, analytics, training, and sensitive-data rules are covered. |
| D-018 | SEC-001 through SEC-010; AI-008 | Entra, break glass, random 24+ character credentials, cookies, CSRF, rate limits, and security controls are covered. |
| D-019 | FR-002; SEO-005; SEO-008; SEO-011; PUB-001 through PUB-005; AI-001 | Atomic publication, separation, isolation, and rollback are covered. |
| D-020 | BR-001; DATA-008; NFR-001 through NFR-007 | Conversion, Core Web Vitals, 3D/load/SLO/recovery targets, and device-tier proposal are covered. |
| D-021 | OPS-006; OPS-007; OPS-012; OPS-013 | Dependency governance, SBOM/licenses, immutable pins, and canaries are covered. |
| D-022 | SEC-008; OPS-014 | Spending, credentials, and external actions remain gated. |
| D-023 | BR-012; OPS-009; OPS-015 | Approved phase and wing sequencing is preserved. |
| D-024 | OPS-003; OPS-015 | Phase 0 acceptance opens definition work only. |

## 15. Dependencies

| Dependency | Affected requirements | State and rule |
|---|---|---|
| Verified legal entity, contacts, jurisdiction, and legal review route | BR-006; SEO-009; SEC-009; DATA-009 | Blocked by MA-002; no facts may be invented. |
| Verified cases, demos, experts, owners/backups, biographies, portraits, rights, and consent | BR-007; BR-008; FR-006; FR-017; PUB-006; SEO-011 | Blocked by MA-003; unverifiable items remain held. |
| Exterior GLB source/license/provenance | UX-009; UX-010; PUB-006 | Blocked by MA-004 for geometry reuse; visual-reference-only work may continue. |
| Approved Azure tenant/subscription/region and cost envelope | AI-006; OPS-010; OPS-011; OPS-014 | Blocked by MA-005/MA-010 for capability/provisioning and cost decisions. |
| Booking mailbox, Entra groups, room owners/backups, Teams app consent | FR-006 through FR-010; FR-019; SEC-001 | Blocked by MA-006 for live integration; contracts and failure cases may be defined now. |
| NVIDIA entitlement, DPA, region, and cost | AI-005; AI-007; OPS-014 | Blocked by MA-007; only public/de-identified development evaluation is allowed. |
| Domain and webmaster ownership | SEO-002; SEO-008; SEO-009 | Blocked by MA-008/MA-009 for external verification/submission; canonical definition remains approved. |
| Approved brand, Stitch/Figma, motion, sound, and 3D references | BR-006; FR-003; UX-001 through UX-011; NFR-007; NFR-008 | Produced and separately approved within Phase 1 before production implementation. |
| Dated technology compatibility matrix and ADRs | FR-015; OPS-004 through OPS-013 | Must be complete and conflict-free before Phase 2 upgrade work. |

## 16. Assumption ledger

| ID | Assumption | Safety/impact | Status |
|---|---|---|---|
| A-001 | Requirement owners are functional roles, not named people. | Avoids inventing staff assignments; MA-003/MA-006 must supply names later. | Safe and reversible. |
| A-002 | “Approved constraint” means policy intent is approved, not that code, content, integration, or launch evidence passes. | Prevents false readiness claims. | Binding interpretation. |
| A-003 | The approved buyer-role list is sufficient for this foundation despite missing interview notes. | No detailed pain points, quotations, budgets, or segment sizes are inferred. | Nonblocking for draft; research may refine without changing scope. |
| A-004 | `hengshidesign.com` is the approved canonical definition, while ownership/control remains unverified. | SEO architecture can proceed; DNS changes cannot. | Safe; MA-008 remains blocked. |
| A-005 | All legacy seeded projects, experts, outcomes, and company facts are unverified until entered in the proof inventory. | Prevents accidental publication of fictional evidence. | Binding safe default. |
| A-006 | Existing APIs are preserved during migration, but their current security behavior is not approved as the production contract. | Allows regression planning without retaining insecure localStorage/Bearer-only or broken authorization behavior. | Safe and reversible. |
| A-007 | RPO ≤24h and RTO ≤8h are accepted initial targets but not residual-risk acceptance. | Keeps R-014 visible for launch reassessment. | Binding interpretation. |
| A-008 | Exact versions, cloud SKUs, provider models, costs, tokens, visual identity, and device-tier 3D thresholds belong to their specialist Phase 1 artifacts. | Avoids premature implementation prescription. | Nonblocking for requirements draft. |
| A-009 | Unpublished/closed wings may be architecturally present but cannot imply capability proof, availability, or completion. | Preserves the campus concept without misleading visitors. | Safe and reversible. |

## 17. Conflict and legacy reconciliation ledger

| ID | Source conflict | Controlling resolution | Requirement effect |
|---|---|---|---|
| C-001 | Legacy SRS/SPEC name React 18, Python 3.11+, PostgreSQL 16, and loosely “latest” packages as targets. | D-004 and OPS-004 through OPS-007. | Those versions are current/prototype evidence only; the dated compatibility graph selects exact stable targets. |
| C-002 | Legacy SAD, backlog, deployment diagram, and spec 005 target AWS/S3/CloudFront/ECS/RDS. | D-014 and OPS-010 through OPS-012. | Azure is the only approved production target; AWS material remains historical. |
| C-003 | Legacy SRS makes defense a primary launch market and lists many secondary/emerging sectors. | D-005, BR-003, and BR-009. | Agriculture then mining are public priorities; defense and other sectors are not launch scope without decisions. |
| C-004 | Legacy SRS proposes managed PaaS, data monetization, IoT, multi-tenancy, billing, marketplace, mobile, and Kubernetes programs. | D-005, D-023, and section 19 exclusions. | They are not current product requirements and require separate future approval. |
| C-005 | Legacy SPEC treats the 3D world as the primary navigation with no traditional menu and a reduced static-gallery fallback. | D-008, D-012, FR-001, UX-002, and UX-005. | Semantic Quick Access is complete and equivalent; fallbacks may reduce rendering cost, not content or conversion. |
| C-006 | Legacy 3D guide requires a 100× scale and fixed palette/type/timings without current provenance or identity approval. | D-006, D-013, UX-010, and the Phase 1 design gate. | These are reference observations only; the new identity and Blender master set approved scale/tokens. |
| C-007 | Legacy performance targets include `<3s including 3D`, 45–60 FPS desktop, 30+ mobile, API/DB timing estimates, and RTO <4h. | D-020 and NFR-001 through NFR-008. | Approved Core Web Vitals, transfer, load, availability, RPO/RTO targets control; device-tier thresholds require Phase 1 approval. |
| C-008 | Legacy auth says Bearer/localStorage, 120-minute tokens, one admin, and incorrectly records RBAC as implemented. | D-018, SEC-001 through SEC-006, and R-004. | Entra roles, secure rotating cookies, CSRF, break glass, timeouts, and negative authorization tests control. |
| C-009 | Draft security sources disagree on login windows, password policy, cookie default, sanitizer behavior, and in-memory versus Redis rate limits. | D-018 and the future approved security/API contract. | This document requires the security outcomes but does not select unapproved numeric password/login policies; Redis is required for production counters. |
| C-010 | Legacy data lifecycle is indefinite with manual backup and mutable single-state content. | D-017, D-019, DATA-004 through DATA-010, and PUB-001 through PUB-005. | Consent retention, verified deletion, immutable releases, draft isolation, outbox, and recovery requirements control. |
| C-011 | Legacy project/portfolio seeds and status percentages may be treated as public proof or current readiness. | D-007, R-008, R-015, BR-008, and PUB-006. | Seeds remain quarantined; readiness is evidence-based and qualitative until gates pass. |
| C-012 | Legacy SPEC lists chat and AI as MVP non-goals. | D-011, D-015, D-016, and AI/FR requirements. | Approved foundation now includes one grounded Reception AI Concierge, handoff, and booking. |

All identified legacy conflicts above are resolved by approved decisions at the
requirements-policy level. None authorizes implementation. The remaining choices
below are human or specialist gates rather than silent conflicts.

## 18. Founder-input questions and human gates

| ID | Decision/input required | Current safe behavior | What it blocks |
|---|---|---|---|
| Q-001 | What verified legal entity/display name, business/privacy contacts, jurisdiction, and independent legal-review route may be published? | Publish no inferred legal facts or private addresses. | Final trust/privacy/contact/legal content and launch review. |
| Q-002 | Which cases, outcomes, capability demos, experts, biographies, portraits, media rights, and publication consents are verified? | Hold every legacy seed and unsupported claim. | Proof, expert, Work/Demos, insight bylines, and room content approval. |
| Q-003 | Who are the approved room/service owners and backups? | Show no false live availability or named ownership. | Live handoff and booking routing. |
| Q-004 | Is commercial reuse/modification of the existing GLB proven, or must it remain visual reference only? | Do not reuse its geometry in the new master. | Existing-geometry reuse; not the independent original rebuild specification. |
| Q-005 | Which Azure tenant/subscription and Europe-first region are approved, and what cost envelope/stop conditions apply? | Perform no provisioning or paid capability activation. | Final cloud feasibility/cost decision and later provisioning. |
| Q-006 | Which booking mailbox, Entra groups, Teams recipients/app consent, owner policy, and calendar rules are approved? | Define contracts only; make no Microsoft 365 write. | Live handoff and booking integration. |
| Q-007 | Is a production NVIDIA entitlement, DPA, region, data-class permission, and cost envelope approved? | NVIDIA remains non-production and public/de-identified only. | NVIDIA production routing. |
| Q-008 | Which organizational Search Console/Bing accounts and DNS authority will own verification? | Make no DNS/webmaster write. | Search verification and submission, not SEO definition. |
| Q-009 | Which proposed device-tier frame-time, memory, and thermal/degradation thresholds are accepted after the 3D specialist supplies evidence? | Inherit no legacy FPS figure. | 3D production acceptance. |
| Q-010 | Are RPO ≤24h and RTO ≤8h acceptable at launch after costed restore evidence, or must they be tightened? | Retain them as targets and an explicit unresolved risk. | Residual recovery-risk acceptance. |
| Q-011 | Is the proposed Phase 1 data-classification matrix and legal basis/consent wording accepted? | Unmapped or sensitive data fails closed and is not retained/routed. | Final privacy, AI, analytics, and retention implementation. |
| Q-012 | Does any exact defense scope proceed to independent legal/security review? | Defense remains unpublished, unindexed, and unavailable to visitor AI. | Defense publication only. |
| Q-013 | What phase budget, delivery envelope, and timing commitments may be made? | Record no public or contractual amount/date; no paid action occurs. | Cost approval and any external commitment, not independent definition work. |
| Q-014 | Which Phase 1 brand, UI, motion, sound, and 3D directions are accepted after specialist review? | Existing prototype visuals remain non-authoritative. | Production design implementation. |

## 19. Explicit out of scope

- Application/UI source changes, dependency or lockfile changes, migrations, data
  mutation, infrastructure provisioning, paid activation, external design writes,
  Git actions, publication, and deployment during this requirements task.
- Public defense content or ordinary visitor-AI defense handling before Q-012 and
  MA-011 are satisfied.
- Visitor accounts, visitor uploads, fixed public pricing, binding AI estimates,
  and AI training on visitor conversations at launch.
- Legacy PaaS resale, data monetization APIs, IoT device management, multi-tenancy,
  billing/subscriptions, marketplace, white-label, native mobile, and Kubernetes
  programs unless a later founder decision adds them.
- WebGPU as a production dependency; WASD/collision walking, gamification, and
  easter eggs.
- Fabricated geographic pages, reviews, customers, awards, locations, experts,
  cases, outcomes, ratings, or superiority claims.
- Final keyword research, exact canonical inventory, brand identity, UI screens,
  Blender production scene, exact API schemas, data model, threat model, exact
  dependency versions, cloud SKUs, or cost estimates; each belongs to its bounded
  Phase 1 specialist artifact.

## 20. Requirements-package acceptance gate

This document is ready for independent review when:

1. Every requirement row has a unique ID, priority, owner, source, status, and
   testable acceptance criteria.
2. D-001 through D-024 each map to one or more requirements.
3. Legacy conflicts are either resolved by approved decisions or recorded as a
   scoped human gate.
4. No public claim, person, customer, location, price, cost, timeline, legal fact,
   or implementation state is invented.
5. Open founder inputs are clearly separated from independent Phase 1 work.

Independent requirements review must assess atomicity, ambiguity, feasibility,
negative/error states, priority, source strength, testability, and cross-artifact
consistency. The project manager—not this producer—owns review disposition,
durable state updates, and the final founder approval gate.
