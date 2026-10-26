# Phase 1 compatibility inventory — v1

## Current authority and dated evidence

The complete production graph remains unselected. Read [governance](../../AGENTS.md),
[decisions](../../DECISIONS.md) and the [reconciliation map](../software-definition/04-reconciliation-map.md)
first. Select the latest mutually compatible stable set across all coupled tools,
frameworks, libraries, runtimes, renderers/exporters, browsers and databases.
Independently newest registry versions and satisfying peer ranges do not prove
compatibility. Resolve, qualify, independently review and reproducibly lock the
complete set before MA-013 acceptance and separately authorized application adoption.

## Accepted bounded exceptions

- [D-072](../../DECISIONS.md#d-072--bounded-gensync-development-and-ci-lint-exception)
  permits only `gensync 1.0.0-beta.2` in the isolated React development/CI lint
  evaluation, under its five reviewed conditions. It expires 2027-01-05. Actual
  conformance, integrity/provenance, licences/advisories, deterministic resolution
  and exclusion from every deployed execution/artifact path remain obligations.
  A devDependency label proves no exclusion. This permits no production runtime,
  general Babel/build use, other prerelease or peer/parity waiver.
- [D-077](../../DECISIONS.md#d-077--temporary-evaluated-three-renderer-exception)
  permits only root `three 0.184.0` with `@types/three 0.184.1` as the temporary
  evaluated pair for the eventual complete stable graph. The [exact conditions](THREE_STABLE_EXCEPTION_PROPOSAL.md)
  retain strict declarations, separate nested-renderer evidence, full graph,
  supply-chain, rollback and adoption gates. Recheck by 2027-01-07, before adoption
  and on a relevant stable fix; continued use then needs a fresh decision.

Neither exception accepts a production graph, changes application dependencies
or waives complete qualification. Do not reopen these already-settled choices.
D-068 defers hosting/provider/region/SKU/cost planning: Azure and AWS remain
candidates. Existing Entra/AI privacy constraints and Outlook/Teams intent remain,
without requiring Microsoft 365. Native local operation requires no Docker.

## Controlling evidence by subject

| Subject | Source and scope |
|---|---|
| Frontend, renderer and lint candidates | [Frontend/3D appendix](refresh-evidence-2026-10-04.md) owns the strict resolver failures, official lint/native alternatives, TypeScript bridge/React/LSP probes and coupled declaration/build/browser results. Each study retains its failures, warnings and exact bounded review; successful fixtures select no full graph. |
| Renderer exception basis | [Published blocker](refresh-evidence-2026-10-04.md#published-renderer-blocker-and-exception-proposal--2026-10-07) and the [D-077 proposal review](reviews/three-stable-exception-v1-2026-10-07.md) retain the evidence for the accepted temporary pair. They grant no application upgrade or broader renderer exception. |
| Frontend inventory, notices and provenance | [Supply-chain observations](refresh-evidence-2026-10-04.md#matched-candidate-supply-chain-observations--2026-10-06), [full installed notice reads](refresh-evidence-2026-10-04.md#full-installed-notice-reads-and-broader-root-inventory--2026-10-08) and [supplemented bundled inventory](refresh-evidence-2026-10-04.md#supplemented-virtual-bundled-inventory--2026-10-08) own the subsequent exact-artifact studies and reviews. The bounded supplement does not turn the original failed npm CLI SBOM into a success. Empty advisory/import lists establish no universal security or deployed-exclusion proof. |
| Backend candidate closure and native qualification | [Backend appendix](backend-evidence-2026-10-04.md) owns the current metadata closure, earlier isolated trial and [preferred-client result/wheel notices](backend-evidence-2026-10-04.md#preferred-client-native-result-and-wheel-notices--2026-10-09). Native library and bounded results reviews do not prove Hengshi API/OIDC/database behavior or select production clients. |
| Identity distribution and rights evidence | [Staff identity comparison](backend-evidence-2026-10-04.md#maintained-staff-identity-client-comparison--2026-10-08) and [distribution observations](backend-evidence-2026-10-04.md#staff-identity-distribution-licences-and-publishing-evidence--2026-10-09) retain source, licence and publishing evidence plus its scoped review. Package identity, archive integrity and available attestation metadata are distinct from verified build provenance and legal clearance. |
| Backend roles and advisory scope | [Role/metadata proposal](backend-evidence-2026-10-04.md#proposed-backend-dependency-roles--2026-10-09) and [dated advisory observation](backend-evidence-2026-10-04.md#separate-dated-advisory-observation) retain conditional identity/migration/test reachability and exact lookup scope. They select no production split and qualify no separately deployed environments. |
| Machine artifacts and reversible waves | The [artifact map below](#artifact-map) preserves the dated baseline, graph, controls, reference registry and original reviews. July provider mappings and candidate observations are historical inputs, subordinate to current decisions. |

The appendices own detailed commands, inputs, source associations, frozen review
receipts and remaining limitations. This index does not duplicate a live evidence
journal. Receipts apply to their exact snapshots; current entry-page edits do not
replace their hashes or expand PASS to new inputs.

## Remaining selection and acceptance work

Under D-097 (2026-10-25), qualify the complete coupled stable graph for the
current increment, including shared/transitive dependencies. Retain future-only
families in their owning increment; they do not block unrelated 2D delivery.
Complete the applicable platform/embedded/deployed inventories; qualify applicable declarations, build/runtime/browser/database and
editor/CI boundaries; establish D-072 isolation, exact licence/notice obligations,
advisory disposition and provenance; produce reproducible locks plus reversible
wave/checkpoint/rollback criteria. Conditional and deferred families retain their
selection and approval gates. No runtime result, legal clearance or implementation
is inferred from a schema, metadata model, source association or synthetic fixture.

MA-013 and applicable selection/adoption permissions remain scoped to the affected
increment. Full integrated acceptance remains required before completion of the
whole product; it is not a blanket prerequisite for increment implementation. Protect the application, its locks/environments and the Atlanta
asset. No installation, dependency upgrade, provider operation, paid activation,
commit, push or deployment is authorized by this entry.

## Historical inventory and preserved entry

The [complete entry before this reconciliation](../../output/research/compatibility-entry-reconciliation-2026-10-12/before/README.md)
preserves the July inventory narrative, later candidate summaries and their exact
review references. Interpret its relative links from this directory. The earlier
[October 9 predecessor](../../output/research/compatibility-entry-consolidation-2026-10-09/README.before.md)
also remains unchanged. Historical awaiting-approval/provider/version statements
do not override current decisions or create new founder requests.

Use the controlling evidence-by-subject table above for current reading; detailed
trial outcomes, failures, warnings, review scopes and limitations remain in those
appendices. This consolidation changes navigation only. No exception condition,
machine artifact, lock, installed environment, review receipt or application is
changed, and no earlier PASS transfers to these edited entry-page bytes.

## Artifact map

| Artifact | Purpose | Authority |
|---|---|---|
| [baseline-inventory.json](baseline-inventory.json) | Machine-readable observed runtimes, packages, locks, manifests, and capability states | Dated baseline evidence only |
| [compatibility-graph.json](compatibility-graph.json) | Machine-readable component and coupling-edge skeleton with candidates, constraints, tests, and rollback | Candidate analysis; lock selection deferred |
| [compatibility-controls.json](compatibility-controls.json) | Machine-readable waves, checkpoints, edge assignments, unsatisfied human gates, coverage, supply-chain obligations, and 44 candidate paths | Revision 1 control model; no gate or checkpoint is accepted |
| [reference-index.json](reference-index.json) | Canonical namespaces and deterministic local resolution for every nested reference in the machine artifacts | Evidence registry; unknown, duplicate, ambiguous, or unresolved references fail validation |
| [evidence-log-2026-07-19.md](evidence-log-2026-07-19.md) | Context7, official-documentation, registry, local-command, inference, and unresolved evidence | Dated evidence record |
| [blockers-and-obligations.md](blockers-and-obligations.md) | Human gates, compatibility blockers, failure modes, wave boundaries, rollback, and test obligations | Required handoff constraints |
| [validate.ps1](validate.ps1) | Deterministic structural, source-reconciliation, link, whitespace, candidate-channel, and secret-shaped-value validation | Validation tool |
| [validation-report-2026-07-19.md](validation-report-2026-07-19.md) | Executed validation evidence and limitations | Necessary but not sufficient for acceptance |
| [architecture and supply-chain review — iteration 1](reviews/architecture-supply-chain-review-iteration-1.md) | Independent review that identified three HIGH and one MEDIUM finding | Durable `REVISE` evidence retained unchanged |
| [architecture and supply-chain review — iteration 2](reviews/architecture-supply-chain-review-iteration-2.md) | Independent closure verification of revision 1 | `PASS`; all four findings closed and no new blocker/HIGH/MEDIUM finding |

The graph/control files retain their dated candidate and gate identities. Resolve
current authority through the constitution and decisions before using them;
historical cloud mappings select neither Azure nor AWS. The original structural
validator and review receipts remain evidence of their exact frozen scopes, not
a current production selection or proof of package/runtime compatibility.

The [independent entry review](../../output/research/compatibility-entry-reconciliation-2026-10-12/independent-review-entry-v1.json)
passes navigation consolidation at eighteen frozen inputs with no findings. This
later receipt link is outside those reviewed bytes. It does not select a graph,
qualify packages/platforms, clear licences/security or accept Phase 1.
