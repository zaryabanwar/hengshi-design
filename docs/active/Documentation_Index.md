# Hengshi Design Digital Platform — Documentation Index

**Document ID:** HD-INDEX-2026-001
**Version:** 1.0
**Date:** February 9, 2026
**Status:** Active | Classification: Internal

---

## Purpose

This index serves as the single source of truth for all project documentation. It catalogs every document, its status (Active, Superseded, Future State), and its relationship to the current implementation.

The platform underwent a strategic architectural pivot in early 2026 from an 11-service microservices design (Angular/Django/MongoDB) to a focused React/FastAPI/PostgreSQL monorepo. Documentation has been updated accordingly.

---

## 1. Active Documents (Current State)

These documents reflect the actual implemented architecture and should be referenced for all development decisions.

| Document | Format | Description |
|----------|--------|-------------|
| `Hengshi_Design_Project_Consolidation_v3.docx` | DOCX | Authoritative project consolidation — executive summary, readiness scorecard, service taxonomy v2, tech stack, sprint roadmap, risk register |
| `Hengshi_Design_SRS_v3.md` | MD | Software Requirements Specification v3.0 — functional and non-functional requirements for React/FastAPI/PostgreSQL monorepo |
| `Hengshi_Design_SAD_v3.md` | MD | Software Architecture Document v3.0 — monorepo architecture, API layer, 3D world system, data layer, deployment strategy |
| `Requirements_Architecture_Mapping_v3.md` | MD | Requirements-to-architecture traceability for current implementation |
| `API_Reference.md` | MD | Current REST API endpoint documentation with request/response schemas |
| `Security_Hardening_Plan.md` | MD | Sprint 1–2 security remediation plan with implementation details |
| `3D_Mega_Menu_Style_Guide_v2.md` | MD | Updated style guide for React Three Fiber / GSAP immersive navigation |
| `Current_System_Architecture.mermaid` | Mermaid | Current monorepo architecture diagram |
| `Current_Database_Schema.mermaid` | Mermaid | Current PostgreSQL schema with relationships |
| `Current_3D_World_System.mermaid` | Mermaid | 3D world configuration and navigation flow |
| `Documentation_Index.md` | MD | This file — master index of all documentation |

---

## 2. Superseded Documents (Historical Reference Only)

These documents are from the original v1.0/v2.0 architecture (Angular/Django/MongoDB/Microservices). They should **not** be referenced for current technical decisions but remain valuable for understanding the evolution of requirements and the long-term enterprise vision.

| Document | Original Version | Superseded By | Notes |
|----------|-----------------|---------------|-------|
| `Software_Requirements_Specification__SRS__-_Hengshi_Design_Digital_Platform.md` | v1.0 (Feb 2025) | `Hengshi_Design_SRS_v3.md` | Tech stack (Angular/Django/MongoDB) no longer current |
| `Updated_Software_Requirements_Specification__SRS__v2_0.md` | v2.0 (Feb 2025) | `Hengshi_Design_SRS_v3.md` | Performance metrics remain aspirational targets for Phase 3+ |
| `Software_Architecture_Document__SAD__-_Hengshi_Design_Digital_Platform.md` | v1.0 (Feb 2025) | `Hengshi_Design_SAD_v3.md` | Microservices/K8s/Kafka architecture deferred |
| `Software_Architecture_Document__SAD__-_Implementation_Specifications_Appendix.md` | v1.0 (Feb 2025) | `Hengshi_Design_SAD_v3.md` | FastAPI replaces Django; PostgreSQL replaces MongoDB |
| `Requirements_to_Architecture_Mapping_Document.md` | v1.0 (Feb 2025) | `Requirements_Architecture_Mapping_v3.md` | Requirements valid; architecture mapping outdated |
| `Hengshi_Design_-_System_Documentation.md` | v1.0 (Feb 2025) | `Hengshi_Design_Project_Consolidation_v3.docx` | Business models and IoT vision remain relevant as Phase 3+ reference |

**Recommendation:** Archive these into a `/docs/archive/v1-v2/` directory. Do not delete — they contain the enterprise vision for future phases.

---

## 3. Future State Architecture Diagrams

The following 30 Mermaid diagrams represent the **original enterprise vision** (microservices, Kubernetes, Kafka, multi-region). They are **not** current state but serve as Phase 3+ reference architectures. Tag as "Future State" when referencing.

| Diagram | Category | Phase |
|---------|----------|-------|
| `High-Level_System_Architecture.mermaid` | System Overview | Phase 3+ |
| `Hengshi_Design_Digital_Platform_-_System_Architecture.mermaid` | Full Platform | Phase 3+ |
| `Authentication_Flow.mermaid` | Security | Phase 2+ (partially relevant) |
| `IoT_Data_Flow.mermaid` | IoT | Phase 2 |
| `IoT_Data_Aggregation_Flow.mermaid` | IoT | Phase 2 |
| `IoT_Device_Provisioning_Process.mermaid` | IoT | Phase 2 |
| `Deployment_Architecture.mermaid` | Infrastructure | Phase 3+ |
| `Detailed_Component_Interaction_Diagram.mermaid` | System Overview | Phase 3+ |
| `Database_Schema_Relationships.mermaid` | Data | Superseded by `Current_Database_Schema.mermaid` |
| `CI_CD_Pipeline_Flow.mermaid` | DevOps | Phase 1 (adapt for GitHub Actions) |
| `Network_Security_Architecture.mermaid` | Security | Phase 3+ |
| `Service_Scaling_and_Failover_Architecture.mermaid` | Infrastructure | Phase 3+ |
| `User_Registration_and_Onboarding_Flow.mermaid` | User Management | Phase 2+ |
| `Service_Subscription_Workflow.mermaid` | Billing | Phase 3 |
| `Billing_and_Payment_Processing.mermaid` | Billing | Phase 3 |
| `Support_Ticket_Lifecycle.mermaid` | Operations | Phase 3+ |
| `Consulting_Module_Architecture_and_Workflow.mermaid` | Modules | Phase 3+ |
| `Operations_Module_Architecture.mermaid` | Modules | Phase 3+ |
| `Security_Module_Components.mermaid` | Security | Phase 3+ |
| `Cloud_Service_Integration_Architecture.mermaid` | Infrastructure | Phase 3+ |
| `Analytics_Pipeline_Architecture.mermaid` | Analytics | Phase 2+ |
| `Real-time_Analytics_Processing_Flow.mermaid` | Analytics | Phase 2+ |
| `Report_Generation_Pipeline.mermaid` | Analytics | Phase 2+ |
| `Data_Backup_and_Recovery_Flow.mermaid` | Operations | Phase 2+ |
| `Event_Processing_System_Flow.mermaid` | Infrastructure | Phase 3+ |
| `Third-party_Service_Integration_Architecture.mermaid` | Integration | Phase 3+ |
| `External_API_Integration_Flow.mermaid` | Integration | Phase 3+ |
| `Payment_Gateway_Integration_Architecture.mermaid` | Billing | Phase 3 |
| `Email_Notification_System_Architecture.mermaid` | Communications | Phase 2 |
| `Monitoring_and_Alerting_System_Architecture.mermaid` | Operations | Phase 1–2 (adapt) |

**Recommendation:** Move to `/docs/architecture/future-state/` directory.

---

## 4. Files to Remove

The following files are empty artifacts from the pre-pivot Angular architecture. They contain no content and serve no purpose.

| File | Reason |
|------|--------|
| `app_component.scss` | Empty, Angular artifact |
| `auth_component.scss` | Empty, Angular artifact |
| `building-entrance_component.scss` | Empty, Angular artifact |
| `dashboard_component.scss` | Empty, Angular artifact |
| `landing_component.html` | Empty, Angular artifact |
| `landing_component.scss` | Empty, Angular artifact |
| `landing_component.ts` | Empty, Angular artifact |

**Recommendation:** Delete these files from the project.

---

## 5. Recommended Project File Structure

```
docs/
├── active/
│   ├── Documentation_Index.md
│   ├── Hengshi_Design_SRS_v3.md
│   ├── Hengshi_Design_SAD_v3.md
│   ├── Requirements_Architecture_Mapping_v3.md
│   ├── API_Reference.md
│   ├── Security_Hardening_Plan.md
│   ├── 3D_Mega_Menu_Style_Guide_v2.md
│   └── Hengshi_Design_Project_Consolidation_v3.docx
├── architecture/
│   ├── current-state/
│   │   ├── Current_System_Architecture.mermaid
│   │   ├── Current_Database_Schema.mermaid
│   │   └── Current_3D_World_System.mermaid
│   └── future-state/
│       ├── [30 original mermaid diagrams]
│       └── README.md (noting these are Phase 3+ reference)
└── archive/
    └── v1-v2/
        ├── SRS_v1.md
        ├── SRS_v2.md
        ├── SAD_v1.md
        ├── SAD_Implementation_Specs.md
        ├── Requirements_Mapping_v1.md
        └── System_Documentation_v1.md
```
