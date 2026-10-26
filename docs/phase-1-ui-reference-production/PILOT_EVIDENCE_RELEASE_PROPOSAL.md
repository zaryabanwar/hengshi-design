# Proposed pilot-release evidence criterion

Status: **Accepted definition under D-059; corrected nonauthor review PASS.** Independent specification
author. D-059 authorizes validator implementation; no actual release is accepted.
Original proposal wording below is provenance superseded by D-059.

Authority: UI_REFERENCE_PRODUCTION_CONTRACT.md:255 requires explicit founder
pilot acceptance; lines 482–495 define individual batch validation/exit, and
lines 600–605 already require a frozen per-batch manifest and _EXIT archive.
No current structured record proves pilot acceptance. Conditional disposition,
complete evidence, validator PASS and review PASS do not independently grant it.

## Minimal durable signal

Propose one repository record: `validation/pilot-release.json`, created only
after explicit founder acceptance, never generated from evidence completeness.
Fields: `schema_version: 1`, `pilot_batch: B01`, `acceptance_decision` (unique
accepted founder decision ID), `released_batches` (exactly B02–B06 and B08),
`pilot_manifest_path`, `pilot_manifest_sha256`, `design_review_path`, `design_review_sha256`,
`accessibility_review_path`, `accessibility_review_sha256`, and the existing B01 _PRE/_EXIT archive references.
Paths are repository-relative; secrets and provider session URLs are forbidden.
The manifest is the immutable B01 batch manifest already required by the contract,
not the mutable aggregate index; subsequent batch evidence cannot invalidate it.

The decision must explicitly accept the referenced B01 exit and release those
conditional batches. Record insertion is an approval-recording action requiring
that founder decision; a matching hash or a generic approved decision is not enough.
Resolve the accepted decision, recorded artifact references, hashes and PASS independent review outcomes with zero CRITICAL/HIGH/MEDIUM findings
under the existing contract; LOW findings follow its carried-finding treatment. Missing signal means held; malformed, stale, forged
or contradictory signal is a validation failure, never implicit authorization.

## Caller behavior and coverage

Definition-only validation checks plans and reports undischargeable obligations;
it cannot certify a batch exit. Batch-exit validation must name its target batch.
Before pilot authorization: reject every execution/exit request; keep B01 held.
During an explicitly authorized B01 pilot: require all B01-owned obligations only;
do not require future B02–B08 or deferred B07/B09 coverage to exit B01.
After recorded founder pilot acceptance: conditional rows become eligible, not
automatically produced or accepted. Validate the named conditional batch's own
obligations and already contracted hard-prerequisite exits. Missing B02 evidence
fails B02 exit; unstarted B03 is not an unrelated B02 coverage failure.
B07/B09 remain ineligible under MA-025 in every context. Deferrals must resolve
to a batch that owns the relevant template/stream; they cannot waive B01 exit.

Negative cases: complete B01 without founder acceptance must not release B02;
unrelated accepted decision, wrong manifest hash or absent review/archive fails;
released batch IDs containing B07/B09 fail; missing executable B02 evidence fails;
complete B02 plus valid prerequisite exit is unaffected by held B07/B09; unknown
target and unmet hard prerequisite fail. After founder approval of this proposed record and validation-mode amendment,
implement and independently verify all negative cases before accepting any exit.
