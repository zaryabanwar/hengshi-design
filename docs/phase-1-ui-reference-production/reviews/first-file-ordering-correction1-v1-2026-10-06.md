# First-file ordering correction 1 — independent review

Date: 2026-10-06. Status: DOING. Disposition: **PASS within the proposed scope**.
Supersedes only the P2 disposition in [the initial review](first-file-ordering-proposal-v1-2026-10-06.md).
One correction cycle consumed; no remaining findings in this bounded proposal.

## Exact reviewed inputs

Packet: `output/research/b01-preflight-2026-10-06/bootstrap-proposal/correction-1/review-inputs.json`.
SHA-256: `2f26919f2face71a5add3604d885e48836da3438551b4b7f1e3f07c27eef8462`.
All 23 exact input identities/hashes are enumerated there, including frozen copies
of the original 16 inputs with their `original_path` identities.
Original packet: `f64714a162ef61175bf3115ddc1d5b25e08707fecdc1c37871ead3498aee3649`.
Original receipt: `c1d51eaedff5d54e8f11f8b68a4745c801cbbf7d90ba813544d91c9460a58c3d`.
Corrected proposed contract: `1779fd3cd71f8210815fd7ddbbcd06faa6e5387e2d91584531be6d3806f8cf61`.
Unchanged proposed scope CSV: `7f100dbdd622a7d540d58dcd22b2aae14be4ee54a6966d8ebc2f8f2c045c76dc`.
Corrected patch: `bb6c0055bbb01e3c25a5b6a1a49cc1201848b44b7b91441621c1310c99715aa6`.
78-guard manifest: `f9031b37deccb3f11c3fcd55d55aece1aa36948c86a7083bbe3193aa8bc29268`.

## P2 closure and preservation

Independent before/correction diff confirms the only additional proposal change
is §11.1 item 6: its complete-capability gate now applies to design/content writes,
with an explicit separately founder-approved empty-file exception under §3.5.
The exception permits creation before file/archiving verification while preserving
private inventory and _PRE gates; it grants no pilot execution or design writes.
This removes the prior circular requirement without enlarging the file scope.
The total proposed two-document amendment remains the original three contract
hunks and WS-P-01 CSV row, plus this single acceptance-clause correction.
Identity/plan, separate single-file approval, immediate read-only target approval,
privacy and named-version/full-editable-archive verification remain sequential.
Uncertain creation still requires reconciliation; no automatic duplicate creation.
No project creation, sharing, seat, billing or later-batch permission is inferred.
Monthly zero-spend/call budget, CB-04/06/07, full coverage, _PRE/_EXIT archives,
independent design/accessibility reviews and B01/later batch gates remain intact.

## Verification and held limits

All 23 frozen hashes and 78 protected guards match before and after this receipt.
The original 16 snapshots preserve their original hashes; initial receipt is intact.
Canonical contract and scope remain equal to their reviewed before copies, unapplied.
Current mutable ledger/capability updates are outside this review; their current
bytes are not asserted to match the older frozen snapshots.
No provider calls, canonical patch application, tests or broad validators were run.
This is coherent proposal ordering, not proof of host/API/privacy/archive capability,
production design, accessibility, pilot readiness or implemented authentication.
Founder amendment acceptance and each operation approval remain required; prior
targetless get_metadata approval provides no substituted identity or creation permission.
