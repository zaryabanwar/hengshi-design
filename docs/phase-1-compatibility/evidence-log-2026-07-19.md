# Compatibility evidence log — 2026-07-19

**Evidence date:** 2026-07-19 (Asia/Karachi)
**Scope:** Read-only repository/runtime inspection, direct Context7 MCP fallback,
official primary documentation, and authoritative package registries
**Secret rule:** Credential values and local secret-input references were neither
read into evidence nor recorded

## Evidence classification

| Class | Meaning |
|---|---|
| Local observation | A file, lock, installed environment, or harmless command describes current state only. |
| Context7 capability | Context7 resolved or queried official documentation; this does not confirm a package release or approve a target. |
| Registry confirmation | npm, PyPI, Node distribution metadata, or another authoritative registry reported a release and metadata on the evidence date. |
| Official documentation | A primary project/vendor page described support, migration, release, or platform behavior. |
| Inference | A conclusion derived from two or more explicit sources; it requires a compatibility spike. |
| Unresolved | Evidence is missing, timed out, region-specific, security-specific, or awaits a human decision. |

## Local commands and outcomes

| ID | Command or inspection | Result | Classification |
|---|---|---|---|
| LOC-001 | `node --version`; `npm --version`; `python --version` | Node 24.14.0, npm 11.11.1, Python 3.14.5 | Local observation |
| LOC-002 | `apps/api/.venv/Scripts/python.exe -m pip freeze` | Installed API environment captured in the baseline inventory | Local observation |
| LOC-003 | `npm ls --depth=0 --json` in `apps/web` and repository root | Direct installed npm versions matched their lock entries | Local observation |
| LOC-004 | Node parsing of both `package-lock.json` files | Lockfile version 3; direct package versions and peer/runtime metadata captured | Local observation |
| LOC-005 | `apps/api/.venv/Scripts/python.exe -m pip check` | Exit 0; no broken installed requirements | Local observation, not reproducibility proof |
| LOC-006 | `pip show pytest-asyncio` plus import-spec check | Package absent even though `requirements.txt` declares it without a bound | Local observation |
| LOC-007 | Manifest search for Python locks, runtime pins, Dockerfiles, Bicep, Azure manifests, dependency automation, and GitHub Actions | No matching production pins, workflows, or cloud manifests found | Local observation |
| LOC-008 | Docker executable file metadata; prior bounded CLI/Compose capability check | Docker CLI file 29.5.2 is present; prior CLI/Compose check timed out, so capability remains unverified | Unresolved capability |
| LOC-009 | `npx --no-install playwright --version` | Playwright CLI 1.61.1 returned successfully | Local capability for version reporting only |
| LOC-010 | Full npm audit attempts for root and web locks | Both exceeded the 60-second bound; no vulnerability-pass claim is made | Unresolved security evidence |
| LOC-011 | `apps/web/playwright.config.ts` inspection | Only a Chromium project is configured; exact multi-browser/device/Safari evidence is absent | Local observation |
| LOC-012 | Scoped manifest/config/file search for Redis, Azure AI/Search, Microsoft Graph, OpenTelemetry/Application Insights, NVIDIA, Blender/glTF tooling, GitHub Actions, Dockerfiles/images, and Bicep/API-version artifacts | No production dependency, workflow, Dockerfile, Bicep manifest, or tool lock was found for these families. The protected exterior GLB and project-state planning references are evidence, not tooling selections. | Local observation; architecture selection deferred |

## Context7 MCP state and outcomes

| State | Evidence |
|---|---|
| Configured | The canonical VS Code MCP inventory contains a Context7 HTTPS Streamable HTTP definition. No endpoint credential material is recorded here. |
| Authenticated | Not established. The successful bounded calls used the service's anonymous path; no credential was requested or exposed. |
| Protocol-tested | `initialize` returned HTTP 200 with MCP protocol `2025-06-18`, Context7 server 3.2.3, and a session identifier. `tools/list` returned `resolve-library-id` and `query-docs`. |
| Capability-tested | Direct safe calls resolved React Three Fiber and FastAPI library IDs and queried React, React Three Fiber, and FastAPI documentation successfully. |
| Active-host exposure | Context7 is not exposed as a native tool in this Codex host, so the approved direct fallback was used. |
| Operational claim | None. The evidence proves only the two documentation operations used in this slice. |

### Context7 query record

| ID | Library ID | Query outcome | Follow-up boundary |
|---|---|---|---|
| CTX7-REACT | `/reactjs/react.dev` | Returned the official React 19 migration guide: use React 18.3 as the warning bridge; align React DOM and TypeScript types; test removed DOM APIs, `act`, JSX namespace, and ref typing changes. | Registry confirmation and repository tests remain mandatory. |
| CTX7-R3F | `/pmndrs/react-three-fiber` | Returned official installation, changelog, and v9 migration material: R3F 8 pairs with React 18; R3F 9 pairs with React 19; the queried v9 peer window includes React/DOM 19 through below 19.3 and Three at least 0.156. | Drei/Three peers, WebGL behavior, types, loading, interactions, screenshots, memory, and performance still require a spike. |
| CTX7-FASTAPI | `/fastapi/fastapi` | Returned official release/version guidance: current FastAPI uses Pydantic 2, recent releases removed Pydantic 1 support, and Python 3.14 makes the Pydantic 1 path unsuitable. | Exact FastAPI/Starlette/Pydantic/Uvicorn/HTTPX behavior requires contract and negative tests. |

## npm registry confirmation

Command form: `npm view <package> version peerDependencies engines dist-tags --json`.
The `latest` tag and a release string without a prerelease suffix were treated as
registry evidence of a stable candidate, never as lock approval.

### Canonical npm and distribution registry records

| ID | Covered evidence |
|---|---|
| REG-001 | Node 24.18.0 distribution metadata and its bundled npm 11.16.0. |
| REG-002 | npm 12.0.1 and npm 11.16.0 version, engine, and distribution-tag metadata. |
| REG-003 | React, React DOM, and React type-package version and peer metadata. |
| REG-004 | React Router and React Router DOM version, engine, and peer metadata. |
| REG-005 | Zustand and GSAP version and peer metadata. |
| REG-006 | React Three Fiber, Drei, and Three version and peer metadata. |
| REG-007 | TypeScript 7, TypeScript 6, and TypeScript 6 bridge version metadata. |
| REG-008 | Vite and Vite React plugin version, engine, and peer metadata. |
| REG-009 | TailwindCSS, PostCSS, and Autoprefixer version and peer metadata. |
| REG-010 | ESLint, typescript-eslint, React Hooks, and React Refresh plugin metadata. |
| REG-011 | Zod version metadata. |
| REG-012 | Playwright, axe Playwright adapter, and Lighthouse CI version and peer metadata. |

| Package | Current | Registry-observed stable | Coupling result |
|---|---:|---:|---|
| Node.js distribution | 24.14.0 | 24.18.0 LTS | Official distribution metadata reports bundled npm 11.16.0. |
| npm | 11.11.1 | 12.0.1 primary; 11.16.0 bundled fallback | Node 24.18.0 satisfies npm 12's Node 24.15+ engine floor, so 12.0.1 is the latest-compatible path to spike first. Bundled npm 11.16.0 is only an exception path if frozen-install, lock, lifecycle-script, or clean-relock evidence blocks 12.0.1. |
| `react` / `react-dom` | 18.3.1 / 18.3.1 | 19.2.7 / 19.2.7 | React DOM requires React 19.2.7. |
| `react-router-dom` / `react-router` | 6.30.3 / absent | 7.18.1 / 8.2.0 | v8 uses `react-router`, requires React/DOM 19.2.7+ and Node 22.22+; package/import migration is required. |
| `@types/react` / `@types/react-dom` | 18.3.27 / 18.3.7 | 19.2.17 / 19.2.3 | DOM types require React types 19.2.x. |
| `@react-three/fiber` | 8.18.0 | 9.6.1 | Requires React/DOM 19 below 19.3 and Three at least 0.156. |
| `@react-three/drei` | 9.122.0 | 10.7.7 | Requires React/DOM 19, R3F 9, and Three at least 0.159. |
| `three` | 0.160.1 | 0.185.1 | Peer floor fits R3F/Drei; API/visual migration is unproven. |
| `zustand` | 4.5.7 | 5.0.14 | React peer range includes React 19; API migration remains. |
| `gsap` | 3.14.2 | 3.15.0 | Registry candidate only. |
| `typescript` | 5.9.3 | 7.0.2 compiler plus `@typescript/typescript6` 6.0.2 API/tooling bridge; 6.0.3-only conditional alternative | TypeScript 7 has no programmatic API, but Microsoft documents the bridge plus npm aliases for side-by-side compiler/tooling use. typescript-eslint 8.64.0 supports TypeScript below 6.1, so both paths need a repository spike. |
| `vite` / `@vitejs/plugin-react` | 5.4.21 / 4.7.0 | 8.1.5 / 6.0.3 | Both require Node 20.19+ or 22.12+ and the plugin requires Vite 8. |
| `tailwindcss` | 3.4.19 | 4.3.3 | v4 changes the PostCSS/Vite integration and supports the approved Safari 16.4 floor. |
| `postcss` / `autoprefixer` | 8.5.6 / 10.4.23 | 8.5.19 / 10.5.4 | Tailwind v4 may remove explicit Autoprefixer depending on the selected integration. |
| `eslint` | 8.57.1 | 10.7.0 | Requires modern Node and flat configuration; current configuration inventory needs a migration review. |
| `@typescript-eslint/parser` / plugin | 6.21.0 / 6.21.0 | 8.64.0 / 8.64.0 | Supports ESLint 8.57, 9, or 10 but TypeScript only below 6.1. |
| `eslint-plugin-react-hooks` | 4.6.2 | 7.1.1 | Supports ESLint through 10. |
| `eslint-plugin-react-refresh` | 0.4.26 | 0.5.3 | Requires ESLint 9 or 10. |
| `zod` | declared 3.25.8 range; no project lock | 4.4.3 | Shared-package installation/consumer topology is not locked or proven. |
| `@playwright/test` | 1.61.1 | 1.61.1 | Current equals registry candidate; browser binaries still need deterministic CI installation. |
| `@axe-core/playwright` | 4.12.1 | 4.12.1 | Current equals registry candidate and peers on Playwright Core. |
| `@lhci/cli` | 0.15.1 | 0.15.1 | Current equals registry candidate; the existing Lighthouse execution history includes a timeout, not a pass. |

Registry endpoints used include
[npm package metadata](https://registry.npmjs.org/react/latest),
[R3F metadata](https://registry.npmjs.org/@react-three%2ffiber/latest),
[Drei metadata](https://registry.npmjs.org/@react-three%2fdrei/latest),
[Vite metadata](https://registry.npmjs.org/vite/latest), and
[typescript-eslint metadata](https://registry.npmjs.org/@typescript-eslint%2fparser/latest), and
[TypeScript 6 bridge metadata](https://registry.npmjs.org/@typescript%2ftypescript6/latest).
The full package list and exact results are represented in the graph.

## PyPI registry confirmation

PyPI JSON metadata was queried directly on 2026-07-19. Requirements shown here
are package metadata, not proof of this application's behavior.

### Canonical PyPI registry records

| ID | Covered evidence |
|---|---|
| REG-PYPI-STACK | Python runtime, pip, FastAPI, Starlette, Pydantic, Uvicorn, SQLAlchemy, Alembic, Psycopg, bcrypt, PyJWT, HTTPX, email-validator, python-dotenv, and pytest release metadata summarized below. |
| REG-PYPI-PYTEST-ASYNCIO | pytest-asyncio 1.4.0 release and pytest compatibility metadata. |

| Package | Current | Registry-observed stable | Relevant metadata |
|---|---:|---:|---|
| Python | 3.14.5 | 3.14.6 | Python 3.14.6 is the latest stable 3.14 maintenance release. |
| pip | 26.1.1 | 26.1.2 | Tooling patch candidate only. |
| FastAPI | 0.138.0 | 0.139.2 | Python 3.10+, Starlette 0.46+, Pydantic 2.9+. |
| Starlette | 1.3.1 | 1.3.1 | Python 3.10+, AnyIO 3.6.2 through below 5; official Python 3.14 support was added earlier. |
| Pydantic | 2.13.4 | 2.13.4 | Python 3.9+, exact Pydantic Core 2.46.4. |
| Uvicorn | 0.49.0 | 0.51.0 | Python 3.10+. |
| SQLAlchemy | 2.0.51 | 2.0.51 | Psycopg extra supports Psycopg 3.0.7+; Python 3.14 fixes are present in the 2.0 line. |
| Alembic | 1.18.4 | 1.18.5 | Python 3.10+; works with SQLAlchemy 1.4+; PostgreSQL migration rehearsal remains required. |
| Psycopg / binary | 3.3.4 / 3.3.4 | 3.3.4 / 3.3.4 | Python 3.10+; binary package must stay exactly aligned with Psycopg. |
| bcrypt | 5.0.0 | 5.0.0 | Python 3.8+. |
| PyJWT | 2.13.0 | 2.13.0 | Python 3.9+. |
| HTTPX | 0.28.1 | 0.28.1 | Python 3.8+; FastAPI standard metadata keeps HTTPX below 1. |
| pytest | 9.1.1 | 9.1.1 | Python 3.10+. |
| pytest-asyncio | absent | 1.4.0 | Requires pytest 8.4 through below 10; compatible at metadata level with pytest 9.1.1. |

Registry endpoints include
[FastAPI JSON](https://pypi.org/pypi/fastapi/json),
[Starlette JSON](https://pypi.org/pypi/starlette/json),
[Pydantic JSON](https://pypi.org/pypi/pydantic/json),
[SQLAlchemy JSON](https://pypi.org/pypi/SQLAlchemy/json),
[Alembic JSON](https://pypi.org/pypi/alembic/json),
[Psycopg JSON](https://pypi.org/pypi/psycopg/json), and
[pytest-asyncio JSON](https://pypi.org/pypi/pytest-asyncio/json).

## Official primary documentation

| ID | Source | Dated conclusion |
|---|---|---|
| OFF-NODE | [Node release schedule](https://nodejs.org/en/about/previous-releases) and [distribution index](https://nodejs.org/dist/index.json) | Node 24 is LTS; 24.18.0 was the newest 24.x distribution row on 2026-07-19. |
| OFF-PYTHON | [Python 3.14.6 release](https://www.python.org/downloads/release/python-3146/) and [3.14 porting notes](https://docs.python.org/3.14/whatsnew/3.14.html) | 3.14.6 is stable; a runtime patch still requires application, extension, memory, and process-model tests. |
| OFF-REACT | [React 19 upgrade guide](https://react.dev/blog/2024/04/25/react-19-upgrade-guide) | React 18.3 is the warning bridge; React DOM APIs, error reporting, JSX transform, tests, refs, and TypeScript types have migration obligations. |
| OFF-R3F | [R3F installation](https://r3f.docs.pmnd.rs/getting-started/installation) and [v9 migration](https://r3f.docs.pmnd.rs/tutorials/v9-migration-guide) | R3F major must match the React major; v9 is the React 19 line. |
| OFF-ROUTER | [React Router upgrade guidance](https://reactrouter.com/upgrading/v7), [v7 DOM bridge](https://api.reactrouter.com/v7/modules/react-router-dom.html), and [current home](https://reactrouter.com/) | v8 raises runtime/framework baselines and the DOM package is a migration bridge, so package/import topology must be tested. |
| OFF-VITE | [Vite 8 announcement](https://vite.dev/blog/announcing-vite8) and [migration guide](https://vite.dev/guide/migration.html) | Vite 8 uses Rolldown and requires a staged build/performance/browser migration. |
| OFF-TS | [TypeScript 6.0 release](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/), [6.0 notes](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-6-0.html), and [7.0 release](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) | TypeScript 7 is stable and has no programmatic API. The official 7.0 release documents a stable `@typescript/typescript6` compatibility package and npm-alias topology so the TypeScript 7 compiler can run beside TypeScript 6 API-dependent tools. |
| OFF-TSESLINT | [typescript-eslint dependency versions](https://typescript-eslint.io/users/dependency-versions/) | Current support is ESLint 8.57/9/10 and TypeScript below 6.1. |
| OFF-TAILWIND | [Tailwind v4 upgrade guide](https://tailwindcss.com/docs/upgrade-guide) | v4 changes CSS/build integration, requires Node 20+ for its upgrade tool, and supports Safari 16.4+. |
| OFF-ESLINT | [ESLint 10 migration](https://eslint.org/docs/latest/use/migrate-to-10.0.0) | v10 drops legacy config and older Node releases and can change rule results. |
| OFF-FASTAPI | [FastAPI release notes](https://fastapi.tiangolo.com/release-notes/) and [version pinning guidance](https://fastapi.tiangolo.com/deployment/versions/) | FastAPI and Pydantic major bounds must be explicit; release notes require migration review. |
| OFF-STARLETTE | [Starlette release notes](https://starlette.dev/release-notes/) | Starlette 1.3.1 is stable and contains parser-limit fixes; the 1.0 line removed earlier deprecated behavior. |
| OFF-PYDANTIC | [Pydantic changelog](https://docs.pydantic.dev/latest/changelog/) | Pydantic and Pydantic Core must remain exactly aligned. |
| OFF-SQLALCHEMY | [SQLAlchemy 2.0 changelog](https://docs.sqlalchemy.org/en/20/changelog/changelog_20.html) | 2.0.51 is current; Python 3.14 and PostgreSQL/Psycopg fixes are present in recent patches. |
| OFF-ALEMBIC | [Alembic changelog](https://alembic.sqlalchemy.org/en/latest/changelog.html) | 1.18.5 is stable; SQL generation and autogenerate still require PostgreSQL rehearsal and downgrade/restore proof. |
| OFF-PSYCOPG | [Psycopg news](https://www.psycopg.org/psycopg3/docs/news.html) | 3.3.4 is stable; binary and Python package versions must align. |
| OFF-POSTGRES | [PostgreSQL version policy](https://www.postgresql.org/support/versioning/) | PostgreSQL 18.4 is the current supported 18 minor; current minor releases are recommended. |
| OFF-AZURE-PG | [Azure supported versions](https://learn.microsoft.com/en-us/azure/postgresql/configure-maintain/concepts-supported-versions) and [Azure PostgreSQL release notes](https://learn.microsoft.com/en-us/azure/postgresql/release-notes/release-notes) | Azure documents PostgreSQL 18 and minor 18.4 generally, but this does not prove the founder-approved region, feature set, quota, or cost. |
| OFF-PLAYWRIGHT | [Playwright release notes](https://playwright.dev/docs/release-notes) | 1.61 is the current stable line observed; deterministic browser-binary installation and Chromium/WebKit/Firefox coverage remain separate. |
| OFF-DOCKER | [Compose Specification](https://docs.docker.com/reference/compose-file/) and [Docker version semantics](https://docs.docker.com/reference/cli/docker/version/) | A present CLI does not establish engine capability; immutable image digests and a successful client/server check are still required. |

## Explicit inferences

1. React 19.2.7, React DOM 19.2.7, R3F 9.6.1, Drei 10.7.7, and Three
   0.185.1 satisfy published peer ranges. This is metadata compatibility only.
2. Node 24.18.0 satisfies the published runtime floors for Vite 8, its React
   plugin, ESLint 10, React Router 8, and Playwright. Editor/CI/container parity
   is not established.
3. TypeScript 7.0.2 remains a production candidate only through Microsoft's
   documented side-by-side topology: the TypeScript 7 compiler plus stable
   `@typescript/typescript6` API/tooling bridge and npm alias. TypeScript 6.0.3-only
   remains a conditional exception alternative. Neither is an automatic lock;
   both need diagnostic, editor, build, and lint parity evidence, and the
   TypeScript 6-only path additionally needs an exception ADR and quarterly
   recheck.
4. The installed FastAPI/Starlette/Pydantic/SQLAlchemy/Psycopg environment is
   internally installable because `pip check` passes. Unbounded requirements and
   absence of a lock mean it is not reproducible.
5. PostgreSQL 18.4 is a conditional service candidate, not a selected database,
   until region, extensions, HA, backup/restore, migration, capacity, and cost
   evidence pass.

## Unresolved evidence

- npm vulnerability evidence timed out and is not a pass; Python advisory,
  SBOM, and license evidence were not available in this bounded slice.
- Docker/Compose execution timed out; engine, API negotiation, Compose parsing,
  image resolution, and health behavior are unverified.
- The approved Azure region/subscription and cost envelope are absent, so no
  region-specific GA or capacity claim is made.
- Exact evergreen browser versions, Playwright browser revisions, Safari/iOS
  device coverage, and 3D device-tier thresholds require the QA/3D slices.
- No compatibility spike, migration, build, browser, visual, performance,
  database, restore, or rollback execution was authorized here.
