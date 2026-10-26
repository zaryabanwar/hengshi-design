## Qualification admission and correction proposal — 2026-10-08

Status: DOING. Definition-only refinement of existing IF-BOOK-02,
`PATCH /api/v1/bookings/lineages/{lineage_id}/qualification`, under accepted
[BF-01A/B](../../phase-1-ux-architecture/FLOWS.md#bf-01a-qualification), the
[booking data boundary](DATA_CONTRACT.md#booking-and-provider-transactions),
[private-process authority](PRIVATE_PROCESS_PROOF.md#scope-and-recommendation)
and [purpose bindings](DATA_CONTRACT.md#record-purpose-retention-binding-proposal--2026-10-08).
It changes no route, required visitor question, budget policy, provider or
application. This proposal needs its own independent review and integrated/founder
acceptance; earlier receipts do not cover these appended bytes.

### Direction and permitted effect

The visitor proposes exactly the existing six data fields: email, organization,
role/job title, desired outcome, one matched canonical wing, and desired timing.
One separate versioned booking-purpose consent record is the seventh element.
Operation identity and expected server revision are protocol metadata, not
additional questions or visitor identity. The path selects an already-created
lineage; neither it nor that metadata grants access. Do not admit caller-supplied
verification, challenge, selected slot, staff assignment, calendar/meeting identity,
server time, proof generation, retention period or completed booking state.
Optional budget stays absent until its representation and meaning are approved.

Recommend one closed qualification-set command carrying all six values and the
separate consent decision, rather than a generic property merge or sparse field
patch. It modifies only the qualification portion of the existing lineage. The
client displays already-permitted values for correction/confirmation under BF-01A;
it does not make the visitor retype unchanged fields. This recommendation does
not create a qualification-read endpoint or broaden IF-BOOK-07's minimal status
projection. Exact authorized review/read delivery still needs a directional
contract; status alone cannot supply fields that it intentionally omits.

Server admission requires current own-lineage proof and CSRF, a permitted action,
current expected revision/state, the raw/closed input boundary, six valid values,
an eligible published canonical wing and exact current applicable notice/purpose
evidence. A route suggestion is not confirmation, and a wing key is not permission
to assign any staff member. Email syntax does not establish ownership; desired
timing is not a meeting instant or delivery promise. No scoring, minimum budget,
marketing permission, AI use, name, phone, upload or visitor account is inferred.
Use the separate proof, raw JSON and current consent boundaries; this appendix
does not invent an email validator, normalization rule, legal basis or credential.

Declining before submission returns to browsing/ephemeral help without sending
the personal qualification payload. If refused, missing, stale or inapplicable
consent nevertheless arrives, it cannot authorize retention or challenge issuance.
Stopping new admission is not a deletion claim: disposing of earlier lawfully
admitted data follows its independently applicable purpose/withdrawal policy.

### Atomic changes and correction fence

Validate the whole command before applying any proposed personal value. Under
the authoritative transaction/fence, recheck object authority, operation meaning,
expected revision, qualification state, notice/purpose eligibility and conflicting
intent. Apply the accepted value set, minimal permitted consent evidence, revision
change and dependent invalidations together. No reader or worker can observe new
email with old email verification, new qualification with old slot eligibility,
or partially replaced fields. Authorization/withdrawal and booking-intent admission
must serialize with this fence; a prior HTTP check cannot win that race by itself.

An initially invalid submission creates no retained lead/brief, qualified value
set or email challenge. Do not persist its supplied values in request logs,
analytics, validation diagnostics, retry queues, audit payloads or operation
fingerprints. Any allowed control/error accounting is minimal, non-payload and
subject to its own finite store/retention profile. If an already-valid qualification
is corrected unsuccessfully, leave the earlier record unchanged only while its
original purpose remains permitted; failure cannot renew consent or retention.
Valid draft values can remain in the open form under its approved privacy boundary,
without silent browser PII persistence. The UX's VALIDATION_ERROR describes rejected
input; it must not erase a previously admitted qualification or provider truth.

Before external booking-intent admission, a valid correction may replace the
qualification under current revision/purpose guards. A changed email atomically
advances its server email revision, invalidates all earlier challenges and verified
email authority, and clears dependent slot selection/eligibility in this lineage.
Any older challenge result or queued dispatch must fail its current revision/purpose
guard; issuing a new challenge remains IF-BOOK-03, not an incidental PATCH effect.
The corrected qualification can be QUALIFICATION_COMPLETE, never VERIFIED merely
because its syntax is valid. Resend is not this correction action.

An unchanged email cannot be silently treated as a newly verified email. Existing
verification is usable only if its exact email revision and applicable purpose/
challenge bindings remain current; any required invalidation wins. Other accepted
qualification changes invalidate an old selection's qualification/review binding
even when the address is unchanged. Require fresh eligibility and visitor review
before a later booking intent; no renewed verification lifetime or automatic
replacement slot follows. The exact unchanged-email state mapping and current
challenge/verification lifetime remain inputs to the later closed state/schema
profile. Do not infer that retaining a verifier permits keeping SLOT_SELECTED.

Once a booking/provider intent is admitted or its outcome is unresolved, refuse
qualification replacement until that intent's current authority has established
that replacement is safe under its approved state policy. In particular, a
timeout, expired lease, RECONCILIATION_ERROR or missing provider read cannot unlock
correction. Neither confirmed bookings nor reschedule/cancel transitions are
rewritten by this endpoint. Their separately reviewed actions retain last confirmed
truth and the accepted lineage. No automatic cancellation, attendee change, second
meeting, new lineage or external retry is created by correcting this form.

### Replay, projection and visitor recovery

Scope operation identity to the authorized lineage and qualification action.
Bind it to the immutable admitted meaning, including the expected revision, all
six proposed values and applicable consent evidence. Changed meaning under the
same identity conflicts; a new identity cannot bypass the revision/intent fence.
The exact privacy-safe binding/store representation remains to be selected: a
plain hash of personal input is not automatically anonymous or retention-free.
Do not retain rejected personal input merely to implement duplicate detection.

For an already-admitted matching operation, reconcile the recorded outcome under
current object/disclosure authority before considering a fresh mutation. Its
original expected revision is not a fresh-write permission, and the revision
advanced by its own application is not a reason to apply it again. A receipt must
distinguish that earlier application from a current eligible qualification;
subsequent correction, withdrawal, expiry or booking progress can make its earlier
state inapplicable. Replay cannot restore earlier values, proof, consent, email
verification, slot eligibility or retention. If the binding/outcome is unavailable,
preserve uncertainty and deny a fresh mutation; do not claim no earlier effect.

The logical server result separates applied, rejected/conflicting, and unresolved
outcomes. An authorized applied receipt needs only the scoped operation reference
and applied revision; any current lineage state is a separately guarded snapshot,
not an assertion that the earlier revision remains current. No raw qualification,
email, consent text, bearer/CSRF, challenge, staff/provider detail or arbitrary
exception text is echoed. Safe validation feedback names only the allowlisted six
field keys or separate consent element and fixed reason categories, with no
submitted value. Object denial reveals no private existence or previous validity.
Exact JSON/status/error variants and finite response limits remain to be frozen;
do not borrow IF-BOOK-01/07's different projections as this route's complete schema.

A timeout, lost/malformed response or unresolved result means completion is unknown.
Keep the same initiating UI intent and reconcile it only under current authority.
IF-BOOK-07 can show permitted current lineage status; its state/revision alone cannot
prove which operation applied. Do not guess success from QUALIFICATION_COMPLETE,
repeat external work, overwrite a newer command, or allocate a replacement lineage.
The qualified intent itself sends no email and creates no calendar record. The
reviewed operation-result protocol must expose a safe same-intent reconciliation
mechanism at the existing boundary before implementation; this appendix adds no
new recovery endpoint. Until that contract exists, show honest uncertainty/Contact.

Preserve BF-01A's linked textual errors, associated labels and already-supplied
valid-value recovery. A permission/consent conflict is not an invitation to keep
retrying. Lost permitted form state needs truthful recovery rather than reconstructing
personal values from unauthorized logs or browser storage. Cross-stream changes
cannot bypass any admission or privacy gate.

### Primary support, validation scope and remaining wire definition

[RFC 5789 section 2](https://www.rfc-editor.org/rfc/rfc5789.html#section-2)
supports atomic application of PATCH changes and collision-aware admission; it
does not make PATCH inherently idempotent or select Hengshi's command format.
[RFC 9110 section 13.1.1](https://www.rfc-editor.org/rfc/rfc9110.html#section-13.1.1)
describes If-Match lost-update protection, but does not select it over an explicit
expected-revision command here. Do not claim that a numeric field implements HTTP
conditional semantics. These are primary references checked 2026-10-08, not a
new library/provider selection or implementation proof.

[JSON Schema 2020-12 validation](https://json-schema.org/draft/2020-12/json-schema-validation#section-7)
and the [jsonschema FAQ](https://python-jsonschema.readthedocs.io/en/stable/faq/#my-schema-specifies-format-validation-why-do-invalid-instances-seem-valid)
separate format assertion from annotation. Context7's `/python-jsonschema/jsonschema`
documentation was consulted: a declared email format alone supplies neither
asserted complete address validation nor mailbox ownership. No new dependency or
schema test is added for this prose/control definition.

Next wire-definition inputs are exact directional request/result/error schemas;
email internationalization/normalization and delivery capability; bounded Unicode
text and desired-timing representation; current notice/purpose mapping; unchanged-
email state transitions; operation admission/reconciliation/retention mechanisms;
and finite media, raw byte, receive/work, response, header and cleanup profiles.
The shared decoder's maxima are ceilings, not a complete route profile. Exact
review/read delivery, provider/challenge bindings, accessibility/load/runtime tests
and integrated/founder acceptance remain. Later tests must exercise actual request,
transaction, concurrent correction/verification/booking/withdrawal, denial and
recovery boundaries; documentation wording checks cannot prove those outcomes.
