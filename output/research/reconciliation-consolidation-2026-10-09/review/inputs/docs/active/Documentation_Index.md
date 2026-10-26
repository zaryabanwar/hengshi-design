# Hengshi Design Digital Platform — Documentation Index

**Document ID:** HD-INDEX-2026-002
**Current definition:** v1
**Original version date:** February 9, 2026
**Last reconciled:** October 4, 2026
**Status:** Active | Classification: Internal

---

## Purpose

This file is a catalog of project documentation, status, location, and relationship
to the current implementation. It is not itself an authority source; the durable
authority bridge below controls.

The platform underwent a strategic architectural pivot in early 2026 from an 11-service microservices design (Angular/Django/MongoDB) to a focused React/FastAPI/PostgreSQL monorepo. A second, non-destructive definition reset was founder-approved on July 18, 2026. The authority bridge below controls while the replacement definition package is produced.

---

## 0. Current Authority Bridge

| Priority | Record | Authority |
|---:|---|---|
| 1 | Current explicit founder approval recorded in root `DECISIONS.md` and detailed `docs/decisions-log.md` | Current founder direction. |
| 2 | Current v1 constitution, `AGENTS.md`, and project safety/governance rules | Binding governance and safety. |
| 3 | Approved decisions and compatibility-exception ADRs | Durable product/technical choices and approved exceptions. |
| 4 | Approved requirements and feature specifications | Controlling approved product behavior. |
| 5 | Approved software-definition and design artifacts | Approved implementation/design intent. |
| 6 | Source, tests, generated artifacts, and live observations | Current implementation evidence; does not create product approval. |
| 7 | Active-but-unreconciled documents, consolidation files, research, drafts, and chat | Supporting evidence only. |

Approved decisions outrank approved requirements; approved requirements outrank research and drafts. Chat history is supporting context only.

The current first-production definition is v1. D-069 requires the latest mutually
compatible stable graph across all retained technology families and coupled tools;
independently newest versions are observations, not selections. D-068 defers
deployment/provider/region/cost planning, with Azure and AWS as candidates and the
lowest feasible cost/free services preferred when planning resumes. Outlook/Teams
remain intended without a Microsoft 365 prerequisite; approved Entra staff identity
and AI privacy routes remain separate restrictions. D-070 targets Europe first,
with reviewed admin-editable company facts and dedicated privacy/security aliases
whose ownership is explicitly undecided. No provider or operational mailbox is
verified by this index. Historical fixed versions and either historical cloud plan
cannot override these decisions.

Phase 0 was accepted through D-024. Phase 1 is DOING: D-025 accepts the foundation, D-035 the identity, D-036 the UX baseline, D-037 the reference-design contract and D-061/D-063 their recorded refinements. D-065 accepts the reviewed architecture boundaries; D-064 adds mouse/touch free movement and spatial streaming, D-066 selects an original modular headquarters, and D-067 selects a nature-integrated visual direction. Detailed visual acceptance and complete Phase 1 acceptance remain pending.

Start from the [system definition and reconciliation map](../software-definition/04-reconciliation-map.md) and [consolidated work scope](../software-definition/05-consolidated-goal.md). They navigate to controlling sources; they do not replace approval records. Current work is recorded in [PROJECT_STATE.yaml](../../PROJECT_STATE.yaml). The `active` folder name and historical titles do not give prototype documents production authority. The later inventory and cleanup recommendations remain historical evidence. Historical document IDs, dependency/schema versions and original evidence names remain accurate; they are not later product releases.

### Current successors for historical documents

These documents are retained for provenance and source comparison, without a
second maintained production specification. New requirements, plans and acceptance
evidence belong in their controlling successors. Recorded later approved SRS/style
guide amendments retain their specific decision authority; their surrounding
February implementation descriptions do not inherit that approval.

| Historical source | Current controlling successor | Use of retained source |
|---|---|---|
| [SRS](Hengshi_Design_SRS_v3.md) and [prototype MVP spec](../SPEC.md) | [Accepted foundation](../phase-1-foundation/01-product-requirements.md), approved amendments in [DECISIONS.md](../../DECISIONS.md), [UX flows](../phase-1-ux-architecture/FLOWS.md) and [World proposal](../phase-1-3d/WORLD_EXPERIENCE.md) | Historical behavior/status descriptions; later accepted requirements remain scoped to their decisions. No new competing SRS. |
| [SAD](Hengshi_Design_SAD_v3.md), [requirements-to-architecture mapping](Requirements_Architecture_Mapping_v3.md) and `docs/current-state/` diagrams | [Accepted boundary baseline](../phase-1-architecture/ARCHITECTURE.md), [movement addendum](../phase-1-architecture/MOVEMENT_STREAMING_ADDENDUM.md) and [logical data contract](../phase-1-architecture/contracts/DATA_CONTRACT.md) | Prototype architecture observations requiring live verification; old verification ticks and diagrams do not prove current behavior. |
| [Security hardening plan](Security_Hardening_Plan.md) | [Security/privacy proposal](../phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md), [recorded risks](../../RISKS.md) and [security feature readiness](../../specs/001-platform-security-hardening/tasks.md) | Historical remediation suggestions, not authority for thresholds, auth changes or an executable sprint. |
| [API reference](API_Reference.md) | Actual source/live OpenAPI for prototype behavior; [interface proposal](../phase-1-architecture/contracts/INTERFACE_CATALOG.md) and [publication contract](../phase-1-architecture/contracts/PUBLICATION_CONTRACT.md) for the proposed replacement | Verify existing routes against code; the new catalogue is not yet a wire-format freeze or replacement API. |
| [Prototype backlog](../BACKLOG.md) | [Current tasks](../../TASKS.md), [checkpoint](../../PROJECT_STATE.yaml) and [feature specifications](../../specs/README.md) | Historical task/readiness claims, not current completion or permission to implement. |
| February DOCX consolidation and historical deployment diagrams | [Project charter](../../PROJECT.md), [reconciliation map](../software-definition/04-reconciliation-map.md) and [deferred deployment entry](../../specs/005-azure-deployment-launch/README.md) | Preserved original consolidation and cloud assumptions; no current provider selection. |

The successor's approval status still controls. A proposed contract does not
become approved because it supersedes historical prose. No archive move, deletion,
new implementation plan, application edit or full Phase 1 acceptance occurs here.

---

## 1. Current Implementation Evidence

These documents describe the prototype and its prior implementation direction. They remain useful evidence, but they do not override the authority bridge or authorize production implementation when they conflict with it.

### 1.1 Core Project Documents

| Document | Location | Format | Description |
|----------|----------|--------|-------------|
| Hengshi_Design_Project_Consolidation_v3.docx | `docs/` | DOCX | February 2026 historical consolidation — implementation snapshot, self-reported readiness scorecard, taxonomy, prior tech stack, roadmap, and risks |
| Documentation_Index.md | `docs/active/` | MD | This file — master index of all documentation |
| SPEC.md | `docs/` | MD | MVP specification — service taxonomy, UX flow, data model, routes, performance requirements |
| BACKLOG.md | `docs/` | MD | Implementation backlog — epics, stories, status tracking |

### 1.2 Technical Reference Documents

| Document | Location | Format | Description |
|----------|----------|--------|-------------|
| Hengshi_Design_SRS_v3.md | `docs/active/` | MD | Software Requirements Specification v3.0 — functional/non-functional requirements with implementation status |
| Hengshi_Design_SAD_v3.md | `docs/active/` | MD | Software Architecture Document v3.0 — monorepo architecture, API layer, 3D world system, deployment strategy |
| Requirements_Architecture_Mapping_v3.md | `docs/active/` | MD | Requirements-to-architecture traceability with gap analysis |
| API_Reference.md | `docs/active/` | MD | REST API endpoint documentation with request/response schemas |
| Security_Hardening_Plan.md | `docs/active/` | MD | Sprint 1–2 security remediation plan with acceptance criteria |
| 3D_Mega_Menu_Style_Guide_v2.md | `docs/active/` | MD | Style guide for React Three Fiber / GSAP immersive navigation |

### 1.3 Architecture Diagrams (Current State)

| Diagram | Location | Description |
|---------|----------|-------------|
| Current_System_Architecture.mermaid | `docs/current-state/` | Monorepo layer architecture — Client → Frontend → API → ORM → Data |
| Current_Database_Schema.mermaid | `docs/current-state/` | PostgreSQL ER diagram — 7 tables with relationships |
| Current_3D_World_System.mermaid | `docs/current-state/` | 3D world entry flow, state machine, component hierarchy, room mapping |
| Current_Authentication_Flow.mermaid | `docs/current-state/` | JWT auth sequence — login, token generation, admin route protection |
| Current_Frontend_Architecture.mermaid | `docs/current-state/` | React component tree — routing, 3D engine, admin, state stores |
| Current_API_Router_Structure.mermaid | `docs/current-state/` | FastAPI router mounting — public, auth, admin routes with middleware |
| Current_Deployment_Pipeline.mermaid | `docs/current-state/` | Current dev setup + planned AWS production architecture |

### 1.4 Developer References

| Document | Location | Description |
|----------|----------|-------------|
| copilot-instructions.md | `.github/` | Development patterns and workflow documentation |
| README.md | Root | Project overview and setup instructions |
| apps/api/README.md | `apps/api/` | API-specific setup and development guide |

---

## 2. Project Knowledge Cleanup

The cleanup recommendations below are historical evidence only. They do not
authorize deletion, archive moves, project-knowledge removal, or any other
destructive action. Any future cleanup requires a separately bounded mechanical
task and its applicable approval.

The following items were previously identified in **Claude Project Knowledge** as cleanup candidates. Their status must be revalidated before any action.

### 2.1 Files to REMOVE from Project Knowledge

**Superseded v1/v2 Documents:**

| File | Reason |
|------|--------|
| `Software_Requirements_Specification__SRS__-_Hengshi_Design_Digital_Platform.md` | Superseded by SRS v3.0 |
| `Updated_Software_Requirements_Specification__SRS__v2_0.md` | Superseded by SRS v3.0 |
| `Software_Architecture_Document__SAD__-_Hengshi_Design_Digital_Platform.md` | Superseded by SAD v3.0 |
| `Software_Architecture_Document__SAD__-_Implementation_Specifications_Appendix.md` | Superseded by SAD v3.0 |
| `Requirements_to_Architecture_Mapping_Document.md` | Superseded by Requirements Mapping v3.0 |
| `Hengshi_Design_-_System_Documentation.md` | Superseded by Consolidation v3 |
| `3D_Mega_Menu_Style_Guide.md` (v1) | Superseded by v2.0 |

**Old Architecture Mermaid Diagrams (30 files — all represent the pre-pivot enterprise vision, not current state):**

| File | Category |
|------|----------|
| `High-Level_System_Architecture.mermaid` | System Overview |
| `Hengshi_Design_Digital_Platform_-_System_Architecture.mermaid` | Full Platform |
| `Authentication_Flow.mermaid` | Security |
| `IoT_Data_Flow.mermaid` | IoT |
| `IoT_Data_Aggregation_Flow.mermaid` | IoT |
| `IoT_Device_Provisioning_Process.mermaid` | IoT |
| `Deployment_Architecture.mermaid` | Infrastructure |
| `Detailed_Component_Interaction_Diagram.mermaid` | System Overview |
| `Database_Schema_Relationships.mermaid` | Data |
| `CI_CD_Pipeline_Flow.mermaid` | DevOps |
| `Network_Security_Architecture.mermaid` | Security |
| `Service_Scaling_and_Failover_Architecture.mermaid` | Infrastructure |
| `User_Registration_and_Onboarding_Flow.mermaid` | User Management |
| `Service_Subscription_Workflow.mermaid` | Billing |
| `Billing_and_Payment_Processing.mermaid` | Billing |
| `Support_Ticket_Lifecycle.mermaid` | Operations |
| `Consulting_Module_Architecture_and_Workflow.mermaid` | Modules |
| `Operations_Module_Architecture.mermaid` | Modules |
| `Security_Module_Components.mermaid` | Security |
| `Cloud_Service_Integration_Architecture.mermaid` | Infrastructure |
| `Analytics_Pipeline_Architecture.mermaid` | Analytics |
| `Real-time_Analytics_Processing_Flow.mermaid` | Analytics |
| `Report_Generation_Pipeline.mermaid` | Analytics |
| `Data_Backup_and_Recovery_Flow.mermaid` | Operations |
| `Event_Processing_System_Flow.mermaid` | Infrastructure |
| `Third-party_Service_Integration_Architecture.mermaid` | Integration |
| `External_API_Integration_Flow.mermaid` | Integration |
| `Payment_Gateway_Integration_Architecture.mermaid` | Billing |
| `Email_Notification_System_Architecture.mermaid` | Communications |
| `Monitoring_and_Alerting_System_Architecture.mermaid` | Operations |

**Empty Angular Component Files (7 files — 0 bytes, artifacts from pre-pivot Angular build):**

| File |
|------|
| `app_component.scss` |
| `auth_component.scss` |
| `building-entrance_component.scss` |
| `dashboard_component.scss` |
| `landing_component.html` |
| `landing_component.scss` |
| `landing_component.ts` |

---

## 3. Codebase Documentation Structure

```
hengshi-design/
├── docs/
│   ├── active/                          # Current technical reference
│   │   ├── Documentation_Index.md       # This file
│   │   ├── Hengshi_Design_SRS_v3.md
│   │   ├── Hengshi_Design_SAD_v3.md
│   │   ├── Requirements_Architecture_Mapping_v3.md
│   │   ├── API_Reference.md
│   │   ├── Security_Hardening_Plan.md
│   │   └── 3D_Mega_Menu_Style_Guide_v2.md
│   ├── current-state/                   # Architecture diagrams (current)
│   │   ├── Current_System_Architecture.mermaid
│   │   ├── Current_Database_Schema.mermaid
│   │   ├── Current_3D_World_System.mermaid
│   │   ├── Current_Authentication_Flow.mermaid
│   │   ├── Current_Frontend_Architecture.mermaid
│   │   ├── Current_API_Router_Structure.mermaid
│   │   └── Current_Deployment_Pipeline.mermaid
│   ├── Hengshi_Design_Project_Consolidation_v3.docx
│   ├── SPEC.md                          # MVP specification
│   └── BACKLOG.md                       # Implementation backlog
├── .github/
│   └── copilot-instructions.md
└── README.md
```
