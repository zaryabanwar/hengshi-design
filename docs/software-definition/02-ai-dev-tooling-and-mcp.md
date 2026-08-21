# 02 — AI Development Tooling and MCP

## Purpose

This file records tool inventory, verified capability states, and safe fallbacks.
Tool availability never bypasses the phase, approval, design, security, or Git
gates in [03-autonomous-ai-development-workflow.md](03-autonomous-ai-development-workflow.md).

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
| Context7 MCP | Configured; protocol- and React capability-tested by safe direct MCP on 2026-07-19; no authentication redirect required; active-host exposure gap remains because it is not natively listed in this Codex host | Official migration, compatibility, deprecation, and runtime guidance |
| Playwright CLI | Configured in `apps/web/playwright.config.ts`; capability status must be rechecked per implementation phase | Browser and accessibility verification |
| Playwright MCP | Configured locally; current-host exposure varies | Live browser inspection and screenshots |
| Stitch MCP | Configured locally; current-host exposure and capability must be tested before design work | Production UI references |
| Figma | Available through the active tool/plugin inventory; authentication and target-file access must be tested before external writes | Design and handoff |
| Chrome/browser tools | Host-dependent; capability-test before relying on them | Browser diagnostics |
| GitHub tooling | Configured/available depending on host; use only after Git approval | Repository and CI workflow |
| Docker + Compose | Docker executable 29.5.2 is installed; `docker --version` / Compose capability checks timed out on 2026-07-19, so operational status is not established | Reproducible local services after a later bounded capability recheck |
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
Phase 1, resolve the current stable tool, action, API, and image versions; during
the relevant upgrade wave, pin npm/Python locks, container digests, GitHub Action
commit SHAs, and cloud API versions. Preview tools may be exercised only in
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
