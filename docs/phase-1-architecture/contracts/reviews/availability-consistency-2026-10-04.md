# Independent availability consistency review — 2026-10-04

Disposition: **PASS, initial candidate**, for the bounded proposed protocol. Independent reviewer: `/root/review_publication_contract`. No actionable finding, producer revision or closure cycle was required. Only this new receipt was written; producer documents and older reviews remain unchanged.

Scope: AVAILABILITY_CONSISTENCY.md against D-065's durable/ephemeral authority boundaries, FR-009, AF-02/SOF-01A/B, DE-22/DE-18/DE-19, action/object authorization, catalogue and logical field/classification boundaries. Authority inputs were inspected in that scope; whole-file hashes below do not imply a renewed exhaustive review of historical content.

## Assessment

The reference guard preserves current PostgreSQL authority for each positive public availability and new handoff eligibility decision. A derived Redis/Teams signal cannot grant availability, renew expiry or override a withdrawn/revoked intent. The protocol binds both setting identity and revision to the current approved scope, covering replacement with a reused revision rather than relying on revision alone. It requires current identity/action/object authority and policy eligibility; administrator status or an unmapped delegate supplies no extra grant.

Receipt, durable acceptance, verified live offer and human acceptance remain distinct outcomes. Unknown commit/admission acknowledgements cannot be called rollback or success, and timeout/cancellation/lease expiry cannot prove a late command is impossible. Relevant authorized unresolved negative effects must be visible to the guard; uncertain admission requires proof of their absence before offering live help. The document expressly treats that durable admission/reconciliation and late-command fencing proof as a prerequisite, rather than claiming that a row lock or an undocumented cross-store transaction already provides it. Unauthorized pending requests cannot gain suppression authority.

SOF-01A's available-after-durable-accept outcome remains a compound success requiring current eligibility and fresh matching projection evidence, consistent with the data/field constraints. SOF-01B removes the initiating interface's live claim immediately while global confirmed withdrawal requires the durable guard; neither local presentation nor a Redis delete is presented as global proof.

The delayed-on-after-off, eviction/restart, restoration, stale Teams, ABA replacement and external revocation cases are covered as required future boundary evidence. Every relevant authority participates in the decision guard; locking a declaration row alone is insufficient. Fresh decision-time expiry after waits, bounded effective validity and clock uncertainty are explicit obligations. Guarded decisions are distinguished from delivery-time revocation and other browsers' screens; measured in-flight/detection limits and cache behavior remain held, without a universal instant-suppression promise.

The proposal introduces no new public staff identity, visitor identity, ownership, grant, retention duration or selected account/provider. Private intent/operation/audit evidence remains private and subject to held retention/deletion/restore policy; the visitor-chat 90-day rule does not become an availability-history rule. Turning availability off cannot silently delete, cancel or confirm an existing conversation, handoff or booking. Consent, assignment and calendar-slot truth retain their separate authority.

[PostgreSQL 18 isolation](https://www.postgresql.org/docs/18/transaction-iso.html) and [locking](https://www.postgresql.org/docs/18/explicit-locking.html) support the stated waiting/updated-row and selected-row lock behavior; these mechanisms alone do not prove a multi-authority guard. [Date/time documentation](https://www.postgresql.org/docs/18/functions-datetime.html) distinguishes transaction-start timestamps from clock_timestamp's actual-time observation. [Redis transactions](https://redis.io/docs/latest/develop/using-commands/transactions/) support server-local isolation/CAS and command-error/rollback limits, not PostgreSQL/Redis atomic commitment. Primary pages were independently inspected; no runtime, isolation level, Redis command/key layout or platform version was selected by this review.

## Verification and limits

Four local references resolve; inspected logical records, public/private fields, roles and flows preserve the existing boundaries. These are artifact/source inspections only. No wording tests, live database writes, lock/clock/CAS experiments, application tests, services or dependency changes were performed. The conformance table describes required future actual-boundary evidence, not executed tests. Physical uniqueness/current binding, admission/fencing, signals/expiry thresholds, operational owners/grants, account capabilities, public wire/cache schemas and measured concurrent/load/restore/delivery behavior remain held. PASS does not establish runtime enforcement, integrated Phase 1/founder acceptance, production/design permission or closure of the broader QA revision exception.

## Exact inspected input SHA256

| Repository-relative input | SHA256 |
|---|---|
| `AGENTS.md` | `55405CB02A96D05F7F6D68E56A588D743F83877FB2691A5A9F2C736126ADBCC5` |
| `.specify/memory/constitution.md` | `33EC0BB02B0D0D9A55D0971589BD19F7242F5D56DA130F8F496BC1D31A8B5D23` |
| `DECISIONS.md` | `C843AE17EE0AA7B9E5DD0BE39595310B5B25C31BEA2B97ECE4E6EBD34C2DADBF` |
| `docs/phase-1-foundation/01-product-requirements.md` | `5B33D8BD87BDB3B093EF319DB3EA3BB64DEAEDDF2706F5D21505BFB66035AA39` |
| `docs/phase-1-ux-architecture/FLOWS.md` | `2169C1543D697E94548EBB4675EA815FA9E36955ADCB808FAF02C3F37107E14B` |
| `docs/phase-1-architecture/ARCHITECTURE.md` | `44717F73094E5FFAE24758C09CC710E3D0282B371C2FCE23D5098CF36CFB6363` |
| `docs/phase-1-architecture/contracts/AVAILABILITY_CONSISTENCY.md` | `6DA0086B9C6AC49C2464F73A61793D410C7E04C1AAEC8D83A328B377E5252A03` |
| `docs/phase-1-architecture/contracts/DATA_CONTRACT.md` | `33F581241825B08972E397ADBDD4F9E6DAE9735AD852E5811011F185F5841C13` |
| `docs/phase-1-architecture/contracts/data-entities.csv` | `EC55F41329D521C36014E8E77B863013A7C0A24A6917706767F59F9227525E64` |
| `docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md` | `73EA12C299CAE216461D6C02C1C5274A2A16F271AC18E8548053DEA824D51204` |
| `docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md` | `736A422316B7F8AED4DA96D9AD7B057D25D762CD3268D2686265598414E8FB8A` |
| `docs/phase-1-architecture/contracts/interface-catalog.csv` | `42018A3E5CC6C1EDF488C392B0349688A92B2CAB5A8F50E717F1BCA84A70A49C` |
| `docs/phase-1-architecture/contracts/process-fields.csv` | `5737B8F4BD47B90A5020AE8943CB2C7786582C605E14D97212B4334FFB26522A` |
| `docs/phase-1-architecture/contracts/data-classification.csv` | `4B163EEC086CB46CA98FABF692632D1778EE116CB014CDA179E5B4A2A5FD44C6` |
