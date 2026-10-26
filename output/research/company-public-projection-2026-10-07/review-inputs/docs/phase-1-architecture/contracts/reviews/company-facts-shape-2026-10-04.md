# Prepared company-facts shape review — v1

Date: 2026-10-04. Verdict: **REVISE** for one Low fixture finding below. Initial independent candidate review; zero review correction cycles used. The schema and new typed-proposal section otherwise satisfy this bounded shape/authority review. No application implementation or legal clearance is inferred.

## Exact reviewed inputs

Independently computed SHA-256 identities; the three commissioned candidate hashes match. The contact preimage diff contains only the typed prepared-facts proposal. Governance/checkpoint inputs below provide context, not a new whole-package acceptance.

| Input | SHA-256 |
|---|---|
| `docs/software-definition/06-entity-and-public-contact.md` | `26B071152F9FABF6608C81FFEA3E8973EED8DB81D9664585350FE0FB5DB8EF91` |
| `docs/phase-1-architecture/contracts/company-facts.schema.json` | `4C3162F19483563B88C1EF6BEED4055A7ACB9C608A947B0707D9AAA39E9F0695` |
| `scripts/validation/test_company_facts_schema.py` | `B249C9B3D04E2001EF9BAF390724D5F072B57EBAF4711D6361D1AC631FDE878D` |
| `output/research/contract-review-reference-reconciliation-2026-10-04/entity-contact.pre-typed-shape.md` | `B495D90C7F4E5061A95F7BDCB6BF53D25F83B795F7DEBD4CE4E4764DED375720` |
| `docs/phase-1-architecture/contracts/DATA_CONTRACT.md` | `46ACFEA99E0D4DB91FB84603699E577100FFFA79CA34F242D658A41DEAB8FB33` |
| `specs/004-design-services-content/spec.md` | `64A357200EAF46B8AAA710D67B2EB05415377F924EC6C1441D0F0731D51D06C7` |
| `AGENTS.md` | `55405CB02A96D05F7F6D68E56A588D743F83877FB2691A5A9F2C736126ADBCC5` |
| `.specify/memory/constitution.md` | `33EC0BB02B0D0D9A55D0971589BD19F7242F5D56DA130F8F496BC1D31A8B5D23` |
| `DECISIONS.md` | `1D53A14AC3347EBEEFEEB728E03862B09DE111B748CEF4E48D5F4CA19141B6D8` |
| `PROJECT.md` | `A483BD2713FE420322772AB7FB07C848AAF103088697C05AB91F35D2E5EA1461` |
| `PROJECT_STATE.yaml` | `DE4791739336EBD3C2A06549CD154BD0E9B8B6A022ECC23458FFC7EA3515C1B3` |
| `docs/software-definition/README.md` | `85AC575C0CF26946E80C2B63AE64B020ACDFE76A530647CD2F798EE8BE16A100` |
| `TASKS.md` | `023F892B3D9620951394BB5E0663D2E850B2B29F7B5377FC2BFC36EED16B7D00` |

## Finding

**CF-SHAPE-LOW-001 — Low — actual certificate validity reused in a synthetic fixture.** `scripts/validation/test_company_facts_schema.py:23` repeats the founder-supplied validity-month pair recorded at `DECISIONS.md:848`–`849`. The other identity/jurisdiction/identifier/contact facts are fictional. The commissioned boundary expressly prohibits repeating real business/legal facts in fixtures; the month pair should also be wholly fictional. Replace that positive fixture pair with unrelated, ordered synthetic months, retaining the month-precision and invalid-input expectations. No production schema, business facts, public disclosure or application change is required. This is fixture isolation, not a privacy incident or legal opinion.

## Shape and authority assessment

- `DATA_CONTRACT.md:60`–`65`, FCT-06 at `specs/004-design-services-content/spec.md:101`, scenario 6 at `200`–`203` and D-070 support typed reviewed revisions, exact string identifiers, source month precision and coherent eligible publication. The new schema proposes a prepared content subdocument, not an editing/publication/auth transport. Required legal-name/jurisdiction fields and labelled optional registration/address/contact fields invent no regulator identifier grammar, numeric conversion, expiry inferred from suffix or verification API.
- `company-facts.schema.json:7` and the nested object definitions close unknown properties at every object level. Approval, activation, staff ownership, evidence/reviewer identity and provider secrets cannot be introduced as content extensions. This is a shape restriction, not permission enforcement; external provenance/workflow records and actual role/revision denial remain required.
- `06-entity-and-public-contact.md:99`–`121` accurately distinguishes explicit month labels from timestamp/day boundaries, treats absent validity as unknown and defers different source precision to a reviewed extension. Contact strings do not verify email syntax, ownership, delivery or monitoring; optional fields do not require public disclosure or activate aliases. Alias ownership stays undecided.
- The draft explicitly holds chronological ordering, blank-only rejection, source verification, disclosure review, resource/transport bounds, safe rendering, provenance, applicable policies and actual publication projections. No unsupported generic maximum length, regulator-specific format or production readiness is silently imposed. Validating a value cannot invalidate/approve revisions, change active derivatives, establish contact operation or publish registration/address facts.

## Focused artifact evidence

Executed `C:/Python314/python.exe -B scripts/validation/test_company_facts_schema.py`: one unittest with 13 mutation subtests passed. Independently checked the Draft 2020-12 schema and exercised a wholly fictional value plus 13 boundary candidates covering required fields, type/empty-string rejection and closed root/registration/PSEB/validity/contact objects; all expected invalid shapes were rejected. Independent probes confirmed blank-only text, reversed month labels and malformed email syntax still pass **shape** validation, consistently with the explicitly held semantic checks. Interpreter observed Python 3.14.5 and installed jsonschema 4.23.0; these observations do not select production versions. No dependency installation was performed.

These are schema/validator artifact tests only. They are not tests of actual admin requests, persistence, editing permissions, review invalidation, publication coherence, disclosure compliance or public HTML/World/AI output. The fixtures' string roundtrip proves synthetic value preservation, not implementation-level source fidelity. No real business identifiers, address or email were added to independent probes or this receipt.

## Scope limits

Review covers only the new typed-proposal section, its schema and focused fixture script, with the named authority/supporting records. Earlier entity/contact legal findings and public facts remain held and are not newly authenticated or cleared. The draft still needs correction verification and integrated acceptance; complete Phase 1, production implementation/public API/admin enforcement, field/resource policies and publication gates remain separate. Only this new receipt was written; producer inputs were preserved, with no credentials, installs, network/external writes, commits or application changes.

## Correction 1 verification — superseding bounded disposition

Date: 2026-10-04. Verdict: **PASS** for the corrected shape proposal and fixture scope. **CF-SHAPE-LOW-001 is closed.** This supersedes the initial candidate's REVISE disposition only for this exact correction; the original review text and findings above remain history. One correction cycle used.

Independently inspected the entire preserved-script/current-script diff: only the positive validity pair at `scripts/validation/test_company_facts_schema.py:23` changed to wholly fictional, ordered month labels. The schema, contact proposal, fixture identifiers and all test expectations remain unchanged. Reran `C:/Python314/python.exe -B scripts/validation/test_company_facts_schema.py`: one unittest with 13 mutation subtests passed.

| Correction input | Independently computed SHA-256 |
|---|---|
| `scripts/validation/test_company_facts_schema.py` | `D872C5C9BEF6D1410C2BE8BE77177FFF63BCC4CB9C2E37BAD72487FE5E679CA9` |
| `output/research/contract-review-reference-reconciliation-2026-10-04/test_company_facts_schema.pre-fictional-month-fix.py` | `B249C9B3D04E2001EF9BAF390724D5F072B57EBAF4711D6361D1AC631FDE878D` |
| `docs/phase-1-architecture/contracts/company-facts.schema.json` | `4C3162F19483563B88C1EF6BEED4055A7ACB9C608A947B0707D9AAA39E9F0695` |
| `docs/software-definition/06-entity-and-public-contact.md` | `26B071152F9FABF6608C81FFEA3E8973EED8DB81D9664585350FE0FB5DB8EF91` |
| Initial review receipt before this append | `1187B0496BCD7255B629D8C1BE752EF154C3AF76D37C8F9B574A32DA1799D7F7` |

No new actionable finding. All original scope limits remain: schema/artifact PASS is not actual admin/backend permission enforcement, semantic fact verification, disclosure/legal clearance, publication correctness, integrated Phase 1 acceptance or production implementation permission. Only this receipt was appended; no producer inputs or application files were edited by the reviewer.
