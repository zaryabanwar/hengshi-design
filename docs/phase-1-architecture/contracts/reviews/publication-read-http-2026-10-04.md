# Independent publication GET wire review — 2026-10-04

Disposition: **PASS, revision 1**, for this bounded proposed definition only. Reviewer: independent agent `/root/review_publication_contract`; producer files were not edited by the reviewer. No remaining actionable finding in the inspected scope.

Scope: IF-PUB-01/02 public GET transport proposal, against D-019/D-065, accepted PUB-001–PUB-007, publication manifest/eligibility/refresh authority, logical interface/field rows, and content FCT-08/FCT-13. Governance and checkpoint documents were inspected for authority and held gates; their hashes below do not imply a fresh exhaustive review of every historical entry.

## Initial finding and closure

- **P2, initial PUBLICATION_READ_HTTP.md:98–99:** the requirement to obtain an unconditional response only when lacking a “verified matching envelope” left current-release identity ambiguous after a wildcard 304. Previously verified A cannot establish that `/current` still selects A after a cutover to B. [RFC 9110 §13.1.2](https://www.rfc-editor.org/rfc/rfc9110.html#section-13.1.2) makes the wildcard condition an existence check, not an identity comparison. Initial candidate SHA256: `ABDA555ED137225EBADDE08F3DE0170D8B55E54089DBAFDFC3AC68AF1D897035`.
- **Closed in revision 1:** lines 98–103 require obtaining and verifying an unconditional 200 after any 304 before accepting or refreshing application context; prior verification is insufficient and 304 cannot extend an older pin. The acceptance table adds the A-to-B cutover/wildcard case. This is a future implementation obligation, not an executed test.

## Assessment and limits

The paths remain catalogue proposals. Requested pins cannot redirect or silently become current; public credentials cannot bypass eligibility or disclose previews. Closed responses preserve the schema's identifier and canonical checksum authority, exclude private process fields, and distinguish known ineligibility (404), unknown authority/cutover (503), failed integrity (500) and failed preconditions (412). No read grants review, approval, activation or withdrawal power.

Server wildcard 304 behavior, validator-free tag/date handling, normal failure checks before preconditions, RFC precedence and ignored range support are coherent with [RFC 9110 §§13.1–13.2 and 14](https://www.rfc-editor.org/rfc/rfc9110.html#section-13). The consumer clarification prevents treating wildcard existence as a successful current-envelope refresh. [RFC 9111 §5.2.2.5](https://www.rfc-editor.org/rfc/rfc9111.html#section-5.2.2.5) supports the proposed no-store profile; the document correctly retains limits for already delivered bytes, uncontrolled intermediaries and separate asset caching. Withdrawal coordination is mandatory while exact fencing, in-flight limits and propagation/detection measurements remain held; no instantaneous revocation guarantee is asserted.

The [FastAPI error-handler](https://fastapi.tiangolo.com/tutorial/handling-errors/) and [additional-response](https://fastapi.tiangolo.com/advanced/additional-responses/) references support available mechanisms, not enforcement or a selected dependency version. Four local document references resolve; CSV public/error rows and schema definitions were inspected. These checks are artifact inspection only. No prose tests, handler execution, database/cache/withdrawal race tests, browser tests, dependency changes or operational probes were performed. Provider choice, request/resource limits, edge/CORS/method behavior, retry timing, retention/legal choices, detailed implementation, the broader QA revision exception and integrated Phase 1/founder acceptance remain held. This receipt does not authorize implementation, publication, deployment or a production lock.

## Exact input SHA256

Paths are repository-relative; hashes identify current bytes, not acceptance of all contents.

| Input | SHA256 |
|---|---|
| `AGENTS.md` | `55405CB02A96D05F7F6D68E56A588D743F83877FB2691A5A9F2C736126ADBCC5` |
| `.specify/memory/constitution.md` | `33EC0BB02B0D0D9A55D0971589BD19F7242F5D56DA130F8F496BC1D31A8B5D23` |
| `PROJECT.md` | `A483BD2713FE420322772AB7FB07C848AAF103088697C05AB91F35D2E5EA1461` |
| `DECISIONS.md` | `C843AE17EE0AA7B9E5DD0BE39595310B5B25C31BEA2B97ECE4E6EBD34C2DADBF` |
| `PROJECT_STATE.yaml` | `BEC75B241725EE91875A2783EC206F257B3B7FA4E53E7C203254C230B6C2E4FB` |
| `docs/software-definition/README.md` | `20AEC5800930F248A5E9C7D134550AB15A7AA6FBF88CF21AFF7FD5390162BB18` |
| `TASKS.md` | `880218BEDCE7ED35A90E6743931759CB40AC6F457071BD770BC51AC4E21B5452` |
| `docs/phase-1-foundation/01-product-requirements.md` | `5B33D8BD87BDB3B093EF319DB3EA3BB64DEAEDDF2706F5D21505BFB66035AA39` |
| `docs/phase-1-architecture/contracts/PUBLICATION_READ_HTTP.md` | `DDAD22E39A58334D08D96BB037B16259A1EF2710712360844AA4FDCC696D5271` |
| `docs/phase-1-architecture/contracts/PUBLICATION_CONTRACT.md` | `D2EE7C9781473250459B700C7C5D7CFBAFA7F88A9BB8DAB5146B0853D3680AD3` |
| `docs/phase-1-architecture/contracts/publication-manifest.schema.json` | `D3620C8326246BC34040188DE610C5823F1013936572D3FFB63A5EB350BC3852` |
| `docs/phase-1-architecture/contracts/interface-catalog.csv` | `42018A3E5CC6C1EDF488C392B0349688A92B2CAB5A8F50E717F1BCA84A70A49C` |
| `docs/phase-1-architecture/contracts/process-fields.csv` | `5737B8F4BD47B90A5020AE8943CB2C7786582C605E14D97212B4334FFB26522A` |
| `specs/004-design-services-content/spec.md` | `64A357200EAF46B8AAA710D67B2EB05415377F924EC6C1441D0F0731D51D06C7` |
