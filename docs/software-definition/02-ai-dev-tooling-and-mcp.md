# 02 — AI Development Tooling and MCP — v1

## Purpose

This file records tool inventory, verified capability states, and safe fallbacks.
Tool availability never bypasses the phase, approval, design, security, or Git
gates in [03-autonomous-ai-development-workflow.md](03-autonomous-ai-development-workflow.md).

D-069 applies latest mutually compatible stable selection to every project tool,
framework, library, runtime and exporter. Installed/current versions and separately
newest releases are inventory observations, not an approved coupled production
set. Resolve, test, review and reproducibly lock the complete graph where used.
This is the first product/current definition v1; preserve real technical/schema
versions and dated capability evidence. Provider selection and cost planning are
deferred under D-068; tooling availability does not reopen them.

## Status Vocabulary

Report each integration precisely:

- **Installed**: software or package is present.
- **Configured**: an inventory contains a server definition.
- **Authenticated**: required credentials or OAuth have been accepted.
- **Protocol-tested**: initialization and tool discovery succeeded.
- **Capability-tested**: a real, safe operation for the intended task succeeded.

One state does not imply the next. Do not call an integration operational until a
relevant harmless capability call passes.

## Canonical Inventory and Secret Safety

The canonical local MCP inventory is `%APPDATA%\Code\User\mcp.json`. Inspect it or
this documented inventory before claiming a server is absent. If it is configured
there but missing from the current agent tool list, report an **active-host
exposure gap** and use a documented safe direct MCP/CLI fallback only when the
task contract permits it.

Never copy, print, log, or document API keys, bearer tokens, connection strings,
cookies, private keys, or other credential values from the inventory. Authentication
uses the provider's visible official OAuth flow or configured secret references;
secrets are never requested in chat.

## Verified Inventory

| Tool / MCP | Verified state | Purpose |
|---|---|---|
| Spec Kit CLI | Installed at `C:\Users\Zaryab\.local\bin\specify.exe`; Codex integration configured | Specification workflow |
| Context7 MCP | Exposed in this Codex host and capability-tested 2026-10-05: library resolution and PostgreSQL 18/Oxlint documentation queries succeeded. The earlier July direct-MCP exposure gap is historical. Query results are source guidance, not an approved compatible graph. | Official migration, compatibility, deprecation, and runtime guidance |
| Playwright CLI | Configured in `apps/web/playwright.config.ts`; capability status must be rechecked per implementation phase | Browser and accessibility verification |
| Playwright MCP | Configured locally; current-host exposure varies | Live browser inspection and screenshots |
| Stitch MCP | **Not configured or exposed on this host, verified 2026-09-06.** No Stitch MCP entry exists in `%APPDATA%\Code\User\mcp.json` (the canonical inventory named by `AGENTS.md`, which itself does not exist on this host), `.cursor/mcp.json`, `.vscode/mcp.json`, `.mcp.json`, `~/.claude.json`, or the Claude desktop configuration. The earlier "configured locally" statement is superseded. | Not used: Figma is the provider selected for reference production |
| Figma MCP | File reads, scoped canvas creation and exports succeeded during approved B01 attempts. The [current B01 call authority](../phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md#calls-costs-and-authority) and [ledger](../phase-1-ui-reference-production/validation/mcp-call-ledger.csv) own attempts and outcomes, separately from actual provider debit. The saved D-095 identity check returned reauthentication required; the founder subsequently confirmed no MCP quota is available. Do not repeat quota/identity/reconnect checks for that known condition. | D-095: batch within actual included20-call availability, then use computer control; no repeated method/per-call prompts within approved scope, extra allowance or paid activation |
| Figma web editor / Design agent / Make | D-095 supersedes D-094's native-only/no-AI restriction within approved scope. Use included Design agent features for native canvas work and Make where suitable for functional prototypes; generated code/prototypes do not establish editable native references or reaction equivalence. The [B01 brief](../phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md) owns actual static construction, scoped reviews, dated AI-credit observations and unresolved preserve/reset evidence. AI credits are separate from MCP quota; verify actual controls/balance before use. On2026-10-17, this chat's existing browser handle rejected access because local browser use was disabled in Work settings; the saved Figma state was not revalidated. | Continue approved scope when browser control is available; inspect generated output and retain independent review/acceptance. No extra quota, paid activation, new scope, account/sharing change, destructive cleanup or implied acceptance |
| Chrome/browser tools | Host-dependent; capability-test before relying on them | Browser diagnostics |
| GitHub tooling | Configured/available depending on host; use only after Git approval | Repository and CI workflow |
| Docker + Compose (historical inventory) | July2026 recorded executable29.5.2 and timed-out capability checks; this is not current runtime evidence. The founder requires Docker-free local operation and has removed Docker images/data. Use the [native Windows operating guide](../../README.md#native-local-operation-on-windows); do not restart Docker or pull images as a fallback. | Historical tooling only; native PostgreSQL, API, web and documentation servers are the local route |
| LibreOffice | Version 26.2.4.2 installed, CLI-tested, capability-tested, and independently reviewed on 2026-07-19; a generated control DOCX and the 24-page historical consolidation converted to PDF and every target page rendered for inspection | DOCX-to-PDF rendering for visual QA, with a fresh control conversion and complete page inspection at each material document gate |
| PostgreSQL MCP | Configured locally as read-only; current-host exposure varies | Safe schema/data inspection |
| Lighthouse CI | Repository configuration present; capability status must be revalidated | Performance evidence |
| axe Playwright | Repository configuration present; capability status must be revalidated | Accessibility evidence |

## Context7 Decision Protocol

For every version-sensitive decision:

1. Resolve the official library identifier through Context7.
2. Query migration, compatibility, deprecation, and supported-runtime guidance.
3. Confirm the release in official vendor notes and the authoritative registry.
4. Record query date, current version, proposed target, coupled peer/runtime
   requirements, breaking changes, security status, test evidence, and rollback.
5. Reject community guidance that conflicts with primary documentation.
6. Re-run the query immediately before exact lock selection.

The 2026-07-19 direct Context7 test initialized MCP, listed
`resolve-library-id` and `query-docs`, resolved the official React documentation as
`/reactjs/react.dev`, and returned the official React 19 upgrade guidance, including
the React 18.3 warning bridge and React DOM/TypeScript migration notes. This proves
protocol and that bounded capability only; it does not pre-approve any package
target. If official authentication later becomes required, use the visible provider
flow.

## Reproducible Tool Selection

Do not use floating `latest` tags in production artifacts or durable CI. During
each relevant increment under D-097, resolve the current stable tool, action, API,
and image versions for its complete coupled dependency graph, including shared
and transitive dependencies. Qualify future-only families when their increment
begins. During the relevant upgrade wave, pin npm/Python locks, container digests,
GitHub Action commit SHAs, and cloud API versions. Preview tools may be exercised only in
isolated non-production compatibility jobs.

## Common Verification Commands

Commands are evidence examples, not permission to bypass task scope or gates:

```powershell
npm run test
npm run test:e2e
npm run qa:lighthouse
npm run qa:axe
```

Use the full Spec Kit path when it is not on `PATH`:

```powershell
C:\Users\Zaryab\.local\bin\specify.exe --help
```
