# Feature Specifications — v1

This directory contains feature-level specifications following the **Spec-Driven
Development (SDD)** cycle.

Read the [current architecture entry](../docs/phase-1-architecture/README.md)
for accepted boundaries and decision amendments. Detailed shared contracts stay
in their owning packages; this index is not another architecture or review ledger.

## Naming Convention

```
specs/
├── NNN-feature-slug/
│   ├── spec.md              # What to build and why
│   ├── research.md          # Background research and findings
│   ├── data-model.md        # Database/data structure changes
│   ├── plan.md              # Technical implementation plan
│   ├── tasks.md             # Ordered, actionable task list
│   └── checklists/
│       └── requirements.md  # Trackable requirements checklist
```

- `NNN` is a zero-padded sequential number (001, 002, ...).
- `feature-slug` is a kebab-case short name for the feature.

## SDD Workflow

```
specify → clarify → plan → tasks → implement
    ↓         ↓        ↓
  review    review   review
```

D-097 governs incremental delivery. Define the assigned feature's scope, design,
contracts, plan and tests before implementing it; unfinished future 3D does not
block unrelated 2D features. Historical reviewed specs below remain useful inputs,
not automatically executable plans. Reuse them without reopening settled choices.
Correction counters are not stop gates; apply the current constitution.

## Current Feature Specs

| # | Feature | Task status | Actual artifacts and authority |
|---|---------|-------------|--------------------------------|
| 001 | [Staff security and privacy enforcement](001-platform-security-hardening/spec.md) | DOING | Proposed v1 spec and [producer checklist](001-platform-security-hardening/checklists/requirements.md) have [bounded independent security/privacy/identity/architecture review PASS](001-platform-security-hardening/reviews/security-feature-v1-2026-10-04.md) at the report's two exact hashes. Prior spec/checklist bytes remain in `history/`; June research/data/plan and task readiness are historical/nonexecutable. Exact methods, grants, thresholds, legal/provider mappings, applicable legal/accessibility review and founder acceptance remain held; no implementation plan or runtime proof. |
| 002 | [Behavior evidence, monitoring and recovery](002-testing-and-monitoring/spec.md) | DOING | Proposed v1 spec and [producer checklist](002-testing-and-monitoring/checklists/requirements.md) retain the [historical PASS/REVISE](002-testing-and-monitoring/reviews/qa-feature-v1-2026-10-04.md). [D-074](../DECISIONS.md#d-074--one-word-qa-browser-release-correction-exception) approved the one-word repair, applied at spec SHA-256 3afdbd73217090da8980ecddad69ce1c447879f1ee00f90f1db47ee2ebb3548e with all other bytes/checklist preserved. [Independent corrected-input PASS](002-testing-and-monitoring/reviews/qa-browser-release-correction-v1-2026-10-06.md) resolves QA-V1-01 only at those identities. Exact measurement/SLI/device/retention/provider inputs and feature/integrated/founder acceptance remain; no plan, executable tasks or runtime test evidence. Later [reference reconciliation PASS](../output/research/qa-feature-reference-reconciliation-2026-10-12/independent-review-references-v1.json) covers review labels and measurement-owner links only; D-097 supersedes the exhausted numeric correction boundary; the old receipt retains its exact scope. |
| 003 | [Visitor-entered World and connected nature campus](003-3d-experience-completion/spec.md) | DOING | Proposed v1 spec and [producer checklist](003-3d-experience-completion/checklists/requirements.md) have [bounded independent review PASS](003-3d-experience-completion/reviews/world-feature-v1-2026-10-04.md) at the corrected hashes; WF-01 is closed by producer revision 2. Final controls/geometry/appearance, measured budgets, rights and founder acceptance remain; no plan or executable tasks. Later [shared-contract binding PASS](../output/research/world-feature-binding-2026-10-12/independent-review-bindings-v1.json) covers the binding table/checklist only, without adopting schemas or accepting controls/geometry. |
| 004 | [Governed service content and semantic SEO](004-design-services-content/spec.md) | DOING | Proposed v1 spec and [producer checklist](004-design-services-content/checklists/requirements.md) have [bounded independent review PASS](004-design-services-content/reviews/content-feature-v1-2026-10-04.md) at its two exact hashes, including initial-HTML, visible-fact/metadata and crawler-purpose coverage. Verified copy, owners/reviewers, rights, legal/exact contracts and founder acceptance remain; no plan, executable tasks or public publication. Later [content binding PASS](../output/research/content-feature-binding-2026-10-12/independent-review-bindings-v1.json) covers contract references and the separation of Phase 1 holds from D-076 deferred production facts only; fictional data remains quarantined. |
| 005 | [Deferred Deployment and Launch](005-azure-deployment-launch/README.md) | TODO | D-068 defers provider/region/cost planning. Azure and AWS remain candidates; existing folder names are historical and select neither. Exact spec/plan/tasks and evidence await later planning. |

The current `.specify/feature.json` points to 001 for the drafted security definition;
this selects a tooling context, not planning or implementation approval. Feature
002/003/004's proposed QA/World/content specs and checklists remain intact alongside
feature 001's preserved historical snapshots and nonexecutable planning inputs.
Their respective held inputs and authority remain explicit. Folder creation,
drafted specs and producer checklists do not constitute independent review or
founder acceptance. The [compatibility package](../docs/phase-1-compatibility/README.md)
owns dependency trials, inventories, reviews and the separately unfinished full
stable graph. They do not select or install the production stack. Do not
reopen supplied company facts, deferred cloud planning or undecided alias ownership.

The later [D-076 correction-1 review](../docs/software-definition/reviews/feature-d076-reconciliation-v1-2026-10-07.md) gives bounded consistency PASS for the security/content amendments at twenty frozen inputs. It resolves staff-only absolute-session scope and later contract-review labels; earlier feature/checklist receipts retain their exact inputs. Concrete mechanisms, legal/operational bindings and feature/integrated acceptance remain held.

## Relationship to product documentation

Use [the reconciliation map](../docs/software-definition/04-reconciliation-map.md)
to find canonical product requirements, UX, identity, architecture and contracts.
Each feature adds its bounded behavior, evidence, data/contracts and delivery plan;
it references shared requirements rather than maintaining a competing SRS/SAD.
Historical fixed-version, AWS and incomplete security assumptions cannot override
DECISIONS.md or the constitution. Keep the protected prototype and approved
artifact provenance intact while reconciling.

D-069 requires the latest mutually compatible stable graph for all coupled tools,
frameworks and libraries. Independently newest observations are not selections.
Use v1 for the current product and definition; retain factual technical/schema
versions and historical evidence identifiers. D-068 retains Outlook/Teams intent
without a Microsoft 365 prerequisite and does not replace approved staff identity
or AI privacy routes. D-070 records Europe-first targeting and editable company
facts with approved but operationally unverified dedicated contact aliases.

## Templates

Templates for all spec artifacts are in `.specify/templates/`.

## How to Start a New Feature

New feature scope follows the constitution, D-097 and the founder's bounded
work-chat prompt. Use the existing Spec Kit artifacts/templates for the relevant
increment; prepare its executable plan/tasks after its scope is approved. There
is no complete-platform definition prerequisite. Existing .specify/feature.json
is only tooling context, not permission to start an adjacent feature.

The [complete predecessor index](../output/research/feature-index-consolidation-2026-10-11/README.before.md)
remains historical evidence, with its original links resolved from this directory.
Feature bodies, checklists, historical plans/tasks and their review receipts are
unchanged; bounded review results do not transfer to later source edits.
