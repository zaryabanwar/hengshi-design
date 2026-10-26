# Independent publication-contract review

Date: 2026-10-04. Reviewer: `review_publication_contract`; independent of producer.
Result: PASS after producer revision 1. Open actionable findings: 0.
Scope: definition-only contract, public JSON shape schema and focused validation tests.

Authority inspected: AGENTS.md, Constitution 2.0.0, PROJECT.md, PROJECT_STATE.yaml,
software-definition README, D-019/D-065, accepted architecture boundaries and
foundation publication/data requirements. The frozen architecture header is
superseded by D-065; this review does not reopen that acceptance.

## First-pass findings and closure

| Finding | Severity | Reinspection evidence | Result |
|---|---|---|---|
| PUB-R1-001: guarding the PostgreSQL generation alone permits a delayed external routing operation to overwrite a newer generation. | High | `PUBLICATION_CONTRACT.md:91-100` requires one outstanding durable cutover, conditional fencing at the external effect boundary or proven terminal serialization, rejection of stale workers and a hold on subsequent cutovers while outcomes are unknown. Lease expiry, timeout and cancellation requests are explicitly insufficient. The out-of-order generation/late-acknowledgement case is required at line 133. | Closed |
| PUB-R1-002: `$` regex anchors accepted final newlines in digests, identifiers, canonical paths and storage keys. | Medium | `publication-manifest.schema.json:22,26,30,34` now uses absolute-end negative assertions. `test_publication_manifest_schema.py:67-70` reproduces all four rejected newline mutations. | Closed |

Withdrawal at `PUBLICATION_CONTRACT.md:104-110` changes serving eligibility rather
than immutable bytes. Changed content requires a new release. No provider operation,
regional availability, drain duration or deployment cutover is certified.

## Exact reviewed bytes

SHA-256:

- `docs/phase-1-architecture/contracts/PUBLICATION_CONTRACT.md`: `3FB162F67A3B80E8E2B2B2E97B7E92935A2C5448C71E1404A385D05FF30EDFF0`
- `docs/phase-1-architecture/contracts/publication-manifest.schema.json`: `D3620C8326246BC34040188DE610C5823F1013936572D3FFB63A5EB350BC3852`
- `scripts/validation/test_publication_manifest_schema.py`: `A3DD5CF00A20FED6955B8A8694C7E572F1FF3D695B7728FEC00C641F69DAAF4C`

Verification: independently ran `python scripts/validation/test_publication_manifest_schema.py`;
2 tests passed, including 19 negative mutations and the positive synthetic shape.
Tests prove only selected shape/format rejection; they do not prove checksums,
approval, graph validity, isolation, concurrency, routing or rollback behavior.

PASS is independent definition-review evidence, not founder acceptance, application
implementation, production dependency selection or permission for external writes.
