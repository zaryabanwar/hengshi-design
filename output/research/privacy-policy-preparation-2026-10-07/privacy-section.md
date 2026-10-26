## EU privacy and retention policy proposal — 2026-10-07

Status: DOING. Prepared under [D-076](../../../DECISIONS.md#d-076--visitor-inactivity-eu-privacy-baseline-and-production-data-deferrals).
The founder delegates a reasoned EU/GDPR-based definition. This section fills
previously unmapped policy choices for independent legal/security review and
integrated Phase 1 acceptance; new periods/bases below are proposals, not adopted
law, existing enforcement or permission to process live personal data. It is the
controlling proposed policy detail; the classification matrix still identifies
classes and restrictions, rather than silently adopting these unreviewed values.
Earlier review receipts cover their frozen inputs only.

### Processing purposes and lawful-basis recommendation

Hengshi's Pakistan legal entity is the proposed controller for website enquiries,
consultation, scheduling and staff operations. Cloud, AI, calendar and email roles
must be assessed individually; do not call every external service a processor.
Europe-first targeting requires a territorial-scope and, where applicable, EEA
representative assessment before live EU collection. EU hosting alone does not
settle the status of processing or international access. This is legal definition
work; provider/cost selection and buying representation remain deferred.

Use an inventory of purposes, data fields, subjects, recipients, lawful basis,
retention, transfer/access locations and rights routes. Select the basis before
collection. Proposed mappings:

| Processing purpose | Proposed basis and limitation |
|---|---|
| Optional saved chat, retained brief/lead and selected human-context transfer | Purpose-specific consent for the optional retention/transfer. Distinct affirmative actions; no preselection, implied consent from entering World, bundled marketing, or disadvantage to semantic browsing/Contact/Book. |
| Visitor-requested ephemeral guidance and discovery scheduling | Contract/pre-contract necessity only where the individual is the prospective contracting party and processing is actually necessary. For a corporate representative's business enquiry, assess legitimate interests with documented purpose, necessity and rights balancing; do not pretend the representative is party to the company's contract. |
| Staff authentication, authoring permissions, controlled availability and security events | Document necessary, proportionate legitimate interests and applicable employment/contract duties separately. Employee consent is not a default substitute for those assessments. Public portraits/bios need their own approved publication basis and revocation handling. |
| Minimal consent, rights-handling and accountability evidence | Identify the specific applicable accountability/legal duty and necessary fields. It does not authorize retaining the underlying chat as proof. |
| Anonymous measurement | Prefer genuinely non-identifying first-party counts. Assess any identifiable collection and terminal-device access separately; an aggregate destination does not make identifiable intake anonymous. |

Consent withdrawal stops its dependent processing/transfer and starts scoped
erasure or restriction as applicable. Do not silently replace withdrawn consent
with legitimate interests to keep the same optional processing alive. Separate
valid legal preservation, if required, must be documented and disclosed. Notice
acceptance is not consent to every purpose, and absence of a durable chat copy
does not exempt transient personal-data processing from legal assessment.

The recommendation follows [EDPB lawful-processing guidance](https://www.edpb.europa.eu/sme/be-compliant/process-personal-data-lawfully_en)
and the [Commission's lawful-basis explanation](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/legal-grounds-processing-data_en).
Those sources establish conditions, not automatic clearance for Hengshi's proposed
mappings. No launch marketing, tracking, training or new sensitive-data collection
is introduced by this proposal; existing refusal/provider restrictions remain.

### Proposed retention schedule and immutable clocks

The accepted DATA-005 90-day rule applies only to consented chat/derived traces
and brief/lead. GDPR does not prescribe a universal 90-day schedule. Each new
duration below is a purpose-based engineering recommendation for review, with
earlier withdrawal, loss of purpose, rights or legal duties taking precedence.
The [EDPB storage-limitation guidance](https://www.edpb.europa.eu/sme/find-practical-info/faq_en?page=1)
requires necessity-based retention and deletion/anonymisation when no longer needed.

| Existing record class / subpurpose | Proposed anchor, period and reason |
|---|---|
| `published_content` | Serve only currently eligible approved releases. Keep non-personal authored history for revision/rollback needs; identifiable portraits, quotes or other personal content require their own rights/purpose expiry. Old release bytes do not authorize renewed public serving. |
| `world_position` | Browser-runtime session only; clear on World exit. No durable movement history or restored tracking profile. |
| `nonconsented_chat` | Ephemeral only; remove at authoritative conversation End/idle expiry or earlier purpose revocation. D-076's 30-minute inactivity policy has no absolute conversation age; per-message buffers remain finite. Provider copies need separately verified compatible handling. |
| `consented_chat_and_derived_traces` | Each legitimately admitted retained message expires 90 days after its first durable admission. A derived trace inherits the earliest expiry of its personal source records; copying/reprocessing does not establish a new anchor. An active conversation can continue while old records age out; there is no hidden 90-day access cutoff or automatic durable transcript recovery. |
| `brief_and_lead` | Expire 90 days after first durable creation for the specific accepted purpose. Edits, reminders, assignment and resume do not reset it. Personal source text copied from another class retains its earlier expiry. An independently approved active-client/legal-record policy is required before moving necessary fields to that separate purpose; no blanket exception. |
| `booking_and_calendar` | Propose 90 days after the final known meeting completion or cancellation for necessary scheduling/reconciliation metadata. Keep the current booking while genuinely unresolved; investigate/review continuing necessity every 30 days rather than silently clearing uncertainty. Prove provider deletion separately. Verification secrets/proofs follow their own short security lifetimes and are never kept as meeting history. |
| `consent_proof` | Keep minimal purpose/notice/revision/decision/time evidence while dependent processing remains authorized or mapped retained records remain live, then through the maximum recoverable-copy window below. Withdrawn consent cannot authorize processing during that evidence period. Prove necessity for any separate dispute hold; no identifying proof retained forever. |
| `staff_identity_and_approval` | Keep minimal current eligibility/binding while authorized. Propose removing obsolete direct roster/profile fields within 30 days of access removal, once reconciliation is known. Existing release-review accountability belongs to separately mapped minimal audit evidence; employment/payroll records and deletion of the Microsoft account are outside this website's authority. |
| `availability_and_handoff` | Public availability projection expires with its authoritative intent/session/scope. Propose clearing settled expired intent rows within 24 hours; unresolved operations retain their reservations/evidence until known settlement and reviewed necessary disposition. Shared handoff content inherits the source record's expiry; no separate longer transcript. |
| `deidentified_provider_payload` | No application retention beyond the admitted operation. Transfer only after actual de-identification and approved entitlement/provider handling; no assumption that vendor storage/training is disabled. |
| `analytics_aggregates` | Propose 13 months for demonstrably non-identifying monthly totals to compare one annual cycle. Do not persist raw personal events while waiting to aggregate, export small identifiable groups, or introduce terminal-device tracking. Exact aggregation/small-group thresholds and any necessary consent remain for review. |
| `audit_and_operational_copies` | Propose 30 days from event for redacted ordinary operational logs and 90 days for minimal security/authorization events, to support diagnosis and incident investigation. No bodies, tokens, chat, email or raw sensitive URLs. A rights-case outcome may retain minimal accountability evidence for 12 months after closure; relevant incident/legal preservation needs a separate documented review date and necessity, not an unlimited archive. |
| `deletion_evidence_and_tombstones` | Keep the minimum scoped suppression key until every recoverable mapped copy has expired or been verified inaccessible, then erase the linkable key after verified cleanup. It is restricted personal data when linkable, even if hashed; a nonidentifying completion count need not retain identity. |
| `secret_or_credential` | Use only the approved secret/session facility and current credential lifetime. Revoke and rotate under the reviewed identity policy; no secret in repository, logs, evidence, training, ordinary records or backups of conversation data. |
| `defense_sensitive` | No launch collection, retention, indexing or provider transfer. Refuse without echoing/logging the payload. |

Propose a **maximum 30-day recoverable-copy window** for backups containing these
personal records. This is a privacy/recovery design constraint for review, not a
hosting choice, a purchased service or proof of restore readiness. Ordinary
application access stops at expiry; residual protected backup copies are isolated
from use, naturally expire within that window, and cannot serve until expiry and
deletion suppression have been applied. Provider copies need an actual verified
bound; an unknown external window cannot be described as 30 days or deleted.

All timestamps are server-issued immutable UTC instants under the approved clock
policy. A policy revision cannot silently move a record's original expiry forward.
Copied data retains its origin and applicable earlier boundary. A justified legal
hold identifies exact records, basis, restricted purpose, approver and finite next
review date; it stops ordinary use and is released when no longer necessary.
Successful row deletion is not evidence of provider/backup completion. If an
unsettled reservation still references expired personal content, deny disclosure
and retain only the minimum restricted reconciliation state that has a reviewed
basis; settlement logic cannot grant indefinite content storage.

### Rights, transparency, incidents and provider gates

Provide a concise layered notice before relevant collection: operator/controller,
purposes and bases, necessary/optional fields, recipients, periods/criteria, rights,
complaint route, transfers and contact. Registration identifiers/address publication
remain founder-deferred; mandatory identity/contact disclosures still need eligible
reviewed content before live collection. Do not advertise unverified aliases.
Dedicated privacy/security ownership remains undecided for now, rather than a
Phase 1 request to assign a person or create a mailbox.

Rights intake must record receipt time, verify control proportionately, scope the
data and respond without undue delay, ordinarily within one calendar month.
An allowed complex-request extension needs a recorded reason and notice within
that first month; do not confuse it with 30 days or an automatic delay. Support
access, correction, erasure, restriction, objection and portability where applicable.
Do not demand identity documents by default, reveal another process to a requester,
recreate expired anonymous history, or refuse all rights merely because visitors
have no accounts. Preserve only necessary case/outcome evidence with the mapped
subpurpose above. [Commission rights guidance](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/dealing-requests-individuals_en)
and [EDPB rights guidance](https://www.edpb.europa.eu/sme/be-compliant/respect-individuals-rights_en)
support these duties; route/verification mechanisms still require definition.

Maintain breach assessment and records, containment and controller/processor
escalation. Notify the competent authority without undue delay and, where feasible,
within 72 hours of awareness unless unlikely to risk individuals; communicate to
affected people when the required high-risk threshold applies. Incomplete facts
do not authorize waiting for the entire investigation. This is a legal-response
obligation, not an advertised sales/support SLA. See [EDPB breach guidance](https://www.edpb.europa.eu/sme/assess-the-risks/data-breaches_en).

Document vendors' actual roles, agreements, subprocessor/support/access locations,
training/telemetry/retention, deletion and recoverable copies before transfer.
Assess EEA/non-EEA processing and remote access against territorial/transfer rules;
use an applicable reviewed transfer mechanism and safeguards, not a checkbox or
presumed adequacy. Approved Azure-Europe private-AI restrictions remain unchanged;
deferred Azure/AWS hosting selection cannot loosen them. The [Commission's transfer
guidance](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/rules-international-data-transfers_en)
and [scope/transfer examples](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/new-standard-contractual-clauses-questions-and-answers-overview_en)
inform the assessment; no provider contract or representative is selected here.

Inventory cookies/storage separately from personal-data bases. Assess narrowly
necessary requested-service/session security storage before using an exemption;
optional tracking cannot be labelled essential or enabled by World entry. Keep
its information separate from any optional consent request. See [EDPB terminal-device
consent guidance](https://www.edpb.europa.eu/system/files/2023-12/edpb_letter_out20230098_feedback_on_cookie_pledge_draft_principles_en.pdf).

### Definition acceptance and later enforcement evidence

Independent legal/security review must assess applicability, the proposed bases,
necessity of each new period/anchor, consent evidence, backup/suppression formula,
rights/incident routes and transfer/representative obligations. Bind accepted
policy IDs to exact record-purpose classes and notice versions before implementation;
unknown mappings deny the affected collection/transfer. Founder acceptance is of
the integrated reviewed definition, not another request to choose arbitrary periods.

Later tests must exercise real collection/persistence/provider and deletion/restore
boundaries: refusal and withdrawal, immutable clocks/copies, old-message expiry in
an active chat, booking terminal/unknown outcomes, unauthorized rights disclosure,
late provider responses, residual backup suppression and deletion completion truth.
Schema/prose checks cannot prove those outcomes or legal compliance. Use synthetic
non-sensitive local data under D-076; no production personal data or outbound action
is authorized by this draft.
