## Incident assessment, escalation and recovery — v1

Status: DOING. Phase 1 engineering definition, 2026-10-09, under D-076 and
SEC/DATA requirements; adoption and integrated acceptance remain pending. It
refines the existing breach obligation without selecting an account, notification
service, endpoint, new role or cloud. Alias owners remain deliberately undecided.

### Detection, awareness and responsibility

An alert or security report starts prompt restricted triage, even when incomplete.
Record the first observation/receipt, the evidence-supported breach-awareness
instant, and the affected interruption separately. Awareness uses reasonable
certainty that personal data were compromised; it cannot wait for complete
forensics, management approval or proof of exfiltration. Assess unauthorized
disclosure/access, alteration and destruction/loss of access. False alarms may
close with reasons; uncertainty requires continued assessment, not a no-risk label.
[EDPB Guidelines 9/2022](https://www.edpb.europa.eu/system/files/2023-04/edpb_guidelines_202209_personal_data_breach_notification_v2.0_en.pdf)
II.A.2–4 supports awareness and processor escalation.

Functional responsibilities are scoped incident coordination, technical
containment/recovery, and privacy/legal assessment plus authorized communication.
These are tasks requiring explicit approved grants, not additional Entra roles or
permission inherited from founder, administrator or mailbox access. Before live
processing, bind responsible primary/backup coverage, secure contact, escalation
and pre-authorized emergency actions. No assignment is inferred now. Missing
coverage holds operational activation; it does not permit ignoring an actual alert
or delaying a legal obligation. The launch procedure must provide continuity
without inventing a support SLA or asking the founder to assign an owner again now.

### Parallel containment and private accountability

Contain, assess and preserve necessary evidence in parallel. Revoke affected
access or stop an unsafe operation under the approved incident authority; do not
use an emergency as permission for publication, broad exports or unrelated reads.
Recovery follows the existing publication fencing, provider reconciliation and
deletion/restore-suppression rules. Absence of confirmed data theft does not prove
safety; restoring a service cannot by itself close the incident assessment.

Use DE-21's restricted security/incident evidence subpurpose for safe action and
assessment references, not transcript, credential, database or email payloads in
ordinary audit logs. Preserve necessary forensic material separately only under
explicit scoped authority and the reviewed purpose/copy policy. A minimal case
records the affected scope, observed facts and uncertainty, evidence references,
timing with clock uncertainty, actual actors, assessment revisions, containment,
communication decisions/receipts and recovery validation. Keep corrections as
attributable amendments rather than silently rewriting earlier findings or clocks.
Hashes/references remain personal data when linkable. A specific preservation
decision needs necessity, basis, exact records and a finite review date; it cannot
renew every source record or exempt ordinary use from expiry. The
[record-purpose binding](DATA_CONTRACT.md#record-purpose-retention-binding-proposal--2026-10-08)
and proposed retention schedule remain controlling and unadopted.

### Applicable notification and communication decisions

Assess Hengshi's controller/processor role for the affected processing, actual
territorial scope and all competent recipients. Hosting location or an EU
representative does not establish a European office or one-stop-shop entitlement.
For a non-EEA controller subject to GDPR without an applicable establishment route,
identify each affected Member State's authority; do not select a single regulator
from a hosting region. See EDPB II.C.2, paragraph 73. Exact jurisdiction/contact
routes and applicable additional duties require legal qualification before live use.

Where GDPR applies, [Articles 33–34](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)
require distinct decisions. A processor informs its controller without undue
delay; it must not first wait for the controller's risk decision. A controller
notifies the competent authority without undue delay and, where feasible, within
72 elapsed hours of awareness, unless risk to individuals is unlikely. This is
not 72 business hours or permission to wait until the deadline. High-risk breaches
also require communication to affected people without undue delay. Document any
exception under Article 34(3) and the protective facts supporting it; encryption,
subsequent mitigation or notification effort are not automatic exemptions. Keep
the required equally effective public communication when the disproportionate
effort condition applies, and honor competent-authority directions.

The authorized assessment considers affected data/people, confidentiality,
integrity/availability impact and likely consequences, including vulnerable people,
misuse and mitigation. Brand/revenue impact is not the individual's risk threshold.
Record reasons for non-notification and reassess when material facts change. Do
not reset established awareness because a case changes owner, more victims are
identified or the first risk conclusion was incomplete. Records are required for
personal-data breaches even when authority notification is not required.

Initial authority notification supplies known nature/categories and approximate
counts where possible, a usable authorized contact, likely consequences, and
response/mitigation. Missing facts are identified and supplied in phases without
undue further delay; late notification includes reasons. Individual communication
uses clear language and useful protective advice with the required contact,
consequences and measures. Neither communication discloses other victims' details,
credentials or exploitable forensic material. A public notice needs its separately
authorized incident/legal route; ordinary content approval cannot postpone a
mandatory communication. No real communication is authorized by this definition.

Track intended recipient, approved content revision, attempted delivery, definitive
submission/delivery evidence and required follow-up separately. A draft, queued job
or timeout is not a sent notification. Reconcile an unknown result through the
qualified channel; do not report success or assume automatic retries are safe.
Notification and recovery stay separate outcomes with their own actual evidence.

### Acceptance and later rehearsal

[NIST SP 800-61 Rev. 3](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf),
April 2025, RS.MA/RS.AN/RS.CO/RS.MI and RC.RP, informs assessment, response,
communication and verified recovery; it does not certify Hengshi. The
[incident rehearsal definition](QA_RECOVERY.md#incident-response-rehearsal--v1)
and existing I/R/V/F recovery clocks define future evidence. Awareness is not the
recovery clock's I, and an RTO result cannot discharge notification obligations.
Reopening after new facts preserves prior evidence and applicable clocks.

Independent review is pending. Exact grants/coverage, lawful purpose/copy bindings,
jurisdiction/notification paths, secure evidence handling and qualified recovery
remain adoption inputs. Synthetic local rehearsals require their own approved
execution scope; no live data, report, incident fault, account or restore was used.

