# First-file ordering proposal — independent review

Date: 2026-10-06. Status: DOING. Disposition: **REVISE**; one P2 finding.
This is proposal consistency review, not founder acceptance or execution approval.
Initial review; zero correction cycles consumed.

## Exact reviewed scope

Only the proposed contract changes at WS-P-01, §3.5 and §9.2, and the proposed
external-write-scope.csv WS-P-01 row were assessed. Canonical files were not applied.
Frozen packet: `output/research/b01-preflight-2026-10-06/bootstrap-proposal/review-inputs.json`.
Packet SHA-256: `f64714a162ef61175bf3115ddc1d5b25e08707fecdc1c37871ead3498aee3649`.
All 16 exact input identities/hashes are enumerated in that packet.
Contract before/canonical: `212452df66b90928c2e5da6cfcd08e8d4bcf59217b06747dd5058a114cb941f6`.
Contract proposed: `8eab48eb2ea5441a336107c08b88a184dd444a69c522d6bd442c5102dd9f1eb7`.
Scope before/canonical: `17bbf1451006a99786cdd624385661b3675f1c2beb8f293164110b3257facf01`.
Scope proposed: `7f100dbdd622a7d540d58dcd22b2aae14be4ee54a6966d8ebc2f8f2c045c76dc`.
Patch: `e6e4fbad2a92660f2239856eb9e3c2f64b7dd3648767025ad83dd86e81c99b9b`.
78-guard manifest: `f9031b37deccb3f11c3fcd55d55aece1aa36948c86a7083bbe3193aa8bc29268`.

## Finding

**P2 — retained absolute write gate conflicts with first-file exception.**
Proposed contract §11.1 item 6 (line 685) still says: “No write occurs until §3.5
capability enablement is completed and recorded.” New §3.5 deliberately creates
the empty file while file/archiving items remain unverified. The catch-all thus
requires completion of the checks that need the not-yet-created target.
Add an explicit carve-out for the separately approved empty first-file bootstrap;
keep completed capability evidence mandatory before every design/content write.
No expansion of the bootstrap or archive substitution is needed.

## Independently verified evidence and limits

Read the actual before/proposed copies, patch, controlling budget/ledger and gates.
Independent read-only diffs confirm exactly three contract hunks and one CSV row;
canonical contract/scope bytes match their before copies. All 16 input hashes and
78 protected guards match before and after receipt creation; packet hash unchanged.
Identity/plan precede a separately approved single empty file; returned-target
read-only inventory, private access and supported named-version/editable-archive
verification precede design writes. Uncertain creation requires reconciliation,
not duplicate creation. Existing project or explicitly approved Drafts is bounded;
project creation, sharing, seats and billing receive no implied authorization.
CB-04/06/07, conservative metering, monthly 20-call/zero-spend boundary, full coverage,
_PRE/_EXIT archives, design/accessibility reviews and later pilot/batch gates remain.
No provider calls, application changes, prose tests or broad validators were run.
This review proves no host/API/archive capability, private sharing or production UI.
The parent's later identity-call report and planned ledger append are outside these
frozen inputs and are not represented as reviewed execution evidence here.
Founder amendment acceptance, each immediate call approval and B01 release stay held.
