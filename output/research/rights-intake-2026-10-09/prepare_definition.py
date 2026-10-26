"""Append the scoped rights-intake definition to two controlling documents."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
security_rel = "docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md"
catalogue_rel = "docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md"
before_dir = HERE / "before"
if before_dir.exists():
    raise SystemExit("Definition already prepared; preserve prior inputs")
before_dir.mkdir()

security = """

## Rights intake and verified response proposal — 2026-10-09

Status: DOING. This refines the existing rights-handling obligation and approved
privacy alias under D-070/D-076. The alias owner remains undecided; delivery,
restricted access and the operating procedure must be verified before publication
or live collection. No new visitor account, portal, role, table, upload facility
or endpoint is selected. Existing action/object grants and retention proposals
remain controlling. Earlier reviews do not cover this addition.

### Intake, receipt and restricted handling

Recommend the approved `privacy@hengshidesign.com` channel, linked from the
semantic privacy/Contact surfaces once verified. Recognized rights requests
received through another provided official channel are routed internally without
requiring a fresh submission or resetting their original receipt. Record the
earliest authoritative receipt instant, requested right and minimally necessary
scope/contact information. Receipt is independent of when staff open the message.
An acknowledgement confirms receipt without revealing whether particular personal
records exist. No request or attachment goes to public AI, analytics, generic
content storage or public release artifacts.

Handling requires explicit current privacy-operation authority and object scope;
an administrator, mailbox reader or requester-supplied name/email gains no broader
record access. Keep necessary case evidence restricted under its reviewed purpose
binding. Do not create a transcript archive, copy unrelated personal material or
automatically process unsolicited attachments. Safe receipt/decision metadata,
verification material and any response payload have separate authorized storage
and disposal bindings; an unknown mailbox/provider copy cannot be omitted.

### Proportionate verification and scoped execution

An active process proof can establish only its already authorized object/purpose.
It cannot become authority for all records or an unrelated privacy-request read.
For historical records, recommend a case-specific control confirmation through a
previously verified contact associated with the relevant record, plus the required
subject/object match and disclosure-risk assessment. Challenge generation, expiry,
one-time consumption and protected transport require qualification before use;
booking challenges cannot be reused as privacy grants. A typed email, matching
name, forwarded message, guessed identifier or expired bearer is insufficient.

Request additional identifying information only when necessary and proportionate
to reasonable doubts, using a reviewed secure procedure. No default government-ID
copy or new visitor registration. Changed contact, representative authority or an
ambiguous match requires restricted assessment, rather than disclosure to the new
address. Preserve a minimal verification conclusion, not unnecessary identity
documents or raw credentials. Where the system genuinely cannot identify a person,
explain that limitation and consider supplied identifying information without
reconstructing expired anonymous chat or collecting a new identity trail.

An authorized handler scopes the requested right against actual record/copy and
recipient inventories. Access output excludes other people's data and secrets;
review justified redactions without refusing all information automatically.
Correction, restriction, objection, erasure and applicable portability receive
their own assessed disposition. Email receipt alone triggers no destructive
operation. Approved deletion uses IF-PRIVACY-01/02 and DE-20; unknown provider or
restore suppression remains pending. An action and a rights response have distinct
outcomes: replying in time cannot falsely declare every copy deleted.

### Deadline, response and accountability

Maintain the original receipt and a calendar-month response deadline, with the
reviewed applicable calendar rules; never substitute thirty days or a staff-read
date. Respond without undue delay. An exceptional extension requires a recorded
reason and notice within the first month, and cannot exceed two further months.
Queues, absent ownership and provider uncertainty do not silently reset the clock.
EDPB access guidance recognizes limited verification/clarification suspension;
the proposed conservative operational default keeps the original deadline until
a competent reviewed decision records the applicable grounds and calculation.

Before delivery, recheck case/recipient authorization and response scope. Ordinary
email can acknowledge receipt, but personal-data delivery needs a reviewed secure
method appropriate to the risk, with the verified recipient bound to that case;
never attach an unrestricted database export. Give a concise response describing
the actual action, any justified limits and required complaint/remedy information.
Requests are normally free. No automatic fee or rejection for repetition, workload
or inability to provide an old process token; exceptional grounds need assessment.

Keep minimal outcome and deadline evidence under the existing proposed rights-case
accountability subpurpose. DE-20 continues to represent deletion/suppression only;
other rights are not silently added to its schema or exposed by its status route.
Exact case/storage/delivery bindings, operating grants, legal review and integrated
acceptance remain required. Later implementation must exercise wrong-recipient
disclosure, expired/forwarded/swapped proof, representative ambiguity, internal
forwarding delay, month-end deadlines, third-party redaction and unknown copies at
the actual intake/verification/store/delivery boundary with synthetic data.

Primary support checked 2026-10-09: [GDPR Articles 11, 12 and 15–21](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng),
[EDPB access guidance](https://www.edpb.europa.eu/documents/guideline/guidelines-012022-on-data-subject-rights-right-of-access_en)
sections 3.1–3.4, 5.3 and 6.2, and [Commission rights guidance](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/dealing-requests-individuals_en).
These sources inform the legal duties; the channel/control workflow above is an
unimplemented Hengshi recommendation. The [dated source captures](../../../output/research/rights-intake-2026-10-09/primary-sources.json)
preserve raw and compressed identities. Independent review of this addition is
pending; no legal clearance, mailbox verification or runtime assurance is claimed.
"""
catalogue = """

## Rights-channel and deletion-interface separation — 2026-10-09

Status: DOING. The [rights-intake proposal](SECURITY_PRIVACY_CONTRACT.md#rights-intake-and-verified-response-proposal--2026-10-09)
defines the existing privacy-channel workflow, receipt clock, proportionate
verification, assessed response and restricted case handling. Alias ownership and
operation remain deferred; no additional public route, account or staff grant is
created. Earlier catalogue reviews do not cover this reference addition.

IF-PRIVACY-01/02 remain deletion-request creation and the same authorized request's
minimal safe status. Receipt of another rights request does not admit it into
DE-20, expand that status projection, grant access to an email-matched record or
turn booking/process credentials into privacy credentials. Actual data delivery
and other rights need the assessed operating procedure and their reviewed exact
storage/delivery bindings; those are not fabricated as new API interfaces here.
Unknown deletion copies remain pending even after an authorized rights response.
The proposal needs independent/integrated acceptance; no adapter is implemented.
"""
for rel, addition in [(security_rel, security), (catalogue_rel, catalogue)]:
    path = ROOT / rel
    before = path.read_bytes()
    (before_dir / path.name).write_bytes(before)
    if addition.splitlines()[2].encode() in before:
        raise SystemExit("Heading already exists")
    path.write_bytes(before + addition.encode())

paths = ["AGENTS.md", ".specify/memory/constitution.md", "PROJECT.md", "DECISIONS.md",
         "PROJECT_STATE.yaml", "TASKS.md", "docs/software-definition/README.md",
         "docs/software-definition/06-entity-and-public-contact.md",
         security_rel, catalogue_rel,
         "docs/phase-1-architecture/contracts/DATA_CONTRACT.md",
         "docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md",
         "docs/phase-1-architecture/contracts/data-classification.csv",
         "docs/phase-1-architecture/contracts/data-entities.csv",
         "docs/phase-1-architecture/contracts/interface-catalog.csv",
         "docs/phase-1-architecture/contracts/process-fields.csv",
         "docs/phase-1-architecture/contracts/reviews/eu-privacy-retention-v1-2026-10-07.md",
         "docs/phase-1-architecture/contracts/reviews/record-purpose-binding-v1-2026-10-08.md",
         "specs/001-platform-security-hardening/spec.md"]
paths += [p.relative_to(ROOT).as_posix() for p in HERE.rglob("*") if p.is_file()]
packet = HERE / "review"
packet.mkdir()
inputs = []
for rel in dict.fromkeys(paths):
    raw = (ROOT / rel).read_bytes()
    target = packet / "inputs" / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(raw)
    inputs.append({"path": rel, "snapshot": target.relative_to(ROOT).as_posix(),
                   "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)})
manifest = packet / "review-inputs.json"
manifest.write_bytes((json.dumps({"status": "DOING", "revision_cycle": 0,
    "scope": "Proposed rights intake and deletion-route separation; exact two appends only",
    "inputs": inputs}, indent=2) + "\n").encode())
print(json.dumps({"inputs": len(inputs), "manifest_sha256": hashlib.sha256(manifest.read_bytes()).hexdigest()}))
