# Independent public-read error-schema review — 2026-10-04

Disposition: **PASS, initial candidate**. Independent reviewer: `/root/review_publication_contract`. No actionable finding or producer revision was required. This receipt covers only the new schema and expanded definition-tooling fixtures at the hashes below; earlier reports remain unchanged.

The five exact `code`/`explanation`/`retryability` objects match the independently reviewed PUBLICATION_READ_HTTP.md application-error table. Root object type, required `error` and `additionalProperties: false` reject missing/wrong root shapes and extra root fields. Whole-object `const` branches reject missing, null, wrong-type, unrecognized, mixed and additional nested fields, including `operation_ref` and diagnostics. The distinct code strings make the five branches disjoint. The proposal remains limited to IF-PUB-01/02; it does not redefine private booking, handoff, AI, staff or privacy operation errors.

These semantics accord with [JSON Schema Validation 2020-12 §6.1.3](https://json-schema.org/draft/2020-12/json-schema-validation#section-6.1.3) and [Core §§4.2.2/10.2.1.3](https://json-schema.org/draft/2020-12/json-schema-core#section-10.2.1.3): equality compares complete object members, and oneOf requires exactly one successful branch. The installed python-jsonschema const/oneOf source was inspected. Local jsonschema **4.23.0** is observed validation tooling, not an approved production dependency or compatibility-graph selection.

Fixture expected bodies are written from the reviewed wire contract, not extracted from the schema under test. Each permitted body is exercised, with extra fields rejected at both levels; negative cases cover missing/null fields, mixed variants, unknown values, unreviewed diagnostic text and malformed shapes. Comparison with the retained envelope-only script confirms its existing fixtures are preserved; the additions are one schema path and the two public-error shape tests. The earlier envelope-only review does not cover these additions.

Independent command: `python scripts/validation/test_publication_manifest_schema.py -v` — **4 tests passed**, exit 0, comprising two existing envelope tests and two new error-schema tests. This is schema/validator boundary evidence, not a test of an application handler. No wording tests, application/dependency/database/service changes or external writes were performed; only this new review file was written.

Limits: validating a decoded object cannot establish duplicate-key rejection at parsing, corresponding HTTP status or headers, safe serialization, public authorization, serving eligibility, withdrawal races, caching, retry execution or actual API enforcement. The schema comment and test docstrings retain that distinction. Future actual-boundary evidence, integrated Phase 1/founder acceptance and the broader QA revision exception remain held. This PASS grants no implementation, publication or deployment permission.

## Exact inspected input SHA256

| Repository-relative input | SHA256 |
|---|---|
| `AGENTS.md` | `55405CB02A96D05F7F6D68E56A588D743F83877FB2691A5A9F2C736126ADBCC5` |
| `.specify/memory/constitution.md` | `33EC0BB02B0D0D9A55D0971589BD19F7242F5D56DA130F8F496BC1D31A8B5D23` |
| `docs/phase-1-architecture/contracts/publication-read-error.schema.json` | `3DBE09D96937C80575A659F4E91B310F8B3D8AF962F632911C5BF7BB340720BF` |
| `scripts/validation/test_publication_manifest_schema.py` | `B8464D4A67D9C8C2F46D4583CF09A6F816661FDF65FD1CCE20568D60FE5A78B4` |
| `docs/phase-1-architecture/contracts/PUBLICATION_READ_HTTP.md` | `DDAD22E39A58334D08D96BB037B16259A1EF2710712360844AA4FDCC696D5271` |
| `docs/phase-1-architecture/contracts/process-fields.csv` | `5737B8F4BD47B90A5020AE8943CB2C7786582C605E14D97212B4334FFB26522A` |
| `docs/phase-1-architecture/contracts/interface-catalog.csv` | `42018A3E5CC6C1EDF488C392B0349688A92B2CAB5A8F50E717F1BCA84A70A49C` |
| `docs/phase-1-architecture/contracts/publication-manifest.schema.json` | `D3620C8326246BC34040188DE610C5823F1013936572D3FFB63A5EB350BC3852` |
| `output/research/contract-review-reference-reconciliation-2026-10-04/test_publication_manifest_schema.reviewed-original.py` | `A3DD5CF00A20FED6955B8A8694C7E572F1FF3D695B7728FEC00C641F69DAAF4C` |
