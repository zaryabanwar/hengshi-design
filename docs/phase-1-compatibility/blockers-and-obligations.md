# Compatibility blockers and rollback/test obligations

**Snapshot:** 2026-07-19
**Status:** Required constraints for later compatibility spikes; no upgrade is authorized

## Blocking gates

| ID | Blocker or human gate | Why it blocks lock selection | Required exit evidence |
|---|---|---|---|
| GATE-COMP-001 | Exact target locks are intentionally deferred. | Registry state, security status, peers, and cloud support can change before an upgrade wave. | Fresh same-day Context7, official docs, registry, advisory, license, and peer-graph recheck plus approved wave plan. |
| GATE-COMP-002 | Known hook-order, admin authorization, and database-configuration defects remain. | Upgrading on an untrustworthy baseline obscures regressions and can preserve insecure behavior. | Failing regression/negative tests first, bounded fixes, browser/API evidence, and independent review before modernization. |
| GATE-COMP-003 | TypeScript 7 has no programmatic API, while typescript-eslint documents TypeScript support only below 6.1. Microsoft documents a stable side-by-side TypeScript 7 compiler plus `@typescript/typescript6` API/tooling bridge. | Neither the bridge topology nor a TypeScript 6-only exception has been tested against this repository's diagnostics, editor, build, and lint behavior. | Spike both paths: (A) TypeScript 7 compiler plus official TypeScript 6 API/tooling bridge and npm alias; (B) TypeScript 6-only compatibility exception. Select neither without full parity evidence and review; path B additionally requires a dated exception ADR and quarterly recheck. |
| GATE-COMP-004 | Python dependencies are unbounded and have no deterministic lock workflow. | The installed venv cannot be reproduced from `requirements.txt`; declared and installed state already diverge for pytest-asyncio. | Approved standards-based lock approach, hashes, fresh environment sync/check, dependency tree, SBOM/license report, and frozen-install proof. |
| GATE-COMP-005 | PostgreSQL 18.4 is not verified in the founder-approved Azure region. | General GA documentation does not prove regional availability, extensions, HA, quota, cost, or approved residency. | MA-005/MA-010 inputs, read-only regional capability evidence, feature/extension matrix, cost envelope, backup/restore rehearsal, and founder architecture/cost approval. |
| GATE-COMP-006 | Docker/Compose capability timed out. | Executable presence does not prove engine connectivity, API negotiation, Compose parsing, image availability, or health behavior. | A bounded successful version/engine/Compose capability recheck; timeout or partial output remains a failure. |
| GATE-COMP-007 | Container and CI references are not immutable. | `postgres:16` floats and no GitHub Actions workflow, action SHA, Dockerfile, or image digest exists. | Approved CI/container design, digest and action-SHA policy, candidate build, SBOM/provenance, non-root/security review, and rollback evidence. |
| GATE-COMP-008 | Browser and 3D device matrices are incomplete. | Chromium-only Playwright configuration cannot prove latest-two evergreen releases, Safari/iOS 16.4, WebGL failure recovery, or device budgets. | Current browser-version matrix, WebKit/Safari device evidence, non-WebGL/reduced-motion/asset-failure paths, and approved device-tier thresholds. |
| GATE-COMP-009 | Dependency security evidence is incomplete. | Full npm audit attempts timed out; Python advisory, SBOM, and license evidence were not produced. | Bounded successful advisory scans, exploitability triage, SBOM/license inventory, and no unresolved production-critical warning. |
| GATE-COMP-010 | Azure/NVIDIA/provider entitlement, data, region, and cost choices remain human gates. | These are material vendor, privacy, compliance, security, and cost decisions. | MA-005, MA-007, and MA-010 evidence plus founder approval; no paid activation or production route before approval. |
| GATE-COMP-011 | npm 12.0.1 is the latest stable candidate compatible with Node 24.18.0; bundled npm 11.16.0 is not the primary target. | Selecting the bundled version merely for lower change would bypass the approved latest-compatible policy. | Spike npm 12.0.1 first with frozen installs, lock drift, lifecycle scripts, and clean relock comparison. Use 11.16.0 only with concrete blocker evidence, a dated exception ADR, independent review, founder approval, and quarterly recheck. |
| GATE-COMP-012 | Required Redis, Azure AI/Search, Microsoft Graph, telemetry, NVIDIA, Blender/glTF, CI-action, container-image, and Bicep/API-version families are absent. | Omitting absent families would force implementers to invent architecture later; selecting exact packages now would invent unapproved product, vendor, data, security, cost, and deployment decisions. | Close the corresponding `deferredFamilies` record with approved requirements/architecture, official stable and lifecycle evidence, coupling proof, threat/data/cost review, tests, rollback, independent review, and applicable founder approval. |

## Failure modes that every later wave must test

| Boundary | Required failure evidence |
|---|---|
| Runtime/toolchain | Unsupported Node/editor/CI runtime fails early; frozen install rejects lock drift; build cache cannot conceal a compiler/bundler regression. |
| React/Router | Hook order, Strict Mode, Suspense, error reporting, route transitions, direct URL loading, 404s, admin navigation, and hydration/prerender boundaries remain correct. |
| 3D renderer | WebGL context loss, asset timeout/404, decoder failure, low memory, reduced motion, non-WebGL, resize, navigation, and scene disposal recover to semantic Quick Access without losing conversion. |
| Styling | Tailwind migration preserves all approved tokens/states, focus, contrast, responsive layouts, content scanning, production CSS, and visual baselines; missing utilities fail CI. |
| Backend | Import/startup failure, invalid configuration, validation errors, authn/authz negatives, CORS/CSRF, rate limits, lifespan, WebSocket, HTTPX test-client, and OpenAPI compatibility are explicit. |
| Database | Missing/invalid PostgreSQL configuration fails closed; upgrade/downgrade, lock timeout, partial DDL, extension mismatch, connection loss, backup corruption, restore, and application rollback are rehearsed. |
| QA | Browser binary drift, unavailable browser, test retry masking, accessibility engine failure, Lighthouse timeout, and load-tool failure are reported as failures, never passes. |
| Container/CI/cloud | Image pull/digest mismatch, unhealthy readiness, secret absence, OIDC denial, region/quota denial, zero-traffic candidate failure, observability loss, and traffic rollback are exercised. |

## Separately reversible implementation slices

The order below is a compatibility dependency order, not implementation
authorization. Each slice requires its own approved bounded contract. The
machine-readable authority for wave/checkpoint membership and all 27 edge
assignments is `compatibility-controls.json`; every listed checkpoint is currently
unaccepted.

| Wave | Scope | Entry gate | Required tests | Rollback obligation |
|---|---|---|---|---|
| WAVE-00 / CP-00 | Stabilize known hook-order, admin-authorization, and PostgreSQL-configuration defects without dependency changes | Later approved Phase 2 contract after Phase 1 acceptance | Failing regression/negative tests first; real entry/inside browser path; viewer-role negatives; PostgreSQL-only startup | Restore only the bounded source patch and retain regression evidence |
| WAVE-01 / CP-01 | Node and npm as one runtime pair; npm 12 primary and bundled npm only as an exception | CP-00; HG-001, HG-002, and HG-003 remain unsatisfied | Frozen root/web installs, lock drift, lifecycle scripts, clean relock, editor/CI parity | Restore prior Node/npm pair, runtime descriptor, and exact locks |
| WAVE-02 / CP-02 | Vite and React plugin pair | CP-01; exact-lock gate | Development/HMR, production build/preview, JSX transform, source maps, bundle comparison | Restore prior Vite/plugin pair, config, and lock |
| WAVE-03 / CP-03 | TypeScript compiler/API topology plus ESLint/parser/plugins | CP-02; TypeScript and exception gates | Typecheck, typed lint, rule inventory, editor/CI diagnostics, no unsafe suppressions | Restore prior compiler, lint packages, config, and lock as one set |
| WAVE-04 / CP-04 | **Atomic** React, React DOM, both React type packages, R3F, and Drei transition | CP-03; exact-lock gate | Peer resolution; Strict Mode/hooks; routes; 3D asset/interaction/context-loss/visual/memory/performance/reduced-motion/fallback; forward and reverse install/build/browser proof | Restore React 18.3.1, DOM 18.3.1, React types 18, R3F 8.18.0, Drei 9.122.0, and prior lock together |
| WAVE-05 / CP-05 | React Router package/import topology | CP-04; retained Router 6 must already have same-spike peer/route proof or join WAVE-04 before CP-04 | Route matrix, direct loads, navigation, 404/error boundaries, admin negatives, three browsers | Restore only prior Router package/import topology |
| WAVE-06 / CP-06 | Three renderer core | CP-05; CP-04 must prove retained Three 0.160.1 satisfies R3F/Drei peers and behavior | Renderer/loaders, color/shaders, screenshots, memory/disposal, frame-time/thermal, context loss | Restore the retained proven Three version and lock |
| WAVE-07 / CP-07 | Zustand state layer | CP-06; exact-lock gate | Selectors/subscriptions, render loop, scene navigation/disposal, forward/reverse browser proof | Restore prior Zustand package and integration |
| WAVE-08 / CP-08 | GSAP motion layer | CP-07; exact-lock gate | Reduced motion, animation cleanup, navigation/focus, forward/reverse browser proof | Restore prior GSAP package and integration |
| WAVE-09 / CP-09 | Tailwind/PostCSS/Autoprefixer topology without UI redesign | Approved UI references; CP-08 | Production CSS, prefixes, responsive/focus/contrast/visuals, Safari/iOS floor, bundle size | Restore prior styling config and lock |
| WAVE-10 / CP-10 | Python runtime, backend/data/auth/test packages, and deterministic Python lock without schema change | CP-09; Python-lock and exact-lock gates | Two identical hashed syncs, imports/typing, API/OpenAPI, auth negatives, lifespan/WebSocket/async/full pytest, advisory/SBOM/license/deprecations | Restore prior runtime, exact lock, and environment image; schema rollback is outside this wave |
| WAVE-11 / CP-11 | Approved regional PostgreSQL service and runtime truth | CP-10; Azure/PostgreSQL, migration, and residual-risk gates | Regional features/extensions, full Alembic graph, partial failure/locks, driver/query performance, immutable backup/timed restore, application rollback and RPO/RTO | Rehearsed restore or parallel prior supported major with compatible application window |
| WAVE-12 / CP-12 | Playwright/browser revisions, axe, Lighthouse, and browser/device matrix | CP-11; exact-lock gate | Chromium/Firefox/WebKit and Safari/iOS evidence, actual entry/inside paths, console/network capture, axe-engine failure, Lighthouse timeout failure, screenshots/traces | Restore prior proven QA tools, browser revisions, adapters, and reports |
| WAVE-13 / CP-13 | Containers, CI actions, Azure APIs/Bicep, observability, and provider adapters | CP-12; architecture, provider/data/cost, paid/external, Git, deployment, and residual-risk gates | Reproducible non-root images; digest/action-SHA; OIDC/RBAC negatives; provider quota/residency/deletion; zero-traffic candidate; readiness/observability/recovery/traffic rollback/cost stops | Retain prior immutable release and compatible data; disable the bounded candidate and reverse traffic only after health checks |

CP-04 can never accept React 19 with R3F 8 or Drei 9. Three remains separate
only because the recorded retained 0.160.1 version satisfies the candidate peer
floors; that metadata fact still requires same-spike behavior proof. Router,
Zustand, and GSAP remain separate only at checkpoints whose retained peer and
behavior evidence is complete.

## Concrete rollback evidence required for every package wave

1. Record the pre-wave runtime versions, manifest/lock hashes, build output hash,
   database compatibility boundary, and test evidence.
2. Use an approved branch/commit or equivalent immutable snapshot before changes;
   this inventory does not create one.
3. Change only one wave's coupled graph. Do not mix product features, folder moves,
   UI redesign, schema changes, or cloud rollout into a package wave.
4. Prove forward install/build/test and reverse install/build/test from a clean
   environment. A cached local success is insufficient.
5. Define rollback triggers before promotion: failed contract, authorization,
   browser, accessibility, visual, performance, security, migration, readiness,
   observability, or recovery evidence.
6. Keep data backward-compatible across source-only waves. Database waves require
   a restore or dual-version compatibility plan; a package-lock revert alone is
   not a database rollback.
7. Retain logs and reports without credentials or matched secret values.

## Human decisions retained

The machine records `HG-001` through `HG-015` in
`compatibility-controls.json` are all `unsatisfied`. They separately retain:

- every exact lock and every compatibility-exception ADR;
- npm primary-versus-exception and TypeScript compiler/API-topology decisions;
- Azure tenant/subscription/region, PostgreSQL generation/features/HA/quota,
  residency, backup/recovery, capacity, and cost;
- the Python lock workflow and container/CI/immutable-reference architecture;
- Azure AI/Search services and SDKs, Microsoft Graph resources/permissions, and
  NVIDIA production entitlement, including provider/API/model, DPA, identity,
  data classes, residency, retention/deletion, security, compliance, quota,
  quality, latency, and cost;
- paid activation, external or consent writes, and credential changes;
- Git-history actions, migrations/data mutation, deployment/production
  promotion/traffic or publication actions; and
- acceptance of residual security, privacy, compliance, vendor, data, cost,
  availability, recovery, or irreversible risk.

No satisfied gate may be recorded without durable founder evidence in the
decision records. This revision supplies no such evidence and approves none of
these decisions.
