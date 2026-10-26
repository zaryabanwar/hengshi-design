# Company identity and public-contact reconciliation — v1

Status: DOING. Evidence date: 2026-10-04. This addendum supplies the facts missing
from foundation ECL-016/ECL-028 and SEO §2.1; it does not replace the accepted
foundation ledger, certify registration status or authorize publication.

## Founder-supplied facts

| Field | Exact supplied value | Evidence boundary |
|---|---|---|
| Public brand | Hengshi Design | Existing approved display name retained. |
| Legal company name | HENGSHI DESIGN (SMC-PRIVATE) LIMITED | Founder supplied in this chat on 2026-10-04; certificate not independently inspected. |
| Registration jurisdiction | Pakistan | Founder supplied; no overseas establishment inferred. |
| SECP CUIN | `0194040` | Preserve as a seven-character string, including the leading zero. |
| PSEB registration number | `Z-25-21131/26` | Preserve exactly; suffix does not establish an expiry date or current validity. |
| PSEB validity labels | Valid From: `Jul-2026`; Valid Till: `Jun-2027` | Founder transcribed the certificate text on 2026-10-04; month precision only, not independently authenticated. |
| Supplied registered address | A-87, Street no.6, Khokhar Town, Defence Road, Sialkot 51310, PB, Pakistan. | Founder supplied for disclosure review; no visitor-accessible office, opening hours or physical HQ claim inferred. |
| Public email | `info@hengshidesign.com` | Founder supplied in response to Contact/privacy/security inventory; ownership, monitored delivery and internal routing not tested. |
| Privacy contact | `privacy@hengshidesign.com` | Dedicated alias approved by founder under D-070; founder will create it; operation not verified. |
| Security contact | `security@hengshidesign.com` | Dedicated alias approved by founder under D-070; founder will create it; operation not verified. |

No additional operational privacy/security aliases, individual names,
incorporation date, NTN, phone, regulator endorsement or compliance certification
are inferred. The legal entity is the proposed website operator/controller;
its precise privacy role and notice obligations still need MA-002 review.

## Public display assessment

The recommendation is to classify the two company identifiers as public business
identity references, subject to evidence/publication review, rather than treat
them as passwords or account-access authority. SECP itself publishes company
CUINs in public company lists. Its incorporation-certificate form explicitly
identifies the CUIN as Corporate Unique Identification No. This supports public
identity use; it does not verify this company's number or impose a website rule.

For PSEB, the reviewed registration guidance explains number allotment and
renewal but contains no explicit instruction requiring confidentiality of the
registration number. Public display is a proposed business-disclosure choice,
not a verified blanket legal permission or mandatory website requirement.
The linked Registration Code of Conduct resolves to a login page; its terms
were not inspected. Confirm any certificate-specific restrictions before release.

Place verified identifiers in existing About/Trust legal details, with the legal
name in the approved footer/Contact/privacy disclosures. Do not invent a new route
or imply SECP/PSEB endorses the services, guarantees quality, or certifies security.
No regulator logo or badge rights are established by registration alone.

Candidate factual block, held for evidence/publication review:

> HENGSHI DESIGN (SMC-PRIVATE) LIMITED · Pakistan  
> SECP CUIN: 0194040  
> PSEB registration number: Z-25-21131/26  
> PSEB validity: July 2026–June 2027  
> Registered address: A-87, Street no.6, Khokhar Town, Defence Road, Sialkot 51310, PB, Pakistan.  
> Contact: info@hengshidesign.com

PSEB current-registration wording remains held until the supplied validity is verified.
Verify spelling/name-to-number correspondence against the incorporation record
and the current PSEB certificate or authoritative registry response. Retain
private evidence separately: do not publish CNIC/passport, bank statements,
signatures, account credentials or an unredacted application bundle.

## Editable company facts in staff administration

The founder explicitly requires editable registration/contact details rather than
constants embedded in frontend code. Treat the identity, identifiers, registered
address, contact facts and registration validity as typed versioned content under
the existing staff authoring/review/publication workflow. Staff admin is the editing
surface; an administrator role does not gain founder approval authority by editing.

An authorized author creates a new candidate revision with source/verification
references; changed values invalidate the relevant prior review. The same approved
release supplies footer, About/Trust/Contact/privacy disclosures, Organization
structured data, World panels and approved AI evidence. Never mutate an active
manifest or expose draft edits immediately. Display fields remain strings, including
the CUIN leading zero and PSEB punctuation. Validity stores explicit source precision:
`2026-07`/`2027-06` are month labels, not invented exact dates/timezone boundaries.
Automated current/expired claims require verified transition rules and dates;
missing/uncertain renewal evidence suppresses that claim without deleting identity.

Changes are auditable and reversible through a new eligible publication revision.
Regulator IDs never authorize an API request or unlock a provider account. This is
an amendment to definition/authoring requirements, not an admin feature implemented
in the protected prototype or an approved production screen.

## Contact and SEO integration

### Typed prepared-facts proposal

The [company-facts shape](../phase-1-architecture/contracts/company-facts.schema.json)
proposes one closed v1 content subdocument for prepared legal name, jurisdiction,
optional registered address, scheme-labelled registration values and purpose-labelled
contact facts. It is not an admin request, partial-edit format, public API response,
publication manifest or deployed validator. Unknown fields are rejected at every
object level; approval, activation, private staff identity, evidence/reviewer records
and provider credentials belong to their separately authorized records, not this
content value. Admin editing still needs the accepted revision/approval workflow.

CUIN and PSEB identifiers remain opaque strings; no numeric conversion, inferred
expiry from suffix, fixed regulator-specific identifier grammar or trimming is
introduced. Supplied month labels map to `from_month`/`through_month` with explicit
`precision: month`. These values are labels, not date-time instants: never invent
a first/last day, timezone or automatic current/expired status. If validity is
absent, treat it as unknown, not perpetual. Other source precision needs an explicitly
reviewed extension rather than silently rounding a certificate's exact dates.

Optional contact facts preserve separate Contact/privacy/security purposes. Their
strings do not establish valid email syntax, ownership, delivery or monitoring.
The schema neither creates an alias nor assigns its undecided owner. Optional
address/identifier data does not compel public disclosure. Every permitted field
still requires source verification and applicable disclosure/content review;
valid shape cannot publish the supplied address or an unverified registration.

Semantic preparation must preserve source text, reject blank-only values, verify
chronological month order and actual identifier/contact/address facts, resolve
approved field/record/transport bounds and safely encode visible output. Those
checks, provenance, applicable legal policies, permission enforcement and exact
publication projections remain inputs before production acceptance. The draft
deliberately does not invent a generic size limit or a regulator verification API.
Its schema checks are artifact evidence only; actual request, persistence,
revision invalidation and publication boundaries require later integration tests.

Context7 `/python-jsonschema/jsonschema` and primary
[JSON Schema object guidance](https://json-schema.org/understanding-json-schema/reference/object)
and [validator documentation](https://python-jsonschema.readthedocs.io/en/stable/validate/)
were checked 2026-10-04. Draft 2020-12 reuses the existing manifest dialect; no
library/runtime/production selection or dependency change is made. This new
proposal has [bounded independent review PASS after fixture correction 1](../phase-1-architecture/contracts/reviews/company-facts-shape-2026-10-04.md).
The [exact inspected proposal bytes](../../output/research/contract-review-reference-reconciliation-2026-10-04/entity-contact.pre-company-shape-review-reference.md)
are preserved; this later reference addition changes no field or authority rule.
The review covers only the typed section, schema and synthetic fixture, not
registration verification, disclosure, admin enforcement or runtime publication.
Integrated acceptance and the held semantic/resource policies remain required. The
[earlier contact document](../../output/research/contract-review-reference-reconciliation-2026-10-04/entity-contact.pre-typed-shape.md)
remains preserved; older contact reviews do not cover this new schema or section.

The general contact and approved dedicated aliases have distinct purposes. A privacy
request is a question/action concerning personal information, such as asking what
was retained or requesting correction/deletion; actual rights, verification and
legal response duties come from the reviewed applicable policy. A security report
describes suspected vulnerability, exposed data or another security issue; it is
not an ordinary sales request. Monitoring means a responsible person reads,
triages and follows up on each kind of message with restricted access.

The founder approved separate `privacy@hengshidesign.com` and
`security@hengshidesign.com` aliases from the start and will create them; `info@`
remains general Contact. This settles the contact direction without claiming
activation. Provider support, restricted access, responsible ownership and actual
delivery must be checked; no zero-cost entitlement or mailbox setup is inferred.
Before launch verify all advertised channels. Do not publish an unverified alias
as operational or route private reports into general enquiry views.
No response SLA, mailbox configuration, email-verification sender or calendar
provider is selected or claimed operational here.

Founder clarification, 2026-10-04: keep ownership of both dedicated aliases
undecided for now. This is an explicit held input, not an assignment to the founder
or general-contact team. Do not repeatedly request an owner during definition
work; resume that question when the founder supplies a role or channel activation
is being prepared. Until then, monitoring/triage and operational publication remain
unverified while unrelated definition work continues.

After facts and visible copy become eligible, Organization structured data may
use the verified legalName and visible contact facts consistently. Registration
identifiers must have explicit scheme labels; they are not tax IDs, locations,
certification awards or invented sameAs profiles. The canonical domain's control
gate MA-008 remains separate. The fictional World and Atlanta asset do not create
a geographic business-location claim.

D-070 establishes Europe as the first target market with broader global ambition.
Keep the founder-supplied Pakistan entity/address accurate; targeting Europe does
not create a European establishment. D-068 defers hosting provider/region/cost
selection and retains Outlook/Teams without a Microsoft 365 prerequisite. These
choices do not independently settle privacy-law applicability or API capability.

Remaining inputs are certificate/record correspondence, PSEB validity verification,
review of the supplied address disclosure, contact ownership/triage and the reviewed privacy
notice/retention basis. They hold only the affected public facts and operations;
they do not stop independent definition work. Commits and pushes remain deferred.

## Official evidence checked

- [SECP Companies Regulations 2024, updated through 25 July 2025](https://www.secp.gov.pk/wp-content/uploads/2026/04/Companies-Regulations-2024-updated-upto-25.07.2025-Reviewed-14042026.pdf), Annexure-C p.248: incorporation-certificate identity fields. This source supports terminology, not an exhaustive current legal-opinion claim.
- [SECP public company list by auditor](https://www.secp.gov.pk/document/list-of-companies-by-auditors-file-1-of-2/?wpdmdl=40504): company names and CUINs are publicly published. Historical list is evidence of disclosure practice, not Hengshi's current registration status.
- [PSEB company registration and renewal](https://techdestination.com/company-registration/): provisional-letter/renewal process, number allotment and application-document classes. The page's Code of Conduct link led to [portal login](https://portal.techdestination.com/auth/login), not readable public terms.
- [RFC 9116](https://www.rfc-editor.org/rfc/rfc9116.html) §1.1 describes security-reporting channels and the security@ convention. This supports the proposed role-address recommendation; it does not require a separate mailbox, create a response SLA or authorize security testing.

These are source observations and a scoped publication recommendation. Founder
facts, independent verification, legal review and publication acceptance remain
distinct evidence states.
