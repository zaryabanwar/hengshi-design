# Phase 1 External UI Reference-Production Contract (MA-025)

**Project:** Hengshi Design
**Package date:** 2026-09-06
**Status:** `awaiting_human` — prepared for founder decision at MA-025
**External-write status:** Not authorized; no Figma or Stitch account, file,
project, comment, export, or API call has been created, read, written, or
attempted

## Purpose

This package is the bounded contract the founder must approve **before** any
external design-provider write may happen. D-037 accepted the UI reference-design
*documentation* contract and explicitly left external production closed. This
package answers the eleven questions that gate must resolve: provider, scope and
sequence, write scope, deliverables, evidence capture, review sequence, cost
boundary, stop conditions, rollback, credential handling, and acceptance criteria.

It creates no screen, no external file, no application code, and no publication.

## Controlling authority

- **D-025** foundation, claims, SEO, 33 routes; `/industries` retained.
- **D-026** Evidence in Motion; evidence-led innovation delivery partner.
- **D-035** frozen Signal Ledger system + Framework Relay logo hybrid; marks
  unregistered and trademark-not-cleared.
- **D-036** the exact Phase 1 UX architecture package.
- **D-037** the exact 13-file UI reference-design freeze, SHA-256
  `97E79201CC36F01718A027AD800E63BDD5AAFC47E41137D65253BAABA6B2120F`.
- **Constitution 2.0.0** principles IV, VII, and VIII.

The D-037 package is the normative input. Where this package and D-037 appear to
differ, D-037 governs and the difference is a defect here.

## Artifact map

| Artifact | Role |
|---|---|
| [MA-025 production contract](UI_REFERENCE_PRODUCTION_CONTRACT.md) | Normative provider decision, batch scope and sequence, write scope, deliverables, evidence capture, review sequence, cost boundary, stop conditions, rollback, credential boundary, and acceptance criteria |
| [Provider evaluation](provider-evaluation.csv) | Criterion-by-criterion Figma/Stitch assessment traced to the accepted contract requirement that drives each criterion |
| [Batch production plan](batch-production-plan.csv) | The nine batches with their MA-025 disposition, execution order, entry and exit conditions |
| [External write scope](external-write-scope.csv) | Eight permitted and eleven prohibited external operations, plus repository and Git scope |
| [Evidence capture plan](evidence-capture-plan.csv) | Thirty evidence, naming, coverage, export, hashing, credential, and claim rules with verification methods |
| [Stop conditions](stop-conditions.csv) | Twelve enumerated halts with escalation target and resume authority |
| [Traceability](traceability.csv) | Forty rows mapping every contract section to its upstream authority and downstream gate |
| [Validator](validation/validate-ui-reference-production.ps1) | Deterministic parsing, exact-set, reference, scope, claim, and gate checks |
| [Validation report](validation/validation-report.md) | Executed command, timestamp, counts, outcome, and limitations |
| [Producer inspection](producer-inspection.md) | Producer scope, completeness, feasibility, and unresolved-gate inspection |

## The two findings that change the shape of this gate

### 1. Only seven of nine batches are authorizable

`design-batch-plan.csv` makes **B07** depend on an approved 3D storyboard and
asset specification and on **MA-004** for GLB reuse. The storyboard workstream is
`not_started` and MA-004 is `blocked`. **B09** hard-requires B07. Therefore:

- **Authorizable now:** B01, B02, B03, B04, B05, B06, B08.
- **Deferred to MA-026:** B07, B09, `docs/ui/UI_SPEC.md`, and the final
  visual-direction decision.

Because B09 produces the evidence index and `UI_SPEC.md`, the D-037 §15 handoff
**cannot complete under MA-025 alone**. Approving MA-025 is not approval of the
whole reference-screen programme.

### 2. Neither provider is reachable from this host today

`AGENTS.md` names `%APPDATA%\Code\User\mcp.json` as the canonical MCP inventory.
That file does not exist here, and no Figma or Stitch MCP is configured or exposed
in any checked location. `docs/software-definition/02-ai-dev-tooling-and-mcp.md`
line 43 claims a Stitch MCP is "Configured locally"; that claim is not true of this
host and is recorded as a correction obligation.

**Approving MA-025 does not by itself make production possible.** One of two
enablement paths (§3.5) must complete first: a human operator working directly in
Figma, or a configured and capability-tested agent path.

## Boundary and non-claims

This package contains Markdown, CSV, and one PowerShell validator only. It does
not create a screen, prototype, component library, external file, or
`docs/ui/UI_SPEC.md`; perform or attempt any provider operation; approve a visual
direction or any exact public or legal copy; assert any Figma free-tier limit
(five are recorded as unverified); certify WCAG 2.2 conformance; or authorize
spend, paid assets, dependencies, migrations, infrastructure, publication, Git
operations, deployment, complete Phase 1 acceptance, or launch.

WCAG 2.2 Level AA for every applicable full page and complete process remains the
normative production and review **target**, never a conformance claim. Design
references and annotations alone cannot establish conformance.

MA-013 compatibility acceptance remains a separate, unaffected gate.

## Review and approval gates

1. Run the deterministic validator and complete producer inspection.
2. Present **MA-025** to the founder. Approval authorizes bounded external
   production for B01–B06 and B08 only.
3. Complete and record §3.5 capability enablement before the first external write.
4. Run B01 as a gated pilot; halt for founder pilot acceptance before B02.
5. Run B02–B08 serially, each exiting on two clean independent reviews.
6. Present MA-026 for B07, B09, `UI_SPEC.md`, and the final visual direction.
