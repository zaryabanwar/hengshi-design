# Native prototype operating guide review — v1

Date: 2026-10-04. Reviewer: independent agent `review_candidate_inventory_v1`.
Review verdict: **REVISE**. Task state: DOING; uncommitted.
Findings: 0 Critical, 0 High, 0 Medium, **1 Low**.

## Scope and commissioned identities

The review covers the current native/top sections of the two guides below and
their bounded observed-runtime claims. Their explicitly labelled lower scaffold
sections remain historical evidence, not current startup authority. Root governance
and Phase 1 boundaries remain in force. No feature, migration, credentials, provider,
production version, production readiness or full Phase 1 acceptance is authorized.

| Exact commissioned document | SHA-256 |
|---|---|
| `README.md` | `7939DFC949B85C1E1C07D47A96C67FDACE5B89782B13E3DCF5E430AB83849ADE` |
| `apps/api/README.md` | `BA2C68D4DDC81A8CB73E7DB740DAD7F65B9AE404715CC1608DA9176D47968574` |

## Finding NATIVE-LOW-001 — ownership command omits the selected API port

Evidence: `README.md:28` filters listener inspection to `5432,5173,8000,8766`,
while `README.md:94`, `:110` and `:122` use the current API port **8001**.
Following the provided initial command therefore omits the listener whose ownership
must be checked before reusing or starting the documented API. The later prose
still requires a port check, so this is a Low instruction-completeness issue,
not evidence of an unsafe running server or an architecture change.

Required bounded correction: include `8001` in that existing filter, preserving
the other ports and the ownership/no-termination constraints. Independently verify
the revised hash and command. Do not change API ports, stop the WSL relay or
restart a correctly owned server to address this documentation finding.

## Independent observations and claim assessment

| Subject | Result and limits |
|---|---|
| Cluster versus service | `postgresql-x64-17` is stopped and points to the Program Files data directory. The current Windows token is not administrator. The separate LOCALAPPDATA walkthrough cluster has `PG_VERSION` 17; `pg_ctl status` reports running PID 18524 with loopback 5432 and `pg_isready` reports accepting connections. This supports the guide’s separation. The prior failed `Start-Service` and authenticated server-version/schema query are producer observations, not re-executed in this review. |
| Listener ownership | Observed loopback 5432/PID18524/postgres; 8001/PID13084/python; 5173/PID1688/node; 8000/PID16464/wslrelay; 8766/PID19316/python. This agrees with the producer observation and confirms why 8000 must remain untouched. Process names/listeners alone cannot identify every application; profile, source, public responses and prior owned-process evidence supplement them. |
| Local profile/configuration | Redacted in-memory comparison confirms the profile repository is this workspace, PostgreSQL driver, IPv4 loopback, port 5432 and database `hengshi`, with the same credential components/database/port as the existing API environment file. The file’s host is localhost; its required `JWT_SECRET` is present. No values, connection strings, account/profile contents or hashes of secret files are recorded. Current comparison does not independently attest the history of `.env` changes or the running process’s complete environment. The producer records process-only overrides and unchanged files. |
| Actual public reads | Independent GETs returned HTTP200 for `http://127.0.0.1:8001/health`, `/api/world`, `/api/services` and `http://127.0.0.1:5173/`. Health payload is the source’s constant `{"status":"ok"}`; `app/main.py:47–49` makes no database check. These public reads support the current positive path only, not schema currency, authorization denial or other workflows. No payload data was persisted. |
| Startup and environment behavior | `apps/api/run.ps1` only activates the virtual environment. Explicit virtual-environment Uvicorn and process-local frontend/API overrides fit the current sources. Existing `load_dotenv` calls do not pass `override=True`; `app/db/session.py:15` defaults to SQLite when configuration is absent. The guide correctly requires PostgreSQL identity/configuration checks rather than treating fallback or health as proof. No start command was re-executed. |
| Browser evidence | Inspected the nonsecret browser observation, inspection script structure and actual admin Services screenshot. The script observes response/page-error events, navigates login and waits for `/admin/services`; the screenshot displays the protected Services interface. Producer observation records login/admin-read HTTP200 and zero page errors. This corroborates a positive walkthrough path; the reviewer did not reauthenticate or replay browser/account actions. It does not establish mutation behavior, denied-role enforcement, full admin workflows or the production authorization model. |
| Known defects | Read-only source still shows `require_admin` returning current user at `apps/api/app/auth/deps.py:48–51`, conditional return before `useMemo` at `apps/web/src/world/WorldHUD.tsx:44–48`, and SQLite fallback. R-003/R-004/R-005 remain open. Guides retain these limitations and make no free-movement, streaming or production claim. |
| Timing and version limits | The 5.29s localhost/0.22s IPv4 comparison is explicitly a producer diagnostic observation, not a load benchmark or causal DNS diagnosis. PostgreSQL17.4 is a recorded prototype observation, not a selected production version. Neither latency measurement nor authenticated DB query was repeated. |
| Historical and data boundaries | Both current sections explicitly demote lower Docker/migration/seed/example-account instructions to history, gate mutations and require an approved isolated test database. No existing environment file should be overwritten; viewer presentation is distinguished from the web/API/database stack. These boundaries are coherent. |

## Supporting evidence identities

These are supporting dated observations, not independently replayed authenticated
journeys or continuing-health guarantees:

| Evidence | SHA-256 |
|---|---|
| `output/playwright/native-runtime/runtime-observation.json` | `89CFAF93C96666DB61B2F2E219278812B09205C34B403A8BAEC6787FECD48A03` |
| `output/playwright/native-runtime/inspect-native.cjs` | `54E7C73166DE56E02EE907ED9B1526D3632DA4EA4BAF59ED2F4C1AD973768F6E` |
| `output/playwright/native-runtime/admin-services.png` | `624C9EF01B182874E10D5BCF0E42DEEEA8C37BBA8FB18BEAC29629A281A3DD8C` |

The official PostgreSQL17 [pg_ctl documentation](https://www.postgresql.org/docs/17/app-pg-ctl.html)
supports `status`, data-directory selection, log redirection, startup waiting and
quoted server options. The [pg_isready documentation](https://www.postgresql.org/docs/17/app-pg-isready.html)
distinguishes connection readiness from correct authentication/database details.
Both were inspected on 2026-10-04; they do not select PostgreSQL17 for production.

Only read-only inspection, public HTTP GETs and this receipt write were performed.
No server start/stop/restart, login, database query/write, credential/role/configuration
change, package install, migration/seed, application/model edit, external operation,
commit or push occurred. The earlier inventory review was preserved unchanged.
This REVISE concerns only NATIVE-LOW-001 and does not reopen settled product scope.

## Superseding disposition — producer correction 1

Date: 2026-10-04. Current bounded review verdict: **PASS**.
NATIVE-LOW-001 is closed. Remaining findings: 0 Critical, 0 High, 0 Medium, 0 Low.
The original REVISE and commissioned identities above remain historical evidence.

| Current reviewed document | SHA-256 |
|---|---|
| `README.md` | `EB8EB95A1F3FDC595CE97FB7B973ADEAD5D61EAA2D032B212046425C2DDC4B8C` |
| `apps/api/README.md` | `BA2C68D4DDC81A8CB73E7DB740DAD7F65B9AE404715CC1608DA9176D47968574` |

Independent closure verification confirms `README.md:28` now includes 8001 while
retaining 5432, 5173, 8000 and 8766. Replacing that single corrected filter in memory
with the prior filter reconstructs the original commissioned README SHA-256
`7939DFC949B85C1E1C07D47A96C67FDACE5B89782B13E3DCF5E430AB83849ADE`.
Exactly one replacement occurrence exists, proving the correction’s byte scope;
the API guide remains unchanged. Ownership constraints, startup commands, historical
demotion and all readiness/security limitations are preserved.

The corrected read-only listener command was executed and includes the current
loopback API port 8001/PID 13084, alongside PostgreSQL port 5432/PID 18524, web
port 5173/PID 1688, WSL relay port 8000/PID 16464 and static viewer port 8766/PID
19316. No listener was altered.
This is a dated ownership-inspection observation, not continuing health proof.

This PASS covers the original bounded guide assessment at the revised identities
and this single correction. All original scope limits remain: no authenticated
journey replay, permission enforcement certification, production readiness,
version selection or full Phase 1 acceptance. Only the reviewer’s report was
appended; no producer/runtime/configuration or prior inventory report was changed.
