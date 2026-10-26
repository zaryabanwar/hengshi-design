# Governed consultation lifecycle v1 — independent bounded review

Date: 2026-10-05. Verdict: **PASS for this proposal slice**. This is the first
independent review of `HANDOFF_LIFECYCLE.md`, not a model revision, implementation
acceptance, legal approval, or acceptance of the wider Phase 1 package.

No blocking contradiction or material unapproved choice was identified in the
reviewed definition. The document develops the existing AF-02/SOF-01 consultation
requirements and existing catalogue routes while explicitly holding decisions
that require later approval. The shared aggregate guard and uniqueness discussion
is a proposed design inference, not selection of a schema, isolation level,
dependency graph, or physical enforcement mechanism.

## Scope and review method

Reviewed the new proposal against frozen foundation, flow, data, security,
availability and interface authorities. Inspected current consent and assignment
guards, duplicate creation and ownership, uncertain operations, availability off,
revocation, delivery/reconnect, alert recovery, retention and media alternatives.
Read repository governance and current project authority/checkpoints before this
review. Existing approved requirements govern the verdict; the proposal cannot
grant itself approval.

Independently compared SHA-256 hashes and byte lengths of all eleven canonical
inputs with their frozen copies before reviewing them. Independently read the
primary PostgreSQL 18 and RFC 6455 documentation cited below. The producer's
Context7 query is recorded provenance, not an independently replayed query or
selected compatibility graph. No application, database, WebSocket, browser,
account, media or physical-device execution was performed for this review.

## Exact reviewed identities

Manifest: `output/research/handoff-lifecycle-2026-10-05/review-inputs.json`.
Its independently observed SHA-256 is
`8f571e7baf1b74682da9ceff7ecc5d55039493210926e11753b7bfcbbcdbbd82`.

Every frozen filename below is relative to
`output/research/handoff-lifecycle-2026-10-05/`. Each listed SHA-256 and byte length
was observed on both the canonical source and its frozen copy; all match the
manifest. These identities bound the verdict.

| Canonical source | Frozen filename | Bytes, each copy | SHA-256, each copy |
| --- | --- | ---: | --- |
| `AGENTS.md` | `AGENTS.md` | 7686 | `55405cb02a96d05f7f6d68e56a588d743f83877fb2691a5a9f2c736126adbcc5` |
| `.specify/memory/constitution.md` | `.specify__memory__constitution.md` | 16234 | `33ec0bb02b0d0d9a55d0971589bd19f7242f5d56da130f8f496bc1d31a8b5d23` |
| `docs/phase-1-foundation/01-product-requirements.md` | `docs__phase-1-foundation__01-product-requirements.md` | 66587 | `5b33d8bd87bdb3b093ef319db3ea3bb64deaeddf2706f5d21505bfb66035aa39` |
| `docs/phase-1-ux-architecture/FLOWS.md` | `docs__phase-1-ux-architecture__FLOWS.md` | 28453 | `2169c1543d697e94548ebb4675ea815fa9e36955adcb808faf02c3f37107e14b` |
| `docs/phase-1-architecture/contracts/DATA_CONTRACT.md` | `docs__phase-1-architecture__contracts__DATA_CONTRACT.md` | 14779 | `46acfea99e0d4db91fb84603699e577100fffa79ca34f242d658a41deab8fb33` |
| `docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md` | `docs__phase-1-architecture__contracts__SECURITY_PRIVACY_CONTRACT.md` | 24722 | `74ab420b5bec9f0aad72f59178f4ea7c626bd14edfa9d4ba02f3aa1dd0a1a254` |
| `docs/phase-1-architecture/contracts/AVAILABILITY_CONSISTENCY.md` | `docs__phase-1-architecture__contracts__AVAILABILITY_CONSISTENCY.md` | 14167 | `6da0086b9c6ac49c2464f73a61793d410c7e04c1aaec8d83a328b377e5252a03` |
| `docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md` | `docs__phase-1-architecture__contracts__INTERFACE_CATALOG.md` | 29527 | `1ed7ea4cd1fe7002848462a7a78e4525f457b60cf6a454d11878a74071c2d7d0` |
| `docs/phase-1-architecture/contracts/interface-catalog.csv` | `docs__phase-1-architecture__contracts__interface-catalog.csv` | 9367 | `42018a3e5cc6c1edf488c392b0349688a92b2cab5a8f50e717f1bca84a70a49c` |
| `docs/phase-1-architecture/contracts/process-fields.csv` | `docs__phase-1-architecture__contracts__process-fields.csv` | 71516 | `5737b8f4bd47b90a5020ae8943cb2c7786582c605e14d97212b4334ffb26522a` |
| `docs/phase-1-architecture/contracts/HANDOFF_LIFECYCLE.md` | `docs__phase-1-architecture__contracts__HANDOFF_LIFECYCLE.md` | 16323 | `2f6972361779ab6b36deeb17249e69f23b04c1468e765e66f504f9fc239f30ff` |

## Findings and authority reconciliation

No actionable REVISE finding was identified within the bounded scope.

1. **Existing process and honest states.** Proposal lines 9–28 and 32–68 retain
   the existing IFCHAT04, IFSTAFF06/10–15 routes and AF-02 lifecycle. Offer,
   durable request, assignment, acceptance, text establishment, delivery and
   external alert are separate facts. A socket handshake or Teams alert cannot
   manufacture acceptance, connection, reading, booking or a response promise.
   Alert failure does not roll back a known request. Refusal, unavailability and
   media failure retain the approved information/text/Book/Contact alternatives.
   This is consistent with FR-009–011, FR-016 and AF-02; no new visitor account,
   route, automatic backup assignment or service-level promise is introduced.

2. **Current consent, authority and one owner.** Lines 48–100 require current
   process/object, consent, assignment and authorization checks at the transition,
   rather than treating an earlier availability read or operation receipt as a
   grant. Different request identities cannot create two routable requests for
   the same governed binding; acceptance/reassignment must coordinate through
   durable ownership, not separate operator-local locks. SOF-01 and the existing
   staff catalogue already require scoped assignment and guarded acceptance.
   The proposal keeps exact grants, assignment policy and physical uniqueness
   design held, including the absent-row case. It does not permit queue readers
   to self-assign or infer an administrative grant.

3. **Unknown outcomes and late work.** Lines 72–100 bind retries to principal,
   process, target and unchanged action, preserve unresolved admission/commit,
   and require old uncertain effects to be resolved or fenced before conflicting
   newer transitions. No timeout, lease expiry, lost reply or alert result is
   treated as proof of rollback. Historical outcomes do not renew consent or
   current access. Atomic transition/outcome recording and independent recoverable
   alert intent fit DATA-010 and the catalogue's idempotent recovery requirements.
   The exact outbox, ordering and recovery proof remains an implementation gate.

4. **Off, reassignment and revocation.** Lines 104–131 distinguish unavailable
   for new routing/acceptance from ending an already accepted conversation.
   Existing conversations still require current process, assignment and consent.
   Reassignment invalidates older ownership generations and their queued/replayed
   delivery; old socket authentication does not authorize new actions. Withdrawal
   and ending require current checks, with unknown authority failing closed.
   The text acknowledges that already disclosed content cannot be recalled and
   holds the cross-system signal/drain/fence/acknowledgement mechanism. This
   preserves SECURITY_PRIVACY_CONTRACT and AVAILABILITY_CONSISTENCY without an
   unsupported instantaneous revocation guarantee or automatic owner replacement.

5. **Reconnect, event scope and media.** Lines 135–160 preserve separate visitor
   and staff directional event contracts, server-bound sender/assignment scope,
   and current replay authorization. Reconnect resumes the same valid process;
   it cannot recreate lost nonconsented ephemeral content, renew policy, or infer
   text delivery from transport success. Event acknowledgement boundaries and
   resource bounds are held. Text, ambience, old browser permission and staff
   acceptance do not imply microphone/camera consent. Separate media opt-in and
   applicable caption/transcript/description alternatives preserve AF-02's
   distinct media requirements; no provider or recording pathway is selected.

6. **Persistence and alert privacy.** Lines 164–182 prohibit retroactive durable
   capture of earlier ephemeral history; a new share must identify its included
   projection and purpose. If the required notice or policy is unapproved, durable
   request/transfer remains held while approved ephemeral help and Book remain.
   Outbox, replay, diagnostics, linkable references and alert metadata inherit
   mapped data restrictions. No transcript dumping into Teams, logs or analytics
   is allowed. The approved 90-day chat/brief/lead scope is not expanded to every
   handoff, consent proof, assignment, operation, alert or audit class. Ending,
   declining and acknowledgement neither reset expiry nor prove deletion.

## Independent primary-source check

Checked on 2026-10-05 against the cited versioned/standard pages, independently
of the producer's Context7 report:

- PostgreSQL documents selected-row locking, deadlock handling and consistent
  lock ordering. Such locks do not by themselves reserve a missing row or prove
  the whole ownership invariant. The proposal correctly labels its shared guard
  recommendation as an inference and holds exact enforcement.
  [PostgreSQL 18 explicit locking](https://www.postgresql.org/docs/18/explicit-locking.html)
- Read Committed can reevaluate a concurrent update's predicate. Stable snapshots
  alone do not enforce every business rule; serialization failures require retry
  of the transaction. The proposal neither selects an isolation level nor claims
  these observations establish compatibility or tested concurrency correctness.
  [PostgreSQL 18 transaction isolation](https://www.postgresql.org/docs/18/transaction-iso.html)
- Browser Origin checks, client authentication and frame/reassembled-message
  resource limits are separate concerns. Origin is not general client identity,
  and the protocol does not define current business authorization, durable
  operation outcomes or consultation ownership. The proposal adds these as
  project obligations rather than attributing them to the transport standard.
  [RFC 6455 sections 10.1–10.5](https://www.rfc-editor.org/rfc/rfc6455.html#section-10)

## Remaining gates and limits of PASS

The proposal's lines 186–206 correctly retain these unproven obligations:

- Approve exact request/event/status/error schemas, authorization grants and
  assignment, decline/reassignment and queue policies. Freeze current identity,
  revision, generation, uncertain-outcome and disclosure contracts before coding.
- Approve consent/projection and data-class mappings, expiry, deletion/restore,
  operation-history retention and any applicable exceptions. This review does
  not provide legal or retention approval.
- Prove actual transaction constraints, cross-authority availability/revocation
  coordination, fan-out/admission fencing, outbox and recovery. Exercise actual
  public boundaries for duplicate creation, concurrent ownership changes,
  withdrawal/off, unknown commits, late workers, old-owner delivery, ending and
  reconnect. Schema checks and mocked success do not establish these invariants.
- Approve numeric replay, queue, message/reassembly, work and retry limits; verify
  selected Microsoft/media account/API capabilities and independently resolve,
  test and lock the complete stable compatibility graph.
- Provide approved production screen references and verify browser journeys,
  accessible recovery, media alternatives and equivalent Quick Access, followed
  by the applicable physical-device, specialist and founder acceptance gates.

Producer link checks, documentation-server/browser availability and zero console
messages are separate producer observations. They were not independently rerun
here and do not prove consultation, privacy, concurrency, legal, accessibility or
runtime behavior. Hash/byte comparisons establish artifact identity only.

This review authored only this receipt. Canonical and frozen inputs were preserved;
no application, schema, model, asset, dependency, configuration, account, commit,
push or external activation was changed. PASS permits this bounded proposal to
proceed through its remaining governance gates; it does not approve implementation
or the wider definition package.
