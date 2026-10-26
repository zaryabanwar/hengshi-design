
## Email ownership control proposal — 2026-10-08

Status: DOING. This completes the logical control profile for existing
IF-BOOK-03 (`POST /api/v1/bookings/lineages/{lineage_id}/email-challenges`)
and IF-BOOK-04 (`POST /api/v1/bookings/lineages/{lineage_id}/email-verification`).
It refines [BF-01B](../../phase-1-ux-architecture/FLOWS.md#bf-01b-email-ownership),
[booking data](DATA_CONTRACT.md#booking-and-provider-transactions) and the
[private-process boundary](PRIVATE_PROCESS_PROOF.md#scope-and-recommendation).
These are concrete engineering recommendations for integrated/founder acceptance,
not implemented controls or a new mail/account/provider entitlement. Earlier
receipts apply only to their preserved inputs. Wire schemas/HTTP envelopes remain
a subsequent representation task; this profile fixes their required semantics.

### Method and accessible interaction

Recommend a single-use, uniformly random eight-ASCII-digit confirmation code
sent to the currently qualified normalized mailbox. Use `secrets.randbelow(10**8)`
and zero-pad to eight digits; leading zeroes are significant. The code confirms
access to that mailbox for this booking lineage only. It creates no visitor
account, staff login, general identity assurance, process cookie, calendar access
or permission to inspect another lineage. In particular, email confirmation is
not Entra authentication or staff MFA. NIST's email-address confirmation distinction
supports this separation; it does not certify this design or select its limits.

Use one labeled text input, `inputmode=numeric`, `autocomplete=one-time-code`,
and an explicit Verify action. Permit whole-code paste and user-agent filling;
do not use eight independent boxes, numeric coercion, disabled paste, puzzles,
automatic submission or unaided memorization/transcription requirements. Email
plain text and HTML present the same contiguous eight digits, purpose, expiry
and a warning not to share the code. The email contains no qualification brief,
staff/personal identity, process proof, CSRF secret, tracking pixel or verification
URL. Copying a code must work with keyboard and assistive technology. Opening,
previewing or scanning email cannot perform verification.

Return to the existing authorized booking form; a new browser/device with only
the email code cannot recover or transfer the process. Reading email on a second
device and copying the code into the original process is allowed. Loss of the
original process uses its approved recovery/Contact boundary; do not disclose
historical data or mint a process proof from mailbox possession. Display no
masked address by default; authorized qualification review supplies the existing
permitted field under its own forthcoming projection, not this response.

The code's representation is exactly eight ASCII digits; whitespace, signs,
separators, Unicode lookalike digits and integer JSON values are invalid. UI may
explain the expected form but does not silently rewrite submitted secrets. Invalid
syntax is not a cryptographic comparison, although its bounded request/abuse
accounting still applies. Invalid, stale, exhausted, superseded and foreign
challenge submissions receive the same non-verifying recovery category after
current object authority; no code value, mailbox membership or remaining guess
count is returned. Access denial precedes these object-specific outcomes.

### Challenge identity, verifier and clocks

The server allocates a UUIDv4 challenge reference with CSPRNG bits and binds it to
the booking process, lineage, current email revision, applicable notice/purpose,
issue operation and code verifier. The reference is not a bearer credential.
Mutable lineage revision and email revision are distinct: a permitted non-email
qualification correction does not make the current code valid for another email
or silently extend its life. No client supplies those server bindings.

Recommend a 600-second code window from the atomic challenge admission, never
from mail acknowledgement or browser receipt. No provider claim resets it.
For timing accessibility, warn with at least 60 seconds remaining and provide
explicit More time with at least 20 seconds to act. Recommend up to ten extensions
of 600 seconds for the same still-valid challenge, without new mail, new code,
reset guesses or automatic continuation. Each extension checks current own proof,
CSRF, challenge/purpose/email bindings and extension count under the same fence.
Concurrent duplicates for the same operation extend once. No extension after
expiry, use, invalidation, withdrawal or loss of process authority; offer permitted
fresh issuance or Contact instead. This bounds the challenge to at most 6,600
seconds from original admission and supplies the ten-extension timing route;
it does not claim complete WCAG conformance. The exact More time representation
belongs to IF-BOOK-03, not a new endpoint or extra qualification question.

Recommend verified-email freshness of 1,800 seconds from successful consumption,
also bounded by current process/purpose/email authority. This is booking-action
freshness, separate from D-076's visitor conversation inactivity policy. It does
not impose an absolute conversation limit or silently renew any proof/consent.
When verification expires before booking-intent admission, do not expose or admit
new slots; invalidate old selection/review eligibility and offer verification
again. After a calendar/meeting intent is admitted, expiry cannot erase confirmed
truth, reexecute provider work or unlock qualification changes. Reschedule/cancel
have their separate authorization rules. Historical verification may remain only
as purpose-permitted evidence; it is not current slot eligibility.

Store a keyed HMAC-SHA-256 verifier rather than a plain/unkeyed short-code hash.
Recommend a separately managed 32-byte CSPRNG key, explicit key identifier, and
an unambiguous domain-separated length-prefixed message containing the action
family, process/lineage/challenge references, email revision and eight code bytes.
Compare equal-length digest bytes with `hmac.compare_digest`; ordinary equality
and fast offline enumeration of an unkeyed eight-digit hash are unsuitable.
The key stays outside the record store, source, snapshots, logs and public output.
Retain the appropriate key only through the governed active-verifier window;
an unavailable or revoked key denies verification, never bypasses it. Key creation,
storage, rotation/restore arrangements and credential changes require their later
applicable approvals. This recommendation does not change staff JWT/bcrypt.

Delivery needs the code transiently. Its encrypted, purpose-mapped outbox copy
uses separately managed encryption authority; HMAC is not reversible encryption.
Only the guarded delivery worker may decrypt for the approved adapter. No secret
is retained in diagnostics, analytics, operation fingerprints or browser storage.
Remove delivery secret material when its permitted need ends; retained delivery
evidence contains no code. Unknown delivery cannot justify indefinite plaintext
or an expired verifier; expiry and unresolved-effect evidence are separate clocks.
The provider's own copies and retention require MA-006/privacy assessment.

### Issuance, resend and uncertain delivery

IF-BOOK-03 has four closed logical commands: issue, explicitly resend, extend the
current challenge, and reconcile an already-admitted issue/resend/extension.
Mutating commands carry their own UUIDv4 operation identity and expected lineage
revision; reconciliation carries only the scoped earlier operation identity.
Resend/extend also identify the current server challenge. No client-supplied email,
code, delivery state, provider identity or verified flag is admitted here. The
mailbox comes from the current valid qualification. Reconciliation sends no code
or personal payload and creates no new operation, mail or renewal.

Current own-process proof, CSRF/action authority, valid complete qualification,
current applicable consent/purpose, supported mailbox delivery form and the atomic
revision/state guard are required before issuance. Refuse issue/resend once a
calendar/meeting intent is admitted; their uncertainty is not an email retry cue.
Current matching replay lookup precedes stale expected revision for fresh work:
the same immutable command returns its still-permitted historical outcome without
new code, mail, attempt counter or extension. Changed input under that operation
conflicts. Outcome/binding remains recoverable throughout its permitted window,
independent of the expected revision becoming stale after admission.

Atomically admit the new challenge, invalidate every earlier challenge/verifier
and dependent selection, reserve delivery/abuse budget, record its operation result
and durable delivery intent, and advance the lineage once to EMAIL_PENDING. Refusal
or known pre-commit failure does none of these. Dispatch only after commit. The
worker rechecks current purpose/email/challenge/expiry and exclusive dispatch
authority immediately before external admission. Stale queued work is suppressed;
already-dispatched or in-flight email cannot be recalled by invalidation.

Track delivery separately as queued, submission_pending, submitted, definitely_not_sent
or delivery_unknown. An adapter acceptance proves submission, not inbox arrival,
reader access or email verification. Enter definitely_not_sent only from authoritative
evidence excluding external submission; local timeout, lease expiry or missing
provider record alone do not establish it. Worker crash/ambiguous adapter response
retains delivery_unknown, fences duplicate dispatch and requires authoritative
adapter reconciliation before safe retry. Retry, where demonstrably safe, preserves
the original intent/code/expiry and does not allocate a challenge or reset a clock.
If the chosen adapter cannot reconcile an uncertain submission, that retry remains
unavailable with honest recovery; no claim of exactly-once external mail follows.

Explicit resend allocates a distinct current challenge/code only after the previous
same-mailbox delivery intent is terminal and applicable budgets permit it; it never
reuses or reactivates the old verifier. A terminal submission may still arrive late;
the old code remains invalid. Unknown old delivery is not definite failure and
cannot be bypassed with a new operation, tab, proof rotation or new lineage for the
same intent. A separately permitted address correction can proceed under IF-BOOK-02
while old delivery is unknown; it invalidates the old challenge but cannot claim
to cancel that email. Issuance to the corrected address is a new current-email
intent, not a retry of the uncertain old one; keep its independent evidence and
purpose/capacity guards. Do not let unknown obsolete delivery lock correction forever.

EMAIL_PENDING describes a pending challenge, never verified or a mail delivery
promise. EMAIL_UNDELIVERABLE requires a current definitely-not-sent refusal supported
by the adapter; EMAIL_EXPIRED requires actual current challenge expiry. Superseded
late callbacks cannot change the current challenge/state. Unknown submission can
coexist with expiry/invalidation; retain the necessary uncertainty evidence without
asserting that expired email was not sent. The public result gives only current
permitted challenge reference, expiry/extension affordance and a fixed safe state;
provider IDs, raw errors, code, verifier and address are absent.

### Verification admission and concurrent effects

IF-BOOK-04 has verify and reconcile logical variants. Verify carries operation ID,
expected lineage revision, challenge reference and the exact eight-digit code;
reconcile sends only the earlier scoped operation ID. Bind retry semantics to the
received typed values without persisting the code: use separately keyed intent
binding with length framing, never a raw/unkeyed code fingerprint. Bindings inherit
the operation's purpose/expiry and cannot form a mailbox/history index.

Before comparison, check current process/CSRF/action authority, operation replay,
current qualification/purpose/email binding, challenge validity and attempt budget.
Fresh verifies compare and consume under the same transaction/fence as correction,
withdrawal, resend, extensions and booking admission. A successful match consumes
the challenge once, records verification against the current email revision and
purpose/process, clears stale selection/review, records the immutable operation
result and advances lineage once to VERIFIED. It grants only current eligibility
for the separately guarded availability/selection stages, not a calendar booking.

Each fresh well-shaped comparison atomically reserves a guess; duplicates of the
same admitted operation do not compare or count again. Recommend at most five
comparisons per challenge, shared across tabs/workers. Five wrong comparisons
invalidate that challenge. The fifth correct comparison can succeed if its complete
authority remains current. A stale/wrong-reference request cannot decrement a
different challenge's counter. A competing success/replacement/end wins through
serialization; no second verification or stale-code promotion can be committed.

Lost acknowledgement is reconciled under current own authority. A matching old
success is a historical applied result, not assurance that verification is still
current; IF-BOOK-07 remains the current-status boundary. A wrong-code operation
has a recoverable fixed rejected outcome, without echoing code or remaining guesses.
If a current-authority reconciliation cannot prove the outcome, return pending or
unavailable and preserve ambiguity; never compare again from a missing receipt.
Read/reconcile/invalid code alone does not renew process access, purpose, verified
freshness or challenge expiry. Only separately eligible admitted activity may
affect the owning process's existing idle policy.

### Abuse, finite work and failure qualification

The eight-digit space has 100,000,000 possibilities (about 26.6 bits), so expiry
and per-challenge limits alone are insufficient. Propose a shared rolling budget
of five issue/resend admissions per process and normalized destination per hour,
and ten per destination per 24 hours, with at least 60 seconds between mail intents
for that destination. A new lineage/proof/email spelling cannot reset destination
budgets; reuse the reviewed mailbox normalization without provider alias guessing.
Track destination controls by a keyed, purpose-mapped digest, not public email
lookup or a permanent user profile. Their finite window/copy cleanup must be
approved under the abuse-purpose mapping before real data is stored.

Propose at most 25 fresh verification comparisons per process and normalized
destination per rolling hour, shared across replacement challenges/workers, plus
the five-comparison challenge cap. Reserve counters atomically before comparison/
send admission; rollback only a proven pre-effect cancellation, never ambiguous
work. More time and replay never reset these counters or create another mail intent.
Provider/limiter/key/clock/store uncertainty refuses new sensitive action; retain
permitted status/reconciliation and public Contact without guessing delivery or
verifying. Infrastructure-wide finite ingress/work limits from the existing private
profile also apply. Exact distributed store/key/expiry implementation is a later
engineering task, not a hidden in-memory counter or a selected Redis deployment.

These numerical budgets are unmeasured proposals, not a response SLA, defence
against all distributed abuse or NIST assurance-level claim. Network/service abuse
controls must complement them without storing browsing/movement histories or
permanently locking a customer mailbox. Capacity or retry guidance reveals no
membership, other-lineage state, provider internals or counter totals.

Later implementation qualification must exercise real transaction/worker boundaries:
simultaneous correct/wrong guesses; duplicate operations and changed code;
same-email qualification correction and changed-email invalidation; expiry at the
comparison/dispatch fence; More time versus expiry/use/End; 11th extension refusal;
new lineage/tab/worker limiter bypass; exactly one local consume and no duplicated
uncertain mail dispatch; known refusal versus ambiguous provider acknowledgement;
late obsolete email/callback; verification expiry before and after booking intent;
lost responses; withdrawal/deletion/restore; unavailable limiter/key/clock/store;
no secret leakage; full-code paste/autofill/leading-zero behavior, focus/errors,
timing warning/extension and screen-reader/mobile equivalence. Synthetic fixtures
are allowed locally; mocks or schema shape alone cannot prove these outcomes.

### Primary sources and acceptance boundary

Checked 2026-10-08: Context7 `/python/cpython`, official
[Python secrets](https://docs.python.org/3/library/secrets.html) and
[HMAC](https://docs.python.org/3/library/hmac.html) APIs; these support the standard
library primitives, not selection of a complete production Python graph.
[OWASP code/token guidance](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
informs randomness, secure storage, single use, expiry and abuse controls by analogy;
Hengshi's flow is email confirmation, not password recovery.
[NIST's email-confirmation distinction](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/)
separates this purpose from out-of-band authentication.
[W3C accessible authentication](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html)
and [timing adjustment](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html)
inform paste/filling and the explicit extension path; no unsupported essential-time
exception or blanket accessibility pass is asserted.

The eight-digit method, clocks, keyed verifiers, delivery state split and budgets
are this proposal's choices, not numerical prescriptions from those sources.
Independent control review and integrated/founder acceptance remain required.
Wire/HTTP representation, the authorized qualification-review projection, exact
purpose/notice/copy policy, MA-006 adapter/account capability, secret management,
distributed persistence and runtime/UI qualification remain tracked obligations.
No source/lock/provider/account/credential/deployment change is authorized here.
