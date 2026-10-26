# Software Definition — Hengshi Design v1

Start with the [visual walkthrough](definition-walkthrough.html) to understand the
intended product. Use the [reconciliation map](04-reconciliation-map.md) to find
each controlling definition, its review evidence and remaining obligations.
The complete Phase 1 package is still DOING; these navigation pages grant no approval.

## Documents

| Entry | Purpose |
|---|---|
| [System boundaries](01-system-boundaries.md) | Approved target and protected prototype boundaries. |
| [Development tools and MCP](02-ai-dev-tooling-and-mcp.md) | Tool inventory, verified access states and safe fallbacks. |
| [Development workflow](03-autonomous-ai-development-workflow.md) | Phase, review and approval rules. |
| [Reconciliation map](04-reconciliation-map.md) | Canonical subjects, historical successors and all fourteen Phase 1 deliverables. |
| [Consolidated scope](05-consolidated-goal.md) | Scope pursued by the active app goal; this file is no separate scheduler. |
| [Entity and public contact](06-entity-and-public-contact.md) | Private editable company facts, eligible public content and contact channels. |
| [Visual walkthrough](definition-walkthrough.html) | The website, World, campus, departments, consultation and engineering explanations. |

## Review and operating entry points

Keep detailed requirements and review histories in their controlling packages.
The following six groups organize the fourteen deliverables without reducing them.

| Document group | Deliverables | Controlling entry |
|---|---|---|
| Product and content | 1 requirements, 2 evidence, 3 SEO | [Accepted foundation](../phase-1-foundation/README.md), [entity/contact amendment](06-entity-and-public-contact.md). |
| Brand | 4 strategy and identity | [Strategy](../phase-1-brand-strategy/03-BRAND_STRATEGY.md), [identity](../phase-1-brand-identity/BRAND_IDENTITY.md). D-026/D-035 are accepted; dated package labels do not reopen them. |
| Visitor experience | 5 UX, 6 production UI references, 7 production 3D definition | [UX](../phase-1-ux-architecture/README.md), [UI production](../phase-1-ui-reference-production/README.md), [B01 brief](../phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md), [World](../phase-1-3d/WORLD_EXPERIENCE.md), [campus build specification](../phase-1-3d/CAMPUS_ASSET_BUILD_SPEC.md). |
| System design | 8 architecture, 9 interfaces/data/publication, 10 security/privacy/AI | [Current architecture entry](../phase-1-architecture/README.md) reconciles accepted boundaries and decision amendments while preserving the frozen baseline; [contract catalogue](../phase-1-architecture/contracts/INTERFACE_CATALOG.md), [publication](../phase-1-architecture/contracts/PUBLICATION_CONTRACT.md), [data](../phase-1-architecture/contracts/DATA_CONTRACT.md), [security/privacy](../phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md) retain detailed authority. |
| Assurance and operation | 11 QA/recovery, 12 compatibility, 13 costed operating envelope | [QA/recovery](../phase-1-architecture/contracts/QA_RECOVERY.md), [compatibility](../phase-1-compatibility/README.md#current-authority-and-dated-evidence). D-068 defers provider, region and cost planning. |
| Feature and historical reconciliation | 14 legacy/feature reconciliation | [Feature index](../../specs/README.md), [historical successor catalogue](../active/Documentation_Index.md#current-successors-for-historical-documents). |

The [coverage table](04-reconciliation-map.md#coverage-against-the-fourteen-phase-1-deliverables)
records what each deliverable still needs. The [subject map](04-reconciliation-map.md#one-controlling-source-per-subject)
and [later contract refinements](04-reconciliation-map.md#later-contract-refinements)
direct readers to the controlling documents and their scoped review receipts. The
map preserves its exact earlier evidence history as supporting material, without
maintaining another live review journal. A receipt applies to its frozen inputs
and scope; later edits do not replace its hashes or inherit its PASS. Definition,
schema and supplied-image reviews do not establish application enforcement,
whole-page accessibility, physical-phone behavior or release readiness.

## Durable Authority Bridge

Read root `AGENTS.md`, the constitution, `PROJECT.md`, `DECISIONS.md` and
`PROJECT_STATE.yaml` before changing the repository. Apply the constitution's
complete authority order: current founder direction and governance, approved
decisions, requirements, software/design artifacts, implementation evidence,
then unreconciled or historical material. Proposed contracts remain proposals.
Feature artifacts refine shared definitions by reference; they do not create
another SRS or architecture authority.

Current decisions retain the semantic website and four equivalent delivery
streams, explicit World entry, mouse/touch free movement, nearby streaming and
visitor-enabled sound. D-065 accepts architecture boundaries; D-071 accepts the
campus composition only. Production controls, appearance, complete contracts,
compatible graph, required reviews and integrated acceptance remain unfinished.

D-076 settles visitor conversation access at 30 minutes of inactivity or
authorized End, with no absolute visitor limit; staff sign-in clocks remain
separate. Public registration, validity and supplied address disclosures are
deferred. Use synthetic non-sensitive data locally; the founder manages real
content through admin before production. Dedicated privacy/security aliases are
accepted, with ownership deliberately undecided. EU privacy recommendations need
exact bindings, adoption and legal clearance; no compliance claim follows.

Use v1 for this first product and definition. Select the latest mutually compatible
stable graph; retain accurate dependency/schema and historical identifiers.
D-072/D-077 are bounded, dated exceptions, not full graph acceptance. Azure and AWS
remain candidates under D-068. Outlook/Teams intent needs no Microsoft 365
prerequisite; actual account/API capabilities and existing Entra/AI privacy
constraints remain separate obligations.

## Related Documentation

[TASKS.md](../../TASKS.md) controls the active outcome;
[MANUAL_ACTIONS.md](../../MANUAL_ACTIONS.md) records founder/external gates and
[RISKS.md](../../RISKS.md) records risks. The [native operating guide](../../README.md#native-local-operation-on-windows)
explains Docker-free prototype operation; dated positive-path observations do
not prove continuing health or production permission enforcement.

Historical SRS/SAD, API reference, backlog, security plan and deployment records
remain evidence with successors named in the [historical catalogue](../active/Documentation_Index.md#current-successors-for-historical-documents).
The `active` folder name and old readiness scores do not grant production authority.
The complete [pre-consolidation entry](../../output/research/definition-entry-consolidation-2026-10-08/README.before.md)
is preserved as evidence, with its original links interpreted from this directory.
Earlier reviewed snapshots remain unchanged. Preserve the existing application,
Atlanta GLB and accepted campus study.

## How This Directory Works

Update the controlling subject once, then reconcile navigation and feature
references. Keep historical receipts as evidence rather than maintaining competing
status narratives. Application development begins only after complete Phase 1
founder acceptance and applicable approved feature artifacts. External design
writes, commits, pushes and deployment keep their separate approval gates.
