# Availability public-read HTTP/body review — v1

Date: 2026-10-04. Verdict: **REVISE** for AVAILABILITY-MED-001 below, bounded proposed GET wire/body definition and artifact evidence. Initial independent review; zero correction cycles used. Public disclosure/timing policy and integrated acceptance remain held. No public handler, staff operation, account capability, provider or production implementation is approved by this receipt.

## Exact reviewed repository inputs

SHA-256 values independently computed; all three commissioned candidate identities match. Supporting records are reviewed only for this proposal's authority and constraints, not newly accepted as complete packages.

| Input | SHA-256 |
|---|---|
| `docs/phase-1-architecture/contracts/AVAILABILITY_READ_HTTP.md` | `B3022E5E634A3C16E353020B3D1C51A8A6F663A845FB47FA7BB7948293020B04` |
| `docs/phase-1-architecture/contracts/availability-read.schema.json` | `6E8599D428A7219D6A31113648133AB51C2050D86FD115F5B8F74EADBD032638` |
| `scripts/validation/test_availability_read_schema.py` | `D16DA8A0DABE712251B9D93514AD8763FA83FF9BFF2D35CD040E2F75C7600461` |
| `docs/phase-1-architecture/contracts/AVAILABILITY_CONSISTENCY.md` | `6DA0086B9C6AC49C2464F73A61793D410C7E04C1AAEC8D83A328B377E5252A03` |
| `docs/phase-1-architecture/contracts/DATA_CONTRACT.md` | `46ACFEA99E0D4DB91FB84603699E577100FFFA79CA34F242D658A41DEAB8FB33` |
| `docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md` | `73EA12C299CAE216461D6C02C1C5274A2A16F271AC18E8548053DEA824D51204` |
| `docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md` | `E0F1EC0BE89C87049AE5B243DD7CF7B92F5331CE380F87AA40BAFDB2F2687388` |
| `docs/phase-1-architecture/contracts/interface-catalog.csv` | `42018A3E5CC6C1EDF488C392B0349688A92B2CAB5A8F50E717F1BCA84A70A49C` |
| `docs/phase-1-architecture/contracts/process-fields.csv` | `5737B8F4BD47B90A5020AE8943CB2C7786582C605E14D97212B4334FFB26522A` |
| `docs/phase-1-foundation/01-product-requirements.md` | `5B33D8BD87BDB3B093EF319DB3EA3BB64DEAEDDF2706F5D21505BFB66035AA39` |
| `docs/phase-1-foundation/06-canonical-route-inventory.json` | `41B750B5493A70A43344CA608084E6ADCE04B82A768969832026FB50F6B59081` |
| `docs/phase-1-ux-architecture/FLOWS.md` | `2169C1543D697E94548EBB4675EA815FA9E36955ADCB808FAF02C3F37107E14B` |
| `AGENTS.md` | `55405CB02A96D05F7F6D68E56A588D743F83877FB2691A5A9F2C736126ADBCC5` |
| `.specify/memory/constitution.md` | `33EC0BB02B0D0D9A55D0971589BD19F7242F5D56DA130F8F496BC1D31A8B5D23` |
| `docs/phase-1-architecture/contracts/PUBLICATION_READ_HTTP.md` — strict consumer-decoding context only | `A383350B1ED9301EAE322B617E95055FC2731DB0C877E2F67C8F60FCFB50D3A0` |

## Authority, scope and projection

- FR-009 at `01-product-requirements.md:137`, AF-02 at `FLOWS.md:65`–`84` and SOF-01A/B at `315`–`316` require explicit staff intent, suppressive-only Teams evidence and truthful recovery. `AVAILABILITY_READ_HTTP.md:60`–`85` retains the consistency protocol's current PostgreSQL authority, exact intent identity/revision, expiry, fresh suppression, pending-negative and guarded-decision requirements. A durable declaration, Teams presence or Redis value alone cannot make a live offer.
- `available` means verified at the server decision point, not reservation, accepted handoff, appointment or response promise. `unavailable` means no verified live offer after public eligibility is established; it does not claim every employee is offline. Uncertain public eligibility yields a safe service error, not guessed retirement/404 or a normal successful result. Existing conversation/booking truth is preserved.
- All five proposed department IDs and paths match the existing canonical `service_wing` records. Those records explicitly retain pending publication and inactive-release statuses; the proposal grants no activation from membership in the schema enum. Selector validation rejects extra decoding/normalization, arbitrary/held inventory and private-existence disclosures. Anonymous reads create no session and credentials do not broaden the public projection.
- The closed success/error variants exclude private staff identity, intent setting/revision, Teams state, queue/calendar, reasons, provider diagnostics and activation authority. The proposed effective `expires_at` is explicitly distinct from raw private declaration expiry and cannot exceed any applicable bound. Its calculation, disclosure approval, lifetime/clock/resource policy and operation permissions remain held at `AVAILABILITY_READ_HTTP.md:68`–`81` and `156`–`161`; no positive result is authorized before those prerequisites.

## HTTP and client obligations

The conditional rules at `AVAILABILITY_READ_HTTP.md:108`–`116` correspond to [RFC 9110 §13](https://www.rfc-editor.org/rfc/rfc9110.html#section-13): evaluate normal eligibility/error checks first; preserve precondition precedence; without selected validators, specific If-Match tags cannot match, while wildcard matching depends on an existing permitted representation. If-None-Match * can yield a bodyless 304 even for an unavailable-state representation. Missing modification dates justify ignoring date preconditions. This GET proposal does not permit 304 to prove current live assistance; the client requires an unconditional matching 200. Actual syntax, precedence and body/header enforcement still require HTTP tests.

`Cache-Control: no-store` and controlled-layer non-reuse are consistent with [RFC 9111 §5.2.2.5](https://www.rfc-editor.org/rfc/rfc9111.html#section-5.2.2.5), without treating it as reliable privacy or instant screen revocation. The proposal requires current-attempt/department matching, suppression of superseded/out-of-order responses, expiry and earlier known invalidation, transit/clock/background/history safeguards, no anchor extension and retained Book/Contact recovery. It does not promise zero in-flight revocation delay or pick timing numbers. HEAD/OPTIONS/CORS, edge errors and transport/rate/resource integration remain separate obligations, not silently implemented.

## Focused schema evidence

Executed `C:/Python314/python.exe -B scripts/validation/test_availability_read_schema.py`: **two schema-tooling tests pass**. Fixtures use synthetic values and fixed proposal oracles, not enumerated implementation-generated expectations. No database, HTTP, Redis, Teams or staff-operation boundary ran.

Independent in-memory checks exercised available/unavailable bodies for all five canonical keys, all five fixed error variants and private-diagnostic exclusion, missing required fields and invalid state types. Nine invalid UTC instants were rejected, including a non-leap calendar date, invalid clock fields, leap seconds, year zero, lowercase separators, offsets and trailing controls. A calendar-valid leap date passed. A well-formed expired instant still passes shape validation, correctly demonstrating that the schema cannot prove effective validity.

The mandatory date-time checker was independently removed in memory: the fixture's setup failed closed. The registered calendar checker rejects an impossible date. The fixture supplies FormatChecker explicitly rather than relying on format annotation alone. Primary [validator documentation](https://python-jsonschema.readthedocs.io/en/stable/validate/) and [RFC 3339 §5.6](https://www.rfc-editor.org/rfc/rfc3339.html#section-5.6) were checked 2026-10-04. This intentionally narrower UTC profile uses normal seconds and uppercase T/Z; it does not assert support for every RFC 3339 variant.

Observed installed Python 3.14.5, jsonschema 4.23.0 and rfc3339-validator 0.1.4. Inspected exact installed FormatChecker.check behavior for the unregistered-format pass-through limit; `C:/Python314/Lib/site-packages/jsonschema/_format.py` SHA-256 is `17F300E76224AE1388C43A83F31FB4D5B1F7EE61B99E1D24C8DAD65122ED59BF`. The current primary documentation identifies jsonschema 4.26.0; it was not substituted for the installed execution behavior or selected as the production graph. No installation or version change occurred.

## Findings and retained obligations

**AVAILABILITY-MED-001 — Medium — strict wire-JSON decoding is not specified before the positive decision.** `AVAILABILITY_READ_HTTP.md:50`–`52` defines UTF-8 JSON and a closed shape; `89`–`93` clears malformed responses, but neither explicitly rejects duplicate decoded member names or invalid Unicode before schema use. A schema validates the decoded object and cannot see discarded duplicate members. Independently demonstrated with wholly synthetic raw JSON: two `availability` members, first unavailable and then available, are collapsed by ordinary Python `json.loads` to the latter; that object passes this schema. This is a parser/schema illustration, not a discovered application exploit or runtime test.

The existing publication-read consumer contract at `PUBLICATION_READ_HTTP.md:174`–`176` explicitly rejects duplicate keys and invalid Unicode before accepting its envelope, but the new presence proposal does not incorporate an equivalent requirement. [RFC 8259 §4 and §8](https://www.rfc-editor.org/rfc/rfc8259.html#section-4) describes duplicate-name and unpaired-surrogate interoperability hazards; an application-specific strict acceptance profile is appropriate here. Add the explicit presence producer/consumer requirement: valid UTF-8 JSON, reject duplicate decoded member names at every object level and invalid Unicode/unpaired surrogates before schema validation, never accept a last-value-wins replacement as live proof, and clear the live offer with existing recovery on rejection. Include raw-response cases in later actual HTTP/client tests. This needs a definition correction only, not a new parser/helper, install, actual handler or numeric resource limit. The current body fixtures correctly remain schema-tooling evidence.

No separate selector blocker is raised: the five positive keys are exact and unsupported/held departments cannot activate; generic malformed edge rejection permits 400/404. A more detailed unknown-selector grammar and shared resource limits still need integration definition, but no numeric cap or broadened key namespace is invented by this review.

Schema tests establish closed body correlation/calendar checking only, not HTTP statuses/headers, strict wire decoding, conditional handling, public disclosure rights, actual current-authority/clock enforcement, database/projection consistency, permission denial, truthful aggregation, provider capability, durable admission/fencing, restoration or browser stale/reordering correctness.

The later actual-boundary cases listed at `AVAILABILITY_READ_HTTP.md:142`–`161` remain required, with the approved timing/disclosure/grants/resource inputs and integrated Phase 1 acceptance. No older consistency/data/security review is extended or replaced. Original company-facts/provider-task reviews remain separate. Only this receipt was written; no producer edits, service/account mutations, Figma calls, installs, credentials, commits or deployments occurred.

Initial-review finalization note: the same review's provisional receipt draft (`6036D53DC0349B28CBB79B57C417A39C864B78A7101128734C8A2BEC7DF5E4D7`) reported PASS before the final raw-decoding check identified the finding above. No producer correction or PASS integration occurred in between. This finalized initial REVISE disposition controls; all three candidate identities are unchanged and zero correction cycles have been used.


## Correction 1 verification — superseding bounded PASS

Verified 2026-10-04. **PASS for this definition-only correction; AVAILABILITY-MED-001 is closed.** One correction cycle has been used. The finalized initial REVISE above remains history; this disposition applies only to the exact corrected HTTP proposal and unchanged schema/fixture identities below.

| Input | Independently verified SHA-256 |
| --- | --- |
| `docs/phase-1-architecture/contracts/AVAILABILITY_READ_HTTP.md` | `EB20C8AA66D0A489EC33AE3364CDF4D53E294826D3E8F3009B0018F4D744D583` |
| `output/research/contract-review-reference-reconciliation-2026-10-04/AVAILABILITY_READ_HTTP.pre-strict-decoding.md` | `B3022E5E634A3C16E353020B3D1C51A8A6F663A845FB47FA7BB7948293020B04` |
| `docs/phase-1-architecture/contracts/availability-read.schema.json` | `6E8599D428A7219D6A31113648133AB51C2050D86FD115F5B8F74EADBD032638` |
| `scripts/validation/test_availability_read_schema.py` | `D16DA8A0DABE712251B9D93514AD8763FA83FF9BFF2D35CD040E2F75C7600461` |
| Initial finalized review bytes (preserved prefix) | `0CE12B0CA3FCB7ADAB8B5D5E4248083242B1A25568C4F3C651A0A3561A29628E` |

Inspected the complete preimage/current diff. Its three hunks add the strict producer/consumer wire acceptance profile, later raw HTTP/client cases, and RFC 8259 supporting context. No unrelated change was found. Producers must serialize unique member names and valid Unicode/UTF-8. Consumers must reject malformed UTF-8/JSON, duplicate decoded member names at every depth including escape-equivalent names, and invalid Unicode scalar sequences/unpaired surrogates before schema use. Replacement decoding and last-value-wins collapse cannot establish availability. Failure clears the live offer while retaining Book/Contact recovery; neither a partial value nor an earlier positive response becomes fresh proof.

The correction explicitly leaves the strict-decoding mechanism and approved raw-response/resource bounds as implementation prerequisites. The later cases require observing raw rejection and client clearing rather than claiming the existing shape fixtures already exercise them. RFC 8259 supports the documented interoperability risks; the stronger rejection policy is accurately identified as a Hengshi requirement, not a JSON Schema capability.

The schema and fixture script are byte-identical to the initial reviewed inputs. No tests were rerun for this prose-only correction and no brittle phrase assertions were added. The independently executed two schema-tooling tests and in-memory diagnostics reported above retain their original scope. The producer's separate seven-family artifact run is not claimed as a new independent run here.

No additional actionable finding is raised within this correction. Public expiry disclosure, timing/clock rules, resource limits, grants, integrated Phase 1 acceptance and actual handler/client tests remain held or required as previously stated. This PASS neither implements nor proves strict decoding, HTTP/precondition behavior, database/projection/current-authority enforcement, live availability, stale/reordered client handling, security, accessibility, operational readiness, provider selection or production acceptance. Prior reviews and protected application evidence retain their scope. Only this receipt was appended; no producer, schema, fixture, application, service, credential, provider, install, commit or deployment change was made by this reviewer.
