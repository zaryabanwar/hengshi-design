## Qualification wire profile proposal — 2026-10-08

Status: DOING. This refines the preceding IF-BOOK-02 control proposal with the
[closed directional module](booking-qualification.schema.json). It preserves
the earlier reviewed catalogue prefix; that receipt covers its thirteen frozen
inputs, not these new bytes. It
retains the existing PATCH path, six required fields and separate noticed consent.
All new bounds/form representations are reversible, unmeasured engineering
proposals requiring independent review and integrated/founder acceptance. No
application, dependency, provider, proof policy or production form is implemented.

### Closed submission, timing and mailbox representation

Reference the module's `request` definition, never its rejecting root. Two closed
commands share the existing own-lineage PATCH boundary:

| Command | Exact client body | Permitted effect |
|---|---|---|
| `set_qualification` | `kind`, CSPRNG UUIDv4 `operation_id`, positive `expected_revision`, closed `qualification` and separate `consent`. | One guarded complete qualification set, subject to all current admission/correction gates. |
| `reconcile_qualification` | `kind` and the same scoped `operation_id` only. | Read the earlier admitted operation's permitted outcome; no new value set, consent, mutation, challenge, calendar action or renewal. |

Qualification contains exactly email, organization, role, desired_outcome,
wing_key and timing. The proposed timing representation is one closed object
with `description`: bounded free text expressing desired project timing, including
uncertainty. It adds no date bands, required deadline, slot instant, duration,
timezone, price or delivery commitment. Protocol metadata is not another question.
Optional budget remains absent until separately approved.

| Field | Proposed decoded Unicode-scalar limit |
|---|---:|
| email | 1–320; shape only, with the additional mailbox validation below |
| organization / role | 1–200 each |
| desired_outcome | 1–2,000 |
| timing.description | 1–500 |

Non-email text requires at least one code point outside Unicode 17's White_Space
property. Preserve entered text; do not silently truncate, transliterate, trim,
apply compatibility normalization or turn it into executable HTML/markdown.
These are code-point limits, not UTF-8 bytes, UTF-16 units or visible graphemes;
the raw body limit still wins, including escaped input. The shared raw admission
profile rejects invalid scalar sequences before schema validation. Any later
rendering uses the independently approved safe text/accessibility boundary.
`wing_key` reuses the existing five canonical keys, with current published
eligibility checked separately. The separate consent object reuses the noticed
decision shape but admits only `grant`; its purpose must be the approved current
booking purpose, not an arbitrary syntactically valid or chat-specific key.
Refusal is a no-personal-payload UI exit, not a second qualification command.
Exact notice, lawful basis, copy and purpose bindings remain required.

Recommend validating a plain mailbox through the existing email-validator family,
not a handwritten regex or Pydantic `EmailStr` alone. The observed installed and
registry stable version is 2.3.0, already in the backend candidate inventory; it
is not a selected complete production graph. Candidate options are explicitly
`check_deliverability=False`, `allow_display_name=False`,
`allow_quoted_local=False`, `allow_domain_literal=False`,
`allow_empty_local=False`, `allow_smtputf8=True`, `strict=True`,
`test_environment=False`. Reject surrounding whitespace rather than quietly
stripping it. No request-time DNS/SMTP lookup or mail dispatch follows. The
normal form is compared only inside this authorized lineage; preserve local-part
case and plus tags rather than applying provider-specific mailbox alias rules or
joining people/histories by email. Do not retain an extra raw spelling by default.
Binding an operation to its received typed values remains distinct from storing
the validated normalized mailbox.

Non-ASCII domains and local parts require separately verified delivery capability.
A syntax result's SMTPUTF8 indication is not an entitlement or deliverability
promise. Until the eventual adapter capability is verified, do not issue a
challenge that requires it, silently rewrite the mailbox, or invent an ASCII-only
customer policy. Capability refusal remains truthful Book/Contact recovery at
the email boundary. Exact adapter submission, supported forms and account/API
binding remain held; no mail provider is selected by this candidate profile.
The JSON Schema deliberately has no email-format assertion: a bounded non-address
can pass shape, so server mailbox validation is mandatory before application.

### Admission ordering, state mapping and same-intent recovery

After method/media/raw decoding, recognizable command-metadata and current
proof/CSRF/action gates, look for the
scoped admitted operation before treating an old expected revision as a fresh
write. For an existing operation, compare the complete received typed intent under
the permitted private binding: all six values, expected revision and consent
reference/decision. JSON property order/insignificant syntax whitespace does not
change typed meaning; changed scalar spellings do, even if mailbox normalization
would yield the same address. Matching replay reconciles only; changed meaning
conflicts without echoing or retaining rejected input. Current disclosure/purpose
denial can suppress a historical receipt. If its binding/outcome cannot be safely
established, return uncertainty, never apply a new command.

For a new set, check the current expected revision, valid normalized mailbox,
six-field validity, wing/notice/purpose eligibility and booking-intent fence.
Under the same atomic authority, apply the complete permitted set, minimal consent
evidence and dependent invalidations; advance lineage revision once for this new
guarded admission. Matching replay does not advance it. Exhaustion of the safe
integer revision range refuses before effects, never resets/reuses a revision.
This advance grants no new access, challenge validity or retention period.
Invalid input retains no lead/qualification payload or personal operation binding.

The proposed post-application mapping is evaluated from current authoritative
state under that fence, not from a browser's claimed state:

| Current conditions before a permitted new set | Resulting booking state |
|---|---|
| No still-applicable challenge/verified authority, including changed normalized email or invalidated purpose binding | QUALIFICATION_COMPLETE; all old challenge/verification and selection authority rejected. |
| Same normalized email and still-applicable challenge/purpose binding, no verified authority | Preserve the truthful current EMAIL_PENDING, EMAIL_EXPIRED or EMAIL_UNDELIVERABLE branch as applicable; no dispatch or freshness extension. |
| Same normalized email and still-valid current verified authority | VERIFIED; clear the old selection/review and stale no-availability result. Fresh availability/selection/review is required before booking. |
| Admitted or unresolved calendar/meeting mutation, confirmed occurrence or reschedule/cancel phase | Refuse replacement under the preceding booking-intent fence; preserve reconciled truth. |

Challenge/verification applicability includes exact email revision, purpose,
revocation and expiry. An expired challenge record can support an EMAIL_EXPIRED
display but never verification or slots. Unknown/inconsistent authority does not
fall through to a convenient successful branch: refuse and reconcile it. Exact
challenge/verification lifetimes and delivery mechanisms remain in IF-BOOK-03/04.
Previously dispatched email may still arrive; its old challenge remains invalid.
The field-set operation itself issues no challenge or calendar intent.

Reconciliation sends no qualification/consent again and allocates no operation.
An applied historical receipt says only which revision this operation applied;
IF-BOOK-07 separately reads current state. A newer revision, withdrawal or expiry
cannot be overwritten by replay. A missing row alone is not proof that an earlier
request never ran: a still-running/uncertain writer or lost binding may exist.
Without authoritative matching applied/pending knowledge, return safe unavailable
and retain uncertainty; do not reuse the operation ID for a fresh write or mint a
new lineage to evade it. Reconciliation/polling renews no idle/absolute access,
consent, challenge, retention or worker lease.

### Minimal results, errors and finite starting profile

Reference `response`; requests and responses are different closed shapes.
All application JSON is UTF-8, `application/json`, `Cache-Control: no-store`,
at most 1,024 emitted bytes, without credential CORS or input/exception echo.
Current own-object authority is checked before disclosing operation references,
applied revisions, field validation or conflicts. Unauthorized paths use one
ACCESS_UNAVAILABLE projection, without object-existence or earlier-validity detail.

| Outcome | HTTP | Closed meaning |
|---|---:|---|
| Applied or authorized matching replay | 200 | `state=applied`, own `operation_id`, historical `applied_revision`; no current-state or verification/booking assertion. |
| Known admitted operation whose application is unresolved | 202 | `state=pending`, own `operation_id`; no completed revision or absence-of-effect claim. |
| Authorized new set fails qualification/notice validation before application | 422 | `state=rejected`, INVALID_QUALIFICATION, `recovery=correct_request`, nonempty `errors` map containing only six field keys and/or consent, each with its closed fixed reason. No submitted value or operation echo. |
| Raw syntax, unknown command/properties or malformed protocol metadata | 400 | INVALID_REQUEST / correct_request. |
| Missing/expired/revoked/wrong-object proof | 404 | ACCESS_UNAVAILABLE / contact; do not distinguish existence. |
| Current object authority but action/CSRF denied | 403 | ACTION_DENIED / contact. |
| Current expected revision or booking state disallows new set | 409 | REVISION_CONFLICT or STATE_CONFLICT / refresh_status; no new mutation. |
| Existing operation has changed typed meaning | 409 | OPERATION_CONFLICT / reconcile. |
| Finite admission exhausted | 503 | CAPACITY_LIMIT / wait; does not deny earlier effects. |
| Outcome/store/binding unavailable or not provable | 503 | SERVICE_UNAVAILABLE / reconcile; preserve uncertainty. |
| Raw body/media/header refused | 413 / 415 / 431 | BODY_TOO_LARGE / UNSUPPORTED_MEDIA / HEADER_TOO_LARGE, each correct_request. |

Unavailable errors contain exactly `state=unavailable`, fixed code and recovery.
Rejected field feedback is available only for a fresh authorized set that has not
been admitted, not as a retrospective no-effect result for an uncertain operation.
For a recognizable new set, missing/invalid known qualification fields or consent
are mapped to the fixed 422 field feedback only after current object authority
and existing-operation checks. A schema failure by itself does not select 400;
unknown members/malformed protocol and known field-value failures have different
classifications. A changed existing intent conflicts instead of claiming that
its earlier application was rejected. Without current object authority, no field
feedback or private conflict detail is disclosed.
Reconcile returns only applied, pending or safe unavailable; never invented
validation feedback from discarded rejected payloads. HTTP correlations, this
command/result pairing and current authority are semantic checks beyond schema.
Localize fixed reasons in the approved UI, associating errors with fields/summary;
do not surface raw library messages. A transport termination/bodyless ingress
error is neither a successful JSON result nor proof that no earlier effect exists.

Use the existing same-origin HTTPS browser proof/CSRF and strict JSON admission
rules. Accept only application/json with absent or single UTF-8 charset and absent
or identity Content-Encoding; no form, alternate encoding, media defaults,
duplicate names, coercion, malformed Unicode or permissive credential origin.
Propose received-body caps of 16,384 bytes for set and 1,024 for reconcile, checked
across actual chunks, with the common lower nesting/string/node limits retained.
Before kind is known, the 16,384 maximum cannot be exceeded; after decoding the
stricter reconcile byte ceiling still applies. Headers/Cookie limits retain the
existing private profile's 16,384 aggregate / 8,192 Cookie-value bytes. Propose a
five-second receive deadline and ten-second observation deadline; observation
timeout never abandons admitted work or decides its outcome.

Propose service-wide limits of 48 admitted receive/set jobs and 16 receive/reconcile
jobs, counting draining/uncertain work until known cleanup, without a hidden queue.
Reserve no personal operation record before all admission/legal gates. At most
16 unsettled/replay-protection operation records per lineage and 4,096 across the
service may remain; at capacity refuse new set before effects, keeping permitted
reconciliation available. A retired operation must remain unable to apply again:
retain minimal necessary suppression until its proof/expected-revision scope can
no longer admit it. Store cleanup is not permission to forget ambiguity, reset a
revision or reexecute an old intent. Each binding/copy inherits its approved
purpose/expiry; hash representations are not automatically anonymous. Finite
mechanisms, ingress buffering, multiworker fencing, clock/cleanup integration and
actual load qualification remain required; these counts are not measured capacity.

### Primary evidence and limits

Checked 2026-10-08: Context7 `/pydantic/pydantic` and official
[Pydantic network types](https://pydantic.dev/docs/validation/latest/api/pydantic/networks/),
[email-validator documentation](https://github.com/JoshData/python-email-validator),
[PyPI metadata](https://pypi.org/pypi/email-validator/json),
[SMTPUTF8 RFC 6531](https://www.rfc-editor.org/rfc/rfc6531.html#section-3.2)
and [Unicode 17 White_Space data](https://www.unicode.org/Public/17.0.0/ucd/PropList.txt).
The [read-only native observations](../../../output/research/booking-qualification-wire-2026-10-08/email-observations.json)
preserve ten public-synthetic syntax/normalization cases with DNS delivery disabled,
installed source hashes, registry requirements and explicit options. This is neither
complete international address conformance nor actual API/provider enforcement.
No library install, runtime/lock change, outbound delivery or full graph selection.

Schema fixtures exercise only the module/validator boundary. They cannot prove
mailbox syntax, scalar-safe raw decoding, consent, atomicity, current state,
operation-result correlation, HTTP, provider or browser enforcement. Exact notice/
basis, adapter capability, allowed purpose/read projections, proven bindings/store/
fences/cleanup, wire freeze, load/accessibility/runtime and integrated/founder
acceptance remain. Earlier control/schema PASS scopes are not broadened by this
later profile; its own independent review and adoption are required.
