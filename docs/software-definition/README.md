# Software Definition — Hengshi Design

This directory defines approved product boundaries, AI tooling, and delivery
workflow for the Hengshi Design platform. It is part of a wider durable authority
system, not an isolated source of truth.

## Documents

| # | Document | Purpose |
|---|---|---|
| 01 | [System Boundaries](01-system-boundaries.md) | Protected prototype, approved target, and surface separation |
| 02 | [AI Dev Tooling and MCP](02-ai-dev-tooling-and-mcp.md) | Tool inventory, verified states, and safe fallbacks |
| 03 | [Autonomous AI Development Workflow](03-autonomous-ai-development-workflow.md) | Phase states, approval gates, tool order, and evidence rules |

## Durable Authority Bridge

Read and apply these sources in order:

1. `AGENTS.md` and `.specify/memory/constitution.md` for operating and governance
   rules.
2. `PROJECT.md`, `DECISIONS.md`, and `PROJECT_STATE.yaml` for approved product
   intent, decisions, and current phase.
3. This directory for approved product-level definitions.
4. Approved feature artifacts under `specs/` for feature-level requirements,
   research, data models, contracts, plans, and tasks.
5. Source code, tests, and live observations as evidence of current behavior.

Approved decisions outrank approved requirements. The constitution contains the
complete conflict-resolution order.

## Related Documentation

| Document | Authority in the current reset |
|---|---|
| `docs/PROJECT_RULES.md` | Binding project rules |
| `TASKS.md`, `RISKS.md`, `MANUAL_ACTIONS.md`, `CHANGELOG.md` | Durable execution records |
| `docs/decisions-log.md` | Detailed decisions and ADR evidence |
| `docs/active/Hengshi_Design_SRS_v3.md` | Prototype/historical evidence pending Phase 1 reconciliation |
| `docs/active/Hengshi_Design_SAD_v3.md` | Prototype/historical evidence pending Phase 1 reconciliation |
| `docs/active/Security_Hardening_Plan.md` | Draft evidence pending approved security definition |
| `docs/active/API_Reference.md` | Current implementation evidence; verify against live OpenAPI |
| `docs/SPEC.md` and `docs/BACKLOG.md` | Legacy prototype scope/task evidence pending reconciliation |

The February 2026 consolidation and “active” documents MUST NOT override the
founder-approved master plan, constitution 2.0.0, or approved durable decisions.
They remain preserved so Phase 1 can supersede individual claims transparently
instead of deleting history.

## How This Directory Works

1. Agents read this README after the root governance and state records.
2. Product definitions are revised and reviewed through the material phase loop.
3. Feature-level specifications refine, but cannot silently contradict, approved
   product decisions.
4. Exact dependency versions remain in the dated compatibility matrix and
   lockfiles, not in timeless product rules.
5. Application development remains closed until the complete Phase 1 package is
   founder-approved.
