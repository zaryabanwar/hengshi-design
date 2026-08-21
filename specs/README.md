# Feature Specifications

This directory contains feature-level specifications following the **Spec-Driven
Development (SDD)** cycle.

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

Each transition requires user review and approval.

## Current Feature Specs

| # | Feature | Status |
|---|---------|--------|
| 001 | Platform Security Hardening | Draft spec + draft plan; task generation gated |
| 002 | Testing and Monitoring | Planned placeholder |
| 003 | 3D Experience Completion | Planned placeholder |
| 004 | Design Services and Content | Planned placeholder |
| 005 | AWS Deployment and Launch | Planned placeholder |

## Templates

Templates for all spec artifacts are in `.specify/templates/`.

## How to Start a New Feature

1. Create a new directory: `specs/NNN-feature-slug/`
2. Copy `.specify/templates/spec-template.md` as `spec.md`
3. Fill in the specification
4. Run the SDD cycle: clarify → plan → tasks → implement
5. Update `.specify/feature.json` to point to the new directory
